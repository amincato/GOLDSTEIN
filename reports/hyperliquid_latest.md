# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-14T10:39:45+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-50.4 bps (z = +1.15)** · mean -98.6 · σ 41.9 · 90% range [-153.9, -21.5]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1090 min
- Dislocations |z|>2: 70 events · P(convergence in 4h) = 74% · avg convergence +4.1 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.004, "-10min": -0.001, "-5min": 0.06, "+0min": 0.91, "+5min": -0.02, "+10min": 0.002, "+15min": 0.002}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 11 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 30 bps

## Funding
- Current +5.0% APR (mean +9.0%, p90 +11.0%)
- **Cost of holding 50x: ~1.3% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._