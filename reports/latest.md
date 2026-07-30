# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-07-30T22:42:39+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ⚠️ **DEMO DATA** — one or more series are synthetic because no live or cached market data was available. Numbers illustrate the methodology, NOT current market conditions. Run `goldstein fetch` from a network-enabled session to populate the cache.

## Market snapshot
- Last price: **972.10** (2026-07-30)
- 1m / 1y return: -0.4% / -8.2%
- Drawdown from high: -47.6%
- Drift estimate (shrunk): 1.2%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 2.3% | 2.3% | 12.7% | **5.4%** |

GARCH persistence 0.999, long-run vol 39.1%.

## Regime
- Statistical (HMM): **calm** (typical duration ~17 days)
- Macro: **neutral** (score -0.06; components: real_yield_trend -0.08, dollar_trend -0.12, risk_aversion +0.01)

## Signal
- Ensemble score: **+0.19** → **LONG**
- Components: mom_3m +0.08, mom_6m +0.31, mom_12m -0.60, trend_50_200 +1.00, mean_reversion +0.37, macro_regime -0.06, cross_asset +0.33

## Cross-asset picture
- Confirmation score: **+0.33** (components: silver_momentum +0.98, gold_silver_ratio +0.48, miners_leadership -0.06, dollar_headwind -0.09)
- Gold/silver ratio z-score (1y): -1.43 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: -0.9%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.24 | +0.49 | +1.06 |
| GDX | -0.06 | +0.33 | +0.88 |
| DXY | -0.13 | -0.26 | -0.15 |
| SPX | +0.05 | +0.04 | +0.06 |
| WTI | +0.03 | +0.21 | +0.83 |
| BTC | -0.30 | -0.02 | -0.09 |

Gold returns vs lagged real-yield changes: lag 0d: +0.02, lag 1d: +0.02, lag 2d: -0.03, lag 5d: -0.04, lag 10d: +0.04

## Leverage recommendation
### → **0.00x LONG**
- Full Kelly: -6.10x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 3.0%/yr
- Binding caps: fractional_kelly=0.00, vol_target=2.76, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.00, signal_conviction=0.19
- **Estimated edge is non-positive; any long leverage is negative-EV under these estimates**

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.01x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.00x
- P(loss) 44.8% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.2%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 0.7% | 47.1% | 0.0% | 0.0% | -11.2% |
| 1.0x | 0.5% | 48.9% | 1.8% | 0.0% | -21.0% |
| 1.5x | -2.2% | 53.0% | 16.7% | 0.0% | -30.1% |
| 2.0x | -5.8% | 55.9% | 25.9% | 0.1% | -38.1% |
| 2.5x | -10.4% | 58.4% | 35.5% | 0.4% | -45.2% |
| 3.0x | -16.2% | 61.1% | 45.0% | 1.6% | -51.3% |
| 4.0x | -30.7% | 65.1% | 66.0% | 12.7% | -61.4% |
| 5.0x | -48.0% | 68.0% | 79.1% | 16.9% | -70.6% |

## Stress tests (at recommended leverage, min 1x)
- Survives all historical scenarios: **YES** · worst: `overnight_gap_20%` (-20.0% equity)
| Scenario | Asset move | Equity | Margin call |
|---|---|---|---|
| gfc_2008_liquidation | -18.1% | 0.82x | no |
| april_2013_crash | -13.8% | 0.86x | no |
| taper_2013_grind | -18.1% | 0.82x | no |
| covid_2020_margin_cascade | -12.4% | 0.88x | no |
| rate_shock_2022 | -14.7% | 0.85x | no |
| overnight_gap_3% | -3.0% | 0.97x | no |
| overnight_gap_5% | -5.0% | 0.95x | no |
| overnight_gap_8% | -8.0% | 0.92x | no |
| overnight_gap_12% | -12.0% | 0.88x | no |
| overnight_gap_20% | -20.0% | 0.80x | no |

## Daily-reset ETP decay (annualized drag vs static leverage)
| Asset vol | 2x drag | 3x drag |
|---|---|---|
| 10% | 1.0% | 3.0% |
| 15% | 2.2% | 6.8% |
| 20% | 4.0% | 12.0% |
| 25% | 6.2% | 18.8% |
| 30% | 9.0% | 27.0% |
| 40% | 16.0% | 48.0% |

## Strategy backtest (10y: vol-target × signal vs buy & hold)
| Metric | Strategy | Buy & hold |
|---|---|---|
| cagr | 2.5% | -0.9% |
| ann_vol | 8.5% | 25.2% |
| sharpe | -0.02 | -0.03 |
| sortino | -0.02 | -0.03 |
| max_drawdown | -19.0% | -41.4% |
| calmar | 0.13 | -0.02 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._