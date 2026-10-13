# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-13T12:59:31+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-53.0 bps (z = +1.11)** · mean -99.4 · σ 41.8 · 90% range [-154.0, -21.3]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1077 min
- Dislocations |z|>2: 81 events · P(convergence in 4h) = 67% · avg convergence +2.9 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.006, "-10min": -0.0, "-5min": 0.06, "+0min": 0.91, "+5min": -0.021, "+10min": 0.003, "+15min": 0.003}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 11 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 30 bps

## Funding
- Current +11.0% APR (mean +9.0%, p90 +11.0%)
- **Cost of holding 50x: ~1.4% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._