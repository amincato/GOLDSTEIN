# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-11-13T13:28:24+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-42.2 bps (z = +0.77)** · mean -79.5 · σ 48.3 · 90% range [-152.4, -9.9]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1578 min
- Dislocations |z|>2: 6 events · P(convergence in 4h) = 100% · avg convergence +17.7 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.001, "-10min": -0.002, "-5min": 0.057, "+0min": 0.917, "+5min": -0.02, "+10min": -0.0, "+15min": -0.001}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 15 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.85** · avg |weekend move| 24 bps

## Funding
- Current +11.0% APR (mean +8.9%, p90 +11.0%)
- **Cost of holding 50x: ~1.2% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._