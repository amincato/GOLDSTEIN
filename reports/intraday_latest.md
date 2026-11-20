# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-20T14:24:49+00:00 · 5m bars · 513 days (131719 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.1% | 44.7 | 820 |
| london | 20.4% | 41.6 | 847 |
| overlap | 29.4% | 64.1 | 1617 |
| ny | 21.0% | 40.8 | 1001 |
| late | 20.7% | 35.7 | 415 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1319 trades · win 40% · PF 0.88 · expectancy -2.67 ticks (-0.08R) · PnL $-10189 · maxDD -48.7%
- **OOS**: 712 trades · win 41% · PF 0.91 · expectancy -6.29 ticks (-0.04R) · PnL $-3849 · maxDD -21.4%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1654 trades · win 55% · PF 0.85 · expectancy -2.78 ticks (-0.07R) · PnL $-12510 · maxDD -56.4%
- **OOS**: 952 trades · win 52% · PF 0.81 · expectancy -8.35 ticks (-0.11R) · PnL $-9171 · maxDD -37.8%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1035 trades · win 36% · PF 0.93 · expectancy -2.29 ticks (-0.05R) · PnL $-5048 · maxDD -31.0%
- **OOS**: 771 trades · win 33% · PF 0.88 · expectancy -4.68 ticks (-0.08R) · PnL $-6323 · maxDD -30.9%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 305 trades · win 17% · PF 1.38 · expectancy 7.46 ticks (0.32R) · PnL $12006 · maxDD -16.6%
- **OOS**: 177 trades · win 14% · PF 0.94 · expectancy -2.76 ticks (-0.02R) · PnL $-1021 · maxDD -16.6%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.02 | -3.10 | -3.81 | -4.48 | -5.92 |
| vwap_reversion | -1.65 | -3.62 | -4.42 | -5.16 | -6.49 |
| momentum_burst | -0.93 | -2.33 | -2.89 | -3.73 | -5.11 |
| session_drift | -8.64 | -9.72 | -10.26 | -10.80 | -13.24 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._