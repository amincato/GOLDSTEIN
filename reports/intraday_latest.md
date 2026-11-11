# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-11T12:59:43+00:00 · 5m bars · 505 days (129764 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.0% | 44.5 | 823 |
| london | 20.4% | 41.5 | 851 |
| overlap | 29.4% | 64.1 | 1623 |
| ny | 21.0% | 40.9 | 1005 |
| late | 20.6% | 35.6 | 416 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1350 trades · win 35% · PF 0.90 · expectancy -1.16 ticks (-0.08R) · PnL $-10279 · maxDD -58.6%
- **OOS**: 732 trades · win 35% · PF 0.91 · expectancy -6.37 ticks (-0.05R) · PnL $-4275 · maxDD -20.3%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1631 trades · win 55% · PF 0.85 · expectancy -2.85 ticks (-0.07R) · PnL $-12555 · maxDD -56.4%
- **OOS**: 933 trades · win 52% · PF 0.83 · expectancy -7.72 ticks (-0.10R) · PnL $-8161 · maxDD -34.4%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1019 trades · win 36% · PF 0.95 · expectancy -1.31 ticks (-0.04R) · PnL $-3950 · maxDD -31.0%
- **OOS**: 755 trades · win 33% · PF 0.85 · expectancy -6.21 ticks (-0.09R) · PnL $-7871 · maxDD -32.1%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 301 trades · win 18% · PF 1.40 · expectancy 9.02 ticks (0.34R) · PnL $12446 · maxDD -16.6%
- **OOS**: 174 trades · win 13% · PF 0.88 · expectancy -6.04 ticks (-0.09R) · PnL $-1990 · maxDD -17.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.98 | -2.96 | -3.67 | -4.35 | -5.65 |
| vwap_reversion | -1.51 | -3.49 | -4.30 | -5.02 | -6.35 |
| momentum_burst | -1.35 | -2.76 | -3.32 | -3.97 | -5.18 |
| session_drift | -8.08 | -9.16 | -9.70 | -10.24 | -12.70 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._