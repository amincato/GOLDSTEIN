# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-12T13:34:56+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-59.6 bps (z = +0.97)** · mean -100.1 · σ 41.7 · 90% range [-154.2, -21.1]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1102 min
- Dislocations |z|>2: 80 events · P(convergence in 4h) = 61% · avg convergence +2.4 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.005, "-10min": 0.0, "-5min": 0.061, "+0min": 0.913, "+5min": -0.02, "+10min": 0.002, "+15min": 0.003}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 11 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 30 bps

## Funding
- Current +11.0% APR (mean +8.9%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._