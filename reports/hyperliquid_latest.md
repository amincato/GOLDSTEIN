# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-19T11:19:03+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-61.8 bps (z = +0.81)** · mean -96.1 · σ 42.3 · 90% range [-153.7, -22.2]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1132 min
- Dislocations |z|>2: 59 events · P(convergence in 4h) = 81% · avg convergence +20.7 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.002, "-10min": 0.001, "-5min": 0.058, "+0min": 0.911, "+5min": -0.021, "+10min": 0.002, "+15min": 0.0}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 12 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 28 bps

## Funding
- Current +11.0% APR (mean +9.0%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._