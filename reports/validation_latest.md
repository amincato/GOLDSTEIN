# GOLDSTEIN — Backtest Validation Report
_Generated 2026-07-30T22:42:08+00:00 · sample 2012-02-03 → 2026-07-30 (3780d) · instrument: futures · data: synthetic_

> ⚠️ **DEMO DATA** — validation ran on synthetic data; it proves the machinery, not a live edge. Populate `data/cache/` for real results.

## Strategy comparison (full engine: costs, financing, liquidation)
| Strategy | CAGR | Vol | Sharpe | PSR>0 | MaxDD | Calmar | Liq. |
|---|---|---|---|---|---|---|---|
| buy_hold_1x | -1.4% | 23.1% | -0.12 | 58% | -65.0% | -0.02 | 0 |
| constant_2x | -12.0% | 46.1% | -0.12 | 44% | -94.3% | -0.13 | 0 |
| constant_3x | -26.8% | 69.2% | -0.13 | 40% | -99.7% | -0.27 | 0 |
| vol_target | 2.1% | 16.3% | -0.04 | 79% | -51.6% | 0.04 | 0 |
| vol_target_x_signal | 3.4% | 9.1% | -0.02 | 94% | -23.7% | 0.14 | 0 |

## Walk-forward (yearly out-of-sample buckets)
| Year | Strat ret | B&H ret | Strat Sharpe | B&H Sharpe | Strat DD | avg lev |
|---|---|---|---|---|---|---|
| 2012 | 4.1% | 3.4% | -1.03 | -0.03 | 0.0% | 0.00x |
| 2013 | 17.0% | -12.4% | 0.96 | -0.41 | -11.8% | 0.65x |
| 2014 | 7.7% | -5.9% | 0.36 | -0.53 | -13.2% | 0.90x |
| 2015 | -4.8% | 6.7% | -0.88 | 0.24 | -8.9% | 0.75x |
| 2016 | -5.1% | -2.6% | -1.22 | -0.63 | -10.1% | 0.63x |
| 2017 | 0.2% | -21.1% | -0.38 | -1.46 | -9.5% | 0.88x |
| 2018 | 19.3% | -17.9% | 1.86 | -1.05 | -4.2% | 0.71x |
| 2019 | -4.8% | 10.5% | -0.92 | 0.46 | -12.7% | 0.48x |
| 2020 | 24.2% | 10.4% | 1.48 | 0.39 | -6.6% | 0.29x |
| 2021 | 8.6% | 32.1% | 0.53 | 1.81 | -8.5% | 0.62x |
| 2022 | -10.1% | -24.1% | -1.45 | -1.21 | -18.8% | 0.54x |
| 2023 | -0.9% | 3.8% | -0.58 | 0.03 | -10.0% | 0.84x |
| 2024 | 1.3% | 5.5% | -0.25 | 0.18 | -8.6% | 0.64x |
| 2025 | 2.6% | -0.2% | -0.13 | -0.16 | -9.5% | 0.41x |
| 2026 | -5.8% | 11.1% | -2.48 | 1.54 | -3.6% | 1.03x |

## Parameter sensitivity (vol-target × signal)
| target vol | vol window | Sharpe | CAGR | MaxDD |
|---|---|---|---|---|
| 10% | 21d | -0.02 | 3.8% | -16.1% |
| 10% | 33d | -0.04 | 3.6% | -14.4% |
| 10% | 63d | -0.10 | 3.3% | -13.1% |
| 15% | 21d | -0.01 | 3.5% | -26.0% |
| 15% | 33d | -0.02 | 3.4% | -23.7% |
| 15% | 63d | -0.09 | 2.8% | -22.4% |
| 20% | 21d | -0.01 | 3.2% | -34.6% |
| 20% | 33d | -0.02 | 3.1% | -31.8% |
| 20% | 63d | -0.08 | 2.4% | -30.2% |

## Verdict — 4/5 robustness checks passed
- ✅ adaptive_psr_above_90
- ✅ adaptive_dd_beats_bh
- ❌ positive_years_majority
- ✅ params_robust
- ✅ no_liquidations
- Years beating B&H on Sharpe: 40% · sensitivity Sharpe spread: 0.09

---
_Validation of methodology, not a guarantee of future returns._