# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-28T12:02:24+00:00 · 5m bars · 467 days (120913 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.3% | 44.5 | 853 |
| london | 20.8% | 42.0 | 881 |
| overlap | 29.7% | 64.3 | 1657 |
| ny | 21.5% | 41.2 | 1037 |
| late | 21.2% | 36.4 | 434 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1196 trades · win 39% · PF 0.85 · expectancy -3.86 ticks (-0.09R) · PnL $-11072 · maxDD -48.7%
- **OOS**: 670 trades · win 42% · PF 0.96 · expectancy -2.81 ticks (-0.00R) · PnL $-1693 · maxDD -16.2%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1501 trades · win 54% · PF 0.83 · expectancy -3.27 ticks (-0.08R) · PnL $-12730 · maxDD -56.4%
- **OOS**: 897 trades · win 54% · PF 0.90 · expectancy -5.08 ticks (-0.06R) · PnL $-4620 · maxDD -20.7%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 934 trades · win 36% · PF 0.94 · expectancy -1.31 ticks (-0.05R) · PnL $-4027 · maxDD -31.0%
- **OOS**: 691 trades · win 33% · PF 0.86 · expectancy -6.38 ticks (-0.08R) · PnL $-6939 · maxDD -31.9%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 278 trades · win 17% · PF 1.37 · expectancy 3.47 ticks (0.34R) · PnL $10697 · maxDD -16.6%
- **OOS**: 165 trades · win 15% · PF 0.97 · expectancy 3.02 ticks (-0.08R) · PnL $-400 · maxDD -17.5%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.03 | -2.94 | -3.66 | -4.41 | -5.76 |
| vwap_reversion | -1.22 | -3.29 | -4.07 | -4.86 | -6.16 |
| momentum_burst | -0.92 | -2.37 | -2.94 | -3.59 | -4.82 |
| session_drift | -6.30 | -7.38 | -7.93 | -8.47 | -11.04 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._