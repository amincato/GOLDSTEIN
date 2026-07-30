# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 735 days · data: cache · 800 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 20 | 595 | +2.57 | +6.5% | +2.70 | 54% |
| 23 | 594 | +3.07 | +7.7% | +2.43 | 54% |
| 07 | 597 | +1.83 | +4.6% | +1.62 | 51% |
| 04 | 595 | +1.04 | +2.6% | +1.48 | 48% |
| 03 | 593 | +1.04 | +2.6% | +1.40 | 53% |
| 02 | 594 | -1.56 | -3.9% | -1.37 | 48% |
| 06 | 596 | +1.38 | +3.5% | +1.29 | 54% |
| 05 | 595 | -1.46 | -3.7% | -1.25 | 52% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 123 | +12.1 | +1.00 | 56% |
| Tue | 125 | +15.6 | +1.24 | 58% |
| Wed | 123 | +12.0 | +0.99 | 54% |
| Thu | 123 | +9.7 | +0.73 | 50% |
| Fri | 122 | +5.8 | +0.44 | 54% |

## Reality check (multiple-testing control)
- Best hour: **20 UTC** (t = +2.70)
- Familywise |t| threshold at 5%: 3.21
- Reality-check p-value for the best pattern: **0.198**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._