# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-09-23T10:19:14+00:00 · 5m bars · 463 days (120062 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.4% | 44.5 | 856 |
| london | 20.9% | 41.9 | 883 |
| overlap | 29.8% | 64.3 | 1662 |
| ny | 21.5% | 41.2 | 1040 |
| late | 21.3% | 36.4 | 435 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1182 trades · win 40% · PF 0.86 · expectancy -3.08 ticks (-0.09R) · PnL $-10085 · maxDD -48.7%
- **OOS**: 671 trades · win 41% · PF 0.94 · expectancy -4.41 ticks (-0.02R) · PnL $-2853 · maxDD -16.8%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1483 trades · win 54% · PF 0.82 · expectancy -3.63 ticks (-0.08R) · PnL $-13199 · maxDD -56.4%
- **OOS**: 897 trades · win 54% · PF 0.92 · expectancy -4.15 ticks (-0.05R) · PnL $-3747 · maxDD -19.6%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 932 trades · win 36% · PF 0.94 · expectancy -1.12 ticks (-0.04R) · PnL $-3844 · maxDD -31.0%
- **OOS**: 677 trades · win 33% · PF 0.85 · expectancy -6.72 ticks (-0.08R) · PnL $-7203 · maxDD -32.1%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 275 trades · win 17% · PF 1.40 · expectancy 6.13 ticks (0.35R) · PnL $11418 · maxDD -16.6%
- **OOS**: 165 trades · win 15% · PF 0.94 · expectancy -1.24 ticks (-0.08R) · PnL $-956 · maxDD -18.1%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.05 | -2.97 | -3.63 | -4.38 | -5.73 |
| vwap_reversion | -1.12 | -3.20 | -3.98 | -4.77 | -6.07 |
| momentum_burst | -0.98 | -2.43 | -3.00 | -3.65 | -4.88 |
| session_drift | -5.88 | -6.97 | -7.51 | -8.05 | -10.63 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._