# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-06T12:15:52+00:00 · 5m bars · 474 days (122577 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.3% | 44.4 | 846 |
| london | 20.8% | 41.9 | 875 |
| overlap | 29.7% | 64.4 | 1651 |
| ny | 21.4% | 41.2 | 1030 |
| late | 21.1% | 36.1 | 429 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1214 trades · win 39% · PF 0.85 · expectancy -4.18 ticks (-0.09R) · PnL $-11523 · maxDD -48.7%
- **OOS**: 679 trades · win 42% · PF 0.96 · expectancy -3.30 ticks (-0.01R) · PnL $-1914 · maxDD -17.6%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1523 trades · win 54% · PF 0.83 · expectancy -3.28 ticks (-0.08R) · PnL $-12813 · maxDD -56.4%
- **OOS**: 905 trades · win 53% · PF 0.88 · expectancy -5.85 ticks (-0.07R) · PnL $-5559 · maxDD -24.5%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 941 trades · win 36% · PF 0.94 · expectancy -1.45 ticks (-0.05R) · PnL $-4167 · maxDD -31.0%
- **OOS**: 711 trades · win 33% · PF 0.85 · expectancy -6.46 ticks (-0.09R) · PnL $-7605 · maxDD -33.2%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 282 trades · win 17% · PF 1.42 · expectancy 9.27 ticks (0.36R) · PnL $12345 · maxDD -16.6%
- **OOS**: 167 trades · win 13% · PF 0.82 · expectancy -8.95 ticks (-0.16R) · PnL $-2875 · maxDD -18.7%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.26 | -3.16 | -3.88 | -4.63 | -5.97 |
| vwap_reversion | -1.26 | -3.30 | -4.12 | -4.95 | -6.24 |
| momentum_burst | -0.81 | -2.25 | -2.81 | -3.47 | -4.69 |
| session_drift | -6.74 | -7.82 | -8.36 | -8.91 | -11.45 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._