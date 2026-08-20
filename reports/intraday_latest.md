# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-20T06:05:18+00:00 · 5m bars · 436 days (113712 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.1 | 879 |
| london | 21.1% | 41.7 | 906 |
| overlap | 29.6% | 63.4 | 1676 |
| ny | 21.6% | 41.0 | 1063 |
| late | 21.5% | 36.6 | 447 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1101 trades · win 40% · PF 0.87 · expectancy -2.66 ticks (-0.09R) · PnL $-9373 · maxDD -48.7%
- **OOS**: 655 trades · win 42% · PF 0.96 · expectancy -2.42 ticks (-0.01R) · PnL $-1574 · maxDD -11.2%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1393 trades · win 54% · PF 0.80 · expectancy -4.51 ticks (-0.10R) · PnL $-14154 · maxDD -55.9%
- **OOS**: 871 trades · win 56% · PF 0.96 · expectancy -2.04 ticks (-0.02R) · PnL $-1732 · maxDD -14.1%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 701 trades · win 36% · PF 0.94 · expectancy -2.77 ticks (-0.05R) · PnL $-2915 · maxDD -15.3%
- **OOS**: 516 trades · win 33% · PF 0.84 · expectancy -9.51 ticks (-0.09R) · PnL $-5863 · maxDD -28.2%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 259 trades · win 16% · PF 1.30 · expectancy -0.22 ticks (0.26R) · PnL $8188 · maxDD -16.6%
- **OOS**: 159 trades · win 17% · PF 1.22 · expectancy 13.06 ticks (0.17R) · PnL $3347 · maxDD -16.7%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.40 | -2.24 | -2.88 | -3.56 | -4.92 |
| vwap_reversion | -0.88 | -2.92 | -3.72 | -4.42 | -5.74 |
| momentum_burst | -0.55 | -2.04 | -2.61 | -3.28 | -4.72 |
| session_drift | -5.52 | -6.60 | -7.14 | -7.69 | -10.35 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._