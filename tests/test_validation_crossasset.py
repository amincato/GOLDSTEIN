"""Tests for cross-asset analytics, validation suite and autonomous monitor."""

import json

import numpy as np
import pandas as pd
import pytest

from goldstein.backtest import validation
from goldstein.config import Settings
from goldstein.data.synthetic import synthetic_macro, synthetic_price
from goldstein.models import crossasset, signals


@pytest.fixture(scope="module")
def market():
    keys = ["XAUUSD", "XAGUSD", "GDX", "DXY", "SPX", "WTI", "BTC"]
    return {k: synthetic_price(k, years=6, seed=11) for k in keys}


def test_synthetic_price_deterministic_and_distinct(market):
    again = synthetic_price("XAGUSD", years=6, seed=11)
    pd.testing.assert_frame_equal(market["XAGUSD"], again)
    assert not market["XAGUSD"]["close"].equals(market["XAUUSD"]["close"])


def test_synthetic_correlations_realistic(market):
    g = market["XAUUSD"]["close"].pct_change().dropna()
    silver = market["XAGUSD"]["close"].pct_change().dropna()
    dxy = market["DXY"]["close"].pct_change().dropna()
    assert g.corr(silver) > 0.4          # silver strongly positive
    assert g.corr(dxy) < -0.15           # dollar negative


def test_crossasset_analyze(market):
    others = {k: market[k]["close"] for k in
              ("XAGUSD", "GDX", "DXY", "SPX", "WTI", "BTC")}
    real = synthetic_macro("REAL10Y", years=6, seed=11)["value"]
    res = crossasset.analyze(market["XAUUSD"]["close"], others, real)
    assert -1.0 <= res.confirmation_score <= 1.0
    assert len(res.correlations) == 6
    assert set(res.components) >= {"silver_momentum", "dollar_headwind"}
    assert res.correlations.loc["XAGUSD", "corr_252d"] > 0.3
    assert 0 in res.lead_lag_real_yield


def test_signal_uses_cross_score(market):
    close = market["XAUUSD"]["close"]
    s_neutral = signals.compute_signal(close, cross_score=0.0)
    s_confirm = signals.compute_signal(close, cross_score=1.0)
    assert s_confirm.score > s_neutral.score
    assert "cross_asset" in s_confirm.components


def test_probabilistic_sharpe_orders():
    rng = np.random.default_rng(3)
    idx = pd.bdate_range("2015-01-01", periods=1500)
    good = pd.Series(rng.normal(0.0008, 0.01, 1500), index=idx)
    bad = pd.Series(rng.normal(-0.0003, 0.01, 1500), index=idx)
    psr_good = validation.probabilistic_sharpe(good)
    psr_bad = validation.probabilistic_sharpe(bad)
    assert 0.0 <= psr_bad < psr_good <= 1.0
    assert psr_good > 0.9


def test_validation_pipeline_offline(tmp_path, monkeypatch):
    import goldstein.data.providers as providers

    monkeypatch.setattr(providers, "CACHE_DIR", tmp_path)
    monkeypatch.setattr(providers, "_fetch_live", lambda spec: None)
    v = validation.run_validation("futures", Settings(lookback_years=6), quick=True)
    assert v["demo_data"] is True
    names = {r["strategy"] for r in v["strategy_suite"]}
    assert names == {"buy_hold_1x", "constant_2x", "constant_3x",
                     "vol_target", "vol_target_x_signal"}
    assert v["verdict"]["checks_total"] == 5
    assert len(v["walk_forward"]) >= 3
    md = validation.render_markdown(v)
    assert "Walk-forward" in md and "Verdict" in md


def test_monitor_diff_and_history(tmp_path, monkeypatch):
    import goldstein.data.providers as providers
    import goldstein.report.generate as gen
    from goldstein.report import monitor

    monkeypatch.setattr(providers, "CACHE_DIR", tmp_path / "cache")
    monkeypatch.setattr(providers, "_fetch_live", lambda spec: None)
    a = gen.analyze("futures", 10_000.0, Settings(mc_paths=150, lookback_years=6))

    first = monitor.update_latest(a, report_dir=tmp_path / "reports")
    assert first["changed"] is True         # baseline counts as a change
    second = monitor.update_latest(a, report_dir=tmp_path / "reports")
    assert second["changed"] is False       # identical analysis -> no changes

    hist = (tmp_path / "reports" / "history.csv").read_text().strip().splitlines()
    assert len(hist) == 2                   # header + one deduped row

    # a doctored leverage jump must be detected
    b = json.loads(json.dumps(a, default=str))
    b["leverage_advice"]["recommended"] = a["leverage_advice"]["recommended"] + 1.0
    third = monitor.update_latest(b, report_dir=tmp_path / "reports")
    assert third["changed"] is True
    assert any("leverage advice" in c for c in third["changes"])


def test_is_daily_rejects_monthly():
    from goldstein.data.providers import _is_daily

    daily_idx = pd.bdate_range("2020-01-01", periods=300)
    monthly_idx = pd.date_range("2000-01-01", periods=300, freq="MS")
    daily = pd.DataFrame({"close": np.ones(300)}, index=daily_idx)
    monthly = pd.DataFrame({"close": np.ones(300)}, index=monthly_idx)
    assert _is_daily(daily)
    assert not _is_daily(monthly)       # the Yahoo range=max degradation case
    assert not _is_daily(daily.iloc[:50])  # too short


def test_demo_vs_degraded_modes():
    from goldstein.report import monitor

    base = {
        "market": {"last_date": "2026-07-30", "last_price": 4000.0},
        "volatility": {"blended_forecast": 0.15},
        "regime": {"hmm_state": "calm", "macro_label": "neutral"},
        "signal": {"score": 0.2},
        "leverage_advice": {"direction": "long", "recommended": 1.0},
        "monte_carlo": {"prob_ruin": 0.0},
    }
    demo = {**base, "demo_data": True, "synthetic_series": ["XAUUSD"]}
    degraded = {**base, "demo_data": False, "synthetic_series": ["REAL10Y"]}
    real = {**base, "demo_data": False, "synthetic_series": []}
    assert monitor.snapshot(demo)["data_mode"] == "demo"
    assert monitor.snapshot(degraded)["data_mode"] == "degraded"
    assert monitor.snapshot(real)["data_mode"] == "real"
