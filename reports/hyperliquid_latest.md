# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-11-03T13:03:08+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-8.6 bps (z = +1.57)** · mean -84.3 · σ 48.2 · 90% range [-153.0, -9.4]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1533 min
- Dislocations |z|>2: 14 events · P(convergence in 4h) = 79% · avg convergence +7.3 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.003, "-10min": -0.0, "-5min": 0.061, "+0min": 0.912, "+5min": -0.019, "+10min": 0.004, "+15min": -0.005}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 14 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.87** · avg |weekend move| 25 bps

## Funding
- Current +11.0% APR (mean +8.8%, p90 +11.0%)
- **Cost of holding 50x: ~0.6% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._