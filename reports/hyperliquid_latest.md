# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-11-04T13:19:08+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-34.8 bps (z = +1.00)** · mean -83.4 · σ 48.5 · 90% range [-152.9, -9.3]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1554 min
- Dislocations |z|>2: 10 events · P(convergence in 4h) = 80% · avg convergence +9.1 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.003, "-10min": 0.001, "-5min": 0.061, "+0min": 0.913, "+5min": -0.017, "+10min": 0.004, "+15min": -0.004}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 14 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.87** · avg |weekend move| 25 bps

## Funding
- Current +11.0% APR (mean +8.8%, p90 +11.0%)
- **Cost of holding 50x: ~1.1% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._