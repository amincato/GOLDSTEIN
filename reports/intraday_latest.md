# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-08-26T06:20:16+00:00 · 5m bars · 441 days (114820 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.6% | 44.3 | 875 |
| london | 21.1% | 41.8 | 903 |
| overlap | 29.6% | 63.6 | 1674 |
| ny | 21.6% | 41.1 | 1059 |
| late | 21.5% | 36.6 | 445 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1113 trades · win 39% · PF 0.86 · expectancy -2.89 ticks (-0.09R) · PnL $-9937 · maxDD -48.7%
- **OOS**: 661 trades · win 42% · PF 0.97 · expectancy -2.51 ticks (-0.01R) · PnL $-1369 · maxDD -10.9%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1410 trades · win 54% · PF 0.80 · expectancy -4.46 ticks (-0.09R) · PnL $-14208 · maxDD -56.4%
- **OOS**: 877 trades · win 56% · PF 0.95 · expectancy -2.61 ticks (-0.03R) · PnL $-2067 · maxDD -15.5%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 705 trades · win 36% · PF 0.94 · expectancy -2.83 ticks (-0.05R) · PnL $-3058 · maxDD -15.3%
- **OOS**: 530 trades · win 33% · PF 0.83 · expectancy -10.28 ticks (-0.10R) · PnL $-6362 · maxDD -28.4%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 262 trades · win 16% · PF 1.33 · expectancy 1.18 ticks (0.29R) · PnL $8879 · maxDD -16.6%
- **OOS**: 160 trades · win 17% · PF 1.22 · expectancy 12.43 ticks (0.16R) · PnL $3333 · maxDD -16.5%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.29 | -2.13 | -2.77 | -3.44 | -4.80 |
| vwap_reversion | -0.89 | -2.96 | -3.75 | -4.45 | -5.77 |
| momentum_burst | -0.79 | -2.27 | -2.84 | -3.51 | -4.94 |
| session_drift | -6.27 | -7.36 | -7.90 | -8.44 | -11.09 |

## Verdict
- OOS survivors at realistic costs: **session_drift**

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._