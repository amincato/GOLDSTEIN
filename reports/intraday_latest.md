# GOLDSTEIN — Intraday Scalping Validation
_Generated 2026-11-02T13:53:24+00:00 · 5m bars · 497 days (127838 bars) · contract MGC · data: cache_

## Session profile (when the market pays)
| Session | ann. vol | avg range (ticks) | avg volume |
|---|---|---|---|
| asia | 23.0% | 44.3 | 828 |
| london | 20.5% | 41.6 | 856 |
| overlap | 29.5% | 64.1 | 1628 |
| ny | 21.1% | 40.9 | 1009 |
| late | 20.7% | 35.6 | 419 |

## Walk-forward (params chosen in-sample, judged out-of-sample)
### orb
- params: `{'stop_atr': 1.3, 'target_atr': 2.0}`
- **IS**: 1278 trades · win 40% · PF 0.87 · expectancy -3.18 ticks (-0.08R) · PnL $-10549 · maxDD -48.7%
- **OOS**: 685 trades · win 41% · PF 0.93 · expectancy -4.53 ticks (-0.03R) · PnL $-2855 · maxDD -21.2%

### vwap_reversion
- params: `{'z_entry': 1.8, 'stop_atr': 1.5, 'target_atr': 1.2}`
- **IS**: 1601 trades · win 55% · PF 0.84 · expectancy -2.92 ticks (-0.07R) · PnL $-12515 · maxDD -56.4%
- **OOS**: 926 trades · win 52% · PF 0.84 · expectancy -6.98 ticks (-0.09R) · PnL $-7522 · maxDD -31.3%

### momentum_burst
- params: `{'range_trigger': 1.8, 'stop_atr': 1.0, 'target_atr': 2.0}`
- **IS**: 993 trades · win 36% · PF 0.95 · expectancy -0.87 ticks (-0.04R) · PnL $-3922 · maxDD -31.0%
- **OOS**: 745 trades · win 33% · PF 0.86 · expectancy -6.66 ticks (-0.09R) · PnL $-7496 · maxDD -32.3%

### session_drift
- params: `{'entry_hour': 0, 'direction': 1}`
- **IS**: 296 trades · win 18% · PF 1.40 · expectancy 9.37 ticks (0.35R) · PnL $12505 · maxDD -16.6%
- **OOS**: 172 trades · win 13% · PF 0.82 · expectancy -9.27 ticks (-0.15R) · PnL $-2980 · maxDD -18.9%

## Cost sensitivity (expectancy in ticks vs spread)
| Strategy | 0.0 | 1.0 | 1.5 | 2.0 | 3.0 ticks |
|---|---|---|---|---|---|
| orb | -0.83 | -2.93 | -3.65 | -4.30 | -5.74 |
| vwap_reversion | -1.51 | -3.50 | -4.27 | -5.02 | -6.33 |
| momentum_burst | -0.99 | -2.41 | -2.97 | -3.62 | -5.02 |
| session_drift | -7.24 | -8.33 | -8.87 | -9.41 | -11.89 |

## Verdict
- **No strategy survives out-of-sample at realistic costs on this sample.** That is a result, not a failure of the tool: do not scalp this market with these setups until an edge shows up.

---
_Research tooling, not investment advice. Intraday leverage on futures can lose more than the margin posted._