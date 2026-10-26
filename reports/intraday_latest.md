# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-26T11:35:20+00:00 · 5m bars · 491 days (126440 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.1% | 44.3 | 833 |
| london | 20.5% | 41.6 | 861 |
| overlap | 29.5% | 64.2 | 1635 |
| ny | 21.2% | 40.9 | 1013 |
| late | 20.8% | 35.7 | 421 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1255 trades · win 40% · PF 0.87 · expectancy -3.42 ticks (-0.09R) · PnL $-10776 · maxDD -48.7%
- **OOS**: 686 trades · win 41% · PF 0.94 · expectancy -3.80 ticks (-0.03R) · PnL $-2551 · maxDD -17.8%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1577 trades · win 54% · PF 0.84 · expectancy -3.16 ticks (-0.07R) · PnL $-12865 · maxDD -56.4%
- **OOS**: 919 trades · win 53% · PF 0.86 · expectancy -6.16 ticks (-0.08R) · PnL $-6411 · maxDD -28.0%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 975 trades · win 36% · PF 0.96 · expectancy -0.43 ticks (-0.03R) · PnL $-3117 · maxDD -31.0%
- **OOS**: 737 trades · win 33% · PF 0.85 · expectancy -6.57 ticks (-0.09R) · PnL $-7702 · maxDD -34.2%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 292 trades · win 17% · PF 1.41 · expectancy 9.28 ticks (0.35R) · PnL $12440 · maxDD -16.6%
- **OOS**: 171 trades · win 13% · PF 0.80 · expectancy -9.76 ticks (-0.16R) · PnL $-3207 · maxDD -18.8%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.15 | -3.05 | -3.77 | -4.45 | -5.82 |
| vwap_reversion | -1.37 | -3.34 | -4.15 | -4.88 | -6.17 |
| momentum_burst | -1.52 | -2.95 | -3.51 | -4.16 | -5.39 |
| session_drift | -8.38 | -9.46 | -10.00 | -10.54 | -13.04 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._