# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-09T14:24:51+00:00 · 5m bars · 503 days (129227 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.0% | 44.5 | 825 |
| london | 20.4% | 41.5 | 852 |
| overlap | 29.4% | 64.1 | 1624 |
| ny | 21.0% | 40.9 | 1006 |
| late | 20.6% | 35.6 | 417 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1294 trades · win 40% · PF 0.87 · expectancy -3.13 ticks (-0.08R) · PnL $-10714 · maxDD -48.7%
- **OOS**: 695 trades · win 41% · PF 0.94 · expectancy -5.00 ticks (-0.03R) · PnL $-2786 · maxDD -21.0%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1619 trades · win 55% · PF 0.85 · expectancy -2.83 ticks (-0.07R) · PnL $-12494 · maxDD -56.4%
- **OOS**: 937 trades · win 52% · PF 0.84 · expectancy -7.05 ticks (-0.10R) · PnL $-7758 · maxDD -32.2%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1010 trades · win 36% · PF 0.95 · expectancy -1.05 ticks (-0.04R) · PnL $-3673 · maxDD -31.0%
- **OOS**: 756 trades · win 33% · PF 0.87 · expectancy -5.74 ticks (-0.08R) · PnL $-6811 · maxDD -32.6%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 299 trades · win 18% · PF 1.41 · expectancy 9.71 ticks (0.34R) · PnL $12635 · maxDD -16.6%
- **OOS**: 174 trades · win 13% · PF 0.93 · expectancy -4.75 ticks (-0.03R) · PnL $-1233 · maxDD -18.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.03 | -3.05 | -3.76 | -4.43 | -5.86 |
| vwap_reversion | -1.34 | -3.33 | -4.13 | -4.88 | -6.22 |
| momentum_burst | -0.96 | -2.37 | -2.94 | -3.69 | -5.08 |
| session_drift | -7.30 | -8.38 | -8.92 | -9.46 | -11.93 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._