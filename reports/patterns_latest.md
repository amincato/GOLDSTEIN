# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 769 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 20 | 622 | +2.01 | +5.1% | +2.10 | 53% |
| 23 | 623 | +2.70 | +6.8% | +2.07 | 54% |
| 07 | 625 | +2.01 | +5.1% | +1.79 | 51% |
| 11 | 625 | +1.87 | +4.7% | +1.77 | 54% |
| 04 | 623 | +1.00 | +2.5% | +1.51 | 48% |
| 05 | 628 | -1.79 | -4.5% | -1.47 | 52% |
| 02 | 623 | -1.52 | -3.8% | -1.36 | 48% |
| 06 | 633 | +1.39 | +3.5% | +1.33 | 53% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 129 | +19.8 | +1.81 | 57% |
| Tue | 130 | +9.8 | +0.78 | 57% |
| Wed | 128 | +19.8 | +1.57 | 55% |
| Thu | 128 | +9.2 | +0.71 | 50% |
| Fri | 128 | +2.9 | +0.20 | 54% |

## Reality check (multiple-testing control)
- Best hour: **20 UTC** (t = +2.10)
- Familywise |t| threshold at 5%: 3.22
- Reality-check p-value for the best pattern: **0.612**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._