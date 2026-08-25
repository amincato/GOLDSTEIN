# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-25T06:06:27+00:00 · 5m bars · 440 days (114533 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.2 | 876 |
| london | 21.1% | 41.8 | 904 |
| overlap | 29.7% | 63.5 | 1675 |
| ny | 21.6% | 41.1 | 1060 |
| late | 21.5% | 36.6 | 446 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1113 trades · win 39% · PF 0.86 · expectancy -2.89 ticks (-0.09R) · PnL $-9937 · maxDD -48.7%
- **OOS**: 655 trades · win 42% · PF 0.97 · expectancy -2.19 ticks (-0.00R) · PnL $-1143 · maxDD -10.9%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1410 trades · win 54% · PF 0.80 · expectancy -4.46 ticks (-0.09R) · PnL $-14208 · maxDD -56.4%
- **OOS**: 871 trades · win 56% · PF 0.96 · expectancy -2.40 ticks (-0.02R) · PnL $-1872 · maxDD -14.8%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 705 trades · win 36% · PF 0.94 · expectancy -2.83 ticks (-0.05R) · PnL $-3058 · maxDD -15.3%
- **OOS**: 524 trades · win 33% · PF 0.83 · expectancy -10.39 ticks (-0.10R) · PnL $-6340 · maxDD -28.3%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 262 trades · win 16% · PF 1.33 · expectancy 1.18 ticks (0.29R) · PnL $8879 · maxDD -16.6%
- **OOS**: 159 trades · win 17% · PF 1.22 · expectancy 12.81 ticks (0.17R) · PnL $3429 · maxDD -16.5%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.21 | -2.05 | -2.69 | -3.36 | -4.72 |
| vwap_reversion | -0.88 | -2.95 | -3.74 | -4.45 | -5.76 |
| momentum_burst | -0.77 | -2.25 | -2.83 | -3.50 | -4.93 |
| session_drift | -6.12 | -7.21 | -7.75 | -8.29 | -10.94 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._