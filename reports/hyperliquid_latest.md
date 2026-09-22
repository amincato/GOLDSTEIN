# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-22T10:23:01+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-88.1 bps (z = +0.63)** · mean -113.1 · σ 39.5 · 90% range [-155.8, -18.2]
- Mean reversion: AR(1) φ=0.996 → half-life ≈ 883 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.006, "-10min": -0.004, "-5min": 0.063, "+0min": 0.91, "+5min": -0.018, "+10min": -0.004, "+15min": 0.006}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 8 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 33 bps

## Funding
- Current +11.0% APR (mean +8.4%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._