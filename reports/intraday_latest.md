# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-31T11:52:45+00:00 · 5m bars · 445 days (115718 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.3 | 872 |
| london | 21.0% | 41.8 | 898 |
| overlap | 29.7% | 63.8 | 1674 |
| ny | 21.6% | 41.1 | 1057 |
| late | 21.4% | 36.6 | 444 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1128 trades · win 40% · PF 0.87 · expectancy -2.54 ticks (-0.09R) · PnL $-9361 · maxDD -48.7%
- **OOS**: 663 trades · win 42% · PF 0.96 · expectancy -2.94 ticks (-0.01R) · PnL $-1847 · maxDD -11.2%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1428 trades · win 54% · PF 0.80 · expectancy -4.25 ticks (-0.09R) · PnL $-13799 · maxDD -56.4%
- **OOS**: 874 trades · win 55% · PF 0.94 · expectancy -3.16 ticks (-0.03R) · PnL $-2683 · maxDD -16.7%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 713 trades · win 36% · PF 0.95 · expectancy -2.26 ticks (-0.04R) · PnL $-2467 · maxDD -15.3%
- **OOS**: 535 trades · win 33% · PF 0.82 · expectancy -10.88 ticks (-0.11R) · PnL $-6840 · maxDD -29.0%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 265 trades · win 17% · PF 1.34 · expectancy 2.27 ticks (0.31R) · PnL $9418 · maxDD -16.6%
- **OOS**: 160 trades · win 16% · PF 1.15 · expectancy 9.59 ticks (0.10R) · PnL $2396 · maxDD -16.8%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.15 | -2.13 | -2.77 | -3.44 | -4.79 |
| vwap_reversion | -0.94 | -3.00 | -3.79 | -4.49 | -5.80 |
| momentum_burst | -0.61 | -2.08 | -2.66 | -3.32 | -4.75 |
| session_drift | -6.64 | -7.72 | -8.26 | -8.80 | -11.44 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._