"""Conditional propagation: projections, lower terms and exact energy balance."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "gravitational_subsidiary", ROOT / "analysis/HC_Cartan_Gravitational_Subsidiary.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


def adm_geometry(bg):
    h, dh, gi = bg["metric"][1:, 1:], bg["metric_first"][:, 1:, 1:], bg["spatial_inverse"]
    n, beta, dbeta = bg["lapse"], bg["shift"], bg["shift_first"]
    lie = np.einsum("k,kij->ij", beta, dh[1:])+dbeta[1:] @ h+h @ dbeta[1:].T
    k = -(dh[0]-lie)/(2*n)
    spatial_connection = np.empty((3, 3, 3))
    for a, i, j in np.ndindex((3, 3, 3)):
        spatial_connection[a, i, j] = sum(gi[a, b]*(dh[i+1, b, j]+dh[j+1, b, i]-dh[b+1, i, j])
                                            for b in range(3))/2
    return k, np.sum(gi*k), spatial_connection


class GravitationalSubsidiaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Gravitational_Subsidiary.json").read_text(encoding="utf-8"))
        rng = np.random.default_rng(41031)
        cls.backgrounds = [model.background(np.eye(4)+rng.normal(size=(4, 4))*.1,
                                            rng.normal(size=(4, 4, 4))*.2) for _ in range(6)]

    def test_source_fingerprints_remain_current(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_naive_evolution_has_a_nondiagonalizable_nilpotent_symbol(self):
        matrix = model.naive_symbol([1, 2, 3])
        self.assertEqual(np.linalg.matrix_rank(matrix), 1)
        np.testing.assert_array_equal(matrix @ matrix, 0)
        np.testing.assert_array_equal(np.linalg.eigvals(matrix), 0)
        self.assertEqual(4-np.linalg.matrix_rank(matrix), 3)

    def test_flat_positive_evolution_has_symmetric_wave_principal_part(self):
        bg = model.background(np.eye(4), np.zeros((4, 4, 4)))
        for i in range(3):
            expected = np.zeros((4, 4))
            expected[0, i+1] = expected[i+1, 0] = 1
            np.testing.assert_array_equal(bg["principal"][i], expected)
        np.testing.assert_array_equal(bg["lower_order"], 0)

    def test_trace_reversal_uses_spatial_projection_not_raw_upper_indices(self):
        e = np.eye(4)
        e[0, 0], e[1:, 0] = 1.1, [.2, -.1, .3]
        bg = model.background(e, np.zeros((4, 4, 4)))
        value = np.array([1., .2, .3, -.4])
        tensor = np.einsum("b,bmn->mn", value, bg["basis"])
        trace = np.sum(bg["metric"]*tensor)
        q = tensor-.5*bg["inverse_metric"]*trace
        lower = bg["metric"] @ q @ bg["metric"]
        np.testing.assert_allclose(lower[1:, 1:], 0, atol=1e-13)
        self.assertGreater(np.linalg.norm(q[1:, 1:]), .1)
        n_covector = bg["metric"] @ bg["normal"]
        self.assertAlmostEqual(n_covector @ tensor @ n_covector, value[0])
        np.testing.assert_allclose(-bg["metric"][1:] @ tensor @ n_covector, value[1:], atol=1e-13)

    def test_positive_symmetrizer_and_real_characteristic_speeds(self):
        q = np.array([.2, -.4, .7])
        for bg in self.backgrounds:
            self.assertGreater(np.linalg.eigvalsh(bg["symmetrizer"])[0], 0)
            matrix = np.einsum("i,iab->ab", q, bg["principal"])
            sym = bg["symmetrizer"] @ matrix
            np.testing.assert_allclose(sym, sym.T, atol=1e-12)
            speed = bg["lapse"]*np.sqrt(q @ bg["spatial_inverse"] @ q)
            expected = -bg["shift"] @ q+np.array([-speed, 0, 0, speed])
            np.testing.assert_allclose(np.sort(np.linalg.eigvals(matrix).real), expected, atol=1e-12)

    def test_full_projected_divergence_matches_all_principal_and_lower_terms(self):
        rng = np.random.default_rng(3105)
        for bg in self.backgrounds:
            value, first = rng.normal(size=4), rng.normal(size=(4, 4))
            expected = first[0]+np.einsum("iab,ib->a", bg["principal"], first[1:])+bg["lower_order"] @ value
            np.testing.assert_allclose(model.projected_divergence(bg, value, first), expected, atol=2e-12)

    def test_decomposition_derivatives_match_independent_metric_differences(self):
        rng = np.random.default_rng(3106)
        e, de = np.eye(4)+rng.normal(size=(4, 4))*.1, rng.normal(size=(4, 4, 4))*.1
        bg = model.background(e, de)
        for r in range(4):
            plus, minus = model.background(e+1e-5*de[r], de), model.background(e-1e-5*de[r], de)
            np.testing.assert_allclose((plus["basis"]-minus["basis"])/(2e-5), bg["basis_first"][r], atol=2e-10)

    def test_lower_order_terms_match_the_independent_ADM_formula(self):
        for bg in self.backgrounds:
            k, trk, connection = adm_geometry(bg)
            n, dn, gi = bg["lapse"], bg["lapse_first"][1:], bg["spatial_inverse"]
            expected = np.zeros((4, 4))
            expected[0, 0] = -2*n*trk
            expected[0, 1:] = -n*np.einsum("ij,kij->k", gi, connection)+2*gi @ dn
            expected[1:, 0] = 2*dn
            expected[1:, 1:] = -bg["shift_first"][1:]-n*trk*np.eye(3)
            np.testing.assert_allclose(bg["lower_order"], expected, atol=2e-12)

    def test_exact_local_energy_balance_includes_acceleration_and_shift(self):
        rng = np.random.default_rng(3108)
        for bg in self.backgrounds:
            h, gi, dgi = bg["metric"][1:, 1:], bg["spatial_inverse"], bg["spatial_inverse_first"]
            n, dn, beta, dbeta = bg["lapse"], bg["lapse_first"], bg["shift"], bg["shift_first"]
            k, trk, _ = adm_geometry(bg)
            value, gradients = rng.normal(size=4), rng.normal(size=(3, 4))
            time = -np.einsum("iab,ib->a", bg["principal"], gradients)-bg["lower_order"] @ value
            scalar, momentum = value[0], value[1:]
            up = gi @ momentum
            energy = .5*(scalar*scalar+momentum @ up)
            v = np.sqrt(np.linalg.det(h))
            dv = .5*v*np.einsum("ij,rij->r", gi, bg["metric_first"][:, 1:, 1:])
            et = scalar*time[0]+up @ time[1:]+.5*momentum @ dgi[0] @ momentum
            lhs = dv[0]*energy+v*et
            for i in range(3):
                de = scalar*gradients[i, 0]+up @ gradients[i, 1:]+.5*momentum @ dgi[i+1] @ momentum
                dup = dgi[i+1, i] @ momentum+gi[i] @ gradients[i, 1:]
                lhs += (dv[i+1]*(n*scalar*up[i]-beta[i]*energy)
                        +v*(dn[i+1]*scalar*up[i]+n*gradients[i, 0]*up[i]+n*scalar*dup
                            -dbeta[i+1, i]*energy-beta[i]*de))
            rhs = v*(1.5*n*trk*scalar**2+.5*n*trk*(momentum @ up)
                     +n*(up @ k @ up)-3*scalar*(up @ dn[1:]))
            self.assertAlmostEqual(lhs, rhs, places=11)

    def test_uniform_positive_symmetrizer_bounds_hold_on_the_saved_ball(self):
        for sample in self.report["sample_checks_not_the_proof"]:
            self.assertGreaterEqual(sample["symmetrizer_minimum_eigenvalue"], self.report["uniform_symmetrizer_lower_bound"]-1e-12)
            self.assertLessEqual(sample["symmetrizer_maximum_eigenvalue"], self.report["uniform_symmetrizer_upper_bound"]+1e-12)
            self.assertLess(sample["principal_symmetry_error"], 1e-12)

    def test_zero_subsidiary_data_remain_homogeneous(self):
        for bg in self.backgrounds:
            np.testing.assert_array_equal(model.projected_divergence(bg, np.zeros(4), np.zeros((4, 4))), 0)

    def test_timelike_coordinate_conormal_is_required(self):
        e = np.eye(4)[[1, 0, 2, 3]]
        with self.assertRaises(ValueError):
            model.background(e, np.zeros((4, 4, 4)))

    def test_open_set_matter_assumptions_are_not_claimed_solved(self):
        self.assertIn("R=0 and F=C-E=0 throughout an open set", self.report["assumptions"])
        self.assertTrue(self.report["R_F_propagation_not_established"])
        self.assertTrue(self.report["full_coupled_hyperbolicity_not_established"])
        self.assertTrue(self.report["finite_Taylor_fields_not_on_shell_on_the_ball"])
        self.assertTrue(self.report["not_interval_certified"])


if __name__ == "__main__":
    unittest.main()
