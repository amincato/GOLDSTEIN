# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-11-19T14:43:30+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-18.0 bps (z = +1.23)** · mean -77.3 · σ 48.3 · 90% range [-152.1, -10.2]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1585 min
- Dislocations |z|>2: 5 events · P(convergence in 4h) = 100% · avg convergence +18.3 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.001, "-10min": -0.004, "-5min": 0.056, "+0min": 0.918, "+5min": -0.019, "+10min": -0.002, "+15min": -0.001}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 16 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.81** · avg |weekend move| 25 bps

## Funding
- Current +11.0% APR (mean +8.9%, p90 +11.0%)
- **Cost of holding 50x: ~0.6% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._