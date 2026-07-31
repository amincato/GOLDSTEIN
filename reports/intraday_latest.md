# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-07-31T08:23:06+00:00 · 5m bars · 419 days (109871 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.9% | 44.0 | 896 |
| london | 21.4% | 41.8 | 924 |
| overlap | 29.7% | 63.1 | 1693 |
| ny | 21.9% | 41.2 | 1085 |
| late | 21.8% | 36.8 | 457 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1056 trades · win 39% · PF 0.84 · expectancy -3.93 ticks (-0.11R) · PnL $-10704 · maxDD -48.7%
- **OOS**: 643 trades · win 43% · PF 1.00 · expectancy -0.32 ticks (0.02R) · PnL $-97 · maxDD -10.5%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1352 trades · win 54% · PF 0.81 · expectancy -3.71 ticks (-0.09R) · PnL $-12410 · maxDD -53.9%
- **OOS**: 840 trades · win 55% · PF 0.94 · expectancy -3.00 ticks (-0.03R) · PnL $-2613 · maxDD -13.9%

### momentum_burst
- params: `{'range_trigger': 2.2, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 676 trades · win 36% · PF 0.95 · expectancy -2.56 ticks (-0.05R) · PnL $-2536 · maxDD -15.3%
- **OOS**: 479 trades · win 33% · PF 0.85 · expectancy -10.05 ticks (-0.08R) · PnL $-5142 · maxDD -28.6%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 251 trades · win 15% · PF 1.19 · expectancy -4.09 ticks (0.16R) · PnL $5156 · maxDD -16.6%
- **OOS**: 153 trades · win 18% · PF 1.07 · expectancy 6.24 ticks (0.03R) · PnL $993 · maxDD -15.9%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.51 | -2.33 | -2.98 | -3.66 | -5.03 |
| vwap_reversion | -0.97 | -3.01 | -3.81 | -4.50 | -5.83 |
| momentum_burst | -0.55 | -2.06 | -2.64 | -3.32 | -4.39 |
| session_drift | -9.02 | -10.10 | -10.64 | -11.18 | -13.90 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._