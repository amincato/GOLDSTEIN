# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-04T08:12:07+00:00 · 5m bars · 422 days (110421 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.8% | 44.0 | 893 |
| london | 21.3% | 41.8 | 920 |
| overlap | 29.6% | 63.0 | 1688 |
| ny | 21.8% | 41.1 | 1081 |
| late | 21.8% | 36.7 | 456 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1068 trades · win 39% · PF 0.85 · expectancy -3.62 ticks (-0.10R) · PnL $-10306 · maxDD -48.7%
- **OOS**: 642 trades · win 43% · PF 0.99 · expectancy -0.79 ticks (0.01R) · PnL $-452 · maxDD -10.7%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1359 trades · win 54% · PF 0.81 · expectancy -3.71 ticks (-0.09R) · PnL $-12674 · maxDD -53.9%
- **OOS**: 843 trades · win 55% · PF 0.94 · expectancy -3.15 ticks (-0.03R) · PnL $-2674 · maxDD -13.8%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 687 trades · win 36% · PF 0.95 · expectancy -2.63 ticks (-0.05R) · PnL $-2438 · maxDD -15.3%
- **OOS**: 479 trades · win 33% · PF 0.84 · expectancy -10.08 ticks (-0.09R) · PnL $-5371 · maxDD -28.7%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 253 trades · win 16% · PF 1.30 · expectancy -0.71 ticks (0.26R) · PnL $8128 · maxDD -16.6%
- **OOS**: 153 trades · win 17% · PF 1.03 · expectancy 4.69 ticks (-0.01R) · PnL $383 · maxDD -16.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.49 | -2.30 | -2.95 | -3.63 | -5.00 |
| vwap_reversion | -1.00 | -3.03 | -3.84 | -4.53 | -5.85 |
| momentum_burst | -0.56 | -2.06 | -2.64 | -3.32 | -4.35 |
| session_drift | -9.23 | -10.32 | -10.86 | -11.40 | -14.11 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._