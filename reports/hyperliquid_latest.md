# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-24T06:26:40+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-132.2 bps (z = -0.22)** · mean -121.3 · σ 50.0 · 90% range [-158.5, -14.1]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1365 min
- Dislocations |z|>2: 74 events · P(convergence in 4h) = 65% · avg convergence +1.5 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.011, "-10min": -0.01, "-5min": 0.093, "+0min": 0.895, "+5min": 0.002, "+10min": -0.007, "+15min": 0.015}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 4 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 39 bps

## Funding
- Current +11.0% APR (mean +8.7%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._