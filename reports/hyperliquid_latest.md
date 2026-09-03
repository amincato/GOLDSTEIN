# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-03T10:08:13+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-95.6 bps (z = +0.57)** · mean -120.7 · σ 43.9 · 90% range [-157.3, -16.0]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1106 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.008, "-10min": 0.005, "-5min": 0.075, "+0min": 0.904, "+5min": -0.005, "+10min": 0.002, "+15min": 0.011}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 5 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 35 bps

## Funding
- Current +11.0% APR (mean +8.3%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._