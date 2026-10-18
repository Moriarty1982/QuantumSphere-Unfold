"""Full unprojected next-stage residuals and frozen-input integration checks."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "cartan_joint_next", ROOT / "analysis/HC_Cartan_Next_Joint_Completion.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class NextJointCompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.saved, _ = model.third.diagnostic.load_data()
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Next_Joint_Completion.json").read_text(encoding="utf-8"))
        cls.coordinates = np.array(cls.report["jet_coordinates"])
        cls.connection_coordinates = np.array(cls.report["connection_coordinates"])
        cls.p4 = np.array(cls.report["fourth_spinor_real"])
        cls.lc = model.third.lc_cubic(cls.prepared, cls.point)
        cls.residual = model.full_residual(cls.prepared, cls.point, cls.coordinates,
                                           cls.connection_coordinates, cls.p4, cls.lc)

    def test_source_fingerprints_remain_current(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_second_spinor_jet_is_exactly_preserved(self):
        changed = model.regular.unpack(self.coordinates)
        np.testing.assert_array_equal(changed["p2"], self.saved["p2"])

    def test_original_lower_point_equations_remain_solved(self):
        p, q = self.prepared, self.point
        result = model.third.spatial.rank_model.point_equations(
            p, q["psi_first"], q["coframe_second"], q["multiplier"], q["multiplier_first"])
        self.assertLess(np.linalg.norm(result["vector"]), 1e-10)

    def test_all_unprojected_components_are_retained(self):
        self.assertEqual(self.residual["vector"].shape, (1114,))
        self.assertEqual(self.residual["constraint"].shape, (20, 4, 4))
        self.assertEqual(self.residual["probe"].shape, (4, 4, 12))
        self.assertEqual(self.residual["gravity"].shape, (4, 4, 4, 4))
        np.testing.assert_allclose(self.residual["vector"], self.report["all_1114_residual"], atol=1e-7)

    def test_the_prior_394_equations_are_not_traded_away(self):
        self.assertLess(np.linalg.norm(self.residual["old"]), 2e-6)

    def test_full_second_probe_and_gravity_equations(self):
        self.assertLess(np.linalg.norm(self.residual["probe"]), 2e-5)
        self.assertLess(np.linalg.norm(self.residual["gravity"]), 2e-5)

    def test_full_third_constraint_after_spinor_recovery(self):
        self.assertLess(np.linalg.norm(self.residual["constraint"]), 2e-5)
        self.assertLess(np.linalg.norm(self.residual["vector"]), 3e-5)

    def test_projected_system_is_affine_on_the_declared_slice(self):
        self.assertEqual(self.report["matrix_shape"], [974, 1840])
        self.assertLess(self.report["random_affine_error_norm"], 1e-6)
        history = self.report["refinement_residual_history"]
        self.assertLess(history[-1], 2e-5)

    def test_no_convergence_or_physical_identification_claim_is_added(self):
        self.assertFalse(self.report["main_TeX_PDF_changed"])
        self.assertTrue(any("neighborhood bound" in limit for limit in self.report["limitations"]))
        self.assertTrue(any("existence" in limit for limit in self.report["limitations"]))

    def test_actual_displaced_constraint_has_fourth_order_remainder(self):
        jets = model.regular.unpack(self.coordinates)
        e4, l3 = self.connection_coordinates[:560].reshape(35, 4, 4), self.connection_coordinates[560:].reshape(20, 4, 4)
        p4 = np.array([model.prior.complexify(v, (3, 4)) for v in self.p4])
        direction = np.array([.7, -.2, .4, .5])
        direction /= np.linalg.norm(direction)
        norms = [np.linalg.norm(model.third.diagnostic.extended_constraint(
            self.prepared, self.point, jets, h*direction, e4, l3, p4)) for h in (.002, .001, .0005)]
        for coarse, fine in zip(norms[:-1], norms[1:]):
            self.assertGreater(coarse/fine, 14.5)
            self.assertLess(coarse/fine, 17.5)


if __name__ == "__main__":
    unittest.main()
