# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-18T14:36:35+00:00 · 5m bars · 511 days (131167 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.0% | 44.5 | 820 |
| london | 20.4% | 41.5 | 848 |
| overlap | 29.4% | 64.1 | 1619 |
| ny | 21.0% | 40.8 | 1001 |
| late | 20.5% | 35.6 | 414 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1316 trades · win 40% · PF 0.89 · expectancy -2.39 ticks (-0.08R) · PnL $-9808 · maxDD -48.7%
- **OOS**: 707 trades · win 40% · PF 0.90 · expectancy -7.15 ticks (-0.05R) · PnL $-4518 · maxDD -22.2%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1648 trades · win 55% · PF 0.85 · expectancy -2.88 ticks (-0.07R) · PnL $-12652 · maxDD -56.4%
- **OOS**: 947 trades · win 52% · PF 0.81 · expectancy -8.12 ticks (-0.11R) · PnL $-8870 · maxDD -37.0%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1032 trades · win 36% · PF 0.94 · expectancy -2.01 ticks (-0.04R) · PnL $-4744 · maxDD -31.0%
- **OOS**: 767 trades · win 33% · PF 0.87 · expectancy -5.24 ticks (-0.08R) · PnL $-7223 · maxDD -31.8%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 304 trades · win 17% · PF 1.38 · expectancy 7.75 ticks (0.32R) · PnL $12088 · maxDD -16.6%
- **OOS**: 176 trades · win 14% · PF 0.94 · expectancy -2.40 ticks (-0.02R) · PnL $-960 · maxDD -16.7%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.99 | -2.96 | -3.67 | -4.35 | -5.66 |
| vwap_reversion | -1.63 | -3.65 | -4.45 | -5.16 | -6.49 |
| momentum_burst | -1.17 | -2.58 | -3.14 | -3.90 | -5.12 |
| session_drift | -8.60 | -9.68 | -10.22 | -10.76 | -13.21 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._