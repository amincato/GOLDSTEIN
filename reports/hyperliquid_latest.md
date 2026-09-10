# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-10T10:05:08+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-96.0 bps (z = +0.54)** · mean -118.6 · σ 41.9 · 90% range [-156.8, -16.6]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1025 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.006, "-10min": -0.003, "-5min": 0.077, "+0min": 0.91, "+5min": -0.005, "+10min": -0.009, "+15min": 0.01}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 6 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 33 bps

## Funding
- Current +11.0% APR (mean +8.2%, p90 +11.0%)
- **Cost of holding 50x: ~1.2% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._