"""GOLDSTEIN CLI — every capability reachable headless, one command each.

Designed for AI-agent operation: stable subcommands, JSON output via --json,
non-zero exit only on real failures, and graceful offline degradation.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys

import numpy as np


def _settings_from(args) -> "Settings":
    from .config import Settings

    s = Settings()
    for attr in ("target_vol", "kelly_fraction", "max_leverage", "seed",
                 "mc_paths", "lookback_years"):
        v = getattr(args, attr, None)
        if v is not None:
            setattr(s, attr, v)
    return s


def cmd_fetch(args) -> int:
    from .data import fetch_all

    sources = fetch_all(_settings_from(args), refresh=True)
    live = sum(1 for v in sources.values() if v == "live")
    for k, v in sources.items():
        print(f"  {k:<14} {v}")
    if live == 0:
        print("\nNo live data reachable (network likely blocked). Cached/synthetic"
              " data will be used; reports will be flagged accordingly.")
    return 0


def cmd_doctor(args) -> int:
    import requests

    from .data import data_status

    print("== cache status ==")
    print(data_status().to_string())
    print("\n== network probes ==")
    for name, url in [
        ("stooq", "https://stooq.com/q/d/l/?s=xauusd&i=d"),
        ("yahoo", "https://query1.finance.yahoo.com/v8/finance/chart/GLD?range=5d&interval=1d"),
        ("fred", "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10"),
    ]:
        try:
            r = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
            print(f"  {name:<6} HTTP {r.status_code}")
        except Exception as exc:
            print(f"  {name:<6} UNREACHABLE ({type(exc).__name__})")
    return 0


def cmd_analyze(args) -> int:
    from .report import generate

    analysis = generate.analyze(args.instrument, args.capital, _settings_from(args))
    if args.json:
        print(json.dumps(analysis, indent=2, default=str))
    else:
        print(generate.render_markdown(analysis))
    return 0


def cmd_report(args) -> int:
    from .report import generate

    analysis = generate.analyze(args.instrument, args.capital, _settings_from(args))
    md, js = generate.save(analysis)
    print(f"markdown: {md}\njson:     {js}")
    if analysis["demo_data"]:
        print("note: DEMO data (synthetic) — run `goldstein fetch` with network access")
    return 0


def cmd_backtest(args) -> int:
    from .backtest import engine, metrics
    from .config import INSTRUMENTS
    from .data import load_series
    from .models import signals as signals_mod

    s = _settings_from(args)
    inst = INSTRUMENTS[args.instrument]
    close = load_series("XAUUSD", s)["close"]
    if args.leverage is not None:
        lev = float(args.leverage)
        result = engine.run(close, lev, inst, s)
        label = f"constant {lev:g}x"
    else:
        sig = signals_mod.signal_history(close)
        lev_series = engine.vol_target_leverage(close, s, signal=sig)
        result = engine.run(close, lev_series, inst, s)
        label = "vol-target × signal"
    print(f"== backtest: {label} on XAUUSD ({inst.label}) ==")
    out = {"strategy": label, "stats": result.stats,
           "liquidations": result.liquidations, "costs": result.costs,
           "buy_and_hold": metrics.summarize(close.pct_change().dropna(), s.risk_free)}
    print(json.dumps(out, indent=2, default=str) if args.json else _fmt_stats(out))
    return 0


def _fmt_stats(out: dict) -> str:
    lines = []
    for k, v in out["stats"].items():
        bh = out["buy_and_hold"].get(k)
        fmt = (lambda x: f"{x:+.2%}") if isinstance(v, float) and abs(v) < 3 else str
        lines.append(f"  {k:<18} {fmt(v):>12}   (b&h {fmt(bh) if isinstance(bh, float) else bh})")
    if out["liquidations"]:
        lines.append(f"  liquidations: {out['liquidations']}")
    return "\n".join(lines)


def cmd_montecarlo(args) -> int:
    from .backtest import montecarlo
    from .config import INSTRUMENTS
    from .data import load_series
    from .features import indicators as ind

    s = _settings_from(args)
    inst = INSTRUMENTS[args.instrument]
    close = load_series("XAUUSD", s)["close"]
    rets = ind.log_returns(close).apply(np.expm1)
    if args.sweep:
        df = montecarlo.leverage_sweep(rets, inst, s)
        print(df.to_json(orient="records", indent=2) if args.json
              else df.to_string(index=False, float_format=lambda x: f"{x:.3f}"))
    else:
        mc = montecarlo.run(rets, args.leverage or 2.0, inst, s)
        print(json.dumps(mc.__dict__, indent=2, default=str))
    return 0


def cmd_stress(args) -> int:
    from .config import INSTRUMENTS
    from .risk import stress

    res = stress.run(args.leverage or 2.0, INSTRUMENTS[args.instrument], args.capital)
    if args.json:
        print(res.table.to_json(orient="records", indent=2))
    else:
        print(res.table.drop(columns=["description"]).to_string(index=False))
        print(f"\nsurvives all historical: {res.survives_all_historical}"
              f" | worst: {res.worst_scenario} ({res.worst_equity_impact:+.1%})")
    return 0


def cmd_decay(args) -> int:
    from .leverage import decay

    print("Annualized daily-reset compounding drag vs static leverage:")
    print(decay.decay_table().to_string(index=False, float_format=lambda x: f"{x:.2%}"))
    for L in (2.0, 3.0):
        be = decay.breakeven_drift(L, args.vol, fees=0.01)
        print(f"\n{L:g}x at {args.vol:.0%} vol needs > {be:.1%}/yr asset drift"
              " to beat holding the asset unlevered (incl. 1% fees)")
    return 0


def main(argv=None) -> int:
    logging.basicConfig(level=logging.WARNING)
    p = argparse.ArgumentParser(
        prog="goldstein",
        description="Quant research & risk platform for leveraged gold investing",
    )
    p.add_argument("--seed", type=int, help="random seed override")
    sub = p.add_subparsers(dest="command", required=True)

    def common(sp, leverage=False):
        sp.add_argument("--instrument", default="futures",
                        choices=["futures", "cfd", "etp2x", "etp3x", "etf1x"])
        sp.add_argument("--capital", type=float, default=10_000.0)
        sp.add_argument("--json", action="store_true", help="machine-readable output")
        sp.add_argument("--target-vol", dest="target_vol", type=float)
        sp.add_argument("--kelly-fraction", dest="kelly_fraction", type=float)
        sp.add_argument("--max-leverage", dest="max_leverage", type=float)
        sp.add_argument("--mc-paths", dest="mc_paths", type=int)
        if leverage:
            sp.add_argument("--leverage", type=float,
                            help="fixed leverage (default: adaptive/2x)")

    sp = sub.add_parser("fetch", help="refresh market data cache from live providers")
    sp.set_defaults(fn=cmd_fetch)
    sp = sub.add_parser("doctor", help="diagnose data cache and network access")
    sp.set_defaults(fn=cmd_doctor)
    sp = sub.add_parser("analyze", help="full analysis to stdout")
    common(sp)
    sp.set_defaults(fn=cmd_analyze)
    sp = sub.add_parser("report", help="full analysis saved to reports/ (md + json)")
    common(sp)
    sp.set_defaults(fn=cmd_report)
    sp = sub.add_parser("backtest", help="backtest constant or adaptive leverage")
    common(sp, leverage=True)
    sp.set_defaults(fn=cmd_backtest)
    sp = sub.add_parser("montecarlo", help="block-bootstrap Monte Carlo risk")
    common(sp, leverage=True)
    sp.add_argument("--sweep", action="store_true", help="sweep leverage 0.5x–5x")
    sp.set_defaults(fn=cmd_montecarlo)
    sp = sub.add_parser("stress", help="historical + parametric stress tests")
    common(sp, leverage=True)
    sp.set_defaults(fn=cmd_stress)
    sp = sub.add_parser("decay", help="leveraged-ETP volatility decay tables")
    sp.add_argument("--vol", type=float, default=0.15)
    sp.set_defaults(fn=cmd_decay)

    args = p.parse_args(argv)
    try:
        return args.fn(args)
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
