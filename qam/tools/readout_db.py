"""Local SQLite index of verified QAM records and cache of readout results."""

import argparse
import json
import re
from pathlib import Path
import sqlite3
from contextlib import closing

from qam.tools.qamhash import verify


DEFAULT_DB = Path("build/qam.sqlite3")


def connect(path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path)
    db.executescript("""
        CREATE TABLE IF NOT EXISTS claims (
            source TEXT, claim_key TEXT, frame TEXT, record TEXT, payload TEXT,
            PRIMARY KEY (source, claim_key)
        );
        CREATE TABLE IF NOT EXISTS readouts (
            identity TEXT PRIMARY KEY, result TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS mma_contexts (
            context_hash TEXT PRIMARY KEY NOT NULL, context TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS mma_receipts (
            receipt_hash TEXT PRIMARY KEY NOT NULL,
            context_hash TEXT NOT NULL,
            instruction TEXT NOT NULL,
            status TEXT NOT NULL CHECK (status IN ('continue', 'guard', 'reject')),
            request TEXT NOT NULL,
            receipt TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS mma_status_counts (
            status TEXT PRIMARY KEY NOT NULL, count INTEGER NOT NULL
        );
        CREATE TRIGGER IF NOT EXISTS count_mma_receipt
        AFTER INSERT ON mma_receipts
        BEGIN
            INSERT INTO mma_status_counts VALUES (NEW.status, 1)
            ON CONFLICT (status) DO UPDATE SET count = count + 1;
        END;
    """)
    return db


def cached_readout(path, identity, calculate):
    """Cache a JSON result against the complete canonical request."""
    with closing(connect(path)) as db:
        return _cached_readout(db, identity, calculate)


def _cached_readout(db, identity, calculate):
    key = json.dumps(identity, sort_keys=True, separators=(",", ":"), allow_nan=False)
    row = db.execute("SELECT result FROM readouts WHERE identity = ?", (key,)).fetchone()
    if row is not None:
        return json.loads(row[0]), True
    result = calculate()
    with db:
        db.execute("INSERT OR IGNORE INTO readouts VALUES (?, ?)",
                   (key, json.dumps(result, allow_nan=False)))
    return result, False


def rebuild_index(db, roots):
    rows = []
    paths = {path.resolve() for root in roots for path in root.rglob("*.qam")}
    for path in sorted(paths):
        if path.parent == Path("qam/examples").resolve() and (
            path.name.startswith("bad_") or path.name == "tampered_statement.qam"
        ):
            continue
        try:
            _, claims, record, errors = verify(path, allow_crlf_source=True)
        except (ValueError, AssertionError) as error:
            print(f"Skipped {path}: {error}")
            continue
        keys = {claim["key"] for claim in claims}
        if errors or len(keys) != len(claims):
            print(f"Skipped {path}: verification failed or duplicate claim keys")
            continue
        base = Path.cwd()
        source = (path.relative_to(base) if path.is_relative_to(base) else path).as_posix()
        for claim in claims:
            rows.append((source, claim["key"], claim["frame"], record, json.dumps(claim, ensure_ascii=False)))
    with db:
        db.execute("DELETE FROM claims")
        db.executemany("INSERT INTO claims VALUES (?, ?, ?, ?, ?)", rows)
    return len(rows)


def premise_trace(db, roots):
    """Snapshot indexed premises in dependency order, with unresolved hashes."""
    nodes = []
    missing = []
    seen = set()

    def visit(digest):
        if digest in seen:
            return
        seen.add(digest)
        row = db.execute(
            """SELECT source, payload FROM claims
               WHERE json_extract(payload, '$.hash') = ?
               ORDER BY source, claim_key LIMIT 1""",
            (digest,),
        ).fetchone()
        if row is None:
            missing.append(digest)
            return
        source, payload = row
        claim = json.loads(payload)
        for parent in claim["sources"]:
            visit(parent)
        nodes.append({"source": source, **claim})

    for root in roots:
        visit(root)
    return {"roots": roots, "claims": nodes, "missing": missing}


def adapter_receipt(interface, request):
    from scripts.qsc_audit import tensor_grammar_check as tensor

    # Reuse the interpreter's envelope and guard validation without running a recipe.
    probe = dict(request, instruction="EXPORT", arguments={"view": "framework"})
    roots = probe.pop("premises", [])
    receipt = interface.execute(probe)
    receipt.pop("receipt_hash")
    receipt["request_hash"] = tensor.digest(request)
    receipt["result"] = {}
    return receipt, roots


def attach_premises(db, receipt, roots, trace):
    if not isinstance(roots, list) or any(
        not isinstance(root, str) or re.fullmatch(r"[0-9A-Fa-f]{32}", root) is None
        for root in roots
    ):
        receipt["errors"].append("Adapter premises must be a list of QAM claim hashes")
        receipt["mma_status"] = "reject"
    elif roots:
        trace = trace if trace is not None else premise_trace(db, [root.upper() for root in roots])
        receipt["premise_trace"] = trace
        if trace["missing"]:
            receipt["obligations"].append("Missing QAM premises: " + ", ".join(trace["missing"]))
            if receipt["mma_status"] == "continue":
                receipt["mma_status"] = "guard"


def route_mml(db, interface, request, *, trace=None):
    from qam.tools import route_search, spin_readout_search
    from scripts.qsc_audit import tensor_grammar_check as tensor

    receipt, roots = adapter_receipt(interface, request)
    attach_premises(db, receipt, roots, trace)
    if receipt["mma_status"] == "continue":
        try:
            result = route_search.search(request.get("arguments"), interface.context["qam"]["guards"])
        except ValueError as error:
            receipt["errors"].append(str(error))
            receipt["mma_status"] = "reject"
        else:
            receipt["result"] = result
            if not any(not route["open_guards"] for route in result["routes"]):
                receipt["mma_status"] = "guard"
                receipt["obligations"].append("No unguarded route in the declared search space")
    receipt["route_solver_hash"] = tensor.digest_bytes(Path(route_search.__file__).read_bytes())
    receipt["spin_solver_hash"] = tensor.digest_bytes(Path(spin_readout_search.__file__).read_bytes())
    receipt["adapter_hash"] = tensor.digest_bytes(Path(__file__).read_bytes())
    return dict(receipt, receipt_hash=tensor.digest(receipt))


def spin_mml(db, interface, request, *, use_cache=True, trace=None):
    """Evaluate the single allowlisted numerical recipe after MMA guard checks."""
    from qam.tools import spin_readout_search as spin
    from scripts.qsc_audit import tensor_grammar_check as tensor

    receipt, roots = adapter_receipt(interface, request)
    args = request.get("arguments")
    if (not isinstance(args, dict) or set(args) != {"recipe", "frame", "max_twice_spin"}
            or args["recipe"] != "op1.spin-counting-effects"
            or args["frame"] not in ("M", "T")
            or type(args["max_twice_spin"]) is not int
            or not 1 <= args["max_twice_spin"] <= 200):
        receipt["errors"].append("READOUT requires the OP1 recipe, frame M/T and integer 2j limit in [1, 200]")
        receipt["mma_status"] = "reject"
    attach_premises(db, receipt, roots, trace)
    if receipt["mma_status"] == "continue":
        frame = args["frame"]
        weights = {j: 2 * int(frame == "M" or j == 1)
                   for j in range(1, args["max_twice_spin"] + 1)}
        identity = {
            "readout": args["recipe"],
            "frame": frame,
            "weights_by_twice_spin": weights,
            "method": "exact-rational, one copy per irrep",
            "implementation_sha256": spin.sha256(Path(spin.__file__).read_bytes()).hexdigest(),
            "context_hash": receipt["context_hash"],
            "adapter_hash": tensor.digest_bytes(Path(__file__).read_bytes()),
            "premise_hashes": [root.upper() for root in roots],
        }
        if use_cache:
            result, _ = _cached_readout(db, identity, lambda: spin.solve(weights))
        else:
            result = spin.solve(weights)
        receipt["result"] = {"identity": identity, "readout": result}
    return dict(receipt, receipt_hash=tensor.digest(receipt))


def execute_mml(db, context, request):
    """Run the existing guarded interpreter and persist its receipt."""
    from scripts.qsc_audit.framework_interface import FrameworkInterface

    interface = FrameworkInterface(context)
    instruction = request.get("instruction") if isinstance(request, dict) else None
    if instruction == "READOUT":
        receipt = spin_mml(db, interface, request)
    elif instruction == "SEARCH_ROUTE":
        receipt = route_mml(db, interface, request)
    else:
        receipt = interface.execute(request)
    with db:
        db.execute("INSERT OR IGNORE INTO mma_contexts VALUES (?, ?)",
                   (receipt["context_hash"], json.dumps(interface.context, allow_nan=False)))
        db.execute(
            """INSERT INTO mma_receipts VALUES (?, ?, ?, ?, ?, ?)
               ON CONFLICT (receipt_hash) DO NOTHING""",
            (receipt["receipt_hash"], receipt["context_hash"],
             instruction if isinstance(instruction, str) else "",
             receipt["mma_status"], json.dumps(request, allow_nan=False),
             json.dumps(receipt, allow_nan=False)),
        )
    return receipt


def readout_tex(receipt):
    """Render the bounded recipe receipt as TeX data, never as raw source text."""
    escapes = {
        chr(92): r"\textbackslash{}", "{": r"\{", "}": r"\}", "$": r"\$",
        "&": r"\&", "#": r"\#", "%": r"\%", "_": r"\_",
        "^": r"\textasciicircum{}", "~": r"\textasciitilde{}",
    }

    def line(value):
        return r"\qamreadoutline{" + "".join(
            escapes.get(char, char) for char in " ".join(value.split())
        ) + "}\n"

    output = [line(f"MMA status: {receipt['mma_status']}")]
    result = receipt["result"]
    if receipt["mma_status"] == "continue":
        from qam.tools.spin_readout_search import report_lines

        output.extend(line(text) for text in report_lines(
            result["identity"]["frame"], result["readout"]
        ))
    else:
        output.extend(line(text) for text in receipt["errors"] + receipt["obligations"])
    digest = receipt["receipt_hash"]
    output.append(line("Receipt SHA-512: " + " ".join(
        digest[index:index + 16] for index in range(0, len(digest), 16)
    )))
    return "".join(output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    commands = parser.add_subparsers(dest="command", required=True)
    index = commands.add_parser("index")
    index.add_argument("root", type=Path, nargs="*")
    find = commands.add_parser("find")
    find.add_argument("query")
    mma = commands.add_parser("mma", help="run a guarded MML request and store its receipt")
    mma.add_argument("context", type=Path)
    mma.add_argument("request", type=Path)
    mma.add_argument("--tex-output", type=Path, help="write a LaTeX fragment for READOUT")
    commands.add_parser("mma-status", help="count distinct stored MMA receipts by status")
    receipt_command = commands.add_parser("receipt", help="retrieve an MMA receipt by SHA-512")
    receipt_command.add_argument("hash", nargs="+", help="hash, optionally in the printed groups")
    receipt_command.add_argument("--tex-output", type=Path, help="regenerate a READOUT fragment")
    receipt_command.add_argument("--replay", action="store_true",
                                 help="rerun against the stored context without using cached results")
    receipt_command.add_argument("--trace", action="store_true",
                                 help="include the stored premise chain in dependency order")
    args = parser.parse_args()
    with closing(connect(args.db)) as db:
        if args.command == "index":
            if any(not root.is_dir() for root in args.root):
                parser.error("each explicit index root must be a directory")
            roots = args.root or [Path("qam"), Path("notes/research"), Path("build/qam-records")]
            print(f"Indexed {rebuild_index(db, roots)} hash-verified claims.")
        elif args.command == "mma":
            from scripts.qsc_audit import tensor_grammar_check as tensor

            try:
                request = tensor.load_json(args.request)
                if args.tex_output:
                    if not isinstance(request, dict) or request.get("instruction") != "READOUT":
                        parser.error("--tex-output requires a READOUT request")
                    output = args.tex_output.resolve()
                    if (output.suffix != ".tex" or output in
                            {path.resolve() for path in (args.context, args.request, args.db)}):
                        parser.error("--tex-output must be a separate .tex file")
                receipt = execute_mml(db, tensor.load_json(args.context), request)
                if args.tex_output:
                    output.parent.mkdir(parents=True, exist_ok=True)
                    output.write_text(readout_tex(receipt), encoding="utf-8")
            except (ValueError, TypeError, KeyError, OSError) as error:
                parser.exit(2, f"Framework input/report error: {error}\n")
            print(json.dumps(receipt))
            return 0 if receipt["mma_status"] == "continue" else 1
        elif args.command == "receipt":
            from scripts.qsc_audit import tensor_grammar_check as tensor

            digest = "".join(args.hash).replace(" ", "").lower()
            row = db.execute(
                "SELECT instruction, request, receipt FROM mma_receipts WHERE receipt_hash = ?",
                (digest,),
            ).fetchone()
            if row is None:
                parser.exit(1, "MMA receipt not found.\n")
            instruction, request_data, receipt_data = row
            request = json.loads(request_data)
            receipt = json.loads(receipt_data)
            body = {key: value for key, value in receipt.items() if key != "receipt_hash"}
            if (receipt.get("receipt_hash") != digest or tensor.digest(body) != digest
                    or tensor.digest(request) != receipt.get("request_hash")):
                parser.exit(2, "Stored MMA receipt or request failed integrity verification.\n")
            if args.tex_output:
                output = args.tex_output.resolve()
                if (instruction != "READOUT" or output.suffix != ".tex"
                        or output == args.db.resolve()):
                    parser.error("--tex-output requires a READOUT receipt and a separate .tex file")
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_text(readout_tex(receipt), encoding="utf-8")
            response = {"request": request, "receipt": receipt}
            if args.trace:
                response["trace"] = receipt.get("premise_trace", {
                    "roots": [], "claims": [], "missing": [],
                    "note": "This receipt has no linked QAM premises.",
                })
            if args.replay:
                from scripts.qsc_audit.framework_interface import FrameworkInterface

                context_row = db.execute(
                    "SELECT context FROM mma_contexts WHERE context_hash = ?",
                    (receipt["context_hash"],),
                ).fetchone()
                if context_row is None:
                    parser.exit(1, "No context snapshot stored for this receipt.\n")
                context = json.loads(context_row[0])
                if tensor.digest(context) != receipt["context_hash"]:
                    parser.exit(2, "Stored MMA context failed integrity verification.\n")
                interface = FrameworkInterface(context)
                if instruction == "SEARCH_ROUTE":
                    current = route_mml(db, interface, request, trace=receipt.get("premise_trace"))
                elif instruction == "READOUT":
                    current = spin_mml(db, interface, request, use_cache=False, trace=receipt.get("premise_trace"))
                else:
                    current = interface.execute(request)
                response["replay"] = {
                    "receipt_matches": current["receipt_hash"] == digest,
                    "result_matches": current["result"].get("readout", current["result"])
                                      == receipt["result"].get("readout", receipt["result"]),
                    "current_receipt": current,
                }
            print(json.dumps(response))
            if args.replay:
                return 0 if response["replay"]["receipt_matches"] else 1
        elif args.command == "mma-status":
            print(json.dumps(dict(db.execute("SELECT status, count FROM mma_status_counts ORDER BY status"))))
        else:
            for source, payload in db.execute(
                """SELECT source, payload FROM claims
                   WHERE instr(lower(payload), lower(?)) > 0 ORDER BY source, claim_key""",
                (args.query,),
            ):
                print(json.dumps({"source": source, **json.loads(payload)}, ensure_ascii=True))


if __name__ == "__main__":
    raise SystemExit(main())
