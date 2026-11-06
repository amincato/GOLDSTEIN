# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-11-06T13:17:20+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-40.6 bps (z = +0.86)** · mean -82.2 · σ 48.5 · 90% range [-152.7, -9.4]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1566 min
- Dislocations |z|>2: 6 events · P(convergence in 4h) = 100% · avg convergence +14.3 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.001, "-10min": -0.003, "-5min": 0.058, "+0min": 0.915, "+5min": -0.019, "+10min": -0.001, "+15min": -0.003}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 14 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.87** · avg |weekend move| 25 bps

## Funding
- Current +11.0% APR (mean +8.9%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._