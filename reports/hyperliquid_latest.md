# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-10-20T10:27:59+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-37.8 bps (z = +1.36)** · mean -95.4 · σ 42.4 · 90% range [-153.7, -22.3]
- Mean reversion: AR(1) φ=0.997 → half-life ≈ 1144 min
- Dislocations |z|>2: 62 events · P(convergence in 4h) = 85% · avg convergence +27.4 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": 0.002, "-10min": 0.001, "-5min": 0.057, "+0min": 0.911, "+5min": -0.022, "+10min": 0.002, "+15min": -0.0}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 12 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.89** · avg |weekend move| 28 bps

## Funding
- Current -3.2% APR (mean +9.0%, p90 +11.0%)
- **Cost of holding 50x: ~1.1% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._