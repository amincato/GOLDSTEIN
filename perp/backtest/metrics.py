"""Per-(asset, leverage, exit-rule) statistics, compounded equity curves and
bootstrap risk of ruin."""
from __future__ import annotations

import numpy as np
import pandas as pd

RUIN_FRACTION = 0.10  # ruined = equity falls to <= 10% of start


def equity_curve(pnls: np.ndarray, start: float, stake_fraction: float) -> np.ndarray:
    eq = np.empty(len(pnls) + 1)
    eq[0] = start
    for i, r in enumerate(pnls):
        eq[i + 1] = eq[i] * (1.0 + stake_fraction * r)
        if eq[i + 1] <= 0:
            eq[i + 1 :] = 0.0
            return eq
    return eq


def max_drawdown(eq: np.ndarray) -> float:
    peak = np.maximum.accumulate(eq)
    with np.errstate(invalid="ignore", divide="ignore"):
        dd = 1.0 - eq / peak
    return float(np.nanmax(dd)) if len(eq) else np.nan


def risk_of_ruin(
    pnls: np.ndarray,
    stake_fraction: float,
    horizon: int = 50,
    n_boot: int = 5000,
    seed: int = 42,
) -> float:
    """P(equity ever <= RUIN_FRACTION * start within `horizon` trades),
    bootstrap-resampling the observed per-trade PnL distribution."""
    if len(pnls) == 0:
        return np.nan
    rng = np.random.default_rng(seed)
    draws = rng.choice(pnls, size=(n_boot, horizon), replace=True)
    ruined = 0
    for path in draws:
        eq = 1.0
        for r in path:
            eq *= 1.0 + stake_fraction * r
            if eq <= RUIN_FRACTION:
                ruined += 1
                break
    return ruined / n_boot


def summarize(trades: pd.DataFrame, start_capital: float = 500.0) -> dict:
    closed = trades[trades["status"].isin(["target", "stop", "liquidated"])]
    pnls = closed["pnl_margin"].to_numpy(dtype=float)
    wins = pnls[pnls > 0]
    losses = pnls[pnls <= 0]
    n = len(closed)
    out = {
        "signals": int(len(trades)),
        "trades": n,
        "skipped_overlap": int((trades["status"] == "skipped_overlap").sum()),
        "still_open": int((trades["status"] == "open").sum()),
        "win_rate": len(wins) / n if n else np.nan,
        "liq_rate": float((closed["status"] == "liquidated").mean()) if n else np.nan,
        "avg_win": float(wins.mean()) if len(wins) else np.nan,
        "avg_loss": float(losses.mean()) if len(losses) else np.nan,
        "expectancy": float(pnls.mean()) if n else np.nan,
        "profit_factor": float(wins.sum() / -losses.sum())
        if len(losses) and losses.sum() < 0
        else np.inf if len(wins) else np.nan,
        "median_hours": float(closed["hours"].median()) if n else np.nan,
    }
    for label, frac in (("full", 1.0), ("quarter", 0.25)):
        eq = equity_curve(pnls, start_capital, frac)
        out[f"final_equity_{label}"] = float(eq[-1])
        out[f"max_dd_{label}"] = max_drawdown(eq)
        out[f"ruin50_{label}"] = risk_of_ruin(pnls, frac)
    return out
