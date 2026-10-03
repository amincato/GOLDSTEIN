# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 791 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 20 | 641 | +2.05 | +5.2% | +2.18 | 53% |
| 23 | 641 | +2.60 | +6.6% | +2.04 | 54% |
| 11 | 650 | +2.04 | +5.1% | +1.96 | 54% |
| 04 | 642 | +1.14 | +2.9% | +1.74 | 49% |
| 07 | 644 | +1.64 | +4.1% | +1.49 | 50% |
| 05 | 647 | -1.64 | -4.1% | -1.37 | 52% |
| 02 | 641 | -1.48 | -3.7% | -1.33 | 48% |
| 06 | 652 | +1.29 | +3.3% | +1.26 | 53% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 132 | +16.1 | +1.46 | 56% |
| Tue | 134 | +8.9 | +0.73 | 56% |
| Wed | 132 | +17.8 | +1.44 | 54% |
| Thu | 132 | +8.8 | +0.70 | 50% |
| Fri | 132 | +4.7 | +0.33 | 55% |

## Reality check (multiple-testing control)
- Best hour: **20 UTC** (t = +2.18)
- Familywise |t| threshold at 5%: 3.13
- Reality-check p-value for the best pattern: **0.520**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._