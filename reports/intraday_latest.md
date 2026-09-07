# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-07T10:46:25+00:00 · 5m bars · 449 days (116944 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.4 | 868 |
| london | 21.0% | 41.8 | 894 |
| overlap | 29.9% | 64.0 | 1673 |
| ny | 21.5% | 41.1 | 1050 |
| late | 21.4% | 36.5 | 440 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1140 trades · win 40% · PF 0.87 · expectancy -2.32 ticks (-0.08R) · PnL $-9060 · maxDD -48.7%
- **OOS**: 679 trades · win 42% · PF 0.94 · expectancy -3.98 ticks (-0.01R) · PnL $-2655 · maxDD -12.6%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1440 trades · win 54% · PF 0.81 · expectancy -4.06 ticks (-0.09R) · PnL $-13602 · maxDD -56.4%
- **OOS**: 883 trades · win 55% · PF 0.93 · expectancy -3.68 ticks (-0.04R) · PnL $-3146 · maxDD -19.3%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 721 trades · win 36% · PF 0.96 · expectancy -2.31 ticks (-0.04R) · PnL $-2271 · maxDD -15.3%
- **OOS**: 544 trades · win 32% · PF 0.79 · expectancy -11.97 ticks (-0.13R) · PnL $-8121 · maxDD -33.1%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 267 trades · win 17% · PF 1.37 · expectancy 3.42 ticks (0.33R) · PnL $10129 · maxDD -16.6%
- **OOS**: 162 trades · win 15% · PF 1.05 · expectancy 3.94 ticks (0.01R) · PnL $869 · maxDD -17.3%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.85 | -2.68 | -3.31 | -4.07 | -5.43 |
| vwap_reversion | -1.06 | -3.16 | -3.95 | -4.75 | -6.06 |
| momentum_burst | -1.12 | -2.59 | -3.16 | -3.82 | -5.06 |
| session_drift | -4.89 | -5.98 | -6.52 | -7.06 | -9.68 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._