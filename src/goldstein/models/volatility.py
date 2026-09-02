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


def realized_variance_from_bars(bars: pd.DataFrame, min_bars: int = 60) -> pd.Series:
    """Daily realized variance from intraday close-to-close log returns
    (sum of squared 5m returns), the estimator HAR-RV was designed for.

    Days are grouped by CME trade date (session opens 23:00 UTC, so bars are
    shifted +1h before taking the date). Days with fewer than `min_bars`
    bars — holidays, partial fetch days — are dropped rather than reported
    as artificially calm."""
    logret = np.log(bars["close"].astype(float)).diff().dropna()
    trade_date = (logret.index + pd.Timedelta(hours=1)).date
    grouped = logret.pow(2).groupby(trade_date)
    rv = grouped.sum()[grouped.count() >= min_bars]
    rv.index = pd.to_datetime(rv.index)
    return rv.sort_index()


def splice_rv(proxy: pd.Series, intraday: pd.Series | None) -> tuple[pd.Series, dict]:
    """One variance series for HAR: true intraday RV where it exists,
    squared-daily-return proxy before that.

    The proxy is multiplicatively bias-adjusted so its mean matches the
    intraday RV over the overlap window — squared daily returns are an
    unbiased but much noisier estimator, and close-to-close vs session-sum
    levels differ, so an unadjusted splice would put a level step exactly
    where the regression is trying to learn dynamics. The returned info dict
    documents the splice date and factor for the report."""
    info = {"har_source": "daily_proxy", "rv_splice_date": None}
    if intraday is None or len(intraday) < 60:
        return proxy, info
    overlap = proxy.index.intersection(intraday.index)
    factor = 1.0
    if len(overlap) >= 30 and float(proxy.loc[overlap].mean()) > 0:
        factor = float(intraday.loc[overlap].mean() / proxy.loc[overlap].mean())
    start = intraday.index[0]
    spliced = pd.concat([proxy[proxy.index < start] * factor, intraday]).sort_index()
    spliced = spliced[~spliced.index.duplicated(keep="last")]
    info.update(
        har_source="intraday_rv",
        rv_splice_date=str(start.date()),
        proxy_bias_factor=round(factor, 4),
    )
    return spliced, info


def har_rv_forecast(returns: pd.Series, rv: pd.Series | None = None) -> float:
    """HAR-RV (Corsi 2009): regress next-day realized variance on daily,
    weekly, monthly averages. Returns annualized vol forecast for ~1 month.

    `rv` is a daily variance series (ideally true intraday RV via
    splice_rv); without it, squared daily returns are the fallback proxy."""
    rv = returns.pow(2) if rv is None else rv.dropna()
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


FIXED_WEIGHTS = {"ewma": 0.3, "garch": 0.4, "har": 0.3}


def _qlike(pred_var: np.ndarray, realized_var: np.ndarray) -> np.ndarray:
    """QLIKE loss — the standard robust loss for variance forecasts
    (Patton 2011): consistent even when the realized proxy is noisy,
    and it punishes under-prediction harder, which is the right asymmetry
    for a series that feeds leverage sizing."""
    ratio = np.maximum(realized_var, 1e-14) / np.maximum(pred_var, 1e-14)
    return ratio - np.log(ratio) - 1.0


def oos_blend_weights(
    returns: pd.Series,
    rv: pd.Series,
    garch: GarchFit,
    horizon: int = 21,
    n_eval: int = 24,
    step: int = 21,
    floor: float = 0.10,
) -> tuple[dict | None, dict]:
    """Inverse-QLIKE blend weights from a rolling forecast evaluation.

    At each of `n_eval` points (spaced `step` days, most recent last) every
    model forecasts the mean daily variance over the next `horizon` days and
    is scored against realized variance:
    - EWMA: truly out-of-sample (causal filter value at t);
    - HAR: truly out-of-sample (refit by lstsq on data <= t at every point);
    - GARCH: PSEUDO out-of-sample — the causal filtered path is used, but
      with full-sample parameters (refitting 24 MLEs per report is not worth
      the wall-clock; the caveat is carried in the diagnostics).
    Weights are proportional to 1/meanQLIKE, floored at `floor` and
    renormalized. Returns (None, diagnostics) when history is too short."""
    df = pd.DataFrame({"r": returns, "rv": rv}).dropna()
    n = len(df)
    min_fit = 300
    points = [
        n - horizon - k * step
        for k in range(n_eval)
        if n - horizon - k * step >= min_fit
    ]
    if len(points) < 8:
        return None, {"weight_method": "fixed_fallback",
                      "reason": f"only {len(points)} eval points"}
    r, rv_a = df["r"].to_numpy(), df["rv"].to_numpy()
    ewma_var = (ewma_vol(df["r"]) ** 2 / TRADING_DAYS).to_numpy()
    gvar = (garch.cond_vol.reindex(df.index).ffill() ** 2 / TRADING_DAYS).to_numpy()
    lr_var = garch.omega / max(1e-12, 1 - garch.persistence)

    losses = {"ewma": [], "garch": [], "har": []}
    for t in points:
        target = float(rv_a[t: t + horizon].mean())
        losses["ewma"].append(_qlike(np.array([ewma_var[t - 1]]), np.array([target]))[0])
        v = gvar[t - 1]
        path = []
        for _ in range(horizon):
            v = lr_var + garch.persistence * (v - lr_var)
            path.append(v)
        losses["garch"].append(_qlike(np.array([np.mean(path)]), np.array([target]))[0])
        rv_t = df["rv"].iloc[:t]
        x = pd.DataFrame({"d": rv_t.shift(1), "w": rv_t.rolling(5).mean().shift(1),
                          "m": rv_t.rolling(21).mean().shift(1)}).dropna()
        X = np.column_stack([np.ones(len(x)), x.values])
        beta, *_ = np.linalg.lstsq(X, rv_t.reindex(x.index).values, rcond=None)
        latest = np.array([1.0, rv_t.iloc[-1], rv_t.iloc[-5:].mean(), rv_t.iloc[-21:].mean()])
        losses["har"].append(_qlike(np.array([max(float(latest @ beta), 1e-14)]),
                                    np.array([target]))[0])

    mean_loss = {k: float(np.mean(v)) for k, v in losses.items()}
    inv = {k: 1.0 / max(v, 1e-12) for k, v in mean_loss.items()}
    total = sum(inv.values())
    w = {k: max(v / total, floor) for k, v in inv.items()}
    norm = sum(w.values())
    w = {k: v / norm for k, v in w.items()}
    return w, {"weight_method": "oos_qlike", "eval_points": len(points),
               "mean_qlike": {k: round(v, 4) for k, v in mean_loss.items()},
               "garch_eval": "pseudo_oos_full_sample_params"}


def bootstrap_forecast_ci(
    returns: pd.Series,
    rv: pd.Series,
    garch: GarchFit,
    weights: dict,
    n_boot: int = 200,
    mean_block: float = 21.0,
    window: int = 1000,
    seed: int = 42,
) -> tuple[float, float] | None:
    """5-95% band on the blended annualized vol forecast via joint
    stationary block bootstrap of (return, RV) pairs over the recent
    `window` days. Per draw: EWMA and GARCH are re-filtered on the bootstrap
    path (GARCH keeps full-sample parameters — the band covers sampling
    variability of the recent history and HAR parameter uncertainty, not
    GARCH parameter uncertainty; refitting 200 MLEs is not worth it and the
    docstring says so). HAR is fully refit per draw."""
    df = pd.DataFrame({"r": returns, "rv": rv}).dropna().iloc[-window:]
    n = len(df)
    if n < 300:
        return None
    rng = np.random.default_rng(seed)
    r2 = (df["r"].to_numpy() ** 2)
    rv_a = df["rv"].to_numpy()
    # joint index paths (stationary bootstrap, geometric blocks)
    p = 1.0 / mean_block
    idx = np.empty((n_boot, n), dtype=np.int64)
    idx[:, 0] = rng.integers(0, n, size=n_boot)
    restart = rng.random((n_boot, n)) < p
    jumps = rng.integers(0, n, size=(n_boot, n))
    for t in range(1, n):
        idx[:, t] = np.where(restart[:, t], jumps[:, t], (idx[:, t - 1] + 1) % n)
    r2_b, rv_b = r2[idx], rv_a[idx]

    lam = 0.94
    ew_var = r2_b[:, :30].mean(axis=1).copy()
    g_var = np.full(n_boot, max(garch.cond_vol.iloc[0] ** 2 / TRADING_DAYS, 1e-12))
    for t in range(1, n):
        ew_var = lam * ew_var + (1 - lam) * r2_b[:, t]
        g_var = garch.omega + garch.alpha * r2_b[:, t - 1] + garch.beta * g_var
    lr_var = garch.omega / max(1e-12, 1 - garch.persistence)
    g_fc = np.zeros(n_boot)
    v = g_var.copy()
    for _ in range(21):
        v = lr_var + garch.persistence * (v - lr_var)
        g_fc += v
    g_fc /= 21.0

    har_fc = np.empty(n_boot)
    for b in range(n_boot):
        s = pd.Series(rv_b[b])
        x = pd.DataFrame({"d": s.shift(1), "w": s.rolling(5).mean().shift(1),
                          "m": s.rolling(21).mean().shift(1)}).dropna()
        X = np.column_stack([np.ones(len(x)), x.values])
        beta, *_ = np.linalg.lstsq(X, s.reindex(x.index).values, rcond=None)
        latest = np.array([1.0, s.iloc[-1], s.iloc[-5:].mean(), s.iloc[-21:].mean()])
        har_fc[b] = max(float(latest @ beta), 1e-14)

    blend_var = (weights["ewma"] * ew_var + weights["garch"] * g_fc
                 + weights["har"] * har_fc)
    vols = np.sqrt(blend_var * TRADING_DAYS)
    return float(np.quantile(vols, 0.05)), float(np.quantile(vols, 0.95))


@dataclass
class VolForecast:
    ewma: float
    garch: float
    har: float
    blended: float
    garch_persistence: float
    long_run: float
    har_source: str = "daily_proxy"     # "intraday_rv" when 5m RV feeds HAR
    rv_splice_date: str | None = None   # first day of true intraday RV
    weights: dict | None = None         # blend weights actually used
    weight_method: str = "fixed"        # "oos_qlike" | "fixed_fallback" | "fixed"
    ci_low: float | None = None         # 5% bootstrap band, annualized
    ci_high: float | None = None        # 95%


def forecast_vol(returns: pd.Series,
                 intraday_rv: pd.Series | None = None,
                 seed: int = 42) -> VolForecast:
    """Blend the three models. Weights come from a rolling out-of-sample
    QLIKE evaluation (oos_blend_weights) — the fixed 0.3/0.4/0.3 is only the
    fallback for short histories. A joint block-bootstrap 5-95% band on the
    blended forecast quantifies sampling uncertainty.

    `intraday_rv`: optional daily realized-variance series from 5m bars
    (realized_variance_from_bars); HAR then runs on true RV spliced with the
    squared-return proxy for the pre-intraday history."""
    ew = float(ewma_vol(returns).iloc[-1])
    g = fit_garch(returns)
    garch_ok = g.converged and 0.5 < g.persistence < 0.9999
    gv = g.forecast(21) if garch_ok else ew
    rv, info = splice_rv(returns.pow(2), intraday_rv)
    hv = har_rv_forecast(returns, rv)

    w, diag = (oos_blend_weights(returns, rv, g) if garch_ok
               else (None, {"weight_method": "fixed_fallback",
                            "reason": "garch_not_converged"}))
    weights = w or dict(FIXED_WEIGHTS)
    blended = float(weights["ewma"] * ew + weights["garch"] * gv
                    + weights["har"] * hv)
    ci = (bootstrap_forecast_ci(returns, rv, g, weights, seed=seed)
          if garch_ok else None)
    return VolForecast(
        ew, gv, hv, blended, g.persistence, g.long_run_vol,
        info["har_source"], info["rv_splice_date"],
        {k: round(v, 3) for k, v in weights.items()}, diag["weight_method"],
        ci[0] if ci else None, ci[1] if ci else None,
    )
