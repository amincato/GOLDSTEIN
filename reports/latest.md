# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-09-01T10:31:15+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,429.60** (2026-09-01)
- 1m / 1y return: 8.2% / 24.8%
- Drawdown from high: -16.7%
- Drift estimate (shrunk): 15.7%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 22.9% | 22.2% | 21.7% | **22.3%** |

GARCH persistence 0.978, long-run vol 19.4%.

## Regime
- Statistical (HMM): **normal** (typical duration ~6 days)
- Macro: **hostile** (score -0.48; components: real_yield_trend -0.95, dollar_trend -0.07, risk_aversion -0.43)

## Signal
- Ensemble score: **-0.20** → **SHORT**
- Components: mom_3m +0.32, mom_6m -0.73, mom_12m +1.00, trend_50_200 -1.00, mean_reversion -0.10, macro_regime -0.48, cross_asset -0.27

## Cross-asset picture
- Confirmation score: **-0.27** (components: silver_momentum -0.89, gold_silver_ratio +0.02, miners_leadership -0.07, dollar_headwind -0.13)
- Gold/silver ratio z-score (1y): -0.07 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: -1.0%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.86 | +0.83 | +1.97 |
| GDX | +0.83 | +0.79 | +1.38 |
| DXY | -0.51 | -0.35 | -0.06 |
| SPX | +0.38 | +0.26 | +0.12 |
| WTI | -0.17 | -0.13 | -0.24 |
| BTC | +0.52 | +0.19 | +0.27 |

Gold returns vs lagged real-yield changes: lag 0d: -0.16, lag 1d: +0.04, lag 2d: -0.01, lag 5d: +0.04, lag 10d: -0.04

## Leverage recommendation
### → **0.02x SHORT**
- Full Kelly: 2.42x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.0%/yr
- Binding caps: fractional_kelly=1.21, vol_target=0.67, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.16, signal_conviction=0.20

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.02x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.01x
- P(loss) 22.2% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.3%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 6.0% | 23.4% | 0.0% | 0.0% | -7.6% |
| 1.0x | 11.2% | 24.8% | 0.0% | 0.0% | -14.7% |
| 1.5x | 13.5% | 28.8% | 0.5% | 0.0% | -21.8% |
| 2.0x | 15.1% | 31.4% | 3.9% | 0.0% | -28.5% |
| 2.5x | 15.9% | 34.7% | 11.5% | 0.0% | -34.6% |
| 3.0x | 15.8% | 37.5% | 24.0% | 0.0% | -40.4% |
| 4.0x | 13.9% | 41.3% | 48.5% | 0.1% | -50.6% |
| 5.0x | 8.3% | 45.4% | 69.5% | 0.4% | -59.4% |

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
| cagr | 8.1% | 12.7% |
| ann_vol | 9.6% | 16.8% |
| sharpe | 0.47 | 0.58 |
| sortino | 0.55 | 0.73 |
| max_drawdown | -21.1% | -25.1% |
| calmar | 0.38 | 0.51 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._