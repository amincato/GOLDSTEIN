# Mechanical signal specification (v2 — strong divergence + strength entry)

Status: **v2**, per user refinement after the v1 results:
1. the RSI divergence must be **at least `rsi_min_delta` = 10 points** wide
   between the two lows/highs, not merely higher/lower;
2. entry is **not** the divergence candle itself: watch the next
   `confirm_window` = 3 candles and enter on the first one showing strength
   — a short-bodied candle with a big rejection spike, or a momentum candle.
   A candle CLOSING beyond the divergence extreme kills the setup.

v1 (`entry_mode="close"`, immediate) and v0 (`entry_mode="pivot"`, 3h lag)
are kept as sensitivity variants. Every rule below is point-in-time: it
uses only candles that have already CLOSED at evaluation time. No
repainting.

Timeframes: signal on 1H candles; S/R levels on 4H candles. All times UTC,
candle timestamps are OPEN times; a candle is "closed" at open_time + 1h
(or + 4h).

## Parameters (defaults; N, X, K, TP/SL are optimized in-sample only)

| name | default | meaning |
|---|---|---|
| `rsi_period` | 14 | RSI on 1H closes (Wilder smoothing) |
| `pivot_k_1h` | 3 | fractal width defining a "low"/"high" on 1H |
| `div_lookback` (N) | 30 | max 1H candles between the two divergence lows |
| `bb_period`, `bb_std` | 20, 2.0 | Bollinger on 1H closes |
| `sr_pivot_k` (K) | 5 | fractal width for 4H S/R pivots |
| `sr_tolerance` (X) | 0.5% | max distance of the low from an S/R level |
| `require_sr` | true | confluence filter (reported with AND without) |
| `atr_period` | 14 | ATR on 1H (Wilder) for the ATR exit variant |
| `rsi_min_delta` | 10 | min RSI points between the two divergence lows |
| `confirm_window` | 3 | candles after the low scanned for a strength entry |
| `body_max_atr` | 0.5 | "short candle": body ≤ this × ATR |
| `wick_body_ratio` | 1.5 | "big spike": rejection wick ≥ this × body |
| `wick_min_atr` | 0.3 | ...and ≥ this × ATR (doji guard) |

## Definitions

**Pivot low (fractal), width k** — candle `i` is a pivot low iff
`low[i] < min(low[i-k .. i-1])` and `low[i] <= min(low[i+1 .. i+k])`
(strict vs the left side, ties allowed on the right so the FIRST candle of a
double-bottom is the pivot). A pivot at `i` is only KNOWN once candle `i+k`
has closed — its **confirmation candle** is `i+k`. Pivot high is the mirror.

**S/R level (4H)** — the price of any 4H pivot low or pivot high with
`sr_pivot_k` candles on each side. A level exists (is usable) only from the
close of its own 4H confirmation candle onward. Both highs and lows count as
levels for both directions (support can act as resistance and vice versa).

## LONG setup (pseudocode, entry_mode="strength" — the v2 default)

```
at the close of each 1H candle t:                      # evaluation clock
  # candle t is the candidate second low (p2) of the divergence.
  # p1 candidates: fractal pivot lows already CONFIRMED (p1 + k <= t),
  # entirely in the past — no repaint anywhere.
  for each confirmed pivot low p1 with (t - p1) <= N, most recent first:
      # 1. STRONG bullish RSI divergence at the divergence candle
      price_LL  = low[t] < low[p1]
      rsi_HL    = RSI[t] >= RSI[p1] + 10          # rsi_min_delta points
      # 2. Bollinger condition at the divergence candle
      bb_ok     = low[t] <= lower_BB(20,2)[t]
      # 3. S/R confluence (4H), only levels already confirmed before
      #    the close of candle t
      sr_ok     = exists level L with |low[t]/L - 1| <= X
      if price_LL and rsi_HL and bb_ok and (sr_ok or not require_sr):
          # 4. strength confirmation: scan candles w = t+1 .. t+3
          for w in the confirmation window:
              if close[w] < low[t]: ABORT          # closed below the low
              body  = |close[w] - open[w]|
              spike = min(open[w], close[w]) - low[w]      # lower wick
              hammer   = body <= 0.5*ATR14[w]              # short candle
                         and spike >= 1.5*body             # big spike
                         and spike >= 0.3*ATR14[w]
                         and close[w] >= (high[w]+low[w])/2 # strong close
              momentum = close[w] > open[w] and close[w] > high[w-1]
              if hammer or momentum:
                  SIGNAL LONG at the close of candle w
                  entry = close[w];  atr = ATR14[w]
                  stop-loss / take-profit per exit variant (below)
                  mark p1 used     # one signal per p1; a NEW confirmed
                  break            # pivot low re-arms the divergence
```

`entry_mode="close"` (v1): enter at the divergence candle's own close, no
strength confirmation. `entry_mode="pivot"` (v0): the second low must itself
be a confirmed fractal pivot; entry lags the low by `pivot_k_1h` candles.
Both kept as comparison rows in the report.

SHORT is the exact mirror: pivot highs, price higher high + RSI lower high,
`high[p2] >= upper_BB[p2]`, low is replaced by high in the S/R distance.

Only one open trade per asset: signals that fire while a trade is open are
recorded but not traded (reported as `skipped_overlap`).

## Exit variants (tested, per side)

| variant | TP | SL |
|---|---|---|
| fixed A | +2% price | -1% price |
| fixed B | +3% price | -1.5% price |
| ATR | +2.0 × ATR14[t] | -1.0 × ATR14[t] |

## Trade simulation (candle-by-candle, conservative)

```
liq_long  = entry * (1 - 0.9/L)      liq_short = entry * (1 + 0.9/L)
for each 1H candle after the entry candle:
    charge borrow: borrow_rate_hourly (default 0.005%/h) on notional
    order of checks inside one candle (worst case first):
       1. LIQUIDATION  if low <= liq (long) / high >= liq (short) → -100% margin
       2. STOP-LOSS    fills at stop * (1 -/+ slippage), default 0.1%
       3. TAKE-PROFIT  fills exactly at TP
still open at data end → counted separately, not in win/loss stats
costs: taker 0.06% per side on notional; PnL is % on margin, floored at -100%
```

## Known consequences of these choices

1. **Immediate entry cuts the lag to zero but catches falling knives**: the
   trigger fires while the low is still unconfirmed — if price keeps
   dropping, the SL/liquidation does the filtering. That is exactly what the
   simulation measures; the lagged variant is reported alongside so the
   trade-off is visible in numbers, not opinions.
2. **RSI divergence uses the trigger/pivot candles' RSI**, not the RSI's own
   pivots.
   Comparing price pivots' RSI values is the standard mechanical reading;
   detecting separate pivots on the RSI series is a stricter variant we can
   test later.
3. **The BB condition is checked at the low candle (p2), not at entry**:
   at entry (3 candles later) price is often back inside the bands — that is
   expected and intentional.
4. **`0.9/L` liquidation approximation** ignores maintenance-margin tiers and
   Jupiter's exact formula; at 30-100x the real buffer is, if anything,
   smaller. Results at high leverage are therefore optimistic, not
   pessimistic — a strategy that fails here fails harder live.
