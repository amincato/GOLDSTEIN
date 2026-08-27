# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-27T16:51:20+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-136.8 bps (z = -0.29)** · mean -123.1 · σ 46.8 · 90% range [-158.0, -14.8]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1266 min
- Dislocations |z|>2: 5 events · P(convergence in 4h) = 20% · avg convergence -0.3 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.008, "-10min": -0.006, "-5min": 0.078, "+0min": 0.9, "+5min": -0.004, "+10min": -0.006, "+15min": 0.011}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 4 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 39 bps

## Funding
- Current +11.0% APR (mean +8.7%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._