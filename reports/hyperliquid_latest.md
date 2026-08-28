# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-28T17:44:44+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-116.1 bps (z = +0.16)** · mean -123.5 · σ 45.9 · 90% range [-157.8, -15.1]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1239 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.002, "-10min": 0.006, "-5min": 0.078, "+0min": 0.905, "+5min": 0.0, "+10min": 0.005, "+15min": 0.004}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 4 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 39 bps

## Funding
- Current +5.8% APR (mean +8.7%, p90 +11.0%)
- **Cost of holding 50x: ~1.3% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._