"""Hourly live alert script (Phase 2).

Evaluates the SAME mechanical signal as the backtester (perp.backtest.signals
— one source of truth) on fresh ccxt candles and sends a Telegram message
when a setup confirms on the latest closed 1H candle.

Parameters come from perp/params_validated.json, written after the backtest
has been run and its parameters approved; until that file exists this script
refuses to run rather than alerting on unvalidated defaults.

Env: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
Run:  python -m perp.alerts.alerts            # single shot (cron-friendly)
      python -m perp.alerts.alerts --loop     # sleep-until-next-hour loop
"""
from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

from ..backtest.signals import SignalParams, find_signals

PARAMS_FILE = Path(__file__).resolve().parents[1] / "params_validated.json"
SYMBOLS = ["ETH/USDT", "BTC/USDT", "SOL/USDT"]
LOOKBACK_1H, LOOKBACK_4H = 600, 400


def fetch_recent(symbol: str, timeframe: str, limit: int) -> pd.DataFrame:
    import ccxt

    ex = ccxt.binance({"enableRateLimit": True, "timeout": 20000})
    rows = ex.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(rows, columns=["ts", "open", "high", "low", "close", "volume"])
    df.index = pd.to_datetime(df["ts"], unit="ms", utc=True)
    df = df[["open", "high", "low", "close", "volume"]].astype(float)
    # drop the still-forming candle: keep only candles whose close is in the past
    step = pd.Timedelta(timeframe)
    now = pd.Timestamp.now(tz="UTC")
    return df[df.index + step <= now]


def telegram_send(text: str) -> None:
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    r = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={"chat_id": chat_id, "text": text, "parse_mode": "Markdown"},
        timeout=30,
    )
    r.raise_for_status()


def check_once(cfg: dict) -> list[str]:
    sent = []
    params = SignalParams(**cfg["signal_params"])
    for symbol in SYMBOLS:
        df1h = fetch_recent(symbol, "1h", LOOKBACK_1H)
        df4h = fetch_recent(symbol, "4h", LOOKBACK_4H)
        sigs = find_signals(df1h, df4h, params)
        if sigs.empty:
            continue
        last = sigs.iloc[-1]
        if last["time"] != df1h.index[-1]:
            continue  # setup is stale, already confirmed on an earlier candle
        side = "LONG" if last["side"] == 1 else "SHORT"
        entry = last["entry"]
        exit_cfg = cfg["exit"]
        if exit_cfg["kind"] == "fixed":
            tp = entry * (1 + last["side"] * exit_cfg["tp"])
            sl = entry * (1 - last["side"] * exit_cfg["sl"])
        else:
            tp = entry + last["side"] * exit_cfg["tp"] * last["atr"]
            sl = entry - last["side"] * exit_cfg["sl"] * last["atr"]
        liq30 = entry * (1 - last["side"] * 0.9 / 30)
        liq50 = entry * (1 - last["side"] * 0.9 / 50)
        msg = (
            f"*{side} setup — {symbol}* (1H close {last['time']:%Y-%m-%d %H:%M} UTC)\n"
            f"entry zone: `{entry:.4g}`\n"
            f"SL: `{sl:.4g}`  TP: `{tp:.4g}`\n"
            f"liq @30x: `{liq30:.4g}` ({abs(liq30/entry-1):.2%} away)\n"
            f"liq @50x: `{liq50:.4g}` ({abs(liq50/entry-1):.2%} away)\n"
            f"divergence low {last['pivot_price']:.4g} @ {last['pivot_time']:%m-%d %H:%M}, "
            f"RSI {last['rsi_p1']:.1f}→{last['rsi_p2']:.1f}, S/R: {last['sr_ok']}"
        )
        telegram_send(msg)
        sent.append(f"{symbol} {side}")
    return sent


def main() -> int:
    if not PARAMS_FILE.exists():
        print(
            f"{PARAMS_FILE} not found — run and validate the backtest first. "
            "Refusing to alert on unvalidated parameters."
        )
        return 1
    cfg = json.loads(PARAMS_FILE.read_text())
    loop = "--loop" in sys.argv
    while True:
        try:
            sent = check_once(cfg)
            stamp = datetime.now(timezone.utc).strftime("%H:%M")
            print(f"[{stamp}] checked {len(SYMBOLS)} symbols, alerts: {sent or 'none'}")
        except Exception as exc:
            print(f"check failed: {type(exc).__name__}: {exc}")
        if not loop:
            return 0
        now = time.time()
        time.sleep(3600 - now % 3600 + 30)  # 30s after the hourly close


if __name__ == "__main__":
    sys.exit(main())
