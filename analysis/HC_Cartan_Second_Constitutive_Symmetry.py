"""Bounded principal symmetric-psi3 compatibility of second constitutive jets.

Neutral odd-cross Cartan comparison only; no coupled completion or propagation.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "second_constitutive_first", Path(__file__).with_name("HC_Cartan_Constitutive_First_Closure.py"))
first = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(first)
neighborhood, regular = first.neighborhood, first.regular
prior, prolong, spatial = first.prior, first.prolong, first.spatial
PAIRS, TRIPLES = prior.PAIR2, prolong.PAIR3
PAIR_WEIGHTS = np.array([1 if r == s else 2 for r, s in PAIRS])


def _finite(value, shape):
    value = np.asarray(value)
    if value.shape != shape or np.iscomplexobj(value) or not np.all(np.isfinite(value)):
        raise ValueError(f"Expected finite real array of shape {shape}")
    return value.astype(float)


def groups():
    """Rows (unique derivative pair, one-form index) sharing a triple."""
    return [tuple((p, mu) for p, (r, s) in enumerate(PAIRS) for mu in range(4)
                  if tuple(sorted((r, s, mu))) == triple) for triple in TRIPLES]


def pack_second(tensor):
    """C2[r,s,a,mu] -> 160 real coordinates, pair then a then mu."""
    tensor = _finite(tensor, (4, 4, 4, 4))
    if not np.allclose(tensor, tensor.swapaxes(0, 1), rtol=0, atol=1e-10):
        raise ValueError("C2 must be symmetric in its first two derivative indices")
    return np.array([tensor[p] for p in PAIRS]).reshape(160)


def unpack_second(values):
    values = _finite(values, (160,)).reshape(10, 4, 4)
    tensor = np.empty((4, 4, 4, 4))
    for (r, s), value in zip(PAIRS, values):
        tensor[r, s] = tensor[s, r] = value
    return tensor


def principal_image(principal, coordinates):
    """Apply L per symmetric triple, using regular.unpack's global Re/Im order."""
    principal = _finite(principal, (4, 24))
    coordinates = _finite(coordinates, (480,))
    values = prior.complexify(coordinates, (20, 3, 4))
    readouts = np.array([principal @ prior.realify(v) for v in values])
    image = np.zeros((10, 4, 4))
    for value, rows in zip(readouts, groups()):
        for p, mu in rows:
            image[p, :, mu] = value
    return image.reshape(160)


def principal_matrix(principal):
    """The bounded 160 x 480 map; no regular equation-system assembly."""
    return np.column_stack([principal_image(principal, v) for v in np.eye(480)])


def project(source, metric="full"):
    """Return image, defect and 20 frame readouts in unique-pair coordinates.

    Full Frobenius norm weights off-diagonal derivative pairs twice. 'unique'
    instead uses the Euclidean norm of the stored 160-vector.
    """
    source = _finite(source, (160,)).reshape(10, 4, 4)
    if metric not in ("full", "unique"):
        raise ValueError("metric must be 'full' or 'unique'")
    weights = PAIR_WEIGHTS if metric == "full" else np.ones(10)
    image = np.zeros_like(source)
    means = []
    for rows in groups():
        mean = sum(weights[p]*source[p, :, mu] for p, mu in rows)/sum(weights[p] for p, _ in rows)
        means.append(mean)
        for p, mu in rows:
            image[p, :, mu] = mean
    return image.reshape(160), (source-image).reshape(160), np.array(means)


def compatibility(source):
    """80 independent equalities; zero iff full three-index symmetry holds."""
    source = _finite(source, (160,)).reshape(10, 4, 4)
    return np.concatenate([source[p, :, mu]-source[rows[0][0], :, rows[0][1]]
                           for rows in groups() for p, mu in rows[1:]])


def minimum_norm_lift(principal, source):
    """Lift the full-Frobenius projection, independently for each triple."""
    principal = _finite(principal, (4, 24))
    if np.linalg.matrix_rank(principal, tol=1e-10) != 4:
        raise ValueError("A surjective 4 x 24 principal readout is required")
    _, _, means = project(source)
    inverse = np.linalg.pinv(principal, rcond=1e-10)
    return prior.realify(np.array([prior.complexify(inverse @ v, (3, 4)) for v in means]))


def input_fingerprints():
    result = first.input_fingerprints()
    for module in (regular, prior, prolong, spatial, spatial.rank_model,
                   prior.cartan, prior.odd, prior.dirac, prior.checks,
                   prior.odd.readouts, prior.odd.background):
        path = Path(module.__file__)
        result[path.name] = None
    result[Path(__file__).name] = None
    # Normalize every pinned text input, including inherited JSON/Markdown pins.
    for name in result:
        path = Path(__file__).with_name(name)
        result[name] = hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def direct_checks(prepared, point, jets, principal):
    """Check actual equations at signed random and sparse psi3 increments."""
    base = regular.equations(prepared, point, jets)
    base_c2 = pack_second(base["constraint_second"])
    rng = np.random.default_rng(73203)
    direction = rng.normal(size=480)
    rows = []
    for vector in (direction, -.25*direction, np.eye(480)[0], np.eye(480)[240]):
        changed = dict(jets, p3=jets["p3"]+prolong.unpack_third(vector, True))
        actual = regular.equations(prepared, point, changed)
        rows.append({
            "principal_error": float(np.linalg.norm(pack_second(actual["constraint_second"])-base_c2
                                                    -principal_image(principal, vector))),
            "connection_second_error": float(np.linalg.norm(actual["connection"]["second"]
                                                            -base["connection"]["second"])),
            "other_equations_error": float(np.linalg.norm(np.r_[
                (actual["constraint_first"]-base["constraint_first"]).reshape(-1),
                prior.realify(actual["probe_first"]-base["probe_first"]),
                (actual["coframe_Euler_first"]-base["coframe_Euler_first"]).reshape(-1)]))})
    correction = minimum_norm_lift(principal, -base_c2)
    changed = dict(jets, p3=jets["p3"]+prolong.unpack_third(correction, True))
    corrected = pack_second(regular.equations(prepared, point, changed)["constraint_second"])
    _, defect, _ = project(base_c2)
    return rows, {"starting_C2_full_norm": float(np.linalg.norm(unpack_second(base_c2))),
                  "compatibility_norm": float(np.linalg.norm(compatibility(base_c2))),
                  "uncancellable_full_norm": float(np.linalg.norm(unpack_second(defect))),
                  "projected_cancellation_error": float(np.linalg.norm(corrected-defect)),
                  "remaining_full_norm": float(np.linalg.norm(unpack_second(corrected)))}


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, _, _ = neighborhood.load_data()
    principal = spatial.constraint_principal_map(prepared["data"]["psi"])
    matrix = principal_matrix(principal)
    projector = np.column_stack([project(v)[0] for v in np.eye(160)])
    weights = np.repeat(PAIR_WEIGHTS, 16)
    singular = np.linalg.svd(matrix, compute_uv=False)
    direct, starting = direct_checks(prepared, point, jets, principal)
    # One row breaks (0,0,1) symmetry; its full metric residual cannot be lifted.
    negative = np.zeros((10, 4, 4))
    negative[PAIRS.index((0, 0)), 0, 1] = 1
    negative = negative.reshape(160)
    image, defect, _ = project(negative)
    lift = minimum_norm_lift(principal, negative)
    base_c2 = pack_second(regular.equations(prepared, point, jets)["constraint_second"])
    negative_jets = dict(jets, p3=jets["p3"]+prolong.unpack_third(lift, True))
    negative_actual = pack_second(regular.equations(prepared, point, negative_jets)["constraint_second"])
    negative_residual = negative_actual-base_c2-negative
    if fingerprints != input_fingerprints():
        raise RuntimeError("Second constitutive inputs changed during evaluation")
    return {"scope": "Principal symmetric-psi3 C2 compatibility at fixed E3/p2/l2; no propagation claim",
            "input_sha256": fingerprints, "starting_jet_loader": "HC_Cartan_Joint_Neighborhood.load_data",
            "coordinate_order": "C2: PAIR2,a,mu; psi3: global real then imaginary PAIR3,channel,spinor",
            "principal_shape": list(principal.shape), "principal_rank": int(np.linalg.matrix_rank(principal)),
            "map_shape": list(matrix.shape), "map_rank": int(np.sum(singular > 1e-9)),
            "kernel_dimension": 480-int(np.sum(singular > 1e-9)),
            "compatibility_dimension": 80, "singular_values": singular.tolist(),
            "principal": principal.tolist(), "pair_frobenius_weights": PAIR_WEIGHTS.tolist(),
            "projector_idempotence_error": float(np.linalg.norm(projector @ projector-projector)),
            "projector_weighted_adjoint_error": float(np.linalg.norm(weights[:, None]*projector
                                                        -projector.T*weights[None, :])),
            "projector_image_error": float(np.linalg.norm(projector @ matrix-matrix)),
            "direct_regular_equations_checks": direct, "starting_jet": starting,
            "negative_control": {"compatibility_norm": float(np.linalg.norm(compatibility(negative))),
                                 "uncancellable_full_norm": float(np.linalg.norm(unpack_second(defect))),
                                 "projected_lift_error": float(np.linalg.norm(principal_image(principal, lift)-image)),
                                 "direct_regular_residual_full_norm": float(np.linalg.norm(unpack_second(negative_residual))),
                                 "direct_regular_defect_error": float(np.linalg.norm(negative_residual+defect)),
                                 "full_target_lift_residual": float(np.linalg.norm(
                                     unpack_second(principal_image(principal, lift)-negative)))},
            "fixed_action_state_couplings": True, "enlarged_system_assembled_or_solved": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("map_shape", "map_rank", "starting_jet", "negative_control")}))


if __name__ == "__main__":
    main()
