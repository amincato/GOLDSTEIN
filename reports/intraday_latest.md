# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-27T11:03:09+00:00 · 5m bars · 492 days (126710 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.1% | 44.3 | 832 |
| london | 20.5% | 41.6 | 861 |
| overlap | 29.5% | 64.2 | 1633 |
| ny | 21.1% | 40.8 | 1011 |
| late | 20.7% | 35.7 | 420 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1260 trades · win 40% · PF 0.87 · expectancy -3.13 ticks (-0.08R) · PnL $-10433 · maxDD -48.7%
- **OOS**: 687 trades · win 41% · PF 0.94 · expectancy -4.24 ticks (-0.03R) · PnL $-2746 · maxDD -18.1%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1583 trades · win 55% · PF 0.84 · expectancy -3.03 ticks (-0.07R) · PnL $-12647 · maxDD -56.4%
- **OOS**: 921 trades · win 53% · PF 0.85 · expectancy -6.60 ticks (-0.09R) · PnL $-6897 · maxDD -29.2%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 978 trades · win 36% · PF 0.95 · expectancy -0.57 ticks (-0.04R) · PnL $-3441 · maxDD -31.0%
- **OOS**: 741 trades · win 33% · PF 0.86 · expectancy -6.21 ticks (-0.08R) · PnL $-7080 · maxDD -33.8%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 293 trades · win 17% · PF 1.40 · expectancy 8.95 ticks (0.34R) · PnL $12354 · maxDD -16.6%
- **OOS**: 171 trades · win 12% · PF 0.78 · expectancy -11.88 ticks (-0.19R) · PnL $-3646 · maxDD -19.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.13 | -3.03 | -3.74 | -4.43 | -5.80 |
| vwap_reversion | -1.44 | -3.41 | -4.22 | -4.94 | -6.23 |
| momentum_burst | -1.39 | -2.81 | -3.37 | -4.02 | -5.25 |
| session_drift | -8.45 | -9.53 | -10.07 | -10.61 | -13.11 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._