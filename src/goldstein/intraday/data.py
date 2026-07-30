"""Intraday data: Yahoo chart API (5m/15m/60m), CSV cache, synthetic fallback.

Yahoo limits: 1m → last 7 days, 5m/15m → last 60 days, 60m → last 730 days.
The daily automation appends fresh bars to the cache so history accumulates
beyond Yahoo's lookback window over time (dedup on timestamp).

All timestamps are UTC. Sessions (approximate, DST ignored):
  asia 00-07, london 07-12, overlap 12-16 (London PM + NY AM = the liquid
  high-vol window), ny 16-21, late 21-24.
"""

from __future__ import annotations

import logging
import time
import zlib

import numpy as np
import pandas as pd
import requests

from ..config import CACHE_DIR

log = logging.getLogger("goldstein.intraday")

_TIMEOUT = 20
_HEADERS = {"User-Agent": "Mozilla/5.0 (goldstein-quant)"}
_RANGE = {"1m": "7d", "5m": "60d", "15m": "60d", "60m": "730d"}

SESSIONS = [
    ("asia", 0, 7),
    ("london", 7, 12),
    ("overlap", 12, 16),
    ("ny", 16, 21),
    ("late", 21, 24),
]


def session_of(index: pd.DatetimeIndex) -> pd.Series:
    hours = index.hour
    out = np.full(len(index), "late", dtype=object)
    for name, h0, h1 in SESSIONS:
        out[(hours >= h0) & (hours < h1)] = name
    return pd.Series(out, index=index, name="session")


def _cache_path(symbol_key: str, interval: str):
    return CACHE_DIR / "intraday" / f"{symbol_key}_{interval}.csv"


def fetch_yahoo_intraday(symbol: str, interval: str = "5m") -> pd.DataFrame | None:
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        f"?range={_RANGE[interval]}&interval={interval}"
    )
    r = requests.get(url, timeout=_TIMEOUT, headers=_HEADERS)
    r.raise_for_status()
    result = r.json()["chart"]["result"][0]
    quote = result["indicators"]["quote"][0]
    idx = pd.to_datetime(result["timestamp"], unit="s", utc=True)
    df = pd.DataFrame(
        {k: quote[k] for k in ("open", "high", "low", "close", "volume")}, index=idx
    ).dropna(subset=["close"])
    df = df[~df.index.duplicated(keep="last")]
    df.index.name = "datetime"
    return df.astype(float) if len(df) > 200 else None


def load_intraday(symbol_key: str = "XAUUSD", yahoo_symbol: str = "GC=F",
                  interval: str = "5m", refresh: bool = False,
                  allow_synthetic: bool = True, seed: int = 42) -> pd.DataFrame:
    """live-append → cache → synthetic ladder for intraday bars."""
    path = _cache_path(symbol_key, interval)
    cached = None
    if path.exists():
        cached = pd.read_csv(path, parse_dates=["datetime"], index_col="datetime")
        cached.index = pd.DatetimeIndex(cached.index, tz="UTC")

    if refresh or cached is None:
        try:
            live = fetch_yahoo_intraday(yahoo_symbol, interval)
        except Exception as exc:
            log.info("intraday fetch failed for %s %s: %s", symbol_key, interval, exc)
            live = None
        if live is not None:
            merged = (pd.concat([cached, live]) if cached is not None else live)
            merged = merged[~merged.index.duplicated(keep="last")].sort_index()
            path.parent.mkdir(parents=True, exist_ok=True)
            merged.to_csv(path)
            merged.attrs["source"] = "live"
            log.info("intraday %s %s: %d bars (last %s)", symbol_key, interval,
                     len(merged), merged.index[-1])
            return merged

    if cached is not None and len(cached) > 200:
        cached.attrs["source"] = "cache"
        return cached
    if not allow_synthetic:
        raise FileNotFoundError(f"no intraday data for {symbol_key} {interval}")
    df = synthetic_intraday(days=60, interval=interval, seed=seed)
    df.attrs["source"] = "synthetic"
    return df


# ------------------------------------------------------------------ synthetic
_SESSION_VOL = {"asia": 0.6, "london": 1.1, "overlap": 1.6, "ny": 1.2, "late": 0.5}


def synthetic_intraday(days: int = 60, interval: str = "5m",
                       seed: int = 42, start_price: float = 4000.0) -> pd.DataFrame:
    """Deterministic 24h intraday series with realistic session vol profile,
    vol clustering and occasional bursts — offline demo & tests only."""
    step_min = {"1m": 1, "5m": 5, "15m": 15, "60m": 60}[interval]
    bars_per_day = (24 * 60) // step_min
    rng = np.random.default_rng(seed + zlib.crc32(interval.encode()) % 1000)

    end = pd.Timestamp.now("UTC").floor("D")
    idx = pd.date_range(end - pd.Timedelta(days=days), end,
                        freq=f"{step_min}min", tz="UTC", inclusive="left")
    idx = idx[idx.dayofweek < 5]
    n = len(idx)

    base_vol = 0.145 / np.sqrt(252 * bars_per_day)      # ~14.5% annualized
    sess_mult = session_of(idx).map(_SESSION_VOL).values
    cluster = np.zeros(n)
    for t in range(1, n):
        cluster[t] = 0.995 * cluster[t - 1] + 0.08 * rng.standard_normal()
    burst = (rng.random(n) < 0.002) * rng.exponential(3.0, n)
    vol = base_vol * sess_mult * np.exp(cluster - cluster.var() / 2) * (1 + burst)
    shocks = rng.standard_t(df=4, size=n) / np.sqrt(2.0)
    rets = vol * shocks
    close = start_price * np.exp(np.cumsum(rets))
    wick = np.abs(rng.standard_normal(n)) * vol * close * 0.7
    open_ = np.concatenate([[start_price], close[:-1]])
    df = pd.DataFrame(
        {
            "open": open_,
            "high": np.maximum(open_, close) + wick,
            "low": np.minimum(open_, close) - wick,
            "close": close,
            "volume": (rng.integers(200, 3000, n) * sess_mult).astype(float),
        },
        index=idx,
    )
    df.index.name = "datetime"
    return df
