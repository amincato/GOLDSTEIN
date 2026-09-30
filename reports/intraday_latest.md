# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-30T11:23:52+00:00 · 5m bars · 469 days (121459 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.3% | 44.5 | 851 |
| london | 20.8% | 41.9 | 879 |
| overlap | 29.7% | 64.3 | 1655 |
| ny | 21.5% | 41.3 | 1035 |
| late | 21.2% | 36.3 | 432 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1202 trades · win 39% · PF 0.85 · expectancy -4.14 ticks (-0.09R) · PnL $-11420 · maxDD -48.7%
- **OOS**: 673 trades · win 42% · PF 0.97 · expectancy -2.54 ticks (-0.01R) · PnL $-1522 · maxDD -16.0%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1507 trades · win 54% · PF 0.81 · expectancy -4.12 ticks (-0.08R) · PnL $-14027 · maxDD -56.4%
- **OOS**: 897 trades · win 54% · PF 0.92 · expectancy -3.96 ticks (-0.06R) · PnL $-3728 · maxDD -21.1%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 934 trades · win 36% · PF 0.94 · expectancy -1.31 ticks (-0.05R) · PnL $-4027 · maxDD -31.0%
- **OOS**: 700 trades · win 33% · PF 0.86 · expectancy -6.31 ticks (-0.08R) · PnL $-7042 · maxDD -31.9%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 279 trades · win 17% · PF 1.36 · expectancy 2.43 ticks (0.33R) · PnL $10410 · maxDD -16.6%
- **OOS**: 166 trades · win 14% · PF 0.99 · expectancy 4.96 ticks (-0.08R) · PnL $-206 · maxDD -17.2%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.07 | -2.98 | -3.70 | -4.45 | -5.80 |
| vwap_reversion | -1.21 | -3.27 | -4.05 | -4.88 | -6.18 |
| momentum_burst | -0.79 | -2.23 | -2.80 | -3.45 | -4.68 |
| session_drift | -6.32 | -7.40 | -7.95 | -8.49 | -11.05 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._