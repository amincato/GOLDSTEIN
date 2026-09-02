"""Offline tests for the century gold series (no network, pure functions)."""
import numpy as np
import pandas as pd

from goldstein.data import history


def test_official_peg_values_and_revaluation():
    peg = history.official_peg_monthly()
    assert peg.index[0] == pd.Timestamp("1920-01-31")
    assert peg.index[-1] == pd.Timestamp("1967-12-31")
    assert float(peg.loc["1933-12-31", "close"]) == 20.67
    assert float(peg.loc["1934-01-31", "close"]) == 20.67
    assert float(peg.loc["1934-02-28", "close"]) == 35.00
    assert (peg["source"] == "official_peg").all()
    # continuous monthly index
    assert (peg.index.to_series().diff().dt.days.dropna() <= 31).all()


def _fake_daily(start, end, level):
    idx = pd.date_range(start, end, freq="B")
    close = level * np.exp(np.linspace(0, 0.05, len(idx)))
    return pd.DataFrame({"close": close, "source": "fake"}, index=idx)


def test_splice_later_segment_wins_on_overlap():
    a = _fake_daily("2000-01-03", "2005-12-30", 300.0)
    b = _fake_daily("2004-01-01", "2010-12-31", 400.0)
    b["source"] = "winner"
    df = history.splice([a, b])
    assert df.index.is_monotonic_increasing
    assert not df.index.duplicated().any()
    overlap_day = df.loc["2004-06-01":"2004-06-08"]
    assert (overlap_day["source"] == "winner").all()


def test_validate_flags_gaps_and_late_start():
    df = history.splice(
        [history.official_peg_monthly(), _fake_daily("1975-01-01", "1980-01-01", 150)]
    )
    problems = history.validate_century(df)
    assert any("gap" in p for p in problems)  # 1968-1974 hole
    ok = history.splice(
        [history.official_peg_monthly(), _fake_daily("1968-01-01", "1990-01-01", 38)]
    )
    assert not any("starts" in p for p in history.validate_century(ok))


def test_real_price_deflates_to_last_common_month():
    idx = pd.date_range("2000-01-31", periods=24, freq="ME")
    close = pd.Series(100.0, index=idx)
    cpi = pd.DataFrame({"value": np.linspace(100, 110, 24)}, index=idx)
    real = history.real_price(close, cpi)
    assert abs(real.iloc[-1] - 100.0) < 1e-9      # base month unchanged
    assert real.iloc[0] > 100.0                   # past deflated upward


def test_drawdown_table_finds_known_episode():
    idx = pd.date_range("2000-01-31", periods=60, freq="ME")
    px = np.concatenate([np.linspace(100, 200, 20),   # rally to peak
                         np.linspace(195, 120, 20),   # -40% drawdown
                         np.linspace(125, 260, 20)])  # recovery + new high
    dd = history.drawdown_table(pd.Series(px, index=idx))
    deepest = dd.iloc[0]
    assert deepest["depth"] < -0.35
    assert deepest["recovered"] != "-"


def test_century_stress_scenarios_from_committed_cache():
    # the repo commits data/cache/XAUUSD_CENTURY.csv, so scenarios must load
    # offline; each replays the full documented window
    from goldstein.config import INSTRUMENTS
    from goldstein.risk import stress

    scen = stress.century_scenarios()
    assert set(scen) == set(stress.CENTURY_EPISODES)
    desc, path, rate = scen["secular_bear_1980_99"]
    assert len(path) > 200 and rate > 0
    total = np.prod([1 + r for r in path]) - 1
    assert total < -0.55                       # the -60% secular bear

    res = stress.run(2.0, INSTRUMENTS["futures"])
    cent = res.table[res.table["type"] == "century"]
    assert len(cent) == len(stress.CENTURY_EPISODES)
    # 2x through the 1980-99 bear with financing must not look survivable
    row = cent[cent["scenario"] == "secular_bear_1980_99"].iloc[0]
    assert row["equity_multiple"] < 0.5
    assert res.survives_all_century is False
    assert res.survives_all_historical in (True, False)  # untouched contract


def test_century_scenarios_missing_cache_is_safe(monkeypatch):
    from goldstein.risk import stress

    monkeypatch.setattr(
        "goldstein.data.providers._read_cache", lambda key: None
    )
    assert stress.century_scenarios() == {}


def test_century_summary_offline_shape():
    df = history.splice(
        [history.official_peg_monthly(), _fake_daily("1968-01-02", "2024-12-31", 38)]
    )
    s = history.century_summary(df, cpi=None)
    assert s["start"].startswith("1920")
    assert "cagr_nominal" in s and np.isfinite(s["cagr_nominal"])
    assert "1970" in s["vol_by_decade"]
    md = history.render_century_markdown(s)
    assert "century series summary" in md and "Deepest drawdowns" in md


def test_realized_variance_from_bars_trade_date_and_min_bars():
    from goldstein.models import volatility as vol

    # two full sessions of 5m bars + one stub day with 3 bars
    idx = pd.date_range("2025-03-03 23:00", periods=2 * 276, freq="5min", tz="UTC")
    rng = np.random.default_rng(1)
    close = 2000 * np.exp(np.cumsum(rng.normal(0, 0.0004, len(idx))))
    bars = pd.DataFrame({"close": close}, index=idx)
    stub = pd.DataFrame(
        {"close": [2000.0, 2001.0, 2002.0]},
        index=pd.date_range("2025-03-06 23:00", periods=3, freq="5min", tz="UTC"),
    )
    rv = vol.realized_variance_from_bars(pd.concat([bars, stub]))
    # 23:00 UTC bars belong to the NEXT CME trade date; stub day dropped
    assert list(rv.index.date.astype(str) if hasattr(rv.index.date, "astype")
                else map(str, rv.index.date)) == ["2025-03-04", "2025-03-05"]
    assert (rv > 0).all()


def test_splice_rv_bias_adjusts_and_switches():
    from goldstein.models import volatility as vol

    days = pd.date_range("2024-01-01", periods=200, freq="D")
    proxy = pd.Series(2e-4, index=days)                 # noisy proxy level
    intraday = pd.Series(1e-4, index=days[100:])        # true RV, half level
    spliced, info = vol.splice_rv(proxy, intraday)
    assert info["har_source"] == "intraday_rv"
    assert info["rv_splice_date"] == str(days[100].date())
    assert abs(info["proxy_bias_factor"] - 0.5) < 1e-9
    assert abs(spliced.loc[days[0]] - 1e-4) < 1e-12     # proxy rescaled
    assert abs(spliced.loc[days[150]] - 1e-4) < 1e-12   # intraday used
    # no intraday -> untouched proxy, documented
    same, info2 = vol.splice_rv(proxy, None)
    assert info2["har_source"] == "daily_proxy" and same.equals(proxy)


def test_forecast_vol_with_and_without_intraday_rv():
    from goldstein.models import volatility as vol

    rng = np.random.default_rng(3)
    days = pd.date_range("2022-01-03", periods=800, freq="B")
    rets = pd.Series(rng.normal(0, 0.01, len(days)), index=days)
    base = vol.forecast_vol(rets)
    assert base.har_source == "daily_proxy" and base.rv_splice_date is None
    rv = pd.Series(1e-4 + rng.normal(0, 1e-5, 300).clip(-5e-5),
                   index=days[-300:])
    enriched = vol.forecast_vol(rets, intraday_rv=rv)
    assert enriched.har_source == "intraday_rv"
    assert enriched.rv_splice_date == str(days[-300].date())
    assert 0.0 < enriched.har < 1.0 and np.isfinite(enriched.blended)


def test_oos_blend_weights_valid_and_deterministic():
    from goldstein.models import volatility as vol

    rng = np.random.default_rng(5)
    days = pd.date_range("2019-01-01", periods=1500, freq="B")
    # regime-switching vol so the models actually differ
    sigma = np.where(np.arange(1500) % 500 < 250, 0.008, 0.018)
    rets = pd.Series(rng.normal(0, sigma), index=days)
    g = vol.fit_garch(rets)
    rv = rets.pow(2)
    w, diag = vol.oos_blend_weights(rets, rv, g)
    assert w is not None and diag["weight_method"] == "oos_qlike"
    assert abs(sum(w.values()) - 1.0) < 1e-9
    assert all(v >= 0.10 - 1e-9 for v in w.values())    # floor respected
    w2, _ = vol.oos_blend_weights(rets, rv, g)
    assert w == w2                                      # deterministic

    short = rets.iloc[:250]
    w3, diag3 = vol.oos_blend_weights(short, short.pow(2), vol.fit_garch(short))
    assert w3 is None and diag3["weight_method"] == "fixed_fallback"


def test_forecast_vol_ci_ordered_and_seeded():
    from goldstein.models import volatility as vol

    rng = np.random.default_rng(7)
    days = pd.date_range("2020-01-01", periods=1200, freq="B")
    # GARCH-ish vol clustering so the fit converges in the sane band
    h, r = 1e-4, []
    for _ in range(len(days)):
        e = rng.normal(0, np.sqrt(h))
        r.append(e)
        h = 5e-6 + 0.08 * e**2 + 0.88 * h
    rets = pd.Series(r, index=days)
    f1 = vol.forecast_vol(rets, seed=1)
    f2 = vol.forecast_vol(rets, seed=1)
    assert (f1.ci_low, f1.ci_high) == (f2.ci_low, f2.ci_high)  # determinism
    assert f1.ci_low is not None and f1.ci_low < f1.ci_high
    assert 0.0 < f1.ci_low < 1.0 and f1.ci_high < 1.0
    assert abs(sum(f1.weights.values()) - 1.0) < 1e-6
    assert f1.weight_method in ("oos_qlike", "fixed_fallback")


def test_deflated_sharpe_deflates():
    from goldstein.backtest import validation as val

    rng = np.random.default_rng(11)
    days = pd.date_range("2020-01-01", periods=1000, freq="B")
    r = pd.Series(rng.normal(0.0005, 0.01, len(days)), index=days)
    psr = val.probabilistic_sharpe(r)
    trials = list(rng.normal(0.02, 0.03, 30))       # 30 lucky-ish trials
    dsr = val.deflated_sharpe(r, trials)
    assert np.isfinite(dsr) and dsr < psr           # deflation must bite
    assert np.isnan(val.deflated_sharpe(r, [0.01]))  # <2 trials -> nan


def test_reality_check_separates_luck_from_skill():
    from goldstein.backtest import validation as val

    rng = np.random.default_rng(13)
    days = pd.date_range("2018-01-01", periods=1500, freq="B")
    bench = pd.Series(rng.normal(0, 0.01, len(days)), index=days)
    lucky = {f"s{i}": bench + pd.Series(rng.normal(0, 0.004, len(days)), index=days)
             for i in range(8)}
    p_null = val.reality_check(lucky, bench, n_boot=300)["p_value"]
    assert p_null > 0.10                            # pure noise family
    skilled = dict(lucky)
    skilled["edge"] = bench + 0.0012                # ~30%/yr genuine excess
    res = val.reality_check(skilled, bench, n_boot=300)
    assert res["p_value"] < 0.05 and res["best_strategy"] == "edge"


def test_futures_roll_cost_charged():
    from goldstein.backtest import engine
    from goldstein.config import INSTRUMENTS

    days = pd.date_range("2020-01-01", periods=600, freq="B")
    px = pd.Series(np.linspace(1800, 2000, len(days)), index=days)
    fut = engine.run(px, 1.0, INSTRUMENTS["futures"])
    etf = engine.run(px, 1.0, INSTRUMENTS["etf1x"])
    assert fut.costs["roll"] > 0
    assert etf.costs["roll"] == 0
    # ~6 rolls/yr * 4bp on ~2.4y of daily accrual
    expected = 6.0 * 0.0004 * (len(days) - 1) / 252
    assert abs(fut.costs["roll"] - expected) < expected * 0.05


def test_cross_check_gold_offline_is_safe(monkeypatch):
    from goldstein.data import providers

    monkeypatch.setattr(providers, "_fetch_stooq",
                        lambda s: (_ for _ in ()).throw(OSError("blocked")))
    out = providers.cross_check_gold()
    assert out["status"] in ("skipped_offline", "no_cache")
