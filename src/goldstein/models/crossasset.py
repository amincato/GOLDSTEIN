"""Cross-asset analytics: assets that historically co-move with gold.

Three outputs feed the rest of the platform:
1. Rolling correlation/beta panel vs gold (63d and 252d) — silver, miners,
   DXY, S&P 500, WTI, BTC — so regime shifts in co-movement are visible.
2. Lead-lag profile vs real-yield changes (gold's dominant macro driver).
3. A confirmation score in [-1, +1]: do the correlated assets confirm the
   gold signal? Silver and miners typically LEAD gold in metal bull moves
   (higher beta), while a rallying dollar contradicts gold strength. The
   score becomes one component of the signal ensemble.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from ..config import TRADING_DAYS
from ..features import indicators as ind


@dataclass
class CrossAssetResult:
    correlations: pd.DataFrame        # index=asset, cols=corr_63d, corr_252d, beta_252d
    gold_silver_ratio_z: float | None
    miners_relative_mom: float | None # GDX vs gold 6m relative momentum
    lead_lag_real_yield: dict         # lag (days) -> corr(gold_ret_t, d_real_t-lag)
    confirmation_score: float         # [-1, 1]
    components: dict = field(default_factory=dict)


def _aligned_returns(gold: pd.Series, others: dict[str, pd.Series],
                     years: int = 3) -> pd.DataFrame:
    frames = {"XAUUSD": np.log(gold / gold.shift(1))}
    for k, s in others.items():
        if s is not None and len(s) > 300:
            frames[k] = np.log(s / s.shift(1))
    df = pd.DataFrame(frames).dropna()
    return df.iloc[-years * TRADING_DAYS:]


def analyze(gold_close: pd.Series, others: dict[str, pd.Series],
            real10y: pd.Series | None = None) -> CrossAssetResult:
    rets = _aligned_returns(gold_close, others)
    g = rets["XAUUSD"]

    rows = []
    for k in rets.columns:
        if k == "XAUUSD":
            continue
        r = rets[k]
        c63 = float(g.iloc[-63:].corr(r.iloc[-63:]))
        c252 = float(g.iloc[-252:].corr(r.iloc[-252:]))
        var_g = float(g.iloc[-252:].var())
        beta = float(g.iloc[-252:].cov(r.iloc[-252:]) / max(var_g, 1e-12))
        rows.append({"asset": k, "corr_63d": c63, "corr_252d": c252,
                     "beta_vs_gold_252d": beta})
    corr_df = pd.DataFrame(rows).set_index("asset") if rows else pd.DataFrame()

    comps: dict[str, float] = {}

    # silver confirms: same-direction 6m momentum, tanh-scaled
    silver = others.get("XAGUSD")
    gs_z = None
    if silver is not None and len(silver) > 300:
        m = ind.momentum(silver, 126).iloc[-1]
        if np.isfinite(m):
            comps["silver_momentum"] = float(np.tanh(m / 0.12))
        ratio = (gold_close / silver.reindex(gold_close.index).ffill()).dropna()
        if len(ratio) > 260:
            z = ind.zscore(ratio, 252).iloc[-1]
            if np.isfinite(z):
                # gold rich vs silver = late-stage metal move -> mild negative
                gs_z = float(z)
                comps["gold_silver_ratio"] = float(np.clip(-z / 3.0, -0.5, 0.5))

    # miners lead: GDX outperforming gold = risk appetite for the metal
    miners = others.get("GDX")
    rel_mom = None
    if miners is not None and len(miners) > 300:
        gm = ind.momentum(gold_close, 126).iloc[-1]
        mm = ind.momentum(miners, 126).iloc[-1]
        if np.isfinite(gm) and np.isfinite(mm):
            rel_mom = float(mm - gm)
            comps["miners_leadership"] = float(np.tanh(rel_mom / 0.15))

    # dollar contradicts: DXY 6m strength is a headwind
    dxy = others.get("DXY")
    if dxy is not None and len(dxy) > 300:
        dm = ind.momentum(dxy, 126).iloc[-1]
        if np.isfinite(dm):
            comps["dollar_headwind"] = float(np.tanh(-dm / 0.05))

    # lead-lag vs real-yield changes
    lead_lag: dict[int, float] = {}
    if real10y is not None and len(real10y) > 300:
        d_real = real10y.diff().reindex(g.index).fillna(0.0)
        for lag in (0, 1, 2, 5, 10):
            c = float(g.iloc[-756:].corr(d_real.shift(lag).iloc[-756:]))
            if np.isfinite(c):
                lead_lag[lag] = c

    score = float(np.mean(list(comps.values()))) if comps else 0.0
    return CrossAssetResult(
        correlations=corr_df,
        gold_silver_ratio_z=gs_z,
        miners_relative_mom=rel_mom,
        lead_lag_real_yield=lead_lag,
        confirmation_score=score,
        components=comps,
    )
