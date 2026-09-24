# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-24T10:33:08+00:00 · 5m bars · 464 days (120343 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.4% | 44.5 | 855 |
| london | 20.9% | 41.9 | 883 |
| overlap | 29.8% | 64.3 | 1660 |
| ny | 21.5% | 41.2 | 1039 |
| late | 21.2% | 36.4 | 435 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1188 trades · win 39% · PF 0.86 · expectancy -3.40 ticks (-0.09R) · PnL $-10483 · maxDD -48.7%
- **OOS**: 669 trades · win 42% · PF 0.95 · expectancy -3.45 ticks (-0.01R) · PnL $-2117 · maxDD -16.5%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1489 trades · win 54% · PF 0.82 · expectancy -3.51 ticks (-0.08R) · PnL $-13049 · maxDD -56.4%
- **OOS**: 899 trades · win 54% · PF 0.91 · expectancy -4.61 ticks (-0.06R) · PnL $-4167 · maxDD -19.8%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 934 trades · win 36% · PF 0.94 · expectancy -1.31 ticks (-0.05R) · PnL $-4027 · maxDD -31.0%
- **OOS**: 680 trades · win 33% · PF 0.85 · expectancy -6.48 ticks (-0.08R) · PnL $-7083 · maxDD -31.9%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 276 trades · win 17% · PF 1.40 · expectancy 5.53 ticks (0.35R) · PnL $11258 · maxDD -16.6%
- **OOS**: 165 trades · win 15% · PF 0.94 · expectancy -0.69 ticks (-0.08R) · PnL $-912 · maxDD -18.0%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.95 | -2.86 | -3.58 | -4.34 | -5.69 |
| vwap_reversion | -1.17 | -3.19 | -4.02 | -4.81 | -6.11 |
| momentum_burst | -0.95 | -2.40 | -2.97 | -3.63 | -4.86 |
| session_drift | -6.02 | -7.10 | -7.64 | -8.18 | -10.76 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._