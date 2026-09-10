# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-09-10T10:05:41+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,437.80** (2026-09-10)
- 1m / 1y return: 0.7% / 21.8%
- Drawdown from high: -16.6%
- Drift estimate (shrunk): 15.9%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 23.2% | 22.2% | 19.6% | **21.9%** |

GARCH persistence 0.978, long-run vol 19.4%.
Blend weights (rolling out-of-sample QLIKE): EWMA 0.36 / GARCH 0.37 / HAR 0.27.
Bootstrap 5-95% band on the blend: 12.6% – 28.2%.
HAR runs on true 5m realized variance from 2025-01-02 (squared-return proxy, bias-adjusted, before that).

## Regime
- Statistical (HMM): **normal** (typical duration ~5 days)
- Macro: **hostile** (score -0.39; components: real_yield_trend -0.84, dollar_trend +0.12, risk_aversion -0.43)

## Signal
- Ensemble score: **-0.18** → **SHORT**
- Components: mom_3m +0.56, mom_6m -0.91, mom_12m +0.96, trend_50_200 -1.00, mean_reversion -0.10, macro_regime -0.39, cross_asset -0.13

## Cross-asset picture
- Confirmation score: **-0.13** (components: silver_momentum -0.96, gold_silver_ratio +0.06, miners_leadership +0.44, dollar_headwind -0.07)
- Gold/silver ratio z-score (1y): -0.18 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: 7.1%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.86 | +0.83 | +1.96 |
| GDX | +0.83 | +0.79 | +1.39 |
| DXY | -0.50 | -0.36 | -0.07 |
| SPX | +0.35 | +0.29 | +0.13 |
| WTI | -0.20 | -0.13 | -0.24 |
| BTC | +0.57 | +0.20 | +0.29 |

Gold returns vs lagged real-yield changes: lag 0d: -0.16, lag 1d: +0.04, lag 2d: -0.01, lag 5d: +0.04, lag 10d: -0.04

## Leverage recommendation
### → **0.02x SHORT**
- Full Kelly: 2.53x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.1%/yr
- Binding caps: fractional_kelly=1.26, vol_target=0.69, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.17, signal_conviction=0.18

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.02x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.01x
- P(loss) 21.4% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.3%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.7% | 22.7% | 0.0% | 0.0% | -7.7% |
| 1.0x | 10.6% | 24.3% | 0.0% | 0.0% | -14.9% |
| 1.5x | 12.7% | 29.1% | 0.5% | 0.0% | -22.1% |
| 2.0x | 14.0% | 32.4% | 4.5% | 0.0% | -28.8% |
| 2.5x | 14.4% | 36.4% | 12.6% | 0.0% | -35.1% |
| 3.0x | 13.9% | 38.8% | 23.4% | 0.0% | -40.9% |
| 4.0x | 11.0% | 43.9% | 51.3% | 0.1% | -51.2% |
| 5.0x | 3.5% | 48.0% | 72.0% | 0.4% | -60.0% |

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
| cagr | 7.0% | 13.0% |
| ann_vol | 9.6% | 16.8% |
| sharpe | 0.36 | 0.58 |
| sortino | 0.41 | 0.74 |
| max_drawdown | -24.3% | -25.1% |
| calmar | 0.29 | 0.52 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._