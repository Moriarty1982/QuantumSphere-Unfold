"""First prolonged Euler laws close only three of the six normal curl responses."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "first_constitutive_closure_test", ROOT / "analysis/HC_Cartan_Constitutive_First_Closure.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class ConstitutiveFirstClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets, _, _ = model.neighborhood.load_data()
        cls.basis, cls.reduced, _, _ = model.normal_basis(cls.prepared, cls.point)
        cls.system = model.assemble(cls.prepared, cls.point, cls.jets, cls.basis)
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Constitutive_First_Closure.json").read_text(encoding="utf-8"))
        cls.gate = model.ward_gate(cls.point["multiplier"])
        cls.changed, cls.higher = model.shifted(cls.point, cls.jets, cls.basis, .01*cls.system["direction"])
        cls.actual = model.regular.equations(cls.prepared, cls.changed, cls.higher)

    def test_current_inputs_and_saved_direction(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        np.testing.assert_allclose(self.report["direction"], self.system["direction"], atol=1e-8)

    def test_exactly_fixed_spinor_first_jet_and_temporal_multiplier_derivative(self):
        np.testing.assert_array_equal(self.changed["psi_first"], self.point["psi_first"])
        np.testing.assert_array_equal(self.changed["multiplier_first"][0, :, 0], self.point["multiplier_first"][0, :, 0])
        np.testing.assert_array_equal(self.changed["multiplier"], self.point["multiplier"])
        np.testing.assert_array_equal(self.higher["p3"], self.jets["p3"])

    def test_normal_restriction_retains_full_22_dimensional_kernel(self):
        self.assertEqual(model.matrix_rank(self.reduced)[0], 6)
        self.assertEqual(self.basis.shape, (56, 22))
        np.testing.assert_allclose(self.basis.T @ self.basis, np.eye(22), atol=1e-12)

    def test_prolonged_matrix_rank_has_a_clear_singular_gap(self):
        self.assertEqual(self.system["matrix"].shape, (212, 742))
        self.assertEqual(self.system["rank"], 175)
        self.assertGreater(self.system["singular"][174], .01)
        self.assertLess(self.system["singular"][175], 1e-9)

    def test_ward_gate_uses_lower_multiplier_without_extra_eta(self):
        np.testing.assert_allclose(self.gate @ self.gate.T, .003*np.eye(3), atol=1e-15)
        x = np.arange(12.).reshape(3, 4)
        np.testing.assert_allclose(self.gate @ x.reshape(-1), x @ self.point["multiplier"][:, 0])

    def test_three_of_six_curl_responses_survive(self):
        before = self.system["curl"][:, :22]
        self.assertEqual(model.matrix_rank(before)[0], 6)
        self.assertEqual(model.matrix_rank(self.gate @ before)[0], 3)
        self.assertEqual(self.system["response_rank"], 3)
        self.assertGreater(self.system["response_singular"][2], .2)
        self.assertLess(self.system["response_singular"][3], 1e-8)

    def test_surviving_response_is_annihilated_by_ward_gate(self):
        self.assertLess(np.linalg.norm(self.gate @ self.system["response"]), 1e-8)
        self.assertLess(np.linalg.norm(self.system["matrix"] @ self.system["direction"]), 1e-8)

    def test_new_witness_retains_all_original_point_equations(self):
        p = self.changed
        lower = model.neighborhood.rank_model.point_equations(
            self.prepared, p["psi_first"], p["coframe_second"], p["multiplier"], p["multiplier_first"])
        self.assertLess(np.linalg.norm(lower["vector"]), 1e-10)

    def test_first_probe_and_gravity_are_now_both_satisfied(self):
        self.assertLess(np.linalg.norm(self.actual["probe_first"]), 1e-8)
        self.assertLess(np.linalg.norm(self.actual["coframe_Euler_first"]), 1e-8)
        c = self.actual["constraint_first"]
        self.assertLess(np.linalg.norm(c[1:]), 1e-8)
        self.assertLess(np.linalg.norm(c[:, :, 0]), 1e-8)
        self.assertGreater(np.linalg.norm(c[0, :, 1:]), .04)

    def test_direct_curl_formula_matches_unprojected_constraint_gradient(self):
        direct = model.spatial.explicit_curl(self.prepared, self.changed)[:3]
        c = self.actual["constraint_first"]
        actual = np.array([c[0, :, i]-c[i, :, 0] for i in range(1, 4)])
        np.testing.assert_allclose(direct, actual, atol=1e-10)
        self.assertLess(np.linalg.norm(self.gate @ actual.reshape(-1)), 1e-10)

    def test_differentiated_lorentz_gates_add_no_row_on_spatial_time_defects(self):
        c = self.actual["constraint_first"]
        generators = model.regular.coframe_normal_gauge_basis()[:16, 4:].T.reshape(6, 4, 4)
        for generator in generators:
            contraction = np.einsum("ram,am->r", c, generator.T @ self.point["multiplier"])
            self.assertLess(np.linalg.norm(contraction), 1e-10)

    def test_random_affine_superposition_is_not_a_linearized_only_fit(self):
        vector = np.random.default_rng(6821).normal(size=742)*.003
        actual = model.residual(self.prepared, *model.shifted(self.point, self.jets, self.basis, vector))
        np.testing.assert_allclose(actual, self.system["base"]+self.system["matrix"] @ vector, atol=2e-9)

    def test_signed_and_double_amplitude_controls(self):
        values = []
        for amplitude in (0., .01, -.01, .02):
            p, higher = model.shifted(self.point, self.jets, self.basis, amplitude*self.system["direction"])
            c = model.regular.equations(self.prepared, p, higher)["constraint_first"]
            values.append(c[0, :, 1:])
            self.assertLess(np.linalg.norm(model.residual(self.prepared, p, higher)), 1e-8)
        np.testing.assert_allclose(values[1]-values[0], -(values[2]-values[0]), atol=1e-9)
        np.testing.assert_allclose(values[3]-values[0], 2*(values[1]-values[0]), atol=1e-9)

    def test_unimposed_second_constitutive_derivatives_are_not_hidden(self):
        self.assertGreater(np.linalg.norm(self.actual["constraint_second"]), .5)
        self.assertTrue(self.report["not_all_constitutive_derivatives_imposed"])
        self.assertTrue(self.report["not_a_regional_solution_or_full_propagation_disproof"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_actual_fields_give_independent_first_derivative_controls(self):
        values = model.field_difference_checks(self.prepared, self.changed, self.higher)
        # Central field differences have truncation/roundoff error, unlike analytic jets.
        self.assertLess(values[-1]["probe_first_fd_error"], 1e-3)
        self.assertLess(values[-1]["coframe_Euler_first_fd_error"], .01)
        self.assertLess(values[-1]["probe_first_fd_error"], .4*values[0]["probe_first_fd_error"])


if __name__ == "__main__":
    unittest.main()
