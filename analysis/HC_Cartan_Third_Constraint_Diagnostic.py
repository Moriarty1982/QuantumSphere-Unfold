"""Third constraint gate: exact spinor principal image, numerical frozen source.

This is the added neutral Cartan comparison, not a native-paper existence proof.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "third_constraint_scalar", Path(__file__).with_name("HC_Cartan_Next_Scalar_Compatibility.py"))
scalar = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scalar)
TRIPLES = tuple(itertools.combinations_with_replacement(range(4), 3))
QUADS = tuple(itertools.combinations_with_replacement(range(4), 4))


def load_data():
    prepared, point, _ = scalar.regular.load_data()
    path = Path(__file__).with_name("HC_Cartan_Next_Scalar_Compatibility.json")
    saved = json.loads(path.read_text(encoding="utf-8"))
    if saved["input_sha256"] != scalar.input_fingerprints():
        raise ValueError("Saved scalar completion has stale source inputs")
    jets = scalar.regular.unpack(np.asarray(saved["joint_394_system"]["jet_coordinates"]))
    return prepared, point, jets, hashlib.sha256(path.read_bytes()).hexdigest()


def groups():
    """Unique derivative-coordinate rows sharing one fully symmetric quartet."""
    result = []
    for quad in QUADS:
        rows = []
        for mu in sorted(set(quad)):
            triple = list(quad)
            triple.remove(mu)
            rows.append((TRIPLES.index(tuple(triple)), mu))
        result.append(rows)
    return result


def project(source):
    """Euclidean projection in unweighted unique-triple coordinates."""
    source = np.asarray(source, float)
    if source.shape != (20, 4, 4):
        raise ValueError("Expected third constraint shape (20, 4, 4)")
    image = np.zeros_like(source)
    means = []
    for rows in groups():
        mean = np.mean([source[t, :, mu] for t, mu in rows], axis=0)
        means.append(mean)
        for t, mu in rows:
            image[t, :, mu] = mean
    return image, source-image, np.asarray(means)


def compatibility(source):
    """180 independent equality conditions, without redundant curl rows."""
    return np.concatenate([source[t, :, mu]-source[rows[0][0], :, rows[0][1]]
                           for rows in groups() for t, mu in rows[1:]])


def principal_image(principal, fourth):
    principal, fourth = np.asarray(principal), np.asarray(fourth)
    if principal.shape != (4, 24) or fourth.shape != (35, 24):
        raise ValueError("Expected principal (4,24) and real fourth jet (35,24)")
    result = np.zeros((20, 4, 4))
    for q, rows in enumerate(groups()):
        for t, mu in rows:
            result[t, :, mu] = principal @ fourth[q]
    return result


def spinor_only_completion(source, principal):
    if np.linalg.matrix_rank(principal, tol=1e-10) != 4:
        raise ValueError("Surjective spinor pairing required")
    _, _, means = project(source)
    fourth = -means @ np.linalg.pinv(principal, rcond=1e-10).T
    return fourth, source+principal_image(principal, fourth)


def connection_image(prepared, fourth_coframe, third_multiplier):
    """Highest E4/lambda3 part only; all lower jets and psi4 are fixed."""
    e4, l3 = np.asarray(fourth_coframe), np.asarray(third_multiplier)
    if e4.shape != (35, 4, 4) or l3.shape != (20, 4, 4):
        raise ValueError("Expected E4 (35,4,4), lambda3 (20,4,4)")
    first = np.array([[e4[QUADS.index(tuple(sorted(triple+(r,))))]
                       for r in range(4)] for triple in TRIPLES])
    omega = (first.reshape(20, 64) @ scalar.regular.LC_LINEAR).reshape(20, 4, 4, 4)
    response = prepared["response"]
    k3 = (l3.reshape(20, 16) @ response) @ prepared["inverse_hessian"].T
    omega += np.einsum("tp,pmab->tmab", k3, scalar.cartan.OMEGA_BASIS)
    psi = prepared["data"]["psi"]
    covariant = np.einsum("tmij,rj->tmri", scalar.prolong.spin_lift(omega), psi)
    return np.array([scalar.odd.readouts.pairing(psi, d, scalar.Q).imag for d in covariant])


def connection_completion(prepared, source, principal):
    columns = []
    for i in range(880):
        basis = np.zeros(880)
        basis[i] = 1
        image = connection_image(prepared, basis[:560].reshape(35, 4, 4),
                                 basis[560:].reshape(20, 4, 4))
        columns.append(image.reshape(-1))
    full = np.column_stack(columns)
    quotient = np.column_stack([project(c.reshape(20, 4, 4))[1].reshape(-1) for c in full.T])
    rhs = -project(source)[1].reshape(-1)
    solution, _, rank, singular = np.linalg.lstsq(quotient, rhs, rcond=1e-10)
    remainder = source+(full @ solution).reshape(20, 4, 4)
    p4, residual = spinor_only_completion(remainder, principal)
    return {"quotient_rank": int(rank), "singular_values": singular.tolist(),
            "coframe_only_quotient_rank": int(np.linalg.matrix_rank(quotient[:, :560], tol=1e-10)),
            "multiplier_only_quotient_rank": int(np.linalg.matrix_rank(quotient[:, 560:], tol=1e-10)),
            "connection_coordinates": solution.tolist(), "fourth_spinor_real": p4.tolist(),
            "full_constraint_residual_norm": float(np.linalg.norm(residual)),
            "residual": residual.tolist(),
            "scope": "C3 only: these higher jets have NOT been checked against FE2 or R2"}


def third_difference(field, step):
    if not np.isfinite(step) or step <= 0:
        raise ValueError("Positive finite step required")
    cache = {}
    result = []
    for triple in TRIPLES:
        value = None
        for signs in itertools.product((-1, 1), repeat=3):
            offset = np.zeros(4, dtype=int)
            for axis, sign in zip(triple, signs):
                offset[axis] += sign
            key = tuple(offset)
            if key not in cache:
                cache[key] = np.asarray(field(step*offset), float)
            term = np.prod(signs)*cache[key]
            value = term.copy() if value is None else value+term
        result.append(value/(8*step**3))
    return np.asarray(result)


def homogeneous_jet(values, order, x, derivative=()):
    """Taylor contribution from unique symmetric derivative coordinates."""
    result = np.zeros(np.asarray(values).shape[1:], dtype=np.asarray(values).dtype)
    for indices, value in zip(itertools.combinations_with_replacement(range(4), order), values):
        counts = [indices.count(i)-derivative.count(i) for i in range(4)]
        if min(counts) < 0:
            continue
        factor = math.prod(x[i]**n/math.factorial(n) for i, n in enumerate(counts))
        result += factor*value
    return result


def extended_constraint(prepared, point, jets, x, e4, l3, p4):
    completion = {"psi_second": jets["p2"], "multiplier_second": jets["l2"],
                  "coframe_third": jets["e3"], "psi_third": jets["p3"]}
    base = scalar.spatial.taylor_fields(prepared, point, completion, x)
    e = base["coframe"]+homogeneous_jet(e4, 4, x)
    de = base["coframe_first"]+np.array([homogeneous_jet(e4, 4, x, (r,)) for r in range(4)])
    dde = base["coframe_second"]+np.array([[homogeneous_jet(e4, 4, x, (r, s))
                                            for s in range(4)] for r in range(4)])
    psi = base["psi"]+homogeneous_jet(p4, 4, x)
    dp = base["psi_first"]+np.array([homogeneous_jet(p4, 4, x, (r,)) for r in range(4)])
    lam = base["multiplier"]+homogeneous_jet(l3, 3, x)
    bundle = scalar.prolong.dirac.bundle(e, de, dde)
    hessian, response, source = scalar.prolong.fast_cartan_data(prepared, e, psi)
    k = np.linalg.solve(hessian, -source+response.T @ lam.reshape(-1))
    omega = bundle["omega"]+scalar.cartan.unpack(k)
    return scalar.odd.channels(psi, scalar.cartan.covariant_jet(psi, dp, omega))["odd"]-e


def independent_response_check(prepared, point, jets, principal):
    rng = np.random.default_rng(37291)
    e4, l3, p4real = rng.normal(size=(35, 4, 4)), rng.normal(size=(20, 4, 4)), rng.normal(size=(35, 24))
    p4 = np.array([scalar.prior.complexify(v, (3, 4)) for v in p4real])
    analytic = connection_image(prepared, e4, l3)+principal_image(principal, p4real)
    zeros = (np.zeros_like(e4), np.zeros_like(l3), np.zeros_like(p4))
    def delta(x):
        return (extended_constraint(prepared, point, jets, x, e4, l3, p4)
                -extended_constraint(prepared, point, jets, x, *zeros))
    coarse, fine = third_difference(delta, 1e-3), third_difference(delta, 5e-4)
    richardson = (4*fine-coarse)/3
    return {"analytic_norm": float(np.linalg.norm(analytic)),
            "coarse_error_norm": float(np.linalg.norm(coarse-analytic)),
            "fine_error_norm": float(np.linalg.norm(fine-analytic)),
            "richardson_error_norm": float(np.linalg.norm(richardson-analytic))}


def evaluate():
    prepared, point, jets, fingerprint = load_data()
    completion = {"psi_second": jets["p2"], "multiplier_second": jets["l2"],
                  "coframe_third": jets["e3"], "psi_third": jets["p3"]}
    def field(x):
        return scalar.spatial.taylor_fields(prepared, point, completion, x)["constraint"]
    steps = (1e-3, 5e-4, 2.5e-4)
    raw = [third_difference(field, h) for h in steps]
    estimates = [(4*raw[i+1]-raw[i])/3 for i in range(2)]
    source = estimates[-1]
    principal = scalar.spatial.constraint_principal_map(prepared["data"]["psi"])
    fourth, residual = spinor_only_completion(source, principal)
    joint = connection_completion(prepared, source, principal)
    projected, obstruction, _ = project(source)
    error = np.linalg.norm(estimates[1]-estimates[0])
    projected_error = np.linalg.norm(project(estimates[1]-estimates[0])[1])
    return {
        "scope": "Source has E4=lambda3=psi4=0; then fit all three new jets for C3 only. No R2/FE2 joint solution claimed.",
        "source_json_sha256": fingerprint,
        "coordinate_convention": "Unique sorted derivative triples, unweighted Euclidean component norm",
        "principal_rank": int(np.linalg.matrix_rank(principal, tol=1e-10)),
        "dimensions": {"fourth_spinor_real": 840, "constraint_third": 320,
                       "principal_image_rank": 140, "independent_compatibility": 180,
                       "spinor_principal_kernel": 700},
        "steps": list(steps),
        "raw_successive_differences": [float(np.linalg.norm(raw[i+1]-raw[i])) for i in range(2)],
        "richardson_difference_norm_not_certified_error_bound": float(error),
        "projected_richardson_difference_norm": float(projected_error),
        "frozen_source_norm": float(np.linalg.norm(source)),
        "removable_symmetric_part_norm": float(np.linalg.norm(projected)),
        "spinor_only_minimum_residual_norm": float(np.linalg.norm(residual)),
        "compatibility_norm": float(np.linalg.norm(compatibility(source))),
        "orthogonal_obstruction_norm": float(np.linalg.norm(obstruction)),
        "completion_equals_projection_error": float(np.linalg.norm(residual-obstruction)),
        "new_connection_jet_completion": joint,
        "independent_highest_jet_response_check": independent_response_check(prepared, point, jets, principal),
        "frozen_source": source.tolist(), "fourth_spinor_real": fourth.tolist(),
        "unresolved": ["E4 and lambda3 may change compatibility source",
                       "Joint R2, FE2, C3 compatibility remains open",
                       "Finite differences are not interval bounds or an existence proof",
                       "Native model and physical coupling identification remain open"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(evaluate(), indent=2)+"\n"
    if args.output:
        args.output.write_text(result, encoding="utf-8")
    else:
        print(result)


if __name__ == "__main__":
    main()
