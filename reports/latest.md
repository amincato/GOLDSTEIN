# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-08-28T17:45:16+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,527.70** (2026-08-28)
- 1m / 1y return: 11.8% / 31.9%
- Drawdown from high: -14.9%
- Drift estimate (shrunk): 16.2%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 22.4% | 20.7% | 20.1% | **21.0%** |

GARCH persistence 0.988, long-run vol 18.0%.

## Regime
- Statistical (HMM): **normal** (typical duration ~5 days)
- Macro: **hostile** (score -0.50; components: real_yield_trend -0.90, dollar_trend -0.17, risk_aversion -0.43)

## Signal
- Ensemble score: **-0.26** → **SHORT**
- Components: mom_3m +0.14, mom_6m -0.82, mom_12m +1.00, trend_50_200 -1.00, mean_reversion -0.38, macro_regime -0.50, cross_asset -0.28

## Cross-asset picture
- Confirmation score: **-0.28** (components: silver_momentum -0.97, gold_silver_ratio +0.05, miners_leadership +0.02, dollar_headwind -0.24)
- Gold/silver ratio z-score (1y): -0.15 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: 0.4%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.86 | +0.83 | +1.97 |
| GDX | +0.84 | +0.79 | +1.39 |
| DXY | -0.52 | -0.35 | -0.06 |
| SPX | +0.38 | +0.26 | +0.12 |
| WTI | -0.16 | -0.12 | -0.23 |
| BTC | +0.54 | +0.19 | +0.27 |

Gold returns vs lagged real-yield changes: lag 0d: -0.16, lag 1d: +0.04, lag 2d: -0.01, lag 5d: +0.04, lag 10d: -0.04

## Leverage recommendation
### → **0.05x SHORT**
- Full Kelly: 2.83x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.3%/yr
- Binding caps: fractional_kelly=1.41, vol_target=0.71, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.26, signal_conviction=0.26

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.05x)
- Terminal wealth p5/p50/p95: 0.99x / 1.01x / 1.02x
- P(loss) 22.6% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.8%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.9% | 24.0% | 0.0% | 0.0% | -7.6% |
| 1.0x | 11.1% | 25.5% | 0.0% | 0.0% | -14.7% |
| 1.5x | 13.6% | 28.7% | 0.2% | 0.0% | -21.8% |
| 2.0x | 15.1% | 31.8% | 4.1% | 0.0% | -28.4% |
| 2.5x | 16.0% | 34.3% | 11.3% | 0.0% | -34.6% |
| 3.0x | 15.9% | 36.7% | 23.6% | 0.0% | -40.3% |
| 4.0x | 13.4% | 41.9% | 47.9% | 0.0% | -50.5% |
| 5.0x | 7.9% | 46.0% | 69.4% | 0.4% | -59.3% |

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
| cagr | 7.8% | 12.9% |
| ann_vol | 9.6% | 16.8% |
| sharpe | 0.44 | 0.58 |
| sortino | 0.51 | 0.74 |
| max_drawdown | -23.6% | -25.1% |
| calmar | 0.33 | 0.51 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._