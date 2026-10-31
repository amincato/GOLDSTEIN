# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 815 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 20 | 661 | +1.90 | +4.8% | +2.08 | 53% |
| 23 | 661 | +2.41 | +6.1% | +1.94 | 54% |
| 11 | 677 | +1.91 | +4.8% | +1.88 | 53% |
| 05 | 667 | -1.85 | -4.7% | -1.58 | 52% |
| 07 | 664 | +1.61 | +4.1% | +1.50 | 50% |
| 04 | 662 | +0.92 | +2.3% | +1.43 | 48% |
| 06 | 672 | +1.32 | +3.3% | +1.32 | 53% |
| 15 | 669 | -1.90 | -4.8% | -1.25 | 51% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 136 | +14.2 | +1.32 | 55% |
| Tue | 138 | +9.6 | +0.81 | 56% |
| Wed | 136 | +15.4 | +1.27 | 53% |
| Thu | 136 | +7.3 | +0.58 | 50% |
| Fri | 136 | +3.3 | +0.24 | 54% |

## Reality check (multiple-testing control)
- Best hour: **20 UTC** (t = +2.08)
- Familywise |t| threshold at 5%: 3.00
- Reality-check p-value for the best pattern: **0.600**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._