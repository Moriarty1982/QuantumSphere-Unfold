#!/usr/bin/env python3
"""Check the research-candidate build in GitHub Actions.

The preview build step runs with continue-on-error, so a failed or incomplete
build of the v4.9.0 research candidate would otherwise pass green. This check
reads the build summaries written by qsc_latex_build.py and fails the job if
the candidate under `sources/research/` was not built cleanly.

Hard checks (all must hold for every research result):
- latexmk return code 0 and a PDF present,
- no fatal errors,
- no undefined references and no undefined citations,
- no multiply defined labels,
- no rerun warning left in the final log.

Overfull boxes are reported but not checked: their count depends on the TeX
distribution (45 under TeX Live 2022, 58 under MiKTeX 25.12 for the same source).
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

RESEARCH_MARKER = "sources/research/"


def log_counts(tex_log: str | None) -> dict:
    counts = {"duplicate_labels": None, "rerun": None}
    if tex_log and Path(tex_log).exists():
        text = Path(tex_log).read_text(encoding="utf-8", errors="replace")
        counts["duplicate_labels"] = text.count("multiply defined")
        counts["rerun"] = text.count("Rerun to get") + text.count("Label(s) may have changed")
    return counts


def main(argv: list[str]) -> int:
    results = []
    for arg in argv:
        path = Path(arg)
        if not path.exists():
            continue
        summary = json.loads(path.read_text(encoding="utf-8"))
        for r in summary.get("results", []):
            if RESEARCH_MARKER in r.get("tex", "").replace("\\", "/"):
                results.append(r)

    lines = ["## Research candidate build check", ""]
    if not results:
        lines.append("No build result for `sources/research/` was found.")
        print("::error title=Research candidate not built::no result for sources/research/ in the build summaries")
        write_summary(lines)
        return 1

    lines += [
        "| TEX | return code | PDF | fatal | undefined refs | undefined cites | duplicate labels | rerun | overfull hbox | verdict |",
        "|---|---:|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    failed = False
    for r in results:
        r.update(log_counts(r.get("tex_log")))
        problems = []
        if r.get("returncode") != 0:
            problems.append(f"return code {r.get('returncode')}")
        if not r.get("pdf"):
            problems.append("no PDF")
        for key in ("fatal_errors", "undefined_refs", "undefined_citations", "duplicate_labels", "rerun"):
            value = r.get(key)
            if value is None:
                problems.append(f"{key} not determined")
            elif value != 0:
                problems.append(f"{key} = {value}")
        verdict = "ok" if not problems else "FAILED: " + "; ".join(problems)
        if problems:
            failed = True
            print(f"::error title=Research candidate build check failed::{r.get('tex')}: {'; '.join(problems)}")
        lines.append(
            f"| `{r.get('tex')}` | {r.get('returncode')} | {'yes' if r.get('pdf') else 'no'} | "
            f"{r.get('fatal_errors')} | {r.get('undefined_refs')} | {r.get('undefined_citations')} | "
            f"{r.get('duplicate_labels')} | {r.get('rerun')} | {r.get('overfull_hbox')} | {verdict} |"
        )

    lines += ["", "Overfull boxes are reported, not checked (distribution-dependent)."]
    write_summary(lines)
    print("\n".join(lines))
    return 1 if failed else 0


def write_summary(lines: list[str]) -> None:
    target = os.environ.get("GITHUB_STEP_SUMMARY")
    if target:
        with open(target, "a", encoding="utf-8") as handle:
            handle.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
