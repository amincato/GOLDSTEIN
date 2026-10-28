# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-28T11:41:45+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-18.2 bps (z = +1.53)** · mean -88.6 · σ 46.1 · 90% range [-153.2, -12.9]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1425 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.002, "-10min": 0.003, "-5min": 0.058, "+0min": 0.913, "+5min": -0.02, "+10min": 0.003, "+15min": -0.003}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 13 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.88** · avg |weekend move| 27 bps

## Funding
- Current +11.0% APR (mean +8.8%, p90 +11.0%)
- **Cost of holding 50x: ~1.2% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._