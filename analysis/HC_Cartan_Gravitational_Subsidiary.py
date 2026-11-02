"""Conditional gravitational subsidiary system, not a full coupled reduction.

Exact Cartan, probe and constitutive equations are assumptions on an open set.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "subsidiary_joint_neighborhood", Path(__file__).with_name("HC_Cartan_Joint_Neighborhood.py"))
neighborhood = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(neighborhood)
cartan = neighborhood.cartan


def background(coframe, first):
    e = cartan.checks._real(coframe, (4, 4), "coframe")
    de = cartan.checks._real(first, (4, 4, 4), "coframe derivatives")
    eta = cartan.ETA
    g = e.T @ eta @ e
    dg = np.array([v.T @ eta @ e+e.T @ eta @ v for v in de])
    inverse = np.linalg.inv(g)
    dinverse = -np.einsum("am,rmn,nb->rab", inverse, dg, inverse)
    if inverse[0, 0] >= 0:
        raise ValueError("Timelike coordinate conormal required")
    gamma = g[1:, 1:]
    if np.linalg.eigvalsh(gamma)[0] <= 0:
        raise ValueError("Spacelike slices required")
    gi = np.linalg.inv(gamma)
    dgi = -np.einsum("am,rmn,nb->rab", gi, dg[:, 1:, 1:], gi)
    lapse = (-inverse[0, 0])**-.5
    dlapse = .5*lapse**3*dinverse[:, 0, 0]
    shift = lapse*lapse*inverse[0, 1:]
    dshift = 2*lapse*dlapse[:, None]*inverse[None, 0, 1:]+lapse*lapse*dinverse[:, 0, 1:]
    normal = np.r_[1., -shift]/lapse
    dnormal = np.empty((4, 4))
    dnormal[:, 0] = -dlapse/lapse**2
    dnormal[:, 1:] = -dshift/lapse+dlapse[:, None]*shift[None, :]/lapse**2
    spatial = np.zeros((4, 4))
    spatial[1:, 1:] = gi
    dspatial = np.zeros((4, 4, 4))
    dspatial[:, 1:, 1:] = dgi
    basis = [spatial+np.outer(normal, normal)]
    dbasis = [dspatial+np.einsum("rm,n->rmn", dnormal, normal)+np.einsum("m,rn->rmn", normal, dnormal)]
    for i in range(1, 4):
        c, dc = spatial[:, i], dspatial[:, :, i]
        basis.append(np.outer(normal, c)+np.outer(c, normal))
        dbasis.append(np.einsum("rm,n->rmn", dnormal, c)+np.einsum("m,rn->rmn", normal, dc)
                      +np.einsum("rm,n->rmn", dc, normal)+np.einsum("m,rn->rmn", c, dnormal))
    basis = np.array(basis)
    dbasis = np.moveaxis(np.array(dbasis), 0, 1)
    christoffel = np.empty((4, 4, 4))
    for rho, mu, nu in np.ndindex((4, 4, 4)):
        christoffel[rho, mu, nu] = sum(inverse[rho, s]*(dg[mu, s, nu]+dg[nu, s, mu]-dg[s, mu, nu])
                                          for s in range(4))/2
    projection = np.vstack((lapse*lapse*np.eye(4)[0], lapse*g[1:]))
    divergence = (np.einsum("mbmn->bn", dbasis)
                  +np.einsum("r,brn->bn", np.einsum("mmr->r", christoffel), basis)
                  +np.einsum("nmr,bmr->bn", christoffel, basis))
    lower = projection @ divergence.T
    principal = np.array([-shift[i]*np.eye(4) for i in range(3)])
    for i in range(3):
        principal[i, 0, 1:] = lapse*gi[i]
        principal[i, i+1, 0] = lapse
    symmetrizer = np.zeros((4, 4))
    symmetrizer[0, 0] = 1
    symmetrizer[1:, 1:] = gi
    return {"metric": g, "metric_first": dg, "inverse_metric": inverse, "lapse": lapse,
            "lapse_first": dlapse, "shift": shift, "shift_first": dshift,
            "spatial_inverse": gi, "spatial_inverse_first": dgi, "normal": normal,
            "basis": basis, "basis_first": dbasis, "projection": projection,
            "christoffel": christoffel, "principal": principal,
            "symmetrizer": symmetrizer, "lower_order": lower}


def projected_divergence(bg, value, first):
    """Independent tensor-divergence expression for any U and partial U."""
    value, first = np.asarray(value), np.asarray(first)
    tensor = np.einsum("b,bmn->mn", value, bg["basis"])
    derivative = np.einsum("rb,bmn->rmn", first, bg["basis"])+np.einsum("b,rbmn->rmn", value, bg["basis_first"])
    connection = bg["christoffel"]
    divergence = (np.einsum("mmn->n", derivative)
                  +np.einsum("r,rn->n", np.einsum("mmr->r", connection), tensor)
                  +np.einsum("nmr,mr->n", connection, tensor))
    return bg["projection"] @ divergence


def naive_symbol(covector):
    covector = cartan.checks._real(covector, (3,), "spatial covector")
    symbol = np.zeros((4, 4))
    symbol[0, 1:] = covector
    return symbol


def input_fingerprints():
    result = neighborhood.input_fingerprints()
    result[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return result


def evaluate():
    fingerprints = input_fingerprints()
    prepared, point, jets, extras, _ = neighborhood.load_data()
    data = neighborhood.coefficient_norms(prepared, point, jets, extras)
    ball = neighborhood.select_radius(data)
    d = ball["coframe_change_bound"]
    symmetrizer_lower = min(1., 1/(1+d*(2+d)))
    symmetrizer_upper = max(1., 1/(1-d*(2+d)))
    rng = np.random.default_rng(4101114)
    directions = np.vstack((np.zeros(4), np.eye(4), -np.eye(4), rng.normal(size=(6, 4))))
    directions[1:] /= np.linalg.norm(directions[1:], axis=1, keepdims=True)
    checks = []
    for direction in directions:
        fields = neighborhood.fields(prepared, point, jets, extras, ball["radius"]*direction)
        bg = background(fields["coframe"], fields["coframe_first"])
        value, first = rng.normal(size=4), rng.normal(size=(4, 4))
        explicit = first[0]+np.einsum("iab,ib->a", bg["principal"], first[1:])+bg["lower_order"] @ value
        direct = projected_divergence(bg, value, first)
        q = rng.normal(size=3)
        symbol = np.einsum("i,iab->ab", q, bg["principal"])
        expected = np.sort(np.r_[-bg["shift"] @ q*np.ones(2),
            -bg["shift"] @ q+bg["lapse"]*np.sqrt(q @ bg["spatial_inverse"] @ q),
            -bg["shift"] @ q-bg["lapse"]*np.sqrt(q @ bg["spatial_inverse"] @ q)])
        checks.append({"symmetrizer_minimum_eigenvalue": float(np.linalg.eigvalsh(bg["symmetrizer"])[0]),
                       "symmetrizer_maximum_eigenvalue": float(np.linalg.eigvalsh(bg["symmetrizer"])[-1]),
                       "principal_symmetry_error": float(np.linalg.norm(bg["symmetrizer"] @ bg["principal"]
                            -(bg["symmetrizer"] @ bg["principal"]).swapaxes(-1, -2))),
                       "projected_divergence_error": float(np.linalg.norm(explicit-direct)),
                       "characteristic_eigenvalue_error": float(np.linalg.norm(np.sort(np.linalg.eigvals(symbol).real)-expected)),
                       "lower_order_matrix_norm": float(np.linalg.norm(bg["lower_order"], 2))})
    if fingerprints != input_fingerprints():
        raise RuntimeError("Subsidiary input sources changed")
    return {"scope": "Conditional homogeneous gravitational subsystem with exact probe and constitutive equations",
            "assumptions": ["Cartan Euler equation eliminated exactly", "R=0 and F=C-E=0 throughout an open set",
                            "spatial projection of trace-reversed coframe Euler tensor vanishes",
                            "sufficiently smooth regular metric, no incoming constraint boundary flux"],
            "input_sha256": fingerprints, "coordinate_radius": ball["radius"],
            "uniform_symmetrizer_lower_bound": symmetrizer_lower,
            "uniform_symmetrizer_upper_bound": symmetrizer_upper,
            "sample_checks_not_the_proof": checks,
            "naive_flat_symbol_rank": int(np.linalg.matrix_rank(naive_symbol([1, 0, 0]))),
            "naive_flat_symbol_square_norm": float(np.linalg.norm(naive_symbol([1, 0, 0]) @ naive_symbol([1, 0, 0]))),
            "R_F_propagation_not_established": True, "full_coupled_hyperbolicity_not_established": True,
            "not_interval_certified": True,
            "finite_Taylor_fields_not_on_shell_on_the_ball": True, "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = evaluate()
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("uniform_symmetrizer_lower_bound", "uniform_symmetrizer_upper_bound")}))


if __name__ == "__main__":
    main()
