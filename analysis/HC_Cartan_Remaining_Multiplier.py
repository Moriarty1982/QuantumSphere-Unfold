"""Six normal multiplier directions in the added neutral odd-cross Cartan model.

A pointwise quotient and response audit, not an extra gauge or evolution claim.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "remaining_regular_gravity", Path(__file__).with_name("HC_Cartan_Regular_Gravity.py"))
gravity = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gravity)
spatial, cartan, prior, prolong = gravity.spatial, gravity.cartan, gravity.prior, gravity.prolong
ETA = gravity.ETA
SPATIAL_INDICES = [4*a+i for a in range(4) for i in range(1, 4)]
EPSILON = np.zeros((4, 4, 4, 4))
for permutation in itertools.permutations(range(4)):
    inversions = sum(permutation[i] > permutation[j] for i in range(4) for j in range(i+1, 4))
    EPSILON[permutation] = (-1.)**inversions


def rank(matrix, tolerance=1e-9):
    """Absolute cutoff, with full singular values retained in the report."""
    return int(np.sum(np.linalg.svd(matrix, compute_uv=False) > tolerance))


def map_report(matrix):
    return {"shape": list(matrix.shape), "rank_at_absolute_1e_minus_9": rank(matrix),
            "norm": float(np.linalg.norm(matrix)),
            "singular_values": np.linalg.svd(matrix, compute_uv=False).tolist()}


def load_data():
    prepared, point, _ = gravity.load_data()
    payload = json.loads(Path(__file__).with_name("HC_Cartan_Regular_Gravity.json").read_text(encoding="utf-8"))
    return prepared, point, gravity.unpack(payload["joint_completion"]["jet_coordinates"])


def normal_point(point, direction, scale=1.):
    """Change only the declared 56 normal entries, leaving all other data fixed."""
    x = cartan.checks._real(direction, (56,), "56 real normal entries")
    result = dict(point)
    for name in ("coframe_second", "psi_first", "multiplier_first"):
        result[name] = point[name].copy()
    result["coframe_second"][0, 0] += scale*x[:16].reshape(4, 4)
    result["psi_first"][0] += scale*prior.complexify(x[16:40], (3, 4))
    result["multiplier_first"][0] += scale*x[40:].reshape(4, 4)
    return result


def axial_response(axial):
    """Normal-frame Clifford identity, L_(a,mu),(nu,bc)=delta_mu,nu eps^(abcd) a_d/2."""
    axial = cartan.checks._real(axial, (4,), "weighted axial vector")
    result = np.zeros((16, 24))
    for mu, (b, c) in itertools.product(range(4), cartan.PAIRS):
        index = 6*mu+cartan.PAIRS.index((b, c))
        for a in range(4):
            result[4*a+mu, index] = EPSILON[a, b, c] @ (ETA @ axial)/2
    return result


def raw_compensating_velocity(vector, spatial_axial_norm):
    v = cartan.checks._real(vector, (3,), "three acceleration parameters")
    spatial_axial_norm = cartan.checks._scalar(spatial_axial_norm, "positive spatial axial norm")
    if spatial_axial_norm <= 0:
        raise ValueError("Positive spatial axial norm required")
    result = np.zeros((4, 4))
    result[1:, 1:] = 4/spatial_axial_norm*np.array(
        [[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    return result


def closed_contorsion(axial, vector, denominator):
    """Contorsion response before removing the axial null from the multiplier."""
    axial = cartan.checks._real(axial, (4,), "weighted axial vector")
    v = cartan.checks._real(vector, (3,), "three acceleration parameters")
    denominator = cartan.checks._scalar(denominator, "nonzero normalization denominator")
    if denominator == 0:
        raise ValueError("Nonzero normalization denominator required")
    result = np.zeros((4, 4, 4))
    h = (np.outer(axial[1:], v)+np.outer(v, axial[1:]))/denominator
    result[1:, 0, 1:] = h
    result[1:, 1:, 0] = -h
    result[0, 0, 1:] = -2*axial[0]*v/denominator
    result[0, 1:, 0] = 2*axial[0]*v/denominator
    result[0, 1:, 1:] = (np.outer(axial[1:], v)-np.outer(v, axial[1:]))/denominator
    return result


def coefficient_identity(prepared):
    """All 4*3 bilinear axial/vector coefficients, with denominator one.

    Here H has integer entries and L has half-integer coefficients. Thus these
    basis-coefficient comparisons are exact dyadic arithmetic, not a random fit.
    """
    hessian = np.linalg.inv(prepared["inverse_hessian"])
    coefficients = []
    for axial, v in itertools.product(np.eye(4), np.eye(3)):
        coefficients.append(hessian @ cartan.pack(closed_contorsion(axial, v, 1.))
                            -axial_response(axial).T @ raw_compensating_velocity(v, 1.).reshape(-1))
    return {"residuals": np.array(coefficients),
            "H_integer_error": float(np.linalg.norm(hessian-np.rint(hessian)))}


def canonical_basis(prepared):
    """Three axial-source nulls and three longitudinal symmetric accelerations.

    The compensating spatial multiplier velocity is chosen perpendicular to
    eta*A_Q in each column, removing the three already exhibited source nulls.
    """
    axial = cartan.axial_currents(prepared["data"]["psi"])[1]
    covector = ETA @ axial
    if abs(axial[0]) < 1e-10 or np.linalg.norm(axial[1:]) < 1e-10:
        raise ValueError("This normal parametrization requires nonzero temporal and spatial A_Q")
    unit_covector = covector/np.linalg.norm(covector)
    spatial_unit = axial[1:]/np.linalg.norm(axial[1:])
    inverse, response = prepared["inverse_hessian"], prepared["response"]
    spatial_selector = np.eye(16)[:, SPATIAL_INDICES]
    connection_map = inverse @ response.T @ spatial_selector
    spatial_connection = connection_map.reshape(4, 6, 12)[1:].reshape(18, 12)
    orthogonality = np.kron(unit_covector[None, :], np.eye(3))
    solve_map = np.vstack((spatial_connection, orthogonality))
    basis = np.zeros((56, 6))
    accelerations, residuals = [], []
    for i, direction in enumerate(np.eye(3)):
        basis[40:, i] = np.outer(unit_covector, np.eye(4)[i+1]).reshape(-1)
        acceleration = np.zeros((4, 4))
        acceleration[1:, 1:] = np.outer(spatial_unit, direction)+np.outer(direction, spatial_unit)
        e2 = np.zeros((4, 4, 4))
        e2[0] = acceleration
        lc = prolong.normal_lorentz(e2)
        target = np.concatenate((-cartan.pack(lc).reshape(4, 6)[1:].reshape(-1), np.zeros(3)))
        velocity_matrix = (np.eye(4)-np.outer(unit_covector, unit_covector)) @ raw_compensating_velocity(
            direction, np.linalg.norm(axial[1:]))
        velocity = velocity_matrix.reshape(-1)[SPATIAL_INDICES]
        basis[:16, 3+i] = acceleration.reshape(-1)
        basis[40:, 3+i] = spatial_selector @ velocity
        accelerations.append(acceleration)
        residuals.append(solve_map @ velocity-target)
    return {"basis": basis, "weighted_axial": axial, "axial_covector_unit": unit_covector,
            "spatial_axial_unit": spatial_unit, "acceleration_basis": np.array(accelerations),
            "source_connection_map": connection_map, "compensation_map": solve_map,
            "compensation_residual": np.array(residuals)}


def spatial_connection_blocks(prepared):
    """Why gravity plus mixed curls forces delta omega_,0 at spatial columns to zero."""
    field, curl = [], []
    for coefficients in np.eye(18):
        full = np.zeros(24)
        full[6:] = coefficients
        connection = np.zeros((4, 4, 4, 4))
        connection[0] = cartan.unpack(full)
        curvature = cartan.curvature_upper(np.zeros((4, 4, 4)), connection)
        field.append(prolong.gravity_euler(curvature).reshape(-1))
        curl.append((prepared["response"] @ full).reshape(4, 4)[:, 1:].reshape(-1))
    field, curl = np.array(field).T, np.array(curl).T
    return {"gravity": field, "mixed_curls": curl, "joint": np.vstack((field, curl))}


def analytic_effects(prepared, direction):
    """Normal principal response; all lower field values and spatial jets stay fixed."""
    x = cartan.checks._real(direction, (56,), "56 real normal entries")
    if np.linalg.norm(x[16:40]) > 1e-10:
        raise ValueError("This response formula is for quotient directions with unchanged Psi_,0")
    e2 = np.zeros((4, 4, 4, 4))
    e2[0, 0] = x[:16].reshape(4, 4)
    l1 = np.zeros((4, 4, 4))
    l1[0] = x[40:].reshape(4, 4)
    lc = np.array([prolong.normal_lorentz(v) for v in e2])
    k1 = l1.reshape(4, 16) @ prepared["response"] @ prepared["inverse_hessian"].T
    contorsion = np.einsum("sp,pmab->smab", k1, cartan.OMEGA_BASIS)
    omega1 = lc+contorsion
    curvature = cartan.curvature_upper(np.zeros((4, 4, 4)), omega1)
    lc_curvature = cartan.curvature_upper(np.zeros((4, 4, 4)), lc)
    # At this normal point delta torsion_,r contains d2E and delta omega_,r.
    torsion_first = np.array([cartan.torsion(np.eye(4), e2[r], omega1[r]) for r in range(4)])
    psi = prepared["data"]["psi"]
    cov1 = np.einsum("smij,rj->smri", prolong.spin_lift(omega1), psi)
    c1 = np.array([spatial.odd.readouts.pairing(psi, v, spatial.Q).imag for v in cov1])
    weight_first = np.einsum("sam,aij->smij", l1, spatial.A)
    return {"LC_connection_first": lc, "contorsion_first": contorsion,
            "connection_first": omega1, "curvature": curvature, "LC_curvature": lc_curvature,
            "torsion_first": torsion_first, "constraint_first": c1,
            "kinetic_density_first": weight_first,
            "Cartan_linear_residual": (k1 @ np.linalg.inv(prepared["inverse_hessian"]).T
                                       -l1.reshape(4, 16) @ prepared["response"])}


def effect_maps(prepared, point, jets, basis):
    principal_names = tuple(analytic_effects(prepared, basis[:, 0]))
    principal = {name: [] for name in principal_names}
    point_maps, higher_maps = [], []
    base_point = spatial.rank_model.point_equations(
        prepared, point["psi_first"], point["coframe_second"], point["multiplier"], point["multiplier_first"])["vector"]
    base_higher = gravity.equations(prepared, point, jets)["vector"]
    connection = spatial.connection_first(prepared, point)
    connection_difference, curvature_difference, higher_affinity = [], [], []
    for x in basis.T:
        effects = analytic_effects(prepared, x)
        for name in principal:
            principal[name].append(effects[name].reshape(-1))
        changed = normal_point(point, x)
        point_maps.append(spatial.rank_model.point_equations(
            prepared, changed["psi_first"], changed["coframe_second"], changed["multiplier"],
            changed["multiplier_first"])["vector"]-base_point)
        higher = gravity.equations(prepared, changed, jets)["vector"]-base_higher
        higher_maps.append(higher)
        double = gravity.equations(prepared, normal_point(point, x, 2), jets)["vector"]-base_higher
        higher_affinity.append(double-2*higher)
        new_connection = spatial.connection_first(prepared, changed)
        connection_difference.append((new_connection[1]-connection[1]-effects["connection_first"]).reshape(-1))
        curvature_difference.append((cartan.curvature_upper(*new_connection)
                                     -cartan.curvature_upper(*connection)-effects["curvature"]).reshape(-1))
    result = {name: np.array(v).T for name, v in principal.items()}
    result.update(point_equations=np.array(point_maps).T, higher_equations=np.array(higher_maps).T,
                  direct_connection_error=np.array(connection_difference).T,
                  direct_curvature_error=np.array(curvature_difference).T,
                  higher_affinity_error=np.array(higher_affinity).T)
    for name, segment in (("first_constraint_equations", slice(0, 64)),
                          ("first_probe_equations", slice(64, 160)),
                          ("first_gravity_equations", slice(160, 224)),
                          ("second_constraint_equations", slice(224, 384))):
        result[name] = result["higher_equations"][segment]
    return result


def quotient_data(prepared, point):
    normal = spatial.normal_curl_system(prepared, point)
    gauge = gravity.coframe_normal_gauge_basis()
    canonical = canonical_basis(prepared)
    basis = canonical["basis"]
    combined = np.column_stack((gauge, basis))
    projector = combined @ np.linalg.pinv(combined, rcond=1e-11)
    return dict(canonical, normal=normal, gauge=gauge,
                combined=combined, kernel_span_error=(np.eye(56)-projector) @ normal["remaining_kernel"])


def field_difference_checks(prepared, point, jets, basis, step=2e-5):
    """Differentiate the actual Taylor fields, retaining every frozen higher jet."""
    connection_error, constraint_error, probe_error, torsion_error = [], [], [], []
    base = gravity.equations(prepared, point, jets)
    for x in basis.T:
        changed = normal_point(point, x)
        expected = analytic_effects(prepared, x)
        higher = gravity.equations(prepared, changed, jets)
        differences = {name: [] for name in ("omega", "constraint", "probe", "torsion")}
        for axis in np.eye(4):
            values = []
            for sign in (1, -1):
                old = gravity.taylor_fields(prepared, point, jets, sign*step*axis)
                new = gravity.taylor_fields(prepared, changed, jets, sign*step*axis)
                values.append({name: new[name]-old[name] for name in ("omega", "constraint", "probe")})
                values[-1]["torsion"] = (cartan.torsion(new["coframe"], new["coframe_first"], new["omega"])
                                          -cartan.torsion(old["coframe"], old["coframe_first"], old["omega"]))
            for name in differences:
                differences[name].append((values[0][name]-values[1][name])/(2*step))
        connection_error.append(np.linalg.norm(np.array(differences["omega"])-expected["connection_first"]))
        constraint_error.append(np.linalg.norm(np.array(differences["constraint"])-expected["constraint_first"]))
        torsion_error.append(np.linalg.norm(np.array(differences["torsion"])-expected["torsion_first"]))
        probe_error.append(np.linalg.norm(np.array(differences["probe"])-(higher["probe_first"]-base["probe_first"])))
    return {"step": step, "connection_first_errors": connection_error,
            "constraint_first_errors": constraint_error, "probe_first_errors": probe_error,
            "torsion_first_errors": torsion_error,
            "finite_differences_are_not_certified_bounds": True}


def algebraic_value_control(prepared, point, basis):
    """Changing lambda's value in ker L.T is not an algebraic parent redundancy.

    Keep the independent connection and its first jet fixed in this deliberately
    off-shell control. The independent coframe Euler expression changes by B.
    """
    omega, omega1 = spatial.connection_first(prepared, point)
    curvature = cartan.curvature_upper(omega, omega1)
    psi = prepared["data"]["psi"]
    base = cartan.coframe_euler(np.eye(4), psi, point["psi_first"], omega, curvature,
                                prior.MASS, point["multiplier"])
    changes = []
    for column in basis[:, :3].T:
        shift = column[40:].reshape(4, 4)
        changes.append((cartan.coframe_euler(np.eye(4), psi, point["psi_first"], omega, curvature,
                                            prior.MASS, point["multiplier"]+shift)-base).reshape(-1))
    return np.array(changes).T


def evaluate():
    prepared, point, jets = load_data()
    quotient = quotient_data(prepared, point)
    basis, gauge = quotient["basis"], quotient["gauge"]
    effects = effect_maps(prepared, point, jets, basis)
    h_inverse, response = prepared["inverse_hessian"], prepared["response"]
    schur = response @ h_inverse @ response.T
    multiplier_basis = basis[40:]
    blocks = spatial_connection_blocks(prepared)
    identity = coefficient_identity(prepared)
    no_acceleration = basis[:, 3:].copy()
    no_acceleration[:16] = 0
    frozen_coframe = quotient["normal"]["matrix"][:, 40:][:, SPATIAL_INDICES]
    fingerprints = {path: hashlib.sha256(Path(__file__).with_name(path).read_bytes()).hexdigest()
                    for path in ("HC_Cartan_Regular_Gravity.json", "HC_Cartan_Spatial_Propagation.json")}
    reports = {}
    for name, matrix in effects.items():
        reports[name] = {"all_six": map_report(matrix),
                         "axial_source_null_three": map_report(matrix[:, :3]),
                         "compensated_three": map_report(matrix[:, 3:])}
    return {"status": "pointwise normal quotient in the added neutral odd-cross Cartan comparison only",
            "input_sha256": fingerprints,
            "unchanged": {"mass": prior.MASS.tolist(), "selector_real": spatial.Q.real.tolist(),
                          "selector_imaginary": spatial.Q.imag.tolist(), "Einstein_coefficient": 1., "vacuum": 0.,
                          "multiplier_value": point["multiplier"].tolist(), "normal_Psi_derivative_change": 0.,
                          "normal_temporal_multiplier_column_change": 0.},
            "normal_system": {"shape": list(quotient["normal"]["matrix"].shape),
                              "rank": quotient["normal"]["rank"],
                              "gauge_rank": rank(gauge), "canonical_quotient_rank": rank(basis),
                              "joint_kernel_basis_rank": rank(quotient["combined"]),
                              "normal_annihilation_norm": float(np.linalg.norm(quotient["normal"]["matrix"] @ basis)),
                              "gauge_orthogonality_norm": float(np.linalg.norm(gauge.T @ basis)),
                              "kernel_span_error": float(np.linalg.norm(quotient["kernel_span_error"])),
                              "spatial_multiplier_projection": map_report(multiplier_basis[SPATIAL_INDICES])},
            "parametrization": {"coordinate_order": "three axial-column coefficients, then three h=s_hat*v^T+v*s_hat^T coefficients",
                                "weighted_axial": quotient["weighted_axial"].tolist(),
                                "weighted_axial_Lorentz_square": float(quotient["weighted_axial"] @ ETA @ quotient["weighted_axial"]),
                                "axial_covector_unit": quotient["axial_covector_unit"].tolist(),
                                "spatial_axial_unit": quotient["spatial_axial_unit"].tolist(),
                                "normal_basis_56_by_6": basis.tolist(),
                                "compensation_map": map_report(quotient["compensation_map"]),
                                "compensation_residual_norm": float(np.linalg.norm(quotient["compensation_residual"]))},
            "source_and_Schur": {"response": map_report(response), "Schur": map_report(schur),
                                 "Lt_on_quotient": map_report(response.T @ multiplier_basis),
                                 "Schur_on_quotient": map_report(schur @ multiplier_basis),
                                 "axial_null_Lt_norm": float(np.linalg.norm(response.T @ multiplier_basis[:, :3])),
                                 "longitudinal_compensation_Schur_norm": float(np.linalg.norm(
                                     schur @ multiplier_basis[:, 3:] @ quotient["spatial_axial_unit"]))},
            "structural_checks": {
                "axial_Clifford_formula_error": float(np.linalg.norm(response-axial_response(quotient["weighted_axial"]))),
                "Cartan_compensation_bilinear_coefficient_error": float(np.linalg.norm(identity["residuals"])),
                "integer_Hessian_error": identity["H_integer_error"],
                "spatial_connection_gravity": map_report(blocks["gravity"]),
                "spatial_connection_mixed_curls": map_report(blocks["mixed_curls"]),
                "spatial_connection_gravity_and_curls": map_report(blocks["joint"]),
                "normal_spatial_multiplier_block_with_E2_fixed": map_report(frozen_coframe),
                "compensated_three_without_acceleration": map_report(quotient["normal"]["matrix"] @ no_acceleration),
                "off_shell_axial_lambda_value_shift_coframe_Euler": map_report(algebraic_value_control(prepared, point, basis))},
            "effects_with_higher_jets_frozen": reports,
            "independent_Taylor_field_differences": field_difference_checks(prepared, point, jets, basis),
            "point_equations_baseline_norm": float(np.linalg.norm(spatial.rank_model.point_equations(
                prepared, point["psi_first"], point["coframe_second"], point["multiplier"], point["multiplier_first"])["vector"])),
            "higher_equations_baseline_norm": float(np.linalg.norm(gravity.equations(prepared, point, jets)["vector"])),
            "not_claimed": ["six additional gauge symmetries or physical modes", "full algebraic multiplier redundancy",
                            "constraint closure or a Cauchy solution", "native HC dynamics or physical normalization"],
            "main_TeX_or_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(evaluate(), indent=2, allow_nan=False)+"\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
