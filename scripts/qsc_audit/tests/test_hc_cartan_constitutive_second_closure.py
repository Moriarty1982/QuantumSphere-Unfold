"""Full C2 compatibility and the next necessary coordinate Ward gate."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "second_constitutive_closure_test", ROOT / "analysis/HC_Cartan_Constitutive_Second_Closure.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class ConstitutiveSecondClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets, _, _ = model.neighborhood.load_data()
        cls.basis, _, _, _ = model.first.normal_basis(cls.prepared, cls.point)
        cls.system = model.assemble(cls.prepared, cls.point, cls.jets, cls.basis)
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Constitutive_Second_Closure.json").read_text(encoding="utf-8"))
        cls.changed, cls.higher = model.shifted(cls.point, cls.jets, cls.basis, .01*cls.system["direction"])
        cls.actual = model.regular.equations(cls.prepared, cls.changed, cls.higher)

    def test_fingerprints_and_stored_witness(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        np.testing.assert_allclose(self.report["direction"], self.system["direction"], atol=1e-8)

    def test_declared_lower_inputs_are_exactly_fixed(self):
        np.testing.assert_array_equal(self.changed["psi_first"], self.point["psi_first"])
        np.testing.assert_array_equal(self.changed["multiplier"], self.point["multiplier"])
        np.testing.assert_array_equal(self.changed["multiplier_first"][1:], self.point["multiplier_first"][1:])
        np.testing.assert_array_equal(self.changed["multiplier_first"][0, :, 0], self.point["multiplier_first"][0, :, 0])
        np.testing.assert_array_equal(self.changed["coframe_second"][1:], self.point["coframe_second"][1:])

    def test_enlarged_rank_has_a_resolved_singular_gap(self):
        self.assertEqual(self.system["matrix"].shape, (372, 1222))
        self.assertEqual(self.system["rank"], 335)
        self.assertGreater(self.system["singular"][334], .008)
        self.assertLess(self.system["singular"][335], 1e-9)

    def test_three_mixed_responses_survive_C2_alone(self):
        self.assertEqual(self.system["response_rank"], 3)
        self.assertGreater(self.system["response_singular"][2], .14)
        self.assertLess(self.system["response_singular"][3], 1e-8)

    def test_all_second_constitutive_components_are_recomputed_unprojected(self):
        c2 = self.actual["constraint_second"]
        self.assertLess(np.linalg.norm(c2), 1e-8)
        np.testing.assert_allclose(c2, c2.swapaxes(0, 1), atol=1e-10)
        self.assertGreater(np.linalg.norm(self.actual["constraint_first"][0, :, 1:]), .006)

    def test_all_imposed_point_and_first_equations_still_hold(self):
        p = self.changed
        lower = model.neighborhood.rank_model.point_equations(
            self.prepared, p["psi_first"], p["coframe_second"], p["multiplier"], p["multiplier_first"])
        self.assertLess(np.linalg.norm(lower["vector"]), 1e-10)
        self.assertLess(np.linalg.norm(self.actual["constraint_first"][1:]), 1e-8)
        self.assertLess(np.linalg.norm(self.actual["constraint_first"][:, :, 0]), 1e-8)
        self.assertLess(np.linalg.norm(self.actual["probe_first"]), 1e-8)
        self.assertLess(np.linalg.norm(self.actual["coframe_Euler_first"]), 1e-8)

    def test_direct_product_rule_reproduces_the_surviving_curl(self):
        c = self.actual["constraint_first"]
        mixed = np.array([c[0, :, i]-c[i, :, 0] for i in range(1, 4)])
        np.testing.assert_allclose(mixed, model.spatial.explicit_curl(self.prepared, self.changed)[:3], atol=1e-10)

    def test_finite_random_superposition_remains_affine(self):
        vector = np.random.default_rng(42782).normal(size=1222)*.003
        actual = model.residual(self.prepared, *model.shifted(self.point, self.jets, self.basis, vector))
        np.testing.assert_allclose(actual, self.system["base"]+self.system["matrix"] @ vector, atol=3e-9)

    def test_signed_and_doubled_amplitude_controls(self):
        values = []
        for amplitude in (0., .01, -.01, .02):
            p, jets = model.shifted(self.point, self.jets, self.basis, amplitude*self.system["direction"])
            result = model.regular.equations(self.prepared, p, jets)
            values.append(result["constraint_first"][0, :, 1:])
            self.assertLess(np.linalg.norm(model.residual(self.prepared, p, jets)), 1e-8)
        np.testing.assert_allclose(values[1]-values[0], -(values[2]-values[0]), atol=1e-9)
        np.testing.assert_allclose(values[3]-values[0], 2*(values[1]-values[0]), atol=1e-9)

    def test_complete_multiplier_gate_is_numerically_invertible(self):
        matrix = model.multiplier_gate(self.point)
        np.testing.assert_array_equal(matrix[0], self.point["multiplier"][:, 0])
        np.testing.assert_array_equal(matrix[1:], self.point["multiplier_first"][1:, :, 0])
        singular = np.linalg.svd(matrix, compute_uv=False)
        self.assertGreater(singular[-1], .0086)
        self.assertEqual(np.linalg.matrix_rank(np.kron(np.eye(3), matrix), tol=1e-9), 12)
        self.assertEqual(self.report["spatial_multiplier_gate_rank_on_remaining_defects"], 3)

    def test_homogeneous_complete_gate_forces_zero_defect(self):
        matrix = model.multiplier_gate(self.point)
        rng = np.random.default_rng(7124)
        for _ in range(5):
            defect = rng.normal(size=(4, 3))
            source = matrix @ defect
            np.testing.assert_allclose(np.linalg.solve(matrix, source), defect, atol=1e-12)
            self.assertGreaterEqual(np.linalg.norm(source), .0086*np.linalg.norm(defect))
        np.testing.assert_array_equal(np.linalg.solve(matrix, np.zeros((4, 3))), np.zeros((4, 3)))

    def test_witness_forces_nonzero_second_gravity_divergences(self):
        terms = model.differentiated_ward_terms(self.prepared, self.changed, self.higher)
        self.assertLess(np.linalg.norm(sum(terms.values())), 1e-8)
        c = self.actual["constraint_first"]
        mixed = np.array([c[0, :, i]-c[i, :, 0] for i in range(1, 4)])
        source = self.changed["multiplier_first"][1:, :, 0] @ mixed.T
        self.assertGreater(np.linalg.norm(source), .004)
        np.testing.assert_allclose(terms["Euler_second_divergence"][1:, 1:], -source, atol=1e-8)

    def test_full_differentiated_identity_retains_every_off_shell_source(self):
        rng = np.random.default_rng(4613)
        psi = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
        p1 = .3*(rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4)))
        prepared = model.prolong.prepare({"psi": psi, "first": p1, "omega": np.zeros((4, 4, 4))})
        point = {"psi_first": p1, "multiplier": rng.normal(size=(4, 4))*.2,
                 "multiplier_first": rng.normal(size=(4, 4, 4))*.3,
                 "coframe_second": model.prior.unpack_second(rng.normal(size=160)*.2)}
        jets = model.regular.unpack(rng.normal(size=1200)*.2)
        terms = model.differentiated_ward_terms(prepared, point, jets)
        total = sum(terms.values())
        self.assertLess(np.linalg.norm(total), 1e-8)
        for value in terms.values():
            self.assertGreater(np.linalg.norm(total-value), 1e-4)

    def test_fourth_coframe_and_third_multiplier_jets_cannot_cancel_the_gate(self):
        gravity = model.neighborhood.joint.gravity
        base = gravity.coframe_euler_second(self.prepared, self.changed, self.higher)
        rng = np.random.default_rng(3117)
        changed = gravity.coframe_euler_second(
            self.prepared, self.changed, self.higher,
            e4=rng.normal(size=(35, 4, 4)), l3=rng.normal(size=(20, 4, 4)))
        difference = changed-base
        self.assertGreater(np.linalg.norm(difference), 1.)
        divergence = np.array([[sum(difference[j, mu, i, mu] for mu in range(4))
                                for i in range(1, 4)] for j in range(1, 4)])
        self.assertLess(np.linalg.norm(divergence), 1e-8)

    def test_actual_second_field_differences_converge_with_reported_error(self):
        checks = model.second_field_checks(self.prepared, self.changed, self.higher)
        errors = [v["full_symmetric_second_constitutive_fd_error"] for v in checks["steps"]]
        self.assertLess(errors[1], .3*errors[0])
        self.assertLess(errors[2], .3*errors[1])
        self.assertLess(checks["richardson_error"], .0002)

    def test_invalid_coordinate_arrays_are_rejected(self):
        for bad in (np.zeros(1221), np.full(1222, np.nan)):
            with self.assertRaises(ValueError):
                model.shifted(self.point, self.jets, self.basis, bad)

    def test_claims_remain_finite_order_and_comparison_only(self):
        self.assertTrue(self.report["mixed_first_curls_not_imposed"])
        self.assertTrue(self.report["second_probe_and_second_gravity_not_imposed"])
        self.assertTrue(self.report["not_a_regional_solution_or_full_propagation_disproof"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
