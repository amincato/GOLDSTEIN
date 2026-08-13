# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-13T07:04:49+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-141.5 bps (z = -0.49)** · mean -113.1 · σ 58.2 · 90% range [-158.6, -12.6]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1641 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.003, "-10min": -0.017, "-5min": 0.095, "+0min": 0.887, "+5min": -0.001, "+10min": -0.009, "+15min": 0.007}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 2 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 77 bps

## Funding
- Current +5.9% APR (mean +8.4%, p90 +11.0%)
- **Cost of holding 50x: ~0.9% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._