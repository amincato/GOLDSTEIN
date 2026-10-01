# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-01T11:51:19+00:00 · 5m bars · 470 days (121742 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.3% | 44.4 | 849 |
| london | 20.8% | 41.9 | 878 |
| overlap | 29.7% | 64.3 | 1654 |
| ny | 21.5% | 41.3 | 1034 |
| late | 21.2% | 36.3 | 431 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1206 trades · win 39% · PF 0.86 · expectancy -3.75 ticks (-0.09R) · PnL $-10967 · maxDD -48.7%
- **OOS**: 672 trades · win 42% · PF 0.95 · expectancy -3.63 ticks (-0.01R) · PnL $-2252 · maxDD -17.2%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1513 trades · win 54% · PF 0.84 · expectancy -3.03 ticks (-0.08R) · PnL $-12408 · maxDD -56.4%
- **OOS**: 902 trades · win 54% · PF 0.88 · expectancy -5.77 ticks (-0.07R) · PnL $-5342 · maxDD -22.4%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 934 trades · win 36% · PF 0.94 · expectancy -1.31 ticks (-0.05R) · PnL $-4027 · maxDD -31.0%
- **OOS**: 705 trades · win 33% · PF 0.85 · expectancy -6.42 ticks (-0.08R) · PnL $-7274 · maxDD -31.9%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 280 trades · win 17% · PF 1.34 · expectancy 0.94 ticks (0.33R) · PnL $9995 · maxDD -16.6%
- **OOS**: 166 trades · win 14% · PF 0.91 · expectancy -1.63 ticks (-0.11R) · PnL $-1392 · maxDD -17.9%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.17 | -3.08 | -3.80 | -4.55 | -5.89 |
| vwap_reversion | -1.12 | -3.14 | -3.96 | -4.79 | -6.09 |
| momentum_burst | -0.79 | -2.23 | -2.80 | -3.46 | -4.68 |
| session_drift | -6.43 | -7.51 | -8.05 | -8.60 | -11.16 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._