# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-09-02T09:58:07+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,357.60** (2026-09-02)
- 1m / 1y return: 2.6% / 21.3%
- Drawdown from high: -18.1%
- Drift estimate (shrunk): 15.4%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 23.4% | 22.8% | 22.4% | **22.8%** |

GARCH persistence 0.978, long-run vol 19.4%.

## Regime
- Statistical (HMM): **normal** (typical duration ~5 days)
- Macro: **hostile** (score -0.51; components: real_yield_trend -0.99, dollar_trend -0.13, risk_aversion -0.42)

## Signal
- Ensemble score: **-0.17** → **SHORT**
- Components: mom_3m +0.35, mom_6m -0.77, mom_12m +0.99, trend_50_200 -1.00, mean_reversion +0.07, macro_regime -0.51, cross_asset -0.07

## Cross-asset picture
- Confirmation score: **-0.07** (components: silver_momentum -0.90, gold_silver_ratio +0.01, miners_leadership +0.60, dollar_headwind +0.03)
- Gold/silver ratio z-score (1y): -0.03 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: 10.5%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.87 | +0.83 | +1.96 |
| GDX | +0.83 | +0.79 | +1.39 |
| DXY | -0.51 | -0.35 | -0.06 |
| SPX | +0.40 | +0.27 | +0.12 |
| WTI | -0.17 | -0.13 | -0.25 |
| BTC | +0.51 | +0.19 | +0.27 |

Gold returns vs lagged real-yield changes: lag 0d: -0.16, lag 1d: +0.03, lag 2d: -0.02, lag 5d: +0.04, lag 10d: -0.04

## Leverage recommendation
### → **0.01x SHORT**
- Full Kelly: 2.24x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 3.9%/yr
- Binding caps: fractional_kelly=1.12, vol_target=0.66, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.10, signal_conviction=0.17

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.01x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.00x
- P(loss) 22.9% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.2%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.7% | 24.4% | 0.0% | 0.0% | -7.7% |
| 1.0x | 10.8% | 26.1% | 0.0% | 0.0% | -14.9% |
| 1.5x | 13.0% | 30.3% | 0.4% | 0.0% | -22.1% |
| 2.0x | 14.3% | 33.4% | 4.5% | 0.0% | -28.8% |
| 2.5x | 14.7% | 36.1% | 12.4% | 0.0% | -35.1% |
| 3.0x | 14.7% | 38.2% | 24.6% | 0.0% | -40.9% |
| 4.0x | 11.8% | 42.7% | 48.6% | 0.1% | -51.2% |
| 5.0x | 6.0% | 47.4% | 71.8% | 0.5% | -59.9% |

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
| cagr | 8.4% | 12.5% |
| ann_vol | 9.6% | 16.8% |
| sharpe | 0.49 | 0.56 |
| sortino | 0.57 | 0.71 |
| max_drawdown | -19.7% | -25.1% |
| calmar | 0.42 | 0.50 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._