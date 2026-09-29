# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-29T11:37:05+00:00 · 5m bars · 468 days (121185 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.3% | 44.5 | 852 |
| london | 20.8% | 41.9 | 880 |
| overlap | 29.7% | 64.3 | 1657 |
| ny | 21.5% | 41.3 | 1036 |
| late | 21.2% | 36.3 | 433 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1196 trades · win 39% · PF 0.85 · expectancy -3.86 ticks (-0.09R) · PnL $-11072 · maxDD -48.7%
- **OOS**: 675 trades · win 42% · PF 0.96 · expectancy -2.94 ticks (-0.01R) · PnL $-1796 · maxDD -16.2%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1501 trades · win 54% · PF 0.83 · expectancy -3.27 ticks (-0.08R) · PnL $-12730 · maxDD -56.4%
- **OOS**: 902 trades · win 54% · PF 0.89 · expectancy -5.30 ticks (-0.07R) · PnL $-4954 · maxDD -21.9%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 934 trades · win 36% · PF 0.94 · expectancy -1.31 ticks (-0.05R) · PnL $-4027 · maxDD -31.0%
- **OOS**: 696 trades · win 34% · PF 0.87 · expectancy -6.06 ticks (-0.07R) · PnL $-6605 · maxDD -31.9%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 278 trades · win 17% · PF 1.37 · expectancy 3.47 ticks (0.34R) · PnL $10697 · maxDD -16.6%
- **OOS**: 166 trades · win 14% · PF 0.97 · expectancy 2.72 ticks (-0.08R) · PnL $-494 · maxDD -17.5%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.99 | -2.90 | -3.62 | -4.37 | -5.72 |
| vwap_reversion | -1.19 | -3.26 | -4.04 | -4.85 | -6.16 |
| momentum_burst | -0.75 | -2.19 | -2.76 | -3.41 | -4.64 |
| session_drift | -6.44 | -7.52 | -8.07 | -8.61 | -11.17 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._