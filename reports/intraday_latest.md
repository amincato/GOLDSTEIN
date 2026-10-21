# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-10-21T10:38:24+00:00 · 5m bars · 487 days (125598 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.1% | 44.3 | 835 |
| london | 20.6% | 41.6 | 863 |
| overlap | 29.6% | 64.2 | 1637 |
| ny | 21.2% | 40.9 | 1016 |
| late | 20.8% | 35.7 | 423 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1245 trades · win 39% · PF 0.86 · expectancy -4.04 ticks (-0.09R) · PnL $-11512 · maxDD -48.7%
- **OOS**: 684 trades · win 42% · PF 0.95 · expectancy -3.64 ticks (-0.02R) · PnL $-2129 · maxDD -19.1%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1565 trades · win 54% · PF 0.84 · expectancy -3.34 ticks (-0.08R) · PnL $-13048 · maxDD -56.4%
- **OOS**: 921 trades · win 53% · PF 0.87 · expectancy -5.72 ticks (-0.08R) · PnL $-6073 · maxDD -28.5%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 966 trades · win 36% · PF 0.95 · expectancy -0.96 ticks (-0.04R) · PnL $-3737 · maxDD -31.0%
- **OOS**: 732 trades · win 33% · PF 0.87 · expectancy -6.18 ticks (-0.08R) · PnL $-6781 · maxDD -33.0%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 290 trades · win 17% · PF 1.39 · expectancy 7.14 ticks (0.34R) · PnL $11802 · maxDD -16.6%
- **OOS**: 170 trades · win 14% · PF 0.91 · expectancy -2.95 ticks (-0.07R) · PnL $-1450 · maxDD -18.4%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -1.06 | -3.06 | -3.78 | -4.44 | -5.90 |
| vwap_reversion | -1.31 | -3.33 | -4.10 | -4.85 | -6.15 |
| momentum_burst | -1.24 | -2.67 | -3.23 | -3.88 | -5.16 |
| session_drift | -7.77 | -8.86 | -9.40 | -9.94 | -12.45 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._