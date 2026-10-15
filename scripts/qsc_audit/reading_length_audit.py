"""Measure the literal active TeX tree and check editorial preservation.

Page counts come from a settled pdfLaTeX AUX file, not source line counts.
The environment hashes are a regression guard, not a mathematical verifier.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
SOURCES = ROOT / "sources"
INPUT = re.compile(r"(?m)^[ \t]*\\input\{([^{}\n]+)\}")
ENVIRONMENT = re.compile(r"\\(begin|end)\{([^{}]+)\}")
PROTECTED = {
    "theorem", "lemma", "proposition", "corollary", "definition",
    "hypothesis", "conjecture", "remark", "proof", "example",
    "equation", "equation*", "align", "align*", "gather", "gather*",
    "multline", "multline*", "displaymath", "table", "table*",
}


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def uncomment(text):
    return re.sub(r"(?m)(?<!\\)%[^\n]*", "", text)


def expanded(path, files, ancestors=()):
    if path in ancestors:
        raise ValueError(f"Cyclic input: {path}")
    source = path.read_text(encoding="utf-8")
    files.append({"path": path.relative_to(ROOT).as_posix(), "sha256": digest(source)})

    def include(match):
        child = SOURCES / match[1]
        if not child.suffix:
            child = child.with_suffix(".tex")
        return expanded(child, files, (*ancestors, path))

    return INPUT.sub(include, source)


def environment_hashes(text):
    stack = []
    hashes = Counter()
    for match in ENVIRONMENT.finditer(text):
        kind, name = match.groups()
        if kind == "begin":
            stack.append((name, match.start()))
        else:
            if not stack or stack[-1][0] != name:
                raise ValueError(f"Mismatched environment at {match.start()}: {name}")
            _, start = stack.pop()
            if name in PROTECTED:
                body = re.sub(r"\s+", " ", text[start:match.end()]).strip()
                hashes[f"{name}:{digest(body)}"] += 1
    if stack:
        raise ValueError(f"Unclosed environments: {stack}")
    # Also protect standalone display formulas outside named environments.
    for body in re.findall(r"\\\[(.*?)\\\]", text, re.S):
        hashes[f"display:{digest(re.sub(r'\s+', ' ', body).strip())}"] += 1
    return hashes


def snapshot(aux_path):
    files = []
    text = uncomment(expanded(SOURCES / "active-core.tex", files))
    if any((ROOT / item["path"]).stat().st_mtime > aux_path.stat().st_mtime for item in files):
        raise ValueError("A TeX source is newer than the AUX file; compile before measuring pages.")
    aux = aux_path.read_text(encoding="utf-8")
    pages = int(re.search(r"\\gdef\s*\\@abspage@last\{(\d+)\}", aux)[1])
    first_appendix = int(re.search(r"\\newlabel\{app:mm-tools\}\{\{[^{}]*\}\{(\d+)\}", aux)[1])
    return {
        "convention": "Pages before app:mm-tools vs that page through bibliography; includes frontmatter/TOC.",
        "pages": {"total": pages, "main_and_frontmatter": first_appendix - 1,
                  "appendices_and_bibliography": pages - first_appendix + 1},
        "source": {"expanded_lines": len(text.splitlines()), "expanded_characters": len(text)},
        "files": files,
        "labels": dict(sorted(Counter(re.findall(r"\\label\{([^{}]+)\}", text)).items())),
        "protected_environments_and_displays": dict(sorted(environment_hashes(text).items())),
        "expanded_sha256": digest(text),
    }


def compare(before, after):
    missing_labels = Counter(before["labels"]) - Counter(after["labels"])
    added_labels = Counter(after["labels"]) - Counter(before["labels"])
    missing_content = (Counter(before["protected_environments_and_displays"])
                       - Counter(after["protected_environments_and_displays"]))
    changed_duplicates = {
        key: count for key, count in after["labels"].items()
        if count > max(1, before["labels"].get(key, 0))
    }
    return {"pages_before": before["pages"], "pages_after": after["pages"],
            "missing_labels": dict(missing_labels), "added_labels": dict(added_labels),
            "missing_protected_content": dict(missing_content),
            "new_duplicate_labels": changed_duplicates}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--aux", type=Path, default=ROOT / "build/math-contract-check/active-core.aux")
    parser.add_argument("--before", type=Path)
    args = parser.parse_args()
    result = snapshot(args.aux)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if args.before:
        comparison = compare(json.loads(args.before.read_text(encoding="utf-8")), result)
        print(json.dumps(comparison, indent=2))
        if any(comparison[key] for key in ("missing_labels", "missing_protected_content", "new_duplicate_labels")):
            raise SystemExit(1)
    else:
        print(json.dumps({"pages": result["pages"], "files": len(result["files"]),
                          "labels": sum(result["labels"].values()),
                          "protected_blocks": sum(result["protected_environments_and_displays"].values())}, indent=2))


if __name__ == "__main__":
    main()
