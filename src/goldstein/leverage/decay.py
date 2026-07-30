"""Daily-reset leveraged ETP analytics (volatility decay).

For an L-x daily-reset product on an asset with annualized drift mu and vol
sigma, the expected log growth is approximately
    g(L) = L * mu - L(L-1) * sigma^2 / 2 - fees
so the "decay" versus naive L-times-buy-and-hold is L(L-1)/2 * sigma^2 per
year. At gold-like vol (~15%) a 3x product bleeds ~6.8%/yr from compounding
alone; in a 30%-vol regime that becomes ~27%/yr.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from ..config import TRADING_DAYS


def decay_rate(leverage: float, sigma: float) -> float:
    """Annualized expected compounding drag vs static L-times exposure."""
    return leverage * (leverage - 1.0) * sigma**2 / 2.0


def decay_table(vols=(0.10, 0.15, 0.20, 0.25, 0.30, 0.40),
                leverages=(2.0, 3.0)) -> pd.DataFrame:
    rows = []
    for sigma in vols:
        row = {"annual_vol": sigma}
        for L in leverages:
            row[f"decay_{L:g}x"] = decay_rate(L, sigma)
        rows.append(row)
    return pd.DataFrame(rows)


def breakeven_drift(leverage: float, sigma: float, fees: float = 0.01) -> float:
    """Minimum annual asset drift for the L-x daily-reset ETP to beat the
    unlevered asset in expected log growth (both self-financed):
    L*mu - L(L-1)sigma^2/2 - fees > mu - 0*  =>  solve for mu."""
    return (decay_rate(leverage, sigma) + fees) / max(leverage - 1.0, 1e-9)


def simulate_reset_vs_static(returns: pd.Series, leverage: float,
                             fees: float = 0.01) -> pd.DataFrame:
    """Realized comparison on an actual return path: daily-reset ETP vs
    static (unrebalanced) leverage vs the raw asset."""
    r = returns.dropna()
    etp = (1 + leverage * r - fees / TRADING_DAYS).cumprod()
    asset = (1 + r).cumprod()
    static = 1 + leverage * (asset - 1)          # can go below zero = wipeout
    out = pd.DataFrame({"asset": asset, "daily_reset": etp, "static": static})
    out.attrs["leverage"] = leverage
    return out
