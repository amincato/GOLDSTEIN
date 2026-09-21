# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-21T11:09:17+00:00 · 5m bars · 461 days (119518 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.4% | 44.5 | 858 |
| london | 20.9% | 41.9 | 885 |
| overlap | 29.8% | 64.3 | 1665 |
| ny | 21.6% | 41.3 | 1042 |
| late | 21.3% | 36.4 | 436 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1176 trades · win 40% · PF 0.87 · expectancy -2.94 ticks (-0.09R) · PnL $-9902 · maxDD -48.7%
- **OOS**: 674 trades · win 41% · PF 0.93 · expectancy -4.68 ticks (-0.02R) · PnL $-3048 · maxDD -16.9%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1477 trades · win 54% · PF 0.81 · expectancy -3.95 ticks (-0.09R) · PnL $-13654 · maxDD -56.4%
- **OOS**: 896 trades · win 54% · PF 0.93 · expectancy -3.74 ticks (-0.05R) · PnL $-3327 · maxDD -19.2%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 929 trades · win 36% · PF 0.95 · expectancy -0.88 ticks (-0.04R) · PnL $-3560 · maxDD -31.0%
- **OOS**: 668 trades · win 33% · PF 0.85 · expectancy -6.70 ticks (-0.08R) · PnL $-6914 · maxDD -32.5%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 274 trades · win 17% · PF 1.41 · expectancy 6.40 ticks (0.36R) · PnL $11485 · maxDD -16.6%
- **OOS**: 164 trades · win 15% · PF 0.94 · expectancy -1.55 ticks (-0.07R) · PnL $-896 · maxDD -18.2%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.07 | -2.99 | -3.65 | -4.40 | -5.75 |
| vwap_reversion | -1.25 | -3.33 | -4.11 | -4.91 | -6.21 |
| momentum_burst | -0.86 | -2.32 | -2.89 | -3.55 | -4.78 |
| session_drift | -5.57 | -6.65 | -7.19 | -7.73 | -10.32 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._