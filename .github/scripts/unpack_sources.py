#!/usr/bin/env python3

from __future__ import annotations

import shutil
import sys
import zipfile
from pathlib import Path


def is_pdf(path_name: str) -> bool:
    return path_name.lower().endswith(".pdf")


def safe_target_path(root: Path, member_name: str) -> Path | None:
    """
    Prevents zip-slip paths like ../../something.
    """
    target = root / member_name
    try:
        target_resolved = target.resolve()
        root_resolved = root.resolve()
    except OSError:
        return None

    if not str(target_resolved).startswith(str(root_resolved)):
        return None

    return target


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: unpack_sources.py <source_dir> <target_dir>", file=sys.stderr)
        return 1

    source_dir = Path(sys.argv[1])
    target_dir = Path(sys.argv[2])

    zip_files = sorted(source_dir.glob("*.zip"))

    if not zip_files:
        print(f"ERROR: No ZIP files found in {source_dir}", file=sys.stderr)
        return 1

    target_dir.mkdir(parents=True, exist_ok=True)

    logs_dir = Path("work/logs")
    logs_dir.mkdir(parents=True, exist_ok=True)

    ignored_pdfs_log = logs_dir / "ignored_pdfs.txt"
    unpack_log = logs_dir / "unpack_log.txt"

    ignored_pdfs: list[str] = []
    unpacked_files: list[str] = []
    skipped_unsafe: list[str] = []

    with unpack_log.open("w", encoding="utf-8") as log:
        for zip_path in zip_files:
            print(f"Unpacking {zip_path}")
            log.write(f"ZIP: {zip_path}\n")

            with zipfile.ZipFile(zip_path, "r") as archive:
                for member in archive.infolist():
                    name = member.filename

                    if name.endswith("/"):
                        continue

                    if is_pdf(name):
                        ignored = f"{zip_path.name}::{name}"
                        ignored_pdfs.append(ignored)
                        log.write(f"  ignored pdf: {name}\n")
                        continue

                    target = safe_target_path(target_dir, name)

                    if target is None:
                        skipped = f"{zip_path.name}::{name}"
                        skipped_unsafe.append(skipped)
                        log.write(f"  skipped unsafe path: {name}\n")
                        continue

                    target.parent.mkdir(parents=True, exist_ok=True)

                    with archive.open(member, "r") as src, target.open("wb") as dst:
                        shutil.copyfileobj(src, dst)

                    unpacked_files.append(str(target))
                    log.write(f"  extracted: {name}\n")

            log.write("\n")

    ignored_pdfs_log.write_text(
        "\n".join(ignored_pdfs) + ("\n" if ignored_pdfs else ""),
        encoding="utf-8",
    )

    if ignored_pdfs:
        print("PDFs were found and ignored:")
        for item in ignored_pdfs:
            print(f"- {item}")
    else:
        print("No PDFs found inside ZIPs.")

    if skipped_unsafe:
        print("WARNING: Some unsafe ZIP paths were skipped:")
        for item in skipped_unsafe:
            print(f"- {item}")

    print(f"Unpacked files: {len(unpacked_files)}")
    print(f"Target folder: {target_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
