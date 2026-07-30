"""Leverage sizing — the core question of the platform.

Stack of independent caps, all computed from forward-looking inputs:
  1. Fractional Kelly            f* = (mu - rf) / sigma^2, scaled by
                                 `kelly_fraction` (half-Kelly default) with
                                 drift shrinkage for estimation error.
  2. Volatility targeting        lev = target_vol / forecast_vol.
  3. Drawdown governor           linearly de-lever as current drawdown
                                 approaches a cutoff (CPPI-flavored).
  4. Signal conviction           scale by |signal| (no edge -> no leverage).
  5. Instrument + global caps.

The recommendation is min() of the caps — deliberately conservative, since
leverage errors are asymmetric (you can't compound your way back from ruin).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from ..config import TRADING_DAYS, Instrument, Settings


@dataclass
class LeverageAdvice:
    recommended: float            # final leverage on capital (0 = stay out)
    direction: str
    caps: dict = field(default_factory=dict)
    kelly_full: float = 0.0
    expected_growth: float = 0.0  # log-growth/yr at recommended leverage
    ruin_note: str = ""


def kelly_fraction(mu: float, sigma: float, rf: float, shrink: float = 0.5) -> float:
    """Full Kelly with drift shrinkage: mu estimation error dominates, so we
    shrink the excess-return estimate toward zero before dividing by var."""
    excess = (mu - rf) * shrink
    return excess / max(sigma**2, 1e-9)


def expected_log_growth(lev: float, mu: float, sigma: float, rf: float,
                        financing_spread: float = 0.0) -> float:
    """Annualized expected log growth of a continuously rebalanced position:
    g(L) = rf + L(mu - rf) - L*spread*(L>1 part) - L^2 sigma^2 / 2."""
    borrow = max(lev - 1.0, 0.0) * financing_spread
    return rf + lev * (mu - rf) - borrow - 0.5 * lev**2 * sigma**2


def drawdown_governor(current_dd: float, cutoff: float = 0.20) -> float:
    """Multiplier in [0,1]: full risk at 0 drawdown, zero at `cutoff`."""
    return float(np.clip(1.0 - abs(current_dd) / cutoff, 0.0, 1.0))


def advise(
    mu: float,
    forecast_vol: float,
    signal_score: float,
    current_drawdown: float,
    instrument: Instrument,
    settings: Settings,
) -> LeverageAdvice:
    rf = settings.risk_free
    k_full = kelly_fraction(mu, forecast_vol, rf, shrink=1.0)
    k_frac = kelly_fraction(mu, forecast_vol, rf, shrink=1.0) * settings.kelly_fraction
    vol_cap = settings.target_vol / max(forecast_vol, 1e-9)
    dd_mult = drawdown_governor(current_drawdown)
    conviction = abs(signal_score)

    caps = {
        "fractional_kelly": max(k_frac, 0.0),
        "vol_target": vol_cap,
        "instrument_max": instrument.max_leverage,
        "global_max": settings.max_leverage,
    }
    base = min(caps.values())
    lev = base * dd_mult * conviction
    lev = float(np.clip(lev, 0.0, min(instrument.max_leverage, settings.max_leverage)))
    caps["drawdown_multiplier"] = dd_mult
    caps["signal_conviction"] = conviction

    direction = "long" if signal_score > 0.1 else "short" if signal_score < -0.1 else "flat"
    if direction == "flat":
        lev = 0.0

    growth = expected_log_growth(lev, mu, forecast_vol, rf, instrument.financing_spread)
    note = ""
    if k_full > 0 and lev > k_full:
        note = "WARNING: above full Kelly — expected growth is DECREASING in leverage here"
    elif k_full <= 0 and direction == "long":
        note = "Estimated edge is non-positive; any long leverage is negative-EV under these estimates"

    return LeverageAdvice(round(lev, 2), direction, caps, float(k_full),
                          float(growth), note)


def leverage_frontier(mu: float, sigma: float, rf: float,
                      financing_spread: float = 0.0,
                      levs: np.ndarray | None = None) -> pd.DataFrame:
    """Growth vs leverage curve — makes the Kelly peak and the over-leverage
    cliff visible in reports."""
    levs = levs if levs is not None else np.arange(0.0, 6.01, 0.25)
    rows = [
        {
            "leverage": float(l),
            "expected_log_growth": expected_log_growth(l, mu, sigma, rf, financing_spread),
            "annual_vol": float(l * sigma),
        }
        for l in levs
    ]
    return pd.DataFrame(rows)
