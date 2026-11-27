# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-27T15:38:55+00:00 · 5m bars · 519 days (132723 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.2% | 44.9 | 817 |
| london | 20.4% | 41.6 | 845 |
| overlap | 29.6% | 64.3 | 1619 |
| ny | 21.1% | 41.1 | 1001 |
| late | 21.2% | 35.9 | 414 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1390 trades · win 35% · PF 0.91 · expectancy -0.65 ticks (-0.07R) · PnL $-9614 · maxDD -58.6%
- **OOS**: 739 trades · win 35% · PF 0.90 · expectancy -6.60 ticks (-0.06R) · PnL $-4902 · maxDD -22.0%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1674 trades · win 54% · PF 0.84 · expectancy -3.12 ticks (-0.07R) · PnL $-13131 · maxDD -56.4%
- **OOS**: 947 trades · win 52% · PF 0.82 · expectancy -7.69 ticks (-0.10R) · PnL $-8504 · maxDD -37.8%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1053 trades · win 36% · PF 0.94 · expectancy -1.85 ticks (-0.04R) · PnL $-4803 · maxDD -31.0%
- **OOS**: 772 trades · win 33% · PF 0.88 · expectancy -5.06 ticks (-0.08R) · PnL $-6557 · maxDD -31.2%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 309 trades · win 17% · PF 1.38 · expectancy 7.44 ticks (0.31R) · PnL $12029 · maxDD -16.6%
- **OOS**: 177 trades · win 13% · PF 0.91 · expectancy -5.48 ticks (-0.04R) · PnL $-1502 · maxDD -15.6%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.82 | -2.99 | -3.70 | -4.36 | -5.80 |
| vwap_reversion | -1.67 | -3.63 | -4.42 | -5.17 | -6.50 |
| momentum_burst | -0.87 | -2.27 | -2.90 | -3.74 | -5.21 |
| session_drift | -9.03 | -10.11 | -10.65 | -11.19 | -13.62 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._