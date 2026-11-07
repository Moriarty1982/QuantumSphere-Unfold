#!/usr/bin/env python3
"""Compile QAM fixtures, check rejection/export behavior and physics provenance.

Uses only the standard library and the installed pdflatex. It does not assert
that formula payloads are mathematically or physically true.
"""
from __future__ import annotations

import argparse
import importlib.util
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

TESTS = Path(__file__).resolve().parent
QAM = TESTS.parents[1]
spec = importlib.util.spec_from_file_location("qamhash", QAM / "tools" / "qamhash.py")
qamhash = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qamhash)

EXPECTED = {
    "fail_physics_no_context": "No valid physics context",
    "fail_physics_profile_mix": "Physics profile mismatch",
    "fail_physics_promotion": "Promotion:",
    "fail_physics_map_target": "does not connect",
    "fail_physics_duplicate": "Physics profile",
    "fail_physics_unknown_profile": "Physics profile",
    "fail_physics_unknown_frame": "not declared",
    "fail_physics_any_frame": "specific declared frame",
    "fail_physics_missing_map": "not declared",
    "fail_physics_target_status": "Promotion:",
    "fail_physics_duplicate_formula": "declared twice",
    "fail_physics_semicolon": "literal semicolon",
}


def run(output: Path) -> int:
    output.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env["TEXINPUTS"] = str(QAM / "tex") + os.pathsep + env.get("TEXINPUTS", "")
    good, errors, exports = 0, [], {}
    for source in sorted(TESTS.glob("pass*.tex")) + sorted(TESTS.glob("fail*.tex")):
        folder = output / source.stem
        folder.mkdir(exist_ok=True)
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
             "-output-directory=" + str(folder), source.name],
            cwd=TESTS, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            timeout=90, encoding="utf-8", errors="replace",
        )
        (folder / "compiler.txt").write_text(result.stdout, encoding="utf-8")
        normalized = " ".join(result.stdout.split())
        if source.stem.startswith("fail"):
            expected = EXPECTED.get(source.stem, "Package qam Error")
            accepted = result.returncode != 0 and "Package qam Error" in normalized and expected in normalized
        else:
            accepted = result.returncode == 0
        if not accepted:
            errors.append(f"{source.name}: unexpected compiler outcome (see {folder / 'compiler.txt'})")
            continue
        good += 1
        record = folder / (source.stem + ".qam")
        if source.stem.startswith("pass") and record.exists():
            # Make source identity verification real, rather than skipping an absent file.
            shutil.copyfile(source, folder / source.name)
            _, claims, _, defects = qamhash.verify(record)
            errors.extend(f"{source.name}: {d}" for d in defects)
            exports[source.stem] = {c["key"]: c for c in claims}

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    require(len(exports.get("pass_notation", {})) == 6, "existing notation export no longer contains six records")
    physics = exports.get("pass_physics", {})
    require(set(physics) == {"qphys-profile-gr", "qphys-profile-qm", "einstein", "schrodinger"},
            "ART/QM example lost records or inherited a wrong context")
    for key, frame, profile, formula in [
        ("einstein", "ART", "gr", r"G_{\mu"),
        ("schrodinger", "QM", "qm", r"\hat H"),
    ]:
        record = physics.get(key, {})
        require(record.get("frame") == frame, f"{key}: wrong exported frame")
        require(record.get("prem") == ["qphys-profile-" + profile], f"{key}: profile provenance lost")
        require(formula in record.get("statement", ""), f"{key}: ordinary formula lost from export")
        require("language L_" in record.get("statement", ""), f"{key}: language role lost")

    converted = exports.get("pass_physics_conversion", {})
    require(converted.get("target", {}).get("frame") == "K", "conversion target frame lost")
    require(converted.get("target", {}).get("prem") == ["qphys-profile-b", "qphys-transfer-target"],
            "conversion lost target interpretation or source transport")
    require("y=2" in converted.get("target", {}).get("statement", ""),
            "target mapping copied the source formula instead of the explicit target payload")
    same_frame = exports.get("pass_physics_same_frame_conversion", {})
    require(same_frame.get("y", {}).get("frame") == "F" and
            same_frame.get("y", {}).get("prem") == ["qphys-profile-b", "qphys-transfer-y"],
            "explicit same-frame profile conversion lost its target interpretation")

    warning = exports.get("pass_physics_warning", {})
    require(set(warning) == {"qphys-profile-a", "qphys-profile-b", "source", "restored"},
            "warning-mode rejection created a formula/transfer or lost the outer context")
    require(warning.get("restored", {}).get("frame") == "F", "nested context did not restore its parent")
    provenance = exports.get("pass_physics_provenance", {}).get("readout", {})
    require(provenance.get("inputs") == ["measurement"], "physics formula lost a measurement input")

    # Check the actual printed default-context behavior, not internal storage flags.
    pdf = output / "pass_physics_display" / "pass_physics_display.pdf"
    if shutil.which("pdftotext") and pdf.exists():
        result = subprocess.run(["pdftotext", "-raw", str(pdf), "-"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                encoding="utf-8", errors="replace", timeout=30)
        require(result.returncode == 0, "could not extract the physics display PDF")
        text = "".join(result.stdout.split())
        for marker, labelled in [("IMPLICIT", False), ("FULL", True),
                                  ("FOREIGN", True), ("RESTORED", False),
                                  ("STANDALONE", True)]:
            match = re.search(marker + r"BEGIN(.*?)" + marker + "END", text)
            require(match is not None, f"missing rendered {marker} formula")
            if match:
                require(("GRF" in match[1] and "LANGART" in match[1]) == labelled,
                        f"{marker}: wrong visibility of the left roles")
    else:
        print("NOTE pdftotext unavailable: rendered-role check skipped")

    # A changed ordinary formula or interpretation must invalidate its saved hash.
    sample = output / "pass_physics" / "pass_physics.qam"
    if sample.exists():
        raw = sample.read_text(encoding="utf-8")
        for name, old, new in [("formula", r"\hat H", r"\hat K"),
                               ("profile", "Classical GR", "Different GR")]:
            changed = output / f"tampered-{name}.qam"
            changed.write_text(raw.replace(old, new), encoding="utf-8")
            require(bool(qamhash.verify(changed)[3]), f"{name} tampering was not detected")
    require(len(exports) >= 10, "expected physics/legacy exports were not generated")
    for error in errors:
        print("FAIL", error)
    print(f"{good} compiler outcomes checked, {len(exports)} exported records verified, {len(errors)} failures")
    return bool(errors)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    if args.output_dir:
        return run(args.output_dir.resolve())
    with tempfile.TemporaryDirectory(prefix="qam-tests-") as folder:
        return run(Path(folder))


if __name__ == "__main__":
    raise SystemExit(main())
