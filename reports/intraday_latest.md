# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-11T06:39:24+00:00 · 5m bars · 428 days (111764 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.8% | 44.1 | 888 |
| london | 21.2% | 41.8 | 915 |
| overlap | 29.7% | 63.2 | 1683 |
| ny | 21.7% | 41.1 | 1074 |
| late | 21.7% | 36.7 | 452 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1080 trades · win 39% · PF 0.86 · expectancy -3.20 ticks (-0.09R) · PnL $-9742 · maxDD -48.7%
- **OOS**: 650 trades · win 42% · PF 0.98 · expectancy -1.14 ticks (0.00R) · PnL $-846 · maxDD -10.9%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1370 trades · win 54% · PF 0.80 · expectancy -3.89 ticks (-0.09R) · PnL $-13220 · maxDD -53.9%
- **OOS**: 860 trades · win 56% · PF 0.95 · expectancy -2.80 ticks (-0.03R) · PnL $-2332 · maxDD -13.5%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 691 trades · win 36% · PF 0.94 · expectancy -2.87 ticks (-0.05R) · PnL $-2917 · maxDD -15.3%
- **OOS**: 498 trades · win 34% · PF 0.86 · expectancy -9.23 ticks (-0.07R) · PnL $-4817 · maxDD -28.2%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 255 trades · win 16% · PF 1.31 · expectancy -0.35 ticks (0.26R) · PnL $8218 · maxDD -16.6%
- **OOS**: 156 trades · win 17% · PF 1.14 · expectancy 9.43 ticks (0.12R) · PnL $2126 · maxDD -16.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.43 | -2.24 | -2.88 | -3.56 | -4.92 |
| vwap_reversion | -0.64 | -2.70 | -3.50 | -4.29 | -5.61 |
| momentum_burst | -0.63 | -2.12 | -2.70 | -3.37 | -4.47 |
| session_drift | -8.73 | -9.81 | -10.35 | -10.90 | -13.58 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._