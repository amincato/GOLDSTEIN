# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-11T10:02:37+00:00 · 5m bars · 453 days (117847 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.5% | 44.4 | 864 |
| london | 21.0% | 41.8 | 890 |
| overlap | 29.9% | 64.1 | 1671 |
| ny | 21.5% | 41.1 | 1047 |
| late | 21.3% | 36.5 | 438 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1152 trades · win 40% · PF 0.88 · expectancy -2.40 ticks (-0.08R) · PnL $-8907 · maxDD -48.7%
- **OOS**: 678 trades · win 41% · PF 0.92 · expectancy -4.88 ticks (-0.02R) · PnL $-3597 · maxDD -15.8%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1452 trades · win 54% · PF 0.81 · expectancy -3.79 ticks (-0.09R) · PnL $-13338 · maxDD -56.4%
- **OOS**: 890 trades · win 54% · PF 0.92 · expectancy -4.13 ticks (-0.05R) · PnL $-3579 · maxDD -19.5%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 728 trades · win 36% · PF 0.96 · expectancy -2.36 ticks (-0.04R) · PnL $-2382 · maxDD -15.3%
- **OOS**: 553 trades · win 32% · PF 0.80 · expectancy -11.38 ticks (-0.12R) · PnL $-7848 · maxDD -34.1%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 269 trades · win 17% · PF 1.36 · expectancy 2.88 ticks (0.32R) · PnL $9940 · maxDD -16.6%
- **OOS**: 163 trades · win 15% · PF 1.05 · expectancy 3.61 ticks (0.00R) · PnL $769 · maxDD -17.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.05 | -2.88 | -3.51 | -4.27 | -5.62 |
| vwap_reversion | -1.27 | -3.36 | -4.15 | -4.94 | -6.25 |
| momentum_burst | -0.91 | -2.37 | -2.94 | -3.60 | -4.84 |
| session_drift | -5.37 | -6.46 | -7.00 | -7.54 | -10.15 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._