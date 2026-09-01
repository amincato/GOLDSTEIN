# ROADMAP — GOLDSTEIN toward objective state-of-the-art

GOLDSTEIN's mandate: **quant research software for gold with a complete
century-scale dataset, at the best level honestly achievable within its own
invariants** — numpy/pandas/scipy only, offline-first, deterministic,
operated by agents with no human setup. "SOTA" here means best published
practice implemented rigorously, not ML buzzwords: with these constraints
the ceiling is institutional-grade *research* tooling, and every claim below
is falsifiable by running the test suite and validation commands.

## Already at good-practice level (verified, keep it that way)

- Vol forecasting: EWMA + GARCH(1,1) by MLE + HAR-RV, blended.
- Regimes: Gaussian HMM by EM + macro score; signals are point-in-time.
- Validation: walk-forward buckets, PSR, cost sensitivity, honest verdicts.
- Risk: stationary block-bootstrap MC, historical stress replay, margin
  mechanics per instrument, daily-reset ETP decay math.
- Discipline: no-lookahead enforced by tests, offline-first, DEMO banners.

## Gap list (priority order)

1. **Century dataset — DONE (this branch)**: 1920→today spliced series
   (official peg → NBER → LBMA fix → modern cache) with per-row source
   labels, CPI deflator, drawdown-episode analytics, validation gates.
   Next: wire the 1971-80 and 1980-82 and 2011-15 REAL-price episodes into
   `risk/stress.py` as first-class scenarios (they are worse than anything
   in the current scenario set).
2. **Realized volatility**: feed HAR with true RV from the 5m intraday
   cache where it exists instead of the Parkinson proxy; document the
   splice date.
3. **Forecast uncertainty**: bootstrap CIs on GARCH/HAR parameters; blend
   weights chosen by rolling out-of-sample loss instead of fixed thirds.
4. **Multiple-testing honesty**: extend the patterns reality-check
   bootstrap (White/SPA-style) to every strategy family the validate
   command sweeps; report deflated Sharpe alongside PSR.
5. **Futures realism**: roll costs from term structure, financing from the
   actual FedFunds path, exchange margin-tier tables for GC/MGC.
6. **Data quality gates**: `doctor` should cross-check XAUUSD cache against
   a second source and flag divergence > tolerance, not just staleness.

## Non-goals

- ML black boxes (violates the dependency and interpretability invariants).
- Order placement anywhere. Research only.
- Pretending pre-1968 peg prices are backtestable market data — they are
  context, clearly labeled, never fed to the strategy engines.
