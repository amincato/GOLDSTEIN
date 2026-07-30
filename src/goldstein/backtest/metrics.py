"""Performance & tail-risk metrics for equity curves and return streams."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from ..config import TRADING_DAYS


def summarize(returns: pd.Series, rf: float = 0.0) -> dict:
    """Full metric panel from a daily simple-return series."""
    r = returns.dropna()
    if len(r) < 20:
        return {"error": "not enough data"}
    equity = (1 + r).cumprod()
    years = len(r) / TRADING_DAYS
    cagr = float(equity.iloc[-1] ** (1 / years) - 1) if equity.iloc[-1] > 0 else -1.0
    ann_vol = float(r.std() * np.sqrt(TRADING_DAYS))
    excess = r - rf / TRADING_DAYS
    sharpe = float(excess.mean() / max(r.std(), 1e-12) * np.sqrt(TRADING_DAYS))
    downside = r[r < 0].std()
    sortino = float(excess.mean() / max(downside, 1e-12) * np.sqrt(TRADING_DAYS))
    dd = equity / equity.cummax() - 1
    max_dd = float(dd.min())
    calmar = float(cagr / abs(max_dd)) if max_dd < 0 else np.inf
    var95 = float(np.percentile(r, 5))
    cvar95 = float(r[r <= var95].mean()) if (r <= var95).any() else var95
    ulcer = float(np.sqrt((dd**2).mean()))
    return {
        "days": len(r),
        "cagr": cagr,
        "ann_vol": ann_vol,
        "sharpe": sharpe,
        "sortino": sortino,
        "calmar": calmar,
        "max_drawdown": max_dd,
        "ulcer_index": ulcer,
        "var_95_daily": var95,
        "cvar_95_daily": cvar95,
        "skew": float(stats.skew(r)),
        "excess_kurtosis": float(stats.kurtosis(r)),
        "worst_day": float(r.min()),
        "best_day": float(r.max()),
        "final_multiple": float(equity.iloc[-1]),
    }


def cornish_fisher_var(returns: pd.Series, alpha: float = 0.01) -> float:
    """Modified VaR adjusting the Gaussian quantile for skew/kurtosis —
    matters for gold, whose crashes are gappier than a normal implies."""
    r = returns.dropna()
    z = stats.norm.ppf(alpha)
    s, k = stats.skew(r), stats.kurtosis(r)
    z_cf = (z + (z**2 - 1) * s / 6 + (z**3 - 3 * z) * k / 24
            - (2 * z**3 - 5 * z) * s**2 / 36)
    return float(r.mean() + z_cf * r.std())
