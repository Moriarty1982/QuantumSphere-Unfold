"""Analytic full real-probe Hessian at E=I, E1=0 on the Cartan branch.

The lower point and p2 are fixed for affinity in l2, e3, p3 and lambda3.
No finite differences or field equations enter probe_second.
"""
import importlib.util
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "second_probe_scalar", Path(__file__).with_name("HC_Cartan_Next_Scalar_Compatibility.py"))
scalar = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scalar)
regular, spatial, prolong, prior, cartan = (
    scalar.regular, scalar.spatial, scalar.prolong, scalar.prior, scalar.cartan)


def _lambda_third(value):
    if value is None:
        return np.zeros((4, 4, 4, 4, 4))
    value = np.asarray(value)
    if np.iscomplexobj(value) or not np.all(np.isfinite(value)):
        raise ValueError("lambda_third must be finite and real")
    if value.shape == (320,):
        return prolong.unpack_third(value)
    if value.shape != (4, 4, 4, 4, 4):
        raise ValueError("lambda_third requires 320 packed coordinates or a full symmetric tensor")
    if not (np.allclose(value, value.swapaxes(0, 1), atol=1e-12, rtol=0)
            and np.allclose(value, value.swapaxes(1, 2), atol=1e-12, rtol=0)):
        raise ValueError("lambda_third derivative axes must be symmetric")
    return value.astype(float, copy=False)


def weight_jets(point, jets, lambda_third=None):
    """Unnormalized derivatives of W^mu=v(E^-1)^mu_a K^a+lambda^a_mu A_a."""
    e2, e3 = point["coframe_second"], jets["e3"]
    flat, charged = prolong.FLAT_WEIGHTS, prolong.Q_WEIGHTS
    w0 = cartan.kinetic_weights(np.eye(4), point["multiplier"])
    w1 = np.einsum("ram,aij->rmij", point["multiplier_first"], charged)
    w2 = (np.einsum("rsaa,mij->rsmij", e2, flat)
          -np.einsum("rsma,aij->rsmij", e2, flat)
          +np.einsum("rsam,aij->rsmij", jets["l2"], charged))
    w3 = (np.einsum("rstaa,mij->rstmij", e3, flat)
          -np.einsum("rstma,aij->rstmij", e3, flat)
          +np.einsum("rstam,aij->rstmij", _lambda_third(lambda_third), charged))
    return w0, w1, w2, w3


def probe_second(prepared, point, jets, lambda_third=None):
    """Return complex R2[r,s,k], shape (4,4,12), including all Z terms.

    jets uses regular.unpack keys p2,l2,e3,p3. lambda_third defaults to zero;
    its 320 real packed coordinates use prolong.PAIR3 then (a,mu).
    The point convention E=I,E1=0 is implicit in the existing point format.
    """
    p = prepared["data"]["psi"].reshape(12)
    p1, p2 = point["psi_first"].reshape(4, 12), jets["p2"].reshape(4, 4, 12)
    p3 = jets["p3"].reshape(4, 4, 4, 12)
    connection = regular.connection_second(prepared, point, jets)

    def lift(omega):
        spin = prolong.spin_lift(omega)
        return np.array([np.kron(np.eye(3), b) for b in spin.reshape(-1, 4, 4)]).reshape(
            spin.shape[:-2]+(12, 12))

    b0, b1, b2 = (lift(connection[key]) for key in ("omega", "first", "second"))
    w0, w1, w2, w3 = weight_jets(point, jets, lambda_third)
    adjoint = lambda value: value.conj().swapaxes(-1, -2)
    d0 = p1+b0 @ p
    d1 = p2+b1 @ p+np.einsum("mij,rj->rmi", b0, p1)
    z0 = np.einsum("mmij->ij", w1)-np.sum(adjoint(b0) @ w0+w0 @ b0, axis=0)
    z1 = np.einsum("rmmij->rij", w2)-np.sum(
        adjoint(b1) @ w0+adjoint(b0) @ w1+w1 @ b0+w0 @ b1, axis=1)
    result = np.empty((4, 4, 12), complex)
    volume2 = np.einsum("rsaa->rs", point["coframe_second"])
    for r in range(4):
        for s in range(4):
            d2 = (p3[r, s]+b2[r, s] @ p+b1[r] @ p1[s]
                  +b1[s] @ p1[r]+b0 @ p2[r, s])
            z2 = np.einsum("mmij->ij", w3[r, s])-np.sum(
                adjoint(b2[r, s]) @ w0+adjoint(b1[r]) @ w1[s]
                +adjoint(b1[s]) @ w1[r]+adjoint(b0) @ w2[r, s]
                +w2[r, s] @ b0+w1[r] @ b1[s]+w1[s] @ b1[r]
                +w0 @ b2[r, s], axis=0)
            result[r, s] = (
                1j*np.sum(w2[r, s] @ d0[..., None]
                          +w1[r] @ d1[s, ..., None]+w1[s] @ d1[r, ..., None]
                          +w0 @ d2[..., None], axis=0).reshape(12)
                -prior.MASS_WEIGHT @ (p2[r, s]+volume2[r, s]*p)
                +0.5j*(z2 @ p+z1[r] @ p1[s]+z1[s] @ p1[r]+z0 @ p2[r, s]))
    return result
