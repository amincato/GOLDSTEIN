# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-06T12:15:53+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-55.7 bps (z = +1.18)** · mean -103.9 · σ 40.9 · 90% range [-154.5, -20.3]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1009 min
- Dislocations |z|>2: 87 events · P(convergence in 4h) = 55% · avg convergence +0.9 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.004, "-10min": 0.001, "-5min": 0.058, "+0min": 0.912, "+5min": -0.023, "+10min": 0.003, "+15min": 0.002}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 10 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 31 bps

## Funding
- Current +11.0% APR (mean +8.8%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._