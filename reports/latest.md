# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-08-19T06:06:46+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,390.10** (2026-08-19)
- 1m / 1y return: 5.9% / 32.5%
- Drawdown from high: -17.5%
- Drift estimate (shrunk): 15.9%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 21.5% | 20.0% | 19.3% | **20.3%** |

GARCH persistence 0.978, long-run vol 19.3%.

## Regime
- Statistical (HMM): **normal** (typical duration ~5 days)
- Macro: **hostile** (score -0.47; components: real_yield_trend -0.85, dollar_trend -0.34, risk_aversion -0.22)

## Signal
- Ensemble score: **-0.31** → **SHORT**
- Components: mom_3m -0.21, mom_6m -0.82, mom_12m +1.00, trend_50_200 -1.00, mean_reversion -0.43, macro_regime -0.47, cross_asset -0.38

## Cross-asset picture
- Confirmation score: **-0.38** (components: silver_momentum -0.86, gold_silver_ratio -0.03, miners_leadership -0.09, dollar_headwind -0.55)
- Gold/silver ratio z-score (1y): +0.09 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: -1.4%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.84 | +0.83 | +1.99 |
| GDX | +0.81 | +0.78 | +1.35 |
| DXY | -0.53 | -0.34 | -0.06 |
| SPX | +0.40 | +0.26 | +0.12 |
| WTI | -0.22 | -0.13 | -0.25 |
| BTC | +0.47 | +0.17 | +0.24 |

Gold returns vs lagged real-yield changes: lag 0d: -0.16, lag 1d: +0.03, lag 2d: -0.01, lag 5d: +0.03, lag 10d: -0.05

## Leverage recommendation
### → **0.03x SHORT**
- Full Kelly: 2.97x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.1%/yr
- Binding caps: fractional_kelly=1.48, vol_target=0.74, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.13, signal_conviction=0.31

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.03x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.01x
- P(loss) 24.1% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.5%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.5% | 25.7% | 0.0% | 0.0% | -7.6% |
| 1.0x | 10.4% | 26.9% | 0.0% | 0.0% | -14.7% |
| 1.5x | 12.4% | 30.6% | 0.5% | 0.0% | -21.9% |
| 2.0x | 13.6% | 33.0% | 4.3% | 0.0% | -28.5% |
| 2.5x | 14.0% | 35.6% | 12.1% | 0.0% | -34.7% |
| 3.0x | 13.5% | 38.2% | 24.1% | 0.0% | -40.5% |
| 4.0x | 10.0% | 42.4% | 47.6% | 0.0% | -50.7% |
| 5.0x | 3.5% | 48.1% | 69.9% | 0.4% | -59.5% |

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
| cagr | 8.5% | 12.6% |
| ann_vol | 9.6% | 16.7% |
| sharpe | 0.51 | 0.57 |
| sortino | 0.59 | 0.73 |
| max_drawdown | -19.9% | -25.1% |
| calmar | 0.43 | 0.50 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._