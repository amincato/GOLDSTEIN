# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-11T10:02:37+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-85.3 bps (z = +0.78)** · mean -117.7 · σ 41.7 · 90% range [-156.7, -16.8]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1003 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.009, "-10min": -0.007, "-5min": 0.077, "+0min": 0.909, "+5min": -0.005, "+10min": -0.01, "+15min": 0.015}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 6 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 33 bps

## Funding
- Current +11.0% APR (mean +8.3%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._