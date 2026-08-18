# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-18T06:04:59+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-133.4 bps (z = -0.32)** · mean -116.1 · σ 53.9 · 90% range [-158.0, -13.4]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1524 min
- Dislocations |z|>2: 24 events · P(convergence in 4h) = 96% · avg convergence +29.5 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.001, "-10min": -0.011, "-5min": 0.09, "+0min": 0.889, "+5min": -0.007, "+10min": -0.003, "+15min": 0.004}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 3 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 52 bps

## Funding
- Current +5.6% APR (mean +8.6%, p90 +11.0%)
- **Cost of holding 50x: ~1.2% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._