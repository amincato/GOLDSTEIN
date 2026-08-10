# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-10T06:59:28+00:00 · 5m bars · 427 days (111516 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.8% | 44.1 | 889 |
| london | 21.3% | 41.8 | 916 |
| overlap | 29.7% | 63.2 | 1685 |
| ny | 21.7% | 41.1 | 1075 |
| late | 21.7% | 36.7 | 453 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1080 trades · win 39% · PF 0.86 · expectancy -3.20 ticks (-0.09R) · PnL $-9742 · maxDD -48.7%
- **OOS**: 647 trades · win 42% · PF 0.98 · expectancy -1.40 ticks (-0.00R) · PnL $-1013 · maxDD -10.9%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1370 trades · win 54% · PF 0.80 · expectancy -3.89 ticks (-0.09R) · PnL $-13220 · maxDD -53.9%
- **OOS**: 854 trades · win 56% · PF 0.95 · expectancy -2.57 ticks (-0.02R) · PnL $-2094 · maxDD -13.5%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 691 trades · win 36% · PF 0.94 · expectancy -2.87 ticks (-0.05R) · PnL $-2917 · maxDD -15.3%
- **OOS**: 495 trades · win 34% · PF 0.87 · expectancy -8.98 ticks (-0.07R) · PnL $-4511 · maxDD -28.2%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 255 trades · win 16% · PF 1.31 · expectancy -0.35 ticks (0.26R) · PnL $8218 · maxDD -16.6%
- **OOS**: 155 trades · win 17% · PF 1.15 · expectancy 9.79 ticks (0.12R) · PnL $2219 · maxDD -16.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.50 | -2.31 | -2.95 | -3.63 | -5.00 |
| vwap_reversion | -0.67 | -2.73 | -3.53 | -4.32 | -5.65 |
| momentum_burst | -0.55 | -2.04 | -2.62 | -3.30 | -4.39 |
| session_drift | -8.61 | -9.70 | -10.24 | -10.78 | -13.47 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._