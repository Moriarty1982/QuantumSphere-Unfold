"""Analytic third Cartan jets and bounded C3 re-preparation checks."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "cartan_c3_reprepare", ROOT / "analysis/HC_Cartan_Third_Constraint_Reprepare.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class ThirdConstraintReprepareTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.saved, cls.fingerprint = model.diagnostic.load_data()
        cls.lc = model.lc_cubic(cls.prepared, cls.point)
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Third_Constraint_Reprepare.json").read_text(encoding="utf-8"))

    def test_saved_input_and_coordinate_roundtrip(self):
        self.assertEqual(self.fingerprint, self.report["input_scalar_completion_sha256"])
        reconstructed = model.regular.unpack(model.coordinates(self.saved))
        for key in self.saved:
            np.testing.assert_allclose(reconstructed[key], self.saved[key])

    def test_lc_third_has_derivative_symmetry_and_lorentz_antisymmetry(self):
        np.testing.assert_allclose(self.lc, self.lc.swapaxes(0, 1), atol=1e-10)
        np.testing.assert_allclose(self.lc, self.lc.swapaxes(1, 2), atol=1e-10)
        np.testing.assert_allclose(self.lc, -self.lc.swapaxes(-1, -2), atol=1e-10)

    def test_lc_third_is_quadratic_in_second_coframe(self):
        changed = dict(self.point, coframe_second=2*self.point["coframe_second"])
        np.testing.assert_allclose(model.lc_cubic(self.prepared, changed), 4*self.lc, atol=1e-10)

    def test_bilinear_third_includes_all_repeated_product_terms(self):
        rng = np.random.default_rng(73)
        psi = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
        p1, p2, p3 = np.zeros((4, 3, 4), complex), np.zeros((4, 4, 3, 4), complex), np.zeros((4, 4, 4, 3, 4), complex)
        p1[0], p2[0, 0], p3[0, 0, 0] = 2*psi, 3*psi, 5*psi
        actual = model.bilinear_third(np.eye(4), psi, p1, p2, p3)
        self.assertAlmostEqual(actual[0, 0, 0], (2*5+6*2*3)*np.vdot(psi, psi).real, places=10)

    def test_analytic_C3_matches_independent_prior_differences(self):
        actual = model.constraint_third(self.prepared, self.point, self.saved, self.lc)
        np.testing.assert_allclose(actual, self.report["analytic_frozen_C3"], atol=1e-8)
        self.assertLess(self.report["analytic_versus_prior_FD_C3_norm"], .005)

    def test_cartan_third_equation_is_satisfied(self):
        value = model.connection_third(self.prepared, self.point, self.saved, self.lc)
        residual = np.einsum("pq,rstq->rstp", self.prepared["hessian"], value["k_third"])-value["rhs_third"]
        self.assertLess(np.linalg.norm(residual), 1e-8)

    def test_all_45_new_compatibilities_are_accessible(self):
        solved = self.report["affine_439_system"]
        self.assertEqual(solved["rank"]-solved["old_394_matrix_rank"], 45)
        self.assertLess(solved["random_affine_error_norm"], 1e-7)

    def test_cokernel_annihilates_every_new_jet_column(self):
        maps = model.new_jet_maps(self.prepared)
        self.assertEqual(maps["rank"], 275)
        self.assertEqual(maps["cokernel"].shape, (320, 45))
        np.testing.assert_allclose(maps["cokernel"].T @ maps["full"], 0, atol=1e-10)

    def test_saved_reprepare_keeps_spinor_hessian(self):
        jets = model.regular.unpack(np.array(self.report["affine_439_system"]["jet_coordinates"]))
        np.testing.assert_array_equal(jets["p2"], self.saved["p2"])

    def test_full_unprojected_714_system_is_recomputed(self):
        jets = model.regular.unpack(np.array(self.report["affine_439_system"]["jet_coordinates"]))
        new = self.report["new_jet_completion"]
        conn = np.array(new["connection_coordinates"])
        p4 = np.array(new["fourth_spinor_real"])
        c3 = (model.constraint_third(self.prepared, self.point, jets, self.lc)
              +model.diagnostic.connection_image(self.prepared, conn[:560].reshape(35, 4, 4), conn[560:].reshape(20, 4, 4))
              +model.diagnostic.principal_image(model.spatial.constraint_principal_map(self.prepared["data"]["psi"]), p4))
        old = model.old_equations(self.prepared, self.point, jets)
        self.assertLess(np.linalg.norm(old), 1e-7)
        self.assertLess(np.linalg.norm(np.concatenate((old, c3.reshape(-1)))), 5e-6)
        np.testing.assert_allclose(c3, new["full_C3_residual"], atol=1e-7)

    def test_old_failure_remains_as_a_negative_control(self):
        self.assertGreater(self.report["frozen_unreachable_C3_norm"], 26000)
        self.assertLess(self.report["all_714_residual_norm"], 5e-6)
        self.assertIn("R2 and FE2 NOT imposed", self.report["scope"])


if __name__ == "__main__":
    unittest.main()
