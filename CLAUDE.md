# CLAUDE.md — Agent Operating Manual

GOLDSTEIN is built to be run by Claude agents (mobile app, web, CLI) with zero
human setup. Read this before doing anything else in the repo.

## Setup (once per session)

```bash
pip install -e .          # deps: numpy, pandas, scipy, requests only
python -m pytest tests/   # 13 offline tests, ~5s — run after any change
```

## The one command that matters

```bash
goldstein report --instrument futures --capital 10000
```

Produces `reports/analysis_<stamp>.md` (human) and `.json` (machine) with:
market snapshot → vol forecast (EWMA/GARCH/HAR blend) → HMM + macro regime →
signal ensemble → **leverage recommendation** → Monte Carlo ruin analysis →
leverage sweep → historical stress tests → ETP decay → strategy backtest.

Instruments: `futures` (COMEX, margin mechanics), `cfd` (retail margin),
`etp2x`/`etp3x` (daily-reset ETPs with decay), `etf1x` (unlevered benchmark).

## Data reality — read carefully

Market-data endpoints are often **blocked** in agent sandboxes. The data layer
degrades: **live → local CSV cache (`data/cache/`) → synthetic**. Reports on
synthetic data carry a `DEMO DATA` banner and `"demo_data": true` in JSON.

Protocol:
1. Run `goldstein doctor` to check network + cache state.
2. If a provider is reachable, run `goldstein fetch` — this refreshes
   `data/cache/*.csv`. **Commit the updated cache** so offline sessions
   inherit real data.
3. If everything is blocked and no cache exists, results are DEMO. Never
   present DEMO numbers as market analysis — say so explicitly.
4. A user can also supply data manually: drop a CSV at
   `data/cache/XAUUSD.csv` with columns `date,open,high,low,close,volume`
   (macro series: `date,value`).

## Command reference

| Command | Purpose |
|---|---|
| `goldstein doctor` | cache freshness + network probes |
| `goldstein fetch` | refresh all series (Stooq → Yahoo → FRED) |
| `goldstein analyze [--json]` | full analysis to stdout |
| `goldstein report` | same, saved to `reports/` |
| `goldstein backtest [--leverage L]` | constant-L or adaptive (vol-target × signal) backtest |
| `goldstein montecarlo [--leverage L] [--sweep]` | block-bootstrap risk / Kelly curve |
| `goldstein stress --leverage L` | historical + gap scenarios, margin-call check |
| `goldstein decay [--vol σ]` | daily-reset ETP decay math |
| `goldstein validate [--quick] [--save]` | strategy suite, walk-forward, PSR, sensitivity → verdict |
| `goldstein monitor` | refresh `reports/latest.*` + `history.csv`, JSON diff of advice changes |

All analysis commands accept `--instrument`, `--capital`, `--json`,
`--target-vol`, `--kelly-fraction`, `--max-leverage`, `--mc-paths`, `--seed`.

## Architecture map

```
src/goldstein/
  config.py         universe, instrument specs (margin, fees, spreads), Settings
  data/providers.py live→cache→synthetic ladder; df.attrs["source"] tells you which
  data/synthetic.py deterministic 3-regime generator (offline demo)
  features/         returns, momentum, RSI, Parkinson vol, drawdown
  models/volatility.py  EWMA, GARCH(1,1) MLE, HAR-RV, blended forecast
  models/regime.py      Gaussian HMM (EM) + macro regime score
  models/signals.py     ensemble signal + point-in-time signal_history()
  models/crossasset.py  correlations/betas vs silver, GDX, DXY, SPX, WTI, BTC;
                        gold/silver z, miners leadership, lead-lag vs real yields;
                        confirmation score feeding the signal ensemble
  leverage/sizing.py    Kelly / vol-target / drawdown governor → advise()
  leverage/decay.py     ETP daily-reset decay analytics
  backtest/engine.py    daily engine: financing, fees, tc, liquidation
  backtest/montecarlo.py stationary block bootstrap, leverage_sweep()
  backtest/validation.py strategy suite, walk-forward buckets, PSR, sensitivity
  report/monitor.py      latest.* + history.csv + material-change diff
  risk/stress.py        historical scenario replay + gap grid
  report/generate.py    analyze() = whole pipeline as one dict; markdown renderer
```

## Invariants — do not break

- **No lookahead**: the engine shifts leverage by one bar; `signal_history()`
  only uses expanding history. Any new signal must be point-in-time.
- **Recommendation = min(caps)**, never an average. Flat signal ⇒ 0x.
- **Offline-first**: everything must run with no network (tests enforce this).
- **Determinism**: same seed ⇒ same synthetic data, same MC results.
- Keep dependencies to numpy/pandas/scipy/requests — agent sandboxes may not
  install heavier packages.

## Typical agent workflows

- *"Analisi oro con leva"* → `goldstein fetch` (best-effort) →
  `goldstein report` → summarize the markdown, flag DEMO if applicable.
- *"Quanto posso leverare in sicurezza?"* → `goldstein montecarlo --sweep`
  + `goldstein stress --leverage <candidate>` → discuss ruin/DD trade-off.
- *"Conviene un ETF 3x?"* → `goldstein decay --vol <current forecast>` +
  compare `--instrument etp3x` vs `futures` reports.
- *"La strategia funziona davvero?"* → `goldstein validate --save`; relay the
  5-check verdict, walk-forward table and PSR honestly (including failures).
- *"Che sta succedendo?"* (mobile quick check) → read `reports/latest.json`
  and `reports/history.csv` — the daily automation keeps them fresh; no
  network needed. Compare the last rows of history.csv for the trend.

## Autonomous loop (already wired)

`.github/workflows/daily-update.yml` runs weekdays: fetch (real network on
GitHub runners) → `goldstein monitor` → commits cache + latest reports +
history → opens a `goldstein-alert` issue on material changes.
`weekly-validation.yml` re-runs the full validation every Saturday.
If you are asked why data is fresh without anyone running fetch: that's why.
Never edit `reports/latest.*` or `history.csv` by hand — the automation owns
them and hand edits create merge noise.

## Safety rules for agents

- Always show the DEMO banner status and the disclaimer when relaying results.
- Never present the output as personalized financial advice; it is model
  research with stated assumptions.
- If the user asks for more leverage than the stress tests survive, show the
  failing scenario table rather than silently complying.
