# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-19T06:05:47+00:00 · 5m bars · 435 days (113430 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.1 | 880 |
| london | 21.1% | 41.7 | 907 |
| overlap | 29.6% | 63.3 | 1674 |
| ny | 21.6% | 41.0 | 1064 |
| late | 21.6% | 36.6 | 448 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1101 trades · win 40% · PF 0.87 · expectancy -2.66 ticks (-0.09R) · PnL $-9373 · maxDD -48.7%
- **OOS**: 649 trades · win 42% · PF 0.95 · expectancy -2.98 ticks (-0.02R) · PnL $-2010 · maxDD -11.2%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1393 trades · win 54% · PF 0.80 · expectancy -4.51 ticks (-0.10R) · PnL $-14154 · maxDD -55.9%
- **OOS**: 867 trades · win 56% · PF 0.96 · expectancy -1.97 ticks (-0.02R) · PnL $-1666 · maxDD -13.9%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 701 trades · win 36% · PF 0.94 · expectancy -2.77 ticks (-0.05R) · PnL $-2915 · maxDD -15.3%
- **OOS**: 510 trades · win 33% · PF 0.83 · expectancy -9.88 ticks (-0.09R) · PnL $-6082 · maxDD -28.2%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 259 trades · win 16% · PF 1.30 · expectancy -0.22 ticks (0.26R) · PnL $8188 · maxDD -16.6%
- **OOS**: 158 trades · win 17% · PF 1.23 · expectancy 13.47 ticks (0.18R) · PnL $3451 · maxDD -16.7%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.41 | -2.25 | -2.89 | -3.57 | -4.93 |
| vwap_reversion | -0.86 | -2.91 | -3.70 | -4.41 | -5.73 |
| momentum_burst | -0.47 | -1.96 | -2.54 | -3.21 | -4.65 |
| session_drift | -8.70 | -9.79 | -10.33 | -10.87 | -13.54 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._