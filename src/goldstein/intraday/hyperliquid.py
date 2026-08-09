"""Hyperliquid gold-perp microstructure analysis vs the reference price.

A perpetual on gold and the underlying reference (spot XAUUSD / COMEX) are
tied by arbitrage but not rigidly: the *basis* (perp/ref - 1) breathes with
funding, liquidations and crypto-native flows. Unlike chart patterns, this
structure is measurable:

  1. Basis distribution + current z-score, and its mean-reversion half-life
     (an AR(1) on the basis) — how stretched is the perp right now, and how
     fast do stretches close?
  2. Dislocation study: after |z| > 2 events, what do basis and perp do over
     the next 1h/4h/24h?
  3. Lead-lag: do perp returns lead reference returns or follow them?
  4. Weekend: the perp trades while COMEX/spot are closed — how well does
     the perp's weekend move predict Monday's reference gap? (If ~1:1, the
     "gap play" is already priced and Monday-open trades have no edge.)
  5. Funding: level, percentiles, annualized carry — what holding a
     leveraged perp position actually costs, and whether extreme funding
     predicts next-day reversion.

Data: Hyperliquid public info API (no auth). Gold-like perps are discovered
automatically across the main universe and builder dexes (XAU/GOLD/PAXG/
XAUT variants). Candles+funding accumulate in data/cache/hyperliquid/.
"""

from __future__ import annotations

import json
import logging
import time
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import requests

from ..config import CACHE_DIR, REPORT_DIR

log = logging.getLogger("goldstein.intraday")

_API = "https://api.hyperliquid.xyz/info"
_HEADERS = {"Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (goldstein-quant)"}
_GOLD_TOKENS = ("XAU", "GOLD", "PAXG", "XAUT")
_TAKER_FEE = 0.00045
_CANDLE_CAP = 5000


def _post(payload: dict, timeout: int = 20):
    r = requests.post(_API, json=payload, timeout=timeout, headers=_HEADERS)
    r.raise_for_status()
    return r.json()


def _is_goldish(name: str) -> bool:
    up = name.upper()
    return any(tok in up for tok in _GOLD_TOKENS)


def discover_gold_perps() -> list[dict]:
    """Search the main universe and builder dexes for gold-like perps."""
    found = []
    meta = _post({"type": "meta"})
    for a in meta.get("universe", []):
        if _is_goldish(a["name"]) and not a.get("isDelisted"):
            found.append({"dex": "", "coin": a["name"]})
    try:
        dexs = _post({"type": "perpDexs"}) or []
    except Exception:
        dexs = []
    for dex in dexs:
        name = (dex or {}).get("name", "")
        if not name:
            continue
        try:
            m = _post({"type": "meta", "dex": name})
        except Exception:
            continue
        for a in m.get("universe", []):
            if _is_goldish(a["name"]) and not a.get("isDelisted"):
                found.append({"dex": name, "coin": a["name"]})
    return found


def fetch_candles(coin: str, interval: str = "5m", days: int = 30) -> pd.DataFrame:
    """Paginated candleSnapshot -> OHLCV (UTC index)."""
    ms_per = {"5m": 300_000, "1h": 3_600_000}[interval]
    end = int(time.time() * 1000)
    start = end - days * 86_400_000
    rows = []
    cursor = start
    while cursor < end:
        chunk_end = min(cursor + ms_per * _CANDLE_CAP, end)
        data = _post({"type": "candleSnapshot",
                      "req": {"coin": coin, "interval": interval,
                              "startTime": cursor, "endTime": chunk_end}})
        if not data:
            break
        rows.extend(data)
        last = data[-1]["t"]
        if last <= cursor:
            break
        cursor = last + ms_per
    return _rows_to_candles(rows)


def _rows_to_candles(rows: list[dict]) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows)
    idx = pd.to_datetime(df["t"], unit="ms", utc=True)
    # .to_numpy(): passing Series alongside an explicit new index would make
    # pandas align on the old RangeIndex and silently produce all-NaN columns
    out = pd.DataFrame(
        {"open": df["o"].astype(float).to_numpy(),
         "high": df["h"].astype(float).to_numpy(),
         "low": df["l"].astype(float).to_numpy(),
         "close": df["c"].astype(float).to_numpy(),
         "volume": df["v"].astype(float).to_numpy(),
         "trades": df["n"].astype(int).to_numpy()},
        index=idx)
    out.index.name = "datetime"
    return out[~out.index.duplicated(keep="last")].sort_index()


def fetch_funding(coin: str, days: int = 30) -> pd.DataFrame:
    end = int(time.time() * 1000)
    start = end - days * 86_400_000
    rows = []
    cursor = start
    for _ in range(40):                       # funding pages are 500 entries
        data = _post({"type": "fundingHistory", "coin": coin,
                      "startTime": cursor, "endTime": end})
        if not data:
            break
        rows.extend(data)
        last = data[-1]["time"]
        if last <= cursor or len(data) < 500:
            break
        cursor = last + 1
    return _rows_to_funding(rows)


def _rows_to_funding(rows: list[dict]) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows)
    idx = pd.to_datetime(df["time"], unit="ms", utc=True)
    prem = (df["premium"].astype(float).to_numpy() if "premium" in df
            else np.full(len(df), np.nan))
    out = pd.DataFrame({"funding_hourly": df["fundingRate"].astype(float).to_numpy(),
                        "premium": prem}, index=idx)
    out.index.name = "datetime"
    return out[~out.index.duplicated(keep="last")].sort_index()


# --------------------------------------------------------------------- cache
def _cache(name: str):
    return CACHE_DIR / "hyperliquid" / f"{name}.csv"


def _merge_cache(name: str, fresh: pd.DataFrame) -> pd.DataFrame:
    path = _cache(name)
    old = None
    if path.exists():
        old = pd.read_csv(path, parse_dates=["datetime"], index_col="datetime")
        old.index = pd.DatetimeIndex(old.index, tz="UTC")
    merged = pd.concat([old, fresh]) if old is not None else fresh
    merged = merged[~merged.index.duplicated(keep="last")].sort_index()
    merged = merged.dropna(how="all")   # purge poisoned all-NaN cache rows
    if len(merged):
        path.parent.mkdir(parents=True, exist_ok=True)
        merged.to_csv(path)
    return merged


# ------------------------------------------------------------------ analysis
def _reference_5m() -> pd.Series | None:
    p = CACHE_DIR / "intraday" / "XAUUSD_5m.csv"
    if not p.exists():
        return None
    df = pd.read_csv(p, parse_dates=["datetime"], index_col="datetime")
    df.index = pd.DatetimeIndex(df.index, tz="UTC")
    return df["close"]


def _ref_market_open(idx: pd.DatetimeIndex) -> np.ndarray:
    """COMEX-ish hours: Sun 22:00 UTC -> Fri 21:00 UTC, daily break 21-22."""
    dow, hour = idx.dayofweek, idx.hour
    closed = ((dow == 5)
              | ((dow == 4) & (hour >= 21))
              | ((dow == 6) & (hour < 22))
              | (hour == 21))
    return ~closed.values if hasattr(closed, "values") else ~closed


def analyze_basis(perp_close: pd.Series, ref_close: pd.Series,
                  funding: pd.DataFrame | None) -> dict:
    both = pd.DataFrame({"perp": perp_close, "ref": ref_close}).dropna()
    open_mask = _ref_market_open(both.index)
    live = both[open_mask]
    out: dict = {"overlap_bars": int(len(live))}
    if len(live) < 500:
        out["error"] = "insufficient overlapping history"
        return out

    basis = live["perp"] / live["ref"] - 1
    bz_mean, bz_std = basis.mean(), basis.std()
    z = (basis - bz_mean) / max(bz_std, 1e-12)
    out["basis"] = {
        "mean_bps": float(bz_mean * 1e4),
        "std_bps": float(bz_std * 1e4),
        "current_bps": float(basis.iloc[-1] * 1e4),
        "current_z": float(z.iloc[-1]),
        "p5_bps": float(basis.quantile(0.05) * 1e4),
        "p95_bps": float(basis.quantile(0.95) * 1e4),
    }
    # AR(1) half-life of basis deviations
    b0, b1 = basis.iloc[:-1].values, basis.iloc[1:].values
    phi = float(np.corrcoef(b0, b1)[0, 1])
    out["basis"]["ar1_phi"] = phi
    out["basis"]["half_life_bars"] = (float(np.log(0.5) / np.log(abs(phi)))
                                      if 0 < phi < 1 else None)

    # dislocation events: |z|>2, first bar of each episode
    hot = (z.abs() > 2.0)
    starts = hot & ~hot.shift(1, fill_value=False)
    events = []
    for t in z.index[starts]:
        i = basis.index.get_loc(t)
        row = {"sign": float(np.sign(z.loc[t]))}
        for label, k in (("1h", 12), ("4h", 48), ("24h", 288)):
            if i + k < len(basis):
                row[f"basis_move_{label}_bps"] = float((basis.iloc[i + k] - basis.iloc[i]) * 1e4)
                row[f"perp_ret_{label}_bps"] = float((live["perp"].iloc[i + k] / live["perp"].iloc[i] - 1) * 1e4)
        events.append(row)
    ev = pd.DataFrame(events)
    if len(ev) >= 5 and "basis_move_4h_bps" in ev:
        conv = -np.sign(ev["sign"]) * ev["basis_move_4h_bps"]
        out["dislocations"] = {
            "n_events": int(len(ev)),
            "p_converge_4h": float((conv > 0).mean()),
            "avg_convergence_4h_bps": float(conv.mean()),
        }

    # lead-lag: corr(perp_ret_t, ref_ret_{t+k})
    pr = np.log(live["perp"] / live["perp"].shift(1))
    rr = np.log(live["ref"] / live["ref"].shift(1))
    ll = {}
    for k in (-3, -2, -1, 0, 1, 2, 3):
        c = pr.corr(rr.shift(-k))
        if np.isfinite(c):
            ll[f"{k * 5:+d}min"] = round(float(c), 3)
    out["lead_lag"] = ll

    # weekend: perp Fri-close -> Sun-open move vs reference Monday gap
    daily_ref = both["ref"][_ref_market_open(both.index)]
    wk = []
    perp_all = perp_close.dropna()
    fri = both.index[(both.index.dayofweek == 4) & (both.index.hour == 20)]
    for f in fri[:-1]:
        try:
            seg = perp_all.loc[f: f + pd.Timedelta(hours=50)]
            ref_after = daily_ref.loc[f + pd.Timedelta(hours=49):].iloc[:1]
            ref_before = daily_ref.loc[:f].iloc[-1]
            if len(seg) > 10 and len(ref_after):
                wk.append({
                    "perp_weekend_ret": float(seg.iloc[-1] / seg.iloc[0] - 1),
                    "ref_gap": float(ref_after.iloc[0] / ref_before - 1),
                })
        except Exception:
            continue
    if len(wk) >= 3:
        wdf = pd.DataFrame(wk)
        out["weekend"] = {
            "n_weekends": int(len(wdf)),
            "corr_perp_move_vs_monday_gap": float(wdf["perp_weekend_ret"].corr(wdf["ref_gap"])),
            "avg_abs_weekend_move_bps": float(wdf["perp_weekend_ret"].abs().mean() * 1e4),
        }

    if funding is not None and len(funding) > 24:
        f = funding["funding_hourly"]
        out["funding"] = {
            "current_hourly": float(f.iloc[-1]),
            "current_apr": float(f.iloc[-1] * 24 * 365),
            "mean_apr": float(f.mean() * 24 * 365),
            "p90_apr": float(f.quantile(0.9) * 24 * 365),
            "cost_50x_per_day_pct_equity": float(abs(f.iloc[-24:].mean()) * 24 * 50 * 100),
        }
    out["taker_cost_50x_round_trip_pct_equity"] = float(2 * _TAKER_FEE * 50 * 100)
    return out


def run(days: int = 30, save: bool = False, coin: str | None = None) -> dict:
    result: dict = {
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    try:
        perps = ([{"dex": "", "coin": coin}] if coin else discover_gold_perps())
    except Exception as exc:
        result["error"] = f"Hyperliquid API unreachable: {exc}"
        return result
    result["gold_perps_found"] = perps
    if not perps:
        result["error"] = "no gold-like perp found on Hyperliquid"
        return result

    target = perps[0]["coin"]
    result["coin"] = target
    candles = fetch_candles(target, "5m", days)
    candles = _merge_cache(f"{target}_5m", candles)
    try:
        funding = fetch_funding(target, days)
        funding = _merge_cache(f"{target}_funding", funding)
    except Exception:
        funding = None
    result["perp_bars"] = int(len(candles))
    ref = _reference_5m()
    if ref is None or candles.empty:
        result["error"] = "missing perp candles or XAUUSD 5m reference cache"
        return result
    result["analysis"] = analyze_basis(candles["close"], ref, funding)

    if save:
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        (REPORT_DIR / "hyperliquid_latest.json").write_text(
            json.dumps(result, indent=2, default=str))
        (REPORT_DIR / "hyperliquid_latest.md").write_text(render_markdown(result))
    return result


def render_markdown(r: dict) -> str:
    L = ["# GOLDSTEIN — Hyperliquid Gold Perp vs Reference",
         f"_Generated {r['generated_utc']} · coin: {r.get('coin', 'n/a')}_", ""]
    add = L.append
    if r.get("error"):
        add(f"> ⚠️ {r['error']}")
        return "\n".join(L)
    a = r["analysis"]
    if a.get("error"):
        add(f"> ⚠️ {a['error']} (overlap bars: {a.get('overlap_bars')})")
        return "\n".join(L)
    b = a["basis"]
    add("## Basis (perp vs reference, market-open hours)")
    add(f"- Current: **{b['current_bps']:+.1f} bps (z = {b['current_z']:+.2f})** ·"
        f" mean {b['mean_bps']:+.1f} · σ {b['std_bps']:.1f} ·"
        f" 90% range [{b['p5_bps']:+.1f}, {b['p95_bps']:+.1f}]")
    hl = b.get("half_life_bars")
    add(f"- Mean reversion: AR(1) φ={b['ar1_phi']:.3f}"
        + (f" → half-life ≈ {hl * 5:.0f} min" if hl else " (no clean mean reversion)"))
    if "dislocations" in a:
        d = a["dislocations"]
        add(f"- Dislocations |z|>2: {d['n_events']} events ·"
            f" P(convergence in 4h) = {d['p_converge_4h']:.0%} ·"
            f" avg convergence {d['avg_convergence_4h_bps']:+.1f} bps")
    add("")
    add("## Lead-lag (corr of perp return vs reference return shifted)")
    add("`" + json.dumps(a["lead_lag"]) + "`")
    add("(positive at +5min ⇒ the perp LEADS the reference by ~one bar)")
    add("")
    if "weekend" in a:
        w = a["weekend"]
        add("## Weekend behaviour")
        add(f"- {w['n_weekends']} weekends · corr(perp weekend move, Monday reference gap)"
            f" = **{w['corr_perp_move_vs_monday_gap']:+.2f}** ·"
            f" avg |weekend move| {w['avg_abs_weekend_move_bps']:.0f} bps")
        add("")
    if "funding" in a:
        f = a["funding"]
        add("## Funding")
        add(f"- Current {f['current_apr']:+.1%} APR (mean {f['mean_apr']:+.1%},"
            f" p90 {f['p90_apr']:+.1%})")
        add(f"- **Cost of holding 50x: ~{f['cost_50x_per_day_pct_equity']:.1f}% of equity"
            f" per day in funding alone**")
    add(f"- Taker fees at 50x: {r['analysis']['taker_cost_50x_round_trip_pct_equity']:.1f}%"
        " of equity per round trip")
    add("\n---\n_Research tooling, not investment advice._")
    return "\n".join(L)
