"""Intraday strategy validation: the burden of proof for a scalper.

1. Walk-forward: parameters selected on the first ~60% of days, judged on
   the untouched remainder — per strategy.
2. Cost sensitivity: expectancy at 0 / 1 / 1.5 / 2 / 3 ticks of spread.
   A scalping edge that dies at realistic spread is not an edge.
3. Session breakdown & exit mix, so the "when" and "how" are visible.

Everything lands in reports/intraday_latest.{md,json}.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from ..config import REPORT_DIR
from .contracts import CONTRACTS, CostModel
from .data import load_intraday
from .engine import RiskRules, run
from .features import add_features, session_stats
from .strategies import PARAM_GRID, STRATEGIES


def _split_days(feat: pd.DataFrame, frac: float = 0.6):
    days = feat["date"].drop_duplicates().sort_values()
    cut = days.iloc[int(len(days) * frac)]
    return feat[feat["date"] <= cut], feat[feat["date"] > cut]


def walk_forward(feat: pd.DataFrame, contract_key: str = "MGC",
                 spread_override: float | None = None) -> dict:
    contract = CONTRACTS[contract_key]
    costs = CostModel.for_contract(contract, spread_override)
    train, test = _split_days(feat)
    out = {}
    for name, fn in STRATEGIES.items():
        best_params, best_score = None, -np.inf
        for params in PARAM_GRID[name]:
            res = run(train, fn(train, **params), contract, costs)
            score = (res.stats.get("expectancy_r", -9) *
                     np.sqrt(max(res.stats.get("n_trades", 0), 1)))
            if res.stats.get("n_trades", 0) >= 10 and score > best_score:
                best_score, best_params = score, params
        if best_params is None:
            out[name] = {"status": "insufficient trades in-sample"}
            continue
        oos = run(test, fn(test, **best_params), contract, costs)
        ins = run(train, fn(train, **best_params), contract, costs)
        out[name] = {
            "status": "ok",
            "best_params": best_params,
            "in_sample": ins.stats,
            "out_of_sample": oos.stats,
        }
    return out


def cost_sensitivity(feat: pd.DataFrame, contract_key: str = "MGC",
                     spreads=(0.0, 1.0, 1.5, 2.0, 3.0)) -> pd.DataFrame:
    contract = CONTRACTS[contract_key]
    rows = []
    for name, fn in STRATEGIES.items():
        sig = fn(feat)
        for sp in spreads:
            res = run(feat, sig, contract, CostModel.for_contract(contract, sp))
            rows.append({
                "strategy": name,
                "spread_ticks": sp,
                "n_trades": res.stats.get("n_trades", 0),
                "expectancy_ticks": res.stats.get("expectancy_ticks", np.nan),
                "profit_factor": res.stats.get("profit_factor", np.nan),
                "total_pnl": res.stats.get("total_pnl", 0.0),
            })
    return pd.DataFrame(rows)


def run_validation(contract_key: str = "MGC", interval: str = "5m",
                   refresh: bool = False, seed: int = 42) -> dict:
    bars = load_intraday(interval=interval, refresh=refresh, seed=seed)
    feat = add_features(bars)
    wf = walk_forward(feat, contract_key)
    cs = cost_sensitivity(feat, contract_key)
    sess = session_stats(feat)

    # verdict: an OOS-surviving strategy must keep positive expectancy at
    # realistic costs and have enough trades to mean anything
    survivors = []
    for name, r in wf.items():
        if r.get("status") != "ok":
            continue
        oos = r["out_of_sample"]
        if (oos.get("n_trades", 0) >= 10
                and oos.get("expectancy_r", -9) > 0
                and oos.get("profit_factor", 0) > 1.1):
            survivors.append(name)

    return {
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "data_source": bars.attrs.get("source"),
        "demo_data": bars.attrs.get("source") == "synthetic",
        "interval": interval,
        "contract": contract_key,
        "sample": {
            "start": str(bars.index[0]), "end": str(bars.index[-1]),
            "bars": len(bars), "days": int(feat["date"].nunique()),
        },
        "session_stats": sess.round(3).reset_index().to_dict(orient="records"),
        "walk_forward": wf,
        "cost_sensitivity": cs.to_dict(orient="records"),
        "oos_survivors": survivors,
    }


def _f(x, d=2):
    return f"{x:.{d}f}" if isinstance(x, (int, float)) and np.isfinite(x) else "n/a"


def render_markdown(v: dict) -> str:
    L = []
    add = L.append
    add("# GOLDSTEIN — Intraday Scalping Validation")
    add(f"_Generated {v['generated_utc']} · {v['interval']} bars ·"
        f" {v['sample']['days']} days ({v['sample']['bars']} bars) ·"
        f" contract {v['contract']} · data: {v['data_source']}_\n")
    if v["demo_data"]:
        add("> ⚠️ **DEMO DATA** — intraday bars are synthetic; this validates the"
            " machinery, not a live edge. Run `goldstein intraday fetch` from a"
            " network-enabled environment (the daily CI does it automatically).\n")

    add("## Session profile (when the market pays)")
    add("| Session | ann. vol | avg range (ticks) | avg volume |")
    add("|---|---|---|---|")
    for r in v["session_stats"]:
        add(f"| {r['session']} | {r['ann_vol']:.1%} | {_f(r['avg_range_ticks'], 1)} |"
            f" {_f(r['avg_volume'], 0)} |")
    add("")

    add("## Walk-forward (params chosen in-sample, judged out-of-sample)")
    for name, r in v["walk_forward"].items():
        add(f"### {name}")
        if r.get("status") != "ok":
            add(f"- {r.get('status')}\n")
            continue
        add(f"- params: `{r['best_params']}`")
        for tag, s in (("IS", r["in_sample"]), ("OOS", r["out_of_sample"])):
            add(f"- **{tag}**: {s.get('n_trades', 0)} trades · win {s.get('win_rate', 0):.0%}"
                f" · PF {_f(s.get('profit_factor'))} · expectancy"
                f" {_f(s.get('expectancy_ticks'))} ticks ({_f(s.get('expectancy_r'))}R)"
                f" · PnL ${_f(s.get('total_pnl'), 0)}"
                f" · maxDD {s.get('max_drawdown', 0):.1%}")
        add("")

    add("## Cost sensitivity (expectancy in ticks vs spread)")
    add("| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |")
    add("|---|---|---|---|---|---|")
    by = {}
    for r in v["cost_sensitivity"]:
        by.setdefault(r["strategy"], {})[r["spread_ticks"]] = r["expectancy_ticks"]
    for name, row in by.items():
        add(f"| {name} | " + " | ".join(_f(row.get(s)) for s in (0.0, 1.0, 1.5, 2.0, 3.0)) + " |")
    add("")

    surv = v["oos_survivors"]
    add(f"## Verdict")
    if surv:
        add(f"- OOS survivors at realistic costs: **{', '.join(surv)}**")
    else:
        add("- **No strategy survives out-of-sample at realistic costs on this"
            " sample.** That is a result, not a failure of the tool: do not"
            " scalp this market with these setups until an edge shows up.")
    add("\n---\n_Research tooling, not investment advice. Intraday leverage on"
        " futures can lose more than the margin posted._")
    return "\n".join(L)


def save(v: dict) -> tuple[str, str]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    md = REPORT_DIR / "intraday_latest.md"
    js = REPORT_DIR / "intraday_latest.json"
    md.write_text(render_markdown(v))
    js.write_text(json.dumps(v, indent=2, default=str))
    return str(md), str(js)
