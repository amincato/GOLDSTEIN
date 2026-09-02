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
