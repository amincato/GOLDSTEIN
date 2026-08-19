# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-19T06:05:47+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-123.2 bps (z = -0.12)** · mean -116.9 · σ 52.5 · 90% range [-157.8, -13.6]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1487 min
- Dislocations |z|>2: 55 events · P(convergence in 4h) = 84% · avg convergence +16.1 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.002, "-10min": -0.019, "-5min": 0.086, "+0min": 0.891, "+5min": -0.009, "+10min": -0.011, "+15min": 0.006}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 3 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 52 bps

## Funding
- Current +6.2% APR (mean +8.5%, p90 +11.0%)
- **Cost of holding 50x: ~0.7% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._