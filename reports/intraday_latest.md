# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-18T10:05:22+00:00 · 5m bars · 459 days (119231 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.5% | 44.5 | 859 |
| london | 20.9% | 41.9 | 886 |
| overlap | 29.8% | 64.3 | 1666 |
| ny | 21.6% | 41.3 | 1044 |
| late | 21.3% | 36.5 | 437 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1172 trades · win 40% · PF 0.87 · expectancy -3.00 ticks (-0.09R) · PnL $-9970 · maxDD -48.7%
- **OOS**: 676 trades · win 42% · PF 0.94 · expectancy -4.38 ticks (-0.02R) · PnL $-2853 · maxDD -16.6%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1471 trades · win 54% · PF 0.81 · expectancy -3.94 ticks (-0.09R) · PnL $-13620 · maxDD -56.4%
- **OOS**: 895 trades · win 55% · PF 0.93 · expectancy -3.56 ticks (-0.05R) · PnL $-3020 · maxDD -19.2%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 923 trades · win 36% · PF 0.95 · expectancy -0.90 ticks (-0.04R) · PnL $-3518 · maxDD -31.0%
- **OOS**: 667 trades · win 33% · PF 0.85 · expectancy -6.63 ticks (-0.08R) · PnL $-6895 · maxDD -32.5%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 273 trades · win 17% · PF 1.41 · expectancy 6.84 ticks (0.36R) · PnL $11599 · maxDD -16.6%
- **OOS**: 164 trades · win 15% · PF 0.95 · expectancy -1.65 ticks (-0.07R) · PnL $-862 · maxDD -18.2%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.06 | -2.98 | -3.64 | -4.40 | -5.75 |
| vwap_reversion | -1.15 | -3.19 | -4.02 | -4.81 | -6.12 |
| momentum_burst | -0.85 | -2.30 | -2.87 | -3.53 | -4.77 |
| session_drift | -5.42 | -6.50 | -7.04 | -7.59 | -10.18 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._