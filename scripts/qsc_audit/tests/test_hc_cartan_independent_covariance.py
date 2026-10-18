"""Independent covariance checks of the added neutral odd-cross Cartan parent.

Saved point jets are not a Cauchy solution or an identification of native physics.
No higher-jet coefficient matrix or continuation solve is constructed here.
"""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "cartan_independent_covariance", ROOT / "analysis/HC_Cartan_Regular_Gravity.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)
parent = model.cartan


def lorentz_generators():
    result = []
    for a, b in itertools.combinations(range(4), 2):
        lower = np.zeros((4, 4))
        lower[a, b], lower[b, a] = 1, -1
        result.append(parent.ETA @ lower)
    return result


def spin_generator(generator):
    return -np.einsum("ab,aij,bjk->ik", parent.ETA @ generator,
                      parent.GAMMA, parent.GAMMA)/4


def unrelated_parent_data():
    rng = np.random.default_rng(74023)
    coframe = np.eye(4)+.05*rng.normal(size=(4, 4))
    psi = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
    first = rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4))
    omega = parent.unpack(.1*rng.normal(size=24))
    omega_first = np.array([parent.unpack(.1*rng.normal(size=24)) for _ in range(4)])
    curvature = parent.curvature_upper(omega, omega_first)
    multiplier = .2*rng.normal(size=(4, 4))
    return (coframe, psi, first, omega, curvature, multiplier), rng


def direct_density(fields):
    e, psi, first, omega, curvature, multiplier = fields
    # Off-shell comparison only; the saved c=1, u=0 data are not modified.
    return parent.direct_parent_density(e, psi, first, omega, curvature,
                                       model.MASS, multiplier, coefficient=.7, vacuum=.09)


def density_difference(fields, variation, step):
    plus = tuple(value+step*delta for value, delta in zip(fields, variation))
    minus = tuple(value-step*delta for value, delta in zip(fields, variation))
    return (direct_density(plus)-direct_density(minus))/(2*step)


class HCCartanIndependentCovarianceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, _ = model.load_data()
        saved = json.loads((ROOT / "analysis/HC_Cartan_Regular_Gravity.json").read_text(encoding="utf-8"))
        cls.jets = model.unpack(np.array(saved["joint_completion"]["jet_coordinates"]))
        cls.result = model.equations(cls.prepared, cls.point, cls.jets)

    def copied_fields(self):
        return ({key: value.copy() for key, value in self.point.items()},
                {key: value.copy() for key, value in self.jets.items()})

    def test_direct_parent_local_lorentz_covariance_including_parameter_derivatives(self):
        fields, rng = unrelated_parent_data()
        e, psi, first, omega, curvature, multiplier = fields
        lower = rng.normal(size=(4, 4))
        lower -= lower.T.copy()
        generator = parent.ETA @ lower
        lower_first = rng.normal(size=(4, 4, 4))
        lower_first -= lower_first.swapaxes(1, 2).copy()
        spin = spin_generator(generator)
        spin_first = -np.einsum("mab,aij,bjk->mik", lower_first,
                                parent.GAMMA, parent.GAMMA)/4
        variation = (
            generator @ e,
            np.einsum("ij,rj->ri", spin, psi),
            np.einsum("ij,mrj->mri", spin, first)+np.einsum("mij,rj->mri", spin_first, psi),
            np.einsum("ab,mbc->mac", parent.ETA @ generator @ parent.ETA, omega)
            -np.einsum("mab,bc->mac", omega, generator)-lower_first,
            np.einsum("ab,mnbc->mnac", generator, curvature)
            +np.einsum("mnab,cb->mnac", curvature, generator),
            -generator.T @ multiplier)
        coarse = abs(density_difference(fields, variation, 1e-4))
        fine = abs(density_difference(fields, variation, 1e-5))
        self.assertLess(fine, 2e-7)
        self.assertLess(fine, .1*coarse)
        omitted = list(variation)
        omitted[2] = np.einsum("ij,mrj->mri", spin, first)
        self.assertGreater(abs(density_difference(fields, omitted, 1e-5)), .1)

    def test_direct_parent_coordinate_covariance_uses_vector_density_multiplier(self):
        fields, rng = unrelated_parent_data()
        e, psi, first, omega, curvature, multiplier = fields
        jacobian = .1*rng.normal(size=(4, 4))  # jacobian[nu, mu] = d_mu xi^nu.
        variation = (
            e @ jacobian,
            np.zeros_like(psi),
            np.einsum("nm,nri->mri", jacobian, first),
            np.einsum("nm,nab->mab", jacobian, omega),
            np.einsum("rm,rnab->mnab", jacobian, curvature)
            +np.einsum("rn,mrab->mnab", jacobian, curvature),
            np.trace(jacobian)*multiplier-multiplier @ jacobian.T)
        predicted = np.trace(jacobian)*direct_density(fields)
        self.assertLess(abs(density_difference(fields, variation, 1e-5)-predicted), 2e-7)
        omitted = list(variation)
        omitted[5] = -multiplier @ jacobian.T
        self.assertGreater(abs(density_difference(fields, omitted, 1e-5)-predicted), .01)

    def test_independent_coframe_euler_matches_direct_parent_variation(self):
        fields, rng = unrelated_parent_data()
        e, psi, first, omega, curvature, multiplier = fields
        delta = rng.normal(size=(4, 4))
        variation = (delta, np.zeros_like(psi), np.zeros_like(first),
                     np.zeros_like(omega), np.zeros_like(curvature), np.zeros_like(multiplier))
        predicted = np.sum(parent.coframe_euler(e, psi, first, omega, curvature,
                                               model.MASS, multiplier, .7, .09)*delta)
        coarse = abs(density_difference(fields, variation, 1e-4)-predicted)
        fine = abs(density_difference(fields, variation, 1e-5)-predicted)
        self.assertLess(fine, 2e-7)
        self.assertLess(fine, .1*coarse)

    def test_complete_lorentz_gauge_jets_preserve_retained_equations(self):
        self.assertLess(np.linalg.norm(self.result["vector"]), 1e-8)
        omitted_errors = []
        for index, generator in enumerate(lorentz_generators()):
            with self.subTest(generator=index):
                point, jets = self.copied_fields()
                spin = spin_generator(generator)
                point["coframe_second"][0, 0] += generator
                omitted_errors.append(np.linalg.norm(
                    model.equations(self.prepared, point, jets)["vector"]-self.result["vector"]))
                jets["p2"][0, 0] += np.einsum("ij,rj->ri", spin, self.prepared["data"]["psi"])
                jets["l2"][0, 0] -= generator.T @ self.point["multiplier"]
                # Product rule for exp(S_J t^2/2) Psi through cubic order.
                for r, s, t in np.ndindex((4, 4, 4)):
                    for a, b, c in ((r, s, t), (r, t, s), (s, t, r)):
                        if a == b == 0:
                            jets["p3"][r, s, t] += (spin @ self.point["psi_first"][c].T).T
                actual = model.equations(self.prepared, point, jets)["vector"]
                self.assertLess(np.linalg.norm(actual-self.result["vector"]), 1e-8)
        self.assertGreater(min(omitted_errors), .1)

    def test_complete_coordinate_gauge_jets_preserve_retained_equations(self):
        self.assertLess(np.linalg.norm(self.result["vector"]), 1e-8)
        omitted_errors = []
        for index, vector in enumerate(np.eye(4)):
            with self.subTest(generator=index):
                point, jets = self.copied_fields()
                point["coframe_second"][0, 0, :, 0] += vector
                omitted_errors.append(np.linalg.norm(
                    model.equations(self.prepared, point, jets)["vector"]-self.result["vector"]))
                jets["p3"][0, 0, 0] += np.einsum("r,rij->ij", vector, self.point["psi_first"])
                jacobian = np.zeros((4, 4))
                jacobian[:, 0] = vector
                jets["l2"][0, 0] += (vector[0]*self.point["multiplier"]
                                      -self.point["multiplier"] @ jacobian.T)
                actual = model.equations(self.prepared, point, jets)["vector"]
                self.assertLess(np.linalg.norm(actual-self.result["vector"]), 1e-8)
        self.assertGreater(min(omitted_errors), .1)

    def test_connection_second_difference_uses_raw_parent_spin_maps_and_hessian(self):
        rng = np.random.default_rng(74025)
        jets = model.unpack(.2*rng.normal(size=1200))
        analytic = model.connection_second(self.prepared, self.point, jets)["second"]
        direction = np.array([.4, -.2, .7, .3])
        direction /= np.linalg.norm(direction)

        def raw_connection(t):
            x = t*direction
            e = np.eye(4)+np.einsum("r,s,rsam->am", x, x, self.point["coframe_second"])/2
            e += np.einsum("r,s,t,rstam->am", x, x, x, jets["e3"])/6
            de = np.einsum("s,rsam->ram", x, self.point["coframe_second"])
            de += np.einsum("s,t,rstam->ram", x, x, jets["e3"])/2
            psi = self.prepared["data"]["psi"]+np.einsum("r,rij->ij", x, self.point["psi_first"])
            psi += np.einsum("r,s,rsij->ij", x, x, jets["p2"])/2
            multiplier = self.point["multiplier"]+np.einsum("r,ram->am", x, self.point["multiplier_first"])
            multiplier += np.einsum("r,s,rsam->am", x, x, jets["l2"])/2
            response, source = parent.spin_maps(e, psi)
            hessian = parent.contorsion_hessian(e)
            k = np.linalg.solve(hessian, -source+response.T @ multiplier.reshape(-1))
            return model.prolong.dirac.bundle(e, de)["omega"]+parent.unpack(k)

        expected = np.einsum("r,s,rsmab->mab", direction, direction, analytic)
        origin = raw_connection(0.)
        errors = []
        for step in (4e-4, 2e-4):
            observed = (raw_connection(step)-2*origin+raw_connection(-step))/step**2
            errors.append(np.linalg.norm(observed-expected))
        self.assertLess(errors[1], 1e-5)
        self.assertLess(errors[1], .4*errors[0])

    def test_metric_curvature_match_does_not_identify_sourced_cartan_curvature(self):
        connection = self.result["connection"]["omega"]
        zero_first = np.zeros((4, 4, 4))
        bundle = model.prolong.dirac.bundle(np.eye(4), zero_first, self.point["coframe_second"])
        psi = self.prepared["data"]["psi"]
        cross = model.odd.channels(psi, parent.covariant_jet(psi, self.point["psi_first"], connection))["odd"]
        cross_bundle = model.prolong.dirac.bundle(
            cross, self.result["constraint_first"],
            self.point["coframe_second"]+self.result["constraint_second"])
        self.assertLess(np.linalg.norm(cross_bundle["curvature"]["riemann"]
                                       -bundle["curvature"]["riemann"]), 1e-8)
        lc_first = np.array([model.prolong.normal_lorentz(v) for v in self.point["coframe_second"]])
        lc_curvature = parent.curvature_upper(bundle["omega"], lc_first)
        self.assertGreater(np.linalg.norm(parent.torsion(np.eye(4), zero_first, connection)), 1.)
        self.assertGreater(np.linalg.norm(self.result["curvature"]-lc_curvature), 1.)
        cartan_scalar = np.einsum("mnmn", self.result["curvature"])
        self.assertGreater(abs(cartan_scalar-bundle["curvature"]["scalar"]), 1.)

    def test_fifty_two_conditional_relations_hold_on_unfitted_higher_jets(self):
        rows = model.noether_dependencies(self.prepared, self.point)
        self.assertEqual(rows.shape, (52, 384))
        for block, expected_rank in ((rows[:24], 24), (rows[24:48], 24),
                                     (rows[48:], 4), (rows, 52)):
            self.assertEqual(np.linalg.matrix_rank(block, tol=1e-10), expected_rank)
        rng = np.random.default_rng(74024)
        for sample in range(3):
            with self.subTest(sample=sample):
                result = model.equations(self.prepared, self.point, model.unpack(.2*rng.normal(size=1200)))
                f1, r1, fe1 = (result[k] for k in ("constraint_first", "probe_first", "coframe_Euler_first"))
                direct = [f1[r, a, s]-f1[s, a, r]
                          for r, s in itertools.combinations(range(4), 2) for a in range(4)]
                for r in range(4):
                    for generator in lorentz_generators():
                        spinor_delta = (spin_generator(generator) @ self.prepared["data"]["psi"].T).T
                        direct.append(np.sum(fe1[r]*generator)
                                      +2*np.vdot(spinor_delta.reshape(-1), r1[r]).real
                                      +np.sum(f1[r]*(generator.T @ self.point["multiplier"])))
                for nu in range(4):
                    direct.append(sum(fe1[mu, nu, mu] for mu in range(4))
                                  +sum(self.point["multiplier"][a, mu]*(f1[mu, a, nu]-f1[nu, a, mu])
                                       for a, mu in np.ndindex((4, 4))))
                self.assertGreater(np.linalg.norm(result["vector"]), 10.)
                np.testing.assert_allclose(rows @ result["vector"], direct, atol=1e-10, rtol=1e-8)
                self.assertLess(np.linalg.norm(direct), 2e-9)


if __name__ == "__main__":
    unittest.main()
