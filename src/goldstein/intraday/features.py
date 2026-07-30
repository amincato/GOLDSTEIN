"""Microstructure features for scalping signals and analytics."""

from __future__ import annotations

import numpy as np
import pandas as pd

from .data import session_of


def add_features(bars: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of the bars enriched with the standard feature set."""
    df = bars.copy()
    day = df.index.normalize()
    df["session"] = session_of(df.index)
    df["date"] = day

    # session VWAP (resets daily): the scalper's fair-value anchor
    typical = (df["high"] + df["low"] + df["close"]) / 3
    pv = (typical * df["volume"]).groupby(day).cumsum()
    vv = df["volume"].groupby(day).cumsum().replace(0, np.nan)
    df["vwap"] = pv / vv

    # ATR in price units (14 bars) — stop/target unit of account
    prev_close = df["close"].shift(1)
    tr = pd.concat(
        [df["high"] - df["low"],
         (df["high"] - prev_close).abs(),
         (df["low"] - prev_close).abs()], axis=1
    ).max(axis=1)
    df["atr"] = tr.ewm(alpha=1 / 14, adjust=False).mean()

    # VWAP z-score: distance from fair value in ATR units
    df["vwap_z"] = (df["close"] - df["vwap"]) / df["atr"].replace(0, np.nan)

    # rolling volume ratio: participation confirmation
    df["vol_ratio"] = df["volume"] / df["volume"].rolling(48).median().replace(0, np.nan)

    # bar range expansion vs recent
    rng = df["high"] - df["low"]
    df["range_ratio"] = rng / rng.rolling(48).median().replace(0, np.nan)

    return df


def opening_range(df: pd.DataFrame, session: str = "overlap",
                  n_bars: int = 6) -> pd.DataFrame:
    """High/low of the first `n_bars` of a session, broadcast to that day's
    later bars (NaN inside the formation window). 6 x 5m = 30 minutes."""
    mask = df["session"] == session
    sess = df[mask]
    grp = sess.groupby(sess["date"])
    rank = grp.cumcount()
    orh = sess["high"].where(rank < n_bars).groupby(sess["date"]).transform("max")
    orl = sess["low"].where(rank < n_bars).groupby(sess["date"]).transform("min")
    out = pd.DataFrame(index=df.index,
                       columns=["or_high", "or_low", "or_ready"], dtype=float)
    out.loc[mask, "or_high"] = orh
    out.loc[mask, "or_low"] = orl
    out.loc[mask, "or_ready"] = (rank >= n_bars).astype(float)
    return out


def session_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Per-session realized vol / range / volume profile — tells the scalper
    WHEN the market actually pays."""
    feat = df if "session" in df.columns else add_features(df)
    rets = np.log(feat["close"] / feat["close"].shift(1))
    bars_per_day = max(1, len(feat) // max(1, feat["date"].nunique()))
    g = feat.assign(ret=rets).groupby("session", observed=True)
    out = pd.DataFrame({
        "bars": g.size(),
        "ann_vol": g["ret"].std() * np.sqrt(252 * bars_per_day),
        "avg_range_ticks": (g["high"].mean() - g["low"].mean()) / 0.10,
        "avg_volume": g["volume"].mean(),
        "avg_abs_move_ticks": g["ret"].apply(lambda s: float(np.abs(s).mean()))
        * feat["close"].mean() / 0.10,
    })
    order = ["asia", "london", "overlap", "ny", "late"]
    return out.reindex([s for s in order if s in out.index])
