# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 827 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 20 | 671 | +1.74 | +4.4% | +1.93 | 52% |
| 23 | 671 | +2.35 | +5.9% | +1.92 | 54% |
| 11 | 687 | +1.88 | +4.7% | +1.87 | 53% |
| 04 | 672 | +0.97 | +2.4% | +1.51 | 48% |
| 05 | 677 | -1.74 | -4.4% | -1.49 | 51% |
| 15 | 679 | -2.08 | -5.2% | -1.38 | 51% |
| 06 | 682 | +1.36 | +3.4% | +1.37 | 53% |
| 07 | 674 | +1.43 | +3.6% | +1.34 | 50% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 138 | +16.4 | +1.53 | 56% |
| Tue | 140 | +7.5 | +0.63 | 55% |
| Wed | 138 | +16.4 | +1.34 | 53% |
| Thu | 138 | +5.7 | +0.46 | 50% |
| Fri | 138 | +0.9 | +0.07 | 54% |

## Reality check (multiple-testing control)
- Best hour: **20 UTC** (t = +1.93)
- Familywise |t| threshold at 5%: 2.97
- Reality-check p-value for the best pattern: **0.714**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._