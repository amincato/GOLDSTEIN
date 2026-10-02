# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-02T11:23:35+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-57.2 bps (z = +1.22)** · mean -106.1 · σ 40.1 · 90% range [-154.8, -19.8]
- Mean reversion: AR(1) φ=0.996 → half-life ≈ 963 min
- Dislocations |z|>2: 48 events · P(convergence in 4h) = 35% · avg convergence -0.8 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.004, "-10min": 0.003, "-5min": 0.056, "+0min": 0.911, "+5min": -0.024, "+10min": 0.004, "+15min": 0.002}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 9 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 30 bps

## Funding
- Current +11.0% APR (mean +8.7%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._