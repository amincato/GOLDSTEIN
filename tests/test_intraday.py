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
    assert set(v["walk_forward"]) == {"orb", "vwap_reversion", "momentum_burst"}
    assert len(v["cost_sensitivity"]) == 15
    md = iv.render_markdown(v)
    assert "Cost sensitivity" in md and "Walk-forward" in md
