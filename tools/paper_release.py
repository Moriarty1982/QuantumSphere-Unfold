"""Release pipeline for the standalone papers (QAM paper, physics paper "One Object, Three Frames").

Each paper has a configuration file release/papers/<id>.json (source folder, build command, payload names,
Zenodo metadata, deposition id and version DOI once reserved). The Zenodo steps reuse tools/zenodo_publish.py
and tools/zenodo_fix_preview.py; this script only derives their arguments from the configuration, so a release
cannot be started with the stale defaults of the generic workflow.

Subcommands (run from anywhere; paths are resolved relative to the repository):

  build   --paper ID [--final] [--out DIR]   typeset, audit the log, assemble payload + SHA256SUMS.txt
  check   --paper ID [--final]               metadata/config consistency, scope wording, payload hashes, DOI on PDF
  stamp   --paper ID --deposition-id N [--doi D]   record the reserved draft: config, release-info.tex, metadata notes
  zenodo  --paper ID --stage reserve|upload|publish [--execute] [--confirm-publish] [--environment E]
  preview --paper ID [--apply] [--record N]  report (or fix) files.default_preview of the published record
  notes   --paper ID                         write the GitHub release notes into the payload folder

Without --execute the zenodo subcommand is a dry run (no API mutation). Every mutating Zenodo step needs the
author's explicit approval (AGENTS.md).
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))
from zenodo_publish import (  # noqa: E402
    ZENODO_API, SANDBOX_API, ZenodoError, load_json, normalize_metadata, read_default_preview, validate_metadata,
)

COMPANION_CONCEPT_DOI = "10.5281/zenodo.19210728"
REPOSITORY_URL = "https://github.com/Moriarty1982/QuantumSphere-Unfold"

# Hard log failures (same zero values as the Companion audit: undefined refs/cites, duplicate labels, rerun).
LOG_FAILURES = [
    (re.compile(r"LaTeX Warning: Reference `[^']*' on page \d+ undefined"), "undefined reference"),
    (re.compile(r"LaTeX Warning: Citation `[^']*' on page \d+ undefined"), "undefined citation"),
    (re.compile(r"There were undefined references"), "undefined references"),
    (re.compile(r"LaTeX Warning: Label `[^']*' multiply defined"), "multiply defined label"),
    (re.compile(r"Rerun to get|Label\(s\) may have changed"), "rerun needed"),
]

# Wording that must not appear in the Zenodo description (honest status, AGENTS.md "Ehrlicher Status").
FORBIDDEN = [
    (re.compile(r"\b(solv(e|es|ed|ing)|clos(e|es|ed|ing)|resolv(e|es|ed|ing)|settl(e|es|ed))\b[^.<]{0,60}\b(OP[1-5]|C5|C6|T2)\b", re.I),
     "describes an open problem as solved"),
    (re.compile(r"\b(OP[1-5]|C5|C6|T2)\b[^.<]{0,40}\b(is|are|was|were) (now )?(solved|closed|resolved|settled)\b", re.I),
     "describes an open problem as solved"),
    (re.compile(r"(prov(e|es|ed|ing)|establish(es|ed)?)\s+(the\s+)?Riemann", re.I), "claims the Riemann hypothesis"),
    (re.compile(r"Riemann[- ]Hypothese[^.<]{0,30}\bbewiesen", re.I), "claims the Riemann hypothesis"),
    (re.compile(r"VERIFIED_EXACT"), "invented receipt label"),
]
SCOPE_MARKERS = ("Scope", "Geltungsbereich")


NEGATION = re.compile(r"\b(no|none|not|never|neither|nor|kein\w*|nicht)\b", re.I)


def forbidden_wording(text: str) -> List[tuple]:
    """Hits of FORBIDDEN, ignoring negated statements such as 'none of OP1-OP5 is settled'."""
    hits = []
    for pattern, label in FORBIDDEN:
        for m in pattern.finditer(text):
            if NEGATION.search(text[max(0, m.start() - 40):m.end()]):
                continue
            hits.append((label, m.group(0)))
    return hits


class ReleaseError(RuntimeError):
    pass


# ---------------------------------------------------------------- helpers

def rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def config_path(paper: str) -> Path:
    return ROOT / "release" / "papers" / f"{paper}.json"


def load_config(paper: str) -> Dict[str, Any]:
    path = config_path(paper)
    if not path.is_file():
        known = sorted(p.stem for p in (ROOT / "release" / "papers").glob("*.json"))
        raise ReleaseError(f"unknown paper {paper!r}; known: {', '.join(known)}")
    cfg = json.loads(path.read_text(encoding="utf-8"))
    if cfg.get("id") != paper:
        raise ReleaseError(f"{rel(path)}: id is {cfg.get('id')!r}, expected {paper!r}")
    return cfg


def save_config(cfg: Dict[str, Any]) -> None:
    config_path(cfg["id"]).write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def run(cmd: List[str], cwd: Path, env: Optional[Dict[str, str]] = None, check: bool = True) -> subprocess.CompletedProcess:
    proc = subprocess.run(cmd, cwd=cwd, env=env, text=True, capture_output=True)
    if check and proc.returncode != 0:
        tail = "\n".join((proc.stdout + proc.stderr).splitlines()[-40:])
        raise ReleaseError(f"command failed ({proc.returncode}): {' '.join(cmd)}\n{tail}")
    return proc


def summary(lines: List[str]) -> None:
    """Print and, inside GitHub Actions, append to the job summary."""
    text = "\n".join(lines)
    print(text)
    target = os.environ.get("GITHUB_STEP_SUMMARY")
    if target:
        with open(target, "a", encoding="utf-8") as f:
            f.write(text + "\n\n")


def pdf_text(pdf: Path, first: int = 1, last: int = 1) -> str:
    if not shutil.which("pdftotext"):
        raise ReleaseError("pdftotext not found (poppler-utils); needed to check the title page")
    return run(["pdftotext", "-f", str(first), "-l", str(last), "-layout", str(pdf), "-"], ROOT).stdout


def pdf_pages(pdf: Path) -> Optional[int]:
    if not shutil.which("pdfinfo"):
        return None
    m = re.search(r"^Pages:\s+(\d+)", run(["pdfinfo", str(pdf)], ROOT).stdout, re.M)
    return int(m.group(1)) if m else None


def payload_dir(cfg: Dict[str, Any]) -> Path:
    return ROOT / cfg["payload_dir"]


def payload_files(cfg: Dict[str, Any]) -> List[Path]:
    """Files listed in SHA256SUMS.txt plus SHA256SUMS.txt itself: exactly what goes to Zenodo."""
    out = payload_dir(cfg)
    sums = out / "SHA256SUMS.txt"
    if not sums.is_file():
        raise ReleaseError(f"{rel(sums)} missing; run `build --final` and commit the payload first")
    names = [line.split(None, 1)[1].strip().lstrip("*") for line in sums.read_text(encoding="utf-8").splitlines() if line.strip()]
    return [out / n for n in names] + [sums]


def release_info_tex(cfg: Dict[str, Any]) -> str:
    doi = cfg.get("version_doi") or ""
    return (
        "% Written by tools/paper_release.py stamp; do not edit by hand.\n"
        "% The title page shows \\releaseline (version and Version DOI); without this file it shows the draft line.\n"
        f"\\def\\paperversion{{{cfg['version']}}}\n"
        f"\\def\\versiondoi{{{doi}}}\n"
        f"\\def\\releasedate{{{cfg.get('release_date', '')}}}\n"
        "\\def\\releaseline{Version \\paperversion\\ifx\\versiondoi\\empty\\else\\enspace$\\cdot$\\enspace"
        "\\href{https://doi.org/\\versiondoi}{doi:\\versiondoi}\\fi"
        "\\ifx\\releasedate\\empty\\else\\enspace$\\cdot$\\enspace\\releasedate\\fi}\n"
    )


# ---------------------------------------------------------------- build

def audit_log(log: Path) -> Dict[str, Any]:
    text = log.read_text(encoding="latin-1")
    failures: List[str] = []
    for pattern, label in LOG_FAILURES:
        hits = pattern.findall(text)
        if hits:
            failures.append(f"{label}: {len(hits)}")
    return {
        "failures": failures,
        "overfull": len(re.findall(r"^Overfull \\hbox", text, re.M)),
        "underfull": len(re.findall(r"^Underfull \\hbox", text, re.M)),
    }


def git_clean(paths: List[str]) -> bool:
    out = run(["git", "status", "--porcelain", "--", *paths], ROOT).stdout
    # build products are ignored by the paper's .gitignore; anything else listed is uncommitted source
    return not out.strip()


def cmd_build(args: argparse.Namespace) -> int:
    cfg = load_config(args.paper)
    src = ROOT / cfg["source_dir"]
    main_tex = src / cfg["main"]
    if not main_tex.is_file():
        raise ReleaseError(f"{rel(main_tex)} not found (is the paper's branch merged or checked out?)")
    stem = main_tex.stem

    if args.final:
        if not cfg.get("version_doi"):
            raise ReleaseError("--final needs the reserved Version DOI; run the reserve stage and `stamp` first")
        if not (src / "release-info.tex").is_file():
            raise ReleaseError(f"{rel(src / 'release-info.tex')} missing; run `stamp`")
        if not git_clean([cfg["source_dir"], *cfg.get("source_extra", [])]):
            raise ReleaseError("uncommitted changes in the paper sources; the payload must come from a commit")

    env = dict(os.environ)
    # Package source state = last commit that touched the paper's sources. Archive and PDF dates come from it, so a
    # rebuild after committing the payload gives the same bytes.
    paths = [cfg["source_dir"], *cfg.get("source_extra", []), *cfg.get("texinputs", []), *cfg.get("build_needs", [])]
    commit, epoch = run(["git", "log", "-1", "--format=%H %ct", "--", *paths], ROOT).stdout.split()
    env.update(SOURCE_DATE_EPOCH=epoch, FORCE_SOURCE_DATE="1")

    # Build in a copy that keeps the relative layout (build.sh uses ../../qam/tex), so the repository stays untouched.
    tree = ROOT / "build" / "paper-release" / cfg["id"] / "tree"
    if tree.exists():
        shutil.rmtree(tree)
    for part in [cfg["source_dir"], *cfg.get("texinputs", []), *cfg.get("source_extra", []), *cfg.get("build_needs", [])]:
        source = ROOT / part
        if source.is_dir():
            shutil.copytree(source, tree / part)
        else:
            (tree / part).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, tree / part)
    texinputs = [str(tree / p) for p in cfg.get("texinputs", [])]
    if texinputs:
        env["TEXINPUTS"] = os.pathsep.join(texinputs) + os.pathsep + os.environ.get("TEXINPUTS", "")
    src = tree / cfg["source_dir"]
    build = cfg["build"]
    if build[0] == "sh":
        run(build, src, env)
    else:
        for engine in build:
            run([engine, "-interaction=nonstopmode", "-halt-on-error", cfg["main"]], src, env)

    pdf = src / f"{stem}.pdf"
    audit = audit_log(src / f"{stem}.log")
    pages = pdf_pages(pdf)
    first = pdf_text(pdf)
    lines = [f"## Build `{cfg['id']}` ({'final' if args.final else 'check'})",
             f"- PDF: {pages} pages, overfull hbox {audit['overfull']}, underfull hbox {audit['underfull']}",
             f"- Log failures: {', '.join(audit['failures']) or 'none'}"]
    problems = list(audit["failures"])
    title_head = cfg["title"].split(":")[0]
    if re.sub(r"\s+", "", title_head).lower() not in re.sub(r"\s+", "", first).lower():
        problems.append(f"title page does not show the configured title start {title_head!r}")
    if args.final:
        flat = re.sub(r"\s+", "", first)
        if cfg["version_doi"] not in flat:
            problems.append(f"title page does not show the Version DOI {cfg['version_doi']} (does it use \\releaseline?)")
        if re.search(r"\bdraft\b", first, re.I):
            problems.append("title page still says 'Draft'")
    else:
        lines.append(f"- Title page DOI: {'present' if cfg.get('version_doi') and cfg['version_doi'] in first else 'not yet (draft build)'}")

    out = Path(args.out) if args.out else (payload_dir(cfg) if args.final else ROOT / "build" / "paper-release" / cfg["id"] / "payload")
    out.mkdir(parents=True, exist_ok=True)
    for old in out.iterdir():
        if old.is_file() and old.name not in ("README.md", "RELEASE_NOTES.md", "BUILD_INFO.json"):
            old.unlink()
    shutil.copy2(pdf, out / cfg["pdf_name"])
    archive = out / cfg["source_archive"]
    prefix = f"{cfg['id']}-v{cfg['version']}/"
    run(["git", "archive", "--format=tar.gz", f"--prefix={prefix}", "-o", str(archive), commit, "--",
         cfg["source_dir"], *cfg.get("source_extra", [])], ROOT)
    for extra in cfg.get("extra_files", []):
        shutil.copy2(tree / extra["from"], out / extra["name"])
    names = [cfg["pdf_name"], cfg["source_archive"], *[e["name"] for e in cfg.get("extra_files", [])]]
    (out / "SHA256SUMS.txt").write_text("".join(f"{sha256(out / n)}  {n}\n" for n in names), encoding="utf-8")

    texver = run(["pdflatex", "--version"], ROOT).stdout.splitlines()[0]
    info = {"paper": cfg["id"], "version": cfg["version"], "source_commit": commit, "pages": pages,
            "overfull_hbox": audit["overfull"], "underfull_hbox": audit["underfull"], "tex": texver,
            "version_doi": cfg.get("version_doi") or None, "final": bool(args.final),
            "files": {n: sha256(out / n) for n in names}}
    (out / "BUILD_INFO.json").write_text(json.dumps(info, indent=2) + "\n", encoding="utf-8")
    lines.append(f"- Package source state (last commit touching the sources): `{commit}`")
    lines.append(f"- Payload in `{rel(out)}`: " + ", ".join(f"`{n}`" for n in names) + ", `SHA256SUMS.txt`")
    if problems:
        lines.append("- **Problems:** " + "; ".join(problems))
        summary(lines)
        return 1
    lines.append("- Result: ok")
    summary(lines)
    return 0


# ---------------------------------------------------------------- check

def check_metadata(cfg: Dict[str, Any]) -> List[str]:
    problems: List[str] = []
    raw = load_json(ROOT / cfg["metadata"])
    payload = normalize_metadata(raw)
    try:
        validate_metadata(payload)
    except ZenodoError as exc:
        problems.append(str(exc))
    md = payload["metadata"]
    if md.get("title") != cfg["title"]:
        problems.append(f"metadata title {md.get('title')!r} differs from config title {cfg['title']!r}")
    if md.get("version") != cfg["version"]:
        problems.append(f"metadata version {md.get('version')!r} differs from config version {cfg['version']!r}")
    desc = md.get("description", "")
    if not any(marker in desc for marker in SCOPE_MARKERS):
        problems.append("description has no scope paragraph ('Scope' / 'Geltungsbereich')")
    problems += [f"description {label}: {hit!r}" for label, hit in forbidden_wording(re.sub(r"<[^>]+>", " ", desc))]
    ids = {(r.get("identifier", "").rstrip("/"), r.get("relation")) for r in md.get("related_identifiers", [])}
    if not any(i == COMPANION_CONCEPT_DOI for i, _ in ids):
        problems.append(f"related_identifiers lack the Companion concept DOI {COMPANION_CONCEPT_DOI}")
    if not any(i == REPOSITORY_URL for i, _ in ids):
        problems.append("related_identifiers lack the repository URL")
    prev = cfg.get("new_version_of")
    if prev and not any(rel_ == "isNewVersionOf" for _, rel_ in ids):
        problems.append("new_version_of is set, but metadata has no isNewVersionOf relation")
    if not prev and any(rel_ in ("isNewVersionOf", "isVersionOf") for _, rel_ in ids):
        problems.append("first version of a new record, but metadata has isVersionOf/isNewVersionOf")
    notes = md.get("notes", "")
    if cfg.get("version_doi") and cfg["version_doi"] not in notes + desc:
        problems.append(f"metadata notes/description do not mention the Version DOI {cfg['version_doi']}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", md.get("publication_date", "")):
        problems.append("publication_date missing or not YYYY-MM-DD")
    return problems


def check_payload(cfg: Dict[str, Any]) -> List[str]:
    problems: List[str] = []
    files = payload_files(cfg)
    out = payload_dir(cfg)
    for line in (out / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, name = line.split(None, 1)
        path = out / name.strip().lstrip("*")
        if not path.is_file():
            problems.append(f"payload file missing: {rel(path)}")
        elif sha256(path) != digest:
            problems.append(f"SHA256 mismatch: {rel(path)}")
    if cfg["pdf_name"] not in [p.name for p in files]:
        problems.append(f"main PDF {cfg['pdf_name']} not listed in SHA256SUMS.txt")
    pdf = out / cfg["pdf_name"]
    if pdf.is_file() and cfg.get("version_doi"):
        first = pdf_text(pdf)
        if cfg["version_doi"] not in re.sub(r"\s+", "", first):
            problems.append(f"payload PDF title page lacks the Version DOI {cfg['version_doi']}")
        if re.search(r"\bdraft\b", first, re.I):
            problems.append("payload PDF title page still says 'Draft'")
    return problems


def cmd_check(args: argparse.Namespace) -> int:
    cfg = load_config(args.paper)
    problems = check_metadata(cfg)
    has_payload = (payload_dir(cfg) / "SHA256SUMS.txt").is_file()
    if args.final or has_payload:
        try:
            problems += check_payload(cfg)
        except ReleaseError as exc:
            problems.append(str(exc))
    if args.final and not cfg.get("deposition_id"):
        problems.append("no deposition_id in the config; reserve and `stamp` first")
    lines = [f"## Check `{cfg['id']}` v{cfg['version']}",
             f"- Metadata: `{cfg['metadata']}`; payload: `{cfg['payload_dir']}` ({'present' if has_payload else 'not built yet'})",
             f"- Deposition: {cfg.get('deposition_id') or 'not reserved'}; Version DOI: {cfg.get('version_doi') or '-'}"]
    lines += [f"- **Problem:** {p}" for p in problems] or ["- Result: ok"]
    summary(lines)
    return 1 if problems else 0


# ---------------------------------------------------------------- stamp

def cmd_stamp(args: argparse.Namespace) -> int:
    cfg = load_config(args.paper)
    if cfg.get("deposition_id") and cfg["deposition_id"] != args.deposition_id and not args.force:
        raise ReleaseError(f"config already has deposition {cfg['deposition_id']}; use --force to replace it")
    doi = args.doi or f"10.5281/zenodo.{args.deposition_id}"
    cfg["deposition_id"] = args.deposition_id
    cfg["version_doi"] = doi
    cfg["release_date"] = args.date or dt.date.today().isoformat()
    save_config(cfg)

    meta_path = ROOT / cfg["metadata"]
    raw = load_json(meta_path)
    md = raw["metadata"] if isinstance(raw.get("metadata"), dict) else raw
    note = f"Version DOI {doi} (reserved on Zenodo, deposition {args.deposition_id}; shown on the title page)."
    old = re.sub(r"\s*Version DOI 10\.5281/zenodo\.\d+ \([^)]*\)\.", "", md.get("notes", "")).strip()
    md["notes"] = (note + (" " + old if old else "")).strip()
    md["publication_date"] = cfg["release_date"]
    meta_path.write_text(json.dumps(raw, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    info = ROOT / cfg["source_dir"] / "release-info.tex"
    if not info.parent.is_dir():
        raise ReleaseError(f"{rel(info.parent)} does not exist")
    info.write_text(release_info_tex(cfg), encoding="utf-8")
    summary([f"## Stamp `{cfg['id']}`",
             f"- deposition_id {args.deposition_id}, Version DOI {doi}, release date {cfg['release_date']}",
             f"- written: `{rel(config_path(cfg['id']))}`, `{rel(meta_path)}`, `{rel(info)}`",
             "- next: commit these three files, then `build --final`, commit the payload, push"])
    return 0


# ---------------------------------------------------------------- zenodo

def zenodo_argv(cfg: Dict[str, Any], stage: str, environment: str, execute: bool) -> List[str]:
    argv = [sys.executable, str(TOOLS / "zenodo_publish.py"), "--metadata", cfg["metadata"], "--environment", environment]
    if stage == "reserve":
        if cfg.get("deposition_id"):
            raise ReleaseError(f"already reserved (deposition {cfg['deposition_id']}); use stage upload")
        argv += ["--reserve-only", "--files", f"{cfg['payload_dir']}/*.pdf"]
        if cfg.get("new_version_of"):
            argv += ["--new-version-of", cfg["new_version_of"]]
    else:
        if not cfg.get("deposition_id"):
            raise ReleaseError("no deposition_id in the config; reserve and `stamp` first")
        files = [rel(p) for p in payload_files(cfg)]
        # replace-files: the draft keeps exactly the payload, also when a new-version draft inherited old files
        argv += ["--deposition-id", cfg["deposition_id"], "--replace-files", "--default-preview", cfg["pdf_name"],
                 "--files", *files]
        if stage == "publish":
            argv += ["--publish", "--confirm-publish"]
    if not execute:
        argv.append("--dry-run")
    return argv


def cmd_zenodo(args: argparse.Namespace) -> int:
    cfg = load_config(args.paper)
    if args.stage == "publish" and args.execute and not args.confirm_publish:
        raise ReleaseError("publishing needs --confirm-publish (and the author's explicit approval)")
    if args.stage in ("upload", "publish"):
        problems = check_metadata(cfg) + check_payload(cfg)
        if problems:
            summary([f"## Zenodo `{cfg['id']}` {args.stage}: stopped before any API call"] + [f"- **Problem:** {p}" for p in problems])
            return 1
    else:
        problems = check_metadata(cfg)
        if problems:
            summary([f"## Zenodo `{cfg['id']}` reserve: stopped before any API call"] + [f"- **Problem:** {p}" for p in problems])
            return 1
    argv = zenodo_argv(cfg, args.stage, args.environment, args.execute)
    print("$ " + " ".join(argv[1:]))
    proc = subprocess.run(argv, cwd=ROOT, text=True, capture_output=True)
    print(proc.stdout)
    print(proc.stderr, file=sys.stderr)
    lines = [f"## Zenodo `{cfg['id']}` {args.stage} ({args.environment}, {'executed' if args.execute else 'dry run'})",
             f"- exit code {proc.returncode}"]
    m = re.search(r'"reserved_doi":\s*"([^"]+)"', proc.stdout)
    d = re.search(r'"deposition_id":\s*"([^"]+)"', proc.stdout)
    if d:
        lines.append(f"- deposition_id: {d.group(1)}")
    if m:
        lines.append(f"- reserved Version DOI: {m.group(1)}")
    if proc.returncode != 0:
        summary(lines)
        return proc.returncode
    if args.stage == "reserve" and args.execute and d:
        lines.append(f"- next: `python tools/paper_release.py stamp --paper {cfg['id']} --deposition-id {d.group(1)}`")

    # Author's standing order (24.11.2026): check the preview after every upload, also after publishing.
    if args.execute and args.stage in ("upload", "publish"):
        api = ZENODO_API if args.environment == "production" else SANDBOX_API
        token = os.environ.get("ZENODO_TOKEN" if args.environment == "production" else "ZENODO_SANDBOX_TOKEN", "")
        if args.stage == "upload":
            current = read_default_preview(api, token, cfg["deposition_id"])
            ok = current == cfg["pdf_name"]
            lines.append(f"- draft preview: {current} ({'ok' if ok else 'WRONG'})")
            if not ok:
                summary(lines)
                return 1
        elif args.environment == "production":
            fix = subprocess.run([sys.executable, str(TOOLS / "zenodo_fix_preview.py"), "--record", cfg["deposition_id"],
                                  "--file", cfg["pdf_name"], "--apply"], cwd=ROOT, text=True, capture_output=True)
            print(fix.stdout, fix.stderr)
            lines.append("- preview of the published record (checked, corrected if needed):")
            lines += [f"  - {line}" for line in fix.stdout.splitlines() if "preview" in line.lower() or line.startswith("Record")]
            lines.append(f"- record: https://zenodo.org/records/{cfg['deposition_id']}")
            if fix.returncode != 0:
                lines.append("- **preview check failed**; run the preview stage again or set it on the record page")
                summary(lines)
                return 1
    summary(lines)
    return 0


def cmd_preview(args: argparse.Namespace) -> int:
    cfg = load_config(args.paper)
    record = args.record or cfg.get("deposition_id")
    if not record:
        raise ReleaseError("no record id: pass --record or stamp the config")
    argv = [sys.executable, str(TOOLS / "zenodo_fix_preview.py"), "--record", record, "--file", cfg["pdf_name"]]
    if args.apply:
        argv.append("--apply")
    proc = subprocess.run(argv, cwd=ROOT, text=True, capture_output=True)
    summary([f"## Preview `{cfg['id']}` record {record} ({'apply' if args.apply else 'report'})", "```",
             (proc.stdout + proc.stderr).strip(), "```"])
    return proc.returncode


# ---------------------------------------------------------------- notes

def cmd_notes(args: argparse.Namespace) -> int:
    cfg = load_config(args.paper)
    if not cfg.get("version_doi"):
        raise ReleaseError("no Version DOI in the config yet")
    md = normalize_metadata(load_json(ROOT / cfg["metadata"]))["metadata"]
    info_path = payload_dir(cfg) / "BUILD_INFO.json"
    info = json.loads(info_path.read_text(encoding="utf-8")) if info_path.is_file() else {}
    record = f"https://zenodo.org/records/{cfg['deposition_id']}"
    text = (f"# {cfg['title']}\n\n"
            f"Version {cfg['version']} ({cfg.get('release_date', '')}).\n\n"
            f"- Version DOI: [{cfg['version_doi']}](https://doi.org/{cfg['version_doi']})\n"
            f"- Zenodo record: {record}\n"
            f"- Source commit of the payload: `{info.get('source_commit', '?')}` (`{cfg['source_dir']}`)\n"
            f"- {info.get('pages', '?')} pages; SHA256 of the files in `{cfg['payload_dir']}/SHA256SUMS.txt`\n\n"
            "## Scope\n\n"
            + re.sub(r"^\s*(Scope|Geltungsbereich)\.\s*", "", re.sub(r"<[^>]+>", "", next((p for p in re.split(r"</p>", md.get("description", "")) if any(s in p for s in SCOPE_MARKERS)), ""))).strip()
            + "\n")
    out = payload_dir(cfg) / "RELEASE_NOTES.md"
    out.write_text(text, encoding="utf-8")
    target = info.get("source_commit", "<SHA>")
    summary([f"## Release notes `{cfg['id']}`", f"- written `{rel(out)}`", "- GitHub release (after the release PR is merged):",
             "```", f"gh workflow run \"GitHub Release anlegen\" --repo Moriarty1982/QuantumSphere-Unfold --ref main \\",
             f"  -f tag={cfg['tag']} -f target={target} \\",
             f"  -f title=\"{cfg['title']} v{cfg['version']}\" -f notes_file={cfg['payload_dir']}/RELEASE_NOTES.md",
             "```", "- or locally:", "```", f"git tag -a {cfg['tag']} {target} -m \"{cfg['id']} v{cfg['version']}, doi:{cfg['version_doi']}\"",
             f"git push origin {cfg['tag']}", "```"])
    return 0


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("build"); p.add_argument("--paper", required=True)
    p.add_argument("--final", action="store_true", help="release build: DOI on the title page, clean sources, payload into payload_dir")
    p.add_argument("--out", help="payload folder (default: payload_dir for --final, build/paper-release/<id> otherwise)")
    p.set_defaults(func=cmd_build)

    p = sub.add_parser("check"); p.add_argument("--paper", required=True); p.add_argument("--final", action="store_true")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("stamp"); p.add_argument("--paper", required=True); p.add_argument("--deposition-id", required=True)
    p.add_argument("--doi"); p.add_argument("--date", help="release date YYYY-MM-DD (default today)")
    p.add_argument("--force", action="store_true"); p.set_defaults(func=cmd_stamp)

    p = sub.add_parser("zenodo"); p.add_argument("--paper", required=True)
    p.add_argument("--stage", required=True, choices=["reserve", "upload", "publish"])
    p.add_argument("--environment", default="production", choices=["production", "sandbox"])
    p.add_argument("--execute", action="store_true", help="really call the API (default: dry run)")
    p.add_argument("--confirm-publish", action="store_true")
    p.set_defaults(func=cmd_zenodo)

    p = sub.add_parser("preview"); p.add_argument("--paper", required=True); p.add_argument("--record")
    p.add_argument("--apply", action="store_true"); p.set_defaults(func=cmd_preview)

    p = sub.add_parser("notes"); p.add_argument("--paper", required=True); p.set_defaults(func=cmd_notes)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ReleaseError, ZenodoError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        if os.environ.get("GITHUB_ACTIONS") == "true":
            print("::error::" + str(exc).replace("\n", " ")[:900])
        raise SystemExit(2)
