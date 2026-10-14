# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-10-14T10:40:14+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,163.10** (2026-10-14)
- 1m / 1y return: -5.1% / -0.0%
- Drawdown from high: -21.7%
- Drift estimate (shrunk): 15.2%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 17.9% | 17.8% | 17.4% | **17.7%** |

GARCH persistence 0.978, long-run vol 19.5%.
Blend weights (rolling out-of-sample QLIKE): EWMA 0.37 / GARCH 0.38 / HAR 0.25.
Bootstrap 5-95% band on the blend: 12.8% – 31.0%.
HAR runs on true 5m realized variance from 2025-01-02 (squared-return proxy, bias-adjusted, before that).

## Regime
- Statistical (HMM): **calm** (typical duration ~3 days)
- Macro: **hostile** (score -0.63; components: real_yield_trend -1.00, dollar_trend -0.51, risk_aversion -0.39)

## Signal
- Ensemble score: **-0.43** → **SHORT**
- Components: mom_3m +0.36, mom_6m -0.89, mom_12m +0.02, trend_50_200 -1.00, mean_reversion +0.36, macro_regime -0.63, cross_asset -0.43

## Cross-asset picture
- Confirmation score: **-0.43** (components: silver_momentum -0.97, gold_silver_ratio -0.18, miners_leadership +0.11, dollar_headwind -0.69)
- Gold/silver ratio z-score (1y): +0.54 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: 1.7%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.84 | +0.82 | +1.96 |
| GDX | +0.84 | +0.79 | +1.40 |
| DXY | -0.49 | -0.36 | -0.06 |
| SPX | +0.38 | +0.30 | +0.13 |
| WTI | -0.09 | -0.13 | -0.26 |
| BTC | +0.49 | +0.21 | +0.30 |

Gold returns vs lagged real-yield changes: lag 0d: -0.17, lag 1d: +0.03, lag 2d: -0.02, lag 5d: +0.03, lag 10d: -0.04

## Leverage recommendation
### → **0.00x SHORT**
- Full Kelly: 3.54x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.1%/yr
- Binding caps: fractional_kelly=1.77, vol_target=0.85, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.00, signal_conviction=0.43

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.01x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.00x
- P(loss) 20.4% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.2%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.6% | 22.2% | 0.0% | 0.0% | -7.6% |
| 1.0x | 10.3% | 24.0% | 0.0% | 0.0% | -14.8% |
| 1.5x | 12.2% | 29.1% | 0.6% | 0.0% | -22.0% |
| 2.0x | 13.4% | 32.8% | 3.4% | 0.0% | -28.7% |
| 2.5x | 13.7% | 35.8% | 12.5% | 0.0% | -34.9% |
| 3.0x | 13.1% | 38.9% | 23.3% | 0.0% | -40.7% |
| 4.0x | 10.0% | 43.3% | 49.3% | 0.2% | -51.0% |
| 5.0x | 3.5% | 48.4% | 70.4% | 0.5% | -59.7% |

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
| cagr | 7.0% | 12.7% |
| ann_vol | 9.6% | 17.0% |
| sharpe | 0.33 | 0.55 |
| sortino | 0.39 | 0.71 |
| max_drawdown | -24.5% | -24.9% |
| calmar | 0.29 | 0.51 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._