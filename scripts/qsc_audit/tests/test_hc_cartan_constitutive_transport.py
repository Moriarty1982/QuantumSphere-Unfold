"""Exact exterior derivative and honest point-jet propagation controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "constitutive_transport_test", ROOT / "analysis/HC_Cartan_Constitutive_Transport.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class ConstitutiveTransportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        (cls.prepared, cls.point, cls.jets, cls.system,
         cls.direction, cls.singular, cls.rows) = model.witness_data()
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Constitutive_Transport.json").read_text(encoding="utf-8"))

    def fixture(self, seed=1912):
        rng = np.random.default_rng(seed)
        p = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
        p1 = rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4))
        p2 = rng.normal(size=(4, 4, 3, 4))+1j*rng.normal(size=(4, 4, 3, 4))
        p2 = (p2+p2.swapaxes(0, 1))/2
        b = rng.normal(size=(4, 12, 12))+1j*rng.normal(size=(4, 12, 12))
        b1 = rng.normal(size=(4, 4, 12, 12))+1j*rng.normal(size=(4, 4, 12, 12))
        e1 = rng.normal(size=(4, 4, 4))
        return p, p1, p2, b, b1, e1

    def test_fingerprints_and_saved_result(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        for actual, saved in zip(self.rows, self.report["witnesses"]):
            np.testing.assert_allclose(actual["spatial_constraint_time_gradient"],
                                       saved["spatial_constraint_time_gradient"], atol=1e-10)

    def test_generic_product_rule_and_exterior_derivative(self):
        for seed in range(1912, 1918):
            p, p1, p2, b, b1, e1 = self.fixture(seed)
            df = model.gradient(p, p1, p2, b, b1, e1)
            expected = np.array([df[r, :, s]-df[s, :, r] for r, s in model.cartan.PAIRS])
            np.testing.assert_allclose(model.curl(p, p1, b, b1, e1), expected, atol=2e-12)

    def test_gradient_matches_actual_polynomial_fields(self):
        p, p1, p2, b, b1, e1 = self.fixture()
        def field(x):
            psi = p+np.einsum("r,rij->ij", x, p1)+np.einsum("r,s,rsij->ij", x, x, p2)/2
            first = p1+np.einsum("s,rsij->rij", x, p2)
            spin = b+np.einsum("r,rmij->mij", x, b1)
            cov = first.reshape(4, 12)+np.einsum("mij,j->mi", spin, psi.reshape(12))
            return np.einsum("i,aij,mj->am", psi.reshape(12).conj(), model.prolong.Q_WEIGHTS, cov).imag-np.einsum("r,ram->am", x, e1)
        step = 1e-5
        fd = np.array([(field(step*v)-field(-step*v))/(2*step) for v in np.eye(4)])
        np.testing.assert_allclose(fd, model.gradient(p, p1, p2, b, b1, e1), atol=1e-7)

    def test_curvature_rewriting_needs_representation_compatibility_terms(self):
        p, p1, _, b, b1, e1 = self.fixture()
        p, f = p.reshape(12), p1.reshape(4, 12)
        cov = f+np.einsum("mij,j->mi", b, p)
        complete, naive = [], []
        for r, s in model.cartan.PAIRS:
            curvature = b1[r, s]-b1[s, r]+b[r] @ b[s]-b[s] @ b[r]
            row, raw = [], []
            for a in model.prolong.Q_WEIGHTS:
                value = (np.vdot(cov[r], a @ cov[s])-np.vdot(cov[s], a @ cov[r])
                         +np.vdot(p, a @ curvature @ p))
                raw.append(value.imag)
                hr, hs = b[r].conj().T @ a+a @ b[r], b[s].conj().T @ a+a @ b[s]
                row.append((value-np.vdot(p, hr @ cov[s])+np.vdot(p, hs @ cov[r])).imag)
            de = e1[r, :, s]-e1[s, :, r]
            complete.append(np.array(row)-de)
            naive.append(np.array(raw)-de)
        actual = model.curl(p, f, b, b1, e1)
        np.testing.assert_allclose(complete, actual, atol=2e-11)
        self.assertGreater(np.linalg.norm(np.array(naive)-actual), 1.)

    def test_symmetric_hessian_cancels_but_nonholonomic_control_does_not(self):
        p, p1, p2, b, b1, e1 = self.fixture()
        df = model.gradient(p, p1, p2, b, b1, e1)
        modified = p2.copy()
        modified[0, 1] += 1j*p
        changed = model.gradient(p, p1, modified, b, b1, e1)
        self.assertGreater(np.linalg.norm(changed-df), .1)
        defect = np.array([changed[r, :, s]-changed[s, :, r] for r, s in model.cartan.PAIRS])
        self.assertGreater(np.linalg.norm(defect-model.curl(p, p1, b, b1, e1)), .1)

    def test_rank_increase_is_six_not_twelve(self):
        self.assertEqual(self.system["original_rank"], 34)
        self.assertEqual(self.system["rank"], 40)
        self.assertEqual(self.system["induced_rank"], 6)
        self.assertEqual(self.system["left_null"].shape, (12, 6))
        self.assertGreater(self.singular[5], 1e-4)
        self.assertLess(self.singular[6], 1e-9)

    def test_normal_kernel_direction_is_not_a_curl_kernel(self):
        self.assertAlmostEqual(np.linalg.norm(self.direction), 1.)
        self.assertLess(np.linalg.norm(self.system["matrix"][:56] @ self.direction), 1e-10)
        self.assertGreater(np.linalg.norm(self.system["matrix"][56:] @ self.direction), 1.)

    def test_all_point_equations_and_spatial_first_constraints_remain_small(self):
        for row in self.rows:
            self.assertLess(row["point_equations_norm"], 1e-10)
            self.assertLess(row["spatial_constraint_gradient_norm"], 1e-10)
            self.assertLess(row["temporal_column_gradient_norm"], 1e-10)
            self.assertLess(row["independent_gradient_error"], 1e-10)
            self.assertLess(row["transport_identity_error"], 1e-10)

    def test_control_drifts_linearly_with_signed_amplitude(self):
        zero, plus, minus, twice = [np.array(row["spatial_constraint_time_gradient"]) for row in self.rows]
        self.assertLess(np.linalg.norm(zero), 1e-10)
        self.assertGreater(np.linalg.norm(plus), .3)
        np.testing.assert_allclose(plus, -minus, atol=1e-10)
        np.testing.assert_allclose(twice, 2*plus, atol=1e-10)

    def test_fixed_data_are_not_refitted(self):
        changed = model.normal_point(self.point, self.direction, .01)
        np.testing.assert_array_equal(changed["multiplier"], self.point["multiplier"])
        np.testing.assert_array_equal(changed["psi_first"][1:], self.point["psi_first"][1:])
        np.testing.assert_array_equal(changed["multiplier_first"][1:], self.point["multiplier_first"][1:])
        np.testing.assert_array_equal(changed["coframe_second"][1:], self.point["coframe_second"][1:])
        second = model.adapted_hessian(self.prepared, changed, self.jets["p2"])
        np.testing.assert_array_equal(second, second.swapaxes(0, 1))

    def test_control_does_not_satisfy_frozen_first_probe_prolongation(self):
        self.assertLess(self.rows[0]["frozen_higher_first_probe_norm"], 1e-8)
        self.assertGreater(self.rows[1]["frozen_higher_first_probe_norm"], 1e-3)

    def test_claims_remain_pointwise_and_comparison_only(self):
        self.assertTrue(self.report["not_a_solution_of_prolonged_or_open_set_equations"])
        self.assertTrue(self.report["not_a_disproof_of_full_parent_propagation"])
        self.assertFalse(self.report["native_identification_or_full_existence_proved"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
