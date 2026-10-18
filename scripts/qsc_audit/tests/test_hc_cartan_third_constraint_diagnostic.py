"""Principal symmetry, Cartan response and frozen third-constraint controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "cartan_third_constraint", ROOT / "analysis/HC_Cartan_Third_Constraint_Diagnostic.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class ThirdConstraintDiagnosticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets, cls.fingerprint = model.load_data()
        cls.principal = model.scalar.spatial.constraint_principal_map(cls.prepared["data"]["psi"])
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Third_Constraint_Diagnostic.json").read_text(encoding="utf-8"))
        cls.source = np.array(cls.report["frozen_source"])

    def test_input_matches_strongest_saved_jet(self):
        self.assertEqual(self.fingerprint, self.report["source_json_sha256"])

    def test_group_partition_covers_each_output_slot_once(self):
        slots = [row for group in model.groups() for row in group]
        self.assertEqual(len(slots), 80)
        self.assertEqual(len(set(slots)), 80)

    def test_fourth_derivative_image_dimension(self):
        self.assertEqual(len(model.QUADS)*4, 140)
        self.assertEqual(np.linalg.matrix_rank(self.principal, tol=1e-10), 4)

    def test_compatibility_count_excludes_redundant_curls(self):
        self.assertEqual(sum(len(g)-1 for g in model.groups())*4, 180)
        self.assertEqual(model.compatibility(self.source).shape, (180,))

    def test_projection_is_idempotent_and_orthogonal(self):
        image, rest, _ = model.project(self.source)
        np.testing.assert_allclose(model.project(image)[0], image, atol=1e-10)
        self.assertLess(abs(np.vdot(image, rest))/(np.linalg.norm(image)*np.linalg.norm(rest)), 1e-12)

    def test_all_principal_images_obey_all_compatibilities(self):
        fourth = np.random.default_rng(813).normal(size=(35, 24))
        image = model.principal_image(self.principal, fourth)
        np.testing.assert_allclose(model.compatibility(image), 0, atol=1e-13)

    def test_spinor_completion_is_the_minimum_residual(self):
        _, residual = model.spinor_only_completion(self.source, self.principal)
        np.testing.assert_allclose(residual, model.project(self.source)[1], atol=1e-8)

    def test_invalid_shapes_and_steps_are_rejected(self):
        with self.assertRaises(ValueError):
            model.project(np.zeros((4, 4)))
        with self.assertRaises(ValueError):
            model.principal_image(self.principal, np.zeros((24, 35)))
        with self.assertRaises(ValueError):
            model.third_difference(lambda x: x, 0)
        with self.assertRaises(ValueError):
            model.spinor_only_completion(self.source, np.zeros((4, 24)))

    def test_third_difference_includes_repeated_indices(self):
        result = model.third_difference(lambda x: np.array([x[0]**3+2*x[0]*x[1]*x[2], x[3]**2]), .125)
        expected = np.zeros((20, 2))
        expected[model.TRIPLES.index((0, 0, 0)), 0] = 6
        expected[model.TRIPLES.index((0, 1, 2)), 0] = 2
        np.testing.assert_allclose(result, expected, atol=1e-12)

    def test_unique_taylor_coordinates_include_correct_factorials(self):
        values = np.zeros((35, 1))
        values[model.QUADS.index((0, 0, 1, 1)), 0] = 12
        x = np.array([2., 3., 0., 0.])
        np.testing.assert_allclose(model.homogeneous_jet(values, 4, x), [108])
        np.testing.assert_allclose(model.homogeneous_jet(values, 4, x, (0, 1)), [72])

    def test_zero_new_connection_jets_give_zero_response(self):
        np.testing.assert_allclose(model.connection_image(self.prepared, np.zeros((35, 4, 4)),
                                                       np.zeros((20, 4, 4))), 0)

    def test_random_highest_response_has_independent_field_control(self):
        check = model.independent_response_check(self.prepared, self.point, self.jets, self.principal)
        self.assertGreater(check["analytic_norm"], 1.)
        self.assertLess(check["richardson_error_norm"], 2e-3)
        self.assertLess(check["fine_error_norm"], check["coarse_error_norm"])

    def test_recorded_source_differences_have_second_order_convergence(self):
        coarse, fine = self.report["raw_successive_differences"]
        self.assertGreater(coarse/fine, 3.8)
        self.assertLess(coarse/fine, 4.2)

    def test_new_coframe_multiplier_residual_is_recomputed_unprojected(self):
        saved = self.report["new_connection_jet_completion"]
        x = np.array(saved["connection_coordinates"])
        p4 = np.array(saved["fourth_spinor_real"])
        residual = (self.source+model.connection_image(self.prepared, x[:560].reshape(35, 4, 4),
                                                      x[560:].reshape(20, 4, 4))
                    +model.principal_image(self.principal, p4))
        np.testing.assert_allclose(residual, saved["residual"], atol=1e-7)
        self.assertAlmostEqual(np.linalg.norm(residual), saved["full_constraint_residual_norm"], places=6)

    def test_frozen_obstruction_is_large_relative_to_difference_control(self):
        remainder = self.report["new_connection_jet_completion"]["full_constraint_residual_norm"]
        self.assertGreater(remainder, 10000)
        self.assertGreater(remainder/self.report["richardson_difference_norm_not_certified_error_bound"], 1e6)

    def test_scope_does_not_claim_full_extension(self):
        self.assertIn("NOT", self.report["new_connection_jet_completion"]["scope"])
        self.assertIn("Joint R2, FE2, C3 compatibility remains open", self.report["unresolved"])

    def test_numerical_projected_rank_has_a_large_singular_gap(self):
        solved = self.report["new_connection_jet_completion"]
        self.assertEqual(solved["quotient_rank"], 135)
        self.assertEqual(solved["coframe_only_quotient_rank"], 95)
        self.assertEqual(solved["multiplier_only_quotient_rank"], 125)
        singular = solved["singular_values"]
        self.assertGreater(singular[134], 4.)
        self.assertLess(singular[135], 1e-10)

    def test_saved_c3_fit_is_reproducible(self):
        computed = model.connection_completion(self.prepared, self.source, self.principal)
        saved = self.report["new_connection_jet_completion"]
        self.assertEqual(computed["quotient_rank"], saved["quotient_rank"])
        self.assertAlmostEqual(computed["full_constraint_residual_norm"], saved["full_constraint_residual_norm"], places=5)


if __name__ == "__main__":
    unittest.main()
