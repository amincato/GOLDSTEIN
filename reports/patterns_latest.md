# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 757 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 20 | 612 | +2.12 | +5.4% | +2.19 | 53% |
| 23 | 613 | +2.70 | +6.8% | +2.04 | 54% |
| 07 | 614 | +2.07 | +5.2% | +1.82 | 51% |
| 05 | 617 | -1.93 | -4.9% | -1.57 | 52% |
| 11 | 614 | +1.66 | +4.2% | +1.55 | 53% |
| 04 | 613 | +1.04 | +2.6% | +1.55 | 48% |
| 02 | 613 | -1.51 | -3.8% | -1.34 | 48% |
| 08 | 617 | +1.32 | +3.3% | +1.28 | 57% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 127 | +19.3 | +1.74 | 57% |
| Tue | 128 | +12.6 | +1.02 | 58% |
| Wed | 126 | +19.6 | +1.53 | 55% |
| Thu | 126 | +8.2 | +0.63 | 50% |
| Fri | 126 | +4.4 | +0.31 | 55% |

## Reality check (multiple-testing control)
- Best hour: **20 UTC** (t = +2.19)
- Familywise |t| threshold at 5%: 3.04
- Reality-check p-value for the best pattern: **0.500**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._