"""Offline tests for the perp subproject (synthetic data, no network).

Run:  python -m pytest perp/tests/
"""
import numpy as np
import pandas as pd
import pytest

from perp.backtest.engine import CostParams, ExitRule, simulate_trades
from perp.backtest.metrics import equity_curve, summarize
from perp.backtest.signals import SignalParams, find_signals


@pytest.fixture(scope="module")
def market():
    rng = np.random.default_rng(7)
    n = 20000
    ret = rng.normal(0, 0.006, n) + 0.00002
    close = 2000 * np.exp(np.cumsum(ret))
    o = np.roll(close, 1)
    o[0] = close[0]
    spread = np.abs(rng.normal(0, 0.004, n))
    high = np.maximum(o, close) * (1 + spread)
    low = np.minimum(o, close) * (1 - spread)
    idx = pd.date_range("2021-01-01", periods=n, freq="1h", tz="UTC")
    df1h = pd.DataFrame(
        {"open": o, "high": high, "low": low, "close": close, "volume": 1.0},
        index=idx,
    )
    df4h = (
        df1h.resample("4h")
        .agg({"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"})
        .dropna()
    )
    return df1h, df4h


@pytest.mark.parametrize("entry_mode", ["close", "pivot"])
def test_signals_found_and_no_lookahead(market, entry_mode):
    df1h, df4h = market
    params = SignalParams(require_sr=False, entry_mode=entry_mode)
    full = find_signals(df1h, df4h, params)
    assert len(full) > 100  # both sides fire on 20k random-walk candles
    assert set(full["side"].unique()) == {1, -1}
    cut_n = 15000
    cut = find_signals(
        df1h.iloc[:cut_n], df4h[df4h.index < df1h.index[cut_n]], params
    )
    cols = ["time", "side", "entry", "pivot_time", "prev_pivot_time", "sr_ok"]
    a = full[full.t_index < cut_n].reset_index(drop=True)[cols]
    assert a.equals(cut.reset_index(drop=True)[cols])


def test_close_mode_enters_at_the_divergence_candle(market):
    df1h, df4h = market
    sigs = find_signals(df1h, df4h, SignalParams(require_sr=False))
    assert (sigs["time"] == sigs["pivot_time"]).all()  # zero entry lag


def test_engine_liquidation_dominates_at_high_leverage(market):
    df1h, df4h = market
    sigs = find_signals(df1h, df4h, SignalParams(require_sr=False))
    rule = ExitRule("fixed", 0.02, 0.01)
    s10 = summarize(simulate_trades(df1h, sigs, 10, rule, CostParams()))
    s100 = summarize(simulate_trades(df1h, sigs, 100, rule, CostParams()))
    # liq distance at 10x (9%) >> SL (1%): never liquidated; at 100x (0.9%)
    # liquidation must fire before the 1% stop can.
    assert s10["liq_rate"] == 0
    assert s100["liq_rate"] > 0.5
    closed = simulate_trades(df1h, sigs, 100, rule, CostParams())
    assert closed["pnl_margin"].min() >= -1.0  # isolated margin floor


def test_engine_determinism(market):
    df1h, df4h = market
    sigs = find_signals(df1h, df4h, SignalParams(require_sr=False))
    rule = ExitRule("atr", 2.0, 1.0)
    t1 = simulate_trades(df1h, sigs, 30, rule, CostParams())
    t2 = simulate_trades(df1h, sigs, 30, rule, CostParams())
    assert t1.equals(t2)


def test_equity_curve_ruin_stops_at_zero():
    eq = equity_curve(np.array([-1.0, 0.5, 0.5]), 500.0, 1.0)
    assert eq[1] == 0.0 and eq[-1] == 0.0
