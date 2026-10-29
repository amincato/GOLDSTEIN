# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-29T11:48:49+00:00 · 5m bars · 494 days (127273 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.0% | 44.3 | 830 |
| london | 20.5% | 41.6 | 857 |
| overlap | 29.5% | 64.1 | 1630 |
| ny | 21.1% | 40.9 | 1010 |
| late | 20.7% | 35.6 | 419 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1266 trades · win 40% · PF 0.87 · expectancy -3.23 ticks (-0.08R) · PnL $-10582 · maxDD -48.7%
- **OOS**: 687 trades · win 41% · PF 0.93 · expectancy -4.92 ticks (-0.03R) · PnL $-3167 · maxDD -21.1%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1589 trades · win 55% · PF 0.84 · expectancy -3.07 ticks (-0.07R) · PnL $-12715 · maxDD -56.4%
- **OOS**: 930 trades · win 53% · PF 0.85 · expectancy -6.43 ticks (-0.09R) · PnL $-6961 · maxDD -30.6%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 984 trades · win 36% · PF 0.95 · expectancy -0.63 ticks (-0.04R) · PnL $-3617 · maxDD -31.0%
- **OOS**: 747 trades · win 33% · PF 0.87 · expectancy -6.51 ticks (-0.08R) · PnL $-7069 · maxDD -32.7%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 294 trades · win 18% · PF 1.41 · expectancy 10.03 ticks (0.36R) · PnL $12679 · maxDD -16.6%
- **OOS**: 172 trades · win 13% · PF 0.82 · expectancy -9.70 ticks (-0.15R) · PnL $-3005 · maxDD -19.0%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.94 | -3.05 | -3.77 | -4.43 | -5.87 |
| vwap_reversion | -1.45 | -3.45 | -4.21 | -4.97 | -6.26 |
| momentum_burst | -1.09 | -2.51 | -3.07 | -3.72 | -4.98 |
| session_drift | -7.13 | -8.21 | -8.75 | -9.29 | -11.79 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._