"""Data layer with graceful degradation.

Priority per series: live provider (Stooq → Yahoo → FRED) → local CSV cache →
deterministic synthetic data. Every DataFrame returned carries
``df.attrs["source"]`` in {"live", "cache", "synthetic"} so downstream reports
can label results honestly (synthetic → DEMO banner).

Network access is often blocked in agent sandboxes; every fetch fails fast
(short timeout) and falls through silently to the next tier.
"""

from __future__ import annotations

import io
import logging
import time
from datetime import date

import pandas as pd
import requests

from ..config import CACHE_DIR, UNIVERSE, Series, Settings
from . import synthetic

log = logging.getLogger("goldstein.data")

_TIMEOUT = 15
_HEADERS = {"User-Agent": "Mozilla/5.0 (goldstein-quant)"}


# ----------------------------------------------------------------- providers
def _fetch_stooq(symbol: str) -> pd.DataFrame | None:
    url = f"https://stooq.com/q/d/l/?s={symbol}&i=d"
    r = requests.get(url, timeout=_TIMEOUT, headers=_HEADERS)
    r.raise_for_status()
    df = pd.read_csv(io.StringIO(r.text))
    if "Close" not in df.columns or df.empty:
        return None
    df.columns = [c.lower() for c in df.columns]
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date").sort_index()
    if "volume" not in df.columns:
        df["volume"] = 0.0
    return df[["open", "high", "low", "close", "volume"]].astype(float)


def _fetch_yahoo(symbol: str) -> pd.DataFrame | None:
    # explicit period1/period2: `range=max&interval=1d` silently degrades to
    # monthly bars on long histories, which poisons every vol estimate
    p1 = 631152000                      # 1990-01-01
    p2 = int(time.time()) + 86400
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        f"?period1={p1}&period2={p2}&interval=1d&events=div%2Csplit"
    )
    r = requests.get(url, timeout=_TIMEOUT, headers=_HEADERS)
    r.raise_for_status()
    result = r.json()["chart"]["result"][0]
    if result.get("meta", {}).get("dataGranularity", "1d") != "1d":
        return None
    quote = result["indicators"]["quote"][0]
    idx = pd.to_datetime(result["timestamp"], unit="s").normalize()
    df = pd.DataFrame(
        {k: quote[k] for k in ("open", "high", "low", "close", "volume")}, index=idx
    ).dropna(subset=["close"])
    df = df[~df.index.duplicated(keep="last")]
    df.index.name = "date"
    return df.astype(float) if not df.empty else None


def _fetch_yahoo_macro(symbol: str) -> pd.DataFrame | None:
    """Macro fallback: a Yahoo index quote's close becomes the series value
    (e.g. ^VIX, ^TNX ~ 10y yield in %, ^IRX ~ 3m bill in %)."""
    df = _fetch_yahoo(symbol)
    if df is None:
        return None
    return df[["close"]].rename(columns={"close": "value"})


def _is_daily(df: pd.DataFrame) -> bool:
    """Reject silently-degraded (weekly/monthly) series: median gap between
    consecutive observations must look like business-daily."""
    if len(df) < 100:
        return False
    gaps = df.index.to_series().diff().dt.days.dropna()
    return float(gaps.median()) <= 4.0


def _fetch_fred(series_id: str) -> pd.DataFrame | None:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    r = requests.get(url, timeout=_TIMEOUT, headers=_HEADERS)
    r.raise_for_status()
    df = pd.read_csv(io.StringIO(r.text), na_values=".")
    df.columns = ["date", "value"]
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date").dropna().sort_index()
    return df.astype(float) if not df.empty else None


def _fetch_live(spec: Series) -> pd.DataFrame | None:
    attempts = []
    if spec.kind == "price":
        # yahoo first: stooq rate-limits shared datacenter IPs (CI runners)
        if spec.yahoo:
            attempts.append(("yahoo", lambda: _fetch_yahoo(spec.yahoo)))
        if spec.stooq:
            attempts.append(("stooq", lambda: _fetch_stooq(spec.stooq)))
    else:
        if spec.fred:
            attempts.append(("fred", lambda: _fetch_fred(spec.fred)))
        if spec.yahoo:
            attempts.append(("yahoo", lambda: _fetch_yahoo_macro(spec.yahoo)))
    for name, fn in attempts:
        try:
            df = fn()
            if df is not None and _is_daily(df):
                log.info("fetched %s from %s (%d rows, last %s)",
                         spec.key, name, len(df), df.index[-1].date())
                df.attrs["provider"] = name
                return df
            if df is not None:
                log.info("rejected %s from %s: not business-daily (%d rows)",
                         spec.key, name, len(df))
        except Exception as exc:  # network blocked / provider down: fall through
            log.info("provider %s failed for %s: %s", name, spec.key, exc)
    return None


# --------------------------------------------------------------------- cache
def _cache_path(key: str):
    return CACHE_DIR / f"{key}.csv"


def _read_cache(key: str) -> pd.DataFrame | None:
    p = _cache_path(key)
    if not p.exists():
        return None
    df = pd.read_csv(p, parse_dates=["date"], index_col="date")
    return df if not df.empty else None


def _write_cache(key: str, df: pd.DataFrame) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(_cache_path(key))


# ----------------------------------------------------------------- interface
def load_series(key: str, settings: Settings | None = None,
                allow_synthetic: bool = True, refresh: bool = False) -> pd.DataFrame:
    """Load one canonical series with the live → cache → synthetic ladder."""
    settings = settings or Settings()
    spec = UNIVERSE[key]

    cached = _read_cache(key)
    if cached is not None and spec.kind == "price" and not _is_daily(cached):
        cached = None                    # poisoned cache (e.g. monthly bars)
    stale = cached is None or (
        date.today() - cached.index[-1].date()
    ).days > 3
    if refresh or stale:
        live = _fetch_live(spec)
        if live is not None:
            _write_cache(key, live)
            live.attrs["source"] = "live"
            return live
    if cached is not None:
        cached.attrs["source"] = "cache"
        return cached
    if not allow_synthetic:
        raise FileNotFoundError(
            f"No live or cached data for {key}; re-run with network access "
            f"or drop a CSV at {_cache_path(key)}"
        )
    df = (
        synthetic.synthetic_price(key, settings.lookback_years, settings.seed)
        if spec.kind == "price"
        else synthetic.synthetic_macro(key, settings.lookback_years, settings.seed)
    )
    df.attrs["source"] = "synthetic"
    return df


def fetch_all(settings: Settings | None = None, refresh: bool = True) -> dict[str, str]:
    """Try to refresh every series in the universe; return {key: source}."""
    out = {}
    for key in UNIVERSE:
        df = load_series(key, settings, refresh=refresh)
        out[key] = df.attrs["source"]
    return out


def data_status() -> pd.DataFrame:
    """Cache freshness table for `goldstein doctor` and reports."""
    rows = []
    for key, spec in UNIVERSE.items():
        cached = _read_cache(key)
        rows.append(
            {
                "series": key,
                "kind": spec.kind,
                "cached_rows": 0 if cached is None else len(cached),
                "last_date": None if cached is None else cached.index[-1].date(),
                "description": spec.description,
            }
        )
    return pd.DataFrame(rows).set_index("series")
