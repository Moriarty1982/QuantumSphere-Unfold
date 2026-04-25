#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_source_folder.py <source_dir>", file=sys.stderr)
        return 1

    source_dir = Path(sys.argv[1])

    if not source_dir.exists() or not source_dir.is_dir():
        print(f"ERROR: Source folder does not exist: {source_dir}", file=sys.stderr)
        return 1

    instruction_file = source_dir / "build_instruction.json"

    if not instruction_file.exists():
        print(f"ERROR: Missing instruction file: {instruction_file}", file=sys.stderr)
        return 1

    try:
        instruction = json.loads(instruction_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"ERROR: Invalid JSON in {instruction_file}: {exc}", file=sys.stderr)
        return 1

    zip_files = sorted(source_dir.glob("*.zip"))

    if not zip_files:
        print(f"ERROR: No ZIP files found in {source_dir}", file=sys.stderr)
        return 1

    logs_dir = Path("work/logs")
    logs_dir.mkdir(parents=True, exist_ok=True)

    normalized_instruction = logs_dir / "build_instruction.normalized.json"
    normalized_instruction.write_text(
        json.dumps(instruction, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"Instruction file OK: {instruction_file}")
    print(f"ZIP count: {len(zip_files)}")
    for zip_file in zip_files:
        print(f"- {zip_file.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
