"""Local SQLite index of verified QAM records and cache of readout results."""

import argparse
import json
import re
from pathlib import Path
import sqlite3
import sys
from concurrent.futures import FIRST_COMPLETED, ProcessPoolExecutor, wait
from contextlib import closing
from fractions import Fraction
from itertools import combinations, islice, permutations
from math import factorial

from qam.tools.qamhash import verify


DEFAULT_DB = Path("build/qam.sqlite3")
GRAM_RANGE_RULE = "7C36EDC97D94E61FF80542EC521D2BC9"
MARKED_RING_RULE = "615F0E4DF0932311F66EDCB74924463E"


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
        CREATE TABLE IF NOT EXISTS mma_batch_reports (
            report_hash TEXT PRIMARY KEY NOT NULL,
            batch TEXT NOT NULL,
            report TEXT NOT NULL
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
        recipe = "op1.marked-ring-pair-certificate"
        target = "marked-ring-transport-certificate"
        db.execute("INSERT OR IGNORE INTO rule_catalog VALUES (?, ?, ?)",
                   (recipe, target, MARKED_RING_RULE))
        db.executemany("INSERT OR IGNORE INTO rule_requirements VALUES (?, ?, 1)", (
            (recipe, "model:eight-spin-half-ring"),
            (recipe, "candidate:unitary-marked-step"),
            (recipe, "evidence:seven-exact-pair-yes-no-intertwiners"),
        ))
        db.execute("INSERT OR IGNORE INTO rule_outputs VALUES (?, ?)", (recipe, target))
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


def marked_ring_mml(db, interface, request, *, trace=None):
    from scripts.qsc_audit import tensor_grammar_check as tensor

    receipt, roots = adapter_receipt(interface, request)
    if isinstance(roots, list) and MARKED_RING_RULE not in roots:
        roots = [MARKED_RING_RULE, *roots]
    attach_premises(db, receipt, roots, trace)
    receipt["adapter_hash"] = tensor.digest_bytes(Path(__file__).read_bytes())
    args = request["arguments"]
    permutation = args.get("permutation")
    pauli = args.get("last_spin_pauli", "I")
    if (set(args) not in ({"recipe", "permutation"}, {"recipe", "permutation", "last_spin_pauli"})
            or not isinstance(permutation, list)
            or len(permutation) != 8 or any(type(point) is not int for point in permutation)
            or set(permutation) != set(range(8)) or pauli not in ("I", "X", "Y", "Z")):
        receipt["errors"].append(
            "Expected a permutation of labels 0 through 7 and an optional Pauli I, X, Y or Z."
        )
        receipt["mma_status"] = "reject"
    elif receipt["mma_status"] == "continue":
        failed = [
            i for i in range(7)
            if {permutation[i], permutation[i + 1]} != {i + 1, (i + 2) % 8}
            or (i == 6 and pauli != "I")
        ]
        receipt["result"] = {
            "rule_hash": MARKED_RING_RULE,
            "scope": "Declared eight-spin point permutation with optional Pauli on the moved last spin.",
            "failed_pair_indices": failed,
            "first_six_pairs_preserved": all(i == 6 for i in failed),
            "seventh_pair_yes_preserved": 6 not in failed,
            "matches_ring_rotation_on_singlet": not failed,
        }
        if failed:
            receipt["obligations"].append("The candidate fails exact adjacent pair transport.")
            receipt["mma_status"] = "guard"
    return dict(receipt, receipt_hash=tensor.digest(receipt))


def split_singlet_block(permutation, blocks):
    """Find a pair in one input block whose images land in different blocks."""
    membership = {point: index for index, block in enumerate(blocks) for point in block}
    for block in blocks:
        left = block[0]
        for right in block[1:]:
            if membership[permutation[left]] != membership[permutation[right]]:
                return {"input_pair": [left, right],
                        "split_image": [permutation[left], permutation[right]]}
    return None


def ring_singlet_partitions(onsite, neighbor):
    """Enumerate invariant even partitions for the transitive two-ring action."""
    partitions = []
    for size in (2, 4, 8, 16):
        for tail in combinations(range(1, 16), size - 1):
            initial = frozenset((0, *tail))
            blocks = [initial]
            seen = {initial}
            covered = set(initial)
            for block in blocks:
                for operation in (onsite, neighbor):
                    image = frozenset(operation[point] for point in block)
                    if image in seen:
                        continue
                    if image & covered:
                        break
                    blocks.append(image)
                    seen.add(image)
                    covered.update(image)
                else:
                    continue
                break
            else:
                if len(covered) == 16:
                    partitions.append({
                        "block_size": size,
                        "blocks": sorted(sorted(block) for block in blocks),
                        "admits_full_input": all(
                            sum(point < 8 for point in block) in (0, 8)
                            and sum(point >= 8 for point in block) in (0, 8)
                            for block in blocks
                        ),
                    })
    return partitions


def ring_holonomy_check(edges):
    """Check eight exact unit quaternions in traversal order."""
    if not isinstance(edges, list) or len(edges) != 8:
        raise ValueError("Expected eight edge holonomies.")
    product = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    transports = []
    for edge in edges:
        if (not isinstance(edge, list) or len(edge) != 4
                or any(not isinstance(value, str)
                       or not re.fullmatch(r"-?[0-9]{1,7}(?:/[1-9][0-9]{0,6})?", value)
                       for value in edge)):
            raise ValueError("Each holonomy needs four bounded rational strings.")
        a, b, c, d = map(Fraction, edge)
        if a*a + b*b + c*c + d*d != 1:
            raise ValueError("Each holonomy must be a unit quaternion.")
        transports.append((a, b, c, d))
        e, f, g, h = product
        product = (a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
                   a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e)
    fixed_frame_witness = None
    for index, transport in enumerate(transports[1:], 1):
        probability = sum(a * b for a, b in zip(transports[0], transport)) ** 2
        if probability != 1:
            fixed_frame_witness = {
                "source_pair": [0, index],
                "yes_probability": str(probability),
            }
            break
    amplitude = abs(product[0])
    if amplitude == 1:
        recovery = {"status": "direct"}
    elif not amplitude:
        recovery = {"status": "zero_singlet_return"}
    else:
        recovery = {
            "status": "conditional_amplification",
            "success_probability": str(amplitude ** 2),
            "additional_requirements": [
                "Coherent control of the repeated holonomic step",
                "Point-to-rest exchange reflection at the two marked sites",
            ],
        }
        if amplitude >= Fraction(1, 2):
            recovery["one_step_amplification"] = {
                "ancilla_amplitude": str(Fraction(1, 2) / amplitude),
                "forward_step_count": 9,
                "output_sign": 1 if product[0] > 0 else -1,
            }
    if amplitude != 1:
        recovery["fixed_pair_route"] = {
            "forward_step_count": 8,
            "fixed_pair_swap_count": 7,
            "fixed_pair": [0, 1],
            "initial_forward_steps": 2,
            "forward_steps_between_swaps": 1,
            "additional_requirements": [
                "Coherent gravitational swap at the fixed pair",
                "Access to intermediate states outside the global singlet",
            ],
        }
    scalar, x, y, z = product
    axis_overlap = 1 - 2 * (x*x + y*y)
    parity_axes = {
        "assumed_first_axis": "z",
        "axis_overlap": str(axis_overlap),
        "independent": abs(axis_overlap) != 1,
        "triplet_overlap_probability": str(axis_overlap ** 2),
    }
    if parity_axes["independent"]:
        phase_cosine = 2 * axis_overlap ** 2 - 1
        previous, cosine = Fraction(1), phase_cosine
        for power in range(1, 33):
            if cosine <= 0:
                parity_axes["reflection_product_power"] = power
                if max(cosine.numerator.bit_length(), cosine.denominator.bit_length()) <= 12000:
                    parity_axes["one_test_weights"] = {
                        "identity": str(-cosine / (1 - cosine)),
                        "forward": str(1 / (2 * (1 - cosine))),
                        "inverse": str(1 / (2 * (1 - cosine))),
                    }
                else:
                    parity_axes["weights_exceed_size_limit"] = True
                break
            previous, cosine = cosine, 2 * phase_cosine * cosine - previous
        else:
            parity_axes["reflection_product_power_exceeds"] = 32
    return {
        "loop_quaternion": [str(value) for value in product],
        "central": not any(product[1:]),
        "witness_pair_yes_probability": str(product[0] ** 2),
        "fixed_frame_singlet_preserved": fixed_frame_witness is None,
        "fixed_frame_witness": fixed_frame_witness,
        "parallel_frame_recovery": recovery,
        "parallel_frame_parity_axes": parity_axes,
    }


def marked_ring_synthesis(db, interface, request, *, trace=None):
    from scripts.qsc_audit import tensor_grammar_check as tensor

    receipt, roots = adapter_receipt(interface, request)
    if isinstance(roots, list) and MARKED_RING_RULE not in roots:
        roots = [MARKED_RING_RULE, *roots]
    attach_premises(db, receipt, roots, trace)
    receipt["adapter_hash"] = tensor.digest_bytes(Path(__file__).read_bytes())
    args = request["arguments"]
    count = args.get("pair_count")
    blocks = args.get("singlet_blocks")
    enumerate_blocks = args.get("enumerate_singlet_blocks", False)
    holonomy = None
    if "edge_holonomies" in args:
        try:
            holonomy = ring_holonomy_check(args["edge_holonomies"])
        except ValueError as error:
            receipt["errors"].append(str(error))
            receipt["mma_status"] = "reject"
    if (set(args) - {"recipe", "pair_count", "singlet_blocks", "enumerate_singlet_blocks",
                     "edge_holonomies"}
            or type(count) is not int
            or not 1 <= count <= 7 or type(enumerate_blocks) is not bool):
        receipt["errors"].append("Expected a prefix of one to seven shifted adjacent pairs.")
        receipt["mma_status"] = "reject"
    elif "singlet_blocks" in args and (
        not isinstance(blocks, list)
        or any(not isinstance(block, list) or not block or len(block) % 2
               or any(type(point) is not int for point in block) for block in blocks)
        or sorted(point for block in blocks for point in block) != list(range(16))
    ):
        receipt["errors"].append("Singlet blocks must partition labels 0 through 15 into even blocks.")
        receipt["mma_status"] = "reject"
    elif receipt["mma_status"] == "continue":
        rotation = [(i + 1) % 8 for i in range(8)]
        prefixes = ([1, 2], [2, 1]) if count == 1 else (rotation[:count + 1],)
        completions = (
            prefix + list(tail)
            for prefix in prefixes
            for tail in permutations(sorted(set(range(8)) - set(prefix)))
        )
        candidate_count = len(prefixes) * factorial(7 - count)
        result = {
            "scope": "Eight-point permutations satisfying a prefix of shifted pair constraints.",
            "pair_count": count,
            "candidate_count": candidate_count,
            "candidates": list(islice(completions, 8)),
            "all_candidates_returned": candidate_count <= 8,
        }
        if candidate_count == 1:
            onsite = [(i + 8) % 16 for i in range(16)]
            neighbor = [8 + (i - 1) % 8 for i in range(8)] + rotation
            composed = [neighbor[onsite[i]] for i in range(16)]
            result["model_route"] = {
                "register_order": "L0..L7,R0..R7",
                "layers": [onsite, neighbor],
                "left_action": composed[:8],
                "right_action": [point - 8 for point in composed[8:]],
                "reference_condition": "The right reference is a rotation eigenstate.",
                "open_native_requirements": [
                    "Gravitational onsite left-right exchange",
                    "Gravitational left-right exchange to the marked neighbor",
                ],
            }
            receipt["obligations"].extend(result["model_route"]["open_native_requirements"])
            if holonomy is not None:
                result["model_route"]["holonomy_check"] = holonomy
                if not holonomy["central"]:
                    receipt["obligations"].append(
                        "Noncentral holonomy fails the parallel-frame singlet pair test."
                    )
            if enumerate_blocks:
                partitions = ring_singlet_partitions(onsite, neighbor)
                result["model_route"]["invariant_singlet_partitions"] = partitions
                result["model_route"]["full_input_partition_count"] = sum(
                    entry["admits_full_input"] for entry in partitions
                )
            if blocks is not None:
                checks = {
                    name: split_singlet_block(operation, blocks)
                    for name, operation in (("onsite", onsite), ("neighbor", neighbor),
                                            ("composition", composed))
                }
                result["model_route"]["split_singlet_blocks"] = checks
                if any(checks.values()):
                    receipt["obligations"].append(
                        "A layer or the composition splits the declared fixed singlet partition."
                    )
        else:
            receipt["obligations"].append("The declared pair constraints leave multiple candidates.")
        receipt["result"] = result
        receipt["mma_status"] = "guard"
    return dict(receipt, receipt_hash=tensor.digest(receipt))


def marked_ring_pair_search(db, interface, request, *, trace=None):
    from scripts.qsc_audit import tensor_grammar_check as tensor

    receipt, roots = adapter_receipt(interface, request)
    attach_premises(db, receipt, roots, trace)
    receipt["adapter_hash"] = tensor.digest_bytes(Path(__file__).read_bytes())
    args = request["arguments"]
    constraints = args.get("pair_constraints")
    if (set(args) != {"recipe", "pair_constraints"}
            or not isinstance(constraints, list) or not 1 <= len(constraints) <= 28
            or any(not isinstance(row, dict) or set(row) != {"source", "target"}
                   for row in constraints)
            or any(not isinstance(pair, list) or len(pair) != 2
                   or any(type(point) is not int or not 0 <= point < 8 for point in pair)
                   or pair[0] == pair[1]
                   for row in constraints for pair in row.values())):
        receipt["errors"].append(
            "Expected 1 to 28 source/target pairs of distinct point labels from 0 through 7."
        )
        receipt["mma_status"] = "reject"
    elif receipt["mma_status"] == "continue":
        candidates = list(permutations(range(8)))
        result = {
            "scope": "Eight-point permutations mapping each unordered source pair to its target.",
            "pair_count": len(constraints),
        }
        for index, row in enumerate(constraints):
            left, right = row["source"]
            target = set(row["target"])
            remaining = [p for p in candidates if {p[left], p[right]} == target]
            if not remaining:
                result["pair_conflict"] = {
                    "constraint_index": index,
                    "preceding_candidate_count": len(candidates),
                    "preceding_candidate": list(candidates[0]),
                    "actual_image": sorted((candidates[0][left], candidates[0][right])),
                    "required_image": sorted(target),
                }
            candidates = remaining
            if not candidates:
                break
        result.update(candidate_count=len(candidates),
                      candidates=[list(p) for p in candidates[:8]],
                      all_candidates_returned=len(candidates) <= 8)
        receipt["result"] = result
    return dict(receipt, receipt_hash=tensor.digest(receipt))


def readout_mml(db, interface, request, *, use_cache=True, trace=None):
    arguments = request.get("arguments")
    if isinstance(arguments, dict) and arguments.get("recipe") == "em.gram-boost-range":
        return gram_mml(db, interface, request, trace=trace)
    if isinstance(arguments, dict) and arguments.get("recipe") == "op1.marked-ring-pair-certificate":
        return marked_ring_mml(db, interface, request, trace=trace)
    if isinstance(arguments, dict) and arguments.get("recipe") == "op1.marked-ring-synthesis":
        return marked_ring_synthesis(db, interface, request, trace=trace)
    if isinstance(arguments, dict) and arguments.get("recipe") == "op1.marked-ring-pair-search":
        return marked_ring_pair_search(db, interface, request, trace=trace)
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
        store_mml_receipt(db, interface.context, request, receipt, instruction)
    return receipt


def store_mml_receipt(db, context, request, receipt, instruction):
    db.execute("INSERT OR IGNORE INTO mma_contexts VALUES (?, ?)",
               (receipt["context_hash"], json.dumps(context, allow_nan=False)))
    db.execute(
        """INSERT INTO mma_receipts VALUES (?, ?, ?, ?, ?, ?)
           ON CONFLICT (receipt_hash) DO NOTHING""",
        (receipt["receipt_hash"], receipt["context_hash"],
         instruction if isinstance(instruction, str) else "",
         receipt["mma_status"], json.dumps(request, allow_nan=False),
         json.dumps(receipt, allow_nan=False)),
    )


def calculate_pair_request(context, request, trace):
    from scripts.qsc_audit.framework_interface import FrameworkInterface

    return marked_ring_pair_search(None, FrameworkInterface(context), request, trace=trace)


def pair_batch_blockers(parents, required_matches, completed):
    return [
        parent for parent in parents
        if completed[parent]["mma_status"] != "continue"
        or (parent in required_matches and not completed[parent].get("candidate_count"))
    ]


def execute_pair_batch(db, context, batch, workers, *, persist=True):
    """Compute pair requests in dependency order without worker database access."""
    from scripts.qsc_audit.framework_interface import FrameworkInterface
    from scripts.qsc_audit import tensor_grammar_check as tensor

    requests = batch.get("requests") if isinstance(batch, dict) else None
    if (not isinstance(requests, list) or not 1 <= len(requests) <= 64
            or set(batch) - {"requests", "depends_on", "requires_match"}
            or any(not isinstance(request, dict) or request.get("instruction") != "READOUT"
                   or not isinstance(request.get("arguments"), dict)
                   or request["arguments"].get("recipe") != "op1.marked-ring-pair-search"
                   or not isinstance(request.get("id"), str) or not request["id"].strip()
                   for request in requests)):
        raise ValueError("Expected 1 to 64 independent marked-ring pair READOUT requests.")
    if len({request["id"] for request in requests}) != len(requests):
        raise ValueError("Batch request IDs must be unique.")
    ids = [request["id"] for request in requests]
    dependencies = batch.get("depends_on", {})
    if (not isinstance(dependencies, dict) or set(dependencies) - set(ids)
            or any(not isinstance(parents, list)
                   or any(not isinstance(parent, str) or parent not in ids for parent in parents)
                   or len(set(parents)) != len(parents)
                   for parents in dependencies.values())):
        raise ValueError("Batch dependencies must name existing request IDs without duplicates.")
    required_matches = batch.get("requires_match", {})
    if (not isinstance(required_matches, dict) or set(required_matches) - set(ids)
            or any(not isinstance(parents, list)
                   or any(not isinstance(parent, str) or parent not in dependencies.get(key, [])
                          for parent in parents)
                   or len(set(parents)) != len(parents)
                   for key, parents in required_matches.items())):
        raise ValueError("Match requirements must name declared predecessors without duplicates.")
    pending = ids.copy()
    resolved = set()
    while pending:
        ready = [key for key in pending if resolved.issuperset(dependencies.get(key, []))]
        if not ready:
            raise ValueError("Batch dependencies contain a cycle.")
        resolved.update(ready)
        pending = [key for key in pending if key not in resolved]
    context = FrameworkInterface(context).context
    traces = []
    with db:
        db.execute("BEGIN")
        for request in requests:
            roots = request.get("premises", [])
            if isinstance(roots, list) and roots and all(
                isinstance(root, str) and re.fullmatch(r"[0-9A-Fa-f]{32}", root) for root in roots
            ):
                traces.append(premise_trace(db, [root.upper() for root in roots]))
            else:
                traces.append(None)

    inputs = dict(zip(ids, zip(requests, traces)))
    receipts = {}
    pending = ids.copy()
    completed_entries = {}
    worker_count = min(workers, len(ids))
    with ProcessPoolExecutor(max_workers=worker_count) as pool:
        running = {}
        while pending or running:
            for key in pending.copy():
                parents = dependencies.get(key, [])
                if not completed_entries.keys() >= set(parents):
                    continue
                failed = pair_batch_blockers(parents, required_matches.get(key, []), completed_entries)
                if failed:
                    completed_entries[key] = {
                        "id": key, "mma_status": "blocked", "blocked_by": failed,
                    }
                elif len(running) < worker_count:
                    running[pool.submit(calculate_pair_request, context, *inputs[key])] = key
                else:
                    continue
                pending.remove(key)
            if running:
                completed, _ = wait(running, return_when=FIRST_COMPLETED)
                for future in completed:
                    key = running.pop(future)
                    receipts[key] = future.result()
                    completed_entries[key] = {
                        "id": key, **receipt_summary(receipts[key], "READOUT", inputs[key][0])
                    }
    report = {
        "batch_hash": tensor.digest(batch),
        "context_hash": receipts[next(key for key in ids if key in receipts)]["context_hash"],
        "entries": [completed_entries[key] for key in ids],
    }
    report["report_hash"] = tensor.digest(report)
    if not persist:
        return report
    with db:
        for key in ids:
            if key in receipts:
                store_mml_receipt(db, context, inputs[key][0], receipts[key], "READOUT")
        db.execute(
            """INSERT INTO mma_batch_reports VALUES (?, ?, ?)
               ON CONFLICT (report_hash) DO NOTHING""",
            (report["report_hash"], json.dumps(batch, allow_nan=False),
             json.dumps(report, allow_nan=False)),
        )
    return report


def read_pair_batch_report(db, report_hash):
    from scripts.qsc_audit import tensor_grammar_check as tensor

    if not db.execute(
        "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'mma_batch_reports'"
    ).fetchone():
        return None
    row = db.execute("SELECT batch, report FROM mma_batch_reports WHERE report_hash = ?",
                     (report_hash,)).fetchone()
    if row is None:
        return None
    batch, report = map(json.loads, row)
    body = {key: value for key, value in report.items() if key != "report_hash"}
    if (report.get("report_hash") != report_hash or tensor.digest(body) != report_hash
            or tensor.digest(batch) != report.get("batch_hash")):
        raise ValueError("Stored MMA batch report or input failed integrity verification.")
    return {"batch": batch, "report": report}


def compare_pair_batch_reports(previous, current):
    old_entries = {entry["id"]: entry for entry in previous["entries"]}
    new_entries = {entry["id"]: entry for entry in current["entries"]}
    changes = []
    for key in dict.fromkeys([*old_entries, *new_entries]):
        old = old_entries.get(key, {})
        new = new_entries.get(key, {})
        fields = sorted(field for field in old.keys() | new.keys()
                        if field not in old or field not in new or old[field] != new[field])
        if fields:
            changes.append({"id": key, "changed_fields": fields,
                            "previous_status": old.get("mma_status"),
                            "current_status": new.get("mma_status")})
    return {
        "report_hash": previous["report_hash"],
        "current_report_hash": current["report_hash"],
        "report_matches": current == previous,
        "changes": changes,
    }


def audit_pair_batch_report(db, stored):
    from scripts.qsc_audit import tensor_grammar_check as tensor

    batch, report = stored["batch"], stored["report"]
    entries = report["entries"]
    requests = batch["requests"]
    entries_by_id = {entry["id"]: entry for entry in entries}
    issues = []
    verified_receipts = 0
    verified_blocked = 0
    context = db.execute("SELECT context FROM mma_contexts WHERE context_hash = ?",
                         (report["context_hash"],)).fetchone()
    if context is None or tensor.digest(json.loads(context[0])) != report["context_hash"]:
        issues.append({"error": "Missing or mismatched context snapshot."})
    if [entry["id"] for entry in entries] != [request["id"] for request in requests]:
        issues.append({"error": "Report entries do not match the batch request order."})
    for entry, request in zip(entries, requests):
        key = entry["id"]
        if key != request["id"]:
            continue
        predecessors = batch.get("depends_on", {}).get(key, [])
        if any(parent not in entries_by_id for parent in predecessors):
            issues.append({"id": key, "error": "Missing predecessor entry."})
            continue
        blocked_by = pair_batch_blockers(
            predecessors, batch.get("requires_match", {}).get(key, []), entries_by_id
        )
        if entry["mma_status"] == "blocked":
            if blocked_by and entry.get("blocked_by") == blocked_by and "receipt_hash" not in entry:
                verified_blocked += 1
            else:
                issues.append({"id": key, "error": "Invalid blocked entry."})
            continue
        digest = entry.get("receipt_hash")
        row = db.execute("SELECT instruction, request, receipt FROM mma_receipts WHERE receipt_hash = ?",
                         (digest,)).fetchone()
        if row is None:
            issues.append({"id": key, "error": "Missing individual receipt."})
            continue
        try:
            instruction, stored_request, body = row
            receipt = json.loads(body)
            payload = {field: value for field, value in receipt.items() if field != "receipt_hash"}
            valid = (
                not blocked_by and instruction == request["instruction"]
                and json.loads(stored_request) == request and receipt["request_hash"] == tensor.digest(request)
                and receipt["context_hash"] == report["context_hash"]
                and receipt["receipt_hash"] == digest and tensor.digest(payload) == digest
                and entry == {"id": key, **receipt_summary(receipt, instruction, request)}
            )
        except (ValueError, AttributeError, KeyError, TypeError):
            valid = False
        if valid:
            verified_receipts += 1
        else:
            issues.append({"id": key, "error": "Receipt, request, context or summary mismatch."})
    return {"report_hash": report["report_hash"], "verified": not issues,
            "verified_receipts": verified_receipts, "verified_blocked": verified_blocked,
            "issues": issues}


def replay_pair_batch_report(db, report_hash, workers):
    from scripts.qsc_audit import tensor_grammar_check as tensor

    stored = read_pair_batch_report(db, report_hash)
    if stored is None:
        raise ValueError("MMA batch report not found.")
    previous = stored["report"]
    context_hash = previous["context_hash"]
    row = db.execute("SELECT context FROM mma_contexts WHERE context_hash = ?",
                     (context_hash,)).fetchone()
    if row is None:
        raise ValueError("No context snapshot stored for this MMA batch report.")
    context = json.loads(row[0])
    if tensor.digest(context) != context_hash:
        raise ValueError("Stored MMA batch context failed integrity verification.")
    current = execute_pair_batch(db, context, stored["batch"], workers, persist=False)
    return compare_pair_batch_reports(previous, current)


def list_pair_batch_reports(db, limit, request_id=None, status=None):
    if not db.execute(
        "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'mma_batch_reports'"
    ).fetchone():
        return []
    if request_id is None and status is None:
        rows = db.execute("SELECT report_hash FROM mma_batch_reports ORDER BY rowid DESC LIMIT ?",
                          (limit,))
    else:
        rows = db.execute(
            """SELECT report_hash FROM mma_batch_reports
               WHERE EXISTS (
                   SELECT 1 FROM json_each(report, '$.entries') AS entry
                   WHERE (? IS NULL OR json_extract(entry.value, '$.id') = ?)
                     AND (? IS NULL OR json_extract(entry.value, '$.mma_status') = ?)
               )
               ORDER BY rowid DESC LIMIT ?""",
            (request_id, request_id, status, status, limit),
        )
    summaries = []
    for (report_hash,) in rows:
        report = read_pair_batch_report(db, report_hash)["report"]
        counts = {"continue": 0, "guard": 0, "reject": 0, "blocked": 0}
        for entry in report["entries"]:
            counts[entry["mma_status"]] += 1
        summaries.append({
            "report_hash": report_hash,
            "batch_hash": report["batch_hash"],
            "request_ids": [entry["id"] for entry in report["entries"]],
            "status_counts": counts,
        })
    return summaries


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
    elif "candidate_count" in result:
        output.append(line(f"Matching permutations: {result['candidate_count']}"))
        if conflict := result.get("pair_conflict"):
            output.append(line(
                f"Constraint {conflict['constraint_index'] + 1} eliminates the remaining candidates. "
                f"Witness image {conflict['actual_image']}, required {conflict['required_image']}."
            ))
        output.extend(line(text) for text in receipt["errors"] + receipt["obligations"])
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
    if "failed_pair_indices" in receipt["result"]:
        for key in ("failed_pair_indices", "first_six_pairs_preserved", "seventh_pair_yes_preserved"):
            if key in receipt["result"]:
                summary[key] = receipt["result"][key]
    if instruction == "READOUT" and "candidate_count" in receipt["result"]:
        for key in ("pair_count", "candidate_count", "candidates", "all_candidates_returned",
                    "pair_conflict"):
            if key in receipt["result"]:
                summary[key] = receipt["result"][key]
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
    batch_command = commands.add_parser("mma-batch", help="run a batch of marked-ring pair requests")
    batch_command.add_argument("context", type=Path)
    batch_command.add_argument("batch", type=Path, help="batch JSON file, or - to read standard input")
    batch_command.add_argument("--workers", type=int, choices=range(1, 5), default=2)
    batch_report = commands.add_parser("batch-report", help="retrieve a verified MMA batch report")
    batch_report.add_argument("report_hash")
    batch_report.add_argument("--report-only", action="store_true", help="omit the original input")
    replay_batch = commands.add_parser("replay-batch", help="recompute a verified MMA batch report")
    replay_batch.add_argument("report_hash")
    replay_batch.add_argument("--workers", type=int, choices=range(1, 5), default=2)
    compare_batch = commands.add_parser("compare-batches", help="compare two verified MMA batch reports")
    compare_batch.add_argument("previous_hash")
    compare_batch.add_argument("current_hash")
    audit_batch = commands.add_parser("audit-batch", help="verify report links to its individual receipts")
    audit_batch.add_argument("report_hash")
    batch_reports = commands.add_parser("batch-reports", help="list recent verified MMA batch reports")
    batch_reports.add_argument("--limit", type=int, choices=range(1, 51), default=10,
                               metavar="1..50")
    batch_reports.add_argument("--request-id", help="match this exact request ID")
    batch_reports.add_argument("--status", choices=("continue", "guard", "reject", "blocked"))
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
    if args.read_only and (args.command in ("index", "mma", "mma-batch", "register-replacement")
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
        elif args.command == "batch-reports":
            try:
                print(json.dumps(list_pair_batch_reports(db, args.limit, args.request_id, args.status)))
            except (ValueError, AttributeError, TypeError, KeyError, sqlite3.OperationalError) as error:
                parser.exit(2, f"{error}\n")
        elif args.command == "compare-batches":
            hashes = ["".join(value.split()).lower()
                      for value in (args.previous_hash, args.current_hash)]
            if any(not re.fullmatch(r"[0-9a-f]{128}", value) for value in hashes):
                parser.error("compare-batches requires two 128-digit SHA-512 hashes")
            try:
                reports = [read_pair_batch_report(db, value) for value in hashes]
                for value, stored in zip(hashes, reports):
                    if stored is None:
                        raise ValueError(f"MMA batch report not found: {value}")
                previous, current = (stored["report"] for stored in reports)
                comparison = compare_pair_batch_reports(previous, current)
                comparison["batch_matches"] = previous["batch_hash"] == current["batch_hash"]
                comparison["context_matches"] = previous["context_hash"] == current["context_hash"]
                comparison["request_order_matches"] = (
                    [entry["id"] for entry in previous["entries"]]
                    == [entry["id"] for entry in current["entries"]]
                )
            except (ValueError, AttributeError, TypeError, KeyError) as error:
                parser.exit(2, f"{error}\n")
            print(json.dumps(comparison))
        elif args.command in ("batch-report", "replay-batch", "audit-batch"):
            digest = "".join(args.report_hash.split()).lower()
            if not re.fullmatch(r"[0-9a-f]{128}", digest):
                parser.error("batch-report requires a 128-digit SHA-512 hash")
            try:
                if args.command == "replay-batch":
                    result = replay_pair_batch_report(db, digest, args.workers)
                else:
                    result = read_pair_batch_report(db, digest)
                    if result is not None:
                        if args.command == "audit-batch":
                            result = audit_pair_batch_report(db, result)
                        elif args.report_only:
                            result = result["report"]
            except (ValueError, AttributeError, TypeError, KeyError, OSError, RuntimeError) as error:
                parser.exit(2, f"{error}\n")
            if result is None:
                parser.exit(1, "MMA batch report not found. Run the batch to store its report.\n")
            print(json.dumps(result))
            if args.command == "audit-batch":
                return int(not result["verified"])
        elif args.command == "mma-batch":
            from scripts.qsc_audit import tensor_grammar_check as tensor

            try:
                batch = (json.load(sys.stdin.buffer) if args.batch == Path("-")
                         else tensor.load_json(args.batch))
                report = execute_pair_batch(db, tensor.load_json(args.context), batch, args.workers)
            except (ValueError, TypeError, KeyError, OSError, RuntimeError) as error:
                parser.exit(2, f"Framework input/report error: {error}\n")
            print(json.dumps(report))
            return int(any(entry["mma_status"] != "continue" for entry in report["entries"]))
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
