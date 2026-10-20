# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-20T10:27:59+00:00 · 5m bars · 486 days (125320 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.1% | 44.3 | 836 |
| london | 20.6% | 41.7 | 866 |
| overlap | 29.6% | 64.2 | 1638 |
| ny | 21.2% | 41.0 | 1017 |
| late | 20.8% | 35.8 | 423 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1241 trades · win 39% · PF 0.86 · expectancy -4.13 ticks (-0.09R) · PnL $-11633 · maxDD -48.7%
- **OOS**: 686 trades · win 42% · PF 0.97 · expectancy -2.11 ticks (-0.01R) · PnL $-1189 · maxDD -16.3%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1559 trades · win 54% · PF 0.83 · expectancy -3.46 ticks (-0.08R) · PnL $-13213 · maxDD -56.4%
- **OOS**: 920 trades · win 53% · PF 0.87 · expectancy -5.67 ticks (-0.08R) · PnL $-6020 · maxDD -27.4%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 963 trades · win 36% · PF 0.95 · expectancy -1.03 ticks (-0.04R) · PnL $-3857 · maxDD -31.0%
- **OOS**: 731 trades · win 34% · PF 0.87 · expectancy -5.90 ticks (-0.07R) · PnL $-6793 · maxDD -34.7%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 289 trades · win 17% · PF 1.39 · expectancy 7.44 ticks (0.34R) · PnL $11882 · maxDD -16.6%
- **OOS**: 170 trades · win 14% · PF 0.86 · expectancy -5.46 ticks (-0.12R) · PnL $-2162 · maxDD -18.4%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.21 | -3.11 | -3.83 | -4.51 | -5.89 |
| vwap_reversion | -1.39 | -3.37 | -4.18 | -4.89 | -6.20 |
| momentum_burst | -1.26 | -2.69 | -3.26 | -3.91 | -5.15 |
| session_drift | -7.92 | -9.00 | -9.54 | -10.08 | -12.60 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._