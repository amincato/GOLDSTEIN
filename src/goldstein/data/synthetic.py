"""Deterministic synthetic market data, calibrated to long-run gold behaviour.

Used when neither the network nor the local cache can supply real data, so the
whole platform stays runnable offline (clearly flagged as DEMO in reports).

The generator is a 3-regime switching model (calm / trending / crisis) with
stochastic volatility, which reproduces the stylized facts that matter for
leverage research: vol clustering, fat tails, drawdown spells and the
negative gold-vs-real-yield / gold-vs-DXY correlations.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from ..config import TRADING_DAYS

# per-regime: (annual drift, annual vol, daily persistence of staying)
_REGIMES = [
    (0.02, 0.10, 0.990),   # calm
    (0.15, 0.16, 0.985),   # trending bull
    (-0.10, 0.32, 0.955),  # crisis / liquidation
]
_TRANSITION_TO = [
    [0.0, 0.7, 0.3],  # from calm
    [0.6, 0.0, 0.4],  # from trending
    [0.5, 0.5, 0.0],  # from crisis
]


def _regime_path(n: int, rng: np.random.Generator) -> np.ndarray:
    states = np.empty(n, dtype=int)
    s = 0
    for t in range(n):
        states[t] = s
        if rng.random() > _REGIMES[s][2]:
            s = int(rng.choice(3, p=_TRANSITION_TO[s]))
    return states


def synthetic_gold(years: int = 15, seed: int = 42, start_price: float = 1200.0) -> pd.DataFrame:
    n = years * TRADING_DAYS
    rng = np.random.default_rng(seed)
    states = _regime_path(n, rng)
    mu = np.array([_REGIMES[s][0] for s in states]) / TRADING_DAYS
    sig = np.array([_REGIMES[s][1] for s in states]) / np.sqrt(TRADING_DAYS)
    # stochastic vol multiplier (log-AR(1)) on top of regime vol
    lv = np.zeros(n)
    for t in range(1, n):
        lv[t] = 0.97 * lv[t - 1] + 0.15 * rng.standard_normal()
    sig = sig * np.exp(lv - lv.var() / 2)
    # Student-t shocks for fat tails
    shocks = rng.standard_t(df=5, size=n) / np.sqrt(5 / 3)
    rets = mu + sig * shocks
    close = start_price * np.exp(np.cumsum(rets))
    dates = pd.bdate_range(end=pd.Timestamp.today().normalize(), periods=n)
    intraday = np.abs(rng.standard_normal(n)) * sig * close
    df = pd.DataFrame(
        {
            "open": close * np.exp(-rets / 2),
            "high": close + intraday,
            "low": np.maximum(close - intraday, 1e-6),
            "close": close,
            "volume": rng.integers(50_000, 300_000, n).astype(float),
        },
        index=dates,
    )
    df.index.name = "date"
    return df


def synthetic_macro(key: str, years: int = 15, seed: int = 42) -> pd.DataFrame:
    """Macro series loosely anchored to the gold path's regimes (same seed)."""
    n = years * TRADING_DAYS
    rng = np.random.default_rng(seed + hash(key) % 10_000)
    states = _regime_path(n, np.random.default_rng(seed))
    anchors = {
        "REAL10Y": (1.0, 0.03, -0.8),      # level, daily noise, crisis shift
        "BREAKEVEN10Y": (2.2, 0.02, -0.3),
        "VIX": (17.0, 0.8, 18.0),
        "FEDFUNDS": (3.0, 0.01, -1.0),
        "DXY": (100.0, 0.35, 2.0),
    }
    level, noise, crisis_shift = anchors.get(key, (1.0, 0.05, 0.0))
    x = np.zeros(n)
    x[0] = level
    for t in range(1, n):
        target = level + (crisis_shift if states[t] == 2 else 0.0)
        x[t] = x[t - 1] + 0.01 * (target - x[t - 1]) + noise * rng.standard_normal()
    if key in ("VIX", "DXY", "FEDFUNDS"):
        x = np.maximum(x, 0.05)
    dates = pd.bdate_range(end=pd.Timestamp.today().normalize(), periods=n)
    df = pd.DataFrame({"value": x}, index=dates)
    df.index.name = "date"
    return df
