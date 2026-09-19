# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 779 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 20 | 631 | +2.09 | +5.3% | +2.19 | 53% |
| 23 | 631 | +2.58 | +6.5% | +1.99 | 54% |
| 11 | 634 | +2.02 | +5.1% | +1.91 | 54% |
| 04 | 632 | +1.13 | +2.9% | +1.71 | 48% |
| 07 | 634 | +1.85 | +4.7% | +1.66 | 50% |
| 02 | 631 | -1.47 | -3.7% | -1.31 | 48% |
| 06 | 642 | +1.35 | +3.4% | +1.31 | 53% |
| 05 | 637 | -1.54 | -3.9% | -1.27 | 52% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 130 | +18.8 | +1.73 | 57% |
| Tue | 132 | +8.1 | +0.66 | 56% |
| Wed | 130 | +20.0 | +1.61 | 55% |
| Thu | 130 | +8.9 | +0.69 | 50% |
| Fri | 130 | +4.1 | +0.29 | 55% |

## Reality check (multiple-testing control)
- Best hour: **20 UTC** (t = +2.19)
- Familywise |t| threshold at 5%: 3.01
- Reality-check p-value for the best pattern: **0.564**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._