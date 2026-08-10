# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-08-10T06:59:28+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-149.9 bps (z = -0.72)** · mean -105.0 · σ 62.5 · 90% range [-159.3, -11.8]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1670 min

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.003, "-10min": -0.015, "-5min": 0.104, "+0min": 0.877, "+5min": 0.0, "+10min": -0.011, "+15min": 0.01}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 2 independent weekends · corr(perp weekend move, Monday reference gap) = n/a (need ≥8 weekends) · avg |weekend move| 77 bps

## Funding
- Current +11.0% APR (mean +8.4%, p90 +11.0%)
- **Cost of holding 50x: ~1.5% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._