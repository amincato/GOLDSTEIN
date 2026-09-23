# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-23T10:19:15+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-82.7 bps (z = +0.76)** · mean -112.6 · σ 39.2 · 90% range [-155.6, -18.4]
- Mean reversion: AR(1) φ=0.996 → half-life ≈ 879 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.007, "-10min": -0.003, "-5min": 0.062, "+0min": 0.91, "+5min": -0.019, "+10min": -0.002, "+15min": 0.006}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 8 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 33 bps

## Funding
- Current +11.0% APR (mean +8.4%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._