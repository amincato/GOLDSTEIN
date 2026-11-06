# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-06T13:17:20+00:00 · 5m bars · 501 days (128939 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.1% | 44.4 | 826 |
| london | 20.5% | 41.5 | 852 |
| overlap | 29.5% | 64.1 | 1626 |
| ny | 21.1% | 40.9 | 1006 |
| late | 20.7% | 35.6 | 418 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1288 trades · win 40% · PF 0.87 · expectancy -3.28 ticks (-0.08R) · PnL $-10838 · maxDD -48.7%
- **OOS**: 692 trades · win 41% · PF 0.94 · expectancy -4.74 ticks (-0.03R) · PnL $-2777 · maxDD -20.9%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1613 trades · win 55% · PF 0.85 · expectancy -2.88 ticks (-0.07R) · PnL $-12495 · maxDD -56.4%
- **OOS**: 934 trades · win 52% · PF 0.84 · expectancy -6.84 ticks (-0.09R) · PnL $-7469 · maxDD -31.7%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1005 trades · win 36% · PF 0.95 · expectancy -0.99 ticks (-0.04R) · PnL $-3860 · maxDD -31.0%
- **OOS**: 752 trades · win 34% · PF 0.87 · expectancy -6.07 ticks (-0.08R) · PnL $-6738 · maxDD -32.4%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 298 trades · win 18% · PF 1.41 · expectancy 9.99 ticks (0.35R) · PnL $12708 · maxDD -16.6%
- **OOS**: 174 trades · win 13% · PF 0.86 · expectancy -8.14 ticks (-0.09R) · PnL $-2336 · maxDD -18.6%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.95 | -2.96 | -3.67 | -4.33 | -5.77 |
| vwap_reversion | -1.37 | -3.35 | -4.16 | -4.91 | -6.25 |
| momentum_burst | -0.92 | -2.33 | -2.90 | -3.54 | -4.94 |
| session_drift | -7.61 | -8.69 | -9.23 | -9.77 | -12.24 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._