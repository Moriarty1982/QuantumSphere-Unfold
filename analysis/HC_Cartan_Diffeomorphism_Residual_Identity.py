"""Off-shell coordinate Ward identity after exact Cartan elimination.

Generic residuals are retained. This is not an autonomous full constraint system.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "diffeomorphism_joint", Path(__file__).with_name("HC_Cartan_Next_Joint_Completion.py"))
joint = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(joint)
regular, spatial, prolong, prior, cartan = joint.regular, joint.third.spatial, joint.prolong, joint.prior, joint.cartan


def ward_terms(data):
    e, de, fe, dfe = (data[key] for key in ("coframe", "coframe_first", "Euler", "Euler_first"))
    lam, dl, f, df = (data[key] for key in ("multiplier", "multiplier_first", "constraint", "constraint_first"))
    divergence = np.einsum("a,an->n", np.einsum("mam->a", dfe), e)
    frame_curl = np.einsum("am,man->n", fe, de)-np.einsum("am,nam->n", fe, de)
    multiplier_curl = np.einsum("am,man->n", lam, df)-np.einsum("am,nam->n", lam, df)
    multiplier_divergence = np.einsum("an,a->n", f, np.einsum("mam->a", dl))
    probe_source = -2*np.array([np.vdot(p, data["probe"]).real for p in data["psi_first"]])
    return {"coframe_Euler_divergence": divergence, "coframe_curl": frame_curl,
            "multiplier_constraint_curl": multiplier_curl,
            "constraint_multiplier_divergence": multiplier_divergence,
            "probe_source": probe_source}


def ward(data):
    return sum(ward_terms(data).values())


def normal_fixture(seed):
    rng = np.random.default_rng(seed)
    original = dict(prolong.load_prior()[0])
    psi = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
    p1 = rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4))
    original.update(psi=psi, first=p1, omega=np.zeros((4, 4, 4)))
    prepared = prolong.prepare(original)
    point = {"psi_first": p1, "multiplier": rng.normal(size=(4, 4))*.2,
             "multiplier_first": rng.normal(size=(4, 4, 4))*.3,
             "coframe_second": prior.unpack_second(rng.normal(size=160)*.4)}
    jets = regular.unpack(rng.normal(size=1200)*.3)
    fields = spatial.rank_model.point_equations(prepared, p1, point["coframe_second"],
                                                point["multiplier"], point["multiplier_first"])
    first = regular.equations(prepared, point, jets)
    return {"coframe": np.eye(4), "coframe_first": np.zeros((4, 4, 4)), "psi": psi,
            "psi_first": p1, "multiplier": point["multiplier"],
            "multiplier_first": point["multiplier_first"], "constraint": fields["constraint"],
            "constraint_first": first["constraint_first"], "probe": fields["probe"].reshape(3, 4),
            "Euler": fields["coframe"], "Euler_first": first["coframe_Euler_first"]}


def local_coordinate_change(data, h):
    """Second coordinate jet at identity Jacobian; h[r,alpha,mu]=h[mu,alpha,r]."""
    h = cartan.checks._real(h, (4, 4, 4), "coordinate second jet")
    if not np.allclose(h, h.swapaxes(0, 2), atol=1e-12, rtol=0):
        raise ValueError("Coordinate second derivatives must commute")
    result = {key: value.copy() for key, value in data.items()}
    dv = np.trace(h, axis1=1, axis2=2)
    for key in ("Euler", "multiplier"):
        result[key+"_first"] += dv[:, None, None]*data[key]-np.einsum("am,rnm->ran", data[key], h)
    for key in ("coframe", "constraint"):
        result[key+"_first"] += np.einsum("am,rmn->ran", data[key], h)
    return result


def local_lorentz_change(data, generators):
    """Lorentz matrix is I at the point; its four derivatives are generators."""
    generators = cartan.checks._real(generators, (4, 4, 4), "Lorentz first derivatives")
    eta = cartan.ETA
    if not np.allclose(generators.swapaxes(-1, -2) @ eta+eta @ generators, 0, atol=1e-12, rtol=0):
        raise ValueError("Lorentz generators required")
    spin = -.25*np.einsum("rab,aij,bjk->rik", eta @ generators, cartan.GAMMA, cartan.GAMMA)
    result = {key: value.copy() for key, value in data.items()}
    for key in ("coframe", "constraint"):
        result[key+"_first"] += generators @ data[key]
    for key in ("Euler", "multiplier"):
        result[key+"_first"] -= generators.swapaxes(-1, -2) @ data[key]
    result["psi_first"] += np.einsum("rij,uj->rui", spin, data["psi"])
    return result


def constant_coordinate_change(data, jacobian):
    """x=D y; Euler, probe and lambda retain their density weights."""
    d = cartan.checks._real(jacobian, (4, 4), "invertible coordinate Jacobian")
    inverse, volume = np.linalg.inv(d), abs(np.linalg.det(d))
    result = {key: value.copy() for key, value in data.items()}
    for key in ("coframe", "constraint"):
        result[key] = data[key] @ d
        result[key+"_first"] = np.einsum("nr,nam,ms->ras", d, data[key+"_first"], d)
    for key in ("Euler", "multiplier"):
        result[key] = volume*data[key] @ inverse.T
        result[key+"_first"] = volume*np.einsum("nr,nam,sm->ras", d, data[key+"_first"], inverse)
    result["psi_first"] = np.einsum("nr,nui->rui", d, data["psi_first"])
    result["probe"] = volume*data["probe"]
    return result


def transformed_fixture(seed):
    data = normal_fixture(seed)
    rng = np.random.default_rng(seed+1)
    h = rng.normal(size=(4, 4, 4))*.2
    data = local_coordinate_change(data, (h+h.swapaxes(0, 2))/2)
    lower = rng.normal(size=(4, 4, 4))*.2
    generators = cartan.ETA @ (lower-lower.swapaxes(-1, -2))/2
    data = local_lorentz_change(data, generators)
    return constant_coordinate_change(data, np.eye(4)+rng.normal(size=(4, 4))*.1)


def input_fingerprints():
    result = joint.input_fingerprints()
    for name in (Path(__file__).name, "HC_Cross_Cartan_Parent.py", "HC_Probe_Law_Revision_Audit.py"):
        raw = Path(__file__).with_name(name).read_bytes().replace(b"\r\n", b"\n")
        result[name] = hashlib.sha256(raw).hexdigest()
    return result


def evaluate():
    fingerprints = input_fingerprints()
    result = []
    for seed in range(72410, 72416):
        data = transformed_fixture(seed)
        terms = ward_terms(data)
        error = sum(terms.values())
        result.append({"seed": seed, "identity": error.tolist(), "identity_norm": float(np.linalg.norm(error)),
                       "coframe_first_norm": float(np.linalg.norm(data["coframe_first"])),
                       "probe_residual_norm": float(np.linalg.norm(data["probe"])),
                       "constraint_residual_norm": float(np.linalg.norm(data["constraint"])),
                       "Euler_residual_norm": float(np.linalg.norm(data["Euler"])),
                       "term_norms": {key: float(np.linalg.norm(value)) for key, value in terms.items()},
                       "omission_control_norms": {key: float(np.linalg.norm(error-value)) for key, value in terms.items()}})
    if fingerprints != input_fingerprints():
        raise RuntimeError("Coordinate Ward inputs changed")
    return {"scope": "Off-shell coordinate Ward identity after exact algebraic Cartan elimination",
            "input_sha256": fingerprints, "random_genuine_jet_controls": result,
            "generic_coframe_jets_from_coordinate_and_Lorentz_transformations": True,
            "probe_and_constitutive_sources_not_dropped": True, "not_full_constraint_propagation": True,
            "main_TeX_PDF_changed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = evaluate()
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps([r["identity_norm"] for r in report["random_genuine_jet_controls"]]))


if __name__ == "__main__":
    main()
