# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-11-20T14:24:50+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-16.8 bps (z = +1.24)** · mean -76.6 · σ 48.4 · 90% range [-152.0, -10.2]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1577 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.001, "-10min": -0.001, "-5min": 0.053, "+0min": 0.92, "+5min": -0.02, "+10min": 0.0, "+15min": -0.002}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 16 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.81** · avg |weekend move| 25 bps

## Funding
- Current -2.7% APR (mean +8.9%, p90 +11.0%)
- **Cost of holding 50x: ~1.0% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._