"""Concept-level QAM/MML/MMA interface with a fixed tensor-role audit adapter."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from typing import Any

try:
    from . import tensor_grammar_check as tensor
except ImportError:  # Direct script invocation.
    import tensor_grammar_check as tensor

VERSION = "qsc-framework-interface/2"
PREDICATES = {
    "QClEq": {"source": {"state", "tensor"}, "target": {"state", "tensor"}},
    "QAdmTransport": {"operator": {"operator", "tensor"}, "source": {"state", "tensor"}, "target": {"state", "tensor"}},
    "QRead": {"readout": {"readout", "tensor"}, "source": {"state", "tensor"}, "witness": {"witness"}},
    "QBranchRef": {"branch": {"branch"}, "source": {"state", "tensor"}, "target": {"state", "tensor"}},
    "QShellRef": {"shell": {"shell"}, "source": {"state", "tensor"}, "target": {"state", "tensor"}},
    "QTensorAdm": {"left": tensor.PRIMITIVE_PAIRS, "right": tensor.PRIMITIVE_PAIRS},
}


def _guard_names(qam: dict, names: Any) -> None:
    tensor._strings(names)
    if any(name not in qam["guards"] for name in names):
        raise tensor.InputError("Undeclared framework guard")


def _role_document(qam: dict, operations: list) -> dict:
    return {"schema": tensor.VERSION, "spaces": qam["spaces"],
            "objects": {name: {field: obj[field] for field in ("kind", "payload", "indices")}
                        for name, obj in qam["objects"].items()},
            "guards": qam["guards"], "mask_universes": qam["mask_universes"],
            "operations": operations}


def validate_context(context: Any) -> None:
    tensor._keys(context, {"schema", "scope", "qam", "provenance"})
    if context["schema"] != VERSION:
        raise tensor.InputError(f"Expected {VERSION}")
    tensor._keys(context["scope"], {"regime", "description"})
    if context["scope"]["regime"] not in {"local", "bounded", "effective", "readout_dependent"}:
        raise tensor.InputError("Framework scope must retain a guarded regime")
    tensor._text(context["scope"]["description"])
    tensor._keys(context["provenance"], {"source", "parent_context_hash"})
    tensor._text(context["provenance"]["source"])
    parent = context["provenance"]["parent_context_hash"]
    if parent is not None and (not isinstance(parent, str) or not re.fullmatch(rf"[0-9a-f]{{{tensor.HASH_HEX_LENGTH}}}", parent)):
        raise tensor.InputError("Parent context hash must be null or a SHA-512 representation reference")
    qam = context["qam"]
    tensor._keys(qam, {"spaces", "objects", "guards", "active_guards", "mask_universes", "relations", "residuals"})
    if not isinstance(qam["objects"], dict):
        raise tensor.InputError("Framework objects must be a map")
    for obj in qam["objects"].values():
        tensor._keys(obj, {"kind", "payload", "indices", "guards", "source"})
        tensor._text(obj["source"])
    tensor.validate_document(_role_document(qam, []))
    if any(name.startswith("__interface__:") for name in qam["guards"]):
        raise tensor.InputError("Guard prefix __interface__: is reserved for adapter declarations")
    _guard_names(qam, qam["active_guards"])
    for obj in qam["objects"].values():
        _guard_names(qam, obj["guards"])
    if not isinstance(qam["relations"], dict) or not isinstance(qam["residuals"], dict):
        raise tensor.InputError("Relations and residuals must be maps")
    for name, relation in qam["relations"].items():
        tensor._text(name)
        tensor._keys(relation, {"predicate", "arguments", "status", "evidence", "guards"})
        if relation["predicate"] not in PREDICATES:
            raise tensor.InputError("Unsupported QAM predicate")
        expected = PREDICATES[relation["predicate"]]
        tensor._keys(relation["arguments"], set(expected))
        for argument, kinds in expected.items():
            name = relation["arguments"][argument]
            obj = tensor._object(_role_document(qam, []), name)
            if obj["kind"] not in kinds:
                raise tensor.InputError("QAM relation argument has an incompatible kind")
        if relation["predicate"] == "QTensorAdm":
            left = qam["objects"][relation["arguments"]["left"]]
            right = qam["objects"][relation["arguments"]["right"]]
            if left["kind"] != right["kind"]:
                raise tensor.InputError("Mixed primitive tensor admissibility is outside this interface")
        if relation["status"] is not None and type(relation["status"]) is not bool:
            raise tensor.InputError("Relation status must be true, false or null")
        if not isinstance(relation["evidence"], str):
            raise tensor.InputError("Relation evidence must be text")
        if relation["status"] is not None:
            tensor._text(relation["evidence"])
        _guard_names(qam, relation["guards"])
    for name, residual in qam["residuals"].items():
        tensor._text(name)
        tensor._keys(residual, {"witness", "status", "evidence"})
        obj = tensor._object(_role_document(qam, []), residual["witness"])
        if obj["kind"] != "witness" or residual["status"] not in {"open", "declared_zero"}:
            raise tensor.InputError("Residual needs a witness and an explicit diagnostic status")
        tensor._text(residual["evidence"])
    tensor.canonical(context)


def _operation_objects(op: dict) -> set[str]:
    """Enumerate object dependencies of the fixed adapter, without executing payloads."""
    names = set()
    for field in ("left", "right"):
        value = op.get(field)
        if isinstance(value, str):
            names.add(value)
        elif isinstance(value, dict) and isinstance(value.get("object"), str):
            names.add(value["object"])
    if isinstance(op.get("comparison"), str):
        names.add(op["comparison"])
    if isinstance(op.get("components"), list):
        for component in op["components"]:
            if isinstance(component, dict) and isinstance(component.get("object"), str):
                names.add(component["object"])
    return names


class FrameworkInterface:
    """Validated conceptual context; requests inspect or audit it, never mutate it."""

    def __init__(self, context: dict):
        validate_context(context)
        self._canonical_context = tensor.canonical(context)

    @property
    def context(self) -> dict:
        return json.loads(self._canonical_context)

    @property
    def context_hash(self) -> str:
        return tensor.digest(self.context)

    def execute(self, request: dict) -> dict:
        context = self.context
        qam = context["qam"]
        result: dict = {}
        errors: list[str] = []
        obligations: list[str] = []
        used_guards: set[str] = set()
        available_guards = dict(qam["guards"])
        tensor.canonical(request)
        try:
            tensor._keys(request, {"id", "instruction", "guards", "arguments"})
            tensor._text(request["id"])
            _guard_names(qam, request["guards"])
            used_guards.update(qam["active_guards"])
            used_guards.update(request["guards"])
            args = request["arguments"]
            if request["instruction"] == "EXPORT":
                tensor._keys(args, {"view"})
                if args["view"] != "framework":
                    raise tensor.InputError("EXPORT supports the framework concept view")
                result = {"framework": context, "payloads_evaluated": False}
            elif request["instruction"] == "SCRUB" and args.get("view") == "framework":
                tensor._keys(args, {"view"})
                for obj in qam["objects"].values():
                    used_guards.update(obj["guards"])
                for relation in qam["relations"].values():
                    used_guards.update(relation["guards"])
                result = {"objects_registered": len(qam["objects"]),
                          "relations_registered": len(qam["relations"]),
                          "relations": qam["relations"], "residuals": qam["residuals"],
                          "structural_truth_evaluated": False}
            elif request["instruction"] == "SCRUB" and args.get("view") == "tensor_roles":
                tensor._keys(args, {"view", "operations"})
                if not isinstance(args["operations"], list):
                    raise tensor.InputError("Tensor-role adapter needs an operation list")
                operations = json.loads(tensor.canonical(args["operations"]))
                request_guards = set(used_guards)
                for op in operations:
                    if not isinstance(op, dict) or "guards" not in op:
                        raise tensor.InputError("Every tensor operation needs declared guards")
                    _guard_names(qam, op["guards"])
                    explicit_guards = list(op["guards"])
                    inherited = set(request_guards)
                    for name in _operation_objects(op):
                        if name in qam["objects"]:
                            inherited.update(qam["objects"][name]["guards"])
                    relation_id = op.pop("admissibility_relation", None)
                    if relation_id is not None:
                        tensor._text(relation_id)
                        if op.get("type") != "tensor_product" or relation_id not in qam["relations"]:
                            raise tensor.InputError("Admissibility relation must name a QTensorAdm declaration for a tensor pair")
                        relation = qam["relations"][relation_id]
                        if relation["predicate"] != "QTensorAdm" or relation["arguments"] != {"left": op.get("left"), "right": op.get("right")}:
                            raise tensor.InputError("Admissibility relation does not match this tensor pair")
                        name = f"__interface__:relation:{relation_id}"
                        available_guards[name] = {"status": relation["status"], "evidence": relation["evidence"]}
                        inherited.update(relation["guards"])
                        inherited.add(name)
                    elif op.get("type") in {"tensor_product", "mixed_readout"} and not explicit_guards:
                        # A general object/request guard is not a tensor-admissibility declaration.
                        tensor._text(op.get("id"))
                        name = f"__interface__:missing_admissibility:{op['id']}"
                        available_guards[name] = {"status": None, "evidence": "No operation-specific admissibility/compatibility declaration supplied."}
                        inherited.add(name)
                    op["guards"] = sorted(set(op["guards"]) | inherited)
                    used_guards.update(op["guards"])
                role_document = _role_document(qam, operations)
                role_document["guards"] = available_guards
                report = tensor.check_document(role_document)
                result = {"adapter": "tensor_roles", "report": report, "residuals": qam["residuals"]}
                if any(any(not error.startswith("Declared guard failed:") for error in r["errors"]) for r in report["receipts"]):
                    errors.append("Tensor-role adapter rejected one or more operations")
                if report["counts"]["unresolved"]:
                    obligations.append("Tensor-role adapter has unresolved admissibility or guards")
            else:
                raise tensor.InputError("Unsupported instruction/view; no implicit execution")
        except (tensor.InputError, TypeError, KeyError, AttributeError) as exc:
            errors.append(str(exc))
        guard_records = {name: available_guards[name] for name in sorted(used_guards)}
        for name, guard in guard_records.items():
            if guard["status"] is not True:
                obligations.append(f"Framework guard {'failed' if guard['status'] is False else 'unresolved'}: {name}")
        source_hashes, source_binding = tensor.source_fingerprints((*tensor.RULE_SOURCES, tensor.PREDICATE_SOURCE))
        body = {"schema": VERSION, "hash_algorithm": tensor.HASH_ALGORITHM, "scope": context["scope"],
                "context_hash": self.context_hash, "request_hash": tensor.digest(request),
                "mma_status": "reject" if errors else "guard" if obligations else "continue",
                "errors": errors, "obligations": obligations, "declared_guards": guard_records,
                "result": result, "state_changed": False, "closure_proved": False,
                "mathematical_relations_proved": False,
                "implementation_hash": tensor.digest_bytes(Path(__file__).read_bytes()),
                "tensor_adapter_hash": tensor.digest_bytes(Path(tensor.__file__).read_bytes()),
                "source_hashes": source_hashes, "source_binding": source_binding}
        return dict(body, receipt_hash=tensor.digest(body))

    def verify(self, request: dict, receipt: dict) -> bool:
        return tensor.canonical(receipt) == tensor.canonical(self.execute(request))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("context", type=Path)
    parser.add_argument("request", type=Path)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path)
    group.add_argument("--verify", type=Path)
    args = parser.parse_args()
    try:
        interface = FrameworkInterface(tensor.load_json(args.context))
        request = tensor.load_json(args.request)
        if args.verify:
            matched = interface.verify(request, tensor.load_json(args.verify))
            print("Framework receipt matches recomputation" if matched else "Framework receipt differs")
            return 0 if matched else 1
        receipt = interface.execute(request)
        rendered = json.dumps(receipt, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
        if args.output:
            if args.output.resolve() in {args.context.resolve(), args.request.resolve()}:
                raise tensor.InputError("Output must not overwrite context or request")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8")
            print(receipt["mma_status"])
        else:
            print(rendered, end="")
        return 0 if receipt["mma_status"] == "continue" else 1
    except (ValueError, TypeError, KeyError, OSError) as exc:
        print(f"Framework input/report error: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
