# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-08T10:07:42+00:00 · 5m bars · 450 days (117017 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.4 | 867 |
| london | 21.0% | 41.8 | 893 |
| overlap | 29.9% | 64.0 | 1673 |
| ny | 21.5% | 41.1 | 1050 |
| late | 21.4% | 36.5 | 440 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1146 trades · win 40% · PF 0.88 · expectancy -2.32 ticks (-0.08R) · PnL $-8801 · maxDD -48.7%
- **OOS**: 673 trades · win 42% · PF 0.94 · expectancy -3.99 ticks (-0.02R) · PnL $-2914 · maxDD -12.7%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1446 trades · win 54% · PF 0.81 · expectancy -4.01 ticks (-0.09R) · PnL $-13607 · maxDD -56.4%
- **OOS**: 878 trades · win 55% · PF 0.93 · expectancy -3.85 ticks (-0.04R) · PnL $-3216 · maxDD -19.3%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 725 trades · win 36% · PF 0.96 · expectancy -2.16 ticks (-0.04R) · PnL $-2032 · maxDD -15.3%
- **OOS**: 540 trades · win 32% · PF 0.78 · expectancy -12.24 ticks (-0.13R) · PnL $-8360 · maxDD -32.5%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 268 trades · win 17% · PF 1.36 · expectancy 3.08 ticks (0.33R) · PnL $10042 · maxDD -16.6%
- **OOS**: 161 trades · win 16% · PF 1.06 · expectancy 4.28 ticks (0.02R) · PnL $972 · maxDD -17.2%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.85 | -2.68 | -3.31 | -4.07 | -5.43 |
| vwap_reversion | -1.09 | -3.19 | -3.98 | -4.77 | -6.08 |
| momentum_burst | -1.12 | -2.59 | -3.16 | -3.82 | -5.06 |
| session_drift | -4.89 | -5.98 | -6.52 | -7.06 | -9.68 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._