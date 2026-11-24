# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-11-24T16:30:25+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-12.1 bps (z = +1.31)** · mean -75.4 · σ 48.5 · 90% range [-151.9, -10.4]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1572 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.001, "-10min": -0.004, "-5min": 0.056, "+0min": 0.924, "+5min": -0.014, "+10min": -0.004, "+15min": -0.004}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 17 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.70** · avg |weekend move| 27 bps

## Funding
- Current +7.8% APR (mean +8.5%, p90 +11.0%)
- **Cost of holding 50x: ~0.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._