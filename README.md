# GOLDSTEIN

**Quant research & risk platform for leveraged gold investing — designed to be operated end-to-end by Claude agents (mobile, web, or CLI).**

GOLDSTEIN answers one question with institutional-grade machinery: *how much leverage on gold, right now, through which instrument — and would the position survive?*

## Capabilities

| Area | What's inside |
|---|---|
| **Data** | Multi-provider ingestion (Stooq → Yahoo → FRED) with local CSV cache and deterministic synthetic fallback, so every command runs even fully offline (flagged as DEMO) |
| **Volatility** | EWMA (RiskMetrics), GARCH(1,1) quasi-MLE, HAR-RV — blended into one forward vol forecast |
| **Regimes** | Gaussian HMM (own EM implementation) → calm/normal/turbulent, plus a macro regime score from real yields, DXY and VIX |
| **Signal** | Ensemble: multi-horizon time-series momentum, 50/200 trend, RSI mean-reversion, macro score, cross-asset confirmation → conviction in [-1, +1] |
| **Cross-asset** | Rolling correlations/betas vs silver, GDX miners, DXY, S&P 500, WTI, BTC; gold/silver ratio z-score; miners leadership; lead-lag vs real-yield changes |
| **Validation** | Strategy suite through the full engine, yearly walk-forward OOS buckets, Probabilistic Sharpe Ratio (Bailey–López de Prado), parameter-sensitivity grid, 5-check robustness verdict |
| **Autonomy** | Daily GitHub Actions cron: fetches real data, refreshes `reports/latest.*` + `history.csv`, commits the cache, opens an issue when the leverage advice materially changes; weekly re-validation |
| **Intraday scalping** | 5m/60m data layer with accumulating cache, session analytics (Asia/London/overlap/NY), trade-level backtester with tick-accurate costs (MGC/GC), strategies (opening-range breakout, VWAP reversion, momentum burst), walk-forward + cost-sensitivity validation |
| **Leverage sizing** | Fractional Kelly ∧ vol targeting ∧ drawdown governor ∧ conviction scaling, capped per instrument (futures / CFD / 2x-3x ETP) |
| **ETP analytics** | Daily-reset volatility decay: closed-form drag, breakeven drift, reset-vs-static simulation |
| **Backtesting** | Daily engine with financing costs, expense ratios, transaction costs, margin liquidation modelling |
| **Monte Carlo** | Stationary block bootstrap (preserves vol clustering) → ruin probability, drawdown distribution, empirical Kelly curve |
| **Stress tests** | Replay of 2008, Apr-2013, 2013 taper, Mar-2020, 2022 rate shock + overnight gap grid, with margin-call detection |
| **Reporting** | One-command markdown + JSON report (`reports/`) |

## Quick start

```bash
pip install -e .
goldstein fetch        # refresh market data (needs network; degrades gracefully)
goldstein report       # full analysis → reports/analysis_<stamp>.{md,json}
```

Key commands (all support `--json` for machine consumption):

```bash
goldstein analyze  --instrument futures --capital 10000   # full analysis to stdout
goldstein backtest --leverage 2                            # constant-leverage backtest
goldstein backtest                                         # adaptive vol-target × signal
goldstein montecarlo --sweep                               # risk across 0.5x–5x
goldstein stress --leverage 3 --instrument cfd             # survival check
goldstein decay --vol 0.20                                 # ETP decay tables
goldstein validate --save                                  # full backtest validation report
goldstein monitor                                          # update latest.*/history.csv + diff advice
goldstein doctor                                           # cache + network diagnostics
```

## Autonomous operation

Two scheduled workflows keep the repo alive without human intervention:

- **`daily-update.yml`** (weekdays 05:45 UTC) — `goldstein fetch` on a network-open runner → `goldstein monitor` → commits `data/cache/`, `reports/latest.{md,json}`, `reports/history.csv` → opens a `goldstein-alert` issue when leverage advice, direction, regime or vol forecast materially change.
- **`weekly-validation.yml`** (Saturday) — full test suite + `goldstein validate --save` on fresh data, committed as `reports/validation_latest.{md,json}`.

Any Claude agent (including from the mobile app) can then read `reports/latest.json` / `history.csv` for the current state without needing network access to data providers.

## Design principles

1. **Leverage errors are asymmetric** — the recommendation is the *minimum* of independent caps (Kelly, vol target, drawdown governor, instrument limits), never an average.
2. **No edge → no leverage** — sizing is scaled by signal conviction and zeroed when flat.
3. **Survivability first** — every recommendation is stress-replayed through gold's worst historical episodes with margin mechanics.
4. **Agent-native** — headless CLI, stable JSON outputs, offline degradation, deterministic seeds. See [CLAUDE.md](CLAUDE.md) for the agent operating manual.

## Disclaimer

Research tooling, **not investment advice**. Leveraged positions can lose more than the initial capital. All model outputs carry material estimation uncertainty.
