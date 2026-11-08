"""Local SQLite index of verified QAM records and cache of readout results."""

import argparse
import json
import re
from pathlib import Path
import sqlite3
from contextlib import closing
from fractions import Fraction

from qam.tools.qamhash import verify


DEFAULT_DB = Path("build/qam.sqlite3")
GRAM_RANGE_RULE = "7C36EDC97D94E61FF80542EC521D2BC9"


def connect(path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path)
    db.executescript("""
        BEGIN IMMEDIATE;
        CREATE TABLE IF NOT EXISTS claims (
            source TEXT, claim_key TEXT, frame TEXT, record TEXT, payload TEXT,
            PRIMARY KEY (source, claim_key)
        );
        CREATE TABLE IF NOT EXISTS readouts (
            identity TEXT PRIMARY KEY, result TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS claims_hash
            ON claims (json_extract(payload, '$.hash'), source, claim_key);
        CREATE TABLE IF NOT EXISTS claim_dependencies (
            claim_hash TEXT NOT NULL,
            premise_hash TEXT NOT NULL,
            PRIMARY KEY (claim_hash, premise_hash)
        ) WITHOUT ROWID;
        CREATE INDEX IF NOT EXISTS claim_dependents
            ON claim_dependencies (premise_hash, claim_hash);
        CREATE TABLE IF NOT EXISTS claim_replacements (
            old_hash TEXT NOT NULL,
            new_hash TEXT NOT NULL CHECK (new_hash <> old_hash),
            reason TEXT NOT NULL CHECK (length(trim(reason)) > 0),
            PRIMARY KEY (old_hash, new_hash)
        ) WITHOUT ROWID;
        CREATE INDEX IF NOT EXISTS claim_replacement_sources
            ON claim_replacements (new_hash, old_hash);
        CREATE TRIGGER IF NOT EXISTS reject_replacement_cycle
        BEFORE INSERT ON claim_replacements
        WHEN EXISTS (
            WITH RECURSIVE successors(digest) AS (
                SELECT NEW.new_hash
                UNION
                SELECT replacement.new_hash FROM successors
                JOIN claim_replacements AS replacement ON replacement.old_hash = successors.digest
            )
            SELECT 1 FROM successors WHERE digest = NEW.old_hash
        )
        BEGIN
            SELECT RAISE(ABORT, 'Replacement would create a cycle');
        END;
        CREATE TABLE IF NOT EXISTS rule_catalog (
            recipe TEXT PRIMARY KEY NOT NULL,
            target TEXT NOT NULL,
            rule_hash TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS rule_requirements (
            recipe TEXT NOT NULL REFERENCES rule_catalog(recipe),
            requirement TEXT NOT NULL,
            required INTEGER NOT NULL CHECK (required IN (0, 1)),
            PRIMARY KEY (recipe, requirement)
        );
        CREATE TABLE IF NOT EXISTS rule_outputs (
            recipe TEXT NOT NULL REFERENCES rule_catalog(recipe),
            quantity TEXT NOT NULL,
            PRIMARY KEY (recipe, quantity)
        ) WITHOUT ROWID;
        CREATE INDEX IF NOT EXISTS rule_output_quantity ON rule_outputs (quantity, recipe);
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
    with db:
        if db.execute("PRAGMA user_version").fetchone()[0] == 0:
            refresh_dependencies(db)
            db.execute("PRAGMA user_version = 1")
        db.execute("INSERT OR IGNORE INTO rule_catalog VALUES (?, ?, ?)",
                   ("em.gram-boost-range", "boosted-gram-range", GRAM_RANGE_RULE))
        db.executemany("INSERT OR IGNORE INTO rule_requirements VALUES (?, ?, ?)", (
            ("em.gram-boost-range", "preparation:E2x-B-unit-yz", 1),
            ("em.gram-boost-range", "boost:z:1/4", 1),
            ("em.gram-boost-range", "measurement:B-dot-ey-interval", 0),
        ))
        db.execute("INSERT OR IGNORE INTO rule_outputs VALUES (?, ?)",
                   ("em.gram-boost-range", "boosted-gram-range"))
    return db


def find_rules(db, target, available):
    """Match declared data against the requirements for a target."""
    rows = db.execute("""
        WITH available(requirement) AS (SELECT value FROM json_each(?))
        , matches AS (
            SELECT rule.recipe, rule.rule_hash,
                   EXISTS (SELECT 1 FROM claims
                           WHERE json_extract(payload, '$.hash') = rule.rule_hash) AS indexed,
                   requirement.requirement, requirement.required,
                   EXISTS (SELECT 1 FROM available
                           WHERE available.requirement = requirement.requirement) AS present
            FROM rule_catalog AS rule
            LEFT JOIN rule_requirements AS requirement USING (recipe)
            WHERE rule.target = ?
        )
        SELECT *, indexed AND NOT MAX(CASE WHEN required AND NOT present THEN 1 ELSE 0 END)
            OVER (PARTITION BY recipe) AS ready
        FROM matches
        ORDER BY recipe, required DESC, requirement
    """, (json.dumps(available), target))
    rules = {}
    for recipe, digest, indexed, requirement, required, present, ready in rows:
        rule = rules.setdefault(recipe, {
            "recipe": recipe, "rule_hash": digest, "indexed": bool(indexed),
            "ready_for_validation": bool(ready), "requirements": [],
        })
        if requirement is not None:
            rule["requirements"].append({
                "name": requirement, "required": bool(required), "present": bool(present),
            })
    return list(rules.values())


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


def refresh_dependencies(db):
    db.execute("DELETE FROM claim_dependencies")
    db.execute("""
        INSERT INTO claim_dependencies
        SELECT DISTINCT json_extract(payload, '$.hash'), premise.value
        FROM claims JOIN json_each(payload, '$.sources') AS premise
    """)


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
        refresh_dependencies(db)
    return len(rows)


def premise_trace(db, roots):
    """Snapshot indexed premises in dependency order, with unresolved hashes."""
    rows = db.execute("""
        WITH RECURSIVE reachable(digest) AS (
            SELECT value FROM json_each(?)
            UNION
            SELECT edge.premise_hash
            FROM reachable AS child
            JOIN claim_dependencies AS edge ON edge.claim_hash = child.digest
        )
        SELECT reachable.digest, claim.source, claim.payload
        FROM reachable
        LEFT JOIN claims AS claim ON claim.rowid = (
            SELECT rowid FROM claims
            WHERE json_extract(payload, '$.hash') = reachable.digest
            ORDER BY source, claim_key LIMIT 1
        )
    """, (json.dumps(roots),))
    claims = {digest: {"source": source, **json.loads(payload)}
              for digest, source, payload in rows if payload is not None}
    nodes = []
    missing = []
    seen = set()
    pending = [(digest, False) for digest in reversed(roots)]
    while pending:
        digest, expanded = pending.pop()
        if expanded:
            nodes.append(claims[digest])
            continue
        if digest in seen:
            continue
        seen.add(digest)
        claim = claims.get(digest)
        if claim is None:
            missing.append(digest)
            continue
        pending.append((digest, True))
        pending.extend((parent, False) for parent in reversed(claim["sources"]))
    return {"roots": roots, "claims": nodes, "missing": missing}


def claim_impact(db, digest):
    """Current downstream claims and historical receipt references."""
    dependents = db.execute("""
        WITH RECURSIVE downstream(digest) AS (
            VALUES (?)
            UNION
            SELECT edge.claim_hash FROM downstream
            JOIN claim_dependencies AS edge ON edge.premise_hash = downstream.digest
        )
        SELECT source, claim_key, json_extract(payload, '$.hash')
        FROM claims WHERE json_extract(payload, '$.hash') IN (SELECT digest FROM downstream)
            AND json_extract(payload, '$.hash') <> ?
        ORDER BY source, claim_key
    """, (digest, digest))
    receipts = db.execute("""
        SELECT receipt_hash, instruction, status, json_extract(request, '$.id'),
               EXISTS (SELECT 1 FROM json_each(receipt, '$.premise_trace.missing')
                       WHERE value = ?) AS missing
        FROM mma_receipts
        WHERE missing OR EXISTS (
            SELECT 1 FROM json_each(receipt, '$.premise_trace.claims')
            WHERE json_extract(value, '$.hash') = ?
        )
        ORDER BY receipt_hash
    """, (digest, digest))
    replacements = db.execute("""
        SELECT old_hash, new_hash, reason FROM claim_replacements
        WHERE old_hash = ? OR new_hash = ? ORDER BY old_hash, new_hash
    """, (digest, digest))
    return {
        "claim_hash": digest,
        "dependents": [dict(source=source, claim_key=key, hash=claim_hash)
                       for source, key, claim_hash in dependents],
        "receipts": [dict(receipt_hash=key, instruction=instruction, status=status,
                          request_id=request_id, premise_missing=bool(missing))
                     for key, instruction, status, request_id, missing in receipts],
        "replacements": [dict(old_hash=old, new_hash=new, reason=reason)
                         for old, new, reason in replacements],
    }


def rule_chains(db, target, max_steps):
    """Suggest catalog paths by matching an output to a requirement."""
    return [json.loads(path) for (path,) in db.execute("""
        WITH RECURSIVE paths(recipe, steps, path) AS (
            SELECT recipe, 1, json_array(recipe) FROM rule_catalog
            UNION ALL
            SELECT requirement.recipe, steps + 1,
                   json_insert(path, '$[#]', requirement.recipe)
            FROM paths JOIN rule_outputs AS output USING (recipe)
            JOIN rule_requirements AS requirement ON requirement.requirement = output.quantity
            WHERE steps < ? AND NOT EXISTS (
                SELECT 1 FROM json_each(path) WHERE value = requirement.recipe
            )
        )
        SELECT DISTINCT path FROM paths JOIN rule_outputs AS output USING (recipe)
        WHERE steps >= 2 AND output.quantity = ? ORDER BY path
    """, (max_steps, target))]


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


def route_mml(db, interface, request, *, use_cache=True, trace=None):
    from qam.tools import route_search, spin_readout_search
    from scripts.qsc_audit import tensor_grammar_check as tensor

    receipt, roots = adapter_receipt(interface, request)
    attach_premises(db, receipt, roots, trace)
    receipt["route_solver_hash"] = tensor.digest_bytes(Path(route_search.__file__).read_bytes())
    receipt["spin_solver_hash"] = tensor.digest_bytes(Path(spin_readout_search.__file__).read_bytes())
    receipt["adapter_hash"] = tensor.digest_bytes(Path(__file__).read_bytes())
    if receipt["mma_status"] == "continue":
        try:
            arguments = request.get("arguments")
            guards = interface.context["qam"]["guards"]

            def calculate():
                return route_search.search(arguments, guards)

            identity = {
                "readout": "op1.search-route",
                "arguments": arguments,
                "context_hash": receipt["context_hash"],
                "premise_hashes": [root.upper() for root in roots],
                "route_solver_hash": receipt["route_solver_hash"],
                "spin_solver_hash": receipt["spin_solver_hash"],
                "adapter_hash": receipt["adapter_hash"],
            }
            result = _cached_readout(db, identity, calculate)[0] if use_cache else calculate()
        except ValueError as error:
            receipt["errors"].append(str(error))
            receipt["mma_status"] = "reject"
        else:
            receipt["result"] = result
            if result.get("channel_check", {}).get("exclusions"):
                receipt["mma_status"] = "guard"
                receipt["obligations"].append("Declared multipoint channel fails a necessary condition")
            if not any(not route["open_guards"] for route in result["routes"]):
                receipt["mma_status"] = "guard"
                receipt["obligations"].append("No unguarded route in the declared search space")
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


def gram_mml(db, interface, request, *, trace=None):
    from scripts.qsc_audit import tensor_grammar_check as tensor

    receipt, roots = adapter_receipt(interface, request)
    if isinstance(roots, list) and GRAM_RANGE_RULE not in roots:
        roots = [GRAM_RANGE_RULE, *roots]
    attach_premises(db, receipt, roots, trace)
    receipt["adapter_hash"] = tensor.digest_bytes(Path(__file__).read_bytes())
    args = request["arguments"]
    fixed = {
        "recipe": "em.gram-boost-range", "preparation": "E2x-B-unit-yz",
        "frame": "Lab", "target_frame": "Boosted", "boost": "z:1/4",
    }
    try:
        if set(args) not in (fixed.keys(), fixed.keys() | {"a", "b"}) or any(
            args[key] != value for key, value in fixed.items()
        ):
            raise ValueError("Gram range requires the declared Lab preparation and z boost to Boosted")
        endpoints = []
        for key, default in (("a", "-1"), ("b", "1")):
            value = args.get(key, default)
            if not isinstance(value, str) or not re.fullmatch(r"-?[0-9]{1,7}(?:/[1-9][0-9]{0,6})?", value):
                raise ValueError("Gram endpoints must be bounded rational strings")
            endpoints.append(Fraction(value))
        a, b = endpoints
        bounds = db.execute("""
            WITH inputs(an, ad, bn, bd) AS (VALUES (?, ?, ?, ?)),
            admissible AS (
                SELECT (8*ad-an)*(8*ad-an) AS left_sq, ad,
                       (8*bd-bn)*(8*bd-bn) AS right_sq, bd
                FROM inputs
                WHERE an >= -ad AND bn <= bd AND an*bd <= bn*ad
            )
            SELECT left_sq, 2*left_sq-45*ad*ad,
                   right_sq, 2*right_sq-45*bd*bd
            FROM admissible
        """, (a.numerator, a.denominator, b.numerator, b.denominator)).fetchone()
        if bounds is None:
            raise ValueError("Gram endpoints must satisfy -1 <= a <= b <= 1")
    except ValueError as error:
        receipt["errors"].append(str(error))
        receipt["mma_status"] = "reject"
    else:
        if receipt["mma_status"] == "continue":
            lo_n, lo_d, hi_n, hi_d = bounds
            receipt["result"] = {
                "rule_hash": GRAM_RANGE_RULE,
                "target_frame": fixed["target_frame"],
                "target": "first diagonal entry of diag(p,1-p)",
                "input_interval": [str(a), str(b)],
                "target_interval": [str(Fraction(lo_n, lo_d)), str(Fraction(hi_n, hi_d))],
            }
    return dict(receipt, receipt_hash=tensor.digest(receipt))


def readout_mml(db, interface, request, *, use_cache=True, trace=None):
    arguments = request.get("arguments")
    if isinstance(arguments, dict) and arguments.get("recipe") == "em.gram-boost-range":
        return gram_mml(db, interface, request, trace=trace)
    return spin_mml(db, interface, request, use_cache=use_cache, trace=trace)


def execute_mml(db, context, request):
    """Run the existing guarded interpreter and persist its receipt."""
    from scripts.qsc_audit.framework_interface import FrameworkInterface

    interface = FrameworkInterface(context)
    instruction = request.get("instruction") if isinstance(request, dict) else None
    if instruction == "READOUT":
        receipt = readout_mml(db, interface, request)
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


def readout_tex(receipt, instruction="READOUT"):
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
    if instruction == "SEARCH_ROUTE":
        output.extend(line(text) for text in receipt["errors"] + receipt["obligations"])
        for route in result.get("routes", []):
            output.append(line("Route: " + " -> ".join(route["operations"])))
            if route["open_guards"]:
                output.append(line("Open guards: " + ", ".join(route["open_guards"])))
        for path in result.get("excluded", []):
            output.append(line("Excluded: " + " -> ".join(path["operations"]) + ". " + path["reason"]))
        channel = result.get("channel_check", {})
        if channel:
            output.append(line(f"Minimum environment dimension: {channel['minimum_environment_dimension']}"))
            if "selective_success_upper_bound" in channel:
                output.append(line("Selective success upper bound: " + channel["selective_success_upper_bound"]))
            output.extend(line(text) for text in channel["exclusions"])
    elif receipt["mma_status"] == "continue" and "target_interval" in result:
        output.append(line("Gram target interval: [" + ", ".join(result["target_interval"]) + "]"))
        output.append(line("QAM rule: " + result["rule_hash"]))
    elif receipt["mma_status"] == "continue":
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


def receipt_summary(receipt, instruction, request):
    summary = {
        "receipt_hash": receipt["receipt_hash"],
        "instruction": instruction,
        "mma_status": receipt["mma_status"],
        "errors": receipt.get("errors", []),
        "obligations": receipt.get("obligations", []),
        "declared_guards": receipt.get("declared_guards", []),
    }
    if instruction == "SEARCH_ROUTE":
        result = receipt["result"]
        routes = result.get("routes", [])
        summary["route_count"] = len(routes)
        summary["open_route_guards"] = sorted({
            guard for route in routes for guard in route.get("open_guards", [])
        })
        if routes:
            minimum = min(len(route.get("open_guards", [])) for route in routes)
            summary["fewest_open_guards"] = minimum
            summary["routes_with_fewest_open_guards"] = [
                {"operations": route["operations"], "open_guards": route.get("open_guards", [])}
                for route in routes if len(route.get("open_guards", [])) == minimum
            ]
        channel = result.get("channel_check")
        if channel:
            summary["channel_exclusions"] = channel.get("exclusions", [])
            declared_channel = request.get("arguments", {}).get("channel", {})
            dimensions = channel.get("fiber") or declared_channel
            summary["channel_dimensions"] = {
                key: dimensions[key]
                for key in ("input_dimension", "output_dimension")
                if key in dimensions
            }
            if "environment_dimension" in declared_channel:
                summary["channel_dimensions"]["declared_environment_dimension"] = (
                    declared_channel["environment_dimension"]
                )
            if "minimum_environment_dimension" in channel:
                summary["channel_dimensions"]["minimum_environment_dimension"] = (
                    channel["minimum_environment_dimension"]
                )
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--read-only", action="store_true")
    commands = parser.add_subparsers(dest="command", required=True)
    index = commands.add_parser("index")
    index.add_argument("root", type=Path, nargs="*")
    find = commands.add_parser("find")
    find.add_argument("query")
    find.add_argument("--limit", type=int)
    rules = commands.add_parser("rules", help="match rules and data requirements for a target")
    rules.add_argument("target")
    rules.add_argument("--have", action="append", default=[], metavar="REQUIREMENT")
    chains = commands.add_parser("chains", help="suggest rule chains for an output quantity")
    chains.add_argument("target")
    chains.add_argument("--max-steps", type=int, choices=range(2, 6), default=3)
    for name, help_text in (
        ("premises", "trace premises of a claim"),
        ("impact", "list downstream claims and historical receipts"),
    ):
        graph = commands.add_parser(name, help=help_text)
        graph.add_argument("claim_hash")
    replace = commands.add_parser("register-replacement", help="record an explicit claim correction")
    replace.add_argument("old_hash")
    replace.add_argument("new_hash")
    replace.add_argument("--reason", required=True)
    mma = commands.add_parser("mma", help="run a guarded MML request and store its receipt")
    mma.add_argument("context", type=Path)
    mma.add_argument("request", type=Path)
    mma.add_argument("--summary", action="store_true", help="return only the receipt identity and MMA diagnostics")
    mma.add_argument("--tex-output", type=Path, help="write a LaTeX fragment for READOUT or SEARCH_ROUTE")
    commands.add_parser("mma-status", help="count distinct stored MMA receipts by status")
    receipts = commands.add_parser("receipts", help="find stored MMA receipts and premise dependents")
    receipts.add_argument("--instruction", choices=("EXPORT", "SCRUB", "READOUT", "SEARCH_ROUTE"))
    receipts.add_argument("--status", choices=("continue", "guard", "reject"))
    receipts.add_argument("--premise", help="QAM claim hash, including transitive premises")
    receipts.add_argument("--limit", type=int, default=20)
    receipt_command = commands.add_parser("receipt", help="retrieve an MMA receipt by SHA-512")
    receipt_command.add_argument("hash", nargs="+", help="hash, optionally in the printed groups")
    receipt_command.add_argument("--tex-output", type=Path, help="regenerate a readout or route fragment")
    receipt_command.add_argument("--replay", action="store_true",
                                 help="rerun against the stored context without using cached results")
    receipt_command.add_argument("--trace", action="store_true",
                                 help="include the stored premise chain in dependency order")
    receipt_command.add_argument("--summary", action="store_true",
                                 help="return only the receipt identity and MMA diagnostics")
    args = parser.parse_args()
    if args.command == "receipt" and args.summary and (args.trace or args.tex_output):
        parser.error("--summary cannot be combined with --trace or --tex-output")
    if args.read_only and (args.command in ("index", "mma", "register-replacement")
                           or getattr(args, "tex_output", None)):
        parser.error("--read-only forbids database updates and file export")
    for name in ("claim_hash", "old_hash", "new_hash"):
        value = getattr(args, name, None)
        if value is not None:
            if re.fullmatch(r"[0-9a-fA-F]{32}", value) is None:
                parser.error(f"{name} requires a 32-digit QAM claim hash")
            setattr(args, name, value.upper())
    if args.read_only and not args.db.is_file():
        parser.exit(1, "QAM database not found. Build its index first.\n")
    database = (sqlite3.connect(args.db.resolve().as_uri() + "?mode=ro", uri=True)
                if args.read_only else connect(args.db))
    with closing(database) as db:
        if args.command == "rules":
            print(json.dumps(find_rules(db, args.target, args.have), indent=2))
        elif args.command == "chains":
            print(json.dumps(rule_chains(db, args.target, args.max_steps), indent=2))
        elif args.command == "premises":
            print(json.dumps(premise_trace(db, [args.claim_hash]), indent=2))
        elif args.command == "impact":
            print(json.dumps(claim_impact(db, args.claim_hash), indent=2))
        elif args.command == "register-replacement":
            try:
                with db:
                    db.execute("INSERT INTO claim_replacements VALUES (?, ?, ?)",
                               (args.old_hash, args.new_hash, args.reason.strip()))
            except sqlite3.IntegrityError as error:
                parser.exit(1, f"Replacement rejected: {error}\n")
        elif args.command == "index":
            if any(not root.is_dir() for root in args.root):
                parser.error("each explicit index root must be a directory")
            roots = args.root or [Path("qam"), Path("notes/research"), Path("build/qam-records")]
            print(f"Indexed {rebuild_index(db, roots)} hash-verified claims.")
        elif args.command == "mma":
            from scripts.qsc_audit import tensor_grammar_check as tensor

            try:
                request = tensor.load_json(args.request)
                if args.tex_output:
                    if not isinstance(request, dict) or request.get("instruction") not in ("READOUT", "SEARCH_ROUTE"):
                        parser.error("--tex-output requires READOUT or SEARCH_ROUTE")
                    output = args.tex_output.resolve()
                    if (output.suffix != ".tex" or output in
                            {path.resolve() for path in (args.context, args.request, args.db)}):
                        parser.error("--tex-output must be a separate .tex file")
                receipt = execute_mml(db, tensor.load_json(args.context), request)
                if args.tex_output:
                    output.parent.mkdir(parents=True, exist_ok=True)
                    output.write_text(readout_tex(receipt, request["instruction"]), encoding="utf-8")
            except (ValueError, TypeError, KeyError, OSError) as error:
                parser.exit(2, f"Framework input/report error: {error}\n")
            if args.summary:
                instruction = request.get("instruction") if isinstance(request, dict) else None
                print(json.dumps(receipt_summary(receipt, instruction, request)))
            else:
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
                if (instruction not in ("READOUT", "SEARCH_ROUTE") or output.suffix != ".tex"
                        or output == args.db.resolve()):
                    parser.error("--tex-output requires a readout or route receipt and a separate .tex file")
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_text(readout_tex(receipt, request["instruction"]), encoding="utf-8")
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
                    current = route_mml(db, interface, request, use_cache=False, trace=receipt.get("premise_trace"))
                elif instruction == "READOUT":
                    current = readout_mml(db, interface, request, use_cache=False, trace=receipt.get("premise_trace"))
                else:
                    current = interface.execute(request)
                response["replay"] = {
                    "receipt_matches": current["receipt_hash"] == digest,
                    "result_matches": current["result"].get("readout", current["result"])
                                      == receipt["result"].get("readout", receipt["result"]),
                    "current_receipt": current,
                }
            if args.summary:
                summary = receipt_summary(receipt, instruction, request)
                if args.replay:
                    summary["replay"] = {
                        "receipt_matches": response["replay"]["receipt_matches"],
                        "result_matches": response["replay"]["result_matches"],
                        "current_receipt_hash": current["receipt_hash"],
                        "changed_fields": sorted(
                            key for key in (receipt.keys() | current.keys()) - {"receipt_hash"}
                            if key not in receipt or key not in current or receipt[key] != current[key]
                        ),
                    }
                print(json.dumps(summary))
            else:
                print(json.dumps(response))
            if args.replay:
                return 0 if response["replay"]["receipt_matches"] else 1
        elif args.command == "receipts":
            if args.limit < 1:
                parser.error("--limit must be positive")
            premise = args.premise.upper() if args.premise else None
            if premise is not None and re.fullmatch(r"[0-9A-F]{32}", premise) is None:
                parser.error("--premise requires a 32-digit QAM claim hash")
            rows = db.execute(
                """SELECT receipt_hash, instruction, status,
                          json_extract(request, '$.id'), context_hash
                   FROM mma_receipts AS entry
                   WHERE (? IS NULL OR instruction = ?)
                     AND (? IS NULL OR status = ?)
                     AND (? IS NULL OR EXISTS (
                         SELECT 1 FROM json_each(entry.receipt, '$.premise_trace.claims')
                         WHERE json_extract(value, '$.hash') = ?
                     ) OR EXISTS (
                         SELECT 1 FROM json_each(entry.receipt, '$.premise_trace.missing')
                         WHERE value = ?
                     ))
                   ORDER BY entry.rowid DESC LIMIT ?""",
                (args.instruction, args.instruction, args.status, args.status,
                 premise, premise, premise, args.limit),
            )
            fields = ("receipt_hash", "instruction", "status", "request_id", "context_hash")
            print(json.dumps([dict(zip(fields, row)) for row in rows]))
        elif args.command == "mma-status":
            print(json.dumps(dict(db.execute("SELECT status, count FROM mma_status_counts ORDER BY status"))))
        else:
            if args.limit is not None and args.limit < 1:
                parser.error("--limit must be positive")
            for source, payload in db.execute(
                """SELECT source, payload FROM claims
                   WHERE instr(lower(payload), lower(?)) > 0 ORDER BY source, claim_key LIMIT ?""",
                (args.query, args.limit if args.limit is not None else -1),
            ):
                print(json.dumps({"source": source, **json.loads(payload)}, ensure_ascii=True))


if __name__ == "__main__":
    raise SystemExit(main())
