"""Mechanical signal — the single source of truth used by both the
backtester and alerts.py. Implements SIGNAL_SPEC.md exactly; if the spec
changes, change it here and nowhere else.

Every signal row is stamped with the confirmation candle t: nothing after
t's close is used. 4H S/R levels are only usable from the close of their own
confirmation candle."""
from __future__ import annotations

from dataclasses import dataclass, asdict

import numpy as np
import pandas as pd

from .indicators import atr, bollinger, pivot_points, rsi


@dataclass
class SignalParams:
    rsi_period: int = 14
    pivot_k_1h: int = 3
    div_lookback: int = 30       # N
    bb_period: int = 20
    bb_std: float = 2.0
    sr_pivot_k: int = 5          # K
    sr_tolerance: float = 0.005  # X
    require_sr: bool = True
    atr_period: int = 14

    def to_dict(self) -> dict:
        return asdict(self)


def _sr_levels(df4h: pd.DataFrame, k: int) -> pd.DataFrame:
    """All 4H pivot high/low levels with the close time from which each level
    is usable (confirmation candle's close = its open time + 4h)."""
    rows = []
    for kind, col in (("low", "low"), ("high", "high")):
        for i in pivot_points(df4h[col], k, kind):
            rows.append(
                {
                    "level": float(df4h[col].iloc[i]),
                    "usable_from": df4h.index[i + k] + pd.Timedelta(hours=4),
                }
            )
    if not rows:
        return pd.DataFrame(columns=["level", "usable_from"])
    return pd.DataFrame(rows).sort_values("usable_from").reset_index(drop=True)


def find_signals(
    df1h: pd.DataFrame, df4h: pd.DataFrame, params: SignalParams
) -> pd.DataFrame:
    """Return one row per confirmed setup, both directions.

    Columns: time (1H open time of confirmation candle t), side (+1/-1),
    entry (close[t]), atr, pivot/divergence details, sr_ok. When
    params.require_sr is False the sr_ok column still reports whether the
    confluence held, so the filter's marginal value can be measured on the
    same signal set.
    """
    p = params
    close, high, low = df1h["close"], df1h["high"], df1h["low"]
    rsi_s = rsi(close, p.rsi_period)
    bb_lo, _, bb_hi = bollinger(close, p.bb_period, p.bb_std)
    atr_s = atr(high, low, close, p.atr_period)
    levels = _sr_levels(df4h, p.sr_pivot_k)
    lvl_prices = levels["level"].to_numpy()
    lvl_usable_ns = np.array(
        [pd.Timestamp(t).value for t in levels["usable_from"]], dtype="int64"
    )

    out = []
    for side, kind, ext in ((1, "low", low), (-1, "high", high)):
        pivots = pivot_points(ext, p.pivot_k_1h, kind)
        for j, p2 in enumerate(pivots):
            t = p2 + p.pivot_k_1h
            if t >= len(df1h):
                continue  # pivot not yet confirmed at data end
            if np.isnan(rsi_s.iloc[p2]) or np.isnan(bb_lo.iloc[p2]) or np.isnan(atr_s.iloc[t]):
                continue
            # Bollinger condition at the divergence extreme
            if side == 1 and not low.iloc[p2] <= bb_lo.iloc[p2]:
                continue
            if side == -1 and not high.iloc[p2] >= bb_hi.iloc[p2]:
                continue
            # divergence vs the most recent qualifying earlier pivot
            p1_match = None
            for p1 in reversed(pivots[:j]):
                if p2 - p1 > p.div_lookback:
                    break
                if np.isnan(rsi_s.iloc[p1]):
                    continue
                price_div = ext.iloc[p2] < ext.iloc[p1] if side == 1 else ext.iloc[p2] > ext.iloc[p1]
                rsi_div = rsi_s.iloc[p2] > rsi_s.iloc[p1] if side == 1 else rsi_s.iloc[p2] < rsi_s.iloc[p1]
                if price_div and rsi_div:
                    p1_match = p1
                    break
            if p1_match is None:
                continue
            # S/R confluence: only levels confirmed before t's close
            t_close = df1h.index[t] + pd.Timedelta(hours=1)
            usable = lvl_prices[lvl_usable_ns <= t_close.value]
            sr_ok = bool(
                usable.size
                and (np.abs(ext.iloc[p2] / usable - 1.0) <= p.sr_tolerance).any()
            )
            if p.require_sr and not sr_ok:
                continue
            out.append(
                {
                    "time": df1h.index[t],
                    "side": side,
                    "entry": float(close.iloc[t]),
                    "atr": float(atr_s.iloc[t]),
                    "pivot_time": df1h.index[p2],
                    "pivot_price": float(ext.iloc[p2]),
                    "prev_pivot_time": df1h.index[p1_match],
                    "rsi_p2": float(rsi_s.iloc[p2]),
                    "rsi_p1": float(rsi_s.iloc[p1_match]),
                    "sr_ok": sr_ok,
                    "t_index": t,
                }
            )
    if not out:
        return pd.DataFrame(
            columns=[
                "time", "side", "entry", "atr", "pivot_time", "pivot_price",
                "prev_pivot_time", "rsi_p2", "rsi_p1", "sr_ok", "t_index",
            ]
        )
    return (
        pd.DataFrame(out)
        .sort_values(["time", "side"], kind="mergesort")
        .reset_index(drop=True)
    )
