# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-16T10:09:16+00:00 · 5m bars · 483 days (124766 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.2% | 44.3 | 838 |
| london | 20.7% | 41.7 | 867 |
| overlap | 29.7% | 64.3 | 1641 |
| ny | 21.3% | 41.0 | 1020 |
| late | 20.9% | 35.8 | 425 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1232 trades · win 39% · PF 0.86 · expectancy -3.93 ticks (-0.09R) · PnL $-11289 · maxDD -48.7%
- **OOS**: 686 trades · win 41% · PF 0.95 · expectancy -3.60 ticks (-0.02R) · PnL $-2191 · maxDD -19.1%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1548 trades · win 54% · PF 0.83 · expectancy -3.71 ticks (-0.08R) · PnL $-13566 · maxDD -56.4%
- **OOS**: 919 trades · win 54% · PF 0.88 · expectancy -5.07 ticks (-0.07R) · PnL $-5499 · maxDD -26.4%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 954 trades · win 36% · PF 0.94 · expectancy -1.66 ticks (-0.05R) · PnL $-4453 · maxDD -31.0%
- **OOS**: 734 trades · win 34% · PF 0.88 · expectancy -5.17 ticks (-0.06R) · PnL $-5912 · maxDD -32.1%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 287 trades · win 17% · PF 1.38 · expectancy 6.29 ticks (0.34R) · PnL $11537 · maxDD -16.6%
- **OOS**: 170 trades · win 15% · PF 0.95 · expectancy -0.40 ticks (-0.04R) · PnL $-761 · maxDD -18.2%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.03 | -3.03 | -3.72 | -4.38 | -5.84 |
| vwap_reversion | -1.34 | -3.36 | -4.13 | -4.89 | -6.19 |
| momentum_burst | -1.18 | -2.61 | -3.18 | -3.83 | -5.11 |
| session_drift | -7.52 | -8.60 | -9.14 | -9.69 | -12.21 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._