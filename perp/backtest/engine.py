"""Candle-by-candle trade simulator with leverage, liquidation, fees,
hourly borrow and conservative fills. See SIGNAL_SPEC.md for the exact
ordering of same-candle events (liquidation → stop → target)."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class CostParams:
    taker_fee: float = 0.0006          # per side, on notional
    borrow_rate_hourly: float = 0.00005  # 0.005%/h on notional
    slippage: float = 0.001            # stop-loss fill slippage


@dataclass
class ExitRule:
    kind: str            # "fixed" | "atr"
    tp: float = 0.02     # price move fraction (fixed) or ATR multiple (atr)
    sl: float = 0.01

    @property
    def name(self) -> str:
        return f"{self.kind}_tp{self.tp:g}_sl{self.sl:g}"


MAINT_FRACTION = 0.9  # liq at entry * (1 -/+ 0.9/L)


def simulate_trades(
    df1h: pd.DataFrame,
    signals: pd.DataFrame,
    leverage: float,
    exit_rule: ExitRule,
    costs: CostParams,
) -> pd.DataFrame:
    """One position per asset at a time: signals arriving while a trade is
    open are marked skipped_overlap and not traded. PnL is % on margin,
    floored at -100% (isolated margin: you cannot lose more than the stake).
    """
    high = df1h["high"].to_numpy()
    low = df1h["low"].to_numpy()
    n = len(df1h)
    rows = []
    busy_until = -1
    for sig in signals.itertuples(index=False):
        t = int(sig.t_index)
        if t <= busy_until:
            rows.append(_row(sig, leverage, status="skipped_overlap"))
            continue
        side, entry = int(sig.side), float(sig.entry)
        if exit_rule.kind == "fixed":
            tp_px = entry * (1 + side * exit_rule.tp)
            sl_px = entry * (1 - side * exit_rule.sl)
        else:
            tp_px = entry + side * exit_rule.tp * float(sig.atr)
            sl_px = entry - side * exit_rule.sl * float(sig.atr)
        liq_px = entry * (1 - side * MAINT_FRACTION / leverage)

        status, exit_px, exit_i = "open", np.nan, n - 1
        for i in range(t + 1, n):
            if side == 1:
                if low[i] <= liq_px:
                    status, exit_px, exit_i = "liquidated", liq_px, i
                elif low[i] <= sl_px:
                    status, exit_px, exit_i = "stop", sl_px * (1 - costs.slippage), i
                elif high[i] >= tp_px:
                    status, exit_px, exit_i = "target", tp_px, i
            else:
                if high[i] >= liq_px:
                    status, exit_px, exit_i = "liquidated", liq_px, i
                elif high[i] >= sl_px:
                    status, exit_px, exit_i = "stop", sl_px * (1 + costs.slippage), i
                elif low[i] <= tp_px:
                    status, exit_px, exit_i = "target", tp_px, i
            if status != "open":
                break
        hours = exit_i - t
        if status == "liquidated":
            pnl = -1.0
        else:
            gross = side * (exit_px / entry - 1.0) if status != "open" else np.nan
            if status == "open":
                pnl = np.nan
            else:
                pnl = leverage * (
                    gross
                    - 2 * costs.taker_fee
                    - costs.borrow_rate_hourly * hours
                )
                pnl = max(pnl, -1.0)
        busy_until = exit_i
        rows.append(
            _row(
                sig,
                leverage,
                status=status,
                exit_price=float(exit_px) if np.isfinite(exit_px) else np.nan,
                exit_time=df1h.index[exit_i],
                hours=hours,
                pnl_margin=pnl,
                tp_px=tp_px,
                sl_px=sl_px,
                liq_px=liq_px,
            )
        )
    return pd.DataFrame(rows)


def _row(sig, leverage, **kw) -> dict:
    base = {
        "time": sig.time,
        "side": int(sig.side),
        "entry": float(sig.entry),
        "leverage": leverage,
        "sr_ok": bool(sig.sr_ok),
        "status": None,
        "exit_price": np.nan,
        "exit_time": pd.NaT,
        "hours": np.nan,
        "pnl_margin": np.nan,
        "tp_px": np.nan,
        "sl_px": np.nan,
        "liq_px": np.nan,
    }
    base.update(kw)
    return base
