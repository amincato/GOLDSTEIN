# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-27T16:51:20+00:00 · 5m bars · 442 days (115227 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.3 | 874 |
| london | 21.1% | 41.8 | 901 |
| overlap | 29.6% | 63.6 | 1671 |
| ny | 21.5% | 41.1 | 1057 |
| late | 21.5% | 36.6 | 445 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1119 trades · win 40% · PF 0.87 · expectancy -2.59 ticks (-0.09R) · PnL $-9520 · maxDD -48.7%
- **OOS**: 666 trades · win 42% · PF 0.97 · expectancy -2.37 ticks (-0.00R) · PnL $-1293 · maxDD -11.1%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1416 trades · win 54% · PF 0.80 · expectancy -4.39 ticks (-0.09R) · PnL $-14151 · maxDD -56.4%
- **OOS**: 880 trades · win 55% · PF 0.95 · expectancy -2.89 ticks (-0.03R) · PnL $-2265 · maxDD -16.5%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 706 trades · win 36% · PF 0.94 · expectancy -2.65 ticks (-0.05R) · PnL $-2934 · maxDD -15.3%
- **OOS**: 536 trades · win 33% · PF 0.83 · expectancy -10.24 ticks (-0.10R) · PnL $-6314 · maxDD -28.5%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 263 trades · win 16% · PF 1.32 · expectancy 1.02 ticks (0.28R) · PnL $8750 · maxDD -16.6%
- **OOS**: 160 trades · win 17% · PF 1.22 · expectancy 12.35 ticks (0.16R) · PnL $3306 · maxDD -16.4%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.26 | -2.24 | -2.88 | -3.55 | -4.91 |
| vwap_reversion | -0.94 | -3.01 | -3.80 | -4.50 | -5.81 |
| momentum_burst | -0.67 | -2.15 | -2.72 | -3.39 | -4.82 |
| session_drift | -6.53 | -7.61 | -8.15 | -8.70 | -11.34 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._