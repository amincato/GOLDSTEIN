# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 803 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 20 | 651 | +1.88 | +4.7% | +2.04 | 53% |
| 23 | 651 | +2.54 | +6.4% | +2.03 | 54% |
| 11 | 661 | +1.98 | +5.0% | +1.93 | 53% |
| 07 | 654 | +1.71 | +4.3% | +1.57 | 51% |
| 04 | 652 | +1.01 | +2.5% | +1.55 | 48% |
| 05 | 657 | -1.80 | -4.5% | -1.52 | 52% |
| 06 | 662 | +1.45 | +3.6% | +1.43 | 53% |
| 15 | 659 | -1.81 | -4.6% | -1.17 | 51% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 134 | +15.3 | +1.40 | 55% |
| Tue | 136 | +9.1 | +0.75 | 56% |
| Wed | 134 | +15.6 | +1.27 | 53% |
| Thu | 134 | +10.1 | +0.81 | 51% |
| Fri | 134 | +4.4 | +0.32 | 55% |

## Reality check (multiple-testing control)
- Best hour: **20 UTC** (t = +2.04)
- Familywise |t| threshold at 5%: 3.01
- Reality-check p-value for the best pattern: **0.654**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._