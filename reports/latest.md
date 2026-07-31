# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-07-31T08:23:26+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,120.50** (2026-07-31)
- 1m / 1y return: 0.2% / 25.1%
- Drawdown from high: -22.5%
- Drift estimate (shrunk): 14.5%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 22.3% | 20.7% | 18.8% | **20.6%** |

GARCH persistence 0.977, long-run vol 19.3%.

## Regime
- Statistical (HMM): **normal** (typical duration ~6 days)
- Macro: **hostile** (score -0.38; components: real_yield_trend -0.58, dollar_trend -0.41, risk_aversion -0.15)

## Signal
- Ensemble score: **-0.42** → **SHORT**
- Components: mom_3m -0.83, mom_6m -0.98, mom_12m +0.98, trend_50_200 -1.00, mean_reversion -0.03, macro_regime -0.38, cross_asset -0.59

## Cross-asset picture
- Confirmation score: **-0.59** (components: silver_momentum -1.00, gold_silver_ratio -0.01, miners_leadership -0.56, dollar_headwind -0.79)
- Gold/silver ratio z-score (1y): +0.04 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: -9.6%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.82 | +0.83 | +1.99 |
| GDX | +0.79 | +0.78 | +1.33 |
| DXY | -0.54 | -0.33 | -0.07 |
| SPX | +0.52 | +0.27 | +0.12 |
| WTI | -0.32 | -0.13 | -0.25 |
| BTC | +0.43 | +0.16 | +0.23 |

Gold returns vs lagged real-yield changes: lag 0d: -0.16, lag 1d: +0.04, lag 2d: -0.01, lag 5d: +0.03, lag 10d: -0.04

## Leverage recommendation
### → **0.00x SHORT**
- Full Kelly: 2.56x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 3.7%/yr
- Binding caps: fractional_kelly=1.28, vol_target=0.73, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.00, signal_conviction=0.42

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.01x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.00x
- P(loss) 22.6% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.2%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.6% | 23.6% | 0.0% | 0.0% | -7.5% |
| 1.0x | 10.4% | 25.2% | 0.0% | 0.0% | -14.6% |
| 1.5x | 12.4% | 29.4% | 0.3% | 0.0% | -21.6% |
| 2.0x | 13.8% | 32.4% | 3.1% | 0.0% | -28.2% |
| 2.5x | 14.2% | 34.9% | 11.5% | 0.0% | -34.4% |
| 3.0x | 13.5% | 37.8% | 23.4% | 0.0% | -40.1% |
| 4.0x | 10.5% | 43.6% | 47.1% | 0.0% | -50.3% |
| 5.0x | 4.3% | 47.9% | 69.5% | 0.4% | -59.0% |

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
| cagr | 8.1% | 12.0% |
| ann_vol | 9.5% | 16.6% |
| sharpe | 0.48 | 0.54 |
| sortino | 0.56 | 0.68 |
| max_drawdown | -23.7% | -25.1% |
| calmar | 0.34 | 0.48 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._