# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-11-05T13:31:56+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-41.7 bps (z = +0.85)** · mean -82.8 · σ 48.5 · 90% range [-152.8, -9.4]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1575 min
- Dislocations |z|>2: 8 events · P(convergence in 4h) = 88% · avg convergence +11.1 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.004, "-10min": 0.002, "-5min": 0.061, "+0min": 0.914, "+5min": -0.017, "+10min": 0.003, "+15min": -0.005}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 14 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.87** · avg |weekend move| 25 bps

## Funding
- Current +11.0% APR (mean +8.8%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._