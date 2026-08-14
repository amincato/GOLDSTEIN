# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-14T07:00:59+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-111.4 bps (z = +0.05)** · mean -114.0 · σ 56.5 · 90% range [-158.4, -12.9]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1591 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.005, "-10min": -0.013, "-5min": 0.089, "+0min": 0.888, "+5min": -0.007, "+10min": -0.006, "+15min": 0.006}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 2 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 77 bps

## Funding
- Current +11.0% APR (mean +8.4%, p90 +11.0%)
- **Cost of holding 50x: ~1.2% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._