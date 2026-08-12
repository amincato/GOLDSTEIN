"""Mechanical signal — the single source of truth used by both the
backtester and alerts.py. Implements SIGNAL_SPEC.md exactly; if the spec
changes, change it here and nowhere else.

Entry modes:
- "close" (default, v1): the trigger candle t IS the second divergence low —
  it makes a lower low vs a prior CONFIRMED fractal pivot low while RSI is
  higher. The signal fires at t's own close, so entry sits at the low zone
  (critical at 30-100x). No repaint: low[t], RSI[t], BB[t] are all final at
  t's close; only p1 needs fractal confirmation and that is entirely in the
  past (p1 + k <= t).
- "pivot" (comparison variant): the second low must itself be a confirmed
  fractal pivot → entry lags the actual low by pivot_k_1h candles.

Every signal is stamped with its trigger candle t: nothing after t's close
is used. 4H S/R levels are usable only from the close of their own
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
    entry_mode: str = "strength"  # "strength" | "close" | "pivot"
    rsi_min_delta: float = 10.0  # min RSI-point gap between the two lows
    confirm_window: int = 3      # candles after the low to look for strength
    body_max_atr: float = 0.5    # "short candle": body <= this x ATR
    wick_body_ratio: float = 1.5  # "big spike": rejection wick >= this x body
    wick_min_atr: float = 0.3    # ...and >= this x ATR (guards doji division)

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


_COLUMNS = [
    "time", "side", "entry", "atr", "pivot_time", "pivot_price",
    "prev_pivot_time", "rsi_p2", "rsi_p1", "sr_ok", "t_index",
]


def find_signals(
    df1h: pd.DataFrame, df4h: pd.DataFrame, params: SignalParams
) -> pd.DataFrame:
    """Return one row per confirmed setup, both directions.

    The sr_ok column always reports whether the S/R confluence held, even
    when require_sr is False, so the filter's marginal value is measurable.
    """
    p = params
    close, high, low = df1h["close"], df1h["high"], df1h["low"]
    open_v = df1h["open"].to_numpy()
    rsi_v = rsi(close, p.rsi_period).to_numpy()
    bb_lo_s, _, bb_hi_s = bollinger(close, p.bb_period, p.bb_std)
    bb_lo, bb_hi = bb_lo_s.to_numpy(), bb_hi_s.to_numpy()
    atr_v = atr(high, low, close, p.atr_period).to_numpy()
    close_v, high_v, low_v = close.to_numpy(), high.to_numpy(), low.to_numpy()
    levels = _sr_levels(df4h, p.sr_pivot_k)
    lvl_prices = levels["level"].to_numpy()
    lvl_usable_ns = np.array(
        [pd.Timestamp(t).value for t in levels["usable_from"]], dtype="int64"
    )
    # asi8 is in the index's native unit (us for parquet round-trips);
    # normalize to ns to match Timestamp.value
    idx_ns = df1h.index.as_unit("ns").asi8
    hour_ns = 3_600_000_000_000

    def sr_check(price: float, t: int) -> bool:
        usable = lvl_prices[lvl_usable_ns <= idx_ns[t] + hour_ns]
        return bool(
            usable.size and (np.abs(price / usable - 1.0) <= p.sr_tolerance).any()
        )

    out = []
    for side, kind, ext in ((1, "low", low_v), (-1, "high", high_v)):
        pivots = pivot_points(df1h["low" if kind == "low" else "high"], p.pivot_k_1h, kind)

        def divergence_p1(confirmed: list[int], t_ref: int, ext_ref: float, rsi_ref: float):
            """Most recent confirmed pivot within N forming a divergence."""
            for p1 in reversed(confirmed):
                if t_ref - p1 > p.div_lookback:
                    return None
                if np.isnan(rsi_v[p1]):
                    continue
                if side == 1:
                    price_div = ext_ref < ext[p1]
                    rsi_div = rsi_ref >= rsi_v[p1] + p.rsi_min_delta
                else:
                    price_div = ext_ref > ext[p1]
                    rsi_div = rsi_ref <= rsi_v[p1] - p.rsi_min_delta
                if price_div and rsi_div:
                    return p1
            return None

        def strength_entry(p2: int):
            """First candle in the confirmation window showing rejection
            (short body + big spike, closing in the strong half) or momentum
            (engulfing the previous candle's extreme). A CLOSE beyond the
            divergence extreme kills the setup."""
            for w in range(p2 + 1, min(p2 + 1 + p.confirm_window, len(df1h))):
                if np.isnan(atr_v[w]):
                    return None
                body = abs(close_v[w] - open_v[w])
                if side == 1:
                    if close_v[w] < low_v[p2]:
                        return None
                    wick = min(open_v[w], close_v[w]) - low_v[w]
                    hammer = (
                        body <= p.body_max_atr * atr_v[w]
                        and wick >= p.wick_body_ratio * body
                        and wick >= p.wick_min_atr * atr_v[w]
                        and close_v[w] >= (high_v[w] + low_v[w]) / 2
                    )
                    momentum = close_v[w] > open_v[w] and close_v[w] > high_v[w - 1]
                else:
                    if close_v[w] > high_v[p2]:
                        return None
                    wick = high_v[w] - max(open_v[w], close_v[w])
                    hammer = (
                        body <= p.body_max_atr * atr_v[w]
                        and wick >= p.wick_body_ratio * body
                        and wick >= p.wick_min_atr * atr_v[w]
                        and close_v[w] <= (high_v[w] + low_v[w]) / 2
                    )
                    momentum = close_v[w] < open_v[w] and close_v[w] < low_v[w - 1]
                if hammer or momentum:
                    return w
            return None

        def emit(t: int, p2: int, p1: int):
            price = ext[p2]
            sr_ok = sr_check(price, t)
            if p.require_sr and not sr_ok:
                return
            out.append(
                {
                    "time": df1h.index[t],
                    "side": side,
                    "entry": float(close_v[t]),
                    "atr": float(atr_v[t]),
                    "pivot_time": df1h.index[p2],
                    "pivot_price": float(price),
                    "prev_pivot_time": df1h.index[p1],
                    "rsi_p2": float(rsi_v[p2]),
                    "rsi_p1": float(rsi_v[p1]),
                    "sr_ok": sr_ok,
                    "t_index": t,
                }
            )

        if p.entry_mode == "pivot":
            for j, p2 in enumerate(pivots):
                t = p2 + p.pivot_k_1h
                if t >= len(df1h):
                    continue
                if np.isnan(rsi_v[p2]) or np.isnan(bb_lo[p2]) or np.isnan(atr_v[t]):
                    continue
                if side == 1 and not low_v[p2] <= bb_lo[p2]:
                    continue
                if side == -1 and not high_v[p2] >= bb_hi[p2]:
                    continue
                p1 = divergence_p1(list(pivots[:j]), p2, ext[p2], rsi_v[p2])
                if p1 is not None:
                    emit(t, p2, p1)
        else:  # "close": trigger candle t is itself the second low
            confirmed: list[int] = []
            pi = 0
            used_p1: set[int] = set()
            for t in range(len(df1h)):
                while pi < len(pivots) and pivots[pi] + p.pivot_k_1h <= t:
                    confirmed.append(int(pivots[pi]))
                    pi += 1
                if np.isnan(rsi_v[t]) or np.isnan(bb_lo[t]) or np.isnan(atr_v[t]):
                    continue
                if side == 1 and not low_v[t] <= bb_lo[t]:
                    continue
                if side == -1 and not high_v[t] >= bb_hi[t]:
                    continue
                p1 = divergence_p1(confirmed, t, ext[t], rsi_v[t])
                if p1 is None or p1 in used_p1:
                    continue  # one signal per p1: no re-fire on every new low
                if p.entry_mode == "strength":
                    w = strength_entry(t)
                    if w is None:
                        continue  # no strength in the window / setup killed
                    used_p1.add(p1)
                    emit(w, t, p1)
                else:
                    used_p1.add(p1)
                    emit(t, t, p1)

    if not out:
        return pd.DataFrame(columns=_COLUMNS)
    return (
        pd.DataFrame(out)
        .sort_values(["time", "side"], kind="mergesort")
        .reset_index(drop=True)
    )
