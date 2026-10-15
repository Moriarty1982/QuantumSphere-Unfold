"""Extract, verify and measure a full-v4.7-derived v4.8 research reading route.

Extraction is a mechanical byte partition. No original source bytes may be
omitted, duplicated or edited in the inherited fragments. New editorial and
research material lives outside those fragments. CRLF/LF checkout conversion
is explicitly recorded and accepted; no other content changes are allowed.
This is not a proof checker.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "release/v4.7.0/Quantum_Sphaera_Companion_v4_7_0_source (2).tex"
WORKING = ROOT / "sources/research"
MANIFEST = WORKING / "v480-source-map.json"

# Each anchor starts a disjoint fragment in the original source order.
ANCHORS = (
    ("00_preamble", None),
    ("01_opening", r"\begin{document}"),
    ("02_release_frontmatter", r"\section*{v4.7.0 Full-Monolith Release Scope and Provenance Notice}"),
    ("03_contents", r"\tableofcontents"),
    ("04_doi_provenance", r"\subsection*{Prior DOI provenance note}"),
    ("05_orbit_scan", r"\section{Alternating Triolic Orbit Scan and Hopf-Fibre Core Surface Readout}"),
    ("06_prior_reader_navigation", r"\section*{Current Reader Navigation and Governing Map}"),
    ("07_qam_infrastructure", r"\section*{Working orientation for \docversion}"),
    ("08_nomenclature", r"\section*{Nomenclature}"),
    ("09_preclosure_memory", r"\section*{Historical tool layer and pre-closure live cores}"),
    ("10_sphaera_and_physics", r"\section{The Central Theorem}"),
    ("11_legacy_synthesis", r"\section*{\QSCver{v1.7.0} Closure--Projection Synthesis Core}"),
    ("12_structural_core", r"\section{Structural Core and Closure Principles}"),
    ("13_hc_hypotheses", r"\section{Hypothesis 7.4: The Heisenberg--Compensator Matrix as a Meta-Field Generator}"),
    ("14_local_crystal", r"\section{Closure-Liquid Crystal and Holographic Julia Boundary}"),
    ("15_hc_repair_and_transport", r"\begin{definition}[Local compact reinforcement pair]"),
    ("16_master_model", r"\section{Toward a Structural ToE Master Equation}"),
    ("17_open_question_genealogy", r"\section*{Open Questions}"),
    ("18_op1_op2_mathematics", r"\subsection{The single underlying gap}"),
    ("19_local_op_entry", r"\begin{theorem}[First machine-fused coupled OP-entry theorem]"),
    ("20_frame_and_teichmueller", r"\begin{theorem}[Self-consistent determination of $\gL$]"),
    ("21_inflow_and_transport_statement", r"\section{Hypothesis subversion: inflow paradigm and cosmological extensions}"),
    ("22_op_transport_arguments", r"\section*{Technical unfolding of the OP transport architecture}"),
    ("23_physical_readouts", r"\subsection[The neutrino k-value]"),
    ("24_computational_specification", r"\section{Computational Interpretation, Enigma Analogy, and Bomba-Style Structural Search}"),
    ("25_appendix_switch", "\\appendix\n\\setcounter{section}{0}"),
    ("26_inherited_technical_appendices", r"\section{Structural Tools for the Millennium Matrix}"),
    ("27_machine_audit_provenance", "\\appendix\n\\section{Provenance and Machine-Audit Layer}"),
    ("28_bibliography", r"\begin{thebibliography}{99}"),
    ("29_shifted_qam", r"\section{\QSCver{legacy.37.0} Migration Map and Backtranslation Contract for the shifted QAM Shift}"),
    ("30_reader_hygiene_history", r"\section{\QSCver{shifted.0.13} Historical Remark Triage and Reader-Hygiene Cleanup}"),
    ("31_op_selector_and_routes", r"\section{OP-Facing Diagnostic Appendix}"),
    ("32_atlas_and_op_promotion", r"\providecommand{\safeop}[1]{\mathsf{#1}}"),
    ("33_bounded_readout_scope", r"\section*{v4.6.0 Integrated Bounded-Readout and T2 Scope-Boundary Appendix}"),
    ("34_mm_hc_and_c5_development", r"\section{Content-State Refresh and v4.7 Handoff Preflight}"),
    ("35_guarded_solve_chain", r"\section{Compressed Post-r54 Guarded Solve Chain: r55--r80}"),
    ("36_frame_typed_endpoint", r"\section{r81 Matter-frame epsilon terminality and Planck/information scale split}"),
    ("37_closing", r"\end{document}"),
)

INPUT = re.compile(r"(?m)^[ \t]*\\input\{([^{}\n]+)\}")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(raw):
    return raw.replace(b"\r\n", b"\n")


def partition(raw):
    newline = b"\r\n" if b"\r\n" in raw else b"\n"
    positions = []
    for name, anchor in ANCHORS:
        token = anchor.encode("utf-8").replace(b"\n", newline) if anchor else None
        if token and raw.count(token) != 1:
            raise ValueError(f"Anchor must occur exactly once: {name}")
        positions.append((name, raw.index(token) if token else 0))
    if [pos for _, pos in positions] != sorted(pos for _, pos in positions):
        raise ValueError("Fragment anchors are out of source order")
    result = []
    for index, (name, start) in enumerate(positions):
        end = positions[index + 1][1] if index + 1 < len(positions) else len(raw)
        result.append((name, start, end, raw[start:end]))
    return result


def source_map(raw, fragments):
    records = []
    offset = 0
    for name, start, end, content in fragments:
        normalized = canonical(content)
        records.append({"path": f"parts/v470/{name}.tex",
                        "start_byte": start, "end_byte": end,
                        "original_first_line": raw[:start].count(b"\n") + 1,
                        "bytes": len(content), "sha256": sha(content),
                        "canonical_start_byte": offset,
                        "canonical_end_byte": offset + len(normalized),
                        "canonical_bytes": len(normalized),
                        "canonical_sha256": sha(normalized)})
        offset += len(normalized)
    return {"origin": SOURCE.relative_to(ROOT).as_posix(),
            "origin_sha256": sha(raw), "origin_bytes": len(raw),
            "canonical_origin_sha256": sha(canonical(raw)),
            "canonical_origin_bytes": len(canonical(raw)),
            "line_ending_policy": "CRLF/LF checkout conversion only; captured and canonical LF offsets/hashes are both recorded.",
            "published_pdf_pages": 1014,
            "working_entry": "v480-companion.tex", "fragments": records}


def extract():
    if MANIFEST.exists():
        raise ValueError("Source map already exists; use check, not destructive regeneration")
    raw = SOURCE.read_bytes()
    fragments = partition(raw)
    folder = WORKING / "parts/v470"
    folder.mkdir(parents=True, exist_ok=True)
    for name, start, end, content in fragments:
        path = folder / f"{name}.tex"
        if path.exists():
            raise ValueError(f"Refusing to overwrite {path}")
        path.write_bytes(content)
    manifest = source_map(raw, fragments)
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"fragments": len(fragments), "bytes_preserved": len(raw), "origin_sha256": sha(raw)}, indent=2))


def portable_map():
    """Add portable hashes without changing any inherited file or captured offset."""
    old = json.loads(MANIFEST.read_text(encoding="utf-8"))
    raw = SOURCE.read_bytes()
    if sha(raw) != old["origin_sha256"]:
        raise ValueError("Cannot refresh a map against a changed captured origin")
    for item in old["fragments"]:
        if sha((WORKING / item["path"]).read_bytes()) != item["sha256"]:
            raise ValueError(f"Cannot refresh a modified fragment: {item['path']}")
    MANIFEST.write_text(json.dumps(source_map(raw, partition(raw)), indent=2) + "\n", encoding="utf-8")
    print("Recorded portable LF hashes; inherited source files unchanged.")


def expand(path, files=None, ancestors=()):
    files = files if files is not None else []
    path = path.resolve()
    if path in ancestors:
        raise ValueError(f"Cyclic input: {path}")
    if not path.is_relative_to(WORKING.resolve()):
        raise ValueError(f"Input outside the research source tree: {path}")
    files.append(path)
    text = path.read_text(encoding="utf-8")

    def include(match):
        child = WORKING / match[1]
        if not child.suffix:
            child = child.with_suffix(".tex")
        return expand(child, files, (*ancestors, path))

    return INPUT.sub(include, text)


def labels(text):
    text = re.sub(r"(?m)(?<!\\)%[^\n]*", "", text)
    return Counter(re.findall(r"\\label\{([^{}]+)\}", text))


def check():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    origin = (ROOT / manifest["origin"]).read_bytes()
    if sha(canonical(origin)) != manifest["canonical_origin_sha256"]:
        raise ValueError("Frozen origin changed")
    contents = []
    previous_end = 0
    for item in manifest["fragments"]:
        content = (WORKING / item["path"]).read_bytes()
        normalized = canonical(content)
        if (item["canonical_start_byte"] != previous_end
                or item["canonical_end_byte"] - previous_end != len(normalized)):
            raise ValueError(f"Coverage gap or overlap: {item['path']}")
        if sha(normalized) != item["canonical_sha256"]:
            raise ValueError(f"Inherited fragment was modified: {item['path']}")
        contents.append(content)
        previous_end = item["canonical_end_byte"]
    if b"".join(canonical(content) for content in contents) != canonical(origin):
        raise ValueError("Reassembled inherited source does not equal the complete original")
    files = []
    text = expand(WORKING / manifest["working_entry"], files)
    counts = Counter(files)
    if len(counts) != len(files):
        raise ValueError("A source file is included more than once")
    for item in manifest["fragments"]:
        if counts[(WORKING / item["path"]).resolve()] != 1:
            raise ValueError(f"Missing inherited fragment: {item['path']}")
    before, after = labels(origin.decode("utf-8")), labels(text)
    missing = before - after
    duplicate = {key: count for key, count in after.items() if count > max(1, before[key])}
    if missing or duplicate:
        raise ValueError(f"Label loss/duplication: {dict(missing)}, {duplicate}")
    return {"origin_sha256": sha(origin), "canonical_origin_sha256": sha(canonical(origin)),
            "original_bytes_preserved": len(origin),
            "byte_identical_reconstruction_in_current_checkout": b"".join(contents) == origin,
            "inherited_fragments": len(contents), "included_files": len(files),
            "original_label_occurrences": sum(before.values()),
            "new_label_occurrences": sum((after - before).values()),
            "missing_labels": dict(missing), "new_duplicate_labels": duplicate,
            "working_expanded_sha256": sha(text.encode("utf-8"))}


def aux_pages(path, first_appendix):
    text = path.read_text(encoding="utf-8")
    total = re.search(r"\\gdef\s*\\@abspage@last\{(\d+)\}", text)
    boundary = re.search(r"\\newlabel\{" + re.escape(first_appendix) + r"\}\{\{[^{}]*\}\{(\d+)\}", text)
    if not total or not boundary:
        raise ValueError(f"Missing settled page information in {path}")
    total, start = int(total[1]), int(boundary[1])
    return {"total": total, "main_and_frontmatter": start - 1,
            "appendices_and_bibliography": total - start + 1}


def measure(before_aux, after_aux, output):
    result = check()
    files = []
    expand(WORKING / "v480-companion.tex", files)
    if max(path.stat().st_mtime for path in files) > after_aux.stat().st_mtime:
        raise ValueError("Research source is newer than its AUX; compile before measuring")
    for aux in (before_aux, after_aux):
        log = aux.with_suffix(".log").read_text(encoding="utf-8", errors="replace")
        if any(token in log for token in ("Label(s) may have changed", "Table widths have changed", "Rerun LaTeX", "undefined references", "undefined citations")):
            raise ValueError(f"Unsettled references/tables in {aux.with_suffix('.log')}")
    result["published_pdf_pages"] = 1014
    result["baseline_rebuilt_pages"] = aux_pages(before_aux, "app:mm-tools")
    result["research_pages"] = aux_pages(after_aux, "v480:appendix-start")
    result["baseline_matches_published_page_count"] = result["baseline_rebuilt_pages"]["total"] == 1014
    if not result["baseline_matches_published_page_count"]:
        raise ValueError("Rebuilt baseline does not match the published 1,014-page document")
    for name, aux in (("baseline", before_aux), ("research", after_aux)):
        log = aux.with_suffix(".log").read_text(encoding="utf-8", errors="replace")
        result[f"{name}_layout_warnings"] = {
            "overfull_boxes": len(re.findall(r"(?m)^Overfull", log)),
            "duplicate_destinations": log.count("destination with the same identifier"),
        }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("extract")
    sub.add_parser("check")
    sub.add_parser("portable-map")
    metric = sub.add_parser("measure")
    metric.add_argument("--before-aux", type=Path, required=True)
    metric.add_argument("--after-aux", type=Path, required=True)
    metric.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "extract":
        extract()
    elif args.command == "portable-map":
        portable_map()
    elif args.command == "check":
        print(json.dumps(check(), indent=2))
    else:
        print(json.dumps(measure(args.before_aux, args.after_aux, args.output), indent=2))


if __name__ == "__main__":
    main()
