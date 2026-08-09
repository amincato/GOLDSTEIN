# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-09T18:23:52+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-147.7 bps (z = -0.70)** · mean -103.6 · σ 62.9 · 90% range [-159.4, -11.7]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1664 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.004, "-10min": -0.014, "-5min": 0.106, "+0min": 0.876, "+5min": 0.003, "+10min": -0.011, "+15min": 0.009}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 2 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 77 bps

## Funding
- Current +11.0% APR (mean +8.4%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._