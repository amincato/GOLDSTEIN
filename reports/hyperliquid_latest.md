# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-11-09T14:24:51+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-53.0 bps (z = +0.59)** · mean -81.7 · σ 48.4 · 90% range [-152.6, -9.6]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1560 min
- Dislocations |z|>2: 6 events · P(convergence in 4h) = 100% · avg convergence +15.3 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.004, "-10min": -0.001, "-5min": 0.057, "+0min": 0.915, "+5min": -0.021, "+10min": 0.001, "+15min": -0.004}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 15 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.85** · avg |weekend move| 24 bps

## Funding
- Current +11.0% APR (mean +8.9%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._