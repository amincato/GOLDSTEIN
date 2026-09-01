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
