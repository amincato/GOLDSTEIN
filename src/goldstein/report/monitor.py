"""Autonomous monitoring: stable latest-report files, longitudinal history,
and change detection between runs.

`goldstein monitor` is the command the scheduled automation (GitHub Actions
cron, Claude Routine, or any cron) runs daily:
  1. full analysis → reports/latest.md + reports/latest.json (stable paths)
  2. append one row to reports/history.csv (longitudinal record)
  3. diff vs the previous latest.json → list of material changes
  4. print a machine-readable summary; exit code 0 always (changes are data,
     not errors)

"Material change" = leverage advice moves ≥ 0.25x, direction flips, regime
label changes, vol forecast moves ≥ 3 vol points, or data source changes.
"""

from __future__ import annotations

import json
from pathlib import Path

from ..config import REPORT_DIR

LATEST_MD = "latest.md"
LATEST_JSON = "latest.json"
HISTORY_CSV = "history.csv"

_HISTORY_COLS = [
    "date", "data_mode", "price", "vol_forecast", "hmm_regime", "macro_regime",
    "signal_score", "direction", "recommended_leverage", "prob_ruin",
]


def snapshot(analysis: dict) -> dict:
    """The small comparable state extracted from a full analysis dict."""
    return {
        "date": analysis["market"]["last_date"],
        "data_mode": "demo" if analysis["demo_data"] else "real",
        "price": round(analysis["market"]["last_price"], 2),
        "vol_forecast": round(analysis["volatility"]["blended_forecast"], 4),
        "hmm_regime": analysis["regime"]["hmm_state"],
        "macro_regime": analysis["regime"]["macro_label"],
        "signal_score": round(analysis["signal"]["score"], 3),
        "direction": analysis["leverage_advice"]["direction"],
        "recommended_leverage": analysis["leverage_advice"]["recommended"],
        "prob_ruin": analysis["monte_carlo"]["prob_ruin"],
    }


def diff(prev: dict | None, curr: dict) -> list[str]:
    if prev is None:
        return ["first run — baseline recorded"]
    changes = []
    if abs(curr["recommended_leverage"] - prev.get("recommended_leverage", 0)) >= 0.25:
        changes.append(
            f"leverage advice {prev.get('recommended_leverage')}x → "
            f"{curr['recommended_leverage']}x"
        )
    if curr["direction"] != prev.get("direction"):
        changes.append(f"direction {prev.get('direction')} → {curr['direction']}")
    if curr["hmm_regime"] != prev.get("hmm_regime"):
        changes.append(f"HMM regime {prev.get('hmm_regime')} → {curr['hmm_regime']}")
    if curr["macro_regime"] != prev.get("macro_regime"):
        changes.append(f"macro regime {prev.get('macro_regime')} → {curr['macro_regime']}")
    if abs(curr["vol_forecast"] - prev.get("vol_forecast", 0)) >= 0.03:
        changes.append(
            f"vol forecast {prev.get('vol_forecast'):.1%} → {curr['vol_forecast']:.1%}"
        )
    if curr["data_mode"] != prev.get("data_mode"):
        changes.append(f"data mode {prev.get('data_mode')} → {curr['data_mode']}")
    return changes


def update_latest(analysis: dict, report_dir: Path | None = None) -> dict:
    """Write latest.{md,json}, append history, return the change summary."""
    from . import generate

    rd = Path(report_dir or REPORT_DIR)
    rd.mkdir(parents=True, exist_ok=True)

    prev_snap = None
    latest_path = rd / LATEST_JSON
    if latest_path.exists():
        try:
            prev_snap = snapshot(json.loads(latest_path.read_text()))
        except Exception:
            prev_snap = None

    (rd / LATEST_MD).write_text(generate.render_markdown(analysis))
    latest_path.write_text(json.dumps(analysis, indent=2, default=str))

    snap = snapshot(analysis)
    hist = rd / HISTORY_CSV
    line = ",".join(str(snap[c]) for c in _HISTORY_COLS)
    if not hist.exists():
        hist.write_text(",".join(_HISTORY_COLS) + "\n" + line + "\n")
    else:
        # avoid duplicate rows for the same market date (idempotent reruns)
        lines = [l for l in hist.read_text().splitlines()
                 if l and not l.startswith(str(snap["date"]) + ",")]
        lines.append(line)
        hist.write_text("\n".join(lines) + "\n")

    changes = diff(prev_snap, snap)
    return {
        "changed": bool(changes),
        "changes": changes,
        "snapshot": snap,
        "previous": prev_snap,
        "paths": {"markdown": str(rd / LATEST_MD), "json": str(latest_path),
                  "history": str(hist)},
    }
