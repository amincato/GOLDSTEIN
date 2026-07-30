"""Historical & parametric stress testing for leveraged gold positions.

Scenario returns are the actual (approximate) gold spot drawdown paths from
the worst episodes of the last two decades, replayed against the current
position at its recommended leverage. This answers the only question that
matters before levering: "would I have survived?".
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from ..config import Instrument

# name -> (description, list of daily returns)
HISTORICAL_SCENARIOS: dict[str, tuple[str, list[float]]] = {
    "gfc_2008_liquidation": (
        "Oct 2008: gold sold in the everything-liquidation, -18% in 3 weeks",
        [-0.030, -0.045, 0.010, -0.060, -0.025, 0.015, -0.040, -0.020],
    ),
    "april_2013_crash": (
        "Apr 12-15 2013: worst 2-day gold crash in 30 years (-13.5%)",
        [-0.052, -0.091],
    ),
    "taper_2013_grind": (
        "2013 taper year: slow grind, -28% over the year (compressed sample)",
        [-0.012] * 10 + [-0.025, -0.008, -0.015, -0.020, -0.010],
    ),
    "covid_2020_margin_cascade": (
        "Mar 2020: gold dumped for margin cash, -12% in 9 sessions",
        [-0.010, -0.036, 0.007, -0.047, -0.021, 0.013, -0.019, -0.005, -0.012],
    ),
    "rate_shock_2022": (
        "Mar-Sep 2022: real-yield surge, -20% over 6 months (compressed)",
        [-0.010] * 8 + [-0.018, -0.014, -0.022, -0.008, -0.016],
    ),
}

PARAMETRIC_GAPS = [-0.03, -0.05, -0.08, -0.12, -0.20]


@dataclass
class StressResult:
    table: pd.DataFrame
    survives_all_historical: bool
    worst_scenario: str
    worst_equity_impact: float


def run(leverage: float, instrument: Instrument, capital: float = 10_000.0) -> StressResult:
    rows = []

    for name, (desc, path) in HISTORICAL_SCENARIOS.items():
        equity = 1.0
        liquidated = False
        for r in path:
            net = leverage * r
            equity *= 1.0 + net
            if instrument.maintenance_margin > 0 and leverage > 1:
                if (1.0 + net) < leverage * instrument.maintenance_margin:
                    liquidated = True
            if equity <= 0:
                equity = 0.0
                liquidated = True
                break
        rows.append(
            {
                "scenario": name,
                "type": "historical",
                "description": desc,
                "asset_move": float(np.prod([1 + r for r in path]) - 1),
                "equity_multiple": round(equity, 4),
                "pnl": round(capital * (equity - 1.0), 2),
                "margin_liquidation": liquidated,
            }
        )

    for gap in PARAMETRIC_GAPS:
        net = leverage * gap
        equity = max(1.0 + net, 0.0)
        liq = (
            instrument.maintenance_margin > 0
            and leverage > 1
            and (1.0 + net) < leverage * instrument.maintenance_margin
        ) or equity <= 0
        rows.append(
            {
                "scenario": f"overnight_gap_{abs(gap):.0%}",
                "type": "parametric",
                "description": f"Single overnight gap of {gap:.0%} (no chance to exit)",
                "asset_move": gap,
                "equity_multiple": round(equity, 4),
                "pnl": round(capital * (equity - 1.0), 2),
                "margin_liquidation": bool(liq),
            }
        )

    df = pd.DataFrame(rows)
    hist = df[df["type"] == "historical"]
    survives = bool(~hist["margin_liquidation"].any() and (hist["equity_multiple"] > 0.5).all())
    worst_idx = df["equity_multiple"].idxmin()
    return StressResult(
        table=df,
        survives_all_historical=survives,
        worst_scenario=str(df.loc[worst_idx, "scenario"]),
        worst_equity_impact=float(df["equity_multiple"].min() - 1.0),
    )


def max_safe_leverage_for_gap(gap: float, instrument: Instrument,
                              max_equity_loss: float = 0.5) -> float:
    """Largest leverage such that a single `gap` move neither breaches
    maintenance margin nor loses more than `max_equity_loss` of equity."""
    loss_cap = max_equity_loss / abs(gap)
    if instrument.maintenance_margin > 0:
        margin_cap = 1.0 / (instrument.maintenance_margin - gap) if instrument.maintenance_margin > gap else np.inf
        # equity/notional after move: (1 + L*gap)/L >= mm  =>  L <= 1/(mm - gap)
        return float(min(loss_cap, margin_cap))
    return float(loss_cap)
