"""Daily-bar backtest engine with realistic leverage mechanics.

Models what actually differs between leveraged wrappers:
- financing cost on borrowed notional (rf + instrument spread), daily accrual
- expense ratio for ETPs
- transaction costs on turnover of target leverage
- daily-reset compounding for ETPs vs margin-account compounding
- margin liquidation: if equity/notional breaches maintenance margin the
  position is force-closed at that bar's close with an extra slippage haircut.

Leverage input is a target-leverage series decided with information available
at the PREVIOUS close (the engine shifts it by one bar to avoid lookahead).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from ..config import TRADING_DAYS, Instrument, Settings
from . import metrics as m


@dataclass
class BacktestResult:
    equity: pd.Series
    returns: pd.Series
    leverage: pd.Series
    stats: dict
    liquidations: list
    costs: dict


def run(
    prices: pd.Series,
    target_leverage: pd.Series | float,
    instrument: Instrument,
    settings: Settings | None = None,
    rf_series: pd.Series | None = None,
) -> BacktestResult:
    settings = settings or Settings()
    px = prices.dropna()
    asset_ret = px.pct_change().fillna(0.0)

    if np.isscalar(target_leverage):
        lev = pd.Series(float(target_leverage), index=px.index)
    else:
        lev = target_leverage.reindex(px.index).ffill().fillna(0.0)
    lev = lev.shift(1).fillna(0.0)                     # decide at t-1, hold at t

    rf_daily = (
        (rf_series.reindex(px.index).ffill() / 100.0 / TRADING_DAYS)
        if rf_series is not None
        else pd.Series(settings.risk_free / TRADING_DAYS, index=px.index)
    )

    n = len(px)
    equity = np.empty(n)
    equity[0] = 1.0
    strat_ret = np.zeros(n)
    liquidations: list[str] = []
    fin_cost_total = tc_total = fee_total = 0.0
    prev_lev = 0.0
    liquidation_slippage = 0.005

    for t in range(1, n):
        L = lev.iloc[t]
        r = asset_ret.iloc[t]
        rf_d = float(rf_daily.iloc[t])

        turnover = abs(L - prev_lev)
        tc = turnover * settings.transaction_cost
        borrow = max(L - 1.0, 0.0) * (rf_d + instrument.financing_spread / TRADING_DAYS)
        cash_yield = max(1.0 - L, 0.0) * rf_d          # uninvested cash earns rf
        fee = instrument.expense_ratio / TRADING_DAYS if instrument.expense_ratio else 0.0

        gross = L * r
        net = gross - borrow + cash_yield - tc - fee
        fin_cost_total += borrow
        tc_total += tc
        fee_total += fee

        # margin liquidation check (close-to-close approximation)
        if instrument.maintenance_margin > 0 and L > 1.0:
            eq_ratio = (1.0 + net) / L                 # equity per unit notional
            if eq_ratio < instrument.maintenance_margin:
                net -= liquidation_slippage * L
                liquidations.append(str(px.index[t].date()))
                L = 0.0                                # flat after forced close

        strat_ret[t] = net
        equity[t] = equity[t - 1] * (1.0 + net)
        if equity[t] <= 0:                             # wiped out
            equity[t:] = max(equity[t], 0.0)
            strat_ret[t + 1:] = 0.0
            liquidations.append(f"{px.index[t].date()} (RUIN)")
            break
        prev_lev = L

    eq = pd.Series(equity, index=px.index)
    rets = pd.Series(strat_ret, index=px.index)
    return BacktestResult(
        equity=eq,
        returns=rets,
        leverage=lev,
        stats=m.summarize(rets, rf=settings.risk_free),
        liquidations=liquidations,
        costs={
            "financing": fin_cost_total,
            "transaction": tc_total,
            "fees": fee_total,
        },
    )


def vol_target_leverage(prices: pd.Series, settings: Settings,
                        signal: pd.Series | None = None,
                        span: int = 33) -> pd.Series:
    """Classic vol-targeting rule as a point-in-time series, optionally
    scaled by a [-1,1] signal (negative = short)."""
    rets = prices.pct_change()
    ewma = rets.ewm(span=span).std() * np.sqrt(TRADING_DAYS)
    lev = (settings.target_vol / ewma).clip(upper=settings.max_leverage)
    if signal is not None:
        lev = lev * signal.reindex(lev.index).ffill().fillna(0.0)
    return lev.fillna(0.0)
