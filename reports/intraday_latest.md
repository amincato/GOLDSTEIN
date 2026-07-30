# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-07-30T23:13:32+00:00 · 5m bars · 43 days (12384 bars) · contract MGC · data: synthetic_

> ⚠️ **DEMO DATA** — intraday bars are synthetic; this validates the machinery, not a live edge. Run `goldstein intraday fetch` from a network-enabled environment (the daily CI does it automatically).

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 15.7% | 30.0 | 964 |
| london | 23.0% | 52.1 | 1779 |
| overlap | 38.9% | 84.3 | 2575 |
| ny | 31.4% | 66.9 | 1926 |
| late | 13.1% | 25.9 | 791 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 85 trades · win 41% · PF 1.00 · expectancy -1.18 ticks (-0.01R) · PnL $6 · maxDD -5.2%
- **OOS**: 62 trades · win 27% · PF 0.47 · expectancy -31.59 ticks (-0.38R) · PnL $-3062 · maxDD -11.0%

### vwap_reversion
- params: `{'z_entry': 1.5, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 146 trades · win 56% · PF 0.96 · expectancy 5.11 ticks (-0.05R) · PnL $-276 · maxDD -6.1%
- **OOS**: 98 trades · win 58% · PF 0.93 · expectancy 0.29 ticks (-0.04R) · PnL $-329 · maxDD -3.3%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 80 trades · win 30% · PF 0.73 · expectancy -12.23 ticks (-0.21R) · PnL $-1825 · maxDD -10.5%
- **OOS**: 49 trades · win 27% · PF 0.56 · expectancy -4.62 ticks (-0.37R) · PnL $-2115 · maxDD -7.8%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -10.89 | -13.72 | -14.24 | -14.78 | -16.28 |
| vwap_reversion | 4.51 | 3.44 | 2.06 | 0.96 | -0.57 |
| momentum_burst | -15.53 | -16.53 | -17.85 | -18.38 | -19.36 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._