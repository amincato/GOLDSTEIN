# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-30T11:41:53+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **+3.0 bps (z = +1.91)** · mean -86.6 · σ 46.9 · 90% range [-153.2, -12.4]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1465 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.002, "-10min": 0.0, "-5min": 0.058, "+0min": 0.913, "+5min": -0.021, "+10min": 0.004, "+15min": -0.004}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 13 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.88** · avg |weekend move| 27 bps

## Funding
- Current +11.0% APR (mean +8.9%, p90 +11.0%)
- **Cost of holding 50x: ~1.3% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._