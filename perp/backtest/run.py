"""In-sample optimization + out-of-sample evaluation.

Discipline:
- parameters (N, X, K, exit rule) are chosen ONLY on data before 2025-01-01;
- 2025+ is touched exactly once, with the chosen parameters, and reported
  separately;
- signals are point-in-time, so computing indicators with pre-2025 warm-up
  history for early-2025 candles is not leakage.

Run:  python -m perp.backtest.run
"""
from __future__ import annotations

import itertools
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from ..data.fetch import SYMBOLS, load_ohlcv
from .engine import CostParams, ExitRule, simulate_trades
from .metrics import summarize
from .signals import SignalParams, find_signals

REPORT_DIR = Path(__file__).resolve().parents[1] / "reports"
OOS_START = pd.Timestamp("2025-01-01", tz="UTC")
LEVERAGES = [10, 20, 30, 50, 100]
OPT_LEVERAGE = 30          # reference leverage used for parameter selection
MIN_TRADES_IS = 25         # combos with fewer in-sample trades are discarded

GRID = {
    "div_lookback": [20, 30, 40],
    "sr_tolerance": [0.003, 0.005, 0.01],
    "sr_pivot_k": [3, 5, 7],
}
EXITS = [
    ExitRule("fixed", 0.02, 0.01),
    ExitRule("fixed", 0.03, 0.015),
    ExitRule("atr", 2.0, 1.0),
]


def signal_sets(df1h, df4h):
    """Yield (combo, signals) once per grid point, S/R filter ON (the
    strategy as specified; the OFF variant is reported separately for the
    chosen parameters only)."""
    for n, x, k in itertools.product(
        GRID["div_lookback"], GRID["sr_tolerance"], GRID["sr_pivot_k"]
    ):
        params = SignalParams(div_lookback=n, sr_tolerance=x, sr_pivot_k=k)
        yield params, find_signals(df1h, df4h, params)


def run_asset(symbol: str, costs: CostParams) -> dict:
    df1h = load_ohlcv(symbol, "1h")
    df4h = load_ohlcv(symbol, "4h")
    is1h = df1h[df1h.index < OOS_START]
    is4h = df4h[df4h.index < OOS_START]

    # ---- in-sample grid search (S/R filter ON) --------------------------
    best, results_is = None, []
    for params, sigs in signal_sets(is1h, is4h):
        for exit_rule in EXITS:
            trades = simulate_trades(is1h, sigs, OPT_LEVERAGE, exit_rule, costs)
            s = summarize(trades)
            rec = {
                "params": params.to_dict(),
                "exit": exit_rule.name,
                **{k: s[k] for k in ("trades", "win_rate", "liq_rate", "expectancy", "profit_factor")},
            }
            results_is.append(rec)
            if s["trades"] >= MIN_TRADES_IS and (
                best is None or s["expectancy"] > best["expectancy"]
            ):
                best = {**rec, "exit_rule": exit_rule, "params_obj": params, "expectancy": s["expectancy"]}
    if best is None:
        return {"symbol": symbol, "error": f"no combo reached {MIN_TRADES_IS} in-sample trades"}

    # ---- evaluation with frozen parameters ------------------------------
    chosen = best["params_obj"]
    out = {
        "symbol": symbol,
        "chosen_params": chosen.to_dict(),
        "chosen_exit": best["exit"],
        "grid_results_is": results_is,
        "tables": [],
        "entry_lag_comparison": [],
    }
    for sr_on in (True, False):
        params_v = SignalParams(**{**chosen.to_dict(), "require_sr": sr_on})
        sigs_full = find_signals(df1h, df4h, params_v)
        for period, frame in (("IS", is1h), ("OOS", df1h)):
            mask = (
                sigs_full["time"] < OOS_START
                if period == "IS"
                else sigs_full["time"] >= OOS_START
            )
            subset = sigs_full[mask].reset_index(drop=True)
            for lev in LEVERAGES:
                trades = simulate_trades(frame, subset, lev, best["exit_rule"], costs)
                out["tables"].append(
                    {
                        "period": period,
                        "sr_filter": sr_on,
                        "leverage": lev,
                        **summarize(trades),
                    }
                )
    # sensitivity: same params, alternative entry modes
    for mode in ("close", "pivot"):
        alt = SignalParams(**{**chosen.to_dict(), "entry_mode": mode})
        sigs_alt = find_signals(df1h, df4h, alt)
        for period, frame in (("IS", is1h), ("OOS", df1h)):
            mask = (
                sigs_alt["time"] < OOS_START
                if period == "IS"
                else sigs_alt["time"] >= OOS_START
            )
            trades = simulate_trades(
                frame, sigs_alt[mask].reset_index(drop=True), OPT_LEVERAGE,
                best["exit_rule"], costs,
            )
            out["entry_lag_comparison"].append(
                {"mode": mode, "period": period, "leverage": OPT_LEVERAGE, **summarize(trades)}
            )
    return out


def render_markdown(all_results: list[dict], stamp: str) -> str:
    lines = [
        f"# Perp strategy backtest — {stamp}",
        "",
        "Parameters tuned on pre-2025 data only; OOS = 2025+. PnL is % on",
        "margin after taker fees (0.06%/side), hourly borrow (0.005%/h) and",
        "0.1% stop slippage. ruin50 = P(equity ≤ 10% of start within 50",
        "trades), bootstrap. full = 100% of sub-account per trade,",
        "quarter = 25% per trade, start $500.",
        "",
    ]
    cols = [
        "leverage", "trades", "still_open", "win_rate", "liq_rate", "avg_win",
        "avg_loss", "expectancy", "profit_factor", "max_dd_full",
        "final_equity_full", "ruin50_full", "final_equity_quarter", "ruin50_quarter",
    ]
    for res in all_results:
        lines.append(f"## {res['symbol']}")
        if "error" in res:
            lines += [f"**{res['error']}**", ""]
            continue
        lines.append(
            f"Chosen (IS only): N={res['chosen_params']['div_lookback']}, "
            f"X={res['chosen_params']['sr_tolerance']:.3%}, "
            f"K={res['chosen_params']['sr_pivot_k']}, exit={res['chosen_exit']}"
        )
        df = pd.DataFrame(res["tables"])
        for period in ("IS", "OOS"):
            for sr_on in (True, False):
                sub = df[(df["period"] == period) & (df["sr_filter"] == sr_on)]
                title = f"### {period} — S/R filter {'ON' if sr_on else 'OFF'}"
                lines += ["", title, "", sub[cols].to_markdown(index=False, floatfmt=".3f")]
        lag = pd.DataFrame(res["entry_lag_comparison"])
        lines += [
            "",
            f"### Entry-mode sensitivity @ {OPT_LEVERAGE}x, S/R ON "
            "(close = enter at the divergence candle, pivot = 3h-lagged fractal)",
            "",
            lag[["mode", "period"] + cols].to_markdown(index=False, floatfmt=".3f"),
            "",
        ]
    return "\n".join(lines)


def main() -> int:
    costs = CostParams()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M")
    all_results = [run_asset(sym, costs) for sym in SYMBOLS]
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    md = render_markdown(all_results, stamp)
    (REPORT_DIR / f"backtest_{stamp}.md").write_text(md)
    (REPORT_DIR / f"backtest_{stamp}.json").write_text(
        json.dumps(all_results, indent=2, default=str)
    )
    print(md)
    print(f"\nSaved to {REPORT_DIR}/backtest_{stamp}.md/.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
