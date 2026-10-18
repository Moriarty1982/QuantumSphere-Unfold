"""Coordinate Ward sources, density factors and general coframe first jets."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "coordinate_residual_ward", ROOT / "analysis/HC_Cartan_Diffeomorphism_Residual_Identity.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class CoordinateResidualIdentityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Diffeomorphism_Residual_Identity.json").read_text(encoding="utf-8"))
        cls.fixtures = [model.transformed_fixture(seed) for seed in range(72410, 72416)]

    def test_saved_sources_and_offshell_controls_reproduce(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        for data, saved in zip(self.fixtures, self.report["random_genuine_jet_controls"]):
            np.testing.assert_allclose(model.ward(data), saved["identity"], atol=1e-11)

    def test_full_coordinate_identity_with_generic_nonzero_residuals(self):
        for data in self.fixtures:
            self.assertLess(np.linalg.norm(model.ward(data)), 1e-10)
            self.assertGreater(np.linalg.norm(data["coframe_first"]), .1)
            for key in ("Euler", "probe", "constraint"):
                self.assertGreater(np.linalg.norm(data[key]), .1)

    def test_omitting_each_residual_source_breaks_the_identity(self):
        for key in model.ward_terms(self.fixtures[0]):
            errors = [np.linalg.norm(model.ward(data)-model.ward_terms(data)[key]) for data in self.fixtures]
            self.assertGreater(max(errors), 1e-3)

    def test_constant_coordinate_covariance_also_holds_for_nonzero_ward_defect(self):
        data = model.normal_fixture(72599)
        data["Euler_first"][0, 2, 0] += 3
        jacobian = np.eye(4)+np.random.default_rng(21).normal(size=(4, 4))*.15
        expected = abs(np.linalg.det(jacobian))*jacobian.T @ model.ward(data)
        transformed = model.constant_coordinate_change(data, jacobian)
        np.testing.assert_allclose(model.ward(transformed), expected, atol=1e-11)

    def test_coordinate_density_weight_is_essential(self):
        data = model.normal_fixture(72600)
        h = np.zeros((4, 4, 4))
        h[0, 0, 0] = 1
        transformed = model.local_coordinate_change(data, h)
        self.assertLess(np.linalg.norm(model.ward(transformed)), 1e-10)
        transformed["multiplier_first"][0] -= data["multiplier"]
        self.assertGreater(np.linalg.norm(model.ward(transformed)), 1e-3)

    def test_coordinate_and_lorentz_first_jets_span_all_64_coframe_slots(self):
        data = model.normal_fixture(72601)
        columns = []
        for a in range(4):
            for r, s in model.prior.PAIR2:
                h = np.zeros((4, 4, 4))
                h[r, a, s] = h[s, a, r] = 1
                columns.append(model.local_coordinate_change(data, h)["coframe_first"].reshape(-1))
        for r in range(4):
            for a, b in model.cartan.PAIRS:
                lower = np.zeros((4, 4, 4))
                lower[r, a, b], lower[r, b, a] = 1, -1
                columns.append(model.local_lorentz_change(data, model.cartan.ETA @ lower)["coframe_first"].reshape(-1))
        self.assertEqual(np.linalg.matrix_rank(np.column_stack(columns), tol=1e-10), 64)

    def test_nonintegrable_coordinate_and_nonlorentz_generators_are_rejected(self):
        data = self.fixtures[0]
        h = np.zeros((4, 4, 4))
        h[0, 1, 2] = 1
        with self.assertRaises(ValueError):
            model.local_coordinate_change(data, h)
        with self.assertRaises(ValueError):
            model.local_lorentz_change(data, np.ones((4, 4, 4)))

    def test_source_identity_is_not_labeled_full_propagation(self):
        self.assertTrue(self.report["probe_and_constitutive_sources_not_dropped"])
        self.assertTrue(self.report["not_full_constraint_propagation"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_symmetric_density_bridge_has_no_extra_volume_connection_term(self):
        rng = np.random.default_rng(72603)
        e, de = np.eye(4)+rng.normal(size=(4, 4))*.1, rng.normal(size=(4, 4, 4))*.2
        s, ds = rng.normal(size=(4, 4)), rng.normal(size=(4, 4, 4))
        s, ds = (s+s.T)/2, (ds+ds.swapaxes(1, 2))/2
        fe = model.cartan.ETA @ e @ s
        dfe = model.cartan.ETA @ de @ s+model.cartan.ETA @ e @ ds
        data = {"coframe": e, "coframe_first": de, "Euler": fe, "Euler_first": dfe,
                "multiplier": np.zeros((4, 4)), "multiplier_first": np.zeros((4, 4, 4)),
                "constraint": np.zeros((4, 4)), "constraint_first": np.zeros((4, 4, 4)),
                "psi_first": np.zeros((4, 3, 4), complex), "probe": np.zeros((3, 4), complex)}
        bundle = model.prolong.dirac.bundle(e, de)
        connection, metric = bundle["curvature"]["connection"], bundle["metric"]
        divergence = np.einsum("mmn->n", ds)+np.einsum("nmr,mr->n", connection, s)
        np.testing.assert_allclose(model.ward(data), metric @ divergence, atol=1e-12)
        wrong = divergence+np.einsum("r,rn->n", np.einsum("mmr->r", connection), s)
        self.assertGreater(np.linalg.norm(model.ward(data)-metric @ wrong), .01)


if __name__ == "__main__":
    unittest.main()
