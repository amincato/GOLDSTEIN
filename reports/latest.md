# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-09-29T11:37:38+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,192.80** (2026-09-29)
- 1m / 1y return: -6.4% / 8.8%
- Drawdown from high: -21.2%
- Drift estimate (shrunk): 15.2%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 22.5% | 22.7% | 19.1% | **21.4%** |

GARCH persistence 0.979, long-run vol 19.6%.
Blend weights (rolling out-of-sample QLIKE): EWMA 0.32 / GARCH 0.34 / HAR 0.34.
Bootstrap 5-95% band on the blend: 12.5% – 30.2%.
HAR runs on true 5m realized variance from 2025-01-02 (squared-return proxy, bias-adjusted, before that).

## Regime
- Statistical (HMM): **normal** (typical duration ~5 days)
- Macro: **hostile** (score -0.51; components: real_yield_trend -1.00, dollar_trend -0.17, risk_aversion -0.36)

## Signal
- Ensemble score: **-0.03** → **FLAT**
- Components: mom_3m +0.68, mom_6m -0.32, mom_12m +0.90, trend_50_200 -1.00, mean_reversion +0.48, macro_regime -0.51, cross_asset +0.04

## Cross-asset picture
- Confirmation score: **+0.04** (components: silver_momentum -0.48, gold_silver_ratio -0.05, miners_leadership +0.71, dollar_headwind -0.02)
- Gold/silver ratio z-score (1y): +0.15 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: 13.4%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.85 | +0.82 | +1.95 |
| GDX | +0.84 | +0.79 | +1.40 |
| DXY | -0.52 | -0.37 | -0.06 |
| SPX | +0.42 | +0.30 | +0.13 |
| WTI | -0.22 | -0.13 | -0.26 |
| BTC | +0.54 | +0.21 | +0.30 |

Gold returns vs lagged real-yield changes: lag 0d: -0.17, lag 1d: +0.03, lag 2d: -0.02, lag 5d: +0.04, lag 10d: -0.04

## Leverage recommendation
### → **0.00x FLAT**
- Full Kelly: 2.44x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.1%/yr
- Binding caps: fractional_kelly=1.22, vol_target=0.70, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.00, signal_conviction=0.03

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.01x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.00x
- P(loss) 23.4% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.2%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.5% | 24.8% | 0.0% | 0.0% | -7.7% |
| 1.0x | 10.3% | 26.1% | 0.1% | 0.0% | -14.9% |
| 1.5x | 12.1% | 31.4% | 0.6% | 0.0% | -22.1% |
| 2.0x | 13.2% | 34.8% | 4.8% | 0.0% | -28.9% |
| 2.5x | 13.3% | 37.8% | 11.8% | 0.0% | -35.1% |
| 3.0x | 12.3% | 40.0% | 24.6% | 0.0% | -40.9% |
| 4.0x | 9.0% | 44.2% | 50.2% | 0.2% | -51.3% |
| 5.0x | 2.4% | 48.8% | 71.8% | 0.8% | -60.1% |

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
| cagr | 6.9% | 12.3% |
| ann_vol | 9.6% | 17.0% |
| sharpe | 0.32 | 0.53 |
| sortino | 0.38 | 0.68 |
| max_drawdown | -26.8% | -24.9% |
| calmar | 0.26 | 0.49 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._