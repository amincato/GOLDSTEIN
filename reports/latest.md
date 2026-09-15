# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-09-15T10:30:49+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,311.20** (2026-09-15)
- 1m / 1y return: -2.4% / 17.1%
- Drawdown from high: -18.9%
- Drift estimate (shrunk): 15.5%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 22.6% | 21.4% | 19.5% | **21.4%** |

GARCH persistence 0.978, long-run vol 19.4%.
Blend weights (rolling out-of-sample QLIKE): EWMA 0.37 / GARCH 0.38 / HAR 0.25.
Bootstrap 5-95% band on the blend: 12.6% – 32.3%.
HAR runs on true 5m realized variance from 2025-01-02 (squared-return proxy, bias-adjusted, before that).

## Regime
- Statistical (HMM): **turbulent** (typical duration ~24 days)
- Macro: **hostile** (score -0.46; components: real_yield_trend -0.99, dollar_trend -0.00, risk_aversion -0.38)

## Signal
- Ensemble score: **-0.18** → **SHORT**
- Components: mom_3m +0.15, mom_6m -0.83, mom_12m +0.97, trend_50_200 -1.00, mean_reversion +0.19, macro_regime -0.46, cross_asset +0.03

## Cross-asset picture
- Confirmation score: **+0.03** (components: silver_momentum -0.90, gold_silver_ratio -0.01, miners_leadership +0.84, dollar_headwind +0.17)
- Gold/silver ratio z-score (1y): +0.03 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: 18.5%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.87 | +0.83 | +1.96 |
| GDX | +0.85 | +0.79 | +1.39 |
| DXY | -0.54 | -0.37 | -0.07 |
| SPX | +0.34 | +0.29 | +0.13 |
| WTI | -0.19 | -0.14 | -0.26 |
| BTC | +0.62 | +0.20 | +0.29 |

Gold returns vs lagged real-yield changes: lag 0d: -0.16, lag 1d: +0.04, lag 2d: -0.02, lag 5d: +0.04, lag 10d: -0.04

## Leverage recommendation
### → **0.01x SHORT**
- Full Kelly: 2.53x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.0%/yr
- Binding caps: fractional_kelly=1.26, vol_target=0.70, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.05, signal_conviction=0.18

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.01x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.00x
- P(loss) 23.8% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.2%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.5% | 24.9% | 0.0% | 0.0% | -7.7% |
| 1.0x | 10.2% | 26.4% | 0.0% | 0.0% | -14.9% |
| 1.5x | 12.0% | 31.7% | 0.9% | 0.0% | -22.1% |
| 2.0x | 13.1% | 35.1% | 3.8% | 0.0% | -28.9% |
| 2.5x | 13.2% | 37.5% | 12.2% | 0.0% | -35.2% |
| 3.0x | 12.7% | 40.2% | 24.4% | 0.0% | -41.0% |
| 4.0x | 8.7% | 45.2% | 51.1% | 0.1% | -51.3% |
| 5.0x | 2.6% | 49.2% | 71.4% | 0.8% | -60.1% |

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
| cagr | 6.5% | 12.6% |
| ann_vol | 9.6% | 16.8% |
| sharpe | 0.29 | 0.55 |
| sortino | 0.34 | 0.70 |
| max_drawdown | -29.8% | -25.1% |
| calmar | 0.22 | 0.50 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._