# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 773 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 20 | 626 | +2.04 | +5.2% | +2.14 | 53% |
| 23 | 626 | +2.64 | +6.6% | +2.03 | 54% |
| 11 | 629 | +1.90 | +4.8% | +1.80 | 54% |
| 07 | 629 | +1.91 | +4.8% | +1.71 | 51% |
| 04 | 627 | +1.13 | +2.8% | +1.69 | 48% |
| 02 | 626 | -1.49 | -3.8% | -1.34 | 48% |
| 05 | 632 | -1.61 | -4.1% | -1.32 | 52% |
| 06 | 637 | +1.30 | +3.3% | +1.25 | 53% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 129 | +19.8 | +1.81 | 57% |
| Tue | 131 | +8.3 | +0.66 | 56% |
| Wed | 129 | +20.4 | +1.63 | 55% |
| Thu | 129 | +7.7 | +0.59 | 50% |
| Fri | 129 | +3.2 | +0.22 | 54% |

## Reality check (multiple-testing control)
- Best hour: **20 UTC** (t = +2.14)
- Familywise |t| threshold at 5%: 3.20
- Reality-check p-value for the best pattern: **0.630**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._