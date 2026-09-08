# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-08T10:07:42+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-99.4 bps (z = +0.47)** · mean -119.8 · σ 42.9 · 90% range [-157.0, -16.3]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1064 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.007, "-10min": -0.003, "-5min": 0.079, "+0min": 0.909, "+5min": -0.003, "+10min": -0.008, "+15min": 0.012}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 6 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 33 bps

## Funding
- Current -0.4% APR (mean +8.2%, p90 +11.0%)
- **Cost of holding 50x: ~0.2% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._