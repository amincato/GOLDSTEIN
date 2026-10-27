# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-27T11:03:09+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-15.4 bps (z = +1.62)** · mean -89.6 · σ 45.7 · 90% range [-153.3, -12.9]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1360 min
- Dislocations |z|>2: 5 events · P(convergence in 4h) = 100% · avg convergence +19.3 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.0, "-10min": 0.004, "-5min": 0.056, "+0min": 0.912, "+5min": -0.021, "+10min": 0.006, "+15min": -0.004}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 13 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.88** · avg |weekend move| 27 bps

## Funding
- Current +9.2% APR (mean +8.8%, p90 +11.0%)
- **Cost of holding 50x: ~1.2% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._