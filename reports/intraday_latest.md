# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-09T10:09:52+00:00 · 5m bars · 451 days (117294 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.4 | 866 |
| london | 21.0% | 41.8 | 892 |
| overlap | 29.8% | 64.0 | 1671 |
| ny | 21.5% | 41.1 | 1049 |
| late | 21.4% | 36.5 | 439 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1146 trades · win 40% · PF 0.88 · expectancy -2.32 ticks (-0.08R) · PnL $-8801 · maxDD -48.7%
- **OOS**: 674 trades · win 42% · PF 0.94 · expectancy -4.11 ticks (-0.02R) · PnL $-2996 · maxDD -13.0%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1446 trades · win 54% · PF 0.81 · expectancy -4.01 ticks (-0.09R) · PnL $-13607 · maxDD -56.4%
- **OOS**: 884 trades · win 55% · PF 0.93 · expectancy -3.85 ticks (-0.04R) · PnL $-3318 · maxDD -19.3%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 725 trades · win 36% · PF 0.96 · expectancy -2.16 ticks (-0.04R) · PnL $-2032 · maxDD -15.3%
- **OOS**: 543 trades · win 32% · PF 0.78 · expectancy -12.47 ticks (-0.14R) · PnL $-8728 · maxDD -34.0%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 268 trades · win 17% · PF 1.36 · expectancy 3.08 ticks (0.33R) · PnL $10042 · maxDD -16.6%
- **OOS**: 162 trades · win 15% · PF 1.05 · expectancy 3.91 ticks (0.01R) · PnL $861 · maxDD -17.2%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.88 | -2.71 | -3.34 | -4.10 | -5.46 |
| vwap_reversion | -1.11 | -3.16 | -4.00 | -4.80 | -6.11 |
| momentum_burst | -1.20 | -2.67 | -3.24 | -3.90 | -5.14 |
| session_drift | -5.04 | -6.13 | -6.67 | -7.21 | -9.83 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._