# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-24T10:33:08+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-90.1 bps (z = +0.56)** · mean -112.0 · σ 38.9 · 90% range [-155.4, -18.5]
- Mean reversion: AR(1) φ=0.996 → half-life ≈ 874 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.007, "-10min": -0.002, "-5min": 0.06, "+0min": 0.91, "+5min": -0.02, "+10min": -0.002, "+15min": 0.006}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 8 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 33 bps

## Funding
- Current +11.0% APR (mean +8.5%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._