# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-11-19T14:43:57+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **3,714.40** (2026-11-19)
- 1m / 1y return: -8.5% / -9.0%
- Drawdown from high: -30.2%
- Drift estimate (shrunk): 12.8%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 25.2% | 25.3% | 20.2% | **23.8%** |

GARCH persistence 0.979, long-run vol 19.7%.
Blend weights (rolling out-of-sample QLIKE): EWMA 0.33 / GARCH 0.38 / HAR 0.29.
Bootstrap 5-95% band on the blend: 13.0% – 28.6%.
HAR runs on true 5m realized variance from 2025-01-02 (squared-return proxy, bias-adjusted, before that).

## Regime
- Statistical (HMM): **turbulent** (typical duration ~22 days)
- Macro: **hostile** (score -0.30; components: real_yield_trend -0.70, dollar_trend -0.55, risk_aversion +0.36)

## Signal
- Ensemble score: **-0.59** → **SHORT**
- Components: mom_3m -0.94, mom_6m -0.90, mom_12m -0.42, trend_50_200 -1.00, mean_reversion +0.73, macro_regime -0.30, cross_asset -0.40

## Cross-asset picture
- Confirmation score: **-0.40** (components: silver_momentum -0.99, gold_silver_ratio -0.50, miners_leadership +0.57, dollar_headwind -0.67)
- Gold/silver ratio z-score (1y): +2.28 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: 9.6%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.85 | +0.82 | +2.00 |
| GDX | +0.86 | +0.79 | +1.45 |
| DXY | -0.41 | -0.39 | -0.07 |
| SPX | +0.32 | +0.30 | +0.15 |
| WTI | -0.32 | -0.16 | -0.33 |
| BTC | +0.42 | +0.22 | +0.32 |

Gold returns vs lagged real-yield changes: lag 0d: -0.17, lag 1d: +0.03, lag 2d: -0.03, lag 5d: +0.04, lag 10d: -0.03

## Leverage recommendation
### → **0.00x SHORT**
- Full Kelly: 1.52x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.2%/yr
- Binding caps: fractional_kelly=0.76, vol_target=0.63, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.00, signal_conviction=0.59

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.01x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.00x
- P(loss) 22.9% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.2%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.6% | 24.2% | 0.0% | 0.0% | -7.6% |
| 1.0x | 10.5% | 25.8% | 0.0% | 0.0% | -14.8% |
| 1.5x | 12.4% | 30.8% | 0.4% | 0.0% | -22.0% |
| 2.0x | 13.6% | 34.2% | 4.0% | 0.0% | -28.8% |
| 2.5x | 14.2% | 36.9% | 12.1% | 0.0% | -35.0% |
| 3.0x | 13.5% | 39.7% | 24.5% | 0.0% | -40.8% |
| 4.0x | 10.3% | 44.2% | 50.4% | 0.1% | -51.2% |
| 5.0x | 3.9% | 48.1% | 71.4% | 0.3% | -60.0% |

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
| cagr | 6.8% | 11.8% |
| ann_vol | 9.5% | 17.1% |
| sharpe | 0.30 | 0.49 |
| sortino | 0.35 | 0.64 |
| max_drawdown | -28.1% | -30.2% |
| calmar | 0.24 | 0.39 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._