"""Check explicit QAM role data; no TeX parser or mathematical proof engine."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

VERSION = "qam-role-audit/2"
HASH_ALGORITHM = "sha512"
HASH_HEX_LENGTH = 128
ROOT = Path(__file__).resolve().parents[2]
RULE_SOURCES = (
    "sources/parts/01_qam_mml_mma_pre_v4_infrastructure/02_store_array_and_pre_v4_readouts.tex",
    "sources/parts/01_qam_mml_mma_pre_v4_infrastructure/03_two_sided_tensor_masks_and_freeze.tex",
    "sources/parts/01_qam_mml_mma_pre_v4_infrastructure/05_qam_tensor_admissibility_translation.tex",
)
PREDICATE_SOURCE = "sources/parts/01_qam_mml_mma_pre_v4_infrastructure/04_qam_predicates_transport_shell.tex"
RULE_CATALOG = Path(__file__).with_name("rule_catalog.json")
ROLES = {
    "front": {"readout", "frame", "observer", "language", "address"},
    "back": {"structure", "action", "field", "transport", "operator"},
}
PRIMITIVE_PAIRS = {"state", "layer", "operator", "readout", "branch", "shell"}
KINDS = PRIMITIVE_PAIRS | {"witness", "tensor", "comparison", "selector"}


class InputError(ValueError):
    """Malformed or unsupported explicit role data."""


def canonical(value: Any) -> str:
    """Deterministic representation equality, not mathematical equivalence."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False)


def digest(value: Any) -> str:
    return digest_bytes(canonical(value).encode("utf-8"))


def digest_bytes(value: bytes) -> str:
    return hashlib.sha512(value).hexdigest()


def source_fingerprints(paths: tuple[str, ...] = RULE_SOURCES) -> tuple[dict, dict]:
    """Bind local source bytes or an explicitly identified standalone rule catalog."""
    present = [(ROOT / path).is_file() for path in paths]
    if all(present):
        return ({path: digest_bytes((ROOT / path).read_bytes()) for path in paths},
                {"mode": "repository_source_files", "source_text_available": True})
    if any(present):
        raise InputError("Incomplete source checkout; cannot silently substitute the rule catalog")
    catalog = load_json(RULE_CATALOG)
    _keys(catalog, {"schema", "publications", "rules"})
    if catalog["schema"] != "qsc-rule-catalog/1" or not isinstance(catalog["rules"], dict):
        raise InputError("Invalid standalone rule catalog")
    _strings(catalog["publications"])
    hashes = {}
    for path in paths:
        if path not in catalog["rules"]:
            raise InputError("Rule catalog is missing a required rule group")
        entry = catalog["rules"][path]
        _keys(entry, {"definitions", "scope"})
        _strings(entry["definitions"])
        _text(entry["scope"])
        hashes[path] = digest({"publications": catalog["publications"], "rule_group": entry})
    return hashes, {"mode": "bundled_rule_catalog", "source_text_available": False,
                    "catalog_hash": digest_bytes(RULE_CATALOG.read_bytes())}


def _keys(value: Any, required: set[str], optional: set[str] | None = None) -> None:
    if not isinstance(value, dict) or not required <= value.keys():
        raise InputError(f"Expected object with fields {sorted(required)}")
    if value.keys() - required - (optional or set()):
        raise InputError(f"Unknown fields: {sorted(value.keys() - required - (optional or set()))}")


def _text(value: Any) -> None:
    if not isinstance(value, str) or not value.strip():
        raise InputError("Expected nonempty text")


def _strings(value: Any) -> None:
    if not isinstance(value, list):
        raise InputError("Expected a list of unique names")
    for item in value:
        _text(item)
    if len(value) != len(set(value)):
        raise InputError("Duplicate name")


def _mask(value: Any, universe: list[str]) -> int:
    if type(value) is not int or not 0 <= value < (1 << len(universe)):
        raise InputError("Mask must be an integer inside its declared finite universe")
    return value


def validate_document(document: Any) -> None:
    _keys(document, {"schema", "spaces", "objects", "guards", "mask_universes", "operations"}, {"metadata"})
    if document["schema"] != VERSION:
        raise InputError(f"Expected schema {VERSION}")
    for field in ("spaces", "objects", "guards", "mask_universes"):
        if not isinstance(document[field], dict):
            raise InputError(f"{field} must be an object")
        for name in document[field]:
            _text(name)
    for space in document["spaces"].values():
        _keys(space, {"dimension"})
        if type(space["dimension"]) is not int or space["dimension"] <= 0:
            raise InputError("Space dimension must be a positive integer")
    for obj in document["objects"].values():
        _keys(obj, {"kind", "payload", "indices"})
        if obj["kind"] not in KINDS or not isinstance(obj["indices"], dict):
            raise InputError("Unknown object kind or invalid index map")
        for name, index in obj["indices"].items():
            _text(name)
            _keys(index, {"label", "side", "variance", "role", "space"})
            _text(index["label"])
            if index["side"] not in ROLES or index["role"] not in ROLES[index["side"]]:
                raise InputError("Index role does not belong to its declared side")
            if index["variance"] not in {"upper", "lower"}:
                raise InputError("Index variance must be upper or lower")
            if index["space"] not in document["spaces"]:
                raise InputError("Undeclared index space")
    for guard in document["guards"].values():
        _keys(guard, {"status", "evidence"})
        if guard["status"] is not None and type(guard["status"]) is not bool:
            raise InputError("Guard status must be true, false or null")
        if not isinstance(guard["evidence"], str):
            raise InputError("Guard evidence must be text")
        if guard["status"] is not None:
            _text(guard["evidence"])
    for universe in document["mask_universes"].values():
        _strings(universe)
    if not isinstance(document["operations"], list):
        raise InputError("operations must be a list")
    ids = []
    for op in document["operations"]:
        if not isinstance(op, dict) or not {"id", "type", "guards"} <= op.keys():
            raise InputError("Every operation needs id, type and guards")
        _text(op["id"])
        _text(op["type"])
        _strings(op["guards"])
        if any(name not in document["guards"] for name in op["guards"]):
            raise InputError("Operation names an undeclared guard")
        ids.append(op["id"])
    if len(ids) != len(set(ids)):
        raise InputError("Duplicate operation id")
    canonical(document)  # Reject nonfinite numbers and unsupported payloads.


def _object(document: dict, name: Any) -> dict:
    _text(name)
    if name not in document["objects"]:
        raise InputError(f"Unknown object {name}")
    return document["objects"][name]


def _index(document: dict, ref: Any) -> dict:
    _keys(ref, {"object", "index"})
    obj = _object(document, ref["object"])
    _text(ref["index"])
    if ref["index"] not in obj["indices"]:
        raise InputError("Unknown index slot")
    return obj["indices"][ref["index"]]


def _universe(document: dict, name: Any) -> list[str]:
    _text(name)
    if name not in document["mask_universes"]:
        raise InputError("Unknown mask universe")
    return document["mask_universes"][name]


def _check_operation(document: dict, op: dict) -> tuple[dict, list[str], list[str]]:
    common = {"id", "type", "guards"}
    errors: list[str] = []
    pending: list[str] = []
    kind = op["type"]
    if kind in {"contract", "compare"}:
        fields = {"left", "right"} | ({"comparison", "comparison_slots"} if kind == "compare" else set())
        _keys(op, common | fields)
        left, right = _index(document, op["left"]), _index(document, op["right"])
        if op["left"] == op["right"]:
            errors.append("An index slot cannot be paired with itself")
        if kind == "contract":
            if left["variance"] == right["variance"]:
                errors.append("Raw same-variance contraction is forbidden; declare a comparison")
            if left["space"] != right["space"] or left["label"] != right["label"]:
                errors.append("Contracted indices must have the same space and dummy label")
        else:
            comparison = _object(document, op["comparison"])
            _strings(op["comparison_slots"])
            if len(op["comparison_slots"]) != 2:
                raise InputError("A binary comparison needs exactly two declared comparison slots")
            if comparison["kind"] != "comparison":
                errors.append("Pairing requires a declared comparison object")
            if left["variance"] != right["variance"]:
                errors.append("This comparison operation expects a same-variance pair")
            for operand, slot in zip((left, right), op["comparison_slots"]):
                comp = _index(document, {"object": op["comparison"], "index": slot})
                if comp["variance"] == operand["variance"]:
                    errors.append("Comparison slot needs the opposite variance")
                if comp["space"] != operand["space"] or comp["label"] != operand["label"]:
                    errors.append("Comparison slots must match operand spaces and labels")
        result = {"role_expansion": {"left": left, "right": right}, "operation": kind}
        if kind == "compare":
            result["comparison"] = comparison
    elif kind == "tensor_product":
        _keys(op, common | {"left", "right"})
        left, right = _object(document, op["left"]), _object(document, op["right"])
        if left["kind"] != right["kind"] or left["kind"] not in PRIMITIVE_PAIRS:
            errors.append("Primitive tensor formation requires an admitted same-kind pair")
        if not op["guards"]:
            pending.append("Tensor admissibility requires a separate structural declaration")
        result = {"components": [op["left"], op["right"]], "kind": left["kind"],
                  "admissibility": "declared_guards_only"}
    elif kind == "mask":
        _keys(op, common | {"universe", "operator", "left"}, {"right"})
        universe = _universe(document, op["universe"])
        left = _mask(op["left"], universe)
        full = (1 << len(universe)) - 1
        if op["operator"] == "complement":
            if "right" in op:
                raise InputError("Complement has one operand")
            value = full ^ left
        else:
            if "right" not in op:
                raise InputError("Binary mask operation needs right")
            right = _mask(op["right"], universe)
            if op["operator"] == "union":
                value = left | right
            elif op["operator"] == "intersection":
                value = left & right
            elif op["operator"] == "xor":
                value = left ^ right
            else:
                raise InputError("Unknown mask operator")
        result = {"universe": op["universe"], "bits": {name: 1 << i for i, name in enumerate(universe)},
                  "value": value, "active_kinds": [name for i, name in enumerate(universe) if value & (1 << i)]}
    elif kind == "mixed_readout":
        _keys(op, common | {"universe", "mask", "components", "aggregation"})
        universe = _universe(document, op["universe"])
        mask = _mask(op["mask"], universe)
        _text(op["aggregation"])
        if not isinstance(op["components"], list) or not op["components"]:
            raise InputError("Mixed readout needs declared components")
        selected, component_ids, available_kinds = [], [], set()
        for component in op["components"]:
            _keys(component, {"object", "readout_kind"})
            obj = _object(document, component["object"])
            if obj["kind"] != "readout":
                errors.append("Mixed-readout components must be readouts")
            if component["readout_kind"] not in universe:
                raise InputError("Component readout kind is outside the mask universe")
            component_ids.append(component["object"])
            available_kinds.add(component["readout_kind"])
            if mask & (1 << universe.index(component["readout_kind"])):
                selected.append({"object": component["object"], "payload_hash": digest(obj["payload"])})
        if len(component_ids) != len(set(component_ids)):
            raise InputError("Duplicate mixed-readout component")
        if any(mask & (1 << i) and name not in available_kinds for i, name in enumerate(universe)):
            errors.append("Mask activates a kind absent from the declared component menu")
        if not op["guards"]:
            pending.append("Mixed-readout compatibility needs a separate guard declaration")
        result = {"selected_components": selected, "aggregation": op["aggregation"],
                  "aggregation_evaluated": False, "payloads_modified": False}
    else:
        raise InputError(f"Unsupported operation type {kind}")
    return result, errors, pending


def check_document(document: Any, rule_sources: dict[str, str] | None = None) -> dict:
    validate_document(document)
    if rule_sources is None:
        sources, source_binding = source_fingerprints()
    else:
        sources, source_binding = rule_sources, {"mode": "caller_supplied_fingerprints", "source_text_available": False}
    context = {"schema": VERSION, "hash_algorithm": HASH_ALGORITHM,
               "input_hash": digest(document), "rule_sources": sources, "source_binding": source_binding,
               "implementation_hash": digest_bytes(Path(__file__).read_bytes())}
    previous = digest(context)
    receipts = []
    for op in document["operations"]:
        try:
            result, errors, pending = _check_operation(document, op)
        except (InputError, TypeError, KeyError) as exc:
            result, errors, pending = {}, [str(exc)], []
        guards = {name: document["guards"][name] for name in op["guards"]}
        for name, guard in guards.items():
            if guard["status"] is False:
                errors.append(f"Declared guard failed: {name}")
            elif guard["status"] is None:
                pending.append(f"Declared guard unresolved: {name}")
        status = "rejected" if errors else "unresolved" if pending else "accepted"
        body = {"operation_id": op["id"], "operation_hash": digest(op), "status": status,
                "errors": errors, "pending": pending, "declared_guards": guards,
                "result": result, "previous_hash": previous}
        previous = digest(body)
        receipts.append(dict(body, receipt_hash=previous))
    counts = {status: sum(r["status"] == status for r in receipts)
              for status in ("accepted", "rejected", "unresolved")}
    report = dict(context, scope="explicit_role_grammar_and_declared_guards_only",
                  mathematical_admissibility_proved=False, closure_proved=False,
                  counts=counts, receipts=receipts, final_chain_hash=previous)
    return dict(report, report_hash=digest(report))


def verify_report(document: dict, report: dict) -> bool:
    """Recompute the entire report, including current source and implementation hashes."""
    return canonical(report) == canonical(check_document(document))


def _unique_object(pairs: list[tuple[str, Any]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise InputError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    def reject_constant(value: str) -> None:
        raise InputError(f"Nonfinite JSON constant: {value}")
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object,
                      parse_constant=reject_constant)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Explicit QAM role-data JSON")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path, help="Write a reproducible JSON report")
    group.add_argument("--verify", type=Path, help="Recompute and compare a saved report")
    args = parser.parse_args()
    try:
        document = load_json(args.input)
        if args.verify:
            matched = verify_report(document, load_json(args.verify))
            print("Report matches recomputation" if matched else "Report differs from recomputation")
            return 0 if matched else 1
        report = check_document(document)
        rendered = json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
        if args.output:
            if args.output.resolve() == args.input.resolve():
                raise InputError("Output must not overwrite the input")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8")
            print(json.dumps(report["counts"], sort_keys=True))
        else:
            print(rendered, end="")
        return 1 if report["counts"]["rejected"] or report["counts"]["unresolved"] else 0
    except (ValueError, TypeError, KeyError, OSError) as exc:
        print(f"Input/report error: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
