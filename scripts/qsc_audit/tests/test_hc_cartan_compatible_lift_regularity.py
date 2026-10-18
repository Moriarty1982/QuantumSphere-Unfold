"""Fresh bounds for the shifted compatible jet, not inherited old radii."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "compatible_lift_regularity_test", ROOT / "analysis/HC_Cartan_Compatible_Lift_Regularity.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class CompatibleLiftRegularityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Compatible_Lift_Regularity.json").read_text(encoding="utf-8"))
        cls.prepared, cls.point, cls.jets, cls.unique, cls.full, cls.lift = model.load_data()

    def test_fingerprints_and_actual_origin(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertEqual(self.report["source_values"], self.lift["source_values"])
        self.assertEqual(self.report["origin"], self.lift["final"])
        self.assertLess(self.report["origin"]["all_1114_norm"], 1e-7)

    def test_coefficients_are_recomputed_from_new_jets(self):
        actual = model.temporal.coefficient_norms(self.prepared, self.point, self.jets, self.full)
        self.assertEqual(actual, self.report["coefficient_norms"])
        cartan = model.cartan_regular.coefficient_norms(self.prepared, self.point, self.jets, self.unique)
        self.assertEqual(cartan, self.report["Cartan_coefficient_norms"])
        old = json.loads((ROOT / "analysis/HC_Cartan_Joint_Neighborhood.json").read_text(encoding="utf-8"))
        self.assertNotEqual(actual["coframe_third"], old["coefficient_norms"]["coframe_third"])

    def test_full_fourth_tensor_multiplicity(self):
        unique = np.zeros((35, 4, 4))
        index = model.prior.joint.third.diagnostic.QUADS.index((0, 1, 2, 3))
        unique[index, 0, 0] = 1.
        self.assertAlmostEqual(np.linalg.norm(model.temporal.unpack_fourth(unique)), np.sqrt(24.))
        self.assertEqual(self.full["p4"].shape, (4, 4, 4, 4, 3, 4))
        self.assertAlmostEqual(np.linalg.norm(self.full["e4"]),
                               self.report["coefficient_norms"]["coframe_fourth"])

    def test_common_radius_is_selected_afresh(self):
        temporal = model.temporal.select_radius(self.report["coefficient_norms"])
        cartan = model.cartan_regular.select_radius(self.report["Cartan_coefficient_norms"])
        self.assertEqual(temporal, self.report["selected_temporal_bound"])
        self.assertEqual(cartan, self.report["selected_Cartan_bound"])
        self.assertEqual(self.report["common_radius"], min(temporal["radius"], cartan["radius"]))
        self.assertGreater(self.report["common_radius"], 0.)

    def test_geometric_and_temporal_sample_bounds(self):
        bound = self.report["common_temporal_bound"]
        for sample in self.report["sample_checks_not_the_proof"]:
            for actual, upper in (("coframe_change", "coframe_change_bound"),
                    ("spinor_change", "spinor_change_bound"),
                    ("temporal_multiplier_change", "temporal_multiplier_change_bound"),
                    ("probe_weight_change", "probe_weight_change_bound"),
                    ("constraint_block_change", "constraint_block_change_bound")):
                self.assertLessEqual(sample[actual], bound[upper]+1e-12)
            self.assertGreaterEqual(sample["probe_minimum_eigenvalue"]+1e-12, bound["probe_eigenvalue_lower_bound"])
            self.assertGreaterEqual(sample["constraint_minimum_singular_value"]+1e-12,
                                    bound["constraint_singular_value_lower_bound"])
            self.assertLess(sample["inverse_metric_time_component"], 0.)
            self.assertGreaterEqual(sample["spatial_metric_minimum_eigenvalue"]+1e-12,
                                    bound["spatial_metric_eigenvalue_lower_bound"])

    def test_Cartan_sample_bounds_and_congruence(self):
        bound = self.report["common_Cartan_bound"]
        for sample in self.report["sample_checks_not_the_proof"]:
            self.assertGreaterEqual(sample["Cartan_minimum_singular_value"]+1e-12,
                                    bound["hessian_singular_value_lower_bound"])
            self.assertLessEqual(sample["Cartan_inverse_norm"], bound["hessian_inverse_norm_upper_bound"]+1e-12)
            self.assertLess(sample["Cartan_congruence_error"], 1e-12)
            self.assertLess(sample["Cartan_residual"], 1e-10)

    def test_independent_field_constructors_agree(self):
        self.assertEqual(len(self.report["sample_checks_not_the_proof"]), 17)
        for sample in self.report["sample_checks_not_the_proof"]:
            for key in ("independent_coframe_error", "independent_spinor_error",
                        "independent_multiplier_error", "independent_connection_error"):
                self.assertLess(sample[key], 1e-11)
        x = self.report["common_radius"]*np.array([.5, -.5, .5, -.5])
        direct = model.temporal.fields(self.prepared, self.point, self.jets, self.full, x)
        alternate = model.cartan_regular.fields(self.prepared, self.point, self.jets, self.unique, x)
        np.testing.assert_allclose(direct["omega"], alternate["omega"], atol=1e-12)

    def test_origin_normal_inverse_not_promoted_to_uniform_rank(self):
        normal = model.prior.source.normal.build_reduction(self.prepared, self.point)
        self.assertEqual(normal["rank"], self.report["origin_normal_rank"])
        self.assertEqual(normal["rank"], 40)
        self.assertAlmostEqual(np.linalg.norm(normal["inverse"], 2), self.report["origin_normal_inverse_norm"])
        self.assertTrue(self.report["not_uniform_full_normal_rank_or_PDE_hyperbolicity"])

    def test_regular_fields_are_not_claimed_as_neighborhood_solution(self):
        self.assertTrue(self.report["not_neighborhood_solution_or_Cauchy_existence"])
        self.assertTrue(self.report["not_interval_certified"])
        self.assertTrue(self.report["no_physical_length_units"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])
        self.assertGreater(max(s["probe_residual"] for s in self.report["sample_checks_not_the_proof"]), 1e-9)

    def test_bounds_also_hold_on_smaller_balls(self):
        for factor in (0., .125, .5, 1.):
            radius = factor*self.report["common_radius"]
            temporal = model.temporal.bound(self.report["coefficient_norms"], radius)
            cartan = model.cartan_regular.bound(self.report["Cartan_coefficient_norms"], radius)
            self.assertTrue(temporal["resolved"])
            self.assertTrue(cartan["resolved"])
            self.assertGreater(temporal["coordinate_time_timelike_margin"], 0.)
            self.assertGreater(cartan["hessian_singular_value_lower_bound"], 0.)


if __name__ == "__main__":
    unittest.main()
