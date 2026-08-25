# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-25T06:06:27+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-133.8 bps (z = -0.25)** · mean -121.8 · σ 49.0 · 90% range [-158.3, -14.3]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1300 min
- Dislocations |z|>2: 87 events · P(convergence in 4h) = 48% · avg convergence -0.1 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.007, "-10min": -0.017, "-5min": 0.087, "+0min": 0.896, "+5min": 0.0, "+10min": -0.017, "+15min": 0.014}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 4 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 39 bps

## Funding
- Current +11.0% APR (mean +8.7%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._