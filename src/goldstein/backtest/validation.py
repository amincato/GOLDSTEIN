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


EULER_GAMMA = 0.5772156649015329


def deflated_sharpe(returns: pd.Series, trial_srs_daily: list[float]) -> float:
    """Deflated Sharpe Ratio (Bailey & López de Prado 2014): PSR measured
    against the Sharpe you would expect the BEST of N unskilled trials to
    show by luck alone. The trial set is every configuration this validation
    actually examined — strategy suite plus sensitivity grid — so the number
    honestly reflects our own search."""
    srs = [s for s in trial_srs_daily if np.isfinite(s)]
    if len(srs) < 2:
        return float("nan")
    var = float(np.var(srs, ddof=1))
    n = len(srs)
    sr_star_daily = np.sqrt(max(var, 0.0)) * (
        (1 - EULER_GAMMA) * sps.norm.ppf(1 - 1 / n)
        + EULER_GAMMA * sps.norm.ppf(1 - 1 / (n * np.e))
    )
    return probabilistic_sharpe(returns, sr_star_daily * np.sqrt(TRADING_DAYS))


def reality_check(strategy_returns: dict[str, pd.Series], benchmark: pd.Series,
                  n_boot: int = 500, mean_block: float = 21.0,
                  seed: int = 42) -> dict:
    """White (2000) reality check on the whole strategy family.

    H0: no strategy in the family beats the benchmark in expectation.
    Stationary block bootstrap of the benchmark-relative return matrix
    (centered, so the null holds in the resamples); p-value = how often the
    best resampled mean beats the best observed mean. Controls the
    familywise 'we tried many configs and kept the best' bias that PSR
    alone cannot see."""
    df = pd.DataFrame(strategy_returns).sub(benchmark, axis=0).dropna()
    n, k = df.shape
    if n < 120 or k < 2:
        return {"p_value": float("nan"), "n_strategies": k, "reason": "too_short"}
    d = df.to_numpy()
    obs = d.mean(axis=0)
    best_i = int(np.argmax(obs))
    centered = d - obs
    rng = np.random.default_rng(seed)
    p_restart = 1.0 / mean_block
    idx = np.empty((n_boot, n), dtype=np.int64)
    idx[:, 0] = rng.integers(0, n, size=n_boot)
    restart = rng.random((n_boot, n)) < p_restart
    jumps = rng.integers(0, n, size=(n_boot, n))
    for t in range(1, n):
        idx[:, t] = np.where(restart[:, t], jumps[:, t], (idx[:, t - 1] + 1) % n)
    boot_best = centered[idx].mean(axis=1).max(axis=1)
    p = float((boot_best >= obs[best_i]).mean())
    return {
        "p_value": p,
        "best_strategy": str(df.columns[best_i]),
        "best_excess_annual": float(obs[best_i] * TRADING_DAYS),
        "n_strategies": int(k),
        "n_boot": n_boot,
    }


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
                   settings: Settings,
                   rf_series: pd.Series | None = None
                   ) -> tuple[pd.DataFrame, dict[str, pd.Series]]:
    inst = INSTRUMENTS[instrument_key]
    rows, rets = [], {}
    for name, lev in _strategies(close, settings).items():
        res = engine.run(close, lev, inst, settings, rf_series=rf_series)
        row = {"strategy": name, **res.stats,
               "psr_vs_0": probabilistic_sharpe(res.returns),
               "liquidations": len(res.liquidations)}
        rows.append(row)
        rets[name] = res.returns
    return pd.DataFrame(rows).set_index("strategy"), rets


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
                          spans=(21, 33, 63),
                          rf_series: pd.Series | None = None
                          ) -> tuple[pd.DataFrame, dict[str, pd.Series]]:
    inst = INSTRUMENTS[instrument_key]
    sig = signals_mod.signal_history(close)
    rows, rets = [], {}
    for tv in target_vols:
        for span in spans:
            s = Settings(**{**settings.__dict__, "target_vol": tv})
            lev = engine.vol_target_leverage(close, s, signal=sig, span=span)
            res = engine.run(close, lev, inst, s, rf_series=rf_series)
            rows.append({
                "target_vol": tv, "vol_window": span,
                "sharpe": res.stats.get("sharpe", np.nan),
                "cagr": res.stats.get("cagr", np.nan),
                "max_drawdown": res.stats.get("max_drawdown", np.nan),
            })
            rets[f"tv{tv:g}_w{span}"] = res.returns
    return pd.DataFrame(rows), rets


def run_validation(instrument_key: str = "futures",
                   settings: Settings | None = None,
                   quick: bool = False) -> dict:
    settings = settings or Settings()
    gold = load_series("XAUUSD", settings)
    close = gold["close"]
    if quick:
        close = close.iloc[-8 * TRADING_DAYS:]
    try:
        ff = load_series("FEDFUNDS", settings, allow_synthetic=False)
        rf_series = ff["value"]        # actual FedFunds path, not a constant
    except Exception:
        rf_series = None

    suite, suite_rets = strategy_suite(close, instrument_key, settings, rf_series)
    wf = walk_forward(close, instrument_key, settings)
    sens, sens_rets = (
        parameter_sensitivity(close, instrument_key, settings, rf_series=rf_series)
        if not quick else
        parameter_sensitivity(close, instrument_key, settings,
                              target_vols=(0.10, 0.15), spans=(21, 63),
                              rf_series=rf_series))

    # multiple-testing honesty: every configuration examined is a trial
    family = {k: v for k, v in {**suite_rets, **sens_rets}.items()
              if k != "buy_hold_1x"}
    trial_srs = [float(r.mean() / r.std()) for r in family.values()
                 if r.std() > 0]
    dsr = deflated_sharpe(suite_rets["vol_target_x_signal"], trial_srs)
    rc = reality_check(family, suite_rets["buy_hold_1x"],
                       seed=settings.seed)

    adaptive = suite.loc["vol_target_x_signal"]
    bh = suite.loc["buy_hold_1x"]
    beats_bh_years = (
        float((wf["strategy_sharpe"] > wf["bh_sharpe"]).mean()) if len(wf) else np.nan
    )
    sharpe_spread = float(sens["sharpe"].max() - sens["sharpe"].min())
    verdict_points = {
        "adaptive_psr_above_90": bool(adaptive["psr_vs_0"] > 0.90),
        "adaptive_dsr_above_50": bool(np.isfinite(dsr) and dsr > 0.50),
        "family_beats_bh_reality_check": bool(
            np.isfinite(rc["p_value"]) and rc["p_value"] < 0.10),
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
        "financing": "fedfunds_path" if rf_series is not None else "flat_fallback",
        "deflated_sharpe_adaptive": float(dsr) if np.isfinite(dsr) else None,
        "reality_check": rc,
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

    dsr = v.get("deflated_sharpe_adaptive")
    rc = v.get("reality_check", {})
    add("## Multiple-testing honesty")
    add(f"- Deflated Sharpe (adaptive, vs best-of-{rc.get('n_strategies', '?')}"
        f"-trials luck): **{_pct(dsr, 0) if dsr is not None else 'n/a'}**")
    if np.isfinite(rc.get("p_value", np.nan)):
        add(f"- White reality check: best family member `{rc['best_strategy']}`"
            f" excess {_pct(rc['best_excess_annual'])}/yr vs B&H,"
            f" p-value **{rc['p_value']:.3f}** ({rc['n_boot']} bootstraps)")
    add(f"- Financing in engine: {v.get('financing', 'n/a')}\n")

    ver = v["verdict"]
    add(f"## Verdict — {ver['checks_passed']}/{ver['checks_total']} robustness checks passed")
    for k in ("adaptive_psr_above_90", "adaptive_dsr_above_50",
              "family_beats_bh_reality_check", "adaptive_dd_beats_bh",
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
