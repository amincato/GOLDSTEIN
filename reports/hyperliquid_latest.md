# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-16T10:09:17+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-54.8 bps (z = +0.99)** · mean -96.8 · σ 42.4 · 90% range [-153.8, -21.9]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1159 min
- Dislocations |z|>2: 52 events · P(convergence in 4h) = 83% · avg convergence +17.7 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.001, "-10min": -0.001, "-5min": 0.059, "+0min": 0.913, "+5min": -0.021, "+10min": -0.0, "+15min": 0.0}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 11 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 30 bps

## Funding
- Current +11.0% APR (mean +9.0%, p90 +11.0%)
- **Cost of holding 50x: ~1.4% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._