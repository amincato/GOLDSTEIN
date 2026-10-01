# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-10-01T11:51:50+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,207.10** (2026-10-01)
- 1m / 1y return: -4.7% / 7.9%
- Drawdown from high: -20.9%
- Drift estimate (shrunk): 15.4%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 21.2% | 21.1% | 19.1% | **20.4%** |

GARCH persistence 0.979, long-run vol 19.6%.
Blend weights (rolling out-of-sample QLIKE): EWMA 0.29 / GARCH 0.37 / HAR 0.34.
Bootstrap 5-95% band on the blend: 13.1% – 29.4%.
HAR runs on true 5m realized variance from 2025-01-02 (squared-return proxy, bias-adjusted, before that).

## Regime
- Statistical (HMM): **calm** (typical duration ~3 days)
- Macro: **hostile** (score -0.52; components: real_yield_trend -1.00, dollar_trend -0.22, risk_aversion -0.35)

## Signal
- Ensemble score: **-0.20** → **SHORT**
- Components: mom_3m +0.39, mom_6m -0.79, mom_12m +0.80, trend_50_200 -1.00, mean_reversion +0.42, macro_regime -0.52, cross_asset -0.14

## Cross-asset picture
- Confirmation score: **-0.14** (components: silver_momentum -0.88, gold_silver_ratio -0.07, miners_leadership +0.69, dollar_headwind -0.32)
- Gold/silver ratio z-score (1y): +0.20 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: 12.7%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.85 | +0.82 | +1.95 |
| GDX | +0.84 | +0.79 | +1.40 |
| DXY | -0.52 | -0.37 | -0.06 |
| SPX | +0.43 | +0.30 | +0.13 |
| WTI | -0.22 | -0.13 | -0.25 |
| BTC | +0.54 | +0.21 | +0.30 |

Gold returns vs lagged real-yield changes: lag 0d: -0.17, lag 1d: +0.03, lag 2d: -0.02, lag 5d: +0.04, lag 10d: -0.04

## Leverage recommendation
### → **0.00x SHORT**
- Full Kelly: 2.74x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.0%/yr
- Binding caps: fractional_kelly=1.37, vol_target=0.73, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.00, signal_conviction=0.20

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.01x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.00x
- P(loss) 23.5% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.2%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.4% | 25.2% | 0.0% | 0.0% | -7.7% |
| 1.0x | 10.1% | 26.7% | 0.0% | 0.0% | -14.9% |
| 1.5x | 11.9% | 31.3% | 0.4% | 0.0% | -22.1% |
| 2.0x | 13.1% | 34.6% | 3.5% | 0.0% | -28.9% |
| 2.5x | 13.1% | 37.1% | 12.7% | 0.0% | -35.1% |
| 3.0x | 12.4% | 39.4% | 24.7% | 0.0% | -41.0% |
| 4.0x | 8.4% | 44.5% | 50.3% | 0.1% | -51.3% |
| 5.0x | 1.4% | 49.1% | 72.8% | 0.7% | -60.2% |

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
| cagr | 6.4% | 12.1% |
| ann_vol | 9.5% | 17.0% |
| sharpe | 0.27 | 0.52 |
| sortino | 0.32 | 0.67 |
| max_drawdown | -28.1% | -24.9% |
| calmar | 0.23 | 0.49 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._