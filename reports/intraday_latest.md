# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-19T11:19:03+00:00 · 5m bars · 485 days (125053 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.1% | 44.3 | 837 |
| london | 20.6% | 41.7 | 866 |
| overlap | 29.6% | 64.3 | 1640 |
| ny | 21.2% | 41.0 | 1019 |
| late | 20.8% | 35.8 | 424 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1241 trades · win 39% · PF 0.86 · expectancy -4.13 ticks (-0.09R) · PnL $-11633 · maxDD -48.7%
- **OOS**: 684 trades · win 42% · PF 0.97 · expectancy -2.38 ticks (-0.01R) · PnL $-1449 · maxDD -16.3%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1559 trades · win 54% · PF 0.83 · expectancy -3.46 ticks (-0.08R) · PnL $-13213 · maxDD -56.4%
- **OOS**: 913 trades · win 54% · PF 0.88 · expectancy -5.32 ticks (-0.07R) · PnL $-5528 · maxDD -25.7%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 963 trades · win 36% · PF 0.95 · expectancy -1.03 ticks (-0.04R) · PnL $-3857 · maxDD -31.0%
- **OOS**: 728 trades · win 33% · PF 0.86 · expectancy -6.25 ticks (-0.08R) · PnL $-7406 · maxDD -34.7%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 289 trades · win 17% · PF 1.39 · expectancy 7.44 ticks (0.34R) · PnL $11882 · maxDD -16.6%
- **OOS**: 169 trades · win 14% · PF 0.87 · expectancy -5.30 ticks (-0.11R) · PnL $-2036 · maxDD -18.4%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.29 | -3.19 | -3.87 | -4.56 | -5.93 |
| vwap_reversion | -1.28 | -3.26 | -4.08 | -4.79 | -6.10 |
| momentum_burst | -1.24 | -2.67 | -3.24 | -3.89 | -5.13 |
| session_drift | -7.83 | -8.91 | -9.45 | -9.99 | -12.51 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._