# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-11-26T15:50:29+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-88.7 bps (z = -0.28)** · mean -75.1 · σ 48.4 · 90% range [-151.8, -10.4]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1508 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.003, "-10min": -0.003, "-5min": 0.056, "+0min": 0.924, "+5min": -0.015, "+10min": -0.001, "+15min": -0.004}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 17 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.70** · avg |weekend move| 27 bps

## Funding
- Current +11.0% APR (mean +8.4%, p90 +11.0%)
- **Cost of holding 50x: ~1.2% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._