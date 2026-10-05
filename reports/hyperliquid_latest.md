# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-05T12:42:35+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-50.3 bps (z = +1.35)** · mean -105.0 · σ 40.4 · 90% range [-154.7, -20.0]
- Mean reversion: AR(1) φ=0.996 → half-life ≈ 978 min
- Dislocations |z|>2: 79 events · P(convergence in 4h) = 44% · avg convergence -0.2 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.004, "-10min": 0.001, "-5min": 0.058, "+0min": 0.912, "+5min": -0.024, "+10min": 0.003, "+15min": 0.003}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 10 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 31 bps

## Funding
- Current +11.0% APR (mean +8.8%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._