# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 785 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 23 | 636 | +2.72 | +6.9% | +2.12 | 54% |
| 20 | 636 | +2.02 | +5.1% | +2.11 | 53% |
| 11 | 639 | +1.97 | +5.0% | +1.88 | 54% |
| 07 | 639 | +1.82 | +4.6% | +1.63 | 50% |
| 04 | 637 | +1.09 | +2.7% | +1.61 | 49% |
| 02 | 636 | -1.52 | -3.8% | -1.36 | 48% |
| 05 | 642 | -1.39 | -3.5% | -1.16 | 52% |
| 00 | 636 | +1.15 | +2.9% | +1.07 | 51% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 131 | +18.4 | +1.71 | 56% |
| Tue | 133 | +8.4 | +0.68 | 56% |
| Wed | 131 | +18.5 | +1.48 | 54% |
| Thu | 131 | +8.4 | +0.66 | 50% |
| Fri | 131 | +4.2 | +0.30 | 55% |

## Reality check (multiple-testing control)
- Best hour: **23 UTC** (t = +2.12)
- Familywise |t| threshold at 5%: 3.27
- Reality-check p-value for the best pattern: **0.642**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._