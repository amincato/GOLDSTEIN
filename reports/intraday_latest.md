# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-04T13:19:08+00:00 · 5m bars · 499 days (128385 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.1% | 44.4 | 827 |
| london | 20.5% | 41.6 | 855 |
| overlap | 29.5% | 64.1 | 1627 |
| ny | 21.1% | 40.8 | 1007 |
| late | 20.7% | 35.6 | 418 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1284 trades · win 40% · PF 0.87 · expectancy -3.28 ticks (-0.08R) · PnL $-10831 · maxDD -48.7%
- **OOS**: 687 trades · win 42% · PF 0.97 · expectancy -2.91 ticks (-0.01R) · PnL $-1445 · maxDD -17.7%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1607 trades · win 55% · PF 0.85 · expectancy -2.76 ticks (-0.07R) · PnL $-12280 · maxDD -56.4%
- **OOS**: 929 trades · win 52% · PF 0.82 · expectancy -7.78 ticks (-0.10R) · PnL $-8248 · maxDD -33.6%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 999 trades · win 36% · PF 0.95 · expectancy -0.88 ticks (-0.04R) · PnL $-3889 · maxDD -31.0%
- **OOS**: 747 trades · win 33% · PF 0.86 · expectancy -6.18 ticks (-0.08R) · PnL $-7347 · maxDD -33.5%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 297 trades · win 18% · PF 1.40 · expectancy 9.03 ticks (0.34R) · PnL $12412 · maxDD -16.6%
- **OOS**: 173 trades · win 12% · PF 0.74 · expectancy -13.74 ticks (-0.22R) · PnL $-4340 · maxDD -18.9%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.81 | -2.81 | -3.53 | -4.21 | -5.51 |
| vwap_reversion | -1.56 | -3.56 | -4.36 | -5.08 | -6.42 |
| momentum_burst | -1.13 | -2.54 | -3.10 | -3.75 | -4.97 |
| session_drift | -7.66 | -8.74 | -9.28 | -9.82 | -12.30 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._