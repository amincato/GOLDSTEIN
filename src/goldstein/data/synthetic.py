"""Deterministic synthetic market data, calibrated to long-run gold behaviour.

Used when neither the network nor the local cache can supply real data, so the
whole platform stays runnable offline (clearly flagged as DEMO in reports).

The generator is a 3-regime switching model (calm / trending / crisis) with
stochastic volatility, which reproduces the stylized facts that matter for
leverage research: vol clustering, fat tails, drawdown spells and the
negative gold-vs-real-yield / gold-vs-DXY correlations.
"""

from __future__ import annotations

import zlib

import numpy as np
import pandas as pd

from ..config import TRADING_DAYS


def _key_seed(key: str, seed: int) -> int:
    """Stable per-series seed (zlib.crc32, NOT hash() which is salted per
    process and would break cross-process determinism)."""
    return seed + zlib.crc32(key.encode()) % 100_000

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


# correlated price assets: key -> (correlation to gold, annual vol, drift, start price)
_CORRELATED = {
    "XAGUSD": (0.75, 0.28, 0.03, 22.0),
    "GDX": (0.70, 0.35, 0.02, 30.0),
    "UGL": (0.95, 0.30, 0.01, 60.0),
    "GLD": (0.99, 0.15, 0.04, 150.0),
    "DXY": (-0.45, 0.07, 0.00, 100.0),
    "SPX": (0.10, 0.18, 0.07, 4000.0),
    "WTI": (0.20, 0.35, 0.02, 70.0),
    "BTC": (0.15, 0.60, 0.10, 40000.0),
}


def synthetic_price(key: str, years: int = 15, seed: int = 42) -> pd.DataFrame:
    """Price series for any universe asset. Gold is the base path; the others
    are generated with realistic correlation to gold so cross-asset analytics
    stay meaningful in DEMO mode."""
    gold = synthetic_gold(years, seed)
    if key == "XAUUSD":
        return gold
    rho, vol, drift, start = _CORRELATED.get(key, (0.0, 0.20, 0.02, 100.0))
    g = np.log(gold["close"] / gold["close"].shift(1)).fillna(0.0).values
    g_std = (g - g.mean()) / max(g.std(), 1e-12)
    rng = np.random.default_rng(_key_seed(key, seed))
    n = len(gold)
    eps = rng.standard_t(df=6, size=n) / np.sqrt(6 / 4)
    z = rho * g_std + np.sqrt(max(1 - rho**2, 0.0)) * eps
    rets = drift / TRADING_DAYS + vol / np.sqrt(TRADING_DAYS) * z
    close = start * np.exp(np.cumsum(rets))
    intraday = np.abs(rng.standard_normal(n)) * vol / np.sqrt(TRADING_DAYS) * close
    df = pd.DataFrame(
        {
            "open": close * np.exp(-rets / 2),
            "high": close + intraday,
            "low": np.maximum(close - intraday, 1e-6),
            "close": close,
            "volume": rng.integers(50_000, 300_000, n).astype(float),
        },
        index=gold.index,
    )
    df.index.name = "date"
    return df


def synthetic_macro(key: str, years: int = 15, seed: int = 42) -> pd.DataFrame:
    """Macro series loosely anchored to the gold path's regimes (same seed)."""
    n = years * TRADING_DAYS
    rng = np.random.default_rng(_key_seed(key, seed))
    states = _regime_path(n, np.random.default_rng(seed))
    anchors = {
        "REAL10Y": (1.0, 0.03, -0.8),      # level, daily noise, crisis shift
        "BREAKEVEN10Y": (2.2, 0.02, -0.3),
        "VIX": (17.0, 0.8, 18.0),
        "FEDFUNDS": (3.0, 0.01, -1.0),
        "NOM10Y": (3.5, 0.03, -0.5),
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
