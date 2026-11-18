# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-11-18T14:37:00+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **3,777.50** (2026-11-18)
- 1m / 1y return: -9.0% / -7.1%
- Drawdown from high: -29.0%
- Drift estimate (shrunk): 13.0%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 24.2% | 22.5% | 20.0% | **22.5%** |

GARCH persistence 0.979, long-run vol 19.7%.
Blend weights (rolling out-of-sample QLIKE): EWMA 0.40 / GARCH 0.33 / HAR 0.28.
Bootstrap 5-95% band on the blend: 13.1% – 30.2%.
HAR runs on true 5m realized variance from 2025-01-02 (squared-return proxy, bias-adjusted, before that).

## Regime
- Statistical (HMM): **turbulent** (typical duration ~22 days)
- Macro: **hostile** (score -0.31; components: real_yield_trend -0.67, dollar_trend -0.58, risk_aversion +0.31)

## Signal
- Ensemble score: **-0.53** → **SHORT**
- Components: mom_3m -0.85, mom_6m -0.83, mom_12m -0.18, trend_50_200 -1.00, mean_reversion +0.64, macro_regime -0.31, cross_asset -0.38

## Cross-asset picture
- Confirmation score: **-0.38** (components: silver_momentum -0.99, gold_silver_ratio -0.50, miners_leadership +0.60, dollar_headwind -0.65)
- Gold/silver ratio z-score (1y): +2.44 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: 10.5%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.85 | +0.82 | +2.00 |
| GDX | +0.86 | +0.79 | +1.45 |
| DXY | -0.42 | -0.39 | -0.07 |
| SPX | +0.33 | +0.30 | +0.15 |
| WTI | -0.34 | -0.17 | -0.34 |
| BTC | +0.47 | +0.22 | +0.32 |

Gold returns vs lagged real-yield changes: lag 0d: -0.18, lag 1d: +0.03, lag 2d: -0.04, lag 5d: +0.04, lag 10d: -0.03

## Leverage recommendation
### → **0.00x SHORT**
- Full Kelly: 1.75x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.1%/yr
- Binding caps: fractional_kelly=0.87, vol_target=0.67, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.00, signal_conviction=0.53

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.01x)
- Terminal wealth p5/p50/p95: 1.00x / 1.00x / 1.00x
- P(loss) 24.2% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -0.2%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 5.6% | 25.5% | 0.0% | 0.0% | -7.7% |
| 1.0x | 10.5% | 27.4% | 0.1% | 0.0% | -14.9% |
| 1.5x | 12.3% | 31.3% | 0.5% | 0.0% | -22.1% |
| 2.0x | 13.4% | 34.8% | 3.1% | 0.0% | -28.9% |
| 2.5x | 13.5% | 37.5% | 12.9% | 0.0% | -35.1% |
| 3.0x | 13.4% | 40.2% | 25.8% | 0.1% | -40.9% |
| 4.0x | 10.2% | 44.9% | 50.3% | 0.1% | -51.3% |
| 5.0x | 2.7% | 48.7% | 71.1% | 0.5% | -60.1% |

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
| cagr | 7.4% | 11.6% |
| ann_vol | 9.6% | 17.1% |
| sharpe | 0.37 | 0.48 |
| sortino | 0.43 | 0.62 |
| max_drawdown | -24.5% | -29.0% |
| calmar | 0.30 | 0.40 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._