# GOLDSTEIN — Leveraged Gold Analysis
_Generated 2026-08-27T16:51:50+00:00 · instrument: **COMEX gold futures (GC/MGC)** · capital: 10,000_

> ℹ️ Gold data is real, but these auxiliary series fell back to synthetic: REAL10Y — the related macro components carry less weight of evidence.

## Market snapshot
- Last price: **4,664.90** (2026-08-27)
- 1m / 1y return: 13.8% / 37.0%
- Drawdown from high: -12.3%
- Drift estimate (shrunk): 16.6%/yr

## Volatility forecast (annualized)
| EWMA | GARCH(1,1) | HAR-RV | **Blend** |
|---|---|---|---|
| 22.6% | 21.1% | 21.1% | **21.5%** |

GARCH persistence 0.987, long-run vol 17.8%.

## Regime
- Statistical (HMM): **normal** (typical duration ~5 days)
- Macro: **hostile** (score -0.51; components: real_yield_trend -0.93, dollar_trend -0.19, risk_aversion -0.41)

## Signal
- Ensemble score: **-0.29** → **SHORT**
- Components: mom_3m +0.04, mom_6m -0.86, mom_12m +1.00, trend_50_200 -1.00, mean_reversion -0.75, macro_regime -0.51, cross_asset -0.27

## Cross-asset picture
- Confirmation score: **-0.27** (components: silver_momentum -0.95, gold_silver_ratio +0.06, miners_leadership +0.03, dollar_headwind -0.22)
- Gold/silver ratio z-score (1y): -0.19 (positive = gold rich vs silver)
- Miners (GDX) 6m momentum vs gold: 0.4%

| Asset | corr 63d | corr 252d | beta vs gold |
|---|---|---|---|
| XAGUSD | +0.86 | +0.83 | +1.97 |
| GDX | +0.83 | +0.79 | +1.38 |
| DXY | -0.51 | -0.34 | -0.06 |
| SPX | +0.39 | +0.27 | +0.12 |
| WTI | -0.17 | -0.12 | -0.23 |
| BTC | +0.53 | +0.19 | +0.27 |

Gold returns vs lagged real-yield changes: lag 0d: -0.16, lag 1d: +0.04, lag 2d: -0.01, lag 5d: +0.04, lag 10d: -0.04

## Leverage recommendation
### → **0.08x SHORT**
- Full Kelly: 2.79x — recommendation uses fractional Kelly ∧ vol-target ∧ drawdown governor ∧ conviction scaling
- Expected log growth at recommendation: 4.7%/yr
- Binding caps: fractional_kelly=1.40, vol_target=0.70, instrument_max=20.00, global_max=3.00, drawdown_multiplier=0.39, signal_conviction=0.29

## Monte Carlo (2000 block-bootstrap paths, 252d, 0.08x)
- Terminal wealth p5/p50/p95: 0.99x / 1.01x / 1.03x
- P(loss) 22.2% · P(DD>25%) 0.0% · P(DD>50%) 0.0% · **P(ruin) 0.0%**
- Expected max drawdown: -1.2%

## Leverage sweep (empirical Kelly curve)
| Lev | median growth/yr | P(loss) | P(DD>50%) | P(ruin) | E[maxDD] |
|---|---|---|---|---|---|
| 0.5x | 6.0% | 23.4% | 0.0% | 0.0% | -7.5% |
| 1.0x | 11.2% | 24.6% | 0.0% | 0.0% | -14.6% |
| 1.5x | 13.7% | 28.7% | 0.2% | 0.0% | -21.7% |
| 2.0x | 15.3% | 31.7% | 4.0% | 0.0% | -28.3% |
| 2.5x | 16.0% | 34.4% | 11.1% | 0.0% | -34.5% |
| 3.0x | 15.8% | 36.8% | 23.7% | 0.0% | -40.2% |
| 4.0x | 13.2% | 41.0% | 48.5% | 0.1% | -50.4% |
| 5.0x | 7.7% | 46.0% | 68.9% | 0.2% | -59.2% |

## Stress tests (at recommended leverage, min 1x)
- Survives all historical scenarios: **YES** · worst: `overnight_gap_20%` (-20.0% equity)
| Scenario | Asset move | Equity | Margin call |
|---|---|---|---|
| gfc_2008_liquidation | -18.1% | 0.82x | no |
| april_2013_crash | -13.8% | 0.86x | no |
| taper_2013_grind | -18.1% | 0.82x | no |
| covid_2020_margin_cascade | -12.4% | 0.88x | no |
| rate_shock_2022 | -14.7% | 0.85x | no |
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
| cagr | 7.3% | 13.3% |
| ann_vol | 9.5% | 16.8% |
| sharpe | 0.40 | 0.61 |
| sortino | 0.47 | 0.77 |
| max_drawdown | -24.9% | -25.1% |
| calmar | 0.29 | 0.53 |

---
_Research tooling, not investment advice. Leverage can lose more than the initial capital. All estimates are model outputs with material uncertainty._