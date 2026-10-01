# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-01T11:51:20+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-49.2 bps (z = +1.46)** · mean -107.2 · σ 39.8 · 90% range [-154.9, -19.5]
- Mean reversion: AR(1) φ=0.996 → half-life ≈ 948 min
- Dislocations |z|>2: 16 events · P(convergence in 4h) = 25% · avg convergence +0.5 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.007, "-10min": -0.001, "-5min": 0.058, "+0min": 0.912, "+5min": -0.022, "+10min": 0.001, "+15min": 0.005}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 9 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 30 bps

## Funding
- Current +11.0% APR (mean +8.7%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._