# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-22T10:41:35+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-19.2 bps (z = +1.72)** · mean -93.4 · σ 43.1 · 90% range [-153.5, -22.0]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1228 min
- Dislocations |z|>2: 8 events · P(convergence in 4h) = 100% · avg convergence +28.7 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.0, "-10min": 0.0, "-5min": 0.058, "+0min": 0.913, "+5min": -0.021, "+10min": 0.002, "+15min": -0.001}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 12 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 28 bps

## Funding
- Current +1.7% APR (mean +8.9%, p90 +11.0%)
- **Cost of holding 50x: ~0.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._