# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-26T06:20:16+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-138.4 bps (z = -0.33)** · mean -122.5 · σ 48.1 · 90% range [-158.2, -14.4]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1303 min
- Dislocations |z|>2: 38 events · P(convergence in 4h) = 29% · avg convergence -2.4 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.005, "-10min": -0.01, "-5min": 0.08, "+0min": 0.899, "+5min": -0.003, "+10min": -0.01, "+15min": 0.011}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 4 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 39 bps

## Funding
- Current +7.9% APR (mean +8.7%, p90 +11.0%)
- **Cost of holding 50x: ~1.0% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._