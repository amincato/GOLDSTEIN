# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-03T08:53:02+00:00 · 5m bars · 421 days (110152 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.8% | 44.0 | 894 |
| london | 21.3% | 41.8 | 922 |
| overlap | 29.7% | 63.0 | 1691 |
| ny | 21.8% | 41.2 | 1083 |
| late | 21.8% | 36.8 | 457 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1062 trades · win 39% · PF 0.85 · expectancy -3.73 ticks (-0.10R) · PnL $-10313 · maxDD -48.7%
- **OOS**: 643 trades · win 43% · PF 0.99 · expectancy -0.69 ticks (0.01R) · PnL $-509 · maxDD -10.7%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1356 trades · win 54% · PF 0.81 · expectancy -3.61 ticks (-0.09R) · PnL $-12362 · maxDD -53.9%
- **OOS**: 841 trades · win 55% · PF 0.94 · expectancy -3.14 ticks (-0.03R) · PnL $-2690 · maxDD -13.9%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 681 trades · win 36% · PF 0.95 · expectancy -2.56 ticks (-0.05R) · PnL $-2487 · maxDD -15.3%
- **OOS**: 481 trades · win 33% · PF 0.84 · expectancy -10.12 ticks (-0.09R) · PnL $-5298 · maxDD -28.7%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 252 trades · win 15% · PF 1.29 · expectancy -1.55 ticks (0.24R) · PnL $7706 · maxDD -16.6%
- **OOS**: 153 trades · win 17% · PF 1.03 · expectancy 4.46 ticks (-0.01R) · PnL $448 · maxDD -16.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.48 | -2.30 | -2.94 | -3.62 | -5.00 |
| vwap_reversion | -0.96 | -3.00 | -3.80 | -4.49 | -5.82 |
| momentum_burst | -0.47 | -1.97 | -2.55 | -3.23 | -4.30 |
| session_drift | -9.12 | -10.20 | -10.74 | -11.28 | -14.00 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._