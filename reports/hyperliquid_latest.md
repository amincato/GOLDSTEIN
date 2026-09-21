# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-21T11:09:18+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-89.3 bps (z = +0.61)** · mean -113.6 · σ 39.8 · 90% range [-155.9, -18.0]
- Mean reversion: AR(1) φ=0.996 → half-life ≈ 895 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.007, "-10min": -0.004, "-5min": 0.061, "+0min": 0.909, "+5min": -0.019, "+10min": -0.003, "+15min": 0.007}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 8 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 33 bps

## Funding
- Current +11.0% APR (mean +8.4%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._