# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-05T13:31:55+00:00 · 5m bars · 500 days (128665 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.1% | 44.4 | 827 |
| london | 20.5% | 41.6 | 853 |
| overlap | 29.5% | 64.1 | 1626 |
| ny | 21.1% | 40.8 | 1007 |
| late | 20.6% | 35.6 | 418 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1288 trades · win 40% · PF 0.87 · expectancy -3.28 ticks (-0.08R) · PnL $-10838 · maxDD -48.7%
- **OOS**: 686 trades · win 41% · PF 0.94 · expectancy -4.49 ticks (-0.02R) · PnL $-2466 · maxDD -20.9%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1613 trades · win 55% · PF 0.85 · expectancy -2.88 ticks (-0.07R) · PnL $-12495 · maxDD -56.4%
- **OOS**: 930 trades · win 52% · PF 0.84 · expectancy -6.94 ticks (-0.09R) · PnL $-7578 · maxDD -31.7%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 1005 trades · win 36% · PF 0.95 · expectancy -0.99 ticks (-0.04R) · PnL $-3860 · maxDD -31.0%
- **OOS**: 747 trades · win 33% · PF 0.87 · expectancy -6.19 ticks (-0.08R) · PnL $-6955 · maxDD -32.4%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 298 trades · win 18% · PF 1.41 · expectancy 9.99 ticks (0.35R) · PnL $12708 · maxDD -16.6%
- **OOS**: 173 trades · win 13% · PF 0.86 · expectancy -7.58 ticks (-0.09R) · PnL $-2230 · maxDD -18.6%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.89 | -2.91 | -3.62 | -4.28 | -5.72 |
| vwap_reversion | -1.38 | -3.37 | -4.17 | -4.92 | -6.26 |
| momentum_burst | -0.92 | -2.34 | -2.90 | -3.55 | -4.94 |
| session_drift | -7.53 | -8.61 | -9.15 | -9.69 | -12.16 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._