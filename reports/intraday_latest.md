# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-05T08:10:40+00:00 · 5m bars · 423 days (110698 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.8% | 44.0 | 892 |
| london | 21.3% | 41.8 | 919 |
| overlap | 29.6% | 63.0 | 1687 |
| ny | 21.8% | 41.1 | 1080 |
| late | 21.8% | 36.7 | 455 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1068 trades · win 39% · PF 0.85 · expectancy -3.62 ticks (-0.10R) · PnL $-10306 · maxDD -48.7%
- **OOS**: 644 trades · win 43% · PF 0.99 · expectancy -0.83 ticks (0.01R) · PnL $-478 · maxDD -10.7%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1359 trades · win 54% · PF 0.81 · expectancy -3.71 ticks (-0.09R) · PnL $-12674 · maxDD -53.9%
- **OOS**: 848 trades · win 55% · PF 0.94 · expectancy -2.96 ticks (-0.03R) · PnL $-2589 · maxDD -13.8%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 687 trades · win 36% · PF 0.95 · expectancy -2.63 ticks (-0.05R) · PnL $-2438 · maxDD -15.3%
- **OOS**: 486 trades · win 33% · PF 0.84 · expectancy -10.01 ticks (-0.09R) · PnL $-5337 · maxDD -28.7%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 253 trades · win 16% · PF 1.30 · expectancy -0.71 ticks (0.26R) · PnL $8128 · maxDD -16.6%
- **OOS**: 154 trades · win 18% · PF 1.17 · expectancy 11.69 ticks (0.15R) · PnL $2546 · maxDD -16.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.46 | -2.27 | -2.92 | -3.60 | -4.97 |
| vwap_reversion | -1.01 | -3.04 | -3.84 | -4.53 | -5.86 |
| momentum_burst | -0.57 | -2.07 | -2.65 | -3.33 | -4.36 |
| session_drift | -9.41 | -10.50 | -11.04 | -11.58 | -14.28 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._