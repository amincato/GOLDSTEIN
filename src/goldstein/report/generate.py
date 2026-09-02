"""Full analysis pipeline + markdown/JSON report generation.

`analyze()` is the single entry point that wires data → features → models →
sizing → risk, returning a plain dict (JSON-serializable) that the CLI and
agents can consume. `render_markdown()` turns it into the human report.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from ..backtest import engine, metrics, montecarlo
from ..config import CACHE_DIR, INSTRUMENTS, REPORT_DIR, TRADING_DAYS, Settings
from ..data import load_series
from ..features import indicators as ind
from ..leverage import decay, sizing
from ..models import crossasset
from ..models import regime as regime_mod
from ..models import signals as signals_mod
from ..models import volatility as vol_mod
from ..risk import stress


def _intraday_rv() -> pd.Series | None:
    """True daily realized variance from the committed 5m cache, for HAR.
    Cache-only on purpose: synthetic intraday bars would poison the RV, so
    absent cache simply means HAR falls back to the daily proxy."""
    path = CACHE_DIR / "intraday" / "XAUUSD_5m.csv"
    if not path.exists():
        return None
    try:
        bars = pd.read_csv(path, parse_dates=["datetime"], index_col="datetime")
        bars.index = pd.DatetimeIndex(bars.index, tz="UTC")
        return vol_mod.realized_variance_from_bars(bars)
    except Exception:
        return None


def _mu_estimate(returns: pd.Series) -> float:
    """Blend of long-run and 3y drift, shrunk toward the long-run gold real
    return (~2%/yr over the very long run) to temper recency bias."""
    long_run = returns.mean() * TRADING_DAYS
    recent = returns.iloc[-3 * TRADING_DAYS:].mean() * TRADING_DAYS
    return float(0.4 * long_run + 0.4 * recent + 0.2 * 0.02)


def analyze(instrument_key: str = "futures", capital: float = 10_000.0,
            settings: Settings | None = None) -> dict:
    settings = settings or Settings()
    instrument = INSTRUMENTS[instrument_key]

    gold = load_series("XAUUSD", settings)
    sources = {"XAUUSD": gold.attrs["source"]}

    def _opt(key):
        try:
            df = load_series(key, settings)
            sources[key] = df.attrs["source"]
            return df
        except Exception:
            sources[key] = "unavailable"
            return None

    real10y = _opt("REAL10Y")
    nom10y = _opt("NOM10Y")
    dxy = _opt("DXY")
    vix = _opt("VIX")
    fedfunds = _opt("FEDFUNDS")
    silver = _opt("XAGUSD")
    miners = _opt("GDX")
    spx = _opt("SPX")
    wti = _opt("WTI")
    btc = _opt("BTC")

    close = gold["close"]
    rets = ind.log_returns(close)
    if fedfunds is not None and len(fedfunds):
        settings.risk_free = float(fedfunds["value"].iloc[-1]) / 100.0

    volf = vol_mod.forecast_vol(rets, intraday_rv=_intraday_rv())
    hmm = regime_mod.fit_hmm(rets.iloc[-8 * TRADING_DAYS:])
    # rates trend input: prefer TIPS real yield; when only synthetic, fall back
    # to the nominal 10y if THAT is real data (trend direction is what matters)
    yields = real10y
    if sources.get("REAL10Y") == "synthetic" and nom10y is not None \
            and sources.get("NOM10Y") != "synthetic":
        yields = nom10y
    macro = regime_mod.macro_regime(
        yields["value"] if yields is not None else None,
        dxy["close"] if dxy is not None else None,
        vix["value"] if vix is not None else None,
    )
    others = {
        k: (df["close"] if df is not None else None)
        for k, df in [("XAGUSD", silver), ("GDX", miners), ("DXY", dxy),
                      ("SPX", spx), ("WTI", wti), ("BTC", btc)]
    }
    cross = crossasset.analyze(close, others,
                               yields["value"] if yields is not None else None)
    sig = signals_mod.compute_signal(close, macro, cross.confirmation_score)
    current_dd = float(ind.drawdown(close).iloc[-1])
    mu = _mu_estimate(rets)

    advice = sizing.advise(mu, volf.blended, sig.score, current_dd, instrument, settings)
    frontier = sizing.leverage_frontier(mu, volf.blended, settings.risk_free,
                                        instrument.financing_spread)

    mc = montecarlo.run(rets.apply(np.expm1), max(advice.recommended, 0.01),
                        instrument, settings)
    sweep = montecarlo.leverage_sweep(rets.apply(np.expm1), instrument, settings)
    st = stress.run(max(advice.recommended, 1.0), instrument, capital)
    dec_table = decay.decay_table()

    # quick strategy backtest: vol-target * signal vs buy & hold
    sig_hist = signals_mod.signal_history(close.iloc[-10 * TRADING_DAYS:])
    lev_series = engine.vol_target_leverage(close.iloc[-10 * TRADING_DAYS:],
                                            settings, signal=sig_hist)
    bt = engine.run(close.iloc[-10 * TRADING_DAYS:], lev_series, instrument, settings)
    bh = metrics.summarize(close.iloc[-10 * TRADING_DAYS:].pct_change().dropna(),
                           settings.risk_free)

    # demo = the CORE series (gold) is synthetic; degraded = real gold but
    # some auxiliary series fell back to synthetic (macro components weaker)
    synthetic_series = sorted(k for k, v in sources.items() if v == "synthetic")
    is_demo = sources.get("XAUUSD") == "synthetic"
    return {
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "demo_data": is_demo,
        "synthetic_series": synthetic_series,
        "data_sources": sources,
        "capital": capital,
        "instrument": {"key": instrument.key, "label": instrument.label,
                       "daily_reset": instrument.daily_reset,
                       "maintenance_margin": instrument.maintenance_margin},
        "market": {
            "last_price": float(close.iloc[-1]),
            "last_date": str(close.index[-1].date()),
            "return_1m": float(close.iloc[-1] / close.iloc[-21] - 1),
            "return_1y": float(close.iloc[-1] / close.iloc[-min(252, len(close) - 1)] - 1),
            "current_drawdown": current_dd,
            "mu_estimate": mu,
        },
        "volatility": {
            "ewma": volf.ewma, "garch": volf.garch, "har_rv": volf.har,
            "blended_forecast": volf.blended,
            "garch_persistence": volf.garch_persistence,
            "long_run": volf.long_run,
            "har_source": volf.har_source,
            "rv_splice_date": volf.rv_splice_date,
        },
        "regime": {
            "hmm_state": hmm.current_label,
            "hmm_expected_duration_days": hmm.expected_duration,
            "hmm_state_vols_annual": [float(v * np.sqrt(TRADING_DAYS)) for v in hmm.vols],
            "macro_label": macro.label,
            "macro_score": macro.score,
            "macro_components": macro.components,
        },
        "signal": {"score": sig.score, "direction": sig.direction,
                   "components": sig.components},
        "cross_asset": {
            "confirmation_score": cross.confirmation_score,
            "components": cross.components,
            "correlations": (cross.correlations.reset_index()
                             .to_dict(orient="records")
                             if len(cross.correlations) else []),
            "gold_silver_ratio_z": cross.gold_silver_ratio_z,
            "miners_relative_mom_6m": cross.miners_relative_mom,
            "lead_lag_real_yield": cross.lead_lag_real_yield,
        },
        "leverage_advice": {
            "recommended": advice.recommended,
            "direction": advice.direction,
            "full_kelly": advice.kelly_full,
            "expected_log_growth": advice.expected_growth,
            "caps": advice.caps,
            "note": advice.ruin_note,
        },
        "leverage_frontier": frontier.to_dict(orient="records"),
        "monte_carlo": mc.__dict__,
        "leverage_sweep": sweep.to_dict(orient="records"),
        "stress": {
            "survives_all_historical": st.survives_all_historical,
            "survives_all_century": st.survives_all_century,
            "worst_scenario": st.worst_scenario,
            "worst_equity_impact": st.worst_equity_impact,
            "table": st.table.to_dict(orient="records"),
        },
        "etp_decay_table": dec_table.to_dict(orient="records"),
        "strategy_backtest": {
            "strategy": bt.stats,
            "buy_and_hold": bh,
            "liquidations": bt.liquidations,
            "costs": bt.costs,
        },
    }


# ------------------------------------------------------------------ markdown
def _pct(x, digits=1):
    return f"{x * 100:.{digits}f}%" if isinstance(x, (int, float)) and np.isfinite(x) else "n/a"


def render_markdown(a: dict) -> str:
    L = []
    add = L.append
    add(f"# GOLDSTEIN — Leveraged Gold Analysis")
    add(f"_Generated {a['generated_utc']} · instrument: **{a['instrument']['label']}**"
        f" · capital: {a['capital']:,.0f}_\n")
    if a["demo_data"]:
        add("> ⚠️ **DEMO DATA** — the gold series itself is synthetic because no"
            " live or cached market data was available. Numbers illustrate the"
            " methodology, NOT current market conditions. Run `goldstein fetch`"
            " from a network-enabled session to populate the cache.\n")
    elif a.get("synthetic_series"):
        add(f"> ℹ️ Gold data is real, but these auxiliary series fell back to"
            f" synthetic: {', '.join(a['synthetic_series'])} — the related macro"
            f" components carry less weight of evidence.\n")

    m_ = a["market"]
    add("## Market snapshot")
    add(f"- Last price: **{m_['last_price']:,.2f}** ({m_['last_date']})")
    add(f"- 1m / 1y return: {_pct(m_['return_1m'])} / {_pct(m_['return_1y'])}")
    add(f"- Drawdown from high: {_pct(m_['current_drawdown'])}")
    add(f"- Drift estimate (shrunk): {_pct(m_['mu_estimate'])}/yr\n")

    v = a["volatility"]
    add("## Volatility forecast (annualized)")
    add(f"| EWMA | GARCH(1,1) | HAR-RV | **Blend** |")
    add(f"|---|---|---|---|")
    add(f"| {_pct(v['ewma'])} | {_pct(v['garch'])} | {_pct(v['har_rv'])} |"
        f" **{_pct(v['blended_forecast'])}** |")
    add(f"\nGARCH persistence {v['garch_persistence']:.3f}, long-run vol {_pct(v['long_run'])}.")
    if v.get("har_source") == "intraday_rv":
        add(f"HAR runs on true 5m realized variance from {v['rv_splice_date']}"
            f" (squared-return proxy, bias-adjusted, before that).\n")
    else:
        add("HAR runs on the squared-daily-return proxy (no intraday RV cache).\n")

    r = a["regime"]
    add("## Regime")
    add(f"- Statistical (HMM): **{r['hmm_state']}** (typical duration"
        f" ~{r['hmm_expected_duration_days']:.0f} days)")
    add(f"- Macro: **{r['macro_label']}** (score {r['macro_score']:+.2f};"
        f" components: {', '.join(f'{k} {v:+.2f}' for k, v in r['macro_components'].items()) or 'n/a'})\n")

    s = a["signal"]
    add("## Signal")
    add(f"- Ensemble score: **{s['score']:+.2f}** → **{s['direction'].upper()}**")
    add("- Components: " + ", ".join(f"{k} {v:+.2f}" for k, v in s["components"].items()) + "\n")

    ca = a.get("cross_asset")
    if ca:
        add("## Cross-asset picture")
        add(f"- Confirmation score: **{ca['confirmation_score']:+.2f}**"
            + (" (components: "
               + ", ".join(f"{k} {v:+.2f}" for k, v in ca["components"].items()) + ")"
               if ca["components"] else ""))
        if ca["gold_silver_ratio_z"] is not None:
            add(f"- Gold/silver ratio z-score (1y): {ca['gold_silver_ratio_z']:+.2f}"
                " (positive = gold rich vs silver)")
        if ca["miners_relative_mom_6m"] is not None:
            add(f"- Miners (GDX) 6m momentum vs gold: {_pct(ca['miners_relative_mom_6m'])}")
        if ca["correlations"]:
            add("\n| Asset | corr 63d | corr 252d | beta vs gold |")
            add("|---|---|---|---|")
            for row in ca["correlations"]:
                add(f"| {row['asset']} | {row['corr_63d']:+.2f} |"
                    f" {row['corr_252d']:+.2f} | {row['beta_vs_gold_252d']:+.2f} |")
        if ca["lead_lag_real_yield"]:
            ll = ", ".join(f"lag {k}d: {v:+.2f}" for k, v in ca["lead_lag_real_yield"].items())
            add(f"\nGold returns vs lagged real-yield changes: {ll}")
        add("")

    la = a["leverage_advice"]
    add("## Leverage recommendation")
    add(f"### → **{la['recommended']:.2f}x {la['direction'].upper()}**")
    add(f"- Full Kelly: {la['full_kelly']:.2f}x — recommendation uses fractional"
        " Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling")
    add(f"- Expected log growth at recommendation: {_pct(la['expected_log_growth'])}/yr")
    add("- Binding caps: " + ", ".join(f"{k}={v:.2f}" for k, v in la["caps"].items()))
    if la["note"]:
        add(f"- **{la['note']}**")
    add("")

    mc = a["monte_carlo"]
    add(f"## Monte Carlo ({mc['paths']} block-bootstrap paths, {mc['horizon_days']}d,"
        f" {mc['leverage']:.2f}x)")
    tw = {int(k): v for k, v in mc["terminal_wealth_pctiles"].items()}
    add(f"- Terminal wealth p5/p50/p95: {tw[5]:.2f}x / {tw[50]:.2f}x / {tw[95]:.2f}x")
    add(f"- P(loss) {_pct(mc['prob_loss'])} · P(DD>25%) {_pct(mc['prob_dd_25'])} ·"
        f" P(DD>50%) {_pct(mc['prob_dd_50'])} · **P(ruin) {_pct(mc['prob_ruin'])}**")
    add(f"- Expected max drawdown: {_pct(mc['expected_max_drawdown'])}\n")

    add("## Leverage sweep (empirical Kelly curve)")
    add("| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |")
    add("|---|---|---|---|---|---|")
    for row in a["leverage_sweep"]:
        add(f"| {row['leverage']:.1f}x | {_pct(row['median_log_growth'])} |"
            f" {_pct(row['prob_loss'])} | {_pct(row['prob_dd_50'])} |"
            f" {_pct(row['prob_ruin'])} | {_pct(row['expected_max_dd'])} |")
    add("")

    st = a["stress"]
    add("## Stress tests (at recommended leverage, min 1x)")
    add(f"- Survives all historical scenarios: **{'YES' if st['survives_all_historical'] else 'NO'}**"
        f" · worst: `{st['worst_scenario']}` ({_pct(st['worst_equity_impact'])} equity)")
    if "survives_all_century" in st:
        add(f"- Survives all CENTURY scenarios (1974-76, 1980-82, 1980-99, 2011-15,"
            f" era financing included): **{'YES' if st['survives_all_century'] else 'NO'}**")
    add("| Scenario | Asset move | Equity | Margin call |")
    add("|---|---|---|---|")
    for row in st["table"]:
        add(f"| {row['scenario']} | {_pct(row['asset_move'])} |"
            f" {row['equity_multiple']:.2f}x | {'⚠️ YES' if row['margin_liquidation'] else 'no'} |")
    add("")

    add("## Daily-reset ETP decay (annualized drag vs static leverage)")
    add("| Asset vol | 2x drag | 3x drag |")
    add("|---|---|---|")
    for row in a["etp_decay_table"]:
        add(f"| {_pct(row['annual_vol'], 0)} | {_pct(row['decay_2x'])} | {_pct(row['decay_3x'])} |")
    add("")

    bt = a["strategy_backtest"]
    if "error" not in bt["strategy"]:
        add("## Strategy backtest (10y: vol-target × signal vs buy & hold)")
        add("| Metric | Strategy | Buy & hold |")
        add("|---|---|---|")
        for k in ("cagr", "ann_vol", "sharpe", "sortino", "max_drawdown", "calmar"):
            f = _pct if k in ("cagr", "ann_vol", "max_drawdown") else lambda x: f"{x:.2f}"
            add(f"| {k} | {f(bt['strategy'][k])} | {f(bt['buy_and_hold'][k])} |")
        if bt["liquidations"]:
            add(f"- Liquidation events: {', '.join(bt['liquidations'])}")
        add("")

    add("---")
    add("_Research tooling, not investment advice. Leverage can lose more than"
        " the initial capital. All estimates are model outputs with material"
        " uncertainty._")
    return "\n".join(L)


def save(analysis: dict, name: str | None = None) -> tuple[str, str]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = name or datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    md_path = REPORT_DIR / f"analysis_{stamp}.md"
    json_path = REPORT_DIR / f"analysis_{stamp}.json"
    md_path.write_text(render_markdown(analysis))
    json_path.write_text(json.dumps(analysis, indent=2, default=str))
    return str(md_path), str(json_path)
