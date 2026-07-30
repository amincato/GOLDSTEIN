# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-07-30T23:17:07+00:00 · 5m bars · 61 days (13795 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 20.9% | 54.6 | 300 |
| london | 20.1% | 51.2 | 405 |
| overlap | 30.8% | 80.5 | 1066 |
| ny | 21.8% | 45.6 | 470 |
| late | 23.6% | 42.8 | 175 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 0.8, 'target_atr': 1.2}`
- **IS**: 152 trades · win 45% · PF 1.11 · expectancy 1.73 ticks (0.06R) · PnL $931 · maxDD -3.1%
- **OOS**: 92 trades · win 39% · PF 0.85 · expectancy -6.52 ticks (-0.09R) · PnL $-836 · maxDD -3.8%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 162 trades · win 52% · PF 0.76 · expectancy -13.05 ticks (-0.08R) · PnL $-1897 · maxDD -9.6%
- **OOS**: 103 trades · win 59% · PF 1.15 · expectancy 7.92 ticks (0.04R) · PnL $615 · maxDD -3.4%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 0.8, 'target_atr': 1.6}`
- **IS**: 150 trades · win 41% · PF 1.15 · expectancy 4.06 ticks (0.12R) · PnL $1514 · maxDD -8.2%
- **OOS**: 97 trades · win 37% · PF 1.07 · expectancy 1.16 ticks (0.01R) · PnL $455 · maxDD -7.7%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -4.17 | -6.57 | -7.08 | -6.59 | -7.61 |
| vwap_reversion | -0.79 | -2.09 | -2.60 | -3.60 | -5.11 |
| momentum_burst | -0.15 | -2.10 | -2.60 | -3.34 | -5.06 |

## Verdict
- OOS survivors at realistic costs: **vwap_reversion**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._