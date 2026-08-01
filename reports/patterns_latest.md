# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 736 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 20 | 595 | +2.57 | +6.5% | +2.70 | 54% |
| 23 | 594 | +3.07 | +7.7% | +2.43 | 54% |
| 07 | 598 | +1.78 | +4.5% | +1.58 | 51% |
| 04 | 596 | +1.05 | +2.7% | +1.50 | 48% |
| 02 | 595 | -1.60 | -4.0% | -1.40 | 48% |
| 03 | 594 | +1.04 | +2.6% | +1.39 | 53% |
| 06 | 597 | +1.39 | +3.5% | +1.30 | 54% |
| 05 | 596 | -1.48 | -3.7% | -1.27 | 52% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 123 | +12.1 | +1.00 | 56% |
| Tue | 125 | +15.6 | +1.24 | 58% |
| Wed | 123 | +12.0 | +0.99 | 54% |
| Thu | 123 | +9.7 | +0.73 | 50% |
| Fri | 123 | +4.8 | +0.36 | 54% |

## Reality check (multiple-testing control)
- Best hour: **20 UTC** (t = +2.70)
- Familywise |t| threshold at 5%: 3.11
- Reality-check p-value for the best pattern: **0.224**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._