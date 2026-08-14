# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-14T07:00:58+00:00 · 5m bars · 431 days (112625 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.7% | 44.1 | 884 |
| london | 21.2% | 41.8 | 911 |
| overlap | 29.7% | 63.3 | 1679 |
| ny | 21.7% | 41.1 | 1069 |
| late | 21.7% | 36.7 | 450 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1089 trades · win 39% · PF 0.86 · expectancy -2.89 ticks (-0.09R) · PnL $-9484 · maxDD -48.7%
- **OOS**: 650 trades · win 42% · PF 0.97 · expectancy -2.08 ticks (-0.01R) · PnL $-1395 · maxDD -11.0%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1382 trades · win 54% · PF 0.80 · expectancy -4.46 ticks (-0.10R) · PnL $-14056 · maxDD -55.5%
- **OOS**: 862 trades · win 56% · PF 0.96 · expectancy -1.98 ticks (-0.02R) · PnL $-1661 · maxDD -13.5%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 695 trades · win 36% · PF 0.95 · expectancy -2.59 ticks (-0.05R) · PnL $-2795 · maxDD -15.3%
- **OOS**: 503 trades · win 33% · PF 0.84 · expectancy -10.05 ticks (-0.09R) · PnL $-5746 · maxDD -28.3%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 257 trades · win 16% · PF 1.30 · expectancy -0.91 ticks (0.25R) · PnL $8010 · maxDD -16.6%
- **OOS**: 157 trades · win 17% · PF 1.18 · expectancy 11.85 ticks (0.16R) · PnL $2696 · maxDD -16.0%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.60 | -2.40 | -3.04 | -3.72 | -5.08 |
| vwap_reversion | -0.82 | -2.87 | -3.67 | -4.46 | -5.78 |
| momentum_burst | -0.65 | -2.15 | -2.72 | -3.39 | -4.65 |
| session_drift | -9.07 | -10.16 | -10.70 | -11.24 | -13.92 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._