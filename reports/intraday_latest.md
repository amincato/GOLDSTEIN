# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-18T06:04:59+00:00 · 5m bars · 434 days (113142 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.7% | 44.1 | 882 |
| london | 21.1% | 41.7 | 908 |
| overlap | 29.6% | 63.2 | 1675 |
| ny | 21.6% | 41.0 | 1066 |
| late | 21.6% | 36.6 | 448 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1095 trades · win 40% · PF 0.86 · expectancy -2.83 ticks (-0.09R) · PnL $-9444 · maxDD -48.7%
- **OOS**: 652 trades · win 42% · PF 0.97 · expectancy -1.96 ticks (-0.01R) · PnL $-1384 · maxDD -11.0%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1388 trades · win 54% · PF 0.80 · expectancy -4.44 ticks (-0.09R) · PnL $-14064 · maxDD -55.5%
- **OOS**: 867 trades · win 56% · PF 0.96 · expectancy -2.11 ticks (-0.02R) · PnL $-1760 · maxDD -14.0%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 697 trades · win 36% · PF 0.94 · expectancy -2.79 ticks (-0.05R) · PnL $-2940 · maxDD -15.3%
- **OOS**: 512 trades · win 34% · PF 0.85 · expectancy -9.34 ticks (-0.08R) · PnL $-5500 · maxDD -28.2%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 258 trades · win 16% · PF 1.29 · expectancy -1.23 ticks (0.24R) · PnL $7926 · maxDD -16.6%
- **OOS**: 158 trades · win 17% · PF 1.19 · expectancy 11.94 ticks (0.17R) · PnL $2968 · maxDD -16.2%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.56 | -2.36 | -3.00 | -3.67 | -5.04 |
| vwap_reversion | -0.82 | -2.87 | -3.67 | -4.47 | -5.79 |
| momentum_burst | -0.45 | -1.94 | -2.52 | -3.19 | -4.44 |
| session_drift | -8.60 | -9.69 | -10.23 | -10.77 | -13.44 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._