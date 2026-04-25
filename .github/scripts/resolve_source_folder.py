#!/usr/bin/env python3

from __future__ import annotations

import os
import re
import sys
from pathlib import Path


def version_key(name: str) -> tuple:
    """
    Sorts folders like v3.35.0 naturally.
    Unknown names are sorted after normal version names.
    """
    match = re.fullmatch(r"v(\d+)\.(\d+)\.(\d+)", name)
    if not match:
        return (999999, name)
    return tuple(int(part) for part in match.groups())


def write_github_output(key: str, value: str) -> None:
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a", encoding="utf-8") as handle:
            handle.write(f"{key}={value}\n")
    else:
        print(f"{key}={value}")


def main() -> int:
    requested_version = sys.argv[1].strip() if len(sys.argv) > 1 and sys.argv[1].strip() else ""

    sources_root = Path("sources")

    if not sources_root.exists():
        print("ERROR: sources/ folder does not exist.", file=sys.stderr)
        return 1

    if requested_version:
        version = requested_version
    else:
        candidates = [p.name for p in sources_root.iterdir() if p.is_dir()]
        if not candidates:
            print("ERROR: No version folders found below sources/.", file=sys.stderr)
            return 1

        version = sorted(candidates, key=version_key)[-1]

    source_dir = sources_root / version

    if not source_dir.exists() or not source_dir.is_dir():
        print(f"ERROR: Source folder does not exist: {source_dir}", file=sys.stderr)
        return 1

    write_github_output("version", version)
    write_github_output("source_dir", str(source_dir))

    print(f"Resolved version: {version}")
    print(f"Resolved source folder: {source_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
