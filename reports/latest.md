# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-07-30T22:49:07+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ⚠️ **DEMO DATA** — one or more series are synthetic because no live or cached market data was available. Numbers illustrate the methodology, NOT current market conditions. Run `goldstein fetch` from a network-enabled session to populate the cache.

## Market snapshot
- Last price: **4,167.30** (2026-07-30)
- 1m / 1y return: 71.7% / 1304.5%
- Drawdown from high: -11.6%
- Drift estimate (shrunk): 207.6%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 86.5% | 80.8% | 82.4% | **83.0%** |

GARCH persistence 0.773, long-run vol 78.9%.

## Regime
- Statistical (HMM): **normal** (typical duration ~34 days)
- Macro: **hostile** (score -0.36; components: real_yield_trend -0.08, dollar_trend -1.00, risk_aversion +0.01)

## Signal
- Ensemble score: **+0.57** → **LONG**
- Components: mom_3m +1.00, mom_6m +1.00, mom_12m +1.00, trend_50_200 +1.00, mean_reversion -0.62, macro_regime -0.36, cross_asset +0.00

## Cross-asset picture
- Confirmation score: **+0.00**

Gold returns vs lagged real-yield changes: lag 0d: +0.02, lag 1d: +0.10, lag 2d: +0.02, lag 5d: +0.03, lag 10d: -0.02

## Leverage recommendation
### → **0.04x LONG**
- Full Kelly: 2.97x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 11.7%/yr
- Binding caps: fractional_kelly=1.48, vol_target=0.18, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.42, signal_conviction=0.57

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.04x)
- Terminal wealth p5/p50/p95: 1.06x / 1.13x / 1.18x
- P(loss) 0.0% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -1.5%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 140.0% | 0.0% | 0.0% | 0.0% | -18.2% |
| 1.0x | 264.5% | 0.1% | 4.8% | 0.0% | -34.1% |
| 1.5x | 370.5% | 0.3% | 42.9% | 0.0% | -47.9% |
| 2.0x | 460.4% | 0.7% | 69.2% | 0.0% | -59.6% |
| 2.5x | 534.4% | 0.9% | 92.8% | 0.0% | -69.2% |
| 3.0x | 592.8% | 1.3% | 96.8% | 0.1% | -77.1% |
| 4.0x | 650.6% | 3.7% | 100.0% | 0.9% | -88.5% |
| 5.0x | -299.6% | 67.6% | 100.0% | 66.1% | -95.4% |

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
| cagr | 0.8% | 1232.7% |
| ann_vol | 2.2% | 78.9% |
| sharpe | -0.97 | 3.65 |
| sortino | -0.13 | 6.02 |
| max_drawdown | -2.8% | -42.0% |
| calmar | 0.28 | 29.34 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._