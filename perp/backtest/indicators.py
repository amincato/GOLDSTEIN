"""Causal indicators shared by backtester and alerts. No lookahead anywhere
except pivots, which carry an explicit confirmation index."""
from __future__ import annotations

import numpy as np
import pandas as pd


def rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    out = 100.0 - 100.0 / (1.0 + avg_gain / avg_loss)
    return out.where(avg_loss > 0, 100.0)


def bollinger(close: pd.Series, period: int = 20, num_std: float = 2.0):
    mid = close.rolling(period).mean()
    sd = close.rolling(period).std(ddof=0)
    return mid - num_std * sd, mid, mid + num_std * sd


def atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> pd.Series:
    prev_close = close.shift(1)
    tr = pd.concat(
        [high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1
    ).max(axis=1)
    return tr.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()


def pivot_points(values: pd.Series, k: int, kind: str) -> np.ndarray:
    """Fractal pivots. Candle i is a pivot low iff its low is strictly below
    the k candles to its left and <= the k candles to its right (first candle
    of an exact double-bottom wins). Mirror for highs.

    Returns integer positions of pivot candles. A pivot at position i is only
    KNOWN (confirmed) once candle i + k has closed — callers must respect
    that; this function itself looks at the full array.
    """
    v = values.to_numpy(dtype=float)
    n = len(v)
    out = []
    for i in range(k, n - k):
        left, right, c = v[i - k : i], v[i + 1 : i + k + 1], v[i]
        if kind == "low":
            if c < left.min() and c <= right.min():
                out.append(i)
        else:
            if c > left.max() and c >= right.max():
                out.append(i)
    return np.asarray(out, dtype=int)
