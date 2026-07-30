# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-07-30T22:59:05+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,169.20** (2026-07-30)
- 1m / 1y return: 2.5% / 26.5%
- Drawdown from high: -21.6%
- Drift estimate (shrunk): 14.8%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 25.5% | 20.4% | 21.8% | **22.4%** |

GARCH persistence 0.978, long-run vol 19.4%.

## Regime
- Statistical (HMM): **turbulent** (typical duration ~23 days)
- Macro: **hostile** (score -0.40; components: real_yield_trend -0.58, dollar_trend -0.48, risk_aversion -0.15)

## Signal
- Ensemble score: **-0.42** → **SHORT**
- Components: mom_3m -0.80, mom_6m -0.98, mom_12m +0.97, trend_50_200 -1.00, mean_reversion -0.14, macro_regime -0.40, cross_asset -0.58

## Cross-asset picture
- Confirmation score: **-0.58** (components: silver_momentum -1.00, gold_silver_ratio -0.00, miners_leadership -0.56, dollar_headwind -0.77)
- Gold/silver ratio z-score (1y): +0.01 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: -9.4%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.81 | +0.82 | +1.97 |
| GDX | +0.79 | +0.78 | +1.33 |
| DXY | -0.57 | -0.34 | -0.07 |
| SPX | +0.54 | +0.27 | +0.12 |
| WTI | -0.31 | -0.13 | -0.25 |
| BTC | +0.43 | +0.16 | +0.23 |

Gold returns vs lagged real-yield changes: lag 0d: -0.16, lag 1d: +0.04, lag 2d: -0.01, lag 5d: +0.03, lag 10d: -0.04

## Leverage recommendation
### → **0.00x SHORT**
- Full Kelly: 2.22x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 3.7%/yr
- Binding caps: fractional_kelly=1.11, vol_target=0.67, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.00, signal_conviction=0.42

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.01x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.00x
- P(loss) 22.9% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.2%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.4% | 24.7% | 0.0% | 0.0% | -7.6% |
| 1.0x | 10.1% | 26.7% | 0.0% | 0.0% | -14.8% |
| 1.5x | 12.2% | 31.1% | 0.2% | 0.0% | -21.9% |
| 2.0x | 13.5% | 34.4% | 3.8% | 0.0% | -28.6% |
| 2.5x | 14.0% | 37.9% | 12.4% | 0.0% | -34.8% |
| 3.0x | 13.5% | 40.0% | 24.2% | 0.0% | -40.6% |
| 4.0x | 10.3% | 44.2% | 48.9% | 0.0% | -50.8% |
| 5.0x | 3.5% | 48.1% | 70.2% | 0.3% | -59.6% |

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
| cagr | 7.7% | 12.2% |
| ann_vol | 9.5% | 16.7% |
| sharpe | 0.44 | 0.55 |
| sortino | 0.51 | 0.70 |
| max_drawdown | -24.9% | -25.1% |
| calmar | 0.31 | 0.49 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._