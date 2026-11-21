# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 833 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 23 | 676 | +2.40 | +6.0% | +1.97 | 54% |
| 20 | 676 | +1.68 | +4.2% | +1.87 | 53% |
| 11 | 692 | +1.77 | +4.5% | +1.77 | 53% |
| 15 | 684 | -2.44 | -6.1% | -1.61 | 51% |
| 05 | 682 | -1.68 | -4.2% | -1.43 | 51% |
| 02 | 676 | -1.56 | -3.9% | -1.43 | 48% |
| 07 | 679 | +1.47 | +3.7% | +1.39 | 50% |
| 06 | 687 | +1.36 | +3.4% | +1.37 | 53% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 139 | +15.6 | +1.46 | 55% |
| Tue | 141 | +7.2 | +0.61 | 55% |
| Wed | 139 | +14.2 | +1.15 | 53% |
| Thu | 139 | +3.1 | +0.24 | 50% |
| Fri | 139 | +0.3 | +0.03 | 54% |

## Reality check (multiple-testing control)
- Best hour: **23 UTC** (t = +1.97)
- Familywise |t| threshold at 5%: 2.99
- Reality-check p-value for the best pattern: **0.682**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._