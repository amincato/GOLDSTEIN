# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-09T12:08:14+00:00 · 5m bars · 477 days (123406 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.2% | 44.3 | 843 |
| london | 20.7% | 41.8 | 872 |
| overlap | 29.7% | 64.3 | 1647 |
| ny | 21.4% | 41.2 | 1027 |
| late | 21.0% | 36.0 | 428 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1219 trades · win 39% · PF 0.86 · expectancy -3.99 ticks (-0.09R) · PnL $-11309 · maxDD -48.7%
- **OOS**: 683 trades · win 41% · PF 0.95 · expectancy -3.92 ticks (-0.02R) · PnL $-2263 · maxDD -18.3%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1532 trades · win 54% · PF 0.83 · expectancy -3.68 ticks (-0.08R) · PnL $-13454 · maxDD -56.4%
- **OOS**: 913 trades · win 54% · PF 0.89 · expectancy -4.98 ticks (-0.07R) · PnL $-4929 · maxDD -25.4%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 945 trades · win 36% · PF 0.94 · expectancy -1.61 ticks (-0.05R) · PnL $-4318 · maxDD -31.0%
- **OOS**: 715 trades · win 34% · PF 0.86 · expectancy -5.67 ticks (-0.08R) · PnL $-6752 · maxDD -31.2%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 284 trades · win 17% · PF 1.40 · expectancy 7.67 ticks (0.35R) · PnL $11909 · maxDD -16.6%
- **OOS**: 168 trades · win 14% · PF 0.92 · expectancy -3.34 ticks (-0.06R) · PnL $-1186 · maxDD -18.4%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.06 | -3.03 | -3.72 | -4.39 | -5.81 |
| vwap_reversion | -1.33 | -3.36 | -4.13 | -4.86 | -6.16 |
| momentum_burst | -1.18 | -2.62 | -3.19 | -3.84 | -5.12 |
| session_drift | -7.11 | -8.20 | -8.74 | -9.28 | -11.82 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._