# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-11T06:39:25+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-142.9 bps (z = -0.57)** · mean -108.1 · σ 61.3 · 90% range [-159.1, -12.1]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1686 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.0, "-10min": -0.016, "-5min": 0.106, "+0min": 0.88, "+5min": 0.005, "+10min": -0.014, "+15min": 0.014}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 2 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 77 bps

## Funding
- Current +7.4% APR (mean +8.4%, p90 +11.0%)
- **Cost of holding 50x: ~1.2% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._