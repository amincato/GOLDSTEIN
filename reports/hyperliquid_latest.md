# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-04T09:59:50+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-99.2 bps (z = +0.48)** · mean -120.2 · σ 43.3 · 90% range [-157.1, -16.1]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1124 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.009, "-10min": 0.003, "-5min": 0.079, "+0min": 0.907, "+5min": 0.002, "+10min": -0.003, "+15min": 0.016}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 5 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 35 bps

## Funding
- Current +11.0% APR (mean +8.3%, p90 +11.0%)
- **Cost of holding 50x: ~0.9% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._