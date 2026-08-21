# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-21T06:07:04+00:00 · 5m bars · 437 days (113997 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.1 | 878 |
| london | 21.1% | 41.7 | 905 |
| overlap | 29.6% | 63.4 | 1677 |
| ny | 21.6% | 41.0 | 1062 |
| late | 21.5% | 36.6 | 447 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1107 trades · win 40% · PF 0.87 · expectancy -2.56 ticks (-0.09R) · PnL $-9333 · maxDD -48.7%
- **OOS**: 653 trades · win 42% · PF 0.97 · expectancy -2.11 ticks (-0.01R) · PnL $-1306 · maxDD -11.2%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1398 trades · win 54% · PF 0.79 · expectancy -4.57 ticks (-0.10R) · PnL $-14260 · maxDD -56.3%
- **OOS**: 872 trades · win 56% · PF 0.97 · expectancy -1.82 ticks (-0.02R) · PnL $-1414 · maxDD -14.1%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 702 trades · win 36% · PF 0.94 · expectancy -2.84 ticks (-0.05R) · PnL $-3013 · maxDD -15.3%
- **OOS**: 521 trades · win 33% · PF 0.84 · expectancy -9.62 ticks (-0.09R) · PnL $-5890 · maxDD -28.1%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 260 trades · win 17% · PF 1.34 · expectancy 1.61 ticks (0.30R) · PnL $9138 · maxDD -16.6%
- **OOS**: 159 trades · win 17% · PF 1.22 · expectancy 13.10 ticks (0.17R) · PnL $3361 · maxDD -16.6%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.16 | -2.00 | -2.64 | -3.31 | -4.68 |
| vwap_reversion | -0.82 | -2.90 | -3.69 | -4.40 | -5.72 |
| momentum_burst | -0.55 | -2.04 | -2.61 | -3.28 | -4.71 |
| session_drift | -5.69 | -6.78 | -7.32 | -7.86 | -10.52 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._