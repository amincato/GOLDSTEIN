# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-07-31T01:03:13+00:00 · 5m bars · 418 days (109761 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.9% | 44.0 | 898 |
| london | 21.4% | 41.8 | 924 |
| overlap | 29.7% | 63.1 | 1693 |
| ny | 21.9% | 41.2 | 1085 |
| late | 21.8% | 36.8 | 458 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1050 trades · win 39% · PF 0.84 · expectancy -4.02 ticks (-0.11R) · PnL $-10791 · maxDD -48.7%
- **OOS**: 649 trades · win 43% · PF 1.00 · expectancy -0.21 ticks (0.02R) · PnL $-10 · maxDD -10.5%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1346 trades · win 54% · PF 0.81 · expectancy -3.79 ticks (-0.09R) · PnL $-12668 · maxDD -53.9%
- **OOS**: 845 trades · win 56% · PF 0.95 · expectancy -2.82 ticks (-0.03R) · PnL $-2243 · maxDD -13.8%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 674 trades · win 36% · PF 0.95 · expectancy -2.45 ticks (-0.04R) · PnL $-2336 · maxDD -15.3%
- **OOS**: 481 trades · win 33% · PF 0.84 · expectancy -10.18 ticks (-0.09R) · PnL $-5342 · maxDD -28.8%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 250 trades · win 15% · PF 1.20 · expectancy -3.95 ticks (0.16R) · PnL $5274 · maxDD -16.6%
- **OOS**: 153 trades · win 18% · PF 1.25 · expectancy 10.72 ticks (0.18R) · PnL $3639 · maxDD -14.7%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.51 | -2.33 | -2.98 | -3.66 | -5.03 |
| vwap_reversion | -0.95 | -2.99 | -3.79 | -4.48 | -5.81 |
| momentum_burst | -0.55 | -2.06 | -2.64 | -3.32 | -4.39 |
| session_drift | -9.02 | -10.10 | -10.64 | -11.18 | -13.90 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._