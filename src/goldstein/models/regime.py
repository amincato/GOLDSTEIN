"""Market regime detection.

Two complementary views:
1. Statistical — Gaussian HMM (own EM implementation, log-space
   forward-backward) on daily returns; states are sorted by volatility and
   labeled calm / normal / turbulent.
2. Macro — rule-based score from real yields, DXY and VIX, since gold's
   fundamental regime is driven by real rates and the dollar.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd
from scipy.stats import norm

_LABELS3 = ["calm", "normal", "turbulent"]


@dataclass
class HmmResult:
    n_states: int
    means: np.ndarray             # daily return mean per state
    vols: np.ndarray              # daily return vol per state
    transition: np.ndarray
    state_prob: pd.DataFrame      # smoothed P(state_t | all data)
    current_state: int
    current_label: str
    expected_duration: float      # days the current regime typically lasts
    log_likelihood: float


def _logsumexp(a: np.ndarray, axis: int | None = None):
    m = np.max(a, axis=axis, keepdims=True)
    out = m + np.log(np.sum(np.exp(a - m), axis=axis, keepdims=True))
    return float(out.reshape(-1)[0]) if axis is None else np.squeeze(out, axis=axis)


def fit_hmm(returns: pd.Series, n_states: int = 3, n_iter: int = 60,
            seed: int = 42) -> HmmResult:
    r = returns.dropna().values
    n = len(r)
    rng = np.random.default_rng(seed)

    # init: split by quantiles of |r| so states start vol-ordered
    q = np.quantile(np.abs(r), np.linspace(0, 1, n_states + 1))
    mu = np.zeros(n_states)
    sd = np.empty(n_states)
    for k in range(n_states):
        mask = (np.abs(r) >= q[k]) & (np.abs(r) <= q[k + 1])
        sd[k] = max(r[mask].std(), 1e-5) if mask.any() else r.std()
        mu[k] = r[mask].mean() if mask.any() else 0.0
    A = np.full((n_states, n_states), 0.05 / max(1, n_states - 1))
    np.fill_diagonal(A, 0.95)
    pi = np.full(n_states, 1 / n_states)

    ll_prev = -np.inf
    for _ in range(n_iter):
        logB = norm.logpdf(r[:, None], mu[None, :], sd[None, :])
        logA = np.log(A)
        # forward
        la = np.empty((n, n_states))
        la[0] = np.log(pi) + logB[0]
        for t in range(1, n):
            la[t] = logB[t] + _logsumexp(la[t - 1][:, None] + logA, axis=0)
        ll = float(_logsumexp(la[-1]))
        # backward
        lb = np.zeros((n, n_states))
        for t in range(n - 2, -1, -1):
            lb[t] = _logsumexp(logA + (logB[t + 1] + lb[t + 1])[None, :], axis=1)
        lgamma = la + lb - ll
        gamma = np.exp(lgamma)
        # transition expectations
        xi_num = np.zeros((n_states, n_states))
        for t in range(n - 1):
            m = la[t][:, None] + logA + (logB[t + 1] + lb[t + 1])[None, :] - ll
            xi_num += np.exp(m)
        # M-step
        pi = gamma[0] / gamma[0].sum()
        A = xi_num / np.maximum(xi_num.sum(axis=1, keepdims=True), 1e-300)
        w = gamma.sum(axis=0)
        mu = (gamma * r[:, None]).sum(axis=0) / w
        sd = np.sqrt((gamma * (r[:, None] - mu[None, :]) ** 2).sum(axis=0) / w)
        sd = np.maximum(sd, 1e-6)
        if abs(ll - ll_prev) < 1e-6 * max(1.0, abs(ll_prev)):
            break
        ll_prev = ll

    # sort states by vol so labels are stable
    order = np.argsort(sd)
    mu, sd = mu[order], sd[order]
    A = A[np.ix_(order, order)]
    gamma = gamma[:, order]

    labels = _LABELS3 if n_states == 3 else [f"state{i}" for i in range(n_states)]
    prob = pd.DataFrame(gamma, index=returns.dropna().index, columns=labels)
    cur = int(np.argmax(gamma[-1]))
    duration = 1.0 / max(1e-9, 1.0 - A[cur, cur])
    return HmmResult(n_states, mu, sd, A, prob, cur, labels[cur],
                     float(duration), ll)


@dataclass
class MacroRegime:
    score: float                  # [-1, 1]; positive = supportive for gold
    label: str
    components: dict = field(default_factory=dict)


def macro_regime(real10y: pd.Series | None, dxy_close: pd.Series | None,
                 vix: pd.Series | None) -> MacroRegime:
    """Heuristic macro score: falling real yields, weak dollar and elevated
    risk aversion are historically bullish gold."""
    comps = {}
    if real10y is not None and len(real10y) > 130:
        chg = real10y.iloc[-1] - real10y.iloc[-126]          # 6m change, pct-pts
        comps["real_yield_trend"] = float(np.clip(-chg / 0.75, -1, 1))
    if dxy_close is not None and len(dxy_close) > 130:
        chg = dxy_close.iloc[-1] / dxy_close.iloc[-126] - 1  # 6m return
        comps["dollar_trend"] = float(np.clip(-chg / 0.08, -1, 1))
    if vix is not None and len(vix) > 260:
        z = (vix.iloc[-21:].mean() - vix.iloc[-252:].mean()) / max(vix.iloc[-252:].std(), 1e-9)
        comps["risk_aversion"] = float(np.clip(z / 2, -1, 1))
    score = float(np.mean(list(comps.values()))) if comps else 0.0
    label = ("supportive" if score > 0.2
             else "hostile" if score < -0.2 else "neutral")
    return MacroRegime(score, label, comps)
