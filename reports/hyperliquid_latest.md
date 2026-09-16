# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-16T10:20:45+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-96.4 bps (z = +0.46)** · mean -115.2 · σ 40.9 · 90% range [-156.3, -17.3]
- Mean reversion: AR(1) φ=0.996 → half-life ≈ 954 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.01, "-10min": -0.003, "-5min": 0.072, "+0min": 0.908, "+5min": -0.006, "+10min": -0.005, "+15min": 0.013}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 7 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 33 bps

## Funding
- Current +2.8% APR (mean +8.4%, p90 +11.0%)
- **Cost of holding 50x: ~0.8% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._