# GOLDSTEIN — Hyperliquid Gold Perp vs Reference
_Generated 2026-11-12T14:01:26+00:00 · coin: PAXG_

## Basis (perp vs reference, market-open hours)
- Current: **-24.9 bps (z = +1.15)** · mean -80.2 · σ 48.2 · 90% range [-152.4, -9.9]
- Mean reversion: AR(1) φ=0.998 → half-life ≈ 1577 min
- Dislocations |z|>2: 7 events · P(convergence in 4h) = 100% · avg convergence +16.4 bps

## Lead-lag (corr of perp return vs reference return shifted)
`{"-15min": -0.003, "-10min": -0.001, "-5min": 0.055, "+0min": 0.917, "+5min": -0.02, "+10min": -0.0, "+15min": -0.002}`
(positive at +5min ⇒ the perp LEADS the reference by ~one bar)

## Weekend behaviour
- 15 independent weekends · corr(perp weekend move, Monday reference gap) = **+0.85** · avg |weekend move| 24 bps

## Funding
- Current -0.4% APR (mean +8.9%, p90 +11.0%)
- **Cost of holding 50x: ~1.4% of equity per day in funding alone**
- Taker fees at 50x: 4.5% of equity per round trip

---
_Research tooling, not investment advice._