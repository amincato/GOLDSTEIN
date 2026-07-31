# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-07-31T00:12:24+00:00 · 5m bars · 158 days (39883 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 32.0% | 68.4 | 938 |
| london | 28.1% | 62.9 | 917 |
| overlap | 37.6% | 95.1 | 1790 |
| ny | 29.5% | 64.5 | 1251 |
| late | 28.8% | 58.3 | 542 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 405 trades · win 37% · PF 1.06 · expectancy 1.30 ticks (0.03R) · PnL $1549 · maxDD -10.4%
- **OOS**: 220 trades · win 34% · PF 0.89 · expectancy -6.82 ticks (-0.07R) · PnL $-1522 · maxDD -8.9%

### vwap_reversion
- params: `{'z_entry': 2.2, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 509 trades · win 57% · PF 1.07 · expectancy 2.87 ticks (-0.00R) · PnL $1888 · maxDD -6.9%
- **OOS**: 267 trades · win 51% · PF 0.77 · expectancy -10.55 ticks (-0.11R) · PnL $-3015 · maxDD -13.3%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 0.8, 'target_atr': 1.6}`
- **IS**: 324 trades · win 37% · PF 1.04 · expectancy 3.47 ticks (0.04R) · PnL $840 · maxDD -6.2%
- **OOS**: 249 trades · win 39% · PF 1.11 · expectancy 2.57 ticks (0.07R) · PnL $1775 · maxDD -8.3%

### session_drift
- params: `{'entry_hour': 16, 'direction': -1}`
- **IS**: 94 trades · win 32% · PF 1.01 · expectancy 2.17 ticks (0.13R) · PnL $154 · maxDD -13.2%
- **OOS**: 52 trades · win 50% · PF 1.92 · expectancy 45.79 ticks (0.40R) · PnL $2381 · maxDD -2.3%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | 0.66 | -0.84 | -1.62 | -1.56 | -2.67 |
| vwap_reversion | -0.19 | -2.28 | -3.26 | -4.04 | -5.33 |
| momentum_burst | -0.93 | -2.24 | -2.75 | -3.35 | -4.67 |
| session_drift | -31.03 | -32.10 | -32.63 | -33.17 | -34.23 |

## Verdict
- OOS survivors at realistic costs: **momentum_burst, session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._