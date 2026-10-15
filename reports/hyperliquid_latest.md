# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-15T10:22:44+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-50.0 bps (z = +1.12)** · mean -97.6 · σ 42.3 · 90% range [-153.9, -21.7]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1146 min
- Dislocations |z|>2: 66 events · P(convergence in 4h) = 71% · avg convergence +11.9 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.002, "-10min": -0.0, "-5min": 0.062, "+0min": 0.913, "+5min": -0.018, "+10min": 0.001, "+15min": 0.0}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 11 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 30 bps

## Funding
- Current +6.6% APR (mean +9.0%, p90 +11.0%)
- **Cost of holding 50x: ~1.1% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._