# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-11-17T14:57:15+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **3,869.20** (2026-11-17)
- 1m / 1y return: -6.6% / -5.0%
- Drawdown from high: -27.2%
- Drift estimate (shrunk): 13.5%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 23.3% | 23.4% | 19.3% | **22.1%** |

GARCH persistence 0.979, long-run vol 19.7%.
Blend weights (rolling out-of-sample QLIKE): EWMA 0.35 / GARCH 0.35 / HAR 0.30.
Bootstrap 5-95% band on the blend: 13.4% – 32.0%.
HAR runs on true 5m realized variance from 2025-01-02 (squared-return proxy, bias-adjusted, before that).

## Regime
- Statistical (HMM): **turbulent** (typical duration ~20 days)
- Macro: **hostile** (score -0.36; components: real_yield_trend -0.77, dollar_trend -0.57, risk_aversion +0.25)

## Signal
- Ensemble score: **-0.52** → **SHORT**
- Components: mom_3m -0.81, mom_6m -0.79, mom_12m -0.16, trend_50_200 -1.00, mean_reversion +0.47, macro_regime -0.36, cross_asset -0.32

## Cross-asset picture
- Confirmation score: **-0.32** (components: silver_momentum -0.99, gold_silver_ratio -0.50, miners_leadership +0.73, dollar_headwind -0.53)
- Gold/silver ratio z-score (1y): +2.18 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: 13.9%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.84 | +0.82 | +2.01 |
| GDX | +0.85 | +0.79 | +1.44 |
| DXY | -0.41 | -0.39 | -0.07 |
| SPX | +0.34 | +0.30 | +0.15 |
| WTI | -0.35 | -0.17 | -0.34 |
| BTC | +0.46 | +0.21 | +0.32 |

Gold returns vs lagged real-yield changes: lag 0d: -0.18, lag 1d: +0.03, lag 2d: -0.04, lag 5d: +0.04, lag 10d: -0.03

## Leverage recommendation
### → **0.00x SHORT**
- Full Kelly: 1.91x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.2%/yr
- Binding caps: fractional_kelly=0.96, vol_target=0.68, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.00, signal_conviction=0.52

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.01x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.00x
- P(loss) 22.8% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.2%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.7% | 24.1% | 0.0% | 0.0% | -7.6% |
| 1.0x | 10.6% | 25.4% | 0.0% | 0.0% | -14.7% |
| 1.5x | 12.6% | 30.1% | 0.3% | 0.0% | -21.9% |
| 2.0x | 13.7% | 33.6% | 3.5% | 0.0% | -28.6% |
| 2.5x | 14.0% | 36.6% | 10.8% | 0.0% | -34.9% |
| 3.0x | 13.7% | 39.7% | 24.4% | 0.0% | -40.7% |
| 4.0x | 10.9% | 43.5% | 50.0% | 0.0% | -51.0% |
| 5.0x | 4.8% | 47.9% | 71.4% | 0.4% | -59.8% |

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
| cagr | 7.2% | 11.8% |
| ann_vol | 9.6% | 17.1% |
| sharpe | 0.34 | 0.49 |
| sortino | 0.40 | 0.64 |
| max_drawdown | -26.8% | -27.6% |
| calmar | 0.27 | 0.43 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._