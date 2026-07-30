"""Volatility forecasting: EWMA (RiskMetrics), GARCH(1,1) by MLE, HAR-RV.

The final forecast is an inverse-error-weighted blend; leverage sizing depends
on it directly, so we prefer an ensemble over any single model.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.optimize import minimize

from ..config import TRADING_DAYS


def ewma_vol(returns: pd.Series, lam: float = 0.94) -> pd.Series:
    """RiskMetrics EWMA conditional vol (annualized)."""
    var = returns.pow(2).ewm(alpha=1 - lam, adjust=False).mean()
    return np.sqrt(var * TRADING_DAYS)


@dataclass
class GarchFit:
    omega: float
    alpha: float
    beta: float
    persistence: float
    long_run_vol: float           # annualized
    cond_vol: pd.Series           # annualized, in-sample
    converged: bool

    def forecast(self, horizon: int = 21) -> float:
        """Mean annualized vol over the next `horizon` days."""
        lr_var = self.omega / max(1e-12, 1 - self.persistence)
        v = (self.cond_vol.iloc[-1] ** 2) / TRADING_DAYS
        path = []
        for _ in range(horizon):
            v = lr_var + self.persistence * (v - lr_var)
            path.append(v)
        return float(np.sqrt(np.mean(path) * TRADING_DAYS))


def fit_garch(returns: pd.Series) -> GarchFit:
    """GARCH(1,1) via quasi-MLE (Gaussian likelihood, L-BFGS-B)."""
    r = returns.dropna().values
    r = r - r.mean()
    var0 = r.var()

    def neg_loglik(params):
        omega, alpha, beta = params
        if omega <= 0 or alpha < 0 or beta < 0 or alpha + beta >= 0.9999:
            return 1e10
        h = np.empty_like(r)
        h[0] = var0
        for t in range(1, len(r)):
            h[t] = omega + alpha * r[t - 1] ** 2 + beta * h[t - 1]
        h = np.maximum(h, 1e-12)
        return 0.5 * np.sum(np.log(h) + r**2 / h)

    x0 = np.array([var0 * 0.05, 0.08, 0.90])
    res = minimize(
        neg_loglik, x0, method="L-BFGS-B",
        bounds=[(1e-12, None), (0.0, 0.5), (0.0, 0.999)],
    )
    omega, alpha, beta = res.x
    h = np.empty_like(r)
    h[0] = var0
    for t in range(1, len(r)):
        h[t] = omega + alpha * r[t - 1] ** 2 + beta * h[t - 1]
    cond = pd.Series(np.sqrt(np.maximum(h, 1e-12) * TRADING_DAYS),
                     index=returns.dropna().index)
    persistence = alpha + beta
    lr_vol = float(np.sqrt(omega / max(1e-12, 1 - persistence) * TRADING_DAYS))
    return GarchFit(float(omega), float(alpha), float(beta),
                    float(persistence), lr_vol, cond, bool(res.success))


def har_rv_forecast(returns: pd.Series) -> float:
    """HAR-RV (Corsi 2009): regress next-day realized variance on daily,
    weekly, monthly averages. Returns annualized vol forecast for ~1 month."""
    rv = returns.pow(2)
    x = pd.DataFrame(
        {
            "d": rv.shift(1),
            "w": rv.rolling(5).mean().shift(1),
            "m": rv.rolling(21).mean().shift(1),
        }
    ).dropna()
    y = rv.reindex(x.index)
    X = np.column_stack([np.ones(len(x)), x.values])
    beta, *_ = np.linalg.lstsq(X, y.values, rcond=None)
    latest = np.array([1.0, rv.iloc[-1], rv.iloc[-5:].mean(), rv.iloc[-21:].mean()])
    pred_var = float(np.clip(latest @ beta, 1e-12, None))
    return float(np.sqrt(pred_var * TRADING_DAYS))


@dataclass
class VolForecast:
    ewma: float
    garch: float
    har: float
    blended: float
    garch_persistence: float
    long_run: float


def forecast_vol(returns: pd.Series) -> VolForecast:
    """Blend the three models; weights favor GARCH when it converged sanely."""
    ew = float(ewma_vol(returns).iloc[-1])
    g = fit_garch(returns)
    gv = g.forecast(21) if g.converged and 0.5 < g.persistence < 0.9999 else ew
    hv = har_rv_forecast(returns)
    blended = float(np.average([ew, gv, hv], weights=[0.3, 0.4, 0.3]))
    return VolForecast(ew, gv, hv, blended, g.persistence, g.long_run_vol)
