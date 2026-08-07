# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-07T06:55:34+00:00 · 5m bars · 425 days (111239 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.8% | 44.1 | 890 |
| london | 21.3% | 41.8 | 917 |
| overlap | 29.7% | 63.1 | 1685 |
| ny | 21.8% | 41.1 | 1077 |
| late | 21.8% | 36.7 | 454 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1074 trades · win 39% · PF 0.86 · expectancy -3.44 ticks (-0.10R) · PnL $-9922 · maxDD -48.7%
- **OOS**: 650 trades · win 42% · PF 0.98 · expectancy -0.96 ticks (0.00R) · PnL $-780 · maxDD -10.8%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1365 trades · win 54% · PF 0.81 · expectancy -3.72 ticks (-0.09R) · PnL $-12859 · maxDD -53.9%
- **OOS**: 853 trades · win 56% · PF 0.95 · expectancy -2.73 ticks (-0.03R) · PnL $-2349 · maxDD -13.7%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 690 trades · win 36% · PF 0.95 · expectancy -2.81 ticks (-0.05R) · PnL $-2787 · maxDD -15.3%
- **OOS**: 491 trades · win 34% · PF 0.86 · expectancy -9.24 ticks (-0.07R) · PnL $-4740 · maxDD -28.3%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 254 trades · win 16% · PF 1.30 · expectancy -0.98 ticks (0.25R) · PnL $8058 · maxDD -16.6%
- **OOS**: 155 trades · win 17% · PF 1.15 · expectancy 9.78 ticks (0.12R) · PnL $2215 · maxDD -16.2%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.50 | -2.31 | -2.95 | -3.63 | -5.00 |
| vwap_reversion | -0.98 | -3.01 | -3.81 | -4.50 | -5.82 |
| momentum_burst | -0.37 | -1.87 | -2.45 | -3.13 | -4.22 |
| session_drift | -8.46 | -9.54 | -10.09 | -10.63 | -13.32 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._