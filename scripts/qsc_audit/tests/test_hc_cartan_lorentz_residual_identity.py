"""Focused off-shell Cartan-eliminated Lorentz residual regressions."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "hc_lorentz_residual", ROOT / "analysis/HC_Cartan_Lorentz_Residual_Identity.py")
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


class LorentzResidualIdentityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.samples = []
        for seed in (74181, 74182, 74183):
            data = audit.fixture(seed)
            fields = audit.pulled_fields(data)
            cls.samples.append((data, fields, audit.residuals(fields)))

    def test_all_six_generators_full_off_shell_identity(self):
        for data, fields, result in self.samples:
            terms = audit.identity_terms(fields, result)
            for index, j in enumerate(audit.generators()):
                with self.subTest(seed=data["seed"], generator=index):
                    np.testing.assert_allclose(j.T @ audit.parent.ETA+audit.parent.ETA @ j, 0, atol=1e-15)
                    self.assertLess(abs(terms[index].sum()), 2e-11)

    def test_saved_report_pins_normalized_local_source_inputs(self):
        report = json.loads((ROOT / "analysis/HC_Cartan_Lorentz_Residual_Identity.json").read_text(encoding="utf-8"))
        self.assertEqual(report["input_sha256"], audit.input_fingerprints())

    def test_unfitted_source_values_and_genuinely_off_shell_residuals(self):
        for _, fields, result in self.samples:
            self.assertGreater(np.linalg.norm(fields["coframe"]-np.eye(4)), .1)
            for key in ("coframe_first", "psi_first", "multiplier", "multiplier_first"):
                self.assertGreater(np.linalg.norm(fields[key]), .1)
            for key in ("F", "R", "FE", "curvature"):
                self.assertGreater(np.linalg.norm(result[key]), .1)
            self.assertGreater(np.linalg.norm(result["R"].real), .1)
            self.assertGreater(np.linalg.norm(result["R"].imag), .1)
            np.testing.assert_allclose(result["Cartan"], 0, atol=2e-12)
            direct_f = audit.regular.odd.channels(fields["psi"], audit.parent.covariant_jet(
                fields["psi"], fields["psi_first"], fields["omega"]))["odd"]-fields["coframe"]
            np.testing.assert_allclose(result["F"], direct_f, atol=1e-14)

    def test_each_generator_detects_wrong_signs_and_omissions(self):
        for data, fields, result in self.samples:
            terms = audit.identity_terms(fields, result)
            for index in range(6):
                with self.subTest(seed=data["seed"], generator=index):
                    for column in range(3):
                        wrong = terms[index].copy()
                        wrong[column] *= -1
                        self.assertGreater(abs(wrong.sum()), 1e-4)
                        self.assertGreater(abs(terms[index].sum()-terms[index, column]), 1e-4)

    def test_full_complex_real_operator_is_essential(self):
        for _, fields, result in self.samples:
            for wrong in (result["R"].real, 1j*result["R"].imag,
                          result["operator"]["ordered"]):
                defect = audit.identity_terms(fields, result, wrong).sum(axis=1)
                self.assertGreater(np.linalg.norm(defect), .01)

    def test_curvature_and_euler_density_pull_back_from_actual_normal_connection(self):
        for data, fields, result in self.samples:
            a = data["A"]
            inv, volume = np.linalg.inv(a), abs(np.linalg.det(a))
            point, connection = data["point"], data["connection"]
            normal = dict(fields, coframe=np.eye(4), coframe_first=np.zeros((4, 4, 4)),
                          psi_first=point["psi_first"], multiplier=point["multiplier"],
                          multiplier_first=point["multiplier_first"], omega=connection["omega"],
                          omega_first=connection["first"])
            base = audit.residuals(normal)
            np.testing.assert_allclose(result["curvature"], np.einsum(
                "rm,sn,rsab->mnab", a, a, base["curvature"]), atol=2e-13)
            np.testing.assert_allclose(result["F"], base["F"] @ a, atol=2e-13)
            np.testing.assert_allclose(result["R"], volume*base["R"], atol=2e-12)
            np.testing.assert_allclose(result["FE"], volume*base["FE"] @ inv.T, atol=2e-12)

    def test_raw_parent_first_and_full_current_second_connection_jets(self):
        data = self.samples[0][0]
        coarse = audit.connection_difference_errors(data, 4e-4)
        fine = audit.connection_difference_errors(data, 2e-4)
        for key in coarse:
            with self.subTest(derivative=key):
                self.assertLess(fine[key], .4*coarse[key])
                self.assertLess(fine[key], 1e-5)

    def test_arbitrary_curvature_breaks_eliminated_identity(self):
        _, fields, result = self.samples[0]
        rng = np.random.default_rng(74184)
        changed = dict(fields, omega_first=fields["omega_first"]+np.array([
            audit.parent.unpack(rng.normal(size=24)) for _ in range(4)]))
        wrong = audit.residuals(changed)
        np.testing.assert_allclose(wrong["Cartan"], result["Cartan"], atol=1e-14)
        self.assertGreater(np.linalg.norm(audit.identity_terms(changed, wrong).sum(axis=1)), .1)


if __name__ == "__main__":
    unittest.main()
