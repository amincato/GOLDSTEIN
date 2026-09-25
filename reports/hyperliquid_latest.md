# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-09-25T10:36:36+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-95.3 bps (z = +0.42)** · mean -111.5 · σ 38.6 · 90% range [-155.3, -18.7]
- Mean reversion: AR(1) φ=0.996 → half-life ≈ 868 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.008, "-10min": -0.002, "-5min": 0.06, "+0min": 0.91, "+5min": -0.019, "+10min": -0.002, "+15min": 0.006}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 8 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 33 bps

## Funding
- Current +11.0% APR (mean +8.5%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._