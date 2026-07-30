"""Scalping strategy library.

Each strategy is a pure function: enriched bars -> signal DataFrame
(dir, stop_ticks, target_ticks), signal evaluated on bar close, filled next
open by the engine. All stops/targets are ATR-scaled so parameters transfer
across volatility regimes. An optional `bias` (from the daily platform
signal) restricts trade direction — scalping WITH the higher-timeframe wind.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .features import add_features, opening_range

TICK = 0.10


def _empty(index) -> pd.DataFrame:
    return pd.DataFrame(
        {"dir": 0.0, "stop_ticks": 0.0, "target_ticks": 0.0}, index=index
    )


def _atr_ticks(feat: pd.DataFrame) -> pd.Series:
    return (feat["atr"] / TICK).clip(lower=4.0)


def _apply_bias(sig: pd.DataFrame, bias: int | None) -> pd.DataFrame:
    if bias is not None and bias != 0:
        sig.loc[np.sign(sig["dir"]) != np.sign(bias), "dir"] = 0.0
    return sig


def orb_breakout(bars: pd.DataFrame, session: str = "overlap", n_bars: int = 6,
                 stop_atr: float = 1.0, target_atr: float = 1.5,
                 vol_confirm: float = 1.2, bias: int | None = None) -> pd.DataFrame:
    """Opening-range breakout on the London/NY overlap: first 30m defines the
    range; trade the first close beyond it with volume confirmation."""
    feat = bars if "vwap" in bars.columns else add_features(bars)
    orng = opening_range(feat, session=session, n_bars=n_bars)
    sig = _empty(feat.index)
    atr_t = _atr_ticks(feat)

    ready = orng["or_ready"] == 1.0
    long_break = ready & (feat["close"] > orng["or_high"]) & (feat["vol_ratio"] >= vol_confirm)
    short_break = ready & (feat["close"] < orng["or_low"]) & (feat["vol_ratio"] >= vol_confirm)
    # only the FIRST breakout per day per direction
    day = feat["date"]
    long_first = long_break & ~long_break.groupby(day).cummax().shift(1).fillna(False)
    short_first = short_break & ~short_break.groupby(day).cummax().shift(1).fillna(False)

    sig.loc[long_first, "dir"] = 1.0
    sig.loc[short_first, "dir"] = -1.0
    active = long_first | short_first
    sig.loc[active, "stop_ticks"] = (atr_t * stop_atr)[active]
    sig.loc[active, "target_ticks"] = (atr_t * target_atr)[active]
    return _apply_bias(sig, bias)


def vwap_reversion(bars: pd.DataFrame, z_entry: float = 1.8,
                   stop_atr: float = 1.2, target_atr: float = 1.0,
                   sessions: tuple = ("london", "overlap", "ny"),
                   max_range_ratio: float = 2.5,
                   bias: int | None = None) -> pd.DataFrame:
    """Fade stretched moves back toward session VWAP — classic mean-reversion
    scalp. Skips bars in a range explosion (that's breakout, not reversion,
    territory) and only trades liquid sessions."""
    feat = bars if "vwap" in bars.columns else add_features(bars)
    sig = _empty(feat.index)
    atr_t = _atr_ticks(feat)

    ok = feat["session"].isin(sessions) & (feat["range_ratio"] < max_range_ratio)
    stretched_up = ok & (feat["vwap_z"] > z_entry)
    stretched_dn = ok & (feat["vwap_z"] < -z_entry)
    # trigger only on the first bar crossing the threshold, not continuously
    first_up = stretched_up & ~stretched_up.shift(1, fill_value=False)
    first_dn = stretched_dn & ~stretched_dn.shift(1, fill_value=False)

    sig.loc[first_dn, "dir"] = 1.0      # stretched below VWAP -> buy the fade
    sig.loc[first_up, "dir"] = -1.0
    active = first_up | first_dn
    sig.loc[active, "stop_ticks"] = (atr_t * stop_atr)[active]
    sig.loc[active, "target_ticks"] = (atr_t * target_atr)[active]
    return _apply_bias(sig, bias)


def momentum_burst(bars: pd.DataFrame, range_trigger: float = 2.0,
                   vol_trigger: float = 2.0, stop_atr: float = 0.8,
                   target_atr: float = 1.6,
                   sessions: tuple = ("london", "overlap", "ny"),
                   bias: int | None = None) -> pd.DataFrame:
    """Trade continuation after a range+volume expansion bar: enter in the
    bar's direction with a tight stop — the pure scalp: small risk, quick
    asymmetric target."""
    feat = bars if "vwap" in bars.columns else add_features(bars)
    sig = _empty(feat.index)
    atr_t = _atr_ticks(feat)

    burst = (
        feat["session"].isin(sessions)
        & (feat["range_ratio"] >= range_trigger)
        & (feat["vol_ratio"] >= vol_trigger)
    )
    up = burst & (feat["close"] > feat["open"])
    dn = burst & (feat["close"] < feat["open"])
    sig.loc[up, "dir"] = 1.0
    sig.loc[dn, "dir"] = -1.0
    active = up | dn
    sig.loc[active, "stop_ticks"] = (atr_t * stop_atr)[active]
    sig.loc[active, "target_ticks"] = (atr_t * target_atr)[active]
    return _apply_bias(sig, bias)


def session_drift(bars: pd.DataFrame, entry_hour: int = 12, direction: int = 1,
                  stop_atr: float = 1.5, bias: int | None = None) -> pd.DataFrame:
    """Time-of-day drift trade: enter at a fixed UTC hour in a fixed
    direction, wide ATR stop, no target — the engine flattens at session
    end, so the position simply harvests that session's drift.

    Which (hour, direction) is worth trading is NOT decided here: the
    walk-forward selects it in-sample and judges it out-of-sample, and the
    pattern miner's reality check says whether the effect is real at all.
    """
    feat = bars if "vwap" in bars.columns else add_features(bars)
    sig = _empty(feat.index)
    atr_t = _atr_ticks(feat)

    hours = feat.index.hour
    next_hours = np.roll(hours, -1)
    # signal on the last bar BEFORE entry_hour so the engine fills at its open
    trigger = (next_hours == entry_hour) & (hours != entry_hour)
    trigger[-1] = False
    trigger = pd.Series(trigger, index=feat.index)
    # one entry per day
    first = trigger & ~trigger.groupby(feat["date"]).cummax().shift(1).fillna(False)

    sig.loc[first, "dir"] = float(np.sign(direction))
    sig.loc[first, "stop_ticks"] = (atr_t * stop_atr)[first]
    sig.loc[first, "target_ticks"] = 1e6      # time-based exit only
    return _apply_bias(sig, bias)


STRATEGIES = {
    "orb": orb_breakout,
    "vwap_reversion": vwap_reversion,
    "momentum_burst": momentum_burst,
    "session_drift": session_drift,
}

PARAM_GRID = {
    "orb": [
        {"stop_atr": s, "target_atr": t}
        for s in (0.8, 1.0, 1.3) for t in (1.2, 1.5, 2.0)
    ],
    "vwap_reversion": [
        {"z_entry": z, "stop_atr": s, "target_atr": t}
        for z in (1.5, 1.8, 2.2) for s, t in ((1.2, 1.0), (1.5, 1.2))
    ],
    "momentum_burst": [
        {"range_trigger": r, "stop_atr": s, "target_atr": t}
        for r in (1.8, 2.2) for s, t in ((0.8, 1.6), (1.0, 2.0))
    ],
    # session opens + London AM/PM fix neighborhood + NY morning
    "session_drift": [
        {"entry_hour": h, "direction": d}
        for h in (0, 7, 10, 12, 14, 16) for d in (1, -1)
    ],
}
