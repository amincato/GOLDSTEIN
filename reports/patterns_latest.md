# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 751 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 23 | 608 | +2.91 | +7.3% | +2.19 | 54% |
| 20 | 607 | +2.11 | +5.3% | +2.13 | 54% |
| 07 | 609 | +2.13 | +5.4% | +1.84 | 51% |
| 04 | 608 | +1.08 | +2.7% | +1.57 | 48% |
| 11 | 609 | +1.58 | +4.0% | +1.48 | 54% |
| 08 | 612 | +1.37 | +3.5% | +1.32 | 57% |
| 02 | 608 | -1.49 | -3.8% | -1.32 | 48% |
| 05 | 608 | -1.63 | -4.1% | -1.31 | 52% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 126 | +18.2 | +1.64 | 57% |
| Tue | 127 | +14.9 | +1.20 | 58% |
| Wed | 125 | +16.4 | +1.32 | 54% |
| Thu | 125 | +8.0 | +0.61 | 50% |
| Fri | 125 | +2.2 | +0.16 | 54% |

## Reality check (multiple-testing control)
- Best hour: **23 UTC** (t = +2.19)
- Familywise |t| threshold at 5%: 3.09
- Reality-check p-value for the best pattern: **0.520**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._