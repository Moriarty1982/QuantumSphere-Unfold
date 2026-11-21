"""Deterministic A-port calibration check. Input errors are absolute complex radii."""

import argparse
import cmath
import json
import math
from pathlib import Path


STATE_SIGNS = {
    "blank_off": 1,
    "blank_on": -1,
    "marker_off": -1,
    "marker_on": 1,
}


def nonnegative(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite nonnegative number")
    if not math.isfinite(value) or value < 0:
        raise ValueError(f"{name} must be a finite nonnegative number")
    return float(value)


def phasor(value, name):
    if not isinstance(value, list) or len(value) != 2:
        raise ValueError(f"{name} must contain [real, imaginary]")
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) for v in value):
        raise ValueError(f"{name} must contain two finite numbers")
    if not all(math.isfinite(v) for v in value):
        raise ValueError(f"{name} must contain two finite numbers")
    return complex(*value)


def pair(value):
    return [value.real, value.imag]


def parse_load(load):
    return (
        phasor(load["x"], "x"),
        phasor(load["y"], "y"),
        nonnegative(load["x_error"], "x_error"),
        nonnegative(load["y_error"], "y_error"),
    )


def evaluate_state(state):
    loads = state["loads"]
    if not isinstance(loads, list) or len(loads) != 2:
        raise ValueError("exactly two fit loads are required")
    x1, y1, ex1, ey1 = parse_load(loads[0])
    x2, y2, ex2, ey2 = parse_load(loads[1])
    x3, y3, ex3, ey3 = parse_load(state["check_load"])
    reference = state["reference"]
    if not isinstance(reference["calibration_id"], str) or not reference["calibration_id"].strip():
        raise ValueError("reference.calibration_id is required")
    direct = phasor(reference["value"], "reference.value")
    direct_error = nonnegative(reference["error"], "reference.error")
    phase_error = nonnegative(state.get("extra_phase_error_rad", 0), "extra_phase_error_rad")
    delta = x2 - x1
    if abs(delta) <= ex1 + ex2:
        raise ValueError("the two fit loads are not separated by their error radii")

    # In the passive scalar model |r| <= 1, so x-error adds at most its own radius.
    fit_error1, fit_error2, check_error = ex1 + ey1, ex2 + ey2, ex3 + ey3
    weights = x2 / delta, -x1 / delta
    intercept = weights[0] * y1 + weights[1] * y2
    intercept_error = abs(weights[0]) * fit_error1 + abs(weights[1]) * fit_error2
    check_weights = (x2 - x3) / delta, (x3 - x1) / delta
    closure = abs(y3 - check_weights[0] * y1 - check_weights[1] * y2)
    closure_bound = check_error + abs(check_weights[0]) * fit_error1 + abs(check_weights[1]) * fit_error2
    slope = (y2 - y1) / delta
    slope_error = (fit_error1 + fit_error2) / abs(delta)

    discrepancy = abs(intercept - direct)
    radius = discrepancy + intercept_error + direct_error
    denominator_floor = abs(direct) - direct_error
    relative_radius = radius / denominator_floor if denominator_floor > 0 else None
    check_passed = closure <= closure_bound and abs(slope) <= 1 + slope_error

    # The disk is normalized by a lower bound on the true reference amplitude.
    # An independent unit-modulus reference error contributes only its phase.
    log_bound = None
    phase_bound = None
    central_log = None
    if relative_radius is not None and relative_radius < 1:
        log_bound = -math.log1p(-relative_radius) + phase_error
        phase_bound = math.asin(relative_radius) + phase_error
        central_log = cmath.log(intercept / direct)

    return {
        "calibration_id": reference["calibration_id"],
        "intercept": pair(intercept),
        "intercept_error": intercept_error,
        "minimum_load_separation": abs(delta) - ex1 - ex2,
        "affine_check_residual": closure,
        "affine_check_bound": closure_bound,
        "passive_slope": pair(slope),
        "passive_slope_error": slope_error,
        "affine_passive_model_consistent": check_passed,
        "reference_discrepancy": discrepancy,
        "relative_radius": relative_radius,
        "log_bound": log_bound,
        "phase_bound_rad": phase_bound,
        "central_log": central_log,
    }


def evaluate(data):
    kind = data["kind"]
    if kind not in ("synthetic", "measured"):
        raise ValueError("kind must be synthetic or measured")
    budget = nonnegative(data["log_budget"], "log_budget")
    raw_endpoints = data["endpoints"]
    if not isinstance(raw_endpoints, list) or len(raw_endpoints) != 2:
        raise ValueError("exactly two band endpoints are required")
    results = []
    for endpoint in raw_endpoints:
        f = nonnegative(endpoint["frequency_hz"], "frequency_hz")
        if f == 0:
            raise ValueError("frequency_hz must be strictly positive")
        states = endpoint["states"]
        if set(states) != set(STATE_SIGNS):
            raise ValueError(f"states must be {', '.join(STATE_SIGNS)}")
        states = {name: evaluate_state(states[name]) for name in STATE_SIGNS}
        consistent = all(s["affine_passive_model_consistent"] for s in states.values())
        bounded = all(s["log_bound"] is not None for s in states.values())
        log_bound = sum(s["log_bound"] for s in states.values()) if bounded else None
        phase_bound = sum(s["phase_bound_rad"] for s in states.values()) if bounded else None
        if not consistent:
            status = "model-inconsistent"
        elif bounded and log_bound <= budget:
            status = "within-budget"
        else:
            status = "uncertified"
        central_log = None
        if bounded:
            central_log = pair(sum(STATE_SIGNS[name] * s["central_log"] for name, s in states.items()))
        for row in states.values():
            del row["central_log"]
        results.append({
            "frequency_hz": f,
            "status": status,
            "log_cross_bound": log_bound,
            "phase_cross_bound_rad": phase_bound,
            "central_log_cross": central_log,
            "states": states,
        })
    low, high = sorted(results, key=lambda row: row["frequency_hz"])
    if low["frequency_hz"] == high["frequency_hz"]:
        raise ValueError("band endpoints must be distinct")
    return {
        "scope": "ordinary A ports",
        "kind": kind,
        "log_budget_per_endpoint": budget,
        "status": "within-budget" if all(row["status"] == "within-budget" for row in results) else "uncertified",
        "phase_difference_bound_rad": (
            low["phase_cross_bound_rad"] + high["phase_cross_bound_rad"]
            if all(row["status"] == "within-budget" for row in results)
            else None
        ),
        "endpoints": [low, high],
    }


def demo(case):
    endpoints = []
    for endpoint, frequency in enumerate((87_127_114_587_306, 87_127_214_587_306)):
        states = {}
        for i, name in enumerate(STATE_SIGNS):
            reference = cmath.rect(0.995, (endpoint + 1) * (i + 1) * 0.01)
            shift = 4e-8j
            curvature = 0
            if endpoint == 1 and name == "marker_on":
                if case == "affine":
                    shift += 7e-7j
                elif case == "curvature":
                    curvature = 1e-3

            def make_load(x):
                y = reference + shift + (0.05 + 0.02j) * x + curvature * x**2
                return {"x": pair(complex(x)), "y": pair(y), "x_error": 1e-8, "y_error": 1e-8}

            states[name] = {
                "loads": [make_load(-0.02), make_load(0.02)],
                "check_load": make_load(0),
                "reference": {
                    "calibration_id": f"synthetic-direct-{endpoint}-{name}",
                    "value": pair(reference),
                    "error": 3e-8,
                },
                "extra_phase_error_rad": 5e-9,
            }
        endpoints.append({"frequency_hz": frequency, "states": states})
    return {"kind": "synthetic", "log_budget": 5e-7, "endpoints": endpoints}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    data = parser.add_mutually_exclusive_group(required=True)
    data.add_argument("--input", type=Path, help="JSON input with two endpoints and four states each")
    data.add_argument("--demo", choices=("nominal", "affine", "curvature"))
    data.add_argument("--example-input", action="store_true", help="print the nominal synthetic JSON input")
    args = parser.parse_args()
    if args.example_input:
        print(json.dumps(demo("nominal"), indent=2))
        return 0
    try:
        inputs = demo(args.demo) if args.demo else json.loads(args.input.read_text(encoding="utf-8"))
        report = evaluate(inputs)
        output = json.dumps(report, indent=2, allow_nan=False)
    except (KeyError, TypeError, ValueError, OverflowError, OSError) as exc:
        parser.exit(2, f"Invalid input: {exc}\n")
    print(output)
    return 0 if report["status"] == "within-budget" else 1


if __name__ == "__main__":
    raise SystemExit(main())
