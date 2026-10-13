# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-13T12:59:31+00:00 · 5m bars · 480 days (123968 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.2% | 44.4 | 841 |
| london | 20.7% | 41.8 | 871 |
| overlap | 29.6% | 64.2 | 1642 |
| ny | 21.3% | 41.1 | 1023 |
| late | 21.0% | 36.0 | 426 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1228 trades · win 39% · PF 0.86 · expectancy -4.16 ticks (-0.09R) · PnL $-11559 · maxDD -48.7%
- **OOS**: 682 trades · win 41% · PF 0.96 · expectancy -2.59 ticks (-0.02R) · PnL $-1574 · maxDD -16.5%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1542 trades · win 54% · PF 0.83 · expectancy -3.82 ticks (-0.08R) · PnL $-13707 · maxDD -56.4%
- **OOS**: 912 trades · win 54% · PF 0.89 · expectancy -4.85 ticks (-0.07R) · PnL $-5006 · maxDD -25.1%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 951 trades · win 36% · PF 0.94 · expectancy -1.41 ticks (-0.04R) · PnL $-4144 · maxDD -31.0%
- **OOS**: 720 trades · win 33% · PF 0.85 · expectancy -5.79 ticks (-0.08R) · PnL $-7362 · maxDD -34.4%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 286 trades · win 17% · PF 1.38 · expectancy 6.61 ticks (0.34R) · PnL $11623 · maxDD -16.6%
- **OOS**: 168 trades · win 14% · PF 0.88 · expectancy -4.40 ticks (-0.12R) · PnL $-1863 · maxDD -18.2%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.34 | -3.25 | -3.93 | -4.62 | -5.96 |
| vwap_reversion | -1.32 | -3.31 | -4.13 | -4.93 | -6.25 |
| momentum_burst | -1.05 | -2.48 | -3.05 | -3.70 | -4.95 |
| session_drift | -7.53 | -8.61 | -9.15 | -9.69 | -12.26 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._