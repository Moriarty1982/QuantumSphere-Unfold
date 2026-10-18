"""Bounded finite-difference R2 of a frozen Taylor truncation, not an extension test."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from types import ModuleType

import numpy as np


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "HC_Cartan_Next_Scalar_Compatibility", HERE / "HC_Cartan_Next_Scalar_Compatibility.py")
scalar = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scalar)
regular, spatial = scalar.regular, scalar.spatial
INITIAL_STEPS = (1e-3, 5e-4, 2.5e-4)
MAX_LEVELS = 9
CONVERGENCE_RTOL = 1e-9
CONVERGENCE_ATOL = 1e-6


def input_fingerprints():
    """Hash loaded local source dependencies; normalize Python line endings."""
    root = HERE.parent
    paths = {Path(__file__).resolve()}
    visited = set()

    def visit(module):
        if id(module) in visited:
            return
        visited.add(id(module))
        path = Path(getattr(module, "__file__", "") or ".").resolve()
        if not path.is_relative_to(root) or path.suffix != ".py":
            return
        paths.add(path)
        for value in vars(module).values():
            if isinstance(value, ModuleType):
                visit(value)

    visit(scalar)
    paths.update(HERE / name for name in (
        "HC_Cartan_Next_Scalar_Compatibility.json", "HC_Cartan_Spatial_Propagation.json",
        "HC_Cartan_Cauchy_Rank.json", "HC_Cartan_Prolongation.json",
        "HC_Cartan_Compatible_Jets.json"))
    result = {}
    for path in sorted(paths):
        data = path.read_bytes()
        if path.suffix == ".py":
            data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        result[path.relative_to(root).as_posix()] = hashlib.sha256(data).hexdigest()
    return result


def load_data():
    prepared, point, _ = regular.load_data()
    payload = json.loads((HERE / "HC_Cartan_Next_Scalar_Compatibility.json").read_text(encoding="utf-8"))
    coordinates = np.asarray(payload["joint_394_system"]["jet_coordinates"], dtype=float)
    return prepared, point, regular.unpack(coordinates), payload


def second_difference(function, step, dimension=4):
    """Full symmetric Hessian of a scalar or array, with central O(h^2) stencils."""
    if not np.isfinite(step) or step <= 0:
        raise ValueError("step must be positive and finite")
    axes = np.eye(dimension)
    origin = np.asarray(function(np.zeros(dimension)))
    result = np.empty((dimension, dimension) + origin.shape,
                      dtype=np.result_type(origin.dtype, float))
    for r in range(dimension):
        for s in range(r, dimension):
            a, b = axes[r], axes[s]
            if r == s:
                value = (function(step*a)-2*origin+function(-step*a))/step**2
            else:
                value = (function(step*(a+b))-function(step*(a-b))
                         -function(step*(-a+b))+function(-step*(a+b)))/(4*step**2)
            result[r, s] = result[s, r] = value
    return result


def richardson(coarse, fine):
    """Cancel the O(h^2) error when fine uses half the coarse step."""
    return (4*np.asarray(fine)-np.asarray(coarse))/3


def encode_complex(value):
    return {"real": value.real.tolist(), "imag": value.imag.tolist()}


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, source = load_data()
    completion = {"psi_second": jets["p2"], "multiplier_second": jets["l2"],
                  "coframe_third": jets["e3"], "psi_third": jets["p3"]}

    def probe(x):
        return spatial.taylor_fields(prepared, point, completion, x)["probe"]

    history, differences, extrapolations = [], [], []
    converged = False
    for level in range(MAX_LEVELS):
        step = INITIAL_STEPS[0]/2**level
        current = second_difference(probe, step)
        differences.append(current)
        entry = {"step": step, "R2": encode_complex(current),
                 "norm": float(np.linalg.norm(current))}
        if level:
            delta = float(np.linalg.norm(current-differences[-2]))
            extrapolated = richardson(differences[-2], current)
            extrapolations.append(extrapolated)
            entry.update({"successive_difference_norm": delta,
                          "Richardson_R2": encode_complex(extrapolated),
                          "Richardson_norm": float(np.linalg.norm(extrapolated))})
            if level >= 2:
                previous_delta = history[-1]["successive_difference_norm"]
                change = float(np.linalg.norm(extrapolations[-1]-extrapolations[-2]))
                scale = float(np.linalg.norm(extrapolated))
                entry.update({"successive_difference_ratio": previous_delta/delta if delta else None,
                              "Richardson_change_norm": change,
                              "Richardson_relative_change": change/max(scale, 1.),
                              "Richardson_change_over_15_error_indicator": change/15})
                converged = change <= CONVERGENCE_ATOL+CONVERGENCE_RTOL*scale
                if len(extrapolations) >= 3:
                    entry["Richardson_change_ratio"] = history[-1]["Richardson_change_norm"]/change if change else None
        history.append(entry)
        if level >= 2 and converged:
            break
    final = extrapolations[-1]
    pair_norms = np.linalg.norm(final, axis=-1)
    largest = np.unravel_index(np.argmax(abs(final)), final.shape)
    fields = spatial.taylor_fields(prepared, point, completion, np.zeros(4))
    scalar_hessian = scalar.scalar_jet(prepared, point, jets)["hessian"]
    if fingerprints != input_fingerprints():
        raise RuntimeError("Input changed during diagnostic; report not saved")
    return {
        "status": "frozen Taylor truncation diagnostic; finite differences are not proof",
        "input_sha256": fingerprints,
        "jet_source": "HC_Cartan_Next_Scalar_Compatibility.json:joint_394_system.jet_coordinates",
        "fixed_lower_point_loader": "HC_Cartan_Next_Scalar_Compatibility.regular.load_data",
        "fixed_lower_point_and_couplings": source["fixed_lower_point_and_couplings"],
        "frozen_jet_norms": {key: float(np.linalg.norm(value)) for key, value in jets.items()},
        "truncation": {"psi_degree": 3, "multiplier_degree": 2, "coframe_degree": 3,
                       "new_higher_derivatives": "zero; in particular lambda3=0; saved p3 and e3 retained",
                       "connection": "full algebraic Cartan solution at every displaced sample, not a polynomial omega"},
        "origin": {"probe_norm": float(np.linalg.norm(fields["probe"])),
                   "Cartan_norm": float(np.linalg.norm(fields["Cartan"])),
                   "scalar_hessian_norm": float(np.linalg.norm(scalar_hessian)),
                   "saved_all_394_norm": source["joint_394_system"]["residuals"]["all_394_norm"]},
        "method": {"initial_steps": list(INITIAL_STEPS), "max_levels": MAX_LEVELS,
                   "convergence_rtol": CONVERGENCE_RTOL, "convergence_atol": CONVERGENCE_ATOL,
                   "criterion": "successive Richardson tensor change <= atol + rtol * tensor norm",
                   "tensor_layout": "R2[r,s,k], r,s=0..3, complex flattened probe k=0..11",
                   "norm_convention": "Euclidean/Frobenius full symmetric tensor; mixed pairs counted twice",
                   "error_indicator": "Richardson change/15 assumes asymptotic fourth-order convergence; not a bound"},
        "history": history,
        "result": {"converged_by_change_criterion": bool(converged),
                   "finest_step": history[-1]["step"], "R2": encode_complex(final),
                   "full_symmetric_norm": float(np.linalg.norm(final)),
                   "max_abs_component": float(np.max(abs(final))),
                   "largest_component_index": [int(i) for i in largest],
                   "pair_norms": pair_norms.tolist()},
        "interpretation": [
            "The already solved scalar Hessian condition does not force full R2=0.",
            "R is first order in psi and multiplier and depends on omega, which uses first coframe derivatives. R2 therefore uses psi3, lambda3 and coframe3.",
            "Variations of p3, l3 and e3 can affect R2, but saved p3 and e3 are already fixed here. A p3/e3 variation would require rechecking the prior 394 conditions; l3 is a new freedom set to zero here.",
            "This frozen Taylor truncation is not an actual extension. No higher-jet extension system is solved, and no impossibility, propagation or local-existence conclusion follows.",
            "Finite-difference convergence is numerical evidence, not proof."],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = evaluate()
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"origin": report["origin"], "result": {
        key: value for key, value in report["result"].items() if key != "R2"},
        "convergence": [{key: value for key, value in entry.items()
                         if key not in ("R2", "Richardson_R2")} for entry in report["history"]]}, indent=2))


if __name__ == "__main__":
    main()
