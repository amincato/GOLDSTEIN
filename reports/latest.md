# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-08-09T18:24:21+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,399.70** (2026-08-07)
- 1m / 1y return: 7.2% / 29.4%
- Drawdown from high: -17.3%
- Drift estimate (shrunk): 15.6%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 28.1% | 23.2% | 26.0% | **25.5%** |

GARCH persistence 0.978, long-run vol 19.4%.

## Regime
- Statistical (HMM): **turbulent** (typical duration ~23 days)
- Macro: **hostile** (score -0.34; components: real_yield_trend -0.61, dollar_trend -0.25, risk_aversion -0.16)

## Signal
- Ensemble score: **-0.41** → **SHORT**
- Components: mom_3m -0.88, mom_6m -0.93, mom_12m +0.96, trend_50_200 -1.00, mean_reversion -0.58, macro_regime -0.34, cross_asset -0.39

## Cross-asset picture
- Confirmation score: **-0.39** (components: silver_momentum -0.97, gold_silver_ratio +0.01, miners_leadership -0.21, dollar_headwind -0.38)
- Gold/silver ratio z-score (1y): -0.03 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: -3.1%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.81 | +0.83 | +1.96 |
| GDX | +0.81 | +0.78 | +1.35 |
| DXY | -0.51 | -0.34 | -0.06 |
| SPX | +0.44 | +0.27 | +0.12 |
| WTI | -0.22 | -0.13 | -0.24 |
| BTC | +0.48 | +0.17 | +0.24 |

Gold returns vs lagged real-yield changes: lag 0d: -0.16, lag 1d: +0.04, lag 2d: -0.01, lag 5d: +0.04, lag 10d: -0.04

## Leverage recommendation
### → **0.03x SHORT**
- Full Kelly: 1.83x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.1%/yr
- Binding caps: fractional_kelly=0.91, vol_target=0.59, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.14, signal_conviction=0.41

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.03x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.01x
- P(loss) 22.2% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.5%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.8% | 23.7% | 0.0% | 0.0% | -7.5% |
| 1.0x | 10.8% | 25.6% | 0.0% | 0.0% | -14.6% |
| 1.5x | 13.1% | 29.6% | 0.4% | 0.0% | -21.7% |
| 2.0x | 14.5% | 33.0% | 3.6% | 0.0% | -28.3% |
| 2.5x | 15.0% | 35.2% | 11.6% | 0.0% | -34.4% |
| 3.0x | 14.8% | 37.8% | 23.4% | 0.0% | -40.1% |
| 4.0x | 12.3% | 41.8% | 47.0% | 0.0% | -50.3% |
| 5.0x | 5.5% | 46.7% | 68.8% | 0.4% | -59.1% |

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
| cagr | 7.9% | 12.7% |
| ann_vol | 9.6% | 16.7% |
| sharpe | 0.46 | 0.58 |
| sortino | 0.53 | 0.73 |
| max_drawdown | -23.6% | -25.1% |
| calmar | 0.34 | 0.51 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._