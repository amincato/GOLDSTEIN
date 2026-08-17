# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-17T06:22:22+00:00 · 5m bars · 433 days (112893 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.7% | 44.1 | 883 |
| london | 21.1% | 41.7 | 910 |
| overlap | 29.6% | 63.3 | 1677 |
| ny | 21.6% | 41.0 | 1067 |
| late | 21.6% | 36.7 | 449 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1095 trades · win 40% · PF 0.86 · expectancy -2.83 ticks (-0.09R) · PnL $-9444 · maxDD -48.7%
- **OOS**: 648 trades · win 42% · PF 0.97 · expectancy -2.09 ticks (-0.01R) · PnL $-1462 · maxDD -11.0%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1388 trades · win 54% · PF 0.80 · expectancy -4.44 ticks (-0.09R) · PnL $-14064 · maxDD -55.5%
- **OOS**: 861 trades · win 56% · PF 0.96 · expectancy -2.10 ticks (-0.02R) · PnL $-1780 · maxDD -14.0%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 697 trades · win 36% · PF 0.94 · expectancy -2.79 ticks (-0.05R) · PnL $-2940 · maxDD -15.3%
- **OOS**: 506 trades · win 33% · PF 0.84 · expectancy -9.76 ticks (-0.09R) · PnL $-5680 · maxDD -28.2%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 258 trades · win 16% · PF 1.29 · expectancy -1.23 ticks (0.24R) · PnL $7926 · maxDD -16.6%
- **OOS**: 158 trades · win 18% · PF 1.21 · expectancy 13.37 ticks (0.19R) · PnL $3201 · maxDD -16.0%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.55 | -2.35 | -2.99 | -3.67 | -5.03 |
| vwap_reversion | -0.85 | -2.91 | -3.70 | -4.51 | -5.83 |
| momentum_burst | -0.61 | -2.10 | -2.67 | -3.35 | -4.60 |
| session_drift | -8.49 | -9.57 | -10.11 | -10.66 | -13.33 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._