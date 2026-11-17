# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-11-17T14:56:46+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-41.3 bps (z = +0.77)** · mean -78.5 · σ 48.1 · 90% range [-152.2, -9.9]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1572 min
- Dislocations |z|>2: 6 events · P(convergence in 4h) = 100% · avg convergence +17.7 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.002, "-10min": -0.004, "-5min": 0.055, "+0min": 0.917, "+5min": -0.02, "+10min": -0.002, "+15min": -0.003}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 16 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.81** · avg |weekend move| 25 bps

## Funding
- Current +11.0% APR (mean +8.9%, p90 +11.0%)
- **Cost of holding 50x: ~1.3% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._