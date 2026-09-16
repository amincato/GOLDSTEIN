# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-16T10:20:44+00:00 · 5m bars · 457 days (118680 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.5% | 44.4 | 861 |
| london | 20.9% | 41.9 | 888 |
| overlap | 29.8% | 64.3 | 1669 |
| ny | 21.4% | 41.1 | 1043 |
| late | 21.3% | 36.5 | 437 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1166 trades · win 40% · PF 0.87 · expectancy -2.80 ticks (-0.08R) · PnL $-9605 · maxDD -48.7%
- **OOS**: 677 trades · win 41% · PF 0.93 · expectancy -4.70 ticks (-0.02R) · PnL $-3280 · maxDD -16.8%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1466 trades · win 54% · PF 0.81 · expectancy -3.98 ticks (-0.09R) · PnL $-13652 · maxDD -56.4%
- **OOS**: 890 trades · win 55% · PF 0.93 · expectancy -3.50 ticks (-0.04R) · PnL $-3022 · maxDD -19.2%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 917 trades · win 36% · PF 0.94 · expectancy -1.01 ticks (-0.04R) · PnL $-3927 · maxDD -31.0%
- **OOS**: 663 trades · win 33% · PF 0.85 · expectancy -7.00 ticks (-0.09R) · PnL $-7117 · maxDD -32.0%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 272 trades · win 17% · PF 1.40 · expectancy 5.10 ticks (0.35R) · PnL $11118 · maxDD -16.6%
- **OOS**: 163 trades · win 14% · PF 0.92 · expectancy -4.47 ticks (-0.10R) · PnL $-1271 · maxDD -18.3%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.97 | -2.89 | -3.56 | -4.31 | -5.66 |
| vwap_reversion | -1.12 | -3.17 | -4.00 | -4.79 | -6.10 |
| momentum_burst | -0.97 | -2.43 | -3.00 | -3.66 | -4.89 |
| session_drift | -5.75 | -6.83 | -7.37 | -7.91 | -10.51 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._