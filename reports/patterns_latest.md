# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 809 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 20 | 656 | +1.85 | +4.7% | +2.02 | 53% |
| 23 | 656 | +2.48 | +6.3% | +1.99 | 54% |
| 11 | 667 | +1.97 | +5.0% | +1.91 | 53% |
| 05 | 662 | -1.80 | -4.5% | -1.53 | 52% |
| 07 | 659 | +1.64 | +4.1% | +1.51 | 50% |
| 04 | 657 | +0.95 | +2.4% | +1.47 | 48% |
| 06 | 667 | +1.45 | +3.6% | +1.43 | 53% |
| 15 | 664 | -1.95 | -4.9% | -1.27 | 51% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 135 | +14.2 | +1.31 | 55% |
| Tue | 137 | +8.7 | +0.72 | 55% |
| Wed | 135 | +15.7 | +1.29 | 53% |
| Thu | 135 | +8.2 | +0.65 | 50% |
| Fri | 135 | +4.1 | +0.30 | 56% |

## Reality check (multiple-testing control)
- Best hour: **20 UTC** (t = +2.02)
- Familywise |t| threshold at 5%: 3.10
- Reality-check p-value for the best pattern: **0.688**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._