# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-08-13T07:05:19+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,435.70** (2026-08-13)
- 1m / 1y return: 11.3% / 32.1%
- Drawdown from high: -16.6%
- Drift estimate (shrunk): 15.9%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 23.2% | 22.0% | 20.1% | **21.8%** |

GARCH persistence 0.987, long-run vol 18.0%.

## Regime
- Statistical (HMM): **calm** (typical duration ~3 days)
- Macro: **hostile** (score -0.42; components: real_yield_trend -0.68, dollar_trend -0.40, risk_aversion -0.19)

## Signal
- Ensemble score: **-0.41** → **SHORT**
- Components: mom_3m -0.75, mom_6m -0.93, mom_12m +0.99, trend_50_200 -1.00, mean_reversion -0.65, macro_regime -0.42, cross_asset -0.42

## Cross-asset picture
- Confirmation score: **-0.42** (components: silver_momentum -0.98, gold_silver_ratio +0.03, miners_leadership -0.16, dollar_headwind -0.57)
- Gold/silver ratio z-score (1y): -0.09 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: -2.4%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.84 | +0.83 | +1.98 |
| GDX | +0.81 | +0.78 | +1.36 |
| DXY | -0.49 | -0.33 | -0.06 |
| SPX | +0.43 | +0.27 | +0.12 |
| WTI | -0.21 | -0.13 | -0.25 |
| BTC | +0.48 | +0.17 | +0.24 |

Gold returns vs lagged real-yield changes: lag 0d: -0.16, lag 1d: +0.03, lag 2d: -0.01, lag 5d: +0.03, lag 10d: -0.04

## Leverage recommendation
### → **0.05x SHORT**
- Full Kelly: 2.57x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.3%/yr
- Binding caps: fractional_kelly=1.29, vol_target=0.69, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.17, signal_conviction=0.41

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.05x)
- Terminal wealth p5/p50/p95: 0.99x / 1.01x / 1.02x
- P(loss) 22.7% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.8%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.6% | 23.9% | 0.0% | 0.0% | -7.6% |
| 1.0x | 10.5% | 25.4% | 0.0% | 0.0% | -14.7% |
| 1.5x | 12.6% | 30.2% | 0.6% | 0.0% | -21.8% |
| 2.0x | 14.0% | 33.2% | 3.9% | 0.0% | -28.4% |
| 2.5x | 14.5% | 35.6% | 11.4% | 0.0% | -34.6% |
| 3.0x | 14.3% | 38.5% | 23.9% | 0.0% | -40.3% |
| 4.0x | 11.7% | 42.8% | 48.0% | 0.0% | -50.6% |
| 5.0x | 6.4% | 47.2% | 69.8% | 0.4% | -59.3% |

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
| cagr | 7.5% | 12.6% |
| ann_vol | 9.5% | 16.7% |
| sharpe | 0.42 | 0.57 |
| sortino | 0.49 | 0.72 |
| max_drawdown | -24.9% | -25.1% |
| calmar | 0.30 | 0.50 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._