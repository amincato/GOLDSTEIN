# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-12T07:00:33+00:00 · 5m bars · 429 days (112071 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.7% | 44.1 | 886 |
| london | 21.2% | 41.8 | 914 |
| overlap | 29.7% | 63.2 | 1681 |
| ny | 21.7% | 41.1 | 1072 |
| late | 21.7% | 36.7 | 451 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1086 trades · win 40% · PF 0.87 · expectancy -2.69 ticks (-0.09R) · PnL $-9202 · maxDD -48.7%
- **OOS**: 646 trades · win 42% · PF 0.96 · expectancy -2.22 ticks (-0.01R) · PnL $-1541 · maxDD -11.1%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1376 trades · win 54% · PF 0.80 · expectancy -4.33 ticks (-0.09R) · PnL $-13860 · maxDD -54.7%
- **OOS**: 859 trades · win 56% · PF 0.97 · expectancy -1.90 ticks (-0.02R) · PnL $-1468 · maxDD -13.2%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 694 trades · win 36% · PF 0.95 · expectancy -2.50 ticks (-0.05R) · PnL $-2673 · maxDD -15.3%
- **OOS**: 498 trades · win 33% · PF 0.85 · expectancy -10.03 ticks (-0.09R) · PnL $-5363 · maxDD -28.4%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 256 trades · win 16% · PF 1.30 · expectancy -0.59 ticks (0.25R) · PnL $8095 · maxDD -16.6%
- **OOS**: 156 trades · win 17% · PF 1.19 · expectancy 11.85 ticks (0.16R) · PnL $2797 · maxDD -16.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.53 | -2.33 | -2.98 | -3.65 | -5.02 |
| vwap_reversion | -0.69 | -2.74 | -3.54 | -4.33 | -5.65 |
| momentum_burst | -0.71 | -2.21 | -2.78 | -3.46 | -4.55 |
| session_drift | -8.86 | -9.94 | -10.48 | -11.02 | -13.71 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._