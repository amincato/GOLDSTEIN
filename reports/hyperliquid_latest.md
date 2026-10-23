# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-23T10:33:33+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-5.4 bps (z = +1.97)** · mean -92.1 · σ 44.0 · 90% range [-153.4, -18.9]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1275 min
- Dislocations |z|>2: 22 events · P(convergence in 4h) = 50% · avg convergence +6.5 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.002, "-10min": 0.002, "-5min": 0.057, "+0min": 0.913, "+5min": -0.021, "+10min": 0.003, "+15min": -0.003}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 12 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 28 bps

## Funding
- Current +4.2% APR (mean +8.9%, p90 +11.0%)
- **Cost of holding 50x: ~0.7% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._