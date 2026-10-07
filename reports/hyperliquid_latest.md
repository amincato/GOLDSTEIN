# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-07T12:03:51+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-34.0 bps (z = +1.67)** · mean -102.9 · σ 41.2 · 90% range [-154.5, -20.5]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1055 min
- Dislocations |z|>2: 75 events · P(convergence in 4h) = 68% · avg convergence +1.9 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.002, "-10min": 0.002, "-5min": 0.058, "+0min": 0.913, "+5min": -0.021, "+10min": 0.002, "+15min": 0.002}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 10 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 31 bps

## Funding
- Current +11.0% APR (mean +8.8%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._