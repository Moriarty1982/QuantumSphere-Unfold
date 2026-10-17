"""Proper-time Dirac comparison, independent spectrum, vacuum and matching limits."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "induced_gravity", ROOT / "analysis/HC_Induced_Gravity_Heat_Kernel.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCInducedGravityHeatKernelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.matrix = model.background.triadic_mass()
        cls.sample = model.coefficients(cls.matrix, 20, 2)
        cls.report = model.evaluate()

    def assertClose(self, actual, expected, rtol=2e-10, atol=1e-12):
        np.testing.assert_allclose(actual, expected, rtol=rtol, atol=atol)

    def test_prepared_mass_spectrum(self):
        self.assertClose(model.mass_spectrum(self.matrix),
                         [0.6-np.sqrt(16.49), 0.6, 0.6+np.sqrt(16.49)])

    def test_invalid_mass_matrices_are_rejected(self):
        for matrix in ([], [[1, 2]], [[1, 1], [0, 1]], [[np.nan]], [[1j]]):
            with self.subTest(matrix=matrix), self.assertRaises(ValueError):
                model.mass_spectrum(matrix)

    def test_cutoff_order_and_finiteness(self):
        for uv, ir in ((0, 0), (1, 1), (1, 2), (2, -1), (np.inf, 1), (2, np.nan)):
            with self.subTest(uv=uv, ir=ir), self.assertRaises(ValueError):
                model.proper_time_integral(1, uv, ir)

    def test_invalid_integral_arguments(self):
        for mass, power in ((np.nan, 2), (np.inf, 3), (1, 1), (1, True), (1, 4)):
            with self.subTest(mass=mass, power=power), self.assertRaises(ValueError):
                model.proper_time_integral(mass, 20, 2, power)

    def test_massless_integrals_exact(self):
        for ir in (0, 2, 19):
            self.assertEqual(model.proper_time_integral(0, 20, ir, 2), 400-ir**2)
            self.assertEqual(model.proper_time_integral(0, 20, ir, 3), (160000-ir**4)/2)

    def test_gamma_integrals_against_finite_window_quadrature(self):
        for mass in (0.0, 0.6, 4.6607881, 9):
            for power in (2, 3):
                self.assertClose(model.proper_time_integral(mass, 20, 2, power),
                                 model.proper_time_integral(mass, 20, 2, power, True))

    def test_gamma_integrals_against_unbounded_proper_time_quadrature(self):
        for mass in (0.0, 0.6, 4.66):
            for power in (2, 3):
                self.assertClose(model.proper_time_integral(mass, 20, 0, power),
                                 model.proper_time_integral(mass, 20, 0, power, True))

    def test_proper_time_windows_are_additive(self):
        for mass in (0.0, 0.6, 4.66):
            for power in (2, 3):
                self.assertClose(model.proper_time_integral(mass, 20, 0, power),
                                 model.proper_time_integral(mass, 20, 2, power)
                                 +model.proper_time_integral(mass, 2, 0, power))

    def test_negative_mass_has_positive_squared_mass_not_tachyon(self):
        for mass in (0.6, 3.46, 4.66):
            self.assertEqual(model.proper_time_integral(mass, 20, 2),
                             model.proper_time_integral(-mass, 20, 2))
        a, b = self.sample, model.coefficients(-self.matrix, 20, 2)
        self.assertClose([a["A"], a["rho_vac"]], [b["A"], b["rho_vac"]])

    def test_internal_unitary_changes_do_not_change_loop_coefficients(self):
        rng = np.random.default_rng(814)
        u, _ = np.linalg.qr(rng.normal(size=(3, 3))+1j*rng.normal(size=(3, 3)))
        changed = model.coefficients(u @ self.matrix @ u.conj().T, 20, 2)
        self.assertClose([changed["A"], changed["rho_vac"]],
                         [self.sample["A"], self.sample["rho_vac"]])

    def test_constant_frame_phases_do_not_change_loop_coefficients(self):
        u = np.diag(np.exp(1j*np.array([0.1, -0.8, 1.7])))
        changed = model.coefficients(u @ self.matrix @ u.conj().T, 20, 2)
        self.assertClose(changed["A"], self.sample["A"])
        self.assertClose(changed["rho_vac"], self.sample["rho_vac"])

    def test_heavy_species_decouple_in_fixed_proper_time_regulator(self):
        light = model.proper_time_integral(0, 2, 0)
        heavy = [model.proper_time_integral(m, 2, 0) for m in (2, 4, 8, 16)]
        self.assertTrue(all(a > b > 0 for a, b in zip([light]+heavy, heavy)))
        self.assertLess(heavy[-1]/light, 1e-28)

    def test_uv_boundary_derivative(self):
        u, v, m, step = 20.0, 2.0, 4.66, 1e-3
        for p in (2, 3):
            derivative = (model.proper_time_integral(m, u+step, v, p)
                          -model.proper_time_integral(m, u-step, v, p))/(2*step)
            self.assertClose(derivative, 2*u**(2*p-3)*np.exp(-m*m/u**2), rtol=2e-8)

    def test_ir_boundary_derivative(self):
        u, v, m, step = 20.0, 2.0, 0.6, 1e-3
        for p in (2, 3):
            derivative = (model.proper_time_integral(m, u, v+step, p)
                          -model.proper_time_integral(m, u, v-step, p))/(2*step)
            self.assertClose(derivative, -2*v**(2*p-3)*np.exp(-m*m/v**2), rtol=4e-7)

    def test_dimensional_scaling(self):
        factor = 3.0
        b = model.coefficients(factor*self.matrix, factor*20, factor*2)
        self.assertClose(b["A"], factor**2*self.sample["A"])
        self.assertClose(b["rho_vac"], factor**4*self.sample["rho_vac"])
        self.assertClose(b["Lambda_cos_truncated"], factor**2*self.sample["Lambda_cos_truncated"])

    def test_identical_species_do_not_suppress_cosmological_ratio(self):
        a, b = model.coefficients([[0.6]], 20, 2), model.coefficients(0.6*np.eye(5), 20, 2)
        self.assertClose(b["A"], 5*a["A"])
        self.assertClose(b["rho_vac"], 5*a["rho_vac"])
        self.assertClose(b["Lambda_cos_truncated"], a["Lambda_cos_truncated"])

    def test_exact_massless_newton_and_vacuum_coefficients(self):
        d = model.coefficients(np.zeros((3, 3)), 20, 2)
        self.assertClose(d["inverse_G"], 3*396/(6*np.pi))
        self.assertClose(d["rho_vac"], 3*(20**4-2**4)/(16*np.pi**2))
        self.assertClose(d["Lambda_cos_truncated"], 3*(400+4))

    def test_massless_zero_ir_limit(self):
        d = model.coefficients(np.zeros((3, 3)), 20, 0)
        self.assertClose(d["Lambda_cos_truncated"], 3*400)
        self.assertClose(d["inverse_G"], 3*400/(6*np.pi))

    def test_positive_curvature_and_vacuum_coefficients(self):
        self.assertGreater(self.sample["A"], 0)
        self.assertGreater(self.sample["rho_vac"], 0)
        self.assertClose(self.sample["inverse_G"], 8*np.pi/self.sample["kappa"])

    def test_independent_truncated_action_integration(self):
        for r in (-0.03, 0, 0.01):
            self.assertClose(model.action_density(r, self.matrix, 20, 2),
                             self.sample["rho_vac"]-self.sample["A"]*r)

    def test_heat_density_is_even_in_mass_and_linear_at_this_truncation(self):
        s, r = 0.03, 0.02
        self.assertClose(model.heat_density(s, r, self.matrix), model.heat_density(s, r, -self.matrix))
        slope = (model.heat_density(s, r, self.matrix)-model.heat_density(s, 0, self.matrix))/r
        expected = -s*np.sum(np.exp(-s*model.mass_spectrum(self.matrix)**2))/(3*(4*np.pi*s)**2)
        self.assertClose(slope, expected)

    def test_unsubtracted_vacuum_bound_for_masses_and_windows(self):
        for ir in (0, 2, 19):
            for masses in ([0, 0, 0], [0.6, 3.46, 4.66], [10, 20, 30]):
                d = model.coefficients(np.diag(masses), 20, ir)
                self.assertGreaterEqual(d["Lambda_cos_truncated"], 3*(400+ir**2)-1e-9)
                self.assertLess(d["Lambda_cos_truncated"], 6*400)

    def test_mass_increase_cannot_fix_unsubtracted_vacuum_ratio(self):
        values = [model.coefficients([[m]], 20, 2)["Lambda_cos_truncated"] for m in (0, 1, 5, 20, 40)]
        self.assertTrue(all(b > a for a, b in zip(values, values[1:])))

    def test_truncated_vacuum_is_outside_weak_curvature(self):
        self.assertClose(self.sample["R_vac_truncated"], 4*self.sample["Lambda_cos_truncated"])
        self.assertGreater(self.sample["R_vac_truncated"]/20**2, 12)
        self.assertTrue(self.report["formulae"]["bound_is_not_a_solution_of_the_full_large_curvature_effective_action"])

    def test_sphere_weyl_volume_normalization(self):
        s = 0.0025
        k = model.sphere_heat(s)["heat_trace"]
        self.assertClose(k/(2/(3*s*s)), 1, rtol=0.003)

    def test_sphere_a2_sign_and_convergence(self):
        values = [model.sphere_heat(s)["a2_per_scalar_curvature"] for s in (0.02, 0.01, 0.005, 0.0025)]
        errors = [abs(x+1/3) for x in values]
        self.assertTrue(all(x < 0 for x in values))
        for a, b in zip(errors, errors[1:]):
            self.assertGreater(a/b, 1.99)
            self.assertLess(a/b, 2.02)
        self.assertLess(errors[-1], 0.000154)

    def test_sphere_constant_remainder_converges_independently(self):
        values = [model.sphere_heat(s)["a4_remainder"] for s in (0.01, 0.005, 0.0025)]
        errors = [abs(v-11/90) for v in values]
        self.assertGreater(errors[0]/errors[1], 1.99)
        self.assertLess(errors[-1], 4.2e-5)

    def test_sphere_radius_scaling(self):
        a, b = model.sphere_heat(0.01), model.sphere_heat(0.09, radius=3)
        self.assertClose(a["heat_trace"], b["heat_trace"])
        self.assertClose(a["a2_per_scalar_curvature"], b["a2_per_scalar_curvature"])

    def test_sphere_tail_bound(self):
        s = 0.02
        d = model.sphere_heat(s, tolerance=1e-7)
        k = d["cutoff_k"]
        extra = 4/3*sum((n**3-n)*np.exp(-s*n*n) for n in range(k+1, k+81))
        self.assertGreater(extra, 0)
        self.assertLess(extra, d["tail_bound"])
        self.assertLess(d["tail_bound"], 1e-7*2/(3*s*s))

    def test_invalid_sphere_inputs(self):
        for s, a, tol in ((0, 1, 1e-12), (1, -1, 1e-12), (1, 1, 0), (1, 1, 1), (np.nan, 1, 1e-12)):
            with self.subTest(s=s, a=a, tol=tol), self.assertRaises(ValueError):
                model.sphere_heat(s, a, tol)

    def test_vacuum_subtraction_is_an_input_leaving_einstein_coefficient_free(self):
        a = model.matching(self.sample, bare_rho=-self.sample["rho_vac"])
        b = model.matching(self.sample, bare_a=self.sample["A"], bare_rho=-self.sample["rho_vac"])
        self.assertEqual(a["Lambda_cos"], 0)
        self.assertEqual(b["Lambda_cos"], 0)
        self.assertClose(b["inverse_G"], 2*a["inverse_G"])
        self.assertClose(b["kappa"], a["kappa"]/2)

    def test_invalid_matched_einstein_sign(self):
        for a in (-self.sample["A"], -2*self.sample["A"], np.nan):
            with self.subTest(a=a), self.assertRaises(ValueError):
                model.matching(self.sample, bare_a=a)

    def test_native_anchors_exist_but_are_not_claimed_proved(self):
        text = (ROOT / "sources/research/parts/v470/10_sphaera_and_physics.tex").read_text(encoding="utf-8")
        for item in self.report["native_source_audit"]:
            self.assertIn("\\label{"+item["label"]+"}", text)
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertIn("NOT native", self.report["status"])
        self.assertGreaterEqual(len(self.report["remaining_obligations"]), 7)

    def test_report_reproduces_saved_values(self):
        saved = json.loads((ROOT / "analysis/HC_Induced_Gravity_Heat_Kernel.json").read_text(encoding="utf-8"))
        self.assertEqual(self.report, saved)
        self.assertClose(saved["sample"]["A"], 1.1335303667644416)
        self.assertClose(saved["sample"]["rho_vac"], 2882.55500807977)


if __name__ == "__main__":
    unittest.main()
