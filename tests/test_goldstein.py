"""Smoke + correctness tests, all offline (synthetic data only)."""

import numpy as np
import pandas as pd
import pytest

from goldstein.backtest import engine, metrics, montecarlo
from goldstein.config import INSTRUMENTS, Settings
from goldstein.data.synthetic import synthetic_gold, synthetic_macro
from goldstein.features import indicators as ind
from goldstein.leverage import decay, sizing
from goldstein.models import regime, signals, volatility


@pytest.fixture(scope="module")
def gold():
    return synthetic_gold(years=8, seed=7)


@pytest.fixture(scope="module")
def rets(gold):
    return ind.log_returns(gold["close"])


def test_synthetic_shape(gold):
    assert len(gold) == 8 * 252
    assert (gold["low"] <= gold["close"]).all()
    assert (gold["high"] >= gold["close"]).all()
    # deterministic
    again = synthetic_gold(years=8, seed=7)
    pd.testing.assert_frame_equal(gold, again)


def test_vol_models(rets):
    vf = volatility.forecast_vol(rets)
    for v in (vf.ewma, vf.garch, vf.har, vf.blended):
        assert 0.02 < v < 1.0
    g = volatility.fit_garch(rets)
    assert 0.0 < g.persistence < 1.0


def test_hmm_regimes(rets):
    h = regime.fit_hmm(rets.iloc[-1500:], n_states=3)
    assert h.current_label in ("calm", "normal", "turbulent")
    # states sorted by vol
    assert h.vols[0] <= h.vols[1] <= h.vols[2]
    # rows of transition matrix sum to 1
    np.testing.assert_allclose(h.transition.sum(axis=1), 1.0, atol=1e-6)


def test_signal_bounds(gold):
    s = signals.compute_signal(gold["close"])
    assert -1.0 <= s.score <= 1.0
    assert s.direction in ("long", "flat", "short")


def test_kelly_math():
    # mu=8%, rf=4%, sigma=15% -> full Kelly = 0.04/0.0225 ≈ 1.78
    k = sizing.kelly_fraction(0.08, 0.15, 0.04, shrink=1.0)
    assert abs(k - 0.04 / 0.0225) < 1e-9
    # growth is maximized exactly at full Kelly (no financing spread)
    g_at = sizing.expected_log_growth(k, 0.08, 0.15, 0.04)
    assert g_at >= sizing.expected_log_growth(k * 0.8, 0.08, 0.15, 0.04)
    assert g_at >= sizing.expected_log_growth(k * 1.2, 0.08, 0.15, 0.04)


def test_advise_flat_when_no_signal():
    adv = sizing.advise(0.05, 0.15, 0.0, 0.0, INSTRUMENTS["futures"], Settings())
    assert adv.recommended == 0.0
    assert adv.direction == "flat"


def test_decay_formula():
    # 3x at 15% vol: 3*2/2 * 0.0225 = 6.75%/yr
    assert abs(decay.decay_rate(3.0, 0.15) - 0.0675) < 1e-12
    assert decay.decay_rate(1.0, 0.30) == 0.0


def test_engine_unlevered_matches_asset(gold):
    inst = INSTRUMENTS["etf1x"]
    s = Settings(transaction_cost=0.0, risk_free=0.0)
    res = engine.run(gold["close"], 1.0, inst, s)
    bh = (1 + gold["close"].pct_change().fillna(0)).cumprod()
    # only the expense ratio should separate them
    drift = (res.equity.iloc[-1] / bh.iloc[-1]) ** (252 / len(gold)) - 1
    assert abs(drift + inst.expense_ratio) < 0.002


def test_engine_leverage_amplifies(gold):
    s = Settings(transaction_cost=0.0)
    r1 = engine.run(gold["close"], 1.0, INSTRUMENTS["futures"], s)
    r2 = engine.run(gold["close"], 2.0, INSTRUMENTS["futures"], s)
    assert r2.stats["ann_vol"] > 1.8 * r1.stats["ann_vol"]


def test_montecarlo_risk_monotonic(rets):
    inst = INSTRUMENTS["cfd"]
    s = Settings(mc_paths=400, mc_horizon_days=252)
    simple = rets.apply(np.expm1)
    low = montecarlo.run(simple, 1.0, inst, s)
    high = montecarlo.run(simple, 4.0, inst, s)
    assert high.prob_dd_50 >= low.prob_dd_50
    assert high.expected_max_drawdown <= low.expected_max_drawdown


def test_stress_liquidation_detection():
    from goldstein.risk import stress

    res_low = stress.run(1.0, INSTRUMENTS["futures"])
    res_high = stress.run(10.0, INSTRUMENTS["futures"])
    assert not res_low.table["margin_liquidation"].any()
    assert res_high.table["margin_liquidation"].any()
    assert not res_high.survives_all_historical


def test_metrics_sane():
    r = pd.Series(np.random.default_rng(1).normal(0.0004, 0.01, 1000))
    stats = metrics.summarize(r)
    assert stats["max_drawdown"] <= 0
    assert 0.05 < stats["ann_vol"] < 0.30


def test_full_analysis_offline(tmp_path, monkeypatch):
    """End-to-end pipeline on synthetic data (cache dir empty, no network)."""
    import goldstein.data.providers as providers
    import goldstein.report.generate as gen

    monkeypatch.setattr(providers, "CACHE_DIR", tmp_path)
    monkeypatch.setattr(providers, "_fetch_live", lambda spec: None)
    a = gen.analyze("futures", 10_000.0, Settings(mc_paths=200, lookback_years=6))
    assert a["demo_data"] is True
    assert a["leverage_advice"]["recommended"] >= 0.0
    md = gen.render_markdown(a)
    assert "DEMO DATA" in md and "Leverage recommendation" in md
