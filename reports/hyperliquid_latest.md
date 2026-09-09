# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-09T10:09:52+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-98.8 bps (z = +0.48)** · mean -119.1 · σ 42.4 · 90% range [-157.0, -16.5]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1049 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.005, "-10min": -0.004, "-5min": 0.075, "+0min": 0.91, "+5min": -0.007, "+10min": -0.01, "+15min": 0.01}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 6 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 33 bps

## Funding
- Current +11.0% APR (mean +8.2%, p90 +11.0%)
- **Cost of holding 50x: ~1.1% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._