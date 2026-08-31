# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-31T11:52:46+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-119.2 bps (z = +0.09)** · mean -123.4 · σ 45.3 · 90% range [-157.7, -15.3]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1210 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.0, "-10min": 0.003, "-5min": 0.074, "+0min": 0.907, "+5min": -0.003, "+10min": -0.002, "+15min": 0.006}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 5 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 35 bps

## Funding
- Current +2.3% APR (mean +8.5%, p90 +11.0%)
- **Cost of holding 50x: ~0.2% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._