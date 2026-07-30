"""Trade-level intraday backtest engine.

This is deliberately NOT a bar-return engine: scalping economics only make
sense at the level of individual trades with entry, stop, target and costs
in ticks. Mechanics:

- A signal at bar t fills at bar t+1's open plus half-spread (+ slippage on
  entry is folded into the spread cost).
- Each subsequent bar is checked against stop and target; if BOTH are inside
  the bar's range the STOP is assumed to fill first (conservative).
- Stops fill with extra adverse slippage (stop_slippage_ticks).
- Any open trade is flattened at the last bar of its session (no overnight).
- One position at a time, max trades/day, and a daily loss limit in R that
  halts trading for the rest of the day — standard scalper risk hygiene.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from .contracts import CostModel, FuturesContract


@dataclass
class RiskRules:
    risk_per_trade: float = 0.005      # fraction of capital risked per trade
    max_trades_per_day: int = 6
    daily_loss_limit_r: float = 3.0    # stop trading after losing this many R
    capital: float = 25_000.0


@dataclass
class Trade:
    entry_time: pd.Timestamp
    exit_time: pd.Timestamp
    direction: int                     # +1 long, -1 short
    entry_px: float
    exit_px: float
    stop_ticks: float
    contracts: int
    gross_ticks: float
    net_ticks: float
    r_multiple: float
    pnl_dollars: float
    exit_reason: str                   # target / stop / eod
    session: str


@dataclass
class ScalpResult:
    trades: list[Trade]
    stats: dict
    daily_pnl: pd.Series
    equity: pd.Series = field(default=None)


def run(bars: pd.DataFrame, signals: pd.DataFrame, contract: FuturesContract,
        costs: CostModel, risk: RiskRules | None = None) -> ScalpResult:
    """bars: OHLCV (+ session/date from add_features).
    signals: DataFrame indexed like bars with columns
      dir (+1/-1/0), stop_ticks (>0), target_ticks (>0) — signal on bar close.
    """
    risk = risk or RiskRules()
    tick = contract.tick_size
    idx = bars.index
    o = bars["open"].values
    h = bars["high"].values
    l = bars["low"].values
    sess = bars["session"].values
    dates = bars["date"].values

    sig_dir = signals["dir"].reindex(idx).fillna(0).values
    sig_stop = signals["stop_ticks"].reindex(idx).ffill().fillna(0).values
    sig_tgt = signals["target_ticks"].reindex(idx).ffill().fillna(0).values

    trades: list[Trade] = []
    day_r = {}
    day_trades = {}
    t = 0
    n = len(idx)
    while t < n - 1:
        d = sig_dir[t]
        if d == 0 or sig_stop[t] <= 0:
            t += 1
            continue
        day = dates[t + 1]
        if day_trades.get(day, 0) >= risk.max_trades_per_day \
                or day_r.get(day, 0.0) <= -risk.daily_loss_limit_r:
            t += 1
            continue

        stop_ticks = float(sig_stop[t])
        target_ticks = float(sig_tgt[t])
        entry = o[t + 1] + d * (costs.spread_ticks / 2) * tick
        stop_px = entry - d * stop_ticks * tick
        target_px = entry + d * target_ticks * tick
        contracts_n = max(int(risk.capital * risk.risk_per_trade
                              / max(stop_ticks * contract.tick_value, 1e-9)), 1)

        exit_px, exit_reason, exit_i = None, "eod", t + 1
        for j in range(t + 1, n):
            if dates[j] != day or sess[j] != sess[t + 1]:
                # session ended on the previous bar -> flat at its close
                exit_i = j - 1
                exit_px = bars["close"].values[exit_i]
                exit_reason = "eod"
                break
            hit_stop = l[j] <= stop_px if d > 0 else h[j] >= stop_px
            hit_tgt = h[j] >= target_px if d > 0 else l[j] <= target_px
            if hit_stop:                       # conservative: stop wins ties
                exit_px = stop_px - d * costs.stop_slippage_ticks * tick
                exit_reason, exit_i = "stop", j
                break
            if hit_tgt:
                exit_px = target_px
                exit_reason, exit_i = "target", j
                break
        else:
            exit_i = n - 1
            exit_px = bars["close"].values[exit_i]

        gross_ticks = d * (exit_px - entry) / tick
        net_ticks = gross_ticks - costs.base_round_trip
        r_mult = net_ticks / stop_ticks
        pnl = net_ticks * contract.tick_value * contracts_n
        trades.append(Trade(idx[t + 1], idx[exit_i], int(d), float(entry),
                            float(exit_px), stop_ticks, contracts_n,
                            float(gross_ticks), float(net_ticks), float(r_mult),
                            float(pnl), exit_reason, str(sess[t + 1])))
        day_r[day] = day_r.get(day, 0.0) + r_mult
        day_trades[day] = day_trades.get(day, 0) + 1
        t = exit_i + 1                          # one position at a time

    return _summarize(trades, bars, risk)


def _summarize(trades: list[Trade], bars: pd.DataFrame,
               risk: RiskRules) -> ScalpResult:
    if not trades:
        empty = pd.Series(dtype=float)
        return ScalpResult(trades, {"n_trades": 0}, empty, empty)
    df = pd.DataFrame([t.__dict__ for t in trades])
    daily = df.groupby(df["entry_time"].dt.normalize())["pnl_dollars"].sum()
    n_days = max(bars["date"].nunique(), 1)
    equity = risk.capital + daily.cumsum()
    dd = equity / equity.cummax() - 1
    wins = df[df["net_ticks"] > 0]
    losses = df[df["net_ticks"] <= 0]
    gross_win = wins["pnl_dollars"].sum()
    gross_loss = -losses["pnl_dollars"].sum()
    sharpe_d = daily.mean() / daily.std() * np.sqrt(252) if daily.std() > 0 else 0.0

    streak, worst_streak = 0, 0
    for x in df["net_ticks"]:
        streak = streak + 1 if x <= 0 else 0
        worst_streak = max(worst_streak, streak)

    stats = {
        "n_trades": len(df),
        "trades_per_day": len(df) / n_days,
        "win_rate": len(wins) / len(df),
        "profit_factor": float(gross_win / gross_loss) if gross_loss > 0 else np.inf,
        "expectancy_ticks": float(df["net_ticks"].mean()),
        "expectancy_r": float(df["r_multiple"].mean()),
        "avg_win_ticks": float(wins["net_ticks"].mean()) if len(wins) else 0.0,
        "avg_loss_ticks": float(losses["net_ticks"].mean()) if len(losses) else 0.0,
        "total_pnl": float(df["pnl_dollars"].sum()),
        "return_on_capital": float(df["pnl_dollars"].sum() / risk.capital),
        "daily_sharpe_ann": float(sharpe_d),
        "max_drawdown": float(dd.min()),
        "max_consecutive_losses": int(worst_streak),
        "exit_mix": df["exit_reason"].value_counts(normalize=True).round(3).to_dict(),
        "by_session": df.groupby("session")["net_ticks"].agg(["count", "mean"])
                        .round(2).to_dict(orient="index"),
    }
    return ScalpResult(trades, stats, daily, equity)
