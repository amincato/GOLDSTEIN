"""Backtest validation suite — the evidence layer behind any leverage claim.

Four independent checks:
1. Strategy comparison  — buy&hold, constant 2x/3x, vol-target, vol-target ×
   signal, all through the realistic engine (costs, financing, liquidation).
2. Walk-forward         — the adaptive strategy is point-in-time by
   construction; we slice its returns into yearly out-of-sample buckets and
   check the edge is stable across years, not one lucky stretch.
3. Probabilistic Sharpe — Bailey & López de Prado PSR: P(true Sharpe > 0)
   given skew, kurtosis and sample length. Guards against backtest luck.
4. Parameter sensitivity — Sharpe/MaxDD across a target-vol × vol-window
   grid. A robust rule has a flat surface; a spike means overfitting.

All of it runs offline and lands in one markdown/JSON validation report.
"""

from __future__ import annotations

from datetime import datetime, timezone

import numpy as np
import pandas as pd
from scipy import stats as sps

from ..config import INSTRUMENTS, REPORT_DIR, TRADING_DAYS, Settings
from ..data import load_series
from ..models import signals as signals_mod
from . import engine, metrics


def probabilistic_sharpe(returns: pd.Series, benchmark_sr: float = 0.0) -> float:
    """PSR = P(true annualized Sharpe > benchmark) adjusting for skew,
    kurtosis and track length (Bailey & López de Prado, 2012)."""
    r = returns.dropna()
    n = len(r)
    if n < 60 or r.std() == 0:
        return float("nan")
    sr_daily = r.mean() / r.std()
    sr_bench_daily = benchmark_sr / np.sqrt(TRADING_DAYS)
    skew = float(sps.skew(r))
    kurt = float(sps.kurtosis(r, fisher=False))
    denom = np.sqrt(max(1 - skew * sr_daily + (kurt - 1) / 4 * sr_daily**2, 1e-12))
    z = (sr_daily - sr_bench_daily) * np.sqrt(n - 1) / denom
    return float(sps.norm.cdf(z))


def _strategies(close: pd.Series, settings: Settings) -> dict[str, pd.Series | float]:
    sig = signals_mod.signal_history(close)
    return {
        "buy_hold_1x": 1.0,
        "constant_2x": 2.0,
        "constant_3x": 3.0,
        "vol_target": engine.vol_target_leverage(close, settings),
        "vol_target_x_signal": engine.vol_target_leverage(close, settings, signal=sig),
    }


def strategy_suite(close: pd.Series, instrument_key: str,
                   settings: Settings) -> pd.DataFrame:
    inst = INSTRUMENTS[instrument_key]
    rows = []
    for name, lev in _strategies(close, settings).items():
        res = engine.run(close, lev, inst, settings)
        row = {"strategy": name, **res.stats,
               "psr_vs_0": probabilistic_sharpe(res.returns),
               "liquidations": len(res.liquidations)}
        rows.append(row)
    return pd.DataFrame(rows).set_index("strategy")


def walk_forward(close: pd.Series, instrument_key: str,
                 settings: Settings) -> pd.DataFrame:
    """Yearly out-of-sample buckets of the adaptive strategy vs buy & hold.

    Decisions inside the engine only use expanding history (signal_history is
    point-in-time and leverage is lagged one bar), so each calendar-year slice
    is genuine OOS for that year."""
    inst = INSTRUMENTS[instrument_key]
    sig = signals_mod.signal_history(close)
    lev = engine.vol_target_leverage(close, settings, signal=sig)
    res = engine.run(close, lev, inst, settings)
    bh = close.pct_change().fillna(0.0)

    rows = []
    for year, r in res.returns.groupby(res.returns.index.year):
        if len(r) < 100:               # skip partial edge years
            continue
        b = bh.loc[r.index]
        s_stats = metrics.summarize(r, settings.risk_free)
        b_stats = metrics.summarize(b, settings.risk_free)
        if "error" in s_stats or "error" in b_stats:
            continue
        rows.append({
            "year": year,
            "strategy_return": s_stats["cagr"],
            "bh_return": b_stats["cagr"],
            "strategy_sharpe": s_stats["sharpe"],
            "bh_sharpe": b_stats["sharpe"],
            "strategy_maxdd": s_stats["max_drawdown"],
            "bh_maxdd": b_stats["max_drawdown"],
            "avg_leverage": float(res.leverage.loc[r.index].abs().mean()),
        })
    return pd.DataFrame(rows).set_index("year")


def parameter_sensitivity(close: pd.Series, instrument_key: str,
                          settings: Settings,
                          target_vols=(0.10, 0.15, 0.20),
                          spans=(21, 33, 63)) -> pd.DataFrame:
    inst = INSTRUMENTS[instrument_key]
    sig = signals_mod.signal_history(close)
    rows = []
    for tv in target_vols:
        for span in spans:
            s = Settings(**{**settings.__dict__, "target_vol": tv})
            lev = engine.vol_target_leverage(close, s, signal=sig, span=span)
            res = engine.run(close, lev, inst, s)
            rows.append({
                "target_vol": tv, "vol_window": span,
                "sharpe": res.stats.get("sharpe", np.nan),
                "cagr": res.stats.get("cagr", np.nan),
                "max_drawdown": res.stats.get("max_drawdown", np.nan),
            })
    return pd.DataFrame(rows)


def run_validation(instrument_key: str = "futures",
                   settings: Settings | None = None,
                   quick: bool = False) -> dict:
    settings = settings or Settings()
    gold = load_series("XAUUSD", settings)
    close = gold["close"]
    if quick:
        close = close.iloc[-8 * TRADING_DAYS:]

    suite = strategy_suite(close, instrument_key, settings)
    wf = walk_forward(close, instrument_key, settings)
    sens = (parameter_sensitivity(close, instrument_key, settings)
            if not quick else
            parameter_sensitivity(close, instrument_key, settings,
                                  target_vols=(0.10, 0.15), spans=(21, 63)))

    adaptive = suite.loc["vol_target_x_signal"]
    bh = suite.loc["buy_hold_1x"]
    beats_bh_years = (
        float((wf["strategy_sharpe"] > wf["bh_sharpe"]).mean()) if len(wf) else np.nan
    )
    sharpe_spread = float(sens["sharpe"].max() - sens["sharpe"].min())
    verdict_points = {
        "adaptive_psr_above_90": bool(adaptive["psr_vs_0"] > 0.90),
        "adaptive_dd_beats_bh": bool(adaptive["max_drawdown"] > bh["max_drawdown"]),
        "positive_years_majority": bool(beats_bh_years >= 0.5) if np.isfinite(beats_bh_years) else False,
        "params_robust": bool(sharpe_spread < 0.6),
        "no_liquidations": bool(adaptive["liquidations"] == 0),
    }
    return {
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "demo_data": gold.attrs.get("source") == "synthetic",
        "data_source": gold.attrs.get("source"),
        "instrument": instrument_key,
        "sample": {"start": str(close.index[0].date()),
                   "end": str(close.index[-1].date()), "days": len(close)},
        "strategy_suite": suite.reset_index().to_dict(orient="records"),
        "walk_forward": wf.reset_index().to_dict(orient="records"),
        "parameter_sensitivity": sens.to_dict(orient="records"),
        "verdict": {
            **verdict_points,
            "checks_passed": sum(verdict_points.values()),
            "checks_total": len(verdict_points),
            "pct_years_beating_bh_sharpe": beats_bh_years,
            "sens_sharpe_spread": sharpe_spread,
        },
    }


def _pct(x, d=1):
    return f"{x * 100:.{d}f}%" if isinstance(x, (int, float)) and np.isfinite(x) else "n/a"


def render_markdown(v: dict) -> str:
    L = []
    add = L.append
    add("# GOLDSTEIN — Backtest Validation Report")
    add(f"_Generated {v['generated_utc']} · sample {v['sample']['start']} →"
        f" {v['sample']['end']} ({v['sample']['days']}d) · instrument:"
        f" {v['instrument']} · data: {v['data_source']}_\n")
    if v["demo_data"]:
        add("> ⚠️ **DEMO DATA** — validation ran on synthetic data; it proves the"
            " machinery, not a live edge. Populate `data/cache/` for real results.\n")

    add("## Strategy comparison (full engine: costs, financing, liquidation)")
    add("| Strategy | CAGR | Vol | Sharpe | PSR>0 | MaxDD | Calmar | Liq. |")
    add("|---|---|---|---|---|---|---|---|")
    for r in v["strategy_suite"]:
        add(f"| {r['strategy']} | {_pct(r['cagr'])} | {_pct(r['ann_vol'])} |"
            f" {r['sharpe']:.2f} | {_pct(r['psr_vs_0'], 0)} | {_pct(r['max_drawdown'])} |"
            f" {r['calmar']:.2f} | {r['liquidations']} |")
    add("")

    if v["walk_forward"]:
        add("## Walk-forward (yearly out-of-sample buckets)")
        add("| Year | Strat ret | B&H ret | Strat Sharpe | B&H Sharpe | Strat DD | avg lev |")
        add("|---|---|---|---|---|---|---|")
        for r in v["walk_forward"]:
            add(f"| {r['year']} | {_pct(r['strategy_return'])} | {_pct(r['bh_return'])} |"
                f" {r['strategy_sharpe']:.2f} | {r['bh_sharpe']:.2f} |"
                f" {_pct(r['strategy_maxdd'])} | {r['avg_leverage']:.2f}x |")
        add("")

    add("## Parameter sensitivity (vol-target × signal)")
    add("| target vol | vol window | Sharpe | CAGR | MaxDD |")
    add("|---|---|---|---|---|")
    for r in v["parameter_sensitivity"]:
        add(f"| {_pct(r['target_vol'], 0)} | {r['vol_window']}d | {r['sharpe']:.2f} |"
            f" {_pct(r['cagr'])} | {_pct(r['max_drawdown'])} |")
    add("")

    ver = v["verdict"]
    add(f"## Verdict — {ver['checks_passed']}/{ver['checks_total']} robustness checks passed")
    for k in ("adaptive_psr_above_90", "adaptive_dd_beats_bh",
              "positive_years_majority", "params_robust", "no_liquidations"):
        add(f"- {'✅' if ver[k] else '❌'} {k}")
    add(f"- Years beating B&H on Sharpe: {_pct(ver['pct_years_beating_bh_sharpe'], 0)}"
        f" · sensitivity Sharpe spread: {ver['sens_sharpe_spread']:.2f}")
    add("\n---\n_Validation of methodology, not a guarantee of future returns._")
    return "\n".join(L)


def save(v: dict) -> tuple[str, str]:
    import json

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    md = REPORT_DIR / "validation_latest.md"
    js = REPORT_DIR / "validation_latest.json"
    md.write_text(render_markdown(v))
    js.write_text(json.dumps(v, indent=2, default=str))
    return str(md), str(js)
