# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-11-03T13:03:39+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **3,935.80** (2026-11-03)
- 1m / 1y return: -6.0% / -1.9%
- Drawdown from high: -26.0%
- Drift estimate (shrunk): 13.6%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 21.4% | 22.3% | 17.6% | **20.5%** |

GARCH persistence 0.979, long-run vol 19.7%.
Blend weights (rolling out-of-sample QLIKE): EWMA 0.30 / GARCH 0.37 / HAR 0.33.
Bootstrap 5-95% band on the blend: 13.2% – 32.6%.
HAR runs on true 5m realized variance from 2025-01-02 (squared-return proxy, bias-adjusted, before that).

## Regime
- Statistical (HMM): **normal** (typical duration ~5 days)
- Macro: **hostile** (score -0.40; components: real_yield_trend -0.64, dollar_trend -0.49, risk_aversion -0.09)

## Signal
- Ensemble score: **-0.44** → **SHORT**
- Components: mom_3m -0.49, mom_6m -0.79, mom_12m +0.19, trend_50_200 -1.00, mean_reversion +0.53, macro_regime -0.40, cross_asset -0.45

## Cross-asset picture
- Confirmation score: **-0.45** (components: silver_momentum -0.97, gold_silver_ratio -0.50, miners_leadership +0.35, dollar_headwind -0.65)
- Gold/silver ratio z-score (1y): +1.86 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: 5.4%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.85 | +0.83 | +2.02 |
| GDX | +0.87 | +0.79 | +1.42 |
| DXY | -0.41 | -0.37 | -0.07 |
| SPX | +0.45 | +0.34 | +0.15 |
| WTI | -0.18 | -0.16 | -0.32 |
| BTC | +0.49 | +0.21 | +0.32 |

Gold returns vs lagged real-yield changes: lag 0d: -0.16, lag 1d: +0.02, lag 2d: -0.03, lag 5d: +0.04, lag 10d: -0.04

## Leverage recommendation
### → **0.00x SHORT**
- Full Kelly: 2.29x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.0%/yr
- Binding caps: fractional_kelly=1.15, vol_target=0.73, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.00, signal_conviction=0.44

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.01x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.00x
- P(loss) 23.5% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.2%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.5% | 24.8% | 0.0% | 0.0% | -7.7% |
| 1.0x | 10.2% | 26.9% | 0.1% | 0.0% | -14.9% |
| 1.5x | 12.1% | 30.6% | 0.7% | 0.0% | -22.1% |
| 2.0x | 13.3% | 33.2% | 4.5% | 0.0% | -28.8% |
| 2.5x | 14.0% | 36.4% | 12.4% | 0.0% | -35.0% |
| 3.0x | 14.1% | 38.6% | 24.9% | 0.0% | -40.7% |
| 4.0x | 11.2% | 43.5% | 49.1% | 0.1% | -51.0% |
| 5.0x | 5.5% | 47.1% | 69.8% | 0.6% | -59.7% |

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
| cagr | 7.1% | 12.0% |
| ann_vol | 9.6% | 17.0% |
| sharpe | 0.35 | 0.52 |
| sortino | 0.41 | 0.67 |
| max_drawdown | -26.8% | -26.7% |
| calmar | 0.27 | 0.45 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._