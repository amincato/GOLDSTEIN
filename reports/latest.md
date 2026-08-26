# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-08-26T06:20:45+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,695.10** (2026-08-26)
- 1m / 1y return: 16.4% / 38.6%
- Drawdown from high: -11.7%
- Drift estimate (shrunk): 16.7%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 22.8% | 21.1% | 20.7% | **21.5%** |

GARCH persistence 0.978, long-run vol 19.4%.

## Regime
- Statistical (HMM): **normal** (typical duration ~5 days)
- Macro: **hostile** (score -0.43; components: real_yield_trend -0.79, dollar_trend -0.15, risk_aversion -0.35)

## Signal
- Ensemble score: **-0.30** → **SHORT**
- Components: mom_3m +0.09, mom_6m -0.88, mom_12m +1.00, trend_50_200 -1.00, mean_reversion -0.87, macro_regime -0.43, cross_asset -0.39

## Cross-asset picture
- Confirmation score: **-0.39** (components: silver_momentum -0.98, gold_silver_ratio +0.02, miners_leadership -0.37, dollar_headwind -0.23)
- Gold/silver ratio z-score (1y): -0.05 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: -5.9%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.86 | +0.83 | +1.97 |
| GDX | +0.82 | +0.79 | +1.38 |
| DXY | -0.50 | -0.34 | -0.06 |
| SPX | +0.38 | +0.27 | +0.12 |
| WTI | -0.14 | -0.13 | -0.24 |
| BTC | +0.53 | +0.19 | +0.27 |

Gold returns vs lagged real-yield changes: lag 0d: -0.16, lag 1d: +0.04, lag 2d: -0.01, lag 5d: +0.04, lag 10d: -0.04

## Leverage recommendation
### → **0.09x SHORT**
- Full Kelly: 2.82x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.8%/yr
- Binding caps: fractional_kelly=1.41, vol_target=0.70, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.41, signal_conviction=0.30

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.09x)
- Terminal wealth p5/p50/p95: 0.99x / 1.01x / 1.04x
- P(loss) 22.4% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -1.4%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.8% | 23.6% | 0.0% | 0.0% | -7.6% |
| 1.0x | 10.7% | 25.2% | 0.0% | 0.0% | -14.7% |
| 1.5x | 12.8% | 29.6% | 0.4% | 0.0% | -21.8% |
| 2.0x | 14.3% | 32.8% | 4.0% | 0.0% | -28.5% |
| 2.5x | 14.7% | 35.0% | 11.8% | 0.0% | -34.7% |
| 3.0x | 14.4% | 37.3% | 23.4% | 0.0% | -40.4% |
| 4.0x | 11.6% | 42.6% | 48.2% | 0.0% | -50.6% |
| 5.0x | 5.8% | 47.2% | 69.2% | 0.5% | -59.4% |

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
| cagr | 8.3% | 13.3% |
| ann_vol | 9.6% | 16.7% |
| sharpe | 0.49 | 0.61 |
| sortino | 0.57 | 0.77 |
| max_drawdown | -19.9% | -25.1% |
| calmar | 0.42 | 0.53 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._