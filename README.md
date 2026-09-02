# GOLDSTEIN

**Quant research & risk platform for leveraged gold investing, with a
century of committed price history — designed to be operated end-to-end by
Claude agents (mobile, web, or CLI) and equally friendly to humans.**

GOLDSTEIN answers one question with institutional-grade machinery: *how much
leverage on gold, right now, through which instrument — and would the
position survive?* Including the part most tools skip: would it have
survived 1974-76, 1980-82, and the two-decade bear that followed.

## Start in 60 seconds

```bash
git clone <this-repo> && cd GOLDSTEIN
pip install -e .              # deps: numpy, pandas, scipy, requests — nothing exotic
python -m pytest tests/       # 61 offline tests, ~1 min, no network needed
goldstein report              # full analysis → reports/analysis_<stamp>.{md,json}
```

That's it. **The repo ships with its data**: committed caches cover gold
daily from 2000, a spliced 1920→today century series, US CPI from 1913,
5-minute intraday bars, and the macro series — so every command works
offline out of the box. `goldstein fetch` refreshes them when you have
network; with no cache and no network, output is generated from synthetic
data and loudly flagged `DEMO DATA`.

## What a report gives you

One command (`goldstein report`) chains the whole pipeline:

market snapshot → **vol forecast** (EWMA + GARCH-MLE + HAR on true 5m
realized variance, blended with weights earned by rolling out-of-sample
QLIKE, with a bootstrap 5-95% band) → **regime** (Gaussian HMM + macro
score) → **signal ensemble** (momentum, trend, mean-reversion, macro,
cross-asset confirmation) → **leverage recommendation** (min of fractional
Kelly, vol target, drawdown governor, instrument caps — never an average) →
**Monte Carlo ruin analysis** → **stress tests** (modern episodes + the
century's real worst cases with era financing) → ETP decay → strategy
backtest.

## Command reference

All analysis commands accept `--instrument {futures,cfd,etp2x,etp3x,etf1x}`,
`--capital`, `--json`, `--seed` and more (`goldstein <cmd> --help`).

| Command | Purpose |
|---|---|
| `goldstein report` / `analyze` | full pipeline, saved to `reports/` / to stdout |
| `goldstein century [--fetch]` | 1920→today series + long-run analytics: real/nominal CAGR, drawdown episodes (1980→2001: −83% real), vol by decade |
| `goldstein backtest [--leverage L]` | constant or adaptive (vol-target × signal) backtest: FedFunds-path financing, fees, roll drag, liquidation |
| `goldstein montecarlo [--sweep]` | block-bootstrap ruin/drawdown risk, empirical Kelly curve |
| `goldstein stress --leverage L` | modern + century scenarios + gap grid, margin-call detection |
| `goldstein validate [--save]` | strategy suite, walk-forward, PSR, **deflated Sharpe**, **White reality check**, sensitivity → 7-check verdict |
| `goldstein decay [--vol σ]` | daily-reset ETP decay math |
| `goldstein monitor` | refresh `reports/latest.*` + `history.csv`, diff the advice |
| `goldstein doctor` | cache freshness, network probes, **cross-source data quality check** |
| `goldstein fetch` | refresh all series (Stooq → Yahoo → FRED) |
| `goldstein intraday …` | 5m/60m scalping research layer (see `CLAUDE.md`) |

## The data story

- **Live → cache → synthetic**, per series, with `df.attrs["source"]` and a
  DEMO banner so nothing synthetic ever masquerades as market data.
- **Century series** (`data/cache/XAUUSD_CENTURY.csv`): official peg
  1920-67 → LBMA-derived monthly 1968-2000 → daily 2000→today, every row
  labeled with its source; CPI 1913→ for real terms. Validation gates refuse
  era gaps and bad joins. There is deliberately **no synthetic fallback** for
  the century — an honest gap beats an invented past.
- **Self-updating**: `daily-update.yml` (weekdays) fetches real data on a
  GitHub runner, refreshes `reports/latest.*` + `history.csv`, commits the
  cache, and opens a `goldstein-alert` issue when the advice materially
  changes; `weekly-validation.yml` re-runs the full validation every
  Saturday. A cloned repo is fresh without anyone running anything.

## Honesty machinery (what makes the numbers trustworthy)

- **No lookahead**: signals are point-in-time, the engine lags leverage one
  bar, and tests enforce truncation invariance.
- **Determinism**: same seed ⇒ same synthetic data, same Monte Carlo.
- **Multiple-testing control**: every configuration the validation examines
  counts as a trial; the Deflated Sharpe and a White reality check price in
  the "we tried many things and kept the best" bias.
- **Century stress**: the recommendation is replayed through 1974-76,
  1980-82, 1980-99 and 2011-15 at era financing rates (14%/yr in the
  Volcker episode), with a separate `survives_all_century` verdict.
- **Uncertainty shown, not hidden**: the vol forecast ships with a bootstrap
  5-95% band; reports state which data fed HAR and from what date.
- Failures are reported as failures. A ❌ in the verdict stays a ❌.

## Also in this repo

`perp/` is a **separate, self-contained subproject** (own README): a
backtesting pipeline for a discretionary crypto-perp strategy on ETH/BTC/SOL
at 10-100x with candle-level liquidation simulation. It shares nothing with
the gold platform except the repo. Its conclusion so far, honestly stated in
`perp/README.md`: no tested configuration survives costs.

`ROADMAP.md` tracks the platform's state-of-the-art gap list — what is done,
what is simplified (and where), and what comes next. `CLAUDE.md` is the
agent operating manual (setup, invariants, workflows).

## Design principles

1. **Leverage errors are asymmetric** — the recommendation is the *minimum*
   of independent caps, never an average; flat signal ⇒ 0x.
2. **Survivability first** — every recommendation must face the century's
   worst, not just the last 20 years.
3. **Offline-first, agent-native** — headless CLI, stable JSON, committed
   caches, deterministic seeds, graceful degradation.
4. **Honesty over polish** — DEMO banners, labeled sources, deflated
   statistics, documented simplifications.

## Disclaimer

Research tooling, **not investment advice**. Leveraged positions can lose
more than the initial capital. All model outputs carry material estimation
uncertainty — the report now quantifies some of it, which is not the same
as eliminating it.
