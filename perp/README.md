# perp — Perp Strategy Backtest & Alert System

Self-contained subproject (isolated from the GOLDSTEIN gold platform — it
shares nothing with `src/goldstein/`). Validates, or falsifies, a
discretionary RSI-divergence + Bollinger + S/R-confluence strategy on
ETH/BTC/SOL perps at 10-100x leverage, with path-dependent liquidation
simulated candle by candle.

**Status: signal definition awaiting approval — see `SIGNAL_SPEC.md`.
The full backtest is not run until the spec is approved.**

## Layout

```
perp/
  SIGNAL_SPEC.md      the mechanical signal definition (approve this first)
  data/
    fetch.py          ccxt → binance.vision → cache ladder; parquet cache
    cache/            committed OHLCV cache (1H + 4H, 2020+)
  backtest/
    indicators.py     RSI, Bollinger, ATR, fractal pivots (all causal)
    signals.py        the signal — single source of truth, also used by alerts
    engine.py         candle-by-candle sim: liquidation, fees, borrow, slippage
    metrics.py        win/liq rates, expectancy, PF, equity curves, risk of ruin
    run.py            IS grid search (pre-2025) + frozen-params OOS report
  alerts/
    alerts.py         hourly Telegram alerts (Phase 2; needs validated params)
  reports/            backtest output (markdown + json)
```

## How to run

```bash
pip install -r perp/requirements.txt

# 1. data (needs real network — in agent sandboxes use the perp-fetch
#    GitHub Actions workflow, which commits the cache to the branch)
python -m perp.data.fetch

# 2. backtest (only after SIGNAL_SPEC.md is approved)
python -m perp.backtest.run          # writes perp/reports/backtest_*.md/.json

# 3. alerts (only after backtest results are validated and
#    perp/params_validated.json is written)
export TELEGRAM_BOT_TOKEN=... TELEGRAM_CHAT_ID=...
python -m perp.alerts.alerts         # single shot, cron-friendly
python -m perp.alerts.alerts --loop  # hourly loop
```

## Simulation assumptions

- Liquidation approx `entry × (1 ∓ 0.9/L)`; any candle low/high touching it
  before TP/SL ⇒ trade LIQUIDATED, −100% of margin.
- Costs: taker 0.06% per side, borrow 0.005%/h (parameterized), stop fills
  with 0.1% adverse slippage. Conservative same-candle ordering:
  liquidation → stop → target.
- Methodology: parameters tuned only on pre-2025 data; 2025+ reported
  separately; S/R filter reported ON and OFF; still-open trades counted
  separately. Risk of ruin = bootstrap P(equity ≤ 10% of start in 50 trades).

This is research tooling, not financial advice, and it places no orders.
