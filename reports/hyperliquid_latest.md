# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-08T12:16:45+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-42.4 bps (z = +1.42)** · mean -101.7 · σ 41.7 · 90% range [-154.4, -20.7]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1068 min
- Dislocations |z|>2: 79 events · P(convergence in 4h) = 61% · avg convergence +2.5 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.006, "-10min": 0.0, "-5min": 0.06, "+0min": 0.912, "+5min": -0.022, "+10min": 0.004, "+15min": 0.004}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 10 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 31 bps

## Funding
- Current +11.0% APR (mean +8.9%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._