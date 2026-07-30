"""Price/return features used by signals, sizing and reporting."""

from __future__ import annotations

import numpy as np
import pandas as pd

from ..config import TRADING_DAYS


def log_returns(close: pd.Series) -> pd.Series:
    return np.log(close / close.shift(1)).dropna()


def realized_vol(returns: pd.Series, window: int = 21) -> pd.Series:
    """Annualized rolling close-to-close volatility."""
    return returns.rolling(window).std() * np.sqrt(TRADING_DAYS)


def parkinson_vol(df: pd.DataFrame, window: int = 21) -> pd.Series:
    """Annualized Parkinson (high/low) volatility — more efficient than c2c."""
    hl = np.log(df["high"] / df["low"]) ** 2
    return np.sqrt(hl.rolling(window).mean() / (4 * np.log(2)) * TRADING_DAYS)


def momentum(close: pd.Series, lookback: int) -> pd.Series:
    """Total return over `lookback` days, skipping the most recent week
    (standard 12-1 style construction to avoid short-term reversal)."""
    skip = min(5, lookback // 4)
    return close.shift(skip) / close.shift(lookback) - 1


def moving_average_state(close: pd.Series, fast: int = 50, slow: int = 200) -> pd.Series:
    """+1 when fast MA above slow MA, -1 below."""
    return np.sign(close.rolling(fast).mean() - close.rolling(slow).mean())


def rsi(close: pd.Series, window: int = 14) -> pd.Series:
    delta = close.diff()
    up = delta.clip(lower=0).ewm(alpha=1 / window, adjust=False).mean()
    down = (-delta.clip(upper=0)).ewm(alpha=1 / window, adjust=False).mean()
    rs = up / down.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def drawdown(close: pd.Series) -> pd.Series:
    return close / close.cummax() - 1


def zscore(series: pd.Series, window: int = 252) -> pd.Series:
    mean = series.rolling(window).mean()
    std = series.rolling(window).std()
    return (series - mean) / std
