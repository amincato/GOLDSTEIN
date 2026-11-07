# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 821 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 23 | 666 | +2.42 | +6.1% | +1.97 | 54% |
| 20 | 666 | +1.77 | +4.5% | +1.95 | 52% |
| 11 | 682 | +1.91 | +4.8% | +1.89 | 54% |
| 05 | 672 | -1.80 | -4.5% | -1.53 | 51% |
| 04 | 667 | +0.98 | +2.5% | +1.53 | 48% |
| 06 | 677 | +1.50 | +3.8% | +1.49 | 53% |
| 07 | 669 | +1.56 | +3.9% | +1.46 | 50% |
| 15 | 674 | -2.09 | -5.3% | -1.38 | 51% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 137 | +15.1 | +1.41 | 55% |
| Tue | 139 | +9.4 | +0.79 | 55% |
| Wed | 137 | +17.6 | +1.44 | 53% |
| Thu | 137 | +7.6 | +0.61 | 50% |
| Fri | 137 | +0.8 | +0.06 | 54% |

## Reality check (multiple-testing control)
- Best hour: **23 UTC** (t = +1.97)
- Familywise |t| threshold at 5%: 3.12
- Reality-check p-value for the best pattern: **0.712**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._