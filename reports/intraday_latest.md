# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-08T12:16:45+00:00 · 5m bars · 476 days (123131 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.2% | 44.4 | 844 |
| london | 20.7% | 41.9 | 873 |
| overlap | 29.7% | 64.4 | 1648 |
| ny | 21.4% | 41.2 | 1027 |
| late | 21.0% | 36.1 | 427 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1214 trades · win 39% · PF 0.85 · expectancy -4.18 ticks (-0.09R) · PnL $-11523 · maxDD -48.7%
- **OOS**: 686 trades · win 42% · PF 0.96 · expectancy -3.30 ticks (-0.01R) · PnL $-1730 · maxDD -17.6%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1529 trades · win 54% · PF 0.83 · expectancy -3.28 ticks (-0.08R) · PnL $-12830 · maxDD -56.4%
- **OOS**: 908 trades · win 53% · PF 0.87 · expectancy -5.91 ticks (-0.07R) · PnL $-5803 · maxDD -25.5%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 942 trades · win 36% · PF 0.94 · expectancy -1.65 ticks (-0.05R) · PnL $-4358 · maxDD -31.0%
- **OOS**: 719 trades · win 33% · PF 0.85 · expectancy -5.92 ticks (-0.08R) · PnL $-7517 · maxDD -33.9%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 283 trades · win 17% · PF 1.41 · expectancy 8.61 ticks (0.36R) · PnL $12168 · maxDD -16.6%
- **OOS**: 168 trades · win 14% · PF 0.85 · expectancy -6.82 ticks (-0.14R) · PnL $-2384 · maxDD -18.5%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.24 | -3.13 | -3.85 | -4.60 | -6.02 |
| vwap_reversion | -1.28 | -3.31 | -4.13 | -4.96 | -6.26 |
| momentum_burst | -0.91 | -2.34 | -2.91 | -3.56 | -4.78 |
| session_drift | -6.93 | -8.01 | -8.55 | -9.09 | -11.63 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._