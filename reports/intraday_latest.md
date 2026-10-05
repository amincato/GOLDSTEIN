# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-05T12:42:34+00:00 · 5m bars · 473 days (122304 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.3% | 44.4 | 847 |
| london | 20.8% | 41.9 | 876 |
| overlap | 29.7% | 64.4 | 1653 |
| ny | 21.4% | 41.3 | 1032 |
| late | 21.1% | 36.2 | 430 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1208 trades · win 39% · PF 0.86 · expectancy -4.04 ticks (-0.09R) · PnL $-11336 · maxDD -48.7%
- **OOS**: 679 trades · win 42% · PF 0.95 · expectancy -3.47 ticks (-0.01R) · PnL $-1998 · maxDD -17.4%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1517 trades · win 54% · PF 0.84 · expectancy -2.81 ticks (-0.08R) · PnL $-12084 · maxDD -56.4%
- **OOS**: 906 trades · win 53% · PF 0.86 · expectancy -6.58 ticks (-0.07R) · PnL $-6265 · maxDD -25.1%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 935 trades · win 36% · PF 0.94 · expectancy -1.48 ticks (-0.05R) · PnL $-4185 · maxDD -31.0%
- **OOS**: 716 trades · win 33% · PF 0.85 · expectancy -6.32 ticks (-0.09R) · PnL $-7490 · maxDD -32.8%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 281 trades · win 17% · PF 1.37 · expectancy 4.72 ticks (0.34R) · PnL $11059 · maxDD -16.6%
- **OOS**: 167 trades · win 13% · PF 0.81 · expectancy -9.82 ticks (-0.16R) · PnL $-2925 · maxDD -18.8%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.24 | -3.14 | -3.86 | -4.61 | -5.96 |
| vwap_reversion | -1.26 | -3.34 | -4.12 | -4.94 | -6.24 |
| momentum_burst | -0.75 | -2.18 | -2.75 | -3.40 | -4.63 |
| session_drift | -6.53 | -7.61 | -8.16 | -8.70 | -11.25 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._