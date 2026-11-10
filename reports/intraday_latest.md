# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-10T13:48:54+00:00 · 5m bars · 504 days (129497 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.0% | 44.5 | 824 |
| london | 20.4% | 41.6 | 852 |
| overlap | 29.4% | 64.1 | 1623 |
| ny | 21.0% | 40.9 | 1006 |
| late | 20.6% | 35.6 | 416 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1347 trades · win 35% · PF 0.89 · expectancy -1.63 ticks (-0.08R) · PnL $-10914 · maxDD -58.6%
- **OOS**: 732 trades · win 35% · PF 0.92 · expectancy -5.56 ticks (-0.05R) · PnL $-3688 · maxDD -20.0%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1625 trades · win 55% · PF 0.84 · expectancy -2.94 ticks (-0.07R) · PnL $-12690 · maxDD -56.4%
- **OOS**: 933 trades · win 52% · PF 0.83 · expectancy -7.47 ticks (-0.10R) · PnL $-7989 · maxDD -33.6%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1016 trades · win 36% · PF 0.96 · expectancy -0.69 ticks (-0.03R) · PnL $-3320 · maxDD -31.0%
- **OOS**: 755 trades · win 33% · PF 0.85 · expectancy -6.66 ticks (-0.09R) · PnL $-8130 · maxDD -32.9%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 300 trades · win 18% · PF 1.40 · expectancy 9.43 ticks (0.34R) · PnL $12559 · maxDD -16.6%
- **OOS**: 174 trades · win 13% · PF 0.88 · expectancy -6.60 ticks (-0.09R) · PnL $-2041 · maxDD -17.6%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.06 | -3.05 | -3.76 | -4.44 | -5.74 |
| vwap_reversion | -1.50 | -3.48 | -4.29 | -5.01 | -6.34 |
| momentum_burst | -1.33 | -2.74 | -3.31 | -3.95 | -5.17 |
| session_drift | -8.06 | -9.14 | -9.68 | -10.22 | -12.68 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._