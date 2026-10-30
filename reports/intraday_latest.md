# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-30T11:41:53+00:00 · 5m bars · 495 days (127546 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.0% | 44.3 | 829 |
| london | 20.5% | 41.6 | 858 |
| overlap | 29.5% | 64.1 | 1628 |
| ny | 21.1% | 40.9 | 1009 |
| late | 20.7% | 35.6 | 418 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1272 trades · win 40% · PF 0.87 · expectancy -3.10 ticks (-0.08R) · PnL $-10434 · maxDD -48.7%
- **OOS**: 683 trades · win 41% · PF 0.94 · expectancy -3.99 ticks (-0.03R) · PnL $-2507 · maxDD -18.0%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1595 trades · win 55% · PF 0.84 · expectancy -3.01 ticks (-0.07R) · PnL $-12637 · maxDD -56.4%
- **OOS**: 925 trades · win 53% · PF 0.85 · expectancy -6.62 ticks (-0.09R) · PnL $-7018 · maxDD -30.0%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 990 trades · win 36% · PF 0.95 · expectancy -0.66 ticks (-0.04R) · PnL $-3649 · maxDD -31.0%
- **OOS**: 745 trades · win 33% · PF 0.85 · expectancy -6.54 ticks (-0.09R) · PnL $-7712 · maxDD -33.8%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 295 trades · win 18% · PF 1.41 · expectancy 9.75 ticks (0.35R) · PnL $12608 · maxDD -16.6%
- **OOS**: 172 trades · win 12% · PF 0.77 · expectancy -11.61 ticks (-0.20R) · PnL $-3815 · maxDD -18.9%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.08 | -3.09 | -3.80 | -4.49 | -5.79 |
| vwap_reversion | -1.43 | -3.43 | -4.24 | -4.96 | -6.25 |
| momentum_burst | -1.24 | -2.66 | -3.22 | -3.87 | -5.09 |
| session_drift | -7.25 | -8.33 | -8.87 | -9.41 | -11.90 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._