# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-06T08:09:15+00:00 · 5m bars · 424 days (110974 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.8% | 44.0 | 891 |
| london | 21.3% | 41.8 | 918 |
| overlap | 29.6% | 63.1 | 1686 |
| ny | 21.8% | 41.1 | 1078 |
| late | 21.8% | 36.7 | 454 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1074 trades · win 39% · PF 0.86 · expectancy -3.44 ticks (-0.10R) · PnL $-9922 · maxDD -48.7%
- **OOS**: 644 trades · win 43% · PF 0.98 · expectancy -0.78 ticks (0.00R) · PnL $-653 · maxDD -10.8%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1365 trades · win 54% · PF 0.81 · expectancy -3.72 ticks (-0.09R) · PnL $-12859 · maxDD -53.9%
- **OOS**: 848 trades · win 56% · PF 0.95 · expectancy -2.77 ticks (-0.03R) · PnL $-2348 · maxDD -13.7%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 690 trades · win 36% · PF 0.95 · expectancy -2.81 ticks (-0.05R) · PnL $-2787 · maxDD -15.3%
- **OOS**: 487 trades · win 34% · PF 0.87 · expectancy -9.26 ticks (-0.07R) · PnL $-4604 · maxDD -28.3%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 254 trades · win 16% · PF 1.30 · expectancy -0.98 ticks (0.25R) · PnL $8058 · maxDD -16.6%
- **OOS**: 155 trades · win 17% · PF 1.17 · expectancy 11.12 ticks (0.15R) · PnL $2470 · maxDD -16.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.37 | -2.18 | -2.83 | -3.51 | -4.88 |
| vwap_reversion | -0.95 | -2.98 | -3.79 | -4.48 | -5.80 |
| momentum_burst | -0.35 | -1.85 | -2.43 | -3.11 | -4.14 |
| session_drift | -8.30 | -9.39 | -9.93 | -10.47 | -13.17 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._