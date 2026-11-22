"""Select compact MMA receipt metadata with SQLite or the HDL comparison model."""

from pathlib import Path
import os
import re
import shutil
import subprocess
from tempfile import TemporaryDirectory
from time import perf_counter


PROJECT_ROOT = Path(__file__).resolve().parents[2]
HDL = PROJECT_ROOT / "qam" / "examples" / "zuse_machine" / "hdl"
MAX_HDL_ROWS = 4096
STATUSES = ("continue", "guard", "reject")
FIELDS = ("receipt_hash", "context_hash", "frame", "status", "instruction")
FRAME_SQL = """CASE WHEN json_type(request, '$.arguments.frame') = 'text'
                    THEN json_extract(request, '$.arguments.frame') END"""
METADATA_SQL = f"SELECT receipt_hash, context_hash, {FRAME_SQL}, status, instruction FROM mma_receipts"


def add_arguments(parser):
    parser.add_argument("--context-hash")
    parser.add_argument("--frame")
    parser.add_argument("--status", choices=STATUSES)
    parser.add_argument("--backend", choices=("sqlite", "hdl"), default="sqlite")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--iverilog", default="iverilog")
    parser.add_argument("--vvp", default="vvp")


def validate(context_hash, frame, status, limit):
    if context_hash is not None and not re.fullmatch(r"[0-9a-fA-F]{128}", context_hash):
        raise ValueError("context_hash must be a 128-digit MMA context hash.")
    if frame is not None and (not frame.strip() or len(frame) > 64):
        raise ValueError("frame must be a nonempty, exact label of at most 64 characters.")
    if status is not None and status not in STATUSES:
        raise ValueError("status must be continue, guard or reject.")
    if type(limit) is not int or not 1 <= limit <= 50:
        raise ValueError("limit must be between 1 and 50.")


def run_command(command):
    try:
        result = subprocess.run(
            command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=20,
        )
    except subprocess.TimeoutExpired as error:
        raise RuntimeError("An HDL command exceeded 20 seconds.") from error
    if result.returncode:
        raise RuntimeError(f"HDL command failed: {result.stderr.strip()[-1600:] or result.stdout.strip()[-1600:]}")
    return result.stdout


def hdl_matches(rows, criteria, iverilog, vvp):
    # Intern strings for an exact, collision-free comparison; zero denotes a missing label.
    codes = {}

    def code(value):
        return 0 if value is None else codes.setdefault(value, len(codes) + 1)

    mask = sum(1 << bit for bit, value in enumerate(criteria) if value is not None)
    header = [len(rows), mask, *(code(value) for value in criteria)]
    with TemporaryDirectory(prefix="qsc-context-") as tmp:
        vectors = Path(tmp) / "rows.txt"
        executable = Path(tmp) / "filter.vvp"
        with vectors.open("w", encoding="ascii", newline="\n") as file:
            print(*header, file=file)
            for row_id, row in enumerate(rows):
                print(row_id, *(code(value) for value in row[1:4]), file=file)

        wsl = None
        if os.name == "nt" and (iverilog, vvp) == ("iverilog", "vvp"):
            if not all(shutil.which(tool) for tool in (iverilog, vvp)):
                wsl = shutil.which("wsl.exe")

        prefix = [wsl, "--exec"] if wsl else []

        def simulator_path(path):
            if wsl:
                return run_command([*prefix, "wslpath", "-a", str(path)]).strip()
            return str(path)

        if wsl:
            local_iverilog, local_vvp = (PROJECT_ROOT / "build" / "hdl-tools" / tool
                                         for tool in ("iverilog", "vvp"))
            if local_iverilog.is_file() and local_vvp.is_file():
                iverilog, vvp = simulator_path(local_iverilog), simulator_path(local_vvp)

        output_path = simulator_path(executable)
        run_command([*prefix, iverilog, "-g2012", "-s", "context_filter_tb", "-o", output_path,
                     simulator_path(HDL / "context_filter.sv"),
                     simulator_path(HDL / "context_filter_tb.sv")])
        output = run_command([*prefix, vvp, output_path, f"+cases={simulator_path(vectors)}"])

    matches = []
    for line in output.splitlines():
        match = re.fullmatch(r"MATCH (\d+)", line)
        if not match:
            raise RuntimeError(f"Unexpected HDL response: {line[:160]}")
        index = int(match[1])
        if not 0 <= index < len(rows) or (matches and index <= matches[-1]):
            raise RuntimeError("HDL returned an invalid or out-of-order row ID.")
        matches.append(index)
    return matches


def select(db, *, context_hash=None, frame=None, status=None, limit=10, backend="sqlite",
           iverilog="iverilog", vvp="vvp"):
    validate(context_hash, frame, status, limit)
    started = perf_counter()
    criteria = (context_hash.lower() if context_hash is not None else None, frame, status)
    scanned = None
    if backend == "sqlite":
        columns = ("context_hash", FRAME_SQL, "status")
        terms = [(column, value) for column, value in zip(columns, criteria) if value is not None]
        where = " WHERE " + " AND ".join(f"{column} = ?" for column, _ in terms) if terms else ""
        rows = db.execute(METADATA_SQL + where + " ORDER BY rowid DESC LIMIT ?",
                          [*(value for _, value in terms), limit]).fetchall()
    elif backend == "hdl":
        candidates = db.execute(METADATA_SQL + " ORDER BY rowid DESC LIMIT ?",
                                (MAX_HDL_ROWS + 1,)).fetchall()
        if len(candidates) > MAX_HDL_ROWS:
            raise ValueError(f"The HDL prototype handles up to {MAX_HDL_ROWS} receipts; use SQLite.")
        scanned = len(candidates)
        matches = hdl_matches(candidates, criteria, iverilog, vvp)
        rows = [candidates[index] for index in matches[:limit]]
    else:
        raise ValueError("backend must be sqlite or hdl.")
    response = {
        "backend": backend,
        "elapsed_ms": round((perf_counter() - started) * 1000, 3),
        "receipts": [dict(zip(FIELDS, row)) for row in rows],
    }
    if scanned is not None:
        response["scanned"] = scanned
    return response
