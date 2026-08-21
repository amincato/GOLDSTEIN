# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-21T06:07:04+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-150.4 bps (z = -0.59)** · mean -120.1 · σ 50.9 · 90% range [-158.6, -13.9]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1459 min
- Dislocations |z|>2: 74 events · P(convergence in 4h) = 61% · avg convergence +1.4 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.018, "-10min": -0.012, "-5min": 0.085, "+0min": 0.897, "+5min": -0.005, "+10min": -0.006, "+15min": 0.021}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 3 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 52 bps

## Funding
- Current +11.0% APR (mean +8.5%, p90 +11.0%)
- **Cost of holding 50x: ~1.1% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._