# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-30T11:23:52+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-54.4 bps (z = +1.37)** · mean -108.4 · σ 39.3 · 90% range [-155.0, -19.4]
- Mean reversion: AR(1) φ=0.996 → half-life ≈ 921 min
- Dislocations |z|>2: 6 events · P(convergence in 4h) = 33% · avg convergence +7.4 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.007, "-10min": -0.003, "-5min": 0.058, "+0min": 0.911, "+5min": -0.021, "+10min": -0.002, "+15min": 0.005}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 9 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 30 bps

## Funding
- Current +11.0% APR (mean +8.7%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._