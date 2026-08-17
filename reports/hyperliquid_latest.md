# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-17T06:22:22+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-125.8 bps (z = -0.20)** · mean -115.0 · σ 55.0 · 90% range [-158.2, -13.1]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1548 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.003, "-10min": -0.011, "-5min": 0.089, "+0min": 0.888, "+5min": -0.008, "+10min": -0.003, "+15min": 0.005}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 3 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 52 bps

## Funding
- Current +11.0% APR (mean +8.6%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._