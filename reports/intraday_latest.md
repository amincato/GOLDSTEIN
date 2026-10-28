# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-28T11:41:45+00:00 · 5m bars · 493 days (126995 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.1% | 44.3 | 831 |
| london | 20.5% | 41.6 | 858 |
| overlap | 29.5% | 64.1 | 1632 |
| ny | 21.1% | 40.8 | 1010 |
| late | 20.7% | 35.6 | 420 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1260 trades · win 40% · PF 0.87 · expectancy -3.13 ticks (-0.08R) · PnL $-10433 · maxDD -48.7%
- **OOS**: 692 trades · win 41% · PF 0.92 · expectancy -5.14 ticks (-0.03R) · PnL $-3364 · maxDD -21.2%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1583 trades · win 55% · PF 0.84 · expectancy -3.03 ticks (-0.07R) · PnL $-12647 · maxDD -56.4%
- **OOS**: 928 trades · win 53% · PF 0.85 · expectancy -6.56 ticks (-0.09R) · PnL $-6937 · maxDD -30.6%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 978 trades · win 36% · PF 0.95 · expectancy -0.57 ticks (-0.04R) · PnL $-3441 · maxDD -31.0%
- **OOS**: 750 trades · win 33% · PF 0.87 · expectancy -6.39 ticks (-0.08R) · PnL $-6911 · maxDD -32.9%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 293 trades · win 17% · PF 1.40 · expectancy 8.95 ticks (0.34R) · PnL $12354 · maxDD -16.6%
- **OOS**: 172 trades · win 13% · PF 0.82 · expectancy -9.77 ticks (-0.15R) · PnL $-2958 · maxDD -19.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.95 | -3.06 | -3.78 | -4.44 | -5.88 |
| vwap_reversion | -1.43 | -3.43 | -4.20 | -4.96 | -6.25 |
| momentum_burst | -1.01 | -2.43 | -3.00 | -3.64 | -4.90 |
| session_drift | -7.07 | -8.15 | -8.69 | -9.23 | -11.73 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._