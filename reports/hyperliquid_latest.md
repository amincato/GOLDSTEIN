# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-18T10:05:23+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-95.5 bps (z = +0.46)** · mean -114.0 · σ 40.2 · 90% range [-156.0, -17.8]
- Mean reversion: AR(1) φ=0.996 → half-life ≈ 921 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.006, "-10min": -0.004, "-5min": 0.062, "+0min": 0.911, "+5min": -0.017, "+10min": -0.003, "+15min": 0.007}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 7 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 33 bps

## Funding
- Current +11.0% APR (mean +8.3%, p90 +11.0%)
- **Cost of holding 50x: ~0.7% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._