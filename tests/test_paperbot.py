"""Paper bot accounting tests — all offline, market mocked."""

import json
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd
import pytest

from goldstein import paperbot


def _mk_candles(px0: float, drift: float, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    idx = pd.date_range("2026-07-01", periods=24 * 30, freq="1h", tz="UTC")
    rets = drift / 24 + 0.02 / np.sqrt(24 * 365) * rng.standard_normal(len(idx))
    close = px0 * np.exp(np.cumsum(rets))
    return pd.DataFrame({"open": close, "high": close, "low": close,
                         "close": close, "volume": 1000.0, "trades": 10},
                        index=idx)


@pytest.fixture
def market(tmp_path, monkeypatch):
    monkeypatch.setattr(paperbot, "STATE_PATH", tmp_path / "state.json")
    monkeypatch.setattr(paperbot, "HISTORY_PATH", tmp_path / "history.csv")
    monkeypatch.setattr(paperbot, "REPORT_MD", tmp_path / "latest.md")

    candles = {
        "BTC": _mk_candles(60_000, 0.004, 1),     # strong uptrend
        "ETH": _mk_candles(3_000, -0.004, 2),     # strong downtrend
        "SOL": _mk_candles(150, 0.0, 3),          # flat -> no conviction
    }
    universe = [
        {"coin": c, "mark_px": float(candles[c]["close"].iloc[-1]),
         "funding_hourly": 1e-5, "day_volume": 1e9}
        for c in candles
    ]
    monkeypatch.setattr(paperbot, "fetch_universe", lambda: universe)
    monkeypatch.setattr(paperbot.hl, "fetch_candles",
                        lambda coin, interval, days: candles[coin])
    return candles, universe


def test_cycle_opens_positions_and_respects_gross_cap(market):
    s = paperbot.run_cycle(datetime(2026, 8, 9, 12, tzinfo=timezone.utc))
    assert s["n_positions"] >= 1
    assert s["gross_leverage"] <= paperbot.MAX_GROSS + 1e-6
    state = json.loads(paperbot.STATE_PATH.read_text())
    # momentum: long the uptrend, short the downtrend
    if "BTC" in state["positions"]:
        assert state["positions"]["BTC"]["sz"] > 0
    if "ETH" in state["positions"]:
        assert state["positions"]["ETH"]["sz"] < 0
    # fees were charged: cash + notional accounting < initial capital
    assert s["equity"] < paperbot.INITIAL_CAPITAL


def test_two_cycles_accounting_consistent(market):
    t0 = datetime(2026, 8, 9, 12, tzinfo=timezone.utc)
    s1 = paperbot.run_cycle(t0)
    s2 = paperbot.run_cycle(t0 + timedelta(days=1))
    # same prices second run: only fees + funding can move equity, slightly
    assert abs(s2["equity"] - s1["equity"]) < 0.02 * paperbot.INITIAL_CAPITAL
    hist = paperbot.HISTORY_PATH.read_text().strip().splitlines()
    assert len(hist) == 3                      # header + 2 rows


def test_kill_switch_flattens(market, monkeypatch):
    t0 = datetime(2026, 8, 9, 12, tzinfo=timezone.utc)
    paperbot.run_cycle(t0)
    state = json.loads(paperbot.STATE_PATH.read_text())
    state["cash"] -= 0.5 * paperbot.INITIAL_CAPITAL     # simulate big loss
    paperbot.STATE_PATH.write_text(json.dumps(state))
    s = paperbot.run_cycle(t0 + timedelta(days=1))
    assert s["halted"] is True
    assert s["n_positions"] == 0
    s3 = paperbot.run_cycle(t0 + timedelta(days=2))
    assert s3["halted"] is True                # stays flat once halted


def test_funding_tilt_prefers_receiving():
    w_pay = paperbot.compute_target_weights(
        {"X": _mk_candles(100, 0.004, 5)}, {"X": 5e-5})    # longs pay a lot
    w_recv = paperbot.compute_target_weights(
        {"X": _mk_candles(100, 0.004, 5)}, {"X": -5e-5})   # longs receive
    if "X" in w_pay and "X" in w_recv:
        assert w_recv["X"] > w_pay["X"]
