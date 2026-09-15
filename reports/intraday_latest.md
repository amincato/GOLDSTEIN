# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-15T10:30:19+00:00 · 5m bars · 456 days (118405 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.5% | 44.4 | 862 |
| london | 20.9% | 41.9 | 889 |
| overlap | 29.8% | 64.3 | 1671 |
| ny | 21.5% | 41.1 | 1045 |
| late | 21.4% | 36.5 | 437 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1160 trades · win 40% · PF 0.88 · expectancy -2.40 ticks (-0.08R) · PnL $-9123 · maxDD -48.7%
- **OOS**: 679 trades · win 41% · PF 0.92 · expectancy -5.33 ticks (-0.03R) · PnL $-3717 · maxDD -17.0%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1461 trades · win 54% · PF 0.81 · expectancy -3.86 ticks (-0.09R) · PnL $-13453 · maxDD -56.4%
- **OOS**: 890 trades · win 54% · PF 0.93 · expectancy -3.86 ticks (-0.05R) · PnL $-3409 · maxDD -19.4%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 914 trades · win 36% · PF 0.95 · expectancy -0.70 ticks (-0.04R) · PnL $-3642 · maxDD -31.0%
- **OOS**: 662 trades · win 33% · PF 0.85 · expectancy -7.23 ticks (-0.09R) · PnL $-7125 · maxDD -32.4%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 271 trades · win 17% · PF 1.35 · expectancy 2.48 ticks (0.31R) · PnL $9690 · maxDD -16.6%
- **OOS**: 163 trades · win 15% · PF 0.96 · expectancy -1.22 ticks (-0.07R) · PnL $-693 · maxDD -18.0%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.96 | -2.88 | -3.51 | -4.27 | -5.62 |
| vwap_reversion | -1.21 | -3.30 | -4.08 | -4.88 | -6.19 |
| momentum_burst | -0.83 | -2.29 | -2.86 | -3.52 | -4.76 |
| session_drift | -5.63 | -6.72 | -7.26 | -7.80 | -10.40 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._