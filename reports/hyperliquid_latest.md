# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-07T10:46:25+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-104.1 bps (z = +0.37)** · mean -119.9 · σ 43.1 · 90% range [-157.1, -16.2]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1070 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.006, "-10min": -0.003, "-5min": 0.078, "+0min": 0.909, "+5min": -0.004, "+10min": -0.008, "+15min": 0.011}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 6 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 33 bps

## Funding
- Current +4.5% APR (mean +8.4%, p90 +11.0%)
- **Cost of holding 50x: ~1.2% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._