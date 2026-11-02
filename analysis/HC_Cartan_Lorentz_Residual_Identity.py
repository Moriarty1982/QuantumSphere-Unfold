"""Off-shell Lorentz identity in the declared neutral Cartan comparison only.

Unfitted jets, c=1, u=0, fixed M and Q. No continuation or field solve.
"""
import importlib.util
import hashlib
import json
from pathlib import Path
import types

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "lorentz_residual_regular", Path(__file__).with_name("HC_Cartan_Regular_Gravity.py"))
regular = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(regular)
parent, prolong = regular.cartan, regular.prolong


def generators():
    for a, b in parent.PAIRS:
        lower = np.zeros((4, 4))
        lower[a, b], lower[b, a] = 1, -1
        yield parent.ETA @ lower


def spin_generator(j):
    return -np.einsum("ab,aij,bjk->ik", parent.ETA @ j,
                      parent.GAMMA, parent.GAMMA)/4


def fixture(seed=74181):
    """Random normal jets, followed by y=A x+B(x,x)/2; no Euler fitting."""
    rng = np.random.default_rng(seed)
    psi = .5*(rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4)))
    p1 = .4*(rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4)))
    lam = .3*rng.normal(size=(4, 4))
    l1 = .4*rng.normal(size=(4, 4, 4))
    e2 = .3*rng.normal(size=(4, 4, 4, 4))
    e2 = (e2+e2.swapaxes(0, 1))/2
    response, source = parent.spin_maps(np.eye(4), psi)
    k = np.linalg.solve(parent.contorsion_hessian(np.eye(4)),
                        -source+response.T @ lam.reshape(-1))
    prepared = prolong.prepare({"psi": psi, "first": p1, "omega": parent.unpack(k)})
    point = {"psi_first": p1, "multiplier": lam,
             "multiplier_first": l1, "coframe_second": e2}
    jets = regular.unpack(.2*rng.normal(size=1200))
    connection = regular.connection_second(prepared, point, jets)
    a = np.eye(4)+.16*rng.normal(size=(4, 4))
    b = .2*rng.normal(size=(4, 4, 4))
    b = (b+b.swapaxes(1, 2))/2
    return {"seed": seed, "prepared": prepared, "point": point, "jets": jets,
            "connection": connection, "A": a, "B": b}


def pulled_fields(data):
    """Exact origin jets; multiplier is a coordinate vector density."""
    a, b, point = data["A"], data["B"], data["point"]
    inv, volume = np.linalg.inv(a), abs(np.linalg.det(a))
    lam, l1 = point["multiplier"], point["multiplier_first"]
    connection = data["connection"]
    w, w1 = connection["omega"], connection["first"]
    dl = []
    for s in range(4):
        da = b[:, :, s]
        dl.append(volume*(np.trace(inv @ da)*lam @ inv.T
                          +np.einsum("r,ram->am", a[:, s], l1) @ inv.T
                          -lam @ inv.T @ da.T @ inv.T))
    return {"coframe": a.copy(), "coframe_first": b.transpose(2, 0, 1).copy(),
            "psi": data["prepared"]["data"]["psi"].copy(),
            "psi_first": np.einsum("rm,rij->mij", a, point["psi_first"]),
            "multiplier": volume*lam @ inv.T, "multiplier_first": np.array(dl),
            "omega": np.einsum("rm,rab->mab", a, w),
            "omega_first": (np.einsum("rms,rab->smab", b, w)
                            +np.einsum("rm,ts,trab->smab", a, a, w1))}


def residuals(fields):
    e, de, psi, dp, lam, dl, w, dw = (fields[k] for k in (
        "coframe", "coframe_first", "psi", "psi_first", "multiplier",
        "multiplier_first", "omega", "omega_first"))
    inv, volume = np.linalg.inv(e), abs(np.linalg.det(e))
    dinv = np.array([-inv @ d @ inv for d in de])
    dvolume = volume*np.einsum("ma,ram->r", inv, de)
    dweights = (np.einsum("r,ma,aij->rmij", dvolume, inv, prolong.FLAT_WEIGHTS)
                +volume*np.einsum("rma,aij->rmij", dinv, prolong.FLAT_WEIGHTS)
                +np.einsum("ram,aij->rmij", dl, prolong.Q_WEIGHTS))
    bc = np.array([np.kron(np.eye(3), s) for s in parent.spin_connection(w)])
    op = regular.odd.real_law.real_operator(
        psi.reshape(-1), dp.reshape(4, 12), parent.kinetic_weights(e, lam), bc,
        volume*regular.prior.MASS_WEIGHT, np.einsum("mmij->ij", dweights))
    curvature = parent.curvature_upper(w, dw)
    f = regular.odd.channels(psi, parent.covariant_jet(psi, dp, w))["odd"]-e
    fe = parent.coframe_euler(e, psi, dp, w, curvature, regular.MASS, lam)
    response, source = parent.spin_maps(e, psi)
    lc = prolong.dirac.bundle(e, de)["omega"]
    cartan = (parent.contorsion_hessian(e) @ parent.pack(w-lc)+source
              -response.T @ lam.reshape(-1))
    return {"F": f, "R": op["symmetric"], "FE": fe, "operator": op,
            "curvature": curvature, "Cartan": cartan}


def identity_terms(fields, result, probe=None):
    r = result["R"] if probe is None else probe
    return np.array([[np.sum(result["FE"]*(j @ fields["coframe"])),
                      2*np.vdot((fields["psi"] @ spin_generator(j).T).reshape(-1), r).real,
                      np.sum(result["F"]*(j.T @ fields["multiplier"]))]
                     for j in generators()])


def raw_normal_fields(data, x):
    """Independent raw-parent elimination along the polynomial normal fields."""
    point, jets = data["point"], data["jets"]
    e2, e3 = point["coframe_second"], jets["e3"]
    e = np.eye(4)+np.einsum("r,s,rsam->am", x, x, e2)/2
    e += np.einsum("r,s,t,rstam->am", x, x, x, e3)/6
    de = np.einsum("s,rsam->ram", x, e2)+np.einsum("s,t,rstam->ram", x, x, e3)/2
    psi = data["prepared"]["data"]["psi"]+np.einsum("r,rij->ij", x, point["psi_first"])
    psi += np.einsum("r,s,rsij->ij", x, x, jets["p2"])/2
    lam = point["multiplier"]+np.einsum("r,ram->am", x, point["multiplier_first"])
    lam += np.einsum("r,s,rsam->am", x, x, jets["l2"])/2
    response, source = parent.spin_maps(e, psi)
    k = np.linalg.solve(parent.contorsion_hessian(e), -source+response.T @ lam.reshape(-1))
    return prolong.dirac.bundle(e, de)["omega"]+parent.unpack(k)


def connection_difference_errors(data, step):
    """All first directions and a mixed second derivative, bypassing fast maps."""
    raw = lambda x: raw_normal_fields(data, x)
    axes = np.eye(4)
    first = np.array([(raw(step*u)-raw(-step*u))/(2*step) for u in axes])
    u, v = axes[1], axes[2]
    mixed = (raw(step*(u+v))-raw(step*(u-v))
             -raw(step*(-u+v))+raw(-step*(u+v)))/(4*step**2)
    def pulled(x):
        y = data["A"] @ x+np.einsum("rmn,m,n->r", data["B"], x, x)/2
        jac = data["A"]+np.einsum("rms,s->rm", data["B"], x)
        return np.einsum("rm,rab->mab", jac, raw(y))

    pulled_first = np.array([(pulled(step*u)-pulled(-step*u))/(2*step) for u in axes])
    return {"first": float(np.linalg.norm(first-data["connection"]["first"])),
            "pulled_first": float(np.linalg.norm(pulled_first-pulled_fields(data)["omega_first"])),
            "mixed_second": float(np.linalg.norm(mixed-data["connection"]["second"][1, 2]))}


def input_fingerprints():
    root = Path(__file__).resolve().parent
    paths, seen = {Path(__file__).resolve()}, set()
    def visit(module):
        path = Path(getattr(module, "__file__", "") or ".").resolve()
        if path.parent != root or path.suffix != ".py" or path in seen:
            return
        seen.add(path)
        paths.add(path)
        for value in vars(module).values():
            if isinstance(value, types.ModuleType):
                visit(value)
    visit(regular)
    return {path.name: hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
            for path in sorted(paths)}


def evaluate():
    fingerprints = input_fingerprints()
    samples = []
    for seed in (74181, 74182, 74183):
        data = fixture(seed)
        fields = pulled_fields(data)
        result = residuals(fields)
        terms = identity_terms(fields, result)
        samples.append({"seed": seed, "E": fields["coframe"].tolist(),
                        "dE": fields["coframe_first"].tolist(),
                        "psi_real": fields["psi"].real.tolist(),
                        "psi_imag": fields["psi"].imag.tolist(),
                        "lambda": fields["multiplier"].tolist(),
                        "F0": result["F"].tolist(),
                        "R_real": result["R"].real.tolist(), "R_imag": result["R"].imag.tolist(),
                        "FE": result["FE"].tolist(), "terms_FE_R_F": terms.tolist(),
                        "identity": terms.sum(axis=1).tolist(),
                        "norms": {key: float(np.linalg.norm(result[key]))
                                  for key in ("F", "R", "FE", "Cartan", "curvature")},
                        "dE_norm": float(np.linalg.norm(fields["coframe_first"])),
                        "wrong_probe_sign": (terms @ np.array([1., -1., 1.])).tolist(),
                        "wrong_multiplier_sign": (terms @ np.array([1., 1., -1.])).tolist(),
                        "ordered_probe_identity": identity_terms(fields, result, result["operator"]["ordered"]).sum(axis=1).tolist()})
    data = fixture()
    differences = {str(h): connection_difference_errors(data, h) for h in (4e-4, 2e-4)}
    if fingerprints != input_fingerprints():
        raise RuntimeError("Lorentz audit source inputs changed")
    return {"scope": "Added neutral commuting-spinor odd-cross comparison; fixed M,Q,c=1,u=0. Numerical off-shell audit, not an existence or native-physics result.",
            "input_sha256": fingerprints,
            "identity": "FE:(J E)+2 Re[(S_J psi)^dagger R]+F:(J.T lambda)=0; F=C[Q]-E",
            "curvature_provenance": "Exact first jet of Cartan-eliminated connection, nonlinear coordinate pullback; no independent curvature draw.",
            "samples": samples,
            "raw_parent_connection_differences": differences}


if __name__ == "__main__":
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(evaluate(), indent=2)+"\n", encoding="utf-8")
    print(output)
