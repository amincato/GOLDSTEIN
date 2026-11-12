# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-12T14:01:26+00:00 · 5m bars · 506 days (130052 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.1% | 44.5 | 822 |
| london | 20.4% | 41.5 | 851 |
| overlap | 29.5% | 64.1 | 1621 |
| ny | 21.1% | 40.8 | 1004 |
| late | 20.6% | 35.6 | 415 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1350 trades · win 35% · PF 0.90 · expectancy -1.16 ticks (-0.08R) · PnL $-10279 · maxDD -58.6%
- **OOS**: 742 trades · win 35% · PF 0.92 · expectancy -6.02 ticks (-0.04R) · PnL $-3956 · maxDD -20.3%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1631 trades · win 55% · PF 0.85 · expectancy -2.85 ticks (-0.07R) · PnL $-12555 · maxDD -56.4%
- **OOS**: 937 trades · win 52% · PF 0.82 · expectancy -8.07 ticks (-0.11R) · PnL $-8612 · maxDD -35.7%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1019 trades · win 36% · PF 0.95 · expectancy -1.31 ticks (-0.04R) · PnL $-3950 · maxDD -31.0%
- **OOS**: 763 trades · win 33% · PF 0.86 · expectancy -6.18 ticks (-0.09R) · PnL $-7753 · maxDD -32.1%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 301 trades · win 18% · PF 1.40 · expectancy 9.02 ticks (0.34R) · PnL $12446 · maxDD -16.6%
- **OOS**: 175 trades · win 13% · PF 0.87 · expectancy -6.30 ticks (-0.09R) · PnL $-2096 · maxDD -17.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.85 | -2.83 | -3.54 | -4.22 | -5.52 |
| vwap_reversion | -1.62 | -3.60 | -4.40 | -5.12 | -6.45 |
| momentum_burst | -1.38 | -2.79 | -3.35 | -4.00 | -5.21 |
| session_drift | -8.23 | -9.31 | -9.85 | -10.39 | -12.84 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._