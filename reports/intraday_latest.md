# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-13T07:04:48+00:00 · 5m bars · 430 days (112348 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.7% | 44.1 | 885 |
| london | 21.2% | 41.8 | 912 |
| overlap | 29.7% | 63.2 | 1680 |
| ny | 21.7% | 41.1 | 1070 |
| late | 21.7% | 36.6 | 450 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1089 trades · win 39% · PF 0.86 · expectancy -2.89 ticks (-0.09R) · PnL $-9484 · maxDD -48.7%
- **OOS**: 646 trades · win 42% · PF 0.96 · expectancy -2.47 ticks (-0.01R) · PnL $-1638 · maxDD -11.0%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1382 trades · win 54% · PF 0.80 · expectancy -4.46 ticks (-0.10R) · PnL $-14056 · maxDD -55.5%
- **OOS**: 859 trades · win 56% · PF 0.97 · expectancy -1.73 ticks (-0.02R) · PnL $-1388 · maxDD -13.1%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 695 trades · win 36% · PF 0.95 · expectancy -2.59 ticks (-0.05R) · PnL $-2795 · maxDD -15.3%
- **OOS**: 500 trades · win 33% · PF 0.84 · expectancy -10.13 ticks (-0.09R) · PnL $-5634 · maxDD -28.3%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 257 trades · win 16% · PF 1.30 · expectancy -0.91 ticks (0.25R) · PnL $8010 · maxDD -16.6%
- **OOS**: 156 trades · win 17% · PF 1.19 · expectancy 12.32 ticks (0.16R) · PnL $2819 · maxDD -16.0%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.65 | -2.45 | -3.10 | -3.77 | -5.14 |
| vwap_reversion | -0.74 | -2.80 | -3.60 | -4.39 | -5.71 |
| momentum_burst | -0.78 | -2.28 | -2.85 | -3.53 | -4.62 |
| session_drift | -8.96 | -10.05 | -10.59 | -11.13 | -13.81 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._