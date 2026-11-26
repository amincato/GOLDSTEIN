# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-26T15:50:29+00:00 · 5m bars · 518 days (132710 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.2% | 44.9 | 817 |
| london | 20.5% | 41.6 | 845 |
| overlap | 29.6% | 64.3 | 1619 |
| ny | 21.2% | 41.1 | 1001 |
| late | 21.2% | 35.9 | 414 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1384 trades · win 35% · PF 0.91 · expectancy -0.80 ticks (-0.07R) · PnL $-9814 · maxDD -58.6%
- **OOS**: 745 trades · win 35% · PF 0.90 · expectancy -6.28 ticks (-0.06R) · PnL $-4702 · maxDD -21.9%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1668 trades · win 54% · PF 0.84 · expectancy -3.09 ticks (-0.07R) · PnL $-13070 · maxDD -56.4%
- **OOS**: 953 trades · win 52% · PF 0.82 · expectancy -7.71 ticks (-0.10R) · PnL $-8565 · maxDD -37.9%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1050 trades · win 36% · PF 0.94 · expectancy -1.67 ticks (-0.04R) · PnL $-4473 · maxDD -31.0%
- **OOS**: 773 trades · win 33% · PF 0.88 · expectancy -5.08 ticks (-0.08R) · PnL $-6703 · maxDD -31.6%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 308 trades · win 18% · PF 1.38 · expectancy 7.74 ticks (0.32R) · PnL $12116 · maxDD -16.6%
- **OOS**: 178 trades · win 13% · PF 0.91 · expectancy -6.00 ticks (-0.05R) · PnL $-1602 · maxDD -16.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.82 | -2.99 | -3.70 | -4.36 | -5.80 |
| vwap_reversion | -1.67 | -3.63 | -4.42 | -5.17 | -6.50 |
| momentum_burst | -0.87 | -2.27 | -2.90 | -3.74 | -5.21 |
| session_drift | -9.03 | -10.11 | -10.65 | -11.19 | -13.62 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._