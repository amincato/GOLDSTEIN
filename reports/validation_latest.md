# GOLDSTEIN — Backtest Validation Report
_Generated 2026-09-26T11:38:32+00:00 · sample 2000-08-30 → 2026-09-25 (6543d) · instrument: futures · data: cache_

## Strategy comparison (full engine: costs, financing, liquidation)
| Strategy | CAGR | Vol | Sharpe | PSR>0 | MaxDD | Calmar | Liq. |
|---|---|---|---|---|---|---|---|
| buy_hold_1x | 10.9% | 17.9% | 0.45 | 100% | -44.9% | 0.24 | 0 |
| constant_2x | 16.7% | 35.8% | 0.50 | 100% | -74.2% | 0.23 | 0 |
| constant_3x | 18.8% | 53.8% | 0.52 | 100% | -89.7% | 0.21 | 0 |
| vol_target | 11.4% | 16.0% | 0.51 | 100% | -46.5% | 0.25 | 0 |
| vol_target_x_signal | 5.2% | 9.8% | 0.16 | 100% | -34.5% | 0.15 | 0 |

## Walk-forward (yearly out-of-sample buckets)
| Year | Strat ret | B&H ret | Strat Sharpe | B&H Sharpe | Strat DD | avg lev |
|---|---|---|---|---|---|---|
| 2001 | 0.5% | 2.5% | -1.14 | -0.03 | -4.0% | 0.13x |
| 2002 | 15.8% | 24.9% | 1.12 | 1.41 | -6.2% | 0.71x |
| 2003 | 10.7% | 19.8% | 0.62 | 0.92 | -10.5% | 0.61x |
| 2004 | -3.0% | 5.3% | -0.66 | 0.15 | -9.3% | 0.46x |
| 2005 | 5.9% | 18.5% | 0.25 | 1.10 | -7.3% | 0.57x |
| 2006 | 13.3% | 23.0% | 0.77 | 0.82 | -11.3% | 0.45x |
| 2007 | 20.4% | 31.4% | 1.46 | 1.49 | -5.4% | 0.59x |
| 2008 | -1.2% | 5.8% | -0.40 | 0.21 | -13.1% | 0.39x |
| 2009 | 12.1% | 23.9% | 0.79 | 0.90 | -7.7% | 0.47x |
| 2010 | 25.0% | 29.8% | 1.60 | 1.46 | -6.2% | 0.73x |
| 2011 | 14.6% | 10.2% | 0.81 | 0.38 | -9.2% | 0.68x |
| 2012 | -5.5% | 7.0% | -1.35 | 0.25 | -11.3% | 0.42x |
| 2013 | 18.8% | -28.2% | 1.23 | -1.56 | -7.5% | 0.50x |
| 2014 | -5.8% | -1.5% | -1.23 | -0.32 | -9.1% | 0.43x |
| 2015 | 5.3% | -10.4% | 0.18 | -0.95 | -6.2% | 0.55x |
| 2016 | -8.1% | 8.5% | -1.24 | 0.34 | -8.7% | 0.57x |
| 2017 | -6.7% | 13.6% | -1.94 | 0.90 | -9.2% | 0.47x |
| 2018 | 3.0% | -2.2% | -0.08 | -0.53 | -4.5% | 0.74x |
| 2019 | 14.7% | 18.9% | 1.09 | 1.21 | -5.9% | 0.73x |
| 2020 | 18.2% | 24.6% | 1.07 | 0.94 | -8.8% | 0.63x |
| 2021 | -2.0% | -3.5% | -1.16 | -0.43 | -6.3% | 0.31x |
| 2022 | -5.8% | -0.1% | -1.13 | -0.18 | -10.2% | 0.47x |
| 2023 | -7.5% | 13.5% | -1.54 | 0.71 | -11.1% | 0.56x |
| 2024 | 19.6% | 27.5% | 1.20 | 1.40 | -7.9% | 0.78x |
| 2025 | 46.5% | 64.4% | 2.62 | 2.30 | -5.4% | 0.67x |
| 2026 | 1.3% | -0.6% | -0.18 | -0.00 | -11.7% | 0.30x |

## Parameter sensitivity (vol-target × signal)
| target vol | vol window | Sharpe | CAGR | MaxDD |
|---|---|---|---|---|
| 10% | 21d | 0.05 | 4.2% | -25.0% |
| 10% | 33d | 0.05 | 4.2% | -23.8% |
| 10% | 63d | 0.04 | 4.1% | -22.5% |
| 15% | 21d | 0.16 | 5.3% | -36.1% |
| 15% | 33d | 0.16 | 5.2% | -34.5% |
| 15% | 63d | 0.15 | 5.1% | -32.7% |
| 20% | 21d | 0.21 | 6.2% | -45.8% |
| 20% | 33d | 0.21 | 6.1% | -44.0% |
| 20% | 63d | 0.21 | 6.0% | -41.9% |

## Multiple-testing honesty
- Deflated Sharpe (adaptive, vs best-of-13-trials luck): **99%**
- White reality check: best family member `constant_3x` excess 19.8%/yr vs B&H, p-value **0.000** (500 bootstraps)
- Financing in engine: fedfunds_path

## Verdict — 6/7 robustness checks passed
- ✅ adaptive_psr_above_90
- ✅ adaptive_dsr_above_50
- ✅ family_beats_bh_reality_check
- ✅ adaptive_dd_beats_bh
- ❌ positive_years_majority
- ✅ params_robust
- ✅ no_liquidations
- Years beating B&H on Sharpe: 27% · sensitivity Sharpe spread: 0.17

---
_Validation of methodology, not a guarantee of future returns._