# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-25T16:09:08+00:00 · 5m bars · 517 days (132566 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.2% | 44.8 | 818 |
| london | 20.5% | 41.6 | 845 |
| overlap | 29.6% | 64.3 | 1619 |
| ny | 21.1% | 41.0 | 1001 |
| late | 21.2% | 35.8 | 414 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1384 trades · win 35% · PF 0.91 · expectancy -0.80 ticks (-0.07R) · PnL $-9814 · maxDD -58.6%
- **OOS**: 749 trades · win 35% · PF 0.90 · expectancy -6.13 ticks (-0.05R) · PnL $-4653 · maxDD -22.7%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1668 trades · win 54% · PF 0.84 · expectancy -3.09 ticks (-0.07R) · PnL $-13070 · maxDD -56.4%
- **OOS**: 953 trades · win 52% · PF 0.81 · expectancy -8.02 ticks (-0.10R) · PnL $-8835 · maxDD -39.0%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1050 trades · win 36% · PF 0.94 · expectancy -1.67 ticks (-0.04R) · PnL $-4473 · maxDD -31.0%
- **OOS**: 771 trades · win 33% · PF 0.85 · expectancy -5.94 ticks (-0.10R) · PnL $-8057 · maxDD -36.8%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 308 trades · win 18% · PF 1.38 · expectancy 7.74 ticks (0.32R) · PnL $12116 · maxDD -16.6%
- **OOS**: 177 trades · win 13% · PF 0.91 · expectancy -5.41 ticks (-0.05R) · PnL $-1554 · maxDD -16.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.77 | -2.84 | -3.55 | -4.27 | -5.62 |
| vwap_reversion | -1.73 | -3.74 | -4.54 | -5.25 | -6.58 |
| momentum_burst | -1.41 | -2.81 | -3.45 | -4.18 | -5.48 |
| session_drift | -9.25 | -10.33 | -10.87 | -11.41 | -13.84 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._