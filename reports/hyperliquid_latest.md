# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-01T10:30:45+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-99.1 bps (z = +0.54)** · mean -123.0 · σ 44.6 · 90% range [-157.6, -15.4]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1127 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.004, "-10min": 0.004, "-5min": 0.075, "+0min": 0.903, "+5min": -0.003, "+10min": 0.001, "+15min": 0.008}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 5 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 35 bps

## Funding
- Current -5.8% APR (mean +8.4%, p90 +11.0%)
- **Cost of holding 50x: ~0.4% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._