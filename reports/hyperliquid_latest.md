# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-11-11T12:59:44+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-45.9 bps (z = +0.73)** · mean -80.8 · σ 48.1 · 90% range [-152.5, -9.7]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1569 min
- Dislocations |z|>2: 6 events · P(convergence in 4h) = 100% · avg convergence +15.2 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.004, "-10min": -0.001, "-5min": 0.054, "+0min": 0.917, "+5min": -0.022, "+10min": -0.0, "+15min": -0.003}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 15 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.85** · avg |weekend move| 24 bps

## Funding
- Current +11.0% APR (mean +8.9%, p90 +11.0%)
- **Cost of holding 50x: ~1.4% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._