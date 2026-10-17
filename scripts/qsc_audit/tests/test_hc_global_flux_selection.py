"""Global bundle flux, constrained block selection and off-constraint instability."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "global_flux_selection", ROOT / "analysis/HC_Global_Flux_Selection.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCGlobalFluxSelectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = model.evaluate()

    def assertClose(self, actual, expected, rtol=3e-8, atol=2e-10):
        np.testing.assert_allclose(actual, expected, rtol=rtol, atol=atol)

    def test_projector_is_rank_one_and_Hermitian(self):
        for shape in (-0.3, 0, 0.3):
            p = model.sphere_data(shape=shape)["P"]
            self.assertClose(p @ p, p)
            self.assertClose(p.conj().T, p)
            self.assertClose(np.trace(p), 1)

    def test_first_and_second_projector_jets(self):
        angles, step = np.array([0.9, 0.4]), 1e-5
        d = model.sphere_data(*angles, shape=0.3)
        for index, e in enumerate(np.eye(2)):
            plus = model.sphere_data(*(angles+step*e), shape=0.3)
            minus = model.sphere_data(*(angles-step*e), shape=0.3)
            self.assertClose((plus["P"]-minus["P"])/(2*step), d["P_first"][index+1])
            self.assertClose((plus["P_first"]-minus["P_first"])/(2*step), d["P_second"][index+1])

    def test_connection_derivative_includes_block_and_projector_terms(self):
        angles, step = np.array([0.9, 0.4]), 1e-5
        d = model.sphere_data(*angles, shape=0.3, amplitude=0.2, mode=3)
        for index, e in enumerate(np.eye(2)):
            plus = model.sphere_data(*(angles+step*e), shape=0.3, amplitude=0.2, mode=3)
            minus = model.sphere_data(*(angles-step*e), shape=0.3, amplitude=0.2, mode=3)
            self.assertClose((plus["connection"]-minus["connection"])/(2*step),
                             d["connection_first"][index+1])

    def test_every_hard_block_choice_is_compatible(self):
        for mode in (1, 2, 3, 4):
            d = model.sphere_data(shape=0.3, amplitude=0.2, mode=mode)
            self.assertClose(d["covariant_P_first"], 0)

    def test_connection_is_unitary_and_traceless(self):
        b = model.sphere_data(shape=-0.3, amplitude=0.2, mode=3)["connection"]
        self.assertClose(b, -b.conj().swapaxes(-1, -2))
        self.assertClose(np.trace(b, axis1=-2, axis2=-1), 0)

    def test_both_patch_frames_realize_the_same_projector(self):
        for patch in ("north", "south"):
            d = model.patch_data(0.9, 0.4, patch, shape=0.3, amplitude=-0.15)
            self.assertClose(np.outer(d["frame"], d["frame"].conj()), d["P"])
            self.assertClose(np.vdot(d["frame"], d["frame"]), 1)

    def test_transition_phase_and_connection_jump(self):
        n = model.patch_data(0.9, 0.4, shape=0.3, amplitude=0.2)
        s = model.patch_data(0.9, 0.4, "south", shape=0.3, amplitude=0.2)
        self.assertClose(s["frame"], np.exp(-0.4j)*n["frame"])
        self.assertClose(s["a_phi"]-n["a_phi"], -1j)

    def test_patch_frames_are_periodic_in_azimuth(self):
        for patch in ("north", "south"):
            a = model.patch_data(0.9, 0.4, patch)
            b = model.patch_data(0.9, 0.4+2*np.pi, patch)
            self.assertClose(a["frame"], b["frame"])

    def test_patch_potentials_equal_direct_frame_reduction(self):
        theta, phi, step = 0.9, 0.4, 1e-5
        d = model.sphere_data(theta, phi, shape=0.3, amplitude=-0.15)
        for patch in ("north", "south"):
            a = model.patch_data(theta, phi, patch, shape=0.3, amplitude=-0.15)
            plus = model.patch_data(theta, phi+step, patch, shape=0.3, amplitude=-0.15)
            minus = model.patch_data(theta, phi-step, patch, shape=0.3, amplitude=-0.15)
            direct = np.vdot(a["frame"], (plus["frame"]-minus["frame"])/(2*step)
                             +d["connection"][2] @ a["frame"])
            self.assertClose(direct, a["a_phi"])

    def test_block_one_form_vanishes_regularly_near_both_poles(self):
        for theta in (1e-3, np.pi-1e-3):
            d = model.sphere_data(theta, 0.4, amplitude=-0.15)
            self.assertClose(d["c_phi"]/np.sin(theta)**2, 0.15)
            self.assertLess(abs(d["c_phi"]/np.sin(theta)), 0.000151)

    def test_geometric_curvature_of_the_deformed_projector(self):
        d = model.sphere_data(shape=0.3)
        k = 2*d["P"]-np.eye(2)
        expected = 0.5j*np.sin(0.9)*(1-0.6*np.cos(0.9))*k
        self.assertClose(d["curvature"][1, 2], expected)

    def test_selected_block_correction_yields_uniform_flux(self):
        for shape in (-0.3, 0, 0.3):
            for theta in (0.3, 0.9, 2.4):
                d = model.sphere_data(theta, 0.4, shape, -shape/2)
                self.assertClose(d["curvature"][1, 2], 0.5j*np.sin(theta)*(2*d["P"]-np.eye(2)))

    def test_selected_patch_connections_lose_the_deformation(self):
        for patch in ("north", "south"):
            selected = model.patch_data(0.9, 0.4, patch, shape=0.3, amplitude=-0.15)
            round_patch = model.patch_data(0.9, 0.4, patch)
            self.assertClose(selected["a_phi"], round_patch["a_phi"])

    def test_global_flux_is_one_for_smooth_block_perturbations(self):
        for shape, amplitude, mode in ((0, 0, 1), (0.3, 0.2, 1),
                                       (-0.3, -0.4, 2), (0.2, 0.1, 3), (0, 0.2, 4)):
            d = model.surface_integrals(shape, amplitude, mode)
            self.assertClose(d["ambient_projected_flux"], 1)
            self.assertClose(d["bundle_flux"], 1)

    def test_complementary_flux_is_opposite(self):
        d = model.sphere_data(shape=0.3, amplitude=-0.15)
        p, f = d["P"], d["curvature"][1, 2]
        self.assertClose(np.trace((np.eye(2)-p) @ f), -np.trace(p @ f))

    def test_canonical_energy_saturates_the_bound(self):
        d = model.surface_integrals()
        self.assertClose(d["energy"], np.pi)
        self.assertClose(d["energy"], d["unit_charge_bound"])

    def test_general_mode_one_energy_matches_the_derived_square(self):
        for shape, amplitude in ((0.3, 0), (0.3, -0.15), (-0.2, 0.4)):
            actual = model.surface_integrals(shape, amplitude, radius=1.7, coupling=0.8)["energy"]
            expected = (np.pi+4*np.pi*(shape+2*amplitude)**2/3)/(1.7**2*0.8**2)
            self.assertClose(actual, expected)

    def test_higher_block_modes_cannot_lower_the_fixed_class_bound(self):
        for mode in (2, 3, 4):
            d = model.surface_integrals(0.3, 0.2, mode)
            self.assertGreater(d["energy"], d["unit_charge_bound"])

    def test_selected_amplitude_is_stationary_and_strictly_minimal(self):
        a, step = -0.15, 1e-3
        energies = [model.surface_integrals(0.3, a+s)["energy"] for s in (-step, 0, step)]
        self.assertClose((energies[2]-energies[0])/(2*step), 0)
        self.assertClose((energies[2]-2*energies[1]+energies[0])/step**2, 32*np.pi/3)

    def test_energy_radius_and_coupling_scaling(self):
        actual = model.surface_integrals(0.3, 0.2, radius=2, coupling=3)["energy"]
        self.assertClose(actual, model.surface_integrals(0.3, 0.2)["energy"]/36)

    def test_integer_charge_bound_has_the_required_symmetries(self):
        self.assertEqual(model.energy_bound(0), 0)
        self.assertClose(model.energy_bound(-2), 4*np.pi)
        self.assertClose(model.energy_bound(3, 2, 3), np.pi/4)

    def test_selected_connection_satisfies_direct_Yang_Mills_check(self):
        for theta, phi in ((0.6, 0.2), (0.9, 0.4), (2.3, -0.7)):
            self.assertLess(np.linalg.norm(model.yang_mills_check(0.3, -0.15, theta, phi)), 2e-8)

    def test_unselected_nonuniform_connection_is_not_Yang_Mills(self):
        self.assertGreater(np.linalg.norm(model.yang_mills_check(0.3)), 0.3)

    def test_azimuth_changes_no_curvature_norm(self):
        norms = [np.linalg.norm(model.sphere_data(0.9, phi, 0.3, -0.15)["curvature"])
                 for phi in (-1, 0.4, 2.7)]
        self.assertClose(norms, np.repeat(norms[0], 3))

    def test_hodge_Rayleigh_ratios(self):
        for mode in (1, 2, 3, 4):
            d = model.hodge_rayleigh(mode)
            self.assertClose(d["Rayleigh"], mode*(mode+1))

    def test_hodge_mode_norm_matches_the_Legendre_integral(self):
        for mode in (1, 2, 3, 4):
            d = model.hodge_rayleigh(mode)
            self.assertClose(d["one_form_norm_squared"], 4*np.pi*mode*(mode+1)/(2*mode+1))

    def test_hodge_spectral_scaling_and_positive_gap(self):
        for radius in (0.5, 1, 2):
            d = model.hodge_rayleigh(1, radius)
            self.assertClose(2*d["Rayleigh"], 4/radius**2)
            self.assertGreater(d["derivative_norm_squared"], 0)

    def test_scaling_path_has_the_exact_curvature_and_leakage(self):
        reference = model.sphere_data()
        for alpha in (0, 0.7, 1, 1.3, 2):
            d = model.sphere_data(alpha=alpha)
            self.assertClose(d["curvature"], (2*alpha-alpha*alpha)*reference["curvature"])
            self.assertClose(d["covariant_P_first"], (1-alpha)*reference["P_first"])

    def test_scaling_path_energy_is_below_constrained_minimum(self):
        for alpha in (0.7, 0.9, 1.1, 1.3):
            d = model.surface_integrals(alpha=alpha)
            self.assertClose(d["energy"], np.pi*(2*alpha-alpha*alpha)**2)
            self.assertLess(d["energy"], d["unit_charge_bound"])
            self.assertGreater(d["max_covariant_P_derivative"], 0.09)

    def test_unconstrained_second_variation_is_negative(self):
        step = 1e-3
        e0 = model.surface_integrals()["energy"]
        plus = model.surface_integrals(alpha=1+step)["energy"]
        minus = model.surface_integrals(alpha=1-step)["energy"]
        self.assertClose((plus-2*e0+minus)/step**2, -4*np.pi, rtol=1e-6)

    def test_global_flat_ambient_endpoints_are_incompatible(self):
        for alpha in (0, 2):
            d = model.surface_integrals(alpha=alpha)
            self.assertLess(d["energy"], 1e-25)
            self.assertClose(d["ambient_projected_flux"], 0)
            self.assertGreater(d["max_covariant_P_derivative"], 0.99)

    def test_compressed_bundle_flux_survives_ambient_flatness(self):
        for alpha in (0, 0.7, 1, 1.3, 2):
            d = model.surface_integrals(alpha=alpha)
            self.assertClose(d["bundle_flux"], 1)
            self.assertClose(d["ambient_projected_flux"], 2*alpha-alpha*alpha)

    def test_zero_connection_retains_extrinsic_image_bundle_curvature(self):
        d = model.sphere_data(alpha=0)
        p, dp = d["P"], d["P_first"]
        self.assertClose(d["curvature"], 0)
        self.assertClose(d["compressed_curvature"][1, 2], p @ model.transport.commutator(dp[1], dp[2]) @ p)
        self.assertGreater(np.linalg.norm(d["compressed_curvature"]), 0.3)

    def test_invalid_angles_shapes_modes_and_patch_names(self):
        for kwargs in ({"theta": 0}, {"theta": np.pi}, {"shape": 0.5},
                       {"mode": 0}, {"mode": True}, {"mode": 1.5}, {"alpha": np.nan}):
            with self.assertRaises(ValueError):
                model.sphere_data(**kwargs)
        with self.assertRaises(ValueError):
            model.patch_data(0.9, 0.4, "other")

    def test_invalid_scales_charges_quadrature_and_zero_hodge_mode(self):
        for kwargs in ({"radius": 0}, {"coupling": -1}, {"charge": True}, {"charge": 0.5}):
            with self.assertRaises(ValueError):
                model.energy_bound(**kwargs)
        for kwargs in ({"nodes": True}, {"nodes": 4}, {"nodes": 8.5}):
            with self.assertRaises(ValueError):
                model.surface_integrals(**kwargs)
        for mode, nodes in ((0, 40), (True, 40), (4, 4), (2, True)):
            with self.assertRaises(ValueError):
                model.hodge_rayleigh(mode, nodes=nodes)
        with self.assertRaises(ValueError):
            model.yang_mills_check(step=0)

    def test_native_Hopf_anchor_exists_without_native_identification(self):
        text = (ROOT / "sources/research/parts/v470/10_sphaera_and_physics.tex").read_text(encoding="utf-8")
        self.assertIn("\\label{thm:hopf}", text)
        self.assertIn("no evaluation identifies native P_C7", self.report["native_source_audit"]["gap"])

    def test_conditional_and_instability_boundaries_are_explicit(self):
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertIn("NOT a derived native topological sector", self.report["status"])
        self.assertTrue(self.report["relaxed_compatibility_negative_control"]["not_an_unconstrained_Yang_Mills_minimum"])
        self.assertTrue(self.report["constrained_Hessian"]["not_a_four_dimensional_mass_or_particle_spectrum"])

    def test_report_reproduces_saved_results(self):
        saved = json.loads((ROOT / "analysis/HC_Global_Flux_Selection.json").read_text(encoding="utf-8"))
        self.assertEqual(self.report, saved)


if __name__ == "__main__":
    unittest.main()
