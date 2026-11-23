# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-23T16:31:58+00:00 · 5m bars · 515 days (132019 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.2% | 44.8 | 820 |
| london | 20.4% | 41.6 | 846 |
| overlap | 29.5% | 64.2 | 1618 |
| ny | 21.1% | 40.9 | 1001 |
| late | 21.2% | 35.8 | 415 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1328 trades · win 40% · PF 0.89 · expectancy -2.40 ticks (-0.08R) · PnL $-9850 · maxDD -48.7%
- **OOS**: 709 trades · win 41% · PF 0.91 · expectancy -6.83 ticks (-0.04R) · PnL $-4180 · maxDD -21.7%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1665 trades · win 55% · PF 0.85 · expectancy -2.97 ticks (-0.07R) · PnL $-12845 · maxDD -56.4%
- **OOS**: 944 trades · win 52% · PF 0.81 · expectancy -8.33 ticks (-0.11R) · PnL $-9082 · maxDD -38.3%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1045 trades · win 36% · PF 0.94 · expectancy -1.94 ticks (-0.04R) · PnL $-4813 · maxDD -31.0%
- **OOS**: 766 trades · win 33% · PF 0.87 · expectancy -5.60 ticks (-0.09R) · PnL $-7098 · maxDD -31.2%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 307 trades · win 17% · PF 1.37 · expectancy 6.75 ticks (0.31R) · PnL $11803 · maxDD -16.6%
- **OOS**: 176 trades · win 13% · PF 0.92 · expectancy -5.02 ticks (-0.04R) · PnL $-1417 · maxDD -16.4%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.96 | -3.13 | -3.83 | -4.50 | -5.94 |
| vwap_reversion | -1.72 | -3.69 | -4.49 | -5.23 | -6.56 |
| momentum_burst | -0.86 | -2.26 | -2.90 | -3.73 | -5.11 |
| session_drift | -8.72 | -9.80 | -10.34 | -10.88 | -13.32 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._