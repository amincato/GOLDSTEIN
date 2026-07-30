"""Dukascopy historical tick backfill — deep intraday history, free.

Dukascopy publishes anonymous, unauthenticated tick archives:
  https://datafeed.dukascopy.com/datafeed/XAUUSD/{YYYY}/{MM-1:02d}/{DD:02d}/{HH:02d}h_ticks.bi5
Each file is LZMA-compressed records of 20 bytes:
  >IIIff : ms-offset-in-hour, ask*scale, bid*scale, askVol, bidVol
For XAUUSD the price scale is 1000 (auto-verified against a plausible gold
price range at decode time).

`backfill()` walks a date range hour by hour, aggregates mid-price ticks to
5m OHLC bars (volume = tick count) and merges them into the standard
intraday cache, extending history far beyond Yahoo's 60-day window.
"""

from __future__ import annotations

import logging
import lzma
import struct
from datetime import date, timedelta

import numpy as np
import pandas as pd
import requests

from ..config import CACHE_DIR

log = logging.getLogger("goldstein.intraday")

_URL = ("https://datafeed.dukascopy.com/datafeed/{sym}/{y}/{m:02d}/{d:02d}/"
        "{h:02d}h_ticks.bi5")
_HEADERS = {"User-Agent": "Mozilla/5.0 (goldstein-quant)"}
_RECORD = struct.Struct(">IIIff")
_SCALES = (1000.0, 100000.0, 100.0)
_PLAUSIBLE = (100.0, 100_000.0)


def decode_bi5(blob: bytes, hour_start: pd.Timestamp) -> pd.DataFrame | None:
    """Decode one .bi5 file to a tick DataFrame (UTC index, mid price)."""
    if not blob:
        return None
    try:
        raw = lzma.decompress(blob)
    except lzma.LZMAError:
        return None
    if len(raw) < _RECORD.size:
        return None
    n = len(raw) // _RECORD.size
    ms = np.empty(n, dtype=np.int64)
    ask = np.empty(n)
    bid = np.empty(n)
    for i, rec in enumerate(_RECORD.iter_unpack(raw[: n * _RECORD.size])):
        ms[i], ask[i], bid[i] = rec[0], rec[1], rec[2]
    mid_raw = (ask + bid) / 2.0
    for scale in _SCALES:                     # auto-detect the price scale
        mid = mid_raw / scale
        if _PLAUSIBLE[0] < np.median(mid) < _PLAUSIBLE[1]:
            idx = hour_start + pd.to_timedelta(ms, unit="ms")
            return pd.DataFrame({"mid": mid}, index=idx)
    return None


def fetch_hour(symbol: str, ts: pd.Timestamp,
               session: requests.Session | None = None) -> pd.DataFrame | None:
    """Fetch+decode one hour of ticks. Dukascopy months are 0-based."""
    url = _URL.format(sym=symbol, y=ts.year, m=ts.month - 1, d=ts.day, h=ts.hour)
    sess = session or requests
    r = sess.get(url, timeout=20, headers=_HEADERS)
    if r.status_code != 200 or not r.content:
        return None
    return decode_bi5(r.content, ts)


def ticks_to_bars(ticks: pd.DataFrame, interval: str = "5min") -> pd.DataFrame:
    bars = ticks["mid"].resample(interval).agg(["first", "max", "min", "last"])
    bars.columns = ["open", "high", "low", "close"]
    bars["volume"] = ticks["mid"].resample(interval).count().astype(float)
    bars = bars.dropna(subset=["close"])
    bars.index.name = "datetime"
    return bars


def backfill(start: date, end: date, symbol: str = "XAUUSD",
             symbol_key: str = "XAUUSD", interval: str = "5m",
             max_failures: int = 200) -> dict:
    """Download [start, end) tick hours, build 5m bars, merge into the cache.

    Weekend hours and holidays 404 and are skipped; persistent network
    failure aborts (max_failures guard) rather than looping forever.
    """
    path = CACHE_DIR / "intraday" / f"{symbol_key}_{interval}.csv"
    cached = None
    if path.exists():
        cached = pd.read_csv(path, parse_dates=["datetime"], index_col="datetime")
        cached.index = pd.DatetimeIndex(cached.index, tz="UTC")

    freq = {"5m": "5min", "15m": "15min", "60m": "60min"}[interval]
    sess = requests.Session()
    all_bars, hours_ok, hours_missing, failures = [], 0, 0, 0
    day = start
    while day < end:
        if day.weekday() < 6:                 # Dukascopy has Sun 22:00 open; keep Mon-Sat
            for h in range(24):
                ts = pd.Timestamp(day.year, day.month, day.day, h, tz="UTC")
                try:
                    ticks = fetch_hour(symbol, ts, sess)
                except Exception as exc:
                    failures += 1
                    log.info("dukascopy failed %s: %s", ts, exc)
                    if failures >= max_failures:
                        log.warning("aborting backfill after %d failures", failures)
                        day = end
                        break
                    continue
                if ticks is None or ticks.empty:
                    hours_missing += 1
                    continue
                all_bars.append(ticks_to_bars(ticks, freq))
                hours_ok += 1
        day = day + timedelta(days=1)

    if all_bars:
        new = pd.concat(all_bars).sort_index()
        merged = pd.concat([cached, new]) if cached is not None else new
        merged = merged[~merged.index.duplicated(keep="last")].sort_index()
        path.parent.mkdir(parents=True, exist_ok=True)
        merged.to_csv(path)
        total = len(merged)
    else:
        total = 0 if cached is None else len(cached)

    return {
        "hours_fetched": hours_ok,
        "hours_missing": hours_missing,
        "failures": failures,
        "bars_added": sum(len(b) for b in all_bars),
        "cache_total_bars": total,
        "cache_path": str(path),
    }
