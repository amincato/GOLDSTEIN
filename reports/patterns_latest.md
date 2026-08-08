# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 745 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 20 | 601 | +2.16 | +5.4% | +2.16 | 54% |
| 23 | 603 | +2.89 | +7.3% | +2.16 | 54% |
| 07 | 604 | +2.21 | +5.6% | +1.90 | 51% |
| 04 | 603 | +1.08 | +2.7% | +1.56 | 48% |
| 11 | 604 | +1.58 | +4.0% | +1.47 | 54% |
| 02 | 603 | -1.47 | -3.7% | -1.28 | 48% |
| 08 | 607 | +1.31 | +3.3% | +1.25 | 57% |
| 16 | 610 | +1.38 | +3.5% | +1.22 | 55% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 125 | +17.1 | +1.53 | 57% |
| Tue | 126 | +15.6 | +1.25 | 59% |
| Wed | 124 | +15.8 | +1.26 | 54% |
| Thu | 124 | +9.2 | +0.70 | 50% |
| Fri | 124 | +1.8 | +0.12 | 54% |

## Reality check (multiple-testing control)
- Best hour: **20 UTC** (t = +2.16)
- Familywise |t| threshold at 5%: 3.03
- Reality-check p-value for the best pattern: **0.566**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._