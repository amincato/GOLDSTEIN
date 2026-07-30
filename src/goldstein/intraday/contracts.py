"""Contract specifications and cost model for intraday gold scalping.

Scalping P&L lives and dies on microcosts, so they are first-class here:
every backtest charges spread + commission + slippage in ticks per round
trip, and validation reports how the edge degrades as costs rise.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FuturesContract:
    key: str
    label: str
    tick_size: float          # price increment
    tick_value: float         # $ per tick per contract
    typical_spread_ticks: float
    commission_per_side: float  # $ per contract per side
    intraday_margin: float    # $ per contract (broker-typical, not exchange min)

    @property
    def point_value(self) -> float:
        return self.tick_value / self.tick_size

    def commission_ticks(self) -> float:
        """Round-trip commission expressed in ticks."""
        return 2.0 * self.commission_per_side / self.tick_value


CONTRACTS: dict[str, FuturesContract] = {
    c.key: c
    for c in [
        FuturesContract("MGC", "Micro Gold futures (COMEX)", 0.10, 1.00, 1.5, 0.60, 1200.0),
        FuturesContract("GC", "Gold futures (COMEX)", 0.10, 10.00, 1.0, 1.50, 12000.0),
    ]
}


@dataclass
class CostModel:
    """Per-round-trip cost in ticks: half-spread paid at each side, plus
    commissions, plus stochastic-execution slippage on stops."""

    spread_ticks: float
    commission_ticks: float
    stop_slippage_ticks: float = 1.0   # extra adverse ticks when a stop fills

    @property
    def base_round_trip(self) -> float:
        return self.spread_ticks + self.commission_ticks

    @classmethod
    def for_contract(cls, c: FuturesContract, spread_override: float | None = None):
        return cls(
            spread_ticks=spread_override if spread_override is not None
            else c.typical_spread_ticks,
            commission_ticks=c.commission_ticks(),
        )
