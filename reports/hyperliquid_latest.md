# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-28T12:02:24+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-64.8 bps (z = +1.19)** · mean -110.7 · σ 38.5 · 90% range [-155.2, -19.0]
- Mean reversion: AR(1) φ=0.996 → half-life ≈ 869 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.008, "-10min": -0.004, "-5min": 0.06, "+0min": 0.911, "+5min": -0.02, "+10min": -0.003, "+15min": 0.007}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 9 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 30 bps

## Funding
- Current +11.0% APR (mean +8.6%, p90 +11.0%)
- **Cost of holding 50x: ~1.4% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._