# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-17T14:56:45+00:00 · 5m bars · 510 days (130893 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.0% | 44.5 | 820 |
| london | 20.4% | 41.5 | 848 |
| overlap | 29.4% | 64.1 | 1618 |
| ny | 21.0% | 40.8 | 1002 |
| late | 20.5% | 35.6 | 415 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1316 trades · win 40% · PF 0.89 · expectancy -2.39 ticks (-0.08R) · PnL $-9808 · maxDD -48.7%
- **OOS**: 704 trades · win 41% · PF 0.90 · expectancy -6.92 ticks (-0.04R) · PnL $-4266 · maxDD -21.7%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1648 trades · win 55% · PF 0.85 · expectancy -2.88 ticks (-0.07R) · PnL $-12652 · maxDD -56.4%
- **OOS**: 943 trades · win 52% · PF 0.82 · expectancy -7.75 ticks (-0.10R) · PnL $-8611 · maxDD -36.0%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1032 trades · win 36% · PF 0.94 · expectancy -2.01 ticks (-0.04R) · PnL $-4744 · maxDD -31.0%
- **OOS**: 761 trades · win 33% · PF 0.88 · expectancy -4.88 ticks (-0.08R) · PnL $-6390 · maxDD -29.9%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 304 trades · win 17% · PF 1.38 · expectancy 7.75 ticks (0.32R) · PnL $12088 · maxDD -16.6%
- **OOS**: 175 trades · win 14% · PF 0.95 · expectancy -2.02 ticks (-0.01R) · PnL $-771 · maxDD -16.7%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.97 | -3.06 | -3.77 | -4.44 | -5.91 |
| vwap_reversion | -1.57 | -3.54 | -4.34 | -5.09 | -6.42 |
| momentum_burst | -0.93 | -2.34 | -2.90 | -3.65 | -5.03 |
| session_drift | -8.27 | -9.35 | -9.89 | -10.43 | -12.88 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._