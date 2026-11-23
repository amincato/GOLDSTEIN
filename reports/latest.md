# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-11-23T16:32:29+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **3,675.40** (2026-11-23)
- 1m / 1y return: -9.0% / -9.9%
- Drawdown from high: -30.9%
- Drift estimate (shrunk): 12.5%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 34.6% | 27.4% | 26.9% | **29.6%** |

GARCH persistence 0.989, long-run vol 18.1%.
Blend weights (rolling out-of-sample QLIKE): EWMA 0.33 / GARCH 0.36 / HAR 0.31.
Bootstrap 5-95% band on the blend: 13.0% – 31.5%.
HAR runs on true 5m realized variance from 2025-01-02 (squared-return proxy, bias-adjusted, before that).

## Regime
- Statistical (HMM): **turbulent** (typical duration ~22 days)
- Macro: **hostile** (score -0.25; components: real_yield_trend -0.60, dollar_trend -0.66, risk_aversion +0.52)

## Signal
- Ensemble score: **-0.61** → **SHORT**
- Components: mom_3m -0.95, mom_6m -0.89, mom_12m -0.47, trend_50_200 -1.00, mean_reversion +0.50, macro_regime -0.25, cross_asset -0.49

## Cross-asset picture
- Confirmation score: **-0.49** (components: silver_momentum -1.00, gold_silver_ratio -0.50, miners_leadership +0.24, dollar_headwind -0.71)
- Gold/silver ratio z-score (1y): +2.55 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: 3.6%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.89 | +0.82 | +1.97 |
| GDX | +0.87 | +0.80 | +1.44 |
| DXY | -0.24 | -0.37 | -0.07 |
| SPX | +0.56 | +0.36 | +0.19 |
| WTI | -0.35 | -0.17 | -0.34 |
| BTC | +0.50 | +0.24 | +0.35 |

Gold returns vs lagged real-yield changes: lag 0d: -0.16, lag 1d: +0.02, lag 2d: -0.03, lag 5d: +0.03, lag 10d: -0.02

## Leverage recommendation
### → **0.00x SHORT**
- Full Kelly: 0.95x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.2%/yr
- Binding caps: fractional_kelly=0.47, vol_target=0.51, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.00, signal_conviction=0.61

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.01x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.00x
- P(loss) 24.1% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.2%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.5% | 25.7% | 0.0% | 0.0% | -7.8% |
| 1.0x | 10.0% | 27.3% | 0.1% | 0.0% | -15.0% |
| 1.5x | 11.7% | 32.2% | 0.5% | 0.0% | -22.3% |
| 2.0x | 12.4% | 34.9% | 4.3% | 0.0% | -29.1% |
| 2.5x | 12.3% | 37.9% | 13.7% | 0.0% | -35.4% |
| 3.0x | 11.5% | 41.0% | 25.9% | 0.1% | -41.3% |
| 4.0x | 8.4% | 45.4% | 51.2% | 0.1% | -51.6% |
| 5.0x | 0.7% | 49.4% | 71.5% | 0.6% | -60.4% |

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
| cagr | 7.2% | 11.6% |
| ann_vol | 9.6% | 17.2% |
| sharpe | 0.34 | 0.48 |
| sortino | 0.40 | 0.62 |
| max_drawdown | -28.5% | -33.9% |
| calmar | 0.25 | 0.34 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._