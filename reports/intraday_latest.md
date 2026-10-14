# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-14T10:39:45+00:00 · 5m bars · 481 days (124218 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.2% | 44.3 | 840 |
| london | 20.7% | 41.8 | 870 |
| overlap | 29.6% | 64.2 | 1641 |
| ny | 21.3% | 41.1 | 1022 |
| late | 20.9% | 35.9 | 425 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1228 trades · win 39% · PF 0.86 · expectancy -4.16 ticks (-0.09R) · PnL $-11559 · maxDD -48.7%
- **OOS**: 686 trades · win 42% · PF 0.97 · expectancy -2.36 ticks (-0.01R) · PnL $-1467 · maxDD -16.5%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1542 trades · win 54% · PF 0.83 · expectancy -3.82 ticks (-0.08R) · PnL $-13707 · maxDD -56.4%
- **OOS**: 914 trades · win 54% · PF 0.89 · expectancy -4.85 ticks (-0.07R) · PnL $-5025 · maxDD -25.1%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 951 trades · win 36% · PF 0.94 · expectancy -1.41 ticks (-0.04R) · PnL $-4144 · maxDD -31.0%
- **OOS**: 725 trades · win 34% · PF 0.87 · expectancy -5.53 ticks (-0.07R) · PnL $-6861 · maxDD -34.4%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 286 trades · win 17% · PF 1.38 · expectancy 6.61 ticks (0.34R) · PnL $11623 · maxDD -16.6%
- **OOS**: 169 trades · win 14% · PF 0.87 · expectancy -4.55 ticks (-0.12R) · PnL $-1979 · maxDD -18.2%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.36 | -3.26 | -3.95 | -4.64 | -6.01 |
| vwap_reversion | -1.36 | -3.35 | -4.17 | -4.97 | -6.28 |
| momentum_burst | -1.09 | -2.52 | -3.09 | -3.74 | -4.99 |
| session_drift | -7.57 | -8.65 | -9.19 | -9.73 | -12.26 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._