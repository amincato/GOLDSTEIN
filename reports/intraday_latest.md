# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-09T18:16:10+00:00 · 5m bars · 425 days (111411 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.8% | 44.1 | 890 |
| london | 21.3% | 41.8 | 916 |
| overlap | 29.8% | 63.2 | 1685 |
| ny | 21.8% | 41.1 | 1075 |
| late | 21.8% | 36.7 | 454 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1074 trades · win 39% · PF 0.86 · expectancy -3.44 ticks (-0.10R) · PnL $-9922 · maxDD -48.7%
- **OOS**: 653 trades · win 42% · PF 0.98 · expectancy -1.04 ticks (0.00R) · PnL $-833 · maxDD -10.8%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1365 trades · win 54% · PF 0.81 · expectancy -3.72 ticks (-0.09R) · PnL $-12859 · maxDD -53.9%
- **OOS**: 859 trades · win 56% · PF 0.94 · expectancy -2.84 ticks (-0.03R) · PnL $-2461 · maxDD -13.7%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 690 trades · win 36% · PF 0.95 · expectancy -2.81 ticks (-0.05R) · PnL $-2787 · maxDD -15.3%
- **OOS**: 496 trades · win 34% · PF 0.87 · expectancy -9.05 ticks (-0.07R) · PnL $-4641 · maxDD -28.3%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 254 trades · win 16% · PF 1.30 · expectancy -0.98 ticks (0.25R) · PnL $8058 · maxDD -16.6%
- **OOS**: 155 trades · win 17% · PF 1.15 · expectancy 9.78 ticks (0.12R) · PnL $2214 · maxDD -16.2%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.52 | -2.33 | -2.98 | -3.65 | -5.02 |
| vwap_reversion | -0.71 | -2.77 | -3.57 | -4.36 | -5.69 |
| momentum_burst | -0.55 | -2.04 | -2.62 | -3.30 | -4.39 |
| session_drift | -8.61 | -9.70 | -10.24 | -10.78 | -13.47 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._