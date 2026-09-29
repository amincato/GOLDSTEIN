# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-29T11:37:05+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-55.3 bps (z = +1.39)** · mean -109.5 · σ 39.0 · 90% range [-155.1, -19.1]
- Mean reversion: AR(1) φ=0.996 → half-life ≈ 899 min
- Dislocations |z|>2: 5 events · P(convergence in 4h) = 40% · avg convergence +9.0 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.006, "-10min": -0.003, "-5min": 0.061, "+0min": 0.911, "+5min": -0.018, "+10min": -0.002, "+15min": 0.003}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 9 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 30 bps

## Funding
- Current +11.0% APR (mean +8.6%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._