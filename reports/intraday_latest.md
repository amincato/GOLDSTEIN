# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-03T13:03:07+00:00 · 5m bars · 498 days (128105 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.0% | 44.3 | 827 |
| london | 20.5% | 41.6 | 856 |
| overlap | 29.5% | 64.1 | 1628 |
| ny | 21.1% | 40.9 | 1008 |
| late | 20.7% | 35.6 | 418 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1278 trades · win 40% · PF 0.87 · expectancy -3.18 ticks (-0.08R) · PnL $-10549 · maxDD -48.7%
- **OOS**: 688 trades · win 42% · PF 0.96 · expectancy -3.11 ticks (-0.02R) · PnL $-1862 · maxDD -17.9%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1601 trades · win 55% · PF 0.84 · expectancy -2.92 ticks (-0.07R) · PnL $-12515 · maxDD -56.4%
- **OOS**: 930 trades · win 52% · PF 0.83 · expectancy -7.42 ticks (-0.10R) · PnL $-7838 · maxDD -32.6%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 993 trades · win 36% · PF 0.95 · expectancy -0.87 ticks (-0.04R) · PnL $-3922 · maxDD -31.0%
- **OOS**: 747 trades · win 33% · PF 0.86 · expectancy -6.31 ticks (-0.09R) · PnL $-7583 · maxDD -33.4%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 296 trades · win 18% · PF 1.40 · expectancy 9.37 ticks (0.35R) · PnL $12505 · maxDD -16.6%
- **OOS**: 173 trades · win 12% · PF 0.76 · expectancy -11.66 ticks (-0.20R) · PnL $-3913 · maxDD -18.9%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.80 | -2.81 | -3.52 | -4.20 | -5.51 |
| vwap_reversion | -1.54 | -3.54 | -4.34 | -5.06 | -6.40 |
| momentum_burst | -1.22 | -2.64 | -3.20 | -3.85 | -5.07 |
| session_drift | -7.56 | -8.64 | -9.18 | -9.72 | -12.20 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._