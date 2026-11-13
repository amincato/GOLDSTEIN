# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-13T13:28:24+00:00 · 5m bars · 507 days (130324 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.1% | 44.5 | 821 |
| london | 20.4% | 41.5 | 850 |
| overlap | 29.5% | 64.1 | 1621 |
| ny | 21.0% | 40.8 | 1004 |
| late | 20.6% | 35.6 | 415 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1356 trades · win 35% · PF 0.90 · expectancy -1.19 ticks (-0.08R) · PnL $-10327 · maxDD -58.6%
- **OOS**: 737 trades · win 35% · PF 0.93 · expectancy -5.45 ticks (-0.04R) · PnL $-3468 · maxDD -20.7%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1637 trades · win 55% · PF 0.85 · expectancy -2.58 ticks (-0.07R) · PnL $-12126 · maxDD -56.4%
- **OOS**: 939 trades · win 52% · PF 0.81 · expectancy -8.39 ticks (-0.11R) · PnL $-9120 · maxDD -36.6%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1022 trades · win 36% · PF 0.95 · expectancy -1.46 ticks (-0.04R) · PnL $-4106 · maxDD -31.0%
- **OOS**: 759 trades · win 33% · PF 0.88 · expectancy -5.54 ticks (-0.08R) · PnL $-6649 · maxDD -30.7%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 302 trades · win 18% · PF 1.39 · expectancy 8.50 ticks (0.33R) · PnL $12299 · maxDD -16.6%
- **OOS**: 175 trades · win 14% · PF 0.95 · expectancy -2.45 ticks (-0.01R) · PnL $-794 · maxDD -16.8%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.81 | -2.91 | -3.62 | -4.29 | -5.72 |
| vwap_reversion | -1.55 | -3.52 | -4.33 | -5.08 | -6.41 |
| momentum_burst | -1.01 | -2.42 | -2.98 | -3.73 | -5.12 |
| session_drift | -8.09 | -9.17 | -9.71 | -10.25 | -12.71 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._