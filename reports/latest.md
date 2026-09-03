# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-09-03T10:08:54+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,472.40** (2026-09-03)
- 1m / 1y return: 5.4% / 25.4%
- Drawdown from high: -15.9%
- Drift estimate (shrunk): 15.9%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 24.6% | 22.0% | 19.5% | **22.0%** |

GARCH persistence 0.978, long-run vol 19.4%.
Blend weights (rolling out-of-sample QLIKE): EWMA 0.31 / GARCH 0.36 / HAR 0.33.
Bootstrap 5-95% band on the blend: 12.8% – 25.3%.
HAR runs on true 5m realized variance from 2025-01-02 (squared-return proxy, bias-adjusted, before that).

## Regime
- Statistical (HMM): **turbulent** (typical duration ~24 days)
- Macro: **hostile** (score -0.46; components: real_yield_trend -0.95, dollar_trend +0.01, risk_aversion -0.44)

## Signal
- Ensemble score: **-0.18** → **SHORT**
- Components: mom_3m +0.29, mom_6m -0.72, mom_12m +0.99, trend_50_200 -1.00, mean_reversion -0.19, macro_regime -0.46, cross_asset -0.14

## Cross-asset picture
- Confirmation score: **-0.14** (components: silver_momentum -0.85, gold_silver_ratio +0.02, miners_leadership +0.36, dollar_headwind -0.08)
- Gold/silver ratio z-score (1y): -0.06 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: 5.7%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.87 | +0.83 | +1.96 |
| GDX | +0.83 | +0.79 | +1.38 |
| DXY | -0.51 | -0.35 | -0.06 |
| SPX | +0.40 | +0.27 | +0.12 |
| WTI | -0.17 | -0.13 | -0.25 |
| BTC | +0.56 | +0.19 | +0.27 |

Gold returns vs lagged real-yield changes: lag 0d: -0.16, lag 1d: +0.03, lag 2d: -0.01, lag 5d: +0.04, lag 10d: -0.04

## Leverage recommendation
### → **0.03x SHORT**
- Full Kelly: 2.51x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.1%/yr
- Binding caps: fractional_kelly=1.25, vol_target=0.68, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.20, signal_conviction=0.18

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.03x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.01x
- P(loss) 22.6% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.5%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.6% | 23.9% | 0.0% | 0.0% | -7.7% |
| 1.0x | 10.5% | 25.4% | 0.0% | 0.0% | -14.9% |
| 1.5x | 12.6% | 29.5% | 0.4% | 0.0% | -22.1% |
| 2.0x | 13.7% | 32.9% | 4.3% | 0.0% | -28.8% |
| 2.5x | 14.2% | 35.6% | 12.7% | 0.0% | -35.1% |
| 3.0x | 13.9% | 38.4% | 24.1% | 0.0% | -40.9% |
| 4.0x | 11.0% | 43.3% | 49.8% | 0.1% | -51.2% |
| 5.0x | 4.2% | 47.7% | 70.9% | 0.5% | -59.9% |

## Stress tests (at recommended leverage, min 1x)
- Survives all historical scenarios: **YES** · worst: `secular_bear_1980_99` (-61.9% equity)
- Survives all CENTURY scenarios (1974-76, 1980-82, 1980-99, 2011-15, era financing included): **NO**
| Scenario | Asset move | Equity | Margin call |
|---|---|---|---|
| gfc_2008_liquidation | -18.1% | 0.82x | no |
| april_2013_crash | -13.8% | 0.86x | no |
| taper_2013_grind | -18.1% | 0.82x | no |
| covid_2020_margin_cascade | -12.4% | 0.88x | no |
| rate_shock_2022 | -14.7% | 0.85x | no |
| bretton_shock_1974_76 | -32.5% | 0.67x | no |
| volcker_collapse_1980_82 | -53.3% | 0.47x | no |
| secular_bear_1980_99 | -61.9% | 0.38x | no |
| post_qe_grind_2011_15 | -39.3% | 0.61x | no |
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
| cagr | 6.0% | 12.9% |
| ann_vol | 9.5% | 16.8% |
| sharpe | 0.26 | 0.58 |
| sortino | 0.31 | 0.74 |
| max_drawdown | -29.1% | -25.1% |
| calmar | 0.21 | 0.52 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._