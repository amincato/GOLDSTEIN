# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-26T11:35:21+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-4.0 bps (z = +1.93)** · mean -90.8 · σ 44.9 · 90% range [-153.4, -15.7]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1305 min
- Dislocations |z|>2: 13 events · P(convergence in 4h) = 100% · avg convergence +12.6 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.0, "-10min": 0.003, "-5min": 0.056, "+0min": 0.911, "+5min": -0.021, "+10min": 0.006, "+15min": -0.004}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 13 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.88** · avg |weekend move| 27 bps

## Funding
- Current +11.0% APR (mean +8.8%, p90 +11.0%)
- **Cost of holding 50x: ~1.4% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._