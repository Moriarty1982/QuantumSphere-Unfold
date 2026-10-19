"""Attribute first-prolongation obstructions to prescribed jets and known identities.

Sampled finite-jet analysis only; changing higher data does not solve lower residuals.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


def local_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


previous = local_module("attribution_general_first", "HC_Cartan_General_First_Source_Gate.py")
ward = local_module("attribution_coordinate_ward", "HC_Cartan_Diffeomorphism_Residual_Identity.py")
general, split, source = previous.general, previous.split, previous.source


def input_fingerprints():
    result = previous.input_fingerprints()
    result.update(ward.input_fingerprints())
    result[Path(__file__).name] = hashlib.sha256(
        Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def known_rows(fields):
    curls = []
    for r in range(4):
        for s in range(r+1, 4):
            for a in range(4):
                row = np.zeros(272)
                row[68*r+4*a+s] = 1
                row[68*s+4*a+r] = -1
                curls.append(row)
    lorentz = np.kron(np.eye(4), split.known_rows(fields)[1])
    coordinate = np.zeros((4, 272))
    e, lam = fields["coframe"], fields["multiplier"]
    for nu in range(4):
        for mu in range(4):
            for a in range(4):
                coordinate[nu, 68*mu+40+4*a+mu] += e[a, nu]
                coordinate[nu, 68*mu+4*a+nu] += lam[a, mu]
                coordinate[nu, 68*nu+4*a+mu] -= lam[a, mu]
    return np.vstack((curls, lorentz, coordinate))


def constitutive_curls(fields, evaluated):
    connection = evaluated["connection"]
    psi, dp, de = (fields[key] for key in ("psi", "psi_first", "coframe_first"))
    spin = general.prolong.spin_lift(connection["omega"])
    dspin = general.prolong.spin_lift(connection["first"])
    covariant = general.cartan.covariant_jet(psi, dp, connection["omega"])
    weights = general.prior.joint.third.scalar.odd.readouts.dirac.WEIGHTS
    values = []
    for r in range(4):
        for s in range(r+1, 4):
            difference = np.einsum("ij,uj->ui", dspin[r, s]-dspin[s, r], psi)
            difference += dp[r] @ spin[s].T-dp[s] @ spin[r].T
            for a in range(4):
                value = (np.vdot(dp[r], (general.prolong.Q @ covariant[s]) @ weights[a].T)
                         -np.vdot(dp[s], (general.prolong.Q @ covariant[r]) @ weights[a].T)
                         +np.vdot(psi, (general.prolong.Q @ difference) @ weights[a].T))
                values.append(value.imag-de[r, a, s]+de[s, a, r])
    return np.array(values)


def known_rhs(fields, evaluated):
    primary = evaluated["vector"]
    lorentz = []
    for r in range(4):
        for generator in split.lorentz.generators():
            row = np.zeros(68)
            row[:16] = (generator.T @ fields["multiplier_first"][r]).ravel()
            spin = fields["psi_first"][r] @ split.lorentz.spin_generator(generator).T
            row[16:40] = 2*general.prior.joint.prior.realify(spin)
            row[40:56] = (generator @ fields["coframe_first"][r]).ravel()
            lorentz.append(-row @ primary)
    data = dict(fields, Euler=evaluated["gravity"], constraint=evaluated["constraint"],
                probe=evaluated["probe"].reshape(3, 4),
                Euler_first=np.zeros((4, 4, 4)), constraint_first=np.zeros((4, 4, 4)))
    return np.r_[constitutive_curls(fields, evaluated), lorentz, -ward.ward(data)]


def row_frame(matrix):
    left, singular, right = np.linalg.svd(matrix, full_matrices=False)
    rank = int(np.sum(singular > max(1e-9, singular[0]*1e-10)))
    return right[:rank].T, rank


def cached_matrix(services, prepared, fields, allowed, fingerprints):
    return services.cached("Cartan.first-attribution-higher/v1", {
        "sources": fingerprints, "numpy": np.__version__, "prepared": prepared,
        "fields": {key: fields[key] for key in previous.FIELD_KEYS}, "allowed": allowed},
        lambda: {"matrix": previous.normal_higher_matrix(prepared, fields, allowed)})["matrix"]


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, _, full, _ = general.domain.load_data()
    services = previous.first.prior.create_container().services()
    original = previous.first.load_system()
    origin_full = previous.first.extraction_matrix() @ original[7][:, :720]
    blocks = source.allowed_cauchy_coordinates()
    normal_indices = np.array(blocks["psi2"]+blocks["lambda2"]+blocks["e3"])
    fixed_indices = np.setdiff1d(np.arange(720), normal_indices)

    def sample(x):
        fields = general.domain.temporal.fields(prepared, point, jets, full, x)
        higher = previous.translated_higher(jets, full, x)
        if np.any(x):
            normal = services.cached("Cartan.general-first-normal-higher/v1", {
                "sources": previous.input_fingerprints(), "numpy": np.__version__,
                "prepared": prepared, "fields": {key: fields[key] for key in previous.FIELD_KEYS},
                "allowed": normal_indices},
                lambda: {"matrix": previous.normal_higher_matrix(prepared, fields, normal_indices)})["matrix"]
            matrix = np.zeros((272, 720))
            matrix[:, normal_indices] = normal
            matrix[:, fixed_indices] = cached_matrix(services, prepared, fields, fixed_indices, fingerprints)
        else:
            matrix = origin_full
            normal = matrix[:, normal_indices]
        actual = previous.first_prolongation(prepared, fields, higher)
        half = previous.first_prolongation(prepared, fields, higher, step=5e-5)
        evaluated = general.equations(prepared, fields)
        rows, rhs = known_rows(fields), known_rhs(fields, evaluated)
        frame, known_rank = row_frame(rows)
        model = previous.first.eliminate(matrix, np.zeros((272, 6)))
        normal_model = previous.first.eliminate(normal, np.zeros((272, 6)))
        projected = model["left_null"] @ (model["left_null"].T @ actual)
        predicted = np.linalg.lstsq(rows, rhs, rcond=1e-10)[0]
        increment = -model["inverse"] @ actual
        delta = source.regular.unpack(np.r_[increment, np.zeros(480)])
        corrected = {key: higher[key]+delta[key] for key in higher}
        direct = previous.first_prolongation(prepared, fields, corrected)
        linear = actual+matrix @ increment
        return {"coordinate": x.tolist(), "all_higher_rank": model["rank"],
            "normal_higher_rank": normal_model["rank"], "known_row_rank": known_rank,
            "left_nullity": model["left_null"].shape[1],
            "known_rows_annihilation_error": float(np.linalg.norm(rows @ matrix)),
            "known_span_left_space_error": float(np.linalg.norm(frame @ frame.T-model["left_null"] @ model["left_null"].T)),
            "known_identity_error": float(np.linalg.norm(rows @ actual-rhs)),
            "known_identity_half_step_error": float(np.linalg.norm(rows @ half-rhs)),
            "projected_reconstruction_error": float(np.linalg.norm(predicted-projected)),
            "normal_only_compatibility_norm": float(np.linalg.norm(normal_model["left_null"].T @ actual)),
            "all_higher_compatibility_norm": float(np.linalg.norm(projected)),
            "known_rhs_norms": {"constitutive_curls": float(np.linalg.norm(rhs[:24])),
                "differentiated_Lorentz_sources": float(np.linalg.norm(rhs[24:48])),
                "coordinate_Ward_sources": float(np.linalg.norm(rhs[48:]))},
            "higher_increment_norm": float(np.linalg.norm(increment)),
            "prescribed_higher_increment_norm": float(np.linalg.norm(increment[fixed_indices])),
            "corrected_direct_first_prolongation_norm": float(np.linalg.norm(direct)),
            "direct_higher_affinity_error": float(np.linalg.norm(direct-linear)),
            "lower_primary_residual_unchanged": float(np.linalg.norm(evaluated["vector"]))}

    with ThreadPoolExecutor(max_workers=2) as pool:
        samples = list(pool.map(sample, (np.zeros(4), np.eye(4)[0]/16384, np.eye(4)[1]/16384)))
    if fingerprints != input_fingerprints():
        raise RuntimeError("Attribution inputs changed during evaluation")
    return {"input_sha256": fingerprints, "scope": "sampled first compatibility attribution, fixed lower data and sources",
            "normal_coordinates": 224, "additional_prescribed_coordinates": 496,
            "known_row_blocks": {"constitutive_curls": 24, "differentiated_Lorentz": 24, "coordinate_Ward": 4},
            "no_regional_solution_or_nonlinear_lower_repair": True, "main_TeX_PDF_changed": False,
            "samples": samples}


if __name__ == "__main__":
    result = evaluate()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps(result["samples"], indent=2))
