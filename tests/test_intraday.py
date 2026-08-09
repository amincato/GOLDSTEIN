"""Tests for the intraday scalping layer (all offline / synthetic)."""

import numpy as np
import pandas as pd
import pytest

from goldstein.intraday.contracts import CONTRACTS, CostModel
from goldstein.intraday.data import session_of, synthetic_intraday
from goldstein.intraday.engine import RiskRules, run
from goldstein.intraday.features import add_features, opening_range, session_stats
from goldstein.intraday.strategies import STRATEGIES, momentum_burst, orb_breakout


@pytest.fixture(scope="module")
def bars():
    return synthetic_intraday(days=40, interval="5m", seed=9)


@pytest.fixture(scope="module")
def feat(bars):
    return add_features(bars)


def test_synthetic_intraday_shape(bars):
    assert len(bars) > 5000
    assert (bars["high"] >= bars[["open", "close"]].max(axis=1) - 1e-9).all()
    assert (bars["low"] <= bars[["open", "close"]].min(axis=1) + 1e-9).all()
    again = synthetic_intraday(days=40, interval="5m", seed=9)
    pd.testing.assert_frame_equal(bars, again)


def test_sessions_and_vol_profile(feat):
    assert set(session_of(feat.index).unique()) <= {"asia", "london", "overlap", "ny", "late"}
    stats = session_stats(feat)
    # synthetic calibration: liquid sessions clearly beat the quiet ones
    assert stats.loc["overlap", "ann_vol"] > stats.loc["asia", "ann_vol"]
    assert stats.loc["overlap", "ann_vol"] > 2 * stats.loc["late", "ann_vol"]


def test_vwap_resets_daily(feat):
    first_bars = feat.groupby("date").head(1)
    typical = (first_bars["high"] + first_bars["low"] + first_bars["close"]) / 3
    np.testing.assert_allclose(first_bars["vwap"], typical, rtol=1e-9)


def test_opening_range(feat):
    orng = opening_range(feat, session="overlap", n_bars=6)
    ready = orng["or_ready"] == 1.0
    assert ready.any()
    assert (orng.loc[ready, "or_high"] >= orng.loc[ready, "or_low"]).all()


def test_engine_costs_reduce_pnl(feat):
    contract = CONTRACTS["MGC"]
    sig = momentum_burst(feat)
    relaxed = RiskRules(daily_loss_limit_r=1e9, max_trades_per_day=10_000)
    free = run(feat, sig, contract, CostModel(0.0, 0.0, 0.0), relaxed)
    costly = run(feat, sig, contract, CostModel(2.0, 1.2, 1.0), relaxed)
    assert free.stats["n_trades"] > 5 and costly.stats["n_trades"] > 5
    # ~3.2 ticks round-trip cost (+stop slippage) must show up as drag;
    # trade counts can differ slightly because entry prices shift with spread
    drag = free.stats["expectancy_ticks"] - costly.stats["expectancy_ticks"]
    assert drag >= 2.5


def test_engine_stop_is_conservative():
    """A bar spanning both stop and target must fill the stop."""
    idx = pd.date_range("2026-01-05 13:00", periods=5, freq="5min", tz="UTC")
    bars = pd.DataFrame({
        "open": [100.0, 100.0, 100.0, 100.0, 100.0],
        "high": [100.1, 100.1, 105.0, 100.1, 100.1],
        "low": [99.9, 99.9, 95.0, 99.9, 99.9],
        "close": [100.0, 100.0, 100.0, 100.0, 100.0],
        "volume": [1000.0] * 5,
    }, index=idx)
    feat = add_features(bars)
    sig = pd.DataFrame({"dir": [0, 1, 0, 0, 0],
                        "stop_ticks": [0, 10, 0, 0, 0],
                        "target_ticks": [0, 10, 0, 0, 0]}, index=idx)
    res = run(feat, sig, CONTRACTS["MGC"], CostModel(0.0, 0.0, 0.0))
    assert res.stats["n_trades"] == 1
    assert res.trades[0].exit_reason == "stop"
    assert res.trades[0].net_ticks == pytest.approx(-10.0)


def test_engine_daily_loss_limit(feat):
    contract = CONTRACTS["MGC"]
    sig = momentum_burst(feat)
    strict = run(feat, sig, contract, CostModel(3.0, 1.2, 2.0),
                 RiskRules(daily_loss_limit_r=1.0, max_trades_per_day=50))
    loose = run(feat, sig, contract, CostModel(3.0, 1.2, 2.0),
                RiskRules(daily_loss_limit_r=50.0, max_trades_per_day=50))
    assert strict.stats["n_trades"] <= loose.stats["n_trades"]


def test_strategies_emit_valid_signals(feat):
    for name, fn in STRATEGIES.items():
        sig = fn(feat)
        active = sig["dir"] != 0
        assert active.sum() > 0, name
        assert (sig.loc[active, "stop_ticks"] > 0).all(), name
        assert (sig.loc[active, "target_ticks"] > 0).all(), name
        assert set(np.unique(sig["dir"])) <= {-1.0, 0.0, 1.0}


def test_bias_filters_direction(feat):
    both = orb_breakout(feat)
    long_only = orb_breakout(feat, bias=1)
    assert (long_only["dir"] >= 0).all()
    assert (long_only["dir"] == 1).sum() <= (both["dir"] == 1).sum()


def test_validation_pipeline(tmp_path, monkeypatch):
    import goldstein.intraday.data as idata
    from goldstein.intraday import validate as iv

    monkeypatch.setattr(idata, "CACHE_DIR", tmp_path)
    monkeypatch.setattr(idata, "fetch_yahoo_intraday", lambda *a, **k: None)
    v = iv.run_validation("MGC", "5m")
    assert v["demo_data"] is True
    assert set(v["walk_forward"]) == {"orb", "vwap_reversion",
                                      "momentum_burst", "session_drift"}
    assert len(v["cost_sensitivity"]) == 20
    md = iv.render_markdown(v)
    assert "Cost sensitivity" in md and "Walk-forward" in md


def test_pattern_miner_detects_planted_effect():
    """Inject a strong hour-13 drift into random bars: the miner must find it
    and it must survive the reality check; clean noise must NOT."""
    from goldstein.intraday import patterns as pat

    rng = np.random.default_rng(5)
    idx = pd.date_range("2024-01-01", periods=24 * 500, freq="60min", tz="UTC")
    idx = idx[idx.dayofweek < 5]
    rets = rng.normal(0, 0.0015, len(idx))
    planted = rets.copy()
    planted[idx.hour == 13] += 0.0025          # ~1.7 sigma daily drift at 13:00
    for name, r, expect in (("noise", rets, False), ("planted", planted, True)):
        close = 2000 * np.exp(np.cumsum(r))
        bars = pd.DataFrame({"open": close, "high": close, "low": close,
                             "close": close, "volume": 100.0}, index=idx)
        rep = pat.mine(bars, n_bootstrap=200, seed=1)
        if expect:
            assert rep.best_hour == 13
            assert rep.reality_check_pvalue < 0.05
            assert 13 in rep.significant_hours
        else:
            assert rep.reality_check_pvalue > 0.05 or not rep.significant_hours


def test_session_drift_signals(feat):
    from goldstein.intraday.strategies import session_drift

    sig = session_drift(feat, entry_hour=12, direction=-1)
    active = sig["dir"] != 0
    assert active.sum() > 10
    assert (sig.loc[active, "dir"] == -1).all()
    # at most one entry per day
    per_day = active.groupby(feat["date"]).sum()
    assert per_day.max() <= 1
    # entries fill at the 12:00 bar open (signal on the bar before)
    next_hours = pd.Series(np.roll(feat.index.hour, -1), index=feat.index)
    assert (next_hours[active] == 12).all()


def test_dukascopy_decode_roundtrip():
    import lzma
    import struct

    from goldstein.intraday.dukascopy import decode_bi5, ticks_to_bars

    hour = pd.Timestamp("2026-03-02 14:00", tz="UTC")
    records = b"".join(
        struct.pack(">IIIff", ms, int(px * 1000) + 50, int(px * 1000) - 50, 1.0, 1.0)
        for ms, px in [(0, 4000.0), (60_000, 4001.5), (299_000, 3999.0),
                       (1_800_000, 4005.0), (3_599_000, 4002.2)]
    )
    ticks = decode_bi5(lzma.compress(records), hour)
    assert ticks is not None and len(ticks) == 5
    assert abs(ticks["mid"].iloc[0] - 4000.0) < 0.2
    bars = ticks_to_bars(ticks, "5min")
    assert len(bars) >= 2
    assert bars["volume"].sum() == 5
    assert decode_bi5(b"", hour) is None
    assert decode_bi5(b"not-lzma", hour) is None


def _synthetic_perp_and_ref(seed=3, days=30, basis_phi=0.97, basis_sig=2e-4):
    """Reference random walk + perp = ref * (1 + AR(1) basis)."""
    rng = np.random.default_rng(seed)
    idx = pd.date_range("2026-06-01", periods=days * 288, freq="5min", tz="UTC")
    ref = 4000 * np.exp(np.cumsum(rng.normal(0, 8e-4, len(idx))))
    basis = np.zeros(len(idx))
    for t in range(1, len(idx)):
        basis[t] = basis_phi * basis[t - 1] + basis_sig * rng.standard_normal()
    perp = ref * (1 + basis)
    return (pd.Series(perp, index=idx, name="perp"),
            pd.Series(ref, index=idx, name="ref"))


def test_hyperliquid_basis_analysis_detects_mean_reversion():
    from goldstein.intraday.hyperliquid import analyze_basis

    perp, ref = _synthetic_perp_and_ref()
    funding = pd.DataFrame(
        {"funding_hourly": np.full(24 * 30, 1.25e-5), "premium": 0.0},
        index=pd.date_range("2026-06-01", periods=24 * 30, freq="1h", tz="UTC"))
    out = analyze_basis(perp, ref, funding)
    assert out["overlap_bars"] > 500
    b = out["basis"]
    assert 0.9 < b["ar1_phi"] < 1.0           # planted AR(1) recovered
    assert b["half_life_bars"] is not None
    assert abs(b["mean_bps"]) < 5             # basis centred near zero
    # lead-lag: contemporaneous corr must dominate
    ll = out["lead_lag"]
    assert ll["+0min"] > 0.9
    # funding: 1.25e-5 hourly ~ 11% APR; 50x cost ~1.5%/day
    assert abs(out["funding"]["mean_apr"] - 1.25e-5 * 24 * 365) < 1e-3
    assert 1.0 < out["funding"]["cost_50x_per_day_pct_equity"] < 2.0


def test_hyperliquid_market_open_mask():
    from goldstein.intraday.hyperliquid import _ref_market_open

    idx = pd.DatetimeIndex([
        "2026-07-25 12:00",  # Saturday -> closed
        "2026-07-24 22:00",  # Friday 22 UTC -> closed
        "2026-07-26 23:00",  # Sunday 23 UTC -> open
        "2026-07-27 14:00",  # Monday -> open
        "2026-07-27 21:30",  # daily break -> closed
    ], tz="UTC")
    mask = _ref_market_open(idx)
    assert list(mask) == [False, False, True, True, False]


def test_hyperliquid_goldish_discovery_filter():
    from goldstein.intraday.hyperliquid import _is_goldish

    assert _is_goldish("XAU")
    assert _is_goldish("km:GOLD")
    assert _is_goldish("PAXG")
    assert not _is_goldish("BTC")
    assert not _is_goldish("SOL")
