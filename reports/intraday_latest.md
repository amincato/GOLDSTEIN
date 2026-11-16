# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-16T14:02:51+00:00 · 5m bars · 509 days (130606 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.0% | 44.5 | 821 |
| london | 20.4% | 41.5 | 849 |
| overlap | 29.4% | 64.1 | 1620 |
| ny | 21.0% | 40.8 | 1003 |
| late | 20.6% | 35.6 | 415 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1362 trades · win 35% · PF 0.90 · expectancy -0.99 ticks (-0.07R) · PnL $-10001 · maxDD -58.6%
- **OOS**: 733 trades · win 35% · PF 0.91 · expectancy -6.08 ticks (-0.05R) · PnL $-4252 · maxDD -21.0%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1642 trades · win 55% · PF 0.85 · expectancy -2.87 ticks (-0.07R) · PnL $-12614 · maxDD -56.4%
- **OOS**: 942 trades · win 52% · PF 0.82 · expectancy -7.68 ticks (-0.10R) · PnL $-8452 · maxDD -35.2%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1028 trades · win 36% · PF 0.94 · expectancy -1.92 ticks (-0.04R) · PnL $-4648 · maxDD -31.0%
- **OOS**: 759 trades · win 33% · PF 0.89 · expectancy -4.78 ticks (-0.07R) · PnL $-6085 · maxDD -30.0%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 303 trades · win 17% · PF 1.39 · expectancy 8.15 ticks (0.33R) · PnL $12201 · maxDD -16.6%
- **OOS**: 175 trades · win 14% · PF 0.95 · expectancy -2.20 ticks (-0.01R) · PnL $-750 · maxDD -16.7%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.87 | -2.96 | -3.67 | -4.34 | -5.82 |
| vwap_reversion | -1.54 | -3.52 | -4.32 | -5.07 | -6.40 |
| momentum_burst | -0.96 | -2.37 | -2.93 | -3.68 | -5.07 |
| session_drift | -8.18 | -9.26 | -9.80 | -10.34 | -12.79 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._