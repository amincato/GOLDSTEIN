# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-15T10:30:19+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-83.0 bps (z = +0.80)** · mean -115.9 · σ 41.2 · 90% range [-156.4, -17.1]
- Mean reversion: AR(1) φ=0.996 → half-life ≈ 958 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.01, "-10min": -0.005, "-5min": 0.071, "+0min": 0.908, "+5min": -0.007, "+10min": -0.006, "+15min": 0.013}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 7 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 33 bps

## Funding
- Current +3.8% APR (mean +8.4%, p90 +11.0%)
- **Cost of holding 50x: ~1.2% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._