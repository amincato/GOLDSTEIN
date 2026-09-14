# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-14T11:01:03+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-75.5 bps (z = +1.00)** · mean -116.8 · σ 41.4 · 90% range [-156.6, -16.9]
- Mean reversion: AR(1) φ=0.996 → half-life ≈ 964 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.009, "-10min": -0.004, "-5min": 0.071, "+0min": 0.908, "+5min": -0.007, "+10min": -0.005, "+15min": 0.014}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 7 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 33 bps

## Funding
- Current +7.8% APR (mean +8.4%, p90 +11.0%)
- **Cost of holding 50x: ~1.3% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._