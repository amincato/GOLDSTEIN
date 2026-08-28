# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-28T17:44:43+00:00 · 5m bars · 443 days (115513 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.3 | 873 |
| london | 21.1% | 41.8 | 900 |
| overlap | 29.7% | 63.8 | 1674 |
| ny | 21.6% | 41.1 | 1057 |
| late | 21.4% | 36.6 | 444 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1119 trades · win 40% · PF 0.87 · expectancy -2.59 ticks (-0.09R) · PnL $-9520 · maxDD -48.7%
- **OOS**: 672 trades · win 42% · PF 0.96 · expectancy -2.85 ticks (-0.01R) · PnL $-1688 · maxDD -11.1%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1416 trades · win 54% · PF 0.80 · expectancy -4.39 ticks (-0.09R) · PnL $-14151 · maxDD -56.4%
- **OOS**: 886 trades · win 56% · PF 0.96 · expectancy -2.54 ticks (-0.03R) · PnL $-1884 · maxDD -16.5%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 706 trades · win 36% · PF 0.94 · expectancy -2.65 ticks (-0.05R) · PnL $-2934 · maxDD -15.3%
- **OOS**: 542 trades · win 33% · PF 0.83 · expectancy -10.27 ticks (-0.10R) · PnL $-6373 · maxDD -28.5%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 263 trades · win 16% · PF 1.32 · expectancy 1.02 ticks (0.28R) · PnL $8750 · maxDD -16.6%
- **OOS**: 161 trades · win 17% · PF 1.20 · expectancy 12.00 ticks (0.16R) · PnL $3176 · maxDD -16.4%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.15 | -2.13 | -2.77 | -3.44 | -4.79 |
| vwap_reversion | -0.78 | -2.84 | -3.63 | -4.33 | -5.69 |
| momentum_burst | -0.61 | -2.08 | -2.66 | -3.32 | -4.75 |
| session_drift | -6.64 | -7.72 | -8.26 | -8.80 | -11.44 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._