# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-19T14:43:30+00:00 · 5m bars · 512 days (131445 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.1% | 44.6 | 819 |
| london | 20.4% | 41.5 | 847 |
| overlap | 29.4% | 64.1 | 1617 |
| ny | 21.0% | 40.8 | 1001 |
| late | 20.5% | 35.6 | 414 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1319 trades · win 40% · PF 0.88 · expectancy -2.67 ticks (-0.08R) · PnL $-10189 · maxDD -48.7%
- **OOS**: 708 trades · win 41% · PF 0.91 · expectancy -6.61 ticks (-0.04R) · PnL $-4052 · maxDD -21.5%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1654 trades · win 55% · PF 0.85 · expectancy -2.78 ticks (-0.07R) · PnL $-12510 · maxDD -56.4%
- **OOS**: 949 trades · win 52% · PF 0.81 · expectancy -8.03 ticks (-0.10R) · PnL $-8840 · maxDD -36.5%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1035 trades · win 36% · PF 0.93 · expectancy -2.29 ticks (-0.05R) · PnL $-5048 · maxDD -31.0%
- **OOS**: 766 trades · win 33% · PF 0.88 · expectancy -4.71 ticks (-0.08R) · PnL $-6424 · maxDD -30.9%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 305 trades · win 17% · PF 1.38 · expectancy 7.46 ticks (0.32R) · PnL $12006 · maxDD -16.6%
- **OOS**: 176 trades · win 14% · PF 0.95 · expectancy -1.97 ticks (-0.01R) · PnL $-881 · maxDD -16.6%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.00 | -3.09 | -3.80 | -4.47 | -5.91 |
| vwap_reversion | -1.55 | -3.52 | -4.32 | -5.06 | -6.39 |
| momentum_burst | -0.88 | -2.28 | -2.84 | -3.68 | -5.06 |
| session_drift | -8.49 | -9.57 | -10.11 | -10.65 | -13.09 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._