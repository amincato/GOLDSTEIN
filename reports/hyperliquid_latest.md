# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-11-02T13:53:24+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-21.5 bps (z = +1.33)** · mean -85.2 · σ 47.9 · 90% range [-153.1, -9.9]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1526 min
- Dislocations |z|>2: 15 events · P(convergence in 4h) = 80% · avg convergence +6.6 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.002, "-10min": 0.001, "-5min": 0.061, "+0min": 0.913, "+5min": -0.018, "+10min": 0.005, "+15min": -0.003}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 14 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.87** · avg |weekend move| 25 bps

## Funding
- Current +11.0% APR (mean +8.9%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._