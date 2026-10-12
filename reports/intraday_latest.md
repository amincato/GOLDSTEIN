# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-12T13:34:56+00:00 · 5m bars · 479 days (123698 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.2% | 44.3 | 842 |
| london | 20.7% | 41.8 | 871 |
| overlap | 29.7% | 64.3 | 1644 |
| ny | 21.3% | 41.1 | 1025 |
| late | 21.0% | 36.0 | 427 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1225 trades · win 39% · PF 0.86 · expectancy -3.92 ticks (-0.09R) · PnL $-11246 · maxDD -48.7%
- **OOS**: 682 trades · win 41% · PF 0.94 · expectancy -4.16 ticks (-0.02R) · PnL $-2468 · maxDD -18.8%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1536 trades · win 54% · PF 0.83 · expectancy -3.66 ticks (-0.08R) · PnL $-13439 · maxDD -56.4%
- **OOS**: 916 trades · win 54% · PF 0.89 · expectancy -4.99 ticks (-0.07R) · PnL $-5024 · maxDD -25.4%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 947 trades · win 36% · PF 0.94 · expectancy -1.81 ticks (-0.05R) · PnL $-4513 · maxDD -31.0%
- **OOS**: 721 trades · win 34% · PF 0.88 · expectancy -5.15 ticks (-0.07R) · PnL $-6211 · maxDD -31.0%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 285 trades · win 17% · PF 1.39 · expectancy 7.31 ticks (0.35R) · PnL $11815 · maxDD -16.6%
- **OOS**: 168 trades · win 14% · PF 0.93 · expectancy -2.48 ticks (-0.06R) · PnL $-1089 · maxDD -18.3%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.08 | -3.09 | -3.77 | -4.44 | -5.86 |
| vwap_reversion | -1.28 | -3.31 | -4.08 | -4.84 | -6.14 |
| momentum_burst | -1.08 | -2.52 | -3.08 | -3.74 | -5.02 |
| session_drift | -7.27 | -8.35 | -8.89 | -9.44 | -11.97 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._