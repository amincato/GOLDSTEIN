# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-25T10:36:36+00:00 · 5m bars · 465 days (120621 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.4% | 44.4 | 853 |
| london | 20.9% | 41.9 | 882 |
| overlap | 29.8% | 64.3 | 1659 |
| ny | 21.5% | 41.3 | 1038 |
| late | 21.2% | 36.4 | 434 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1193 trades · win 39% · PF 0.86 · expectancy -3.48 ticks (-0.09R) · PnL $-10602 · maxDD -48.7%
- **OOS**: 668 trades · win 42% · PF 0.95 · expectancy -3.43 ticks (-0.01R) · PnL $-2102 · maxDD -16.4%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1495 trades · win 54% · PF 0.82 · expectancy -3.44 ticks (-0.08R) · PnL $-12961 · maxDD -56.4%
- **OOS**: 897 trades · win 54% · PF 0.91 · expectancy -4.79 ticks (-0.06R) · PnL $-4317 · maxDD -20.1%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 934 trades · win 36% · PF 0.94 · expectancy -1.31 ticks (-0.05R) · PnL $-4027 · maxDD -31.0%
- **OOS**: 686 trades · win 34% · PF 0.86 · expectancy -6.29 ticks (-0.08R) · PnL $-6748 · maxDD -31.9%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 277 trades · win 17% · PF 1.39 · expectancy 5.02 ticks (0.34R) · PnL $11121 · maxDD -16.6%
- **OOS**: 165 trades · win 15% · PF 0.96 · expectancy 1.59 ticks (-0.08R) · PnL $-583 · maxDD -17.7%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.99 | -2.90 | -3.62 | -4.37 | -5.72 |
| vwap_reversion | -1.19 | -3.21 | -4.04 | -4.83 | -6.13 |
| momentum_burst | -0.86 | -2.31 | -2.88 | -3.54 | -4.76 |
| session_drift | -6.18 | -7.26 | -7.80 | -8.34 | -10.91 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._