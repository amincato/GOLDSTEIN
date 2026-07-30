"""Directional signal ensemble for gold.

Combines time-series momentum (multi-horizon), trend state (MA cross),
short-term mean reversion and the macro regime score into one conviction
score in [-1, +1]. The score scales (and can zero out) recommended leverage —
leverage without an edge estimate is just amplified noise.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from ..features import indicators as ind
from .regime import MacroRegime


@dataclass
class SignalResult:
    score: float                  # [-1, 1] conviction
    direction: str                # long / flat / short
    components: dict = field(default_factory=dict)

    @property
    def is_long(self) -> bool:
        return self.score > 0.1


def _tanh_clip(x: float, scale: float) -> float:
    return float(np.tanh(x / scale))


def compute_signal(close: pd.Series, macro: MacroRegime | None = None,
                   cross_score: float | None = None) -> SignalResult:
    comps: dict[str, float] = {}

    # multi-horizon time-series momentum (3m / 6m / 12m), vol-scaled feel
    for label, lb in (("mom_3m", 63), ("mom_6m", 126), ("mom_12m", 252)):
        m = ind.momentum(close, lb).iloc[-1]
        if np.isfinite(m):
            comps[label] = _tanh_clip(m, 0.10)

    ma = ind.moving_average_state(close).iloc[-1]
    if np.isfinite(ma):
        comps["trend_50_200"] = float(ma)

    # short-term mean reversion: fade stretched RSI, small weight
    r = ind.rsi(close).iloc[-1]
    if np.isfinite(r):
        comps["mean_reversion"] = float(np.clip((50 - r) / 30, -1, 1))

    if macro is not None:
        comps["macro_regime"] = macro.score
    if cross_score is not None:
        comps["cross_asset"] = float(cross_score)

    weights = {
        "mom_3m": 0.12, "mom_6m": 0.18, "mom_12m": 0.18,
        "trend_50_200": 0.17, "mean_reversion": 0.05, "macro_regime": 0.15,
        "cross_asset": 0.15,
    }
    avail = {k: v for k, v in comps.items() if k in weights}
    wsum = sum(weights[k] for k in avail)
    score = sum(weights[k] * v for k, v in avail.items()) / max(wsum, 1e-9)
    direction = "long" if score > 0.1 else "short" if score < -0.1 else "flat"
    return SignalResult(float(score), direction, comps)


def signal_history(close: pd.Series, step: int = 5) -> pd.Series:
    """Point-in-time signal series for backtesting (computed every `step`
    days on expanding history, forward-filled)."""
    idx = close.index
    out = pd.Series(np.nan, index=idx)
    for i in range(260, len(idx), step):
        out.iloc[i] = compute_signal(close.iloc[: i + 1]).score
    return out.ffill().fillna(0.0)
