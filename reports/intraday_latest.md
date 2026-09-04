# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-04T09:59:49+00:00 · 5m bars · 449 days (116810 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.4 | 868 |
| london | 21.0% | 41.8 | 895 |
| overlap | 29.7% | 63.9 | 1672 |
| ny | 21.5% | 41.1 | 1051 |
| late | 21.4% | 36.5 | 441 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1140 trades · win 40% · PF 0.87 · expectancy -2.32 ticks (-0.08R) · PnL $-9060 · maxDD -48.7%
- **OOS**: 673 trades · win 42% · PF 0.95 · expectancy -3.62 ticks (-0.01R) · PnL $-2390 · maxDD -11.9%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1440 trades · win 54% · PF 0.81 · expectancy -4.06 ticks (-0.09R) · PnL $-13602 · maxDD -56.4%
- **OOS**: 880 trades · win 55% · PF 0.92 · expectancy -3.93 ticks (-0.04R) · PnL $-3436 · maxDD -19.3%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 721 trades · win 36% · PF 0.96 · expectancy -2.31 ticks (-0.04R) · PnL $-2271 · maxDD -15.3%
- **OOS**: 541 trades · win 32% · PF 0.80 · expectancy -11.63 ticks (-0.12R) · PnL $-7920 · maxDD -32.3%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 267 trades · win 17% · PF 1.37 · expectancy 3.42 ticks (0.33R) · PnL $10129 · maxDD -16.6%
- **OOS**: 162 trades · win 15% · PF 1.08 · expectancy 6.39 ticks (0.03R) · PnL $1274 · maxDD -17.3%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.19 | -2.16 | -2.80 | -3.46 | -4.82 |
| vwap_reversion | -1.18 | -3.23 | -4.02 | -4.72 | -6.03 |
| momentum_burst | -0.94 | -2.41 | -2.99 | -3.65 | -5.07 |
| session_drift | -4.78 | -5.86 | -6.40 | -6.95 | -9.57 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._