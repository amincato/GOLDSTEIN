# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-03T10:08:13+00:00 · 5m bars · 448 days (116534 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.4 | 869 |
| london | 21.0% | 41.8 | 896 |
| overlap | 29.7% | 63.8 | 1671 |
| ny | 21.5% | 41.1 | 1053 |
| late | 21.4% | 36.6 | 441 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1134 trades · win 40% · PF 0.87 · expectancy -2.35 ticks (-0.08R) · PnL $-9031 · maxDD -48.7%
- **OOS**: 674 trades · win 42% · PF 0.95 · expectancy -3.19 ticks (-0.01R) · PnL $-2159 · maxDD -11.3%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1434 trades · win 54% · PF 0.81 · expectancy -4.18 ticks (-0.09R) · PnL $-13732 · maxDD -56.4%
- **OOS**: 879 trades · win 55% · PF 0.93 · expectancy -3.72 ticks (-0.04R) · PnL $-3210 · maxDD -18.3%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 717 trades · win 36% · PF 0.95 · expectancy -2.40 ticks (-0.04R) · PnL $-2539 · maxDD -15.3%
- **OOS**: 540 trades · win 32% · PF 0.81 · expectancy -11.18 ticks (-0.12R) · PnL $-7395 · maxDD -31.0%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 266 trades · win 17% · PF 1.34 · expectancy 1.93 ticks (0.31R) · PnL $9331 · maxDD -16.6%
- **OOS**: 162 trades · win 15% · PF 1.06 · expectancy 3.69 ticks (0.01R) · PnL $877 · maxDD -17.3%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.58 | -2.42 | -3.05 | -3.81 | -5.17 |
| vwap_reversion | -1.10 | -3.20 | -3.99 | -4.79 | -6.10 |
| momentum_burst | -1.04 | -2.51 | -3.08 | -3.75 | -4.99 |
| session_drift | -5.97 | -7.06 | -7.60 | -8.14 | -10.77 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._