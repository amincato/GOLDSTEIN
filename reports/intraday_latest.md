# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-15T10:22:44+00:00 · 5m bars · 482 days (124492 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.2% | 44.3 | 839 |
| london | 20.7% | 41.7 | 868 |
| overlap | 29.7% | 64.3 | 1642 |
| ny | 21.3% | 41.0 | 1021 |
| late | 20.9% | 35.9 | 425 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1232 trades · win 39% · PF 0.86 · expectancy -3.93 ticks (-0.09R) · PnL $-11289 · maxDD -48.7%
- **OOS**: 683 trades · win 42% · PF 0.96 · expectancy -3.24 ticks (-0.01R) · PnL $-1930 · maxDD -19.1%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1548 trades · win 54% · PF 0.83 · expectancy -3.71 ticks (-0.08R) · PnL $-13566 · maxDD -56.4%
- **OOS**: 913 trades · win 54% · PF 0.88 · expectancy -5.19 ticks (-0.07R) · PnL $-5574 · maxDD -26.7%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 954 trades · win 36% · PF 0.94 · expectancy -1.66 ticks (-0.05R) · PnL $-4453 · maxDD -31.0%
- **OOS**: 728 trades · win 34% · PF 0.89 · expectancy -4.89 ticks (-0.06R) · PnL $-5637 · maxDD -32.1%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 287 trades · win 17% · PF 1.38 · expectancy 6.29 ticks (0.34R) · PnL $11537 · maxDD -16.6%
- **OOS**: 169 trades · win 15% · PF 0.96 · expectancy -0.21 ticks (-0.03R) · PnL $-630 · maxDD -18.2%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.94 | -2.94 | -3.63 | -4.29 | -5.75 |
| vwap_reversion | -1.38 | -3.40 | -4.17 | -4.93 | -6.23 |
| momentum_burst | -1.05 | -2.49 | -3.05 | -3.70 | -4.99 |
| session_drift | -7.43 | -8.51 | -9.05 | -9.59 | -12.12 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._