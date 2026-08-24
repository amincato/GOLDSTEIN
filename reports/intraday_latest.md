# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-24T06:26:40+00:00 · 5m bars · 439 days (114275 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.2 | 877 |
| london | 21.1% | 41.7 | 904 |
| overlap | 29.6% | 63.5 | 1676 |
| ny | 21.6% | 41.0 | 1061 |
| late | 21.5% | 36.6 | 446 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1110 trades · win 40% · PF 0.86 · expectancy -2.69 ticks (-0.09R) · PnL $-9643 · maxDD -48.7%
- **OOS**: 655 trades · win 42% · PF 0.98 · expectancy -1.97 ticks (-0.00R) · PnL $-1061 · maxDD -11.1%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1404 trades · win 54% · PF 0.79 · expectancy -4.55 ticks (-0.10R) · PnL $-14292 · maxDD -56.4%
- **OOS**: 871 trades · win 56% · PF 0.96 · expectancy -2.08 ticks (-0.02R) · PnL $-1597 · maxDD -14.1%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 704 trades · win 36% · PF 0.94 · expectancy -2.75 ticks (-0.05R) · PnL $-2938 · maxDD -15.3%
- **OOS**: 522 trades · win 33% · PF 0.83 · expectancy -10.11 ticks (-0.09R) · PnL $-6230 · maxDD -28.2%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 261 trades · win 16% · PF 1.33 · expectancy 1.35 ticks (0.29R) · PnL $9009 · maxDD -16.6%
- **OOS**: 159 trades · win 17% · PF 1.22 · expectancy 12.91 ticks (0.17R) · PnL $3417 · maxDD -16.6%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.21 | -2.05 | -2.69 | -3.36 | -4.72 |
| vwap_reversion | -0.89 | -2.97 | -3.76 | -4.47 | -5.78 |
| momentum_burst | -0.65 | -2.13 | -2.70 | -3.37 | -4.81 |
| session_drift | -5.87 | -6.95 | -7.49 | -8.04 | -10.69 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._