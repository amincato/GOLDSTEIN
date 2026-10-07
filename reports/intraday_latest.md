# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-07T12:03:50+00:00 · 5m bars · 475 days (122850 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.2% | 44.4 | 845 |
| london | 20.8% | 41.9 | 874 |
| overlap | 29.7% | 64.3 | 1649 |
| ny | 21.4% | 41.2 | 1028 |
| late | 21.0% | 36.1 | 429 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1214 trades · win 39% · PF 0.85 · expectancy -4.18 ticks (-0.09R) · PnL $-11523 · maxDD -48.7%
- **OOS**: 684 trades · win 42% · PF 0.96 · expectancy -3.17 ticks (-0.01R) · PnL $-1635 · maxDD -17.6%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1529 trades · win 54% · PF 0.83 · expectancy -3.28 ticks (-0.08R) · PnL $-12830 · maxDD -56.4%
- **OOS**: 907 trades · win 53% · PF 0.87 · expectancy -5.96 ticks (-0.07R) · PnL $-5931 · maxDD -26.0%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 942 trades · win 36% · PF 0.94 · expectancy -1.65 ticks (-0.05R) · PnL $-4358 · maxDD -31.0%
- **OOS**: 709 trades · win 34% · PF 0.86 · expectancy -5.65 ticks (-0.08R) · PnL $-6810 · maxDD -30.7%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 283 trades · win 17% · PF 1.41 · expectancy 8.61 ticks (0.36R) · PnL $12168 · maxDD -16.6%
- **OOS**: 167 trades · win 13% · PF 0.80 · expectancy -7.68 ticks (-0.17R) · PnL $-3163 · maxDD -18.5%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.93 | -2.91 | -3.60 | -4.26 | -5.60 |
| vwap_reversion | -1.42 | -3.45 | -4.23 | -4.96 | -6.25 |
| momentum_burst | -1.24 | -2.68 | -3.25 | -3.90 | -5.19 |
| session_drift | -6.88 | -7.97 | -8.51 | -9.05 | -11.60 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._