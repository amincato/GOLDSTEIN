# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-10T10:05:08+00:00 · 5m bars · 452 days (117570 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.5% | 44.4 | 865 |
| london | 21.0% | 41.8 | 891 |
| overlap | 29.9% | 64.1 | 1671 |
| ny | 21.5% | 41.1 | 1048 |
| late | 21.3% | 36.5 | 439 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1152 trades · win 40% · PF 0.88 · expectancy -2.40 ticks (-0.08R) · PnL $-8907 · maxDD -48.7%
- **OOS**: 673 trades · win 42% · PF 0.93 · expectancy -4.35 ticks (-0.02R) · PnL $-3216 · maxDD -14.3%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1452 trades · win 54% · PF 0.81 · expectancy -3.79 ticks (-0.09R) · PnL $-13338 · maxDD -56.4%
- **OOS**: 884 trades · win 54% · PF 0.92 · expectancy -4.37 ticks (-0.05R) · PnL $-3768 · maxDD -19.5%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 728 trades · win 36% · PF 0.96 · expectancy -2.36 ticks (-0.04R) · PnL $-2382 · maxDD -15.3%
- **OOS**: 547 trades · win 32% · PF 0.79 · expectancy -12.32 ticks (-0.13R) · PnL $-8444 · maxDD -34.1%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 269 trades · win 17% · PF 1.36 · expectancy 2.88 ticks (0.32R) · PnL $9940 · maxDD -16.6%
- **OOS**: 162 trades · win 15% · PF 1.06 · expectancy 3.97 ticks (0.01R) · PnL $878 · maxDD -17.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.91 | -2.74 | -3.37 | -4.13 | -5.48 |
| vwap_reversion | -1.20 | -3.30 | -4.09 | -4.88 | -6.19 |
| momentum_burst | -1.25 | -2.72 | -3.29 | -3.95 | -5.19 |
| session_drift | -5.18 | -6.26 | -6.81 | -7.35 | -9.96 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._