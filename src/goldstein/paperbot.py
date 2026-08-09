"""Autonomous PAPER trading bot for Hyperliquid perps.

The first rung of the ladder toward any live bot: identical decision logic,
real market prices, real fee/funding accounting — but virtual capital. The
daily CI runs it and commits the state, so the equity curve is a tamper-proof
track record (every decision is committed BEFORE the next price is known).

Strategy (deliberately the only family with documented positive expectation
for a small account, at low leverage):
  - Universe: most liquid HL perps by daily notional volume (+ any gold perp)
  - Signal per asset: multi-horizon time-series momentum (7d/48h/12h) blended
    and tanh-squashed, plus a carry tilt — positions that RECEIVE funding are
    preferred, positions that pay it are penalized
  - Sizing: per-asset vol targeting (annualized), portfolio gross leverage
    hard-capped at MAX_GROSS (default 2x — not 50x, on purpose)
  - Rebalance: once per run (daily CI), full close/reopen semantics with
    taker fees charged on all turnover; funding accrued on held positions
  - Kill switch: if equity < 60% of initial, the bot goes flat and stays flat

Ladder: paper (this) → Hyperliquid TESTNET (real order API, fake funds;
needs a testnet API wallet) → real capital only on explicit user setup of
keys, never by default. This module NEVER signs or sends orders.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from .config import CACHE_DIR, REPORT_DIR
from .intraday import hyperliquid as hl

log = logging.getLogger("goldstein.paperbot")

STATE_PATH = CACHE_DIR.parent / "paperbot" / "state.json"
HISTORY_PATH = REPORT_DIR / "paperbot_history.csv"
REPORT_MD = REPORT_DIR / "paperbot_latest.md"

INITIAL_CAPITAL = 10_000.0
MAX_GROSS = 2.0
PER_ASSET_VOL_TARGET = 0.20         # annualized per-position vol target
MAX_ASSETS = 6
TAKER_FEE = 0.00045
KILL_SWITCH_EQUITY = 0.60           # go flat below 60% of initial
_HOURS_YEAR = 24 * 365


# ------------------------------------------------------------------- market
def fetch_universe() -> list[dict]:
    """Most liquid perps + any gold perp: [{coin, mark_px, funding_hourly}]."""
    meta, ctxs = hl._post({"type": "metaAndAssetCtxs"})
    rows = []
    for asset, ctx in zip(meta["universe"], ctxs):
        if asset.get("isDelisted"):
            continue
        try:
            rows.append({
                "coin": asset["name"],
                "mark_px": float(ctx["markPx"]),
                "funding_hourly": float(ctx.get("funding", 0.0)),
                "day_volume": float(ctx.get("dayNtlVlm", 0.0)),
            })
        except (KeyError, TypeError, ValueError):
            continue
    rows.sort(key=lambda r: -r["day_volume"])
    top = rows[:MAX_ASSETS]
    for r in rows[MAX_ASSETS:]:
        if hl._is_goldish(r["coin"]) and len(top) < MAX_ASSETS + 1:
            top.append(r)
    return top


def compute_target_weights(candles: dict[str, pd.DataFrame],
                           funding: dict[str, float]) -> dict[str, float]:
    """Signed target weights (fraction of equity per asset), gross-capped."""
    weights = {}
    for coin, df in candles.items():
        if df is None or len(df) < 24 * 10:
            continue
        px = df["close"]
        rets = np.log(px / px.shift(1)).dropna()
        vol_ann = float(rets.std() * np.sqrt(_HOURS_YEAR))
        if not np.isfinite(vol_ann) or vol_ann < 1e-4:
            continue
        mom = (0.5 * np.tanh((px.iloc[-1] / px.iloc[-24 * 7] - 1) / 0.10)
               + 0.3 * np.tanh((px.iloc[-1] / px.iloc[-48] - 1) / 0.05)
               + 0.2 * np.tanh((px.iloc[-1] / px.iloc[-12] - 1) / 0.03))
        # carry tilt: positive funding favors shorts (they receive it)
        carry_apr = funding.get(coin, 0.0) * _HOURS_YEAR
        tilt = float(np.clip(-carry_apr / 0.20, -0.3, 0.3))
        score = float(np.clip(mom + tilt, -1.0, 1.0))
        if abs(score) < 0.15:                      # no conviction -> no position
            continue
        weights[coin] = score * (PER_ASSET_VOL_TARGET / vol_ann)

    gross = sum(abs(w) for w in weights.values())
    if gross > MAX_GROSS:
        weights = {c: w * MAX_GROSS / gross for c, w in weights.items()}
    return weights


# -------------------------------------------------------------------- state
def _load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {"initial_capital": INITIAL_CAPITAL, "cash": INITIAL_CAPITAL,
            "positions": {}, "last_run": None, "halted": False}


def _save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2, default=str))


def mark_to_market(state: dict, prices: dict[str, float]) -> float:
    """Cash (realized PnL, fees, funding) + unrealized PnL of open perps."""
    return float(state["cash"] + sum(
        pos["sz"] * (prices.get(coin, pos["entry_px"]) - pos["entry_px"])
        for coin, pos in state["positions"].items()
    ))


def run_cycle(now: datetime | None = None) -> dict:
    """One decision cycle: mark, accrue funding, rebalance, persist, report."""
    now = now or datetime.now(timezone.utc)
    state = _load_state()
    market = fetch_universe()
    prices = {r["coin"]: r["mark_px"] for r in market}
    funding = {r["coin"]: r["funding_hourly"] for r in market}

    actions: list[str] = []

    # funding accrual on held positions since last run (approx: current rate)
    if state["last_run"]:
        hours = max((now - datetime.fromisoformat(state["last_run"])).total_seconds() / 3600, 0)
        for coin, pos in state["positions"].items():
            px = prices.get(coin, pos["entry_px"])
            notional = pos["sz"] * px
            paid = funding.get(coin, 0.0) * hours * notional   # longs pay +funding
            if paid:
                state["cash"] -= paid
                actions.append(f"funding {coin}: {-paid:+.2f}$ ({hours:.0f}h)")

    equity = mark_to_market(state, prices)

    # kill switch
    if equity < KILL_SWITCH_EQUITY * state["initial_capital"]:
        state["halted"] = True
    if state["halted"]:
        for coin, pos in list(state["positions"].items()):
            px = prices.get(coin, pos["entry_px"])
            state["cash"] += pos["sz"] * (px - pos["entry_px"])
            state["cash"] -= abs(pos["sz"] * px) * TAKER_FEE
            del state["positions"][coin]
            actions.append(f"KILL-SWITCH flat {coin}")
        equity = state["cash"]
        targets = {}
    else:
        candles = {}
        for r in market:
            try:
                candles[r["coin"]] = hl.fetch_candles(r["coin"], "1h", days=30)
            except Exception as exc:
                log.info("candles failed for %s: %s", r["coin"], exc)
        targets = compute_target_weights(candles, funding)

        # full-rebalance semantics: close everything, reopen targets
        for coin, pos in list(state["positions"].items()):
            px = prices.get(coin, pos["entry_px"])
            state["cash"] += pos["sz"] * (px - pos["entry_px"])
            state["cash"] -= abs(pos["sz"] * px) * TAKER_FEE
            del state["positions"][coin]
        equity = state["cash"]
        # size on fee-adjusted equity so gross stays under the cap post-fees
        gross_target = sum(abs(w) for w in targets.values())
        sizing_equity = equity * (1 - gross_target * TAKER_FEE)
        for coin, w in targets.items():
            px = prices.get(coin)
            if px is None or abs(w) < 0.01:
                continue
            notional = w * sizing_equity
            sz = notional / px
            state["cash"] -= abs(notional) * TAKER_FEE
            state["positions"][coin] = {"sz": sz, "entry_px": px,
                                        "entry_time": now.isoformat()}
            actions.append(f"open {coin} {w:+.2%} ({notional:+,.0f}$ @ {px:g})")
        equity = mark_to_market(state, prices)

    state["last_run"] = now.isoformat()
    _save_state(state)

    gross = sum(abs(p["sz"] * prices.get(c, p["entry_px"]))
                for c, p in state["positions"].items()) / max(equity, 1e-9)
    row = {"datetime": now.isoformat(timespec="seconds"),
           "equity": round(equity, 2), "gross_leverage": round(gross, 3),
           "n_positions": len(state["positions"]),
           "halted": state["halted"]}
    _append_history(row)
    summary = {**row, "actions": actions,
               "positions": {c: {"weight": round(p["sz"] * prices.get(c, p["entry_px"]) / max(equity, 1e-9), 3)}
                             for c, p in state["positions"].items()},
               "return_since_inception": round(equity / state["initial_capital"] - 1, 4)}
    _write_report(summary)
    return summary


def _append_history(row: dict) -> None:
    HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    header = "datetime,equity,gross_leverage,n_positions,halted\n"
    line = f"{row['datetime']},{row['equity']},{row['gross_leverage']},{row['n_positions']},{row['halted']}\n"
    if not HISTORY_PATH.exists():
        HISTORY_PATH.write_text(header + line)
    else:
        with open(HISTORY_PATH, "a") as f:
            f.write(line)


def _write_report(s: dict) -> None:
    L = ["# GOLDSTEIN — Paper Bot (Hyperliquid perps, virtual capital)",
         f"_Run {s['datetime']} · equity **${s['equity']:,.2f}**"
         f" ({s['return_since_inception']:+.2%} since inception) ·"
         f" gross leverage {s['gross_leverage']:.2f}x ·"
         f" {'⛔ HALTED (kill switch)' if s['halted'] else 'active'}_", ""]
    if s["positions"]:
        L.append("| Coin | Weight |")
        L.append("|---|---|")
        for c, p in s["positions"].items():
            L.append(f"| {c} | {p['weight']:+.1%} |")
    else:
        L.append("_Flat._")
    if s["actions"]:
        L.append("\nActions this run:")
        L += [f"- {a}" for a in s["actions"]]
    L.append("\n> Virtual capital. Momentum + funding-carry, vol-targeted, "
             f"gross ≤ {MAX_GROSS}x, kill switch at {KILL_SWITCH_EQUITY:.0%}."
             " No orders are sent anywhere. Track record accumulates in"
             " `reports/paperbot_history.csv`.")
    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    REPORT_MD.write_text("\n".join(L))
