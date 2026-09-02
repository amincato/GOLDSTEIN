# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-02T09:57:36+00:00 · 5m bars · 447 days (116255 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.4 | 870 |
| london | 21.0% | 41.8 | 897 |
| overlap | 29.7% | 63.8 | 1672 |
| ny | 21.6% | 41.1 | 1054 |
| late | 21.4% | 36.6 | 442 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1134 trades · win 40% · PF 0.87 · expectancy -2.35 ticks (-0.08R) · PnL $-9031 · maxDD -48.7%
- **OOS**: 670 trades · win 42% · PF 0.95 · expectancy -3.48 ticks (-0.01R) · PnL $-2342 · maxDD -11.3%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1434 trades · win 54% · PF 0.81 · expectancy -4.18 ticks (-0.09R) · PnL $-13732 · maxDD -56.4%
- **OOS**: 873 trades · win 55% · PF 0.93 · expectancy -3.64 ticks (-0.04R) · PnL $-3156 · maxDD -18.1%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 717 trades · win 36% · PF 0.95 · expectancy -2.40 ticks (-0.04R) · PnL $-2539 · maxDD -15.3%
- **OOS**: 536 trades · win 33% · PF 0.82 · expectancy -10.82 ticks (-0.11R) · PnL $-6928 · maxDD -29.1%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 266 trades · win 17% · PF 1.34 · expectancy 1.93 ticks (0.31R) · PnL $9331 · maxDD -16.6%
- **OOS**: 161 trades · win 15% · PF 0.99 · expectancy 1.55 ticks (-0.05R) · PnL $-169 · maxDD -17.3%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.72 | -2.55 | -3.19 | -3.95 | -5.30 |
| vwap_reversion | -1.04 | -3.14 | -3.93 | -4.73 | -6.05 |
| momentum_burst | -0.92 | -2.39 | -2.96 | -3.63 | -4.87 |
| session_drift | -6.93 | -8.02 | -8.56 | -9.10 | -11.73 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._