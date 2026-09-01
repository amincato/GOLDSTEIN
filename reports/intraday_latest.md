# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-01T10:30:45+00:00 · 5m bars · 446 days (115985 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.3 | 870 |
| london | 21.1% | 41.8 | 898 |
| overlap | 29.7% | 63.8 | 1672 |
| ny | 21.6% | 41.1 | 1055 |
| late | 21.5% | 36.6 | 442 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1128 trades · win 40% · PF 0.87 · expectancy -2.54 ticks (-0.09R) · PnL $-9361 · maxDD -48.7%
- **OOS**: 670 trades · win 42% · PF 0.96 · expectancy -2.57 ticks (-0.00R) · PnL $-1594 · maxDD -11.1%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1428 trades · win 54% · PF 0.80 · expectancy -4.25 ticks (-0.09R) · PnL $-13799 · maxDD -56.4%
- **OOS**: 881 trades · win 55% · PF 0.94 · expectancy -3.25 ticks (-0.04R) · PnL $-2846 · maxDD -17.1%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 713 trades · win 36% · PF 0.95 · expectancy -2.26 ticks (-0.04R) · PnL $-2467 · maxDD -15.3%
- **OOS**: 540 trades · win 33% · PF 0.82 · expectancy -10.94 ticks (-0.11R) · PnL $-7000 · maxDD -29.2%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 265 trades · win 17% · PF 1.34 · expectancy 2.27 ticks (0.31R) · PnL $9418 · maxDD -16.6%
- **OOS**: 161 trades · win 16% · PF 1.05 · expectancy 4.37 ticks (0.00R) · PnL $738 · maxDD -16.8%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.56 | -2.40 | -3.04 | -3.80 | -5.15 |
| vwap_reversion | -0.95 | -3.06 | -3.85 | -4.65 | -5.96 |
| momentum_burst | -0.92 | -2.39 | -2.96 | -3.63 | -4.87 |
| session_drift | -6.75 | -7.84 | -8.38 | -8.92 | -11.55 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._