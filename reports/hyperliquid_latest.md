# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-21T10:38:25+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-26.6 bps (z = +1.59)** · mean -94.4 · σ 42.8 · 90% range [-153.6, -22.5]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1199 min
- Dislocations |z|>2: 34 events · P(convergence in 4h) = 94% · avg convergence +27.5 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.0, "-10min": -0.001, "-5min": 0.058, "+0min": 0.913, "+5min": -0.022, "+10min": 0.0, "+15min": -0.0}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 12 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 28 bps

## Funding
- Current +1.7% APR (mean +9.0%, p90 +11.0%)
- **Cost of holding 50x: ~0.8% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._