# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-20T06:05:19+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-154.3 bps (z = -0.69)** · mean -118.5 · σ 51.6 · 90% range [-158.3, -13.7]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1480 min
- Dislocations |z|>2: 74 events · P(convergence in 4h) = 70% · avg convergence +2.7 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.011, "-10min": -0.017, "-5min": 0.09, "+0min": 0.895, "+5min": -0.003, "+10min": -0.01, "+15min": 0.017}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 3 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 52 bps

## Funding
- Current +11.0% APR (mean +8.6%, p90 +11.0%)
- **Cost of holding 50x: ~1.4% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._