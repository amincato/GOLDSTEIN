# GOLDSTEIN — Intraday Seasonality Mining
_60m bars · 763 days · data: cache · 500 bootstrap draws_

## Hour-of-day effects (UTC)
| Hour | n | mean (bps) | ann. if held | t-stat | hit rate |
|---|---|---|---|---|---|
| 20 | 617 | +2.08 | +5.2% | +2.16 | 53% |
| 23 | 618 | +2.71 | +6.8% | +2.06 | 54% |
| 07 | 620 | +1.94 | +4.9% | +1.72 | 51% |
| 11 | 620 | +1.76 | +4.4% | +1.65 | 54% |
| 05 | 623 | -1.94 | -4.9% | -1.58 | 52% |
| 04 | 618 | +0.98 | +2.5% | +1.47 | 48% |
| 06 | 628 | +1.51 | +3.8% | +1.43 | 54% |
| 02 | 618 | -1.55 | -3.9% | -1.38 | 48% |

## Day-of-week (daily totals)
| Day | n | mean (bps) | t-stat | hit rate |
|---|---|---|---|---|
| Mon | 128 | +20.0 | +1.82 | 58% |
| Tue | 129 | +12.1 | +0.98 | 57% |
| Wed | 127 | +18.8 | +1.49 | 54% |
| Thu | 127 | +7.6 | +0.59 | 50% |
| Fri | 127 | +3.6 | +0.25 | 54% |

## Reality check (multiple-testing control)
- Best hour: **20 UTC** (t = +2.16)
- Familywise |t| threshold at 5%: 2.94
- Reality-check p-value for the best pattern: **0.570**
- **No hour-of-day pattern survives multiple-testing control.** Apparent seasonality in the raw table is consistent with chance.

---
_A pattern that does not survive the reality check must not be traded, regardless of how good its row looks._