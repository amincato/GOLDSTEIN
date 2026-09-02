# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-02T09:57:36+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-89.5 bps (z = +0.73)** · mean -121.8 · σ 44.3 · 90% range [-157.4, -15.6]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1108 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.004, "-10min": 0.007, "-5min": 0.078, "+0min": 0.903, "+5min": -0.001, "+10min": 0.004, "+15min": 0.007}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 5 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 35 bps

## Funding
- Current +4.4% APR (mean +8.3%, p90 +11.0%)
- **Cost of holding 50x: ~0.1% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._