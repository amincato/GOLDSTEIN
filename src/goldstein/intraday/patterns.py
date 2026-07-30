"""Systematic intraday pattern mining with multiple-testing control.

Scans hour-of-day and day-of-week return effects (the documented gold
anomalies cluster around the London AM/PM fixes and session opens) and —
crucially — refuses to be fooled by its own search: testing 24 hours means
the best hour looks "significant" by chance alone. We control for that with
a White's-Reality-Check-style bootstrap: the observed max |t| across all
patterns is compared against its null distribution obtained by circularly
shifting the hour labels (preserves the return series' autocorrelation while
destroying any true time-of-day alignment).

A pattern is only declared REAL if it survives that familywise test.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd


@dataclass
class PatternReport:
    hour_table: pd.DataFrame          # per-UTC-hour stats
    dow_table: pd.DataFrame           # per-day-of-week stats
    best_hour: int
    best_hour_tstat: float
    reality_check_pvalue: float       # P(max|t| >= observed | no true effect)
    significant_hours: list           # hours surviving the familywise test
    n_bootstrap: int
    components: dict = field(default_factory=dict)


def _hour_stats(rets: pd.Series, hours: np.ndarray) -> pd.DataFrame:
    rows = []
    for h in range(24):
        r = rets.values[hours == h]
        if len(r) < 30:
            continue
        mean = r.mean()
        t = mean / (r.std(ddof=1) / np.sqrt(len(r))) if r.std() > 0 else 0.0
        rows.append({
            "hour_utc": h,
            "n": len(r),
            "mean_bps": mean * 1e4,
            "ann_return_if_held": mean * 252 * 100,   # % if this hour held daily
            "t_stat": t,
            "hit_rate": float((r > 0).mean()),
        })
    return pd.DataFrame(rows).set_index("hour_utc")


def _max_abs_t(rets_values: np.ndarray, hours: np.ndarray) -> float:
    best = 0.0
    for h in range(24):
        r = rets_values[hours == h]
        if len(r) < 30 or r.std() == 0:
            continue
        t = abs(r.mean() / (r.std(ddof=1) / np.sqrt(len(r))))
        best = max(best, t)
    return best


def mine(bars: pd.DataFrame, n_bootstrap: int = 500, seed: int = 42,
         alpha: float = 0.05) -> PatternReport:
    """Run the seasonality scan on (ideally hourly) bars."""
    rets = np.log(bars["close"] / bars["close"].shift(1)).dropna()
    hours = rets.index.hour.values
    dows = rets.index.dayofweek.values

    hour_tab = _hour_stats(rets, hours)

    dow_rows = []
    names = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    daily = rets.groupby(rets.index.normalize()).sum()
    ddow = daily.index.dayofweek
    for d in range(5):
        r = daily.values[ddow == d]
        if len(r) < 20:
            continue
        t = r.mean() / (r.std(ddof=1) / np.sqrt(len(r))) if r.std() > 0 else 0.0
        dow_rows.append({"day": names[d], "n": len(r), "mean_bps": r.mean() * 1e4,
                         "t_stat": t, "hit_rate": float((r > 0).mean())})
    dow_tab = pd.DataFrame(dow_rows).set_index("day")

    observed_max = _max_abs_t(rets.values, hours)
    rng = np.random.default_rng(seed)
    null_max = np.empty(n_bootstrap)
    n = len(rets)
    for b in range(n_bootstrap):
        shift = int(rng.integers(24, n - 24))
        null_max[b] = _max_abs_t(rets.values, np.roll(hours, shift))
    pvalue = float((null_max >= observed_max).mean())

    # familywise threshold: alpha-quantile of the null max distribution
    threshold = float(np.quantile(null_max, 1 - alpha))
    significant = [int(h) for h, row in hour_tab.iterrows()
                   if abs(row["t_stat"]) >= threshold]

    best_hour = int(hour_tab["t_stat"].abs().idxmax()) if len(hour_tab) else -1
    best_t = float(hour_tab.loc[best_hour, "t_stat"]) if len(hour_tab) else 0.0
    return PatternReport(hour_tab, dow_tab, best_hour, best_t, pvalue,
                         significant, n_bootstrap,
                         {"familywise_t_threshold": threshold})


def render_markdown(rep: PatternReport, meta: dict) -> str:
    L = []
    add = L.append
    add("# GOLDSTEIN — Intraday Seasonality Mining")
    add(f"_{meta.get('interval')} bars · {meta.get('days')} days ·"
        f" data: {meta.get('source')} · {rep.n_bootstrap} bootstrap draws_\n")
    if meta.get("source") == "synthetic":
        add("> ⚠️ **DEMO DATA** — synthetic bars; patterns here are noise by"
            " construction.\n")
    add("## Hour-of-day effects (UTC)")
    add("| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |")
    add("|---|---|---|---|---|---|")
    tab = rep.hour_table.sort_values("t_stat", key=lambda s: s.abs(),
                                     ascending=False).head(8)
    for h, r in tab.iterrows():
        add(f"| {h:02d} | {r['n']:.0f} | {r['mean_bps']:+.2f} |"
            f" {r['ann_return_if_held']:+.1f}% | {r['t_stat']:+.2f} |"
            f" {r['hit_rate']:.0%} |")
    add("")
    add("## Day-of-week (daily totals)")
    add("| Day | n | mean (bps) | t-stat | hit rate |")
    add("|---|---|---|---|---|")
    for d, r in rep.dow_table.iterrows():
        add(f"| {d} | {r['n']:.0f} | {r['mean_bps']:+.1f} | {r['t_stat']:+.2f} |"
            f" {r['hit_rate']:.0%} |")
    add("")
    add("## Reality check (multiple-testing control)")
    add(f"- Best hour: **{rep.best_hour:02d} UTC** (t = {rep.best_hour_tstat:+.2f})")
    add(f"- Familywise |t| threshold at 5%: {rep.components['familywise_t_threshold']:.2f}")
    add(f"- Reality-check p-value for the best pattern: **{rep.reality_check_pvalue:.3f}**")
    if rep.significant_hours:
        add(f"- Hours surviving the familywise test: "
            f"**{', '.join(f'{h:02d} UTC' for h in rep.significant_hours)}**")
    else:
        add("- **No hour-of-day pattern survives multiple-testing control.**"
            " Apparent seasonality in the raw table is consistent with chance.")
    add("\n---\n_A pattern that does not survive the reality check must not be"
        " traded, regardless of how good its row looks._")
    return "\n".join(L)
