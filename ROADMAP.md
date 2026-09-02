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
   with per-row source labels, CPI deflator, drawdown-episode analytics,
   validation gates; the committed cache (`data/cache/XAUUSD_CENTURY.csv`,
   `CPIAUCNS.csv`) makes it fully offline. **Century stress scenarios —
   DONE**: 1974-76, 1980-82, 1980-99 and 2011-15 replay from the committed
   series inside `risk/stress.py` with era-appropriate financing, and the
   report carries a separate `survives_all_century` verdict (month-close
   paths understate intramonth pain: failing is definitive, passing is only
   necessary). Next data upgrade: replace the 1968-2000 monthly datahub
   segment with the LBMA daily fix if/when FRED becomes reachable from CI.
2. **Realized volatility — DONE**: HAR runs on true daily RV (sum of
   squared 5m returns, CME trade-date sessions) from the committed intraday
   cache, spliced with the bias-adjusted squared-return proxy for earlier
   history; the report states the source and splice date, and everything
   degrades to the proxy when the cache is absent.
3. **Forecast uncertainty — DONE**: blend weights come from a rolling
   out-of-sample QLIKE evaluation (EWMA/HAR truly OOS, GARCH pseudo-OOS
   with full-sample parameters — documented), floored and renormalized,
   falling back to fixed thirds on short histories; a joint (return, RV)
   stationary-block-bootstrap 5-95% band on the blended forecast ships in
   every report. Known limit, stated in the code: the band excludes GARCH
   parameter uncertainty (200 MLE refits per report is not worth the
   wall-clock).
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
