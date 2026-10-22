# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-22T10:41:35+00:00 · 5m bars · 488 days (125875 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.1% | 44.3 | 834 |
| london | 20.6% | 41.6 | 862 |
| overlap | 29.6% | 64.2 | 1636 |
| ny | 21.2% | 40.9 | 1015 |
| late | 20.8% | 35.7 | 422 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1245 trades · win 39% · PF 0.86 · expectancy -4.04 ticks (-0.09R) · PnL $-11512 · maxDD -48.7%
- **OOS**: 687 trades · win 41% · PF 0.94 · expectancy -3.88 ticks (-0.02R) · PnL $-2481 · maxDD -19.6%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1565 trades · win 54% · PF 0.84 · expectancy -3.34 ticks (-0.08R) · PnL $-13048 · maxDD -56.4%
- **OOS**: 925 trades · win 53% · PF 0.87 · expectancy -5.57 ticks (-0.07R) · PnL $-6007 · maxDD -28.5%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 966 trades · win 36% · PF 0.95 · expectancy -0.96 ticks (-0.04R) · PnL $-3737 · maxDD -31.0%
- **OOS**: 738 trades · win 33% · PF 0.87 · expectancy -6.21 ticks (-0.08R) · PnL $-6799 · maxDD -33.0%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 290 trades · win 17% · PF 1.39 · expectancy 7.14 ticks (0.34R) · PnL $11802 · maxDD -16.6%
- **OOS**: 171 trades · win 14% · PF 0.90 · expectancy -3.21 ticks (-0.07R) · PnL $-1544 · maxDD -18.4%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.10 | -3.09 | -3.81 | -4.47 | -5.92 |
| vwap_reversion | -1.29 | -3.30 | -4.07 | -4.83 | -6.12 |
| momentum_burst | -1.31 | -2.74 | -3.30 | -3.95 | -5.21 |
| session_drift | -7.88 | -8.96 | -9.50 | -10.04 | -12.55 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._