"""Century-scale gold price history (1920 → today) and long-run analytics.

Builds ``data/cache/XAUUSD_CENTURY.csv``: monthly closes for the fixed-price
era, daily from 1968, spliced with the modern XAUUSD cache. Every row carries
a ``source`` label so downstream analysis can state exactly where each number
comes from. Also maintains ``data/cache/CPIAUCNS.csv`` (US CPI, monthly,
1913→) so returns can be reported in real terms — over a century the nominal
series alone is misleading.

Era ladder (documented; a real observation always beats a peg constant):

1920-1949   NBER macrohistory M04051USM324NNBR via FRED (monthly price of
            gold, New York) when reachable; otherwise the official U.S.
            price: $20.67/oz until 1934-01, $35.00/oz from 1934-02 (Gold
            Reserve Act). Caveat: during 1933 the market price floated above
            the old parity; the official series understates that interlude.
1950-1967   $35.00 Bretton Woods peg (the London fix stayed within pennies
            of the peg until the 1968 two-tier split).
1968-       LBMA PM fix, daily, via FRED GOLDPMGBD228NLBM (AM fix fallback).
            FRED's LBMA license ended in 2022 but the full 1968-2022 history
            remains downloadable.
bridge      the modern XAUUSD cache (Stooq/Yahoo) for dates after the last
            LBMA observation.

Offline-first: the peg segment is generated deterministically with no
network, and cached segments are reused, so `goldstein century` always works
offline once the cache has been committed. There is NO synthetic fallback
here — a made-up century would be worse than an honest gap.
"""

from __future__ import annotations

import io
import logging
import time

import numpy as np
import pandas as pd
import requests

from ..config import CACHE_DIR, TRADING_DAYS
from .providers import _HEADERS, _fetch_stooq, _read_cache, _write_cache

log = logging.getLogger("goldstein.data.history")

CENTURY_KEY = "XAUUSD_CENTURY"
CPI_KEY = "CPIAUCNS"
CENTURY_START = "1920-01-31"
REVALUATION = "1934-01-31"          # last month at $20.67; $35 from 1934-02
LBMA_SERIES = ("GOLDPMGBD228NLBM", "GOLDAMGBD228NLBM")
NBER_SERIES = "M04051USM324NNBR"


DATAHUB_GOLD = "https://raw.githubusercontent.com/datasets/gold-prices/main/data/monthly.csv"
DATAHUB_CPI = "https://raw.githubusercontent.com/datasets/cpi-us/main/data/cpiai.csv"


def _fred_csv(series_id: str, timeout: int = 90, tries: int = 3) -> pd.DataFrame | None:
    """fredgraph.csv with a patient timeout and retries: half-century daily
    series routinely take >15s to render server-side, which is why the
    fail-fast fetcher in providers.py is not reused here."""
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    for attempt in range(tries):
        try:
            r = requests.get(url, timeout=timeout, headers=_HEADERS)
            r.raise_for_status()
            df = pd.read_csv(io.StringIO(r.text), na_values=".")
            df.columns = ["date", "value"]
            df["date"] = pd.to_datetime(df["date"])
            df = df.set_index("date").dropna().sort_index()
            if not df.empty:
                return df.astype(float)
        except Exception as exc:
            log.info("FRED %s attempt %d failed: %s", series_id, attempt + 1, exc)
            time.sleep(5 * (attempt + 1))
    return None


def _fetch_csv(url: str) -> pd.DataFrame | None:
    try:
        r = requests.get(url, timeout=60, headers=_HEADERS)
        r.raise_for_status()
        return pd.read_csv(io.StringIO(r.text))
    except Exception as exc:
        log.info("fetch %s failed: %s", url, exc)
        return None


# ------------------------------------------------------------------ segments
def official_peg_monthly() -> pd.DataFrame:
    """Deterministic official-price segment, 1920-01 → 1967-12, month-end."""
    idx = pd.date_range(CENTURY_START, "1967-12-31", freq="ME")
    close = np.where(idx <= pd.Timestamp(REVALUATION), 20.67, 35.00)
    return pd.DataFrame({"close": close, "source": "official_peg"}, index=idx)


def _fetch_nber_monthly() -> pd.DataFrame | None:
    """NBER macrohistory monthly gold price (New York), through 1949."""
    df = _fred_csv(NBER_SERIES)
    if df is None:
        return None
    df = df[(df.index >= CENTURY_START) & (df["value"] > 5) & (df["value"] < 60)]
    if df.empty:
        return None
    out = df.rename(columns={"value": "close"})
    out.index = out.index + pd.offsets.MonthEnd(0)
    out["source"] = "nber_m04051"
    return out[["close", "source"]]


def _fetch_lbma_daily() -> pd.DataFrame | None:
    """Post-1968 reference era, best source first:
    LBMA fix daily (FRED) → Stooq XAUUSD full daily → datahub monthly."""
    for series in LBMA_SERIES:
        df = _fred_csv(series)
        if df is not None and len(df) > 1000:
            out = df.rename(columns={"value": "close"})
            out["source"] = f"lbma_{series[4:6].lower()}_fix"
            return out[["close", "source"]]
    try:
        stooq = _fetch_stooq("xauusd")
    except Exception as exc:
        log.info("stooq xauusd failed: %s", exc)
        stooq = None
    if stooq is not None and stooq.index[0] < pd.Timestamp("1990-01-01"):
        out = stooq[["close"]].copy()
        out["source"] = "stooq_xauusd"
        return out
    raw = _fetch_csv(DATAHUB_GOLD)
    if raw is not None and {"Date", "Price"} <= set(raw.columns):
        out = pd.DataFrame(
            {"close": raw["Price"].astype(float).values, "source": "datahub_monthly"},
            index=pd.to_datetime(raw["Date"]) + pd.offsets.MonthEnd(0),
        )
        out = out[out.index >= "1968-01-01"]
        if len(out) > 300:
            return out
    return None


def _modern_segment() -> pd.DataFrame | None:
    """Daily closes from the platform's own XAUUSD cache (Stooq/Yahoo)."""
    df = _read_cache("XAUUSD")
    if df is None or "close" not in df.columns:
        return None
    out = df[["close"]].copy()
    out["source"] = "xauusd_cache"
    return out


# -------------------------------------------------------------------- splice
def splice(segments: list[pd.DataFrame]) -> pd.DataFrame:
    """Concatenate era segments; on overlapping dates the LATER segment in
    the list wins (callers order: peg < NBER < modern cache < LBMA fix, so
    the LBMA fix rules its whole 1968-2022 span and the modern cache only
    supplies the tail FRED no longer serves)."""
    frames = [s for s in segments if s is not None and not s.empty]
    if not frames:
        raise ValueError("no century segments available")
    df = pd.concat(frames)
    df = df[~df.index.duplicated(keep="last")].sort_index()
    df = df[df["close"] > 0]
    df.index.name = "date"
    return df


def validate_century(df: pd.DataFrame) -> list[str]:
    """Sanity problems worth refusing to cache over. Returns messages."""
    problems = []
    if df.index[0] > pd.Timestamp("1920-12-31"):
        problems.append(f"series starts {df.index[0].date()}, expected 1920")
    gaps = df.index.to_series().diff().dt.days.dropna()
    if gaps.max() > 45:
        worst = gaps.idxmax()
        problems.append(f"gap of {gaps.max():.0f} days ending {worst.date()}")
    # a >60% one-step move in a spliced monthly/daily series is a bad join
    # (the 1934 revaluation is +69% — whitelist it)
    step = df["close"].pct_change().abs()
    step = step[step.index != pd.Timestamp("1934-02-28")]
    if step.max() > 0.60:
        problems.append(f"suspicious {step.max():.0%} jump at {step.idxmax().date()}")
    return problems


def build_century(refresh: bool = True) -> pd.DataFrame:
    """Assemble, validate and cache the century series."""
    segments = [official_peg_monthly()]
    if refresh:
        segments.append(_fetch_nber_monthly())
    segments.append(_modern_segment())
    lbma = _fetch_lbma_daily() if refresh else None
    if lbma is not None:
        _write_cache("XAUUSD_LBMA", lbma)              # keep raw era cached
    else:
        lbma = _read_cache("XAUUSD_LBMA")
    segments.append(lbma)
    df = splice(segments)
    problems = validate_century(df)
    for msg in problems:
        log.warning("century series: %s", msg)
    _write_cache(CENTURY_KEY, df)
    return df


def load_century(refresh: bool = False) -> pd.DataFrame:
    """Cache-first load; build (offline-capable) when absent or refreshing."""
    if not refresh:
        cached = _read_cache(CENTURY_KEY)
        if cached is not None:
            return cached
    return build_century(refresh=refresh)


def load_cpi(refresh: bool = False) -> pd.DataFrame | None:
    """US CPI (NSA, monthly, 1913→). None when never fetched and offline."""
    if refresh:
        df = _fred_csv(CPI_KEY)
        if df is None:
            raw = _fetch_csv(DATAHUB_CPI)
            if raw is not None and {"Date", "Index"} <= set(raw.columns):
                df = pd.DataFrame(
                    {"value": raw["Index"].astype(float).values},
                    index=pd.to_datetime(raw["Date"]),
                )
                df.index.name = "date"
        if df is not None and len(df) > 500:
            df.index = df.index + pd.offsets.MonthEnd(0)
            _write_cache(CPI_KEY, df)
            return df
    return _read_cache(CPI_KEY)


# ----------------------------------------------------------------- analytics
def monthly_close(df: pd.DataFrame) -> pd.Series:
    return df["close"].resample("ME").last().dropna()


def real_price(close_m: pd.Series, cpi: pd.DataFrame) -> pd.Series:
    """Deflate to the CPI level of the latest common month."""
    cpi_m = cpi["value"].resample("ME").last().reindex(close_m.index).ffill()
    aligned = pd.concat({"px": close_m, "cpi": cpi_m}, axis=1).dropna()
    base = aligned["cpi"].iloc[-1]
    return aligned["px"] * base / aligned["cpi"]


def drawdown_table(close_m: pd.Series, top: int = 10) -> pd.DataFrame:
    """Peak → trough → recovery episodes, deepest first."""
    peak = close_m.cummax()
    dd = close_m / peak - 1.0
    episodes, in_dd, start = [], False, None
    for t, v in dd.items():
        if not in_dd and v < 0:
            in_dd, start = True, t
        elif in_dd and v == 0:
            seg = dd.loc[start:t]
            episodes.append((start, seg.idxmin(), float(seg.min()), t))
            in_dd = False
    if in_dd:
        seg = dd.loc[start:]
        episodes.append((start, seg.idxmin(), float(seg.min()), pd.NaT))
    rows = [
        {
            "peak": s.strftime("%Y-%m"),
            "trough": tr.strftime("%Y-%m"),
            "depth": depth,
            "recovered": "-" if pd.isna(rec) else rec.strftime("%Y-%m"),
            "months_to_recover": np.nan if pd.isna(rec)
            else (rec.to_period("M") - s.to_period("M")).n,
        }
        for s, tr, depth, rec in episodes
    ]
    cols = ["peak", "trough", "depth", "recovered", "months_to_recover"]
    if not rows:
        return pd.DataFrame(columns=cols)
    return pd.DataFrame(rows)[cols].sort_values("depth").head(top).reset_index(drop=True)


def century_summary(df: pd.DataFrame, cpi: pd.DataFrame | None) -> dict:
    close_m = monthly_close(df)
    years = (close_m.index[-1] - close_m.index[0]).days / 365.25
    out = {
        "start": str(df.index[0].date()),
        "end": str(df.index[-1].date()),
        "rows": int(len(df)),
        "sources": df["source"].value_counts().to_dict(),
        "validation_problems": validate_century(df),
        "cagr_nominal": float((close_m.iloc[-1] / close_m.iloc[0]) ** (1 / years) - 1),
        "vol_by_decade": {
            str(dec): float(g.pct_change().std() * np.sqrt(12))
            for dec, g in close_m.groupby(close_m.index.year // 10 * 10)
            if len(g) > 12
        },
        "drawdowns_nominal": drawdown_table(close_m).to_dict("records"),
    }
    if cpi is not None:
        real_m = real_price(close_m, cpi)
        ry = (real_m.index[-1] - real_m.index[0]).days / 365.25
        r10 = real_m.pct_change(120).dropna()
        out.update(
            {
                "cagr_real": float((real_m.iloc[-1] / real_m.iloc[0]) ** (1 / ry) - 1),
                "drawdowns_real": drawdown_table(real_m).to_dict("records"),
                "worst_10y_real": {
                    "window_end": r10.idxmin().strftime("%Y-%m"),
                    "total_return": float(r10.min()),
                },
                "best_10y_real": {
                    "window_end": r10.idxmax().strftime("%Y-%m"),
                    "total_return": float(r10.max()),
                },
            }
        )
    return out


def _dd_block(records: list[dict]) -> str:
    """Plain-text drawdown table: no tabulate dependency (repo invariant:
    numpy/pandas/scipy/requests only)."""
    df = pd.DataFrame(records)
    if df.empty:
        return "(none)"
    df["depth"] = df["depth"].map(lambda v: f"{v:.1%}")
    return "```\n" + df.to_string(index=False) + "\n```"


def render_century_markdown(s: dict) -> str:
    lines = [
        "# Gold — century series summary",
        "",
        f"Coverage: **{s['start']} → {s['end']}** ({s['rows']} rows)",
        "Sources: " + ", ".join(f"{k}={v}" for k, v in s["sources"].items()),
        "",
        f"CAGR nominal: **{s['cagr_nominal']:.2%}/yr**"
        + (f" — real: **{s['cagr_real']:.2%}/yr**" if "cagr_real" in s else
           " (real: CPI cache missing, run `goldstein century --fetch`)"),
        "",
        "Annualized monthly vol by decade: "
        + ", ".join(f"{k}s {v:.0%}" for k, v in s["vol_by_decade"].items()),
        "",
        "## Deepest drawdowns (nominal, monthly closes)",
        "",
        _dd_block(s["drawdowns_nominal"]),
    ]
    if "drawdowns_real" in s:
        lines += [
            "",
            "## Deepest drawdowns (REAL, CPI-deflated)",
            "",
            _dd_block(s["drawdowns_real"]),
            "",
            f"Worst 10y real total return: {s['worst_10y_real']['total_return']:.0%}"
            f" (window ending {s['worst_10y_real']['window_end']}) — best:"
            f" {s['best_10y_real']['total_return']:.0%}"
            f" ({s['best_10y_real']['window_end']})",
        ]
    if s["validation_problems"]:
        lines += ["", "## Validation warnings", ""]
        lines += [f"- {p}" for p in s["validation_problems"]]
    lines += [
        "",
        "*Fixed-price era (1920-1967) uses official U.S. prices (and NBER "
        "observations where fetched): drawdown/vol statistics there reflect "
        "the peg, not a free market. The 1934 revaluation (+69%) is a policy "
        "step, not a return anyone could earn. Interpret pre-1968 rows as "
        "context, not as backtestable prices.*",
    ]
    return "\n".join(lines)
