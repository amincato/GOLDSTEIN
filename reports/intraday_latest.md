# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-23T10:33:33+00:00 · 5m bars · 489 days (126150 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.1% | 44.3 | 834 |
| london | 20.6% | 41.6 | 862 |
| overlap | 29.5% | 64.2 | 1635 |
| ny | 21.2% | 40.9 | 1014 |
| late | 20.8% | 35.7 | 422 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1250 trades · win 39% · PF 0.86 · expectancy -3.84 ticks (-0.09R) · PnL $-11293 · maxDD -48.7%
- **OOS**: 685 trades · win 41% · PF 0.94 · expectancy -4.39 ticks (-0.03R) · PnL $-2824 · maxDD -20.2%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1571 trades · win 54% · PF 0.84 · expectancy -3.20 ticks (-0.08R) · PnL $-12847 · maxDD -56.4%
- **OOS**: 923 trades · win 53% · PF 0.86 · expectancy -5.98 ticks (-0.08R) · PnL $-6506 · maxDD -28.8%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 971 trades · win 36% · PF 0.95 · expectancy -0.87 ticks (-0.04R) · PnL $-3648 · maxDD -31.0%
- **OOS**: 736 trades · win 33% · PF 0.86 · expectancy -6.57 ticks (-0.08R) · PnL $-7215 · maxDD -33.2%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 291 trades · win 17% · PF 1.38 · expectancy 6.86 ticks (0.33R) · PnL $11727 · maxDD -16.6%
- **OOS**: 171 trades · win 13% · PF 0.85 · expectancy -7.65 ticks (-0.11R) · PnL $-2351 · maxDD -18.9%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.07 | -3.07 | -3.79 | -4.45 | -5.90 |
| vwap_reversion | -1.31 | -3.32 | -4.09 | -4.85 | -6.14 |
| momentum_burst | -1.34 | -2.76 | -3.33 | -3.98 | -5.24 |
| session_drift | -8.04 | -9.12 | -9.66 | -10.20 | -12.70 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._