"""Analytic Hessian of the independent coframe Euler density, c=1, vacuum=0.

Normal point E=I,E1=0 only. This differentiates the independent Palatini
coframe variation after evaluating the Cartan connection, not metric LC gravity.
"""
import importlib.util
import itertools
from pathlib import Path

import numpy as np


SPEC = importlib.util.spec_from_file_location(
    "second_gravity_third", Path(__file__).with_name("HC_Cartan_Third_Constraint_Reprepare.py"))
third = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(third)
scalar, regular, prolong, prior, cartan = (
    third.scalar, third.regular, third.prolong, third.prior, third.cartan)


def highest_delta_omega3(prepared, e4=None, l3=None):
    """New E4 (35,4,4) and lambda3 (20,4,4) contribution to full omega3."""
    e4 = np.zeros((35, 4, 4)) if e4 is None else cartan.checks._real(
        e4, (35, 4, 4), "unique E4 coordinates")
    l3 = np.zeros((20, 4, 4)) if l3 is None else cartan.checks._real(
        l3, (20, 4, 4), "unique lambda3 coordinates")
    quads = third.diagnostic.QUADS
    de = np.array([[e4[quads.index(tuple(sorted(indices+(mu,))))]
                    for mu in range(4)] for indices in third.TRIPLES])
    unique = (de.reshape(20, 64) @ regular.LC_LINEAR).reshape(20, 4, 4, 4)
    k3 = (l3.reshape(20, 16) @ prepared["response"]) @ prepared["inverse_hessian"].T
    unique += np.einsum("tp,pmab->tmab", k3, cartan.OMEGA_BASIS)
    result = np.empty((4, 4, 4, 4, 4, 4))
    for indices, value in zip(third.TRIPLES, unique):
        for permutation in set(itertools.permutations(indices)):
            result[permutation] = value
    return result


def curvature_second(omega, first, second, omega3):
    """Full upper curvature Hessian; derivative axes precede (mu,nu,a,b)."""
    eta = cartan.ETA
    a0, a1, a2 = (np.einsum("ab,...bc->...ac", eta, w)
                  for w in (omega, first, second))
    result = np.empty((4,)*6)
    for r, s, mu, nu in np.ndindex((4,)*4):
        product = (a2[r, s, mu] @ a0[nu]+a1[r, mu] @ a1[s, nu]
                   +a1[s, mu] @ a1[r, nu]+a0[mu] @ a2[r, s, nu]
                   -a2[r, s, nu] @ a0[mu]-a1[r, nu] @ a1[s, mu]
                   -a1[s, nu] @ a1[r, mu]-a0[nu] @ a2[r, s, mu])
        result[r, s, mu, nu] = (product @ eta
            +eta @ (omega3[r, s, mu, nu]-omega3[r, s, nu, mu]) @ eta)
    return result


def normal_frame_response(delta, cross, mass, curvature):
    """Exact E-directional derivative of coframe_euler at I with matter/R fixed."""
    identity, j = np.eye(4), -delta
    v = np.trace(delta)
    ld = -np.trace(cross)-mass
    dld = v*ld-np.sum(j.T*cross)
    result = (dld*identity+ld*j.T+v*cross.T+(j @ cross+cross @ j).T)

    def contract(left, right):
        return np.einsum("ma,nb,mnab->", left, right, curvature)

    lg = contract(identity, identity)/2
    dlg = v*lg+(contract(j, identity)+contract(identity, j))/2
    result += dlg*identity+lg*j.T
    for a, nu in np.ndindex(4, 4):
        di = -np.outer(identity[:, a], identity[nu])
        ddi = -np.outer(j[:, a], identity[nu])-np.outer(identity[:, a], j[nu])
        dr = contract(di, identity)+contract(identity, di)
        ddr = (contract(ddi, identity)+contract(di, j)
               +contract(j, di)+contract(identity, ddi))
        result[a, nu] += (v*dr+ddr)/2
    return result


def coframe_euler_second(prepared, point, jets, *, e4=None, l3=None,
                         omega3=None, lc_third=None):
    """Return real FE2[r,s,a,mu], shape (4,4,4,4), unnormalized derivatives.

    Fix the lower point, E2 and p2 for affinity in l2,e3,p3,e4,l3.
    e4/l3 are unique symmetric coordinate tensors. omega3 is an optional
    absolute full (4,4,4,4,4,4) override, mutually exclusive with e4/l3.
    lc_third can cache third.lc_cubic(prepared,point), with E4 excluded.
    """
    if omega3 is not None:
        if e4 is not None or l3 is not None:
            raise ValueError("Use an absolute omega3 override or e4/l3, not both")
        omega3 = cartan.checks._real(omega3, (4,)*6, "full omega3 override")
        connection = regular.connection_second(prepared, point, jets)
    else:
        if lc_third is None:
            lc_third = third.lc_cubic(prepared, point)
        connection = third.connection_third(prepared, point, jets, lc_third)
        omega3 = connection["third"]+highest_delta_omega3(prepared, e4, l3)
    w0, w1, w2 = (connection[key] for key in ("omega", "first", "second"))
    r0 = cartan.curvature_upper(w0, w1)
    r2 = curvature_second(w0, w1, w2, omega3)
    b0, b1, b2 = (prolong.spin_lift(w) for w in (w0, w1, w2))
    psi, p1, p2 = prepared["data"]["psi"], point["psi_first"], jets["p2"]
    d0 = cartan.covariant_jet(psi, p1, w0)
    d1 = (p2+np.einsum("rmij,uj->rmui", b1, psi)
          +np.einsum("mij,ruj->rmui", b0, p1))
    d2 = (jets["p3"]+np.einsum("rsmij,uj->rsmui", b2, psi)
          +np.einsum("rmij,suj->rsmui", b1, p1)
          +np.einsum("smij,ruj->rsmui", b1, p1)
          +np.einsum("mij,rsuj->rsmui", b0, p2))
    pair = scalar.odd.readouts.pairing
    x0 = pair(psi, d0).imag
    mass0 = np.vdot(psi, scalar.MASS @ psi @ scalar.BETA.T).real
    result = np.empty((4, 4, 4, 4))
    for r, s in np.ndindex(4, 4):
        x2 = (pair(p2[r, s], d0)+pair(p1[r], d1[s])
              +pair(p1[s], d1[r])+pair(psi, d2[r, s])).imag
        mass2 = (2*np.vdot(psi, scalar.MASS @ p2[r, s] @ scalar.BETA.T).real
                 +2*np.vdot(p1[r], scalar.MASS @ p1[s] @ scalar.BETA.T).real)
        result[r, s] = ((-np.trace(x2)-mass2)*np.eye(4)+x2.T
                        +prolong.gravity_euler(r2[r, s])+jets["l2"][r, s]
                        +normal_frame_response(point["coframe_second"][r, s], x0, mass0, r0))
    return result


gravity_second = coframe_euler_second
