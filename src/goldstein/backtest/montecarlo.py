"""Monte Carlo risk engine: stationary block bootstrap of historical returns.

Block bootstrap (Politis–Romano) preserves volatility clustering, which is
exactly what kills leveraged positions — an iid bootstrap would materially
understate drawdown and ruin risk.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from ..config import TRADING_DAYS, Instrument, Settings


@dataclass
class MonteCarloResult:
    leverage: float
    horizon_days: int
    paths: int
    terminal_wealth_pctiles: dict     # {5: ..., 25: ..., 50: ..., 75: ..., 95: ...}
    prob_loss: float                  # P(terminal < 1)
    prob_dd_25: float                 # P(max drawdown worse than -25%)
    prob_dd_50: float
    prob_ruin: float                  # P(equity <= 10% or margin wipeout)
    expected_max_drawdown: float
    median_log_growth: float


def _stationary_bootstrap(r: np.ndarray, n_out: int, n_paths: int,
                          mean_block: float, rng: np.random.Generator) -> np.ndarray:
    """Sample paths via stationary bootstrap with geometric block lengths."""
    n = len(r)
    p = 1.0 / mean_block
    idx = np.empty((n_paths, n_out), dtype=np.int64)
    start = rng.integers(0, n, size=n_paths)
    idx[:, 0] = start
    restart = rng.random((n_paths, n_out)) < p
    steps = rng.integers(0, n, size=(n_paths, n_out))
    for t in range(1, n_out):
        cont = (idx[:, t - 1] + 1) % n
        idx[:, t] = np.where(restart[:, t], steps[:, t], cont)
    return r[idx]


def run(
    returns: pd.Series,
    leverage: float,
    instrument: Instrument,
    settings: Settings | None = None,
    horizon_days: int | None = None,
) -> MonteCarloResult:
    settings = settings or Settings()
    horizon = horizon_days or settings.mc_horizon_days
    rng = np.random.default_rng(settings.seed)
    r = returns.dropna().values
    paths = _stationary_bootstrap(r, horizon, settings.mc_paths, 20.0, rng)

    borrow_d = max(leverage - 1.0, 0.0) * (
        settings.risk_free + instrument.financing_spread
    ) / TRADING_DAYS
    fee_d = instrument.expense_ratio / TRADING_DAYS
    net = leverage * paths - borrow_d - fee_d

    growth = np.cumprod(1.0 + net, axis=1)
    # margin wipeout: equity per notional below maintenance at any point
    if instrument.maintenance_margin > 0 and leverage > 1:
        wipe = (1.0 + net < leverage * instrument.maintenance_margin).any(axis=1)
    else:
        wipe = np.zeros(len(net), dtype=bool)
    floor = np.minimum.accumulate(growth / np.maximum.accumulate(growth, axis=1), axis=1)
    max_dd = floor.min(axis=1) - 1.0
    terminal = growth[:, -1]
    terminal[wipe] = np.minimum(terminal[wipe], 0.05)

    ruin = (terminal <= 0.10) | wipe
    pct = {q: float(np.percentile(terminal, q)) for q in (5, 25, 50, 75, 95)}
    med_growth = float(np.log(max(np.median(terminal), 1e-9)) / (horizon / TRADING_DAYS))
    return MonteCarloResult(
        leverage=leverage,
        horizon_days=horizon,
        paths=settings.mc_paths,
        terminal_wealth_pctiles=pct,
        prob_loss=float((terminal < 1.0).mean()),
        prob_dd_25=float((max_dd < -0.25).mean()),
        prob_dd_50=float((max_dd < -0.50).mean()),
        prob_ruin=float(ruin.mean()),
        expected_max_drawdown=float(max_dd.mean()),
        median_log_growth=med_growth,
    )


def leverage_sweep(returns: pd.Series, instrument: Instrument,
                   settings: Settings | None = None,
                   leverages=(0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0)) -> pd.DataFrame:
    """Risk profile across leverage levels — the empirical Kelly curve."""
    rows = []
    for L in leverages:
        mc = run(returns, L, instrument, settings)
        rows.append(
            {
                "leverage": L,
                "median_terminal": mc.terminal_wealth_pctiles[50],
                "p5_terminal": mc.terminal_wealth_pctiles[5],
                "median_log_growth": mc.median_log_growth,
                "prob_loss": mc.prob_loss,
                "prob_dd_50": mc.prob_dd_50,
                "prob_ruin": mc.prob_ruin,
                "expected_max_dd": mc.expected_max_drawdown,
            }
        )
    return pd.DataFrame(rows)
