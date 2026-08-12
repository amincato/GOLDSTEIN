"""OHLCV download + parquet cache.

Ladder: ccxt (Binance spot REST) → data.binance.vision monthly/daily zips →
whatever is already in perp/data/cache/. Agent sandboxes usually block both
network paths; the perp-fetch GitHub Actions workflow runs this on a real
runner and commits the cache, exactly like GOLDSTEIN's daily update.

Run:  python -m perp.data.fetch
"""
from __future__ import annotations

import io
import sys
import time
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

CACHE_DIR = Path(__file__).resolve().parent / "cache"
SYMBOLS = ["ETH/USDT", "BTC/USDT", "SOL/USDT"]
TIMEFRAMES = ["1h", "4h"]
SINCE = datetime(2020, 1, 1, tzinfo=timezone.utc)
VISION = "https://data.binance.vision/data/spot"


def cache_path(symbol: str, timeframe: str) -> Path:
    return CACHE_DIR / f"{symbol.replace('/', '')}_{timeframe}.parquet"


def load_ohlcv(symbol: str, timeframe: str) -> pd.DataFrame:
    """Load cached candles (UTC open-time index, ohlcv columns)."""
    path = cache_path(symbol, timeframe)
    if not path.exists():
        raise FileNotFoundError(
            f"No cache for {symbol} {timeframe}. Run the perp-fetch workflow "
            "or `python -m perp.data.fetch` on a machine with network access."
        )
    df = pd.read_parquet(path)
    df.index = pd.to_datetime(df.index, utc=True).as_unit("ns")
    return df.sort_index()


def _normalize(rows: list[list]) -> pd.DataFrame:
    df = pd.DataFrame(rows, columns=["ts", "open", "high", "low", "close", "volume"])
    ts = df["ts"].astype("int64")
    ts = ts.where(ts < 10**14, ts // 1000)  # 2025+ vision files use microseconds
    df.index = pd.to_datetime(ts, unit="ms", utc=True)
    df = df[["open", "high", "low", "close", "volume"]].astype(float)
    return df[~df.index.duplicated(keep="last")].sort_index()


def _fetch_ccxt(symbol: str, timeframe: str, since: datetime) -> pd.DataFrame:
    import ccxt

    ex = ccxt.binance({"enableRateLimit": True, "timeout": 20000})
    since_ms = int(since.timestamp() * 1000)
    rows: list[list] = []
    while True:
        batch = ex.fetch_ohlcv(symbol, timeframe, since=since_ms, limit=1000)
        if not batch:
            break
        rows.extend(r[:6] for r in batch)
        if len(batch) < 1000:
            break
        since_ms = batch[-1][0] + 1
        time.sleep(ex.rateLimit / 1000)
    return _normalize(rows)


def _fetch_vision(symbol: str, timeframe: str, since: datetime) -> pd.DataFrame:
    sym = symbol.replace("/", "")
    frames = []
    month = pd.Timestamp(since).to_period("M")
    last_full = (pd.Timestamp.now(tz=None).to_period("M")) - 1
    while month <= last_full:
        url = f"{VISION}/monthly/klines/{sym}/{timeframe}/{sym}-{timeframe}-{month}.zip"
        r = requests.get(url, timeout=60)
        if r.status_code == 200:
            with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                raw = pd.read_csv(z.open(z.namelist()[0]), header=None)
            if str(raw.iloc[0, 0]).startswith("open_time"):
                raw = raw.iloc[1:]
            frames.append(_normalize(raw.iloc[:, :6].values.tolist()))
        month += 1
    # current month: daily files
    day = pd.Timestamp(str(last_full + 1) + "-01")
    today = pd.Timestamp.utcnow().tz_localize(None).normalize()
    while day < today:
        url = (
            f"{VISION}/daily/klines/{sym}/{timeframe}/"
            f"{sym}-{timeframe}-{day.date()}.zip"
        )
        r = requests.get(url, timeout=60)
        if r.status_code == 200:
            with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                raw = pd.read_csv(z.open(z.namelist()[0]), header=None)
            frames.append(_normalize(raw.iloc[:, :6].values.tolist()))
        day += pd.Timedelta(days=1)
    if not frames:
        return pd.DataFrame()
    df = pd.concat(frames)
    return df[~df.index.duplicated(keep="last")].sort_index()


def fetch_symbol(symbol: str, timeframe: str) -> tuple[pd.DataFrame, str]:
    path = cache_path(symbol, timeframe)
    existing = None
    since = SINCE
    if path.exists():
        existing = load_ohlcv(symbol, timeframe)
        if len(existing):
            since = existing.index[-1].to_pydatetime()
    for name, fn in (("ccxt", _fetch_ccxt), ("binance.vision", _fetch_vision)):
        try:
            fresh = fn(symbol, timeframe, since)
        except Exception as exc:  # network blocked, provider down, ...
            print(f"  {name} failed: {type(exc).__name__}: {str(exc)[:100]}")
            continue
        if fresh is None or fresh.empty:
            continue
        df = fresh if existing is None else pd.concat([existing, fresh])
        df = df[~df.index.duplicated(keep="last")].sort_index()
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path)
        return df, name
    if existing is not None:
        return existing, "cache"
    return pd.DataFrame(), "none"


def main() -> int:
    ok = True
    for symbol in SYMBOLS:
        for timeframe in TIMEFRAMES:
            df, source = fetch_symbol(symbol, timeframe)
            if df.empty:
                print(f"{symbol} {timeframe}: NO DATA (all sources blocked)")
                ok = False
            else:
                print(
                    f"{symbol} {timeframe}: {len(df)} candles "
                    f"[{df.index[0]} → {df.index[-1]}] via {source}"
                )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
