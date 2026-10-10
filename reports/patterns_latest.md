# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 797 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 20 | 646 | +1.91 | +4.8% | +2.05 | 53% |
| 23 | 646 | +2.58 | +6.5% | +2.04 | 54% |
| 11 | 657 | +2.06 | +5.2% | +2.00 | 54% |
| 04 | 647 | +1.03 | +2.6% | +1.59 | 48% |
| 07 | 649 | +1.67 | +4.2% | +1.53 | 51% |
| 06 | 657 | +1.48 | +3.7% | +1.45 | 54% |
| 05 | 652 | -1.70 | -4.3% | -1.43 | 52% |
| 02 | 646 | -1.53 | -3.9% | -1.38 | 48% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 133 | +15.7 | +1.44 | 56% |
| Tue | 135 | +9.4 | +0.78 | 56% |
| Wed | 133 | +16.6 | +1.34 | 53% |
| Thu | 133 | +9.4 | +0.75 | 50% |
| Fri | 133 | +3.9 | +0.28 | 55% |

## Reality check (multiple-testing control)
- Best hour: **20 UTC** (t = +2.05)
- Familywise |t| threshold at 5%: 3.13
- Reality-check p-value for the best pattern: **0.698**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._