"""Evaluate an ordinary A-port measurement using its signed cross contrast."""

import argparse
import cmath
import json
import math
from pathlib import Path

import op5_a_port_check as core


def phase_transfer(endpoint):
    states = endpoint["states"]
    cell_sum = math.fsum(state.get("extra_phase_error_rad", 0) for state in states.values())
    if "phase_transfer_contrast" not in endpoint:
        return cell_sum, cell_sum, None
    contrast = endpoint["phase_transfer_contrast"]
    calibration_id = contrast["calibration_id"]
    if not isinstance(calibration_id, str) or not calibration_id.strip():
        raise ValueError("phase_transfer_contrast.calibration_id is required")
    if any("extra_phase_error_rad" not in state for state in states.values()):
        raise ValueError("phase_transfer_contrast requires explicit phase bounds in all four states")
    error = core.nonnegative(contrast["error_rad"], "phase_transfer_contrast.error_rad")
    return min(cell_sum, error), cell_sum, calibration_id


def evaluate(data):
    report = core.evaluate(data)
    budget = report["log_budget_per_endpoint"]
    endpoints = sorted(data["endpoints"], key=lambda row: row["frequency_hz"])
    for endpoint, result in zip(endpoints, report["endpoints"], strict=True):
        transfer, cell_transfer, calibration_id = phase_transfer(endpoint)
        result["legacy_log_cross_bound"] = result["log_cross_bound"]
        result["legacy_phase_cross_bound_rad"] = result["phase_cross_bound_rad"]
        result["phase_transfer_bound_rad"] = transfer
        result["cell_phase_transfer_sum_rad"] = cell_transfer
        result["phase_transfer_calibration_id"] = calibration_id
        result["centered_log_cross_bound"] = None
        result["centered_phase_cross_bound_rad"] = None

        if result["central_log_cross"] is None:
            continue

        central = complex(*result["central_log_cross"])
        cell_radii = []
        own_radii = []
        for name, fit in result["states"].items():
            reference = endpoint["states"][name]["reference"]
            cell_radii.append(fit["relative_radius"])
            own_radii.extend((
                fit["intercept_error"] / abs(complex(*fit["intercept"])),
                reference["error"] / abs(complex(*reference["value"])),
            ))

        # The existing near-one disks fix the lift of the signed cell logarithms.
        centered_log = abs(central) + math.fsum(-math.log1p(-r) for r in own_radii)
        centered_phase = abs(central.imag) + math.fsum(math.asin(r) for r in own_radii)
        cell_log = math.fsum(-math.log1p(-r) for r in cell_radii)
        cell_phase = math.fsum(math.asin(r) for r in cell_radii)
        result["centered_log_cross_bound"] = centered_log + transfer
        result["centered_phase_cross_bound_rad"] = centered_phase + transfer
        result["log_cross_bound"] = min(centered_log, cell_log) + transfer
        result["phase_cross_bound_rad"] = min(centered_phase, cell_phase) + transfer
        if result["status"] != "model-inconsistent":
            result["status"] = "within-budget" if result["log_cross_bound"] <= budget else "uncertified"

    qualified = all(row["status"] == "within-budget" for row in report["endpoints"])
    report["status"] = "within-budget" if qualified else "uncertified"
    report["phase_difference_bound_rad"] = (
        math.fsum(row["phase_cross_bound_rad"] for row in report["endpoints"])
        if qualified else None
    )
    return report


def demo(case):
    if case in ("nominal", "affine", "curvature"):
        return core.demo(case)
    inputs = core.demo("nominal")
    rotation = cmath.exp(4e-7j)
    for endpoint in inputs["endpoints"]:
        for state in endpoint["states"].values():
            for load in [*state["loads"], state["check_load"]]:
                load["y"] = core.pair(complex(*load["y"]) * rotation)
            if case in ("grouped", "cell-phase"):
                state["extra_phase_error_rad"] = 2e-7
        if case == "grouped":
            endpoint["phase_transfer_contrast"] = {
                "error_rad": 1e-8,
                "calibration_id": "synthetic-signed-phase-contrast",
            }
    return inputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--input", type=Path, help="JSON with two band endpoints")
    source.add_argument("--demo", choices=("nominal", "common", "cell-phase", "grouped", "affine", "curvature"))
    source.add_argument("--example-input", action="store_true", help="print synthetic grouped input")
    args = parser.parse_args()
    if args.example_input:
        print(json.dumps(demo("grouped"), indent=2))
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
