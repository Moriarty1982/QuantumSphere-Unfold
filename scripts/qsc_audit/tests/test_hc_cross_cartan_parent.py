"""Independent first-order variations and conditional Cartan/odd-coframe obstruction."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("cross_cartan_parent", ROOT / "analysis/HC_Cross_Cartan_Parent.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCCrossCartanParentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.geometry = model.odd.reference_geometry()
        cls.g = cls.geometry
        cls.psi = cls.g["data"]["psi"]
        cls.schur = model.schur_compatibility(cls.g)
        cls.block = model.cartan_constraint_completion(cls.g)
        cls.report = model.evaluate()

    def assertClose(self, actual, expected, atol=2e-11, rtol=2e-8):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=rtol)

    def random_data(self, seed=451):
        rng = np.random.default_rng(seed)
        e = np.eye(4)+0.1*rng.normal(size=(4, 4))
        psi = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
        first = rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4))
        omega = model.unpack(rng.normal(size=24)*0.1)
        domega = np.array([model.unpack(rng.normal(size=24)*0.1) for _ in range(4)])
        lam = rng.normal(size=(4, 4))*0.1
        return rng, e, psi, first, omega, domega, lam

    def test_connection_basis_has_24_independent_lower_antisymmetric_components(self):
        self.assertEqual(model.OMEGA_BASIS.shape, (24, 4, 4, 4))
        k = np.linspace(-1, 1, 24)
        self.assertClose(model.pack(model.unpack(k)), k)
        self.assertClose(model.unpack(k), -model.unpack(k).swapaxes(1, 2))

    def test_pack_rejects_non_lorentz_connection(self):
        with self.assertRaises(ValueError):
            model.pack(np.ones((4, 4, 4)))

    def test_frame_rejects_singular_nonfinite_and_complex_values(self):
        for e in (np.zeros((4, 4)), np.eye(4)*np.nan, np.eye(4)*(1+1j)):
            with self.assertRaises(ValueError):
                model.frame_data(e)

    def test_volume_uses_absolute_determinant_on_reference_orientation(self):
        e, _, v = model.frame_data(self.g["frame"])
        self.assertLess(np.linalg.det(e), 0)
        self.assertClose(v, -np.linalg.det(e))

    def test_spin_lift_matches_existing_same_coframe_lift(self):
        self.assertClose(model.spin_connection(self.g["bundle"]["omega"]), self.g["bundle"]["spin"])

    def test_lc_torsion_vanishes_with_the_actual_first_jet(self):
        self.assertClose(model.torsion(self.g["frame"], self.g["first"], self.g["bundle"]["omega"]), 0)

    def test_curvature_is_antisymmetric_in_coordinate_and_upper_frame_pairs(self):
        _, _, _, _, w, dw, _ = self.random_data()
        r = model.curvature_upper(w, dw)
        self.assertClose(r, -r.swapaxes(0, 1))
        self.assertClose(r, -r.swapaxes(2, 3))

    def test_lc_palatini_scalar_matches_existing_metric_curvature(self):
        step = 1e-6
        dw = np.array([(model.odd.reference_geometry(model.odd.POINT+step*u)["bundle"]["omega"]
                        -model.odd.reference_geometry(model.odd.POINT-step*u)["bundle"]["omega"])/(2*step)
                       for u in np.eye(4)])
        r = model.curvature_upper(self.g["bundle"]["omega"], dw)
        _, _, v = model.frame_data(self.g["frame"])
        scalar = 2*model.palatini_density(self.g["frame"], r)/v
        self.assertClose(scalar, self.g["bundle"]["curvature"]["scalar"], atol=0.01, rtol=2e-7)

    def test_contorsion_hessian_is_real_symmetric_invertible_and_not_positive_energy(self):
        h = model.contorsion_hessian(np.eye(4))
        self.assertClose(h, h.T)
        self.assertEqual(np.linalg.matrix_rank(h), 24)
        eig = np.linalg.eigvalsh(h)
        self.assertLess(eig[0], 0)
        self.assertGreater(eig[-1], 0)

    def test_hessian_reconstructs_independently_evaluated_quadratic_curvature(self):
        rng, e, _, _, _, _, _ = self.random_data()
        k = rng.normal(size=24)
        h = model.contorsion_hessian(e, 0.7)
        self.assertClose(k @ h @ k/2, model.palatini_density(e, model.curvature_upper(model.unpack(k)), 0.7))

    def test_zero_coefficient_is_not_inverted(self):
        with self.assertRaises(ValueError):
            model.contorsion_hessian(np.eye(4), 0)

    def test_curvature_hessian_scales_with_einstein_coefficient(self):
        h = model.contorsion_hessian(np.eye(4))
        self.assertClose(model.contorsion_hessian(np.eye(4), -0.3), -0.3*h)

    def test_cross_connection_response_is_exact_not_a_first_order_truncation(self):
        _, e, p, dp, w, _, _ = self.random_data()
        response, _ = model.spin_maps(e, p)
        base = model.odd.channels(p, dp)["odd"]
        cross = model.odd.channels(p, model.covariant_jet(p, dp, w))["odd"]
        self.assertClose(cross-base, (response @ model.pack(w)).reshape(4, 4))

    def test_cross_response_is_transverse_to_weighted_axial_for_each_column(self):
        response, _ = model.spin_maps(self.g["frame"], self.psi)
        _, aq = model.axial_currents(self.psi)
        for column in response.T:
            self.assertClose(aq @ model.ETA @ column.reshape(4, 4), 0)

    def test_independent_connection_source_varies_real_dirac_and_cross_terms(self):
        rng, e, p, dp, w, _, lam = self.random_data()
        variation = rng.normal(size=24)
        response, source = model.spin_maps(e, p)
        mass = model.odd.background.triadic_mass()

        def density(omega):
            return (model.matter_density(e, p, dp, omega, mass)
                    -np.sum(lam*model.odd.channels(p, model.covariant_jet(p, dp, omega))["odd"]))
        step = 1e-5
        numeric = (density(w+step*model.unpack(variation))-density(w-step*model.unpack(variation)))/(2*step)
        self.assertClose(numeric, (source-response.T @ lam.reshape(-1)) @ variation, atol=5e-9)

    def test_independent_coframe_euler_matches_pointwise_density_variation(self):
        rng, e, p, dp, w, dw, lam = self.random_data()
        variation = rng.normal(size=(4, 4))
        r, mass = model.curvature_upper(w, dw), model.odd.background.triadic_mass()
        fe = model.coframe_euler(e, p, dp, w, r, mass, lam, 0.8, 0.04)

        def density(frame):
            return model.direct_parent_density(frame, p, dp, w, r, mass, lam, 0.8, 0.04)
        step = 1e-5
        numeric = (density(e+step*variation)-density(e-step*variation))/(2*step)
        self.assertClose(numeric, np.sum(fe*variation), atol=2e-8)

    def test_independent_coframe_scale_identity_keeps_mass_and_multiplier(self):
        _, e, p, dp, w, dw, lam = self.random_data()
        r, mass = model.curvature_upper(w, dw), model.odd.background.triadic_mass()
        _, _, volume = model.frame_data(e)
        ld = model.matter_density(e, p, dp, w, mass)
        lm = -volume*np.vdot(p, mass @ p @ model.BETA.T).real
        lg = model.palatini_density(e, r, 0.8)
        lv = -0.04*volume
        fe = model.coframe_euler(e, p, dp, w, r, mass, lam, 0.8, 0.04)
        self.assertClose(np.sum(fe*e), 3*(ld-lm)+4*lm+2*lg+4*lv+np.sum(lam*e))

    def test_general_curved_weights_are_hermitian(self):
        _, e, _, _, _, _, lam = self.random_data()
        weights = model.kinetic_weights(e, lam)
        self.assertClose(weights, weights.conj().swapaxes(-1, -2))

    def test_flat_weights_reduce_to_prior_phase_current_parent(self):
        lam = np.arange(16).reshape(4, 4)*0.01
        self.assertClose(model.kinetic_weights(np.eye(4), lam), model.odd.effective_weights(1., lam))

    def test_real_action_connection_variation_includes_full_palatini_derivative(self):
        self.assertLess(self.report["independent_action_variations"]["connection_variation_error"], 1e-7)

    def test_same_parent_probe_variation_retains_connection_adjoint_and_density(self):
        self.assertLess(self.report["independent_action_variations"]["probe_variation_error"], 1e-7)

    def test_same_parent_multiplier_variation_is_the_coframe_constraint(self):
        self.assertLess(self.report["independent_action_variations"]["multiplier_variation_error"], 1e-7)

    def test_independent_coframe_variation_and_lc_chain_rule_agree(self):
        r = self.report["independent_action_variations"]
        self.assertLess(r["independent_coframe_variation_error"], 1e-7)
        self.assertLess(r["LC_coframe_chain_rule_error"], 1e-7)

    def test_dropping_lc_connection_reaction_changes_the_actual_variation(self):
        r = self.report["independent_action_variations"]
        self.assertGreater(abs(r["omitted_LC_spin_reaction"]), 1e-4)
        self.assertGreater(abs(r["omitted_LC_spin_reaction"]), 1000*r["LC_coframe_chain_rule_error"])

    def test_parent_phase_current_still_satisfies_offshell_ward_identity(self):
        self.assertLess(self.report["independent_action_variations"]["phase_Ward_error"], 1e-11)

    def test_reference_has_independent_total_and_weighted_axial_currents(self):
        tf = model.torsion_free_check(self.g["frame"], self.psi)
        self.assertEqual(tf["axial_pair_rank"], 2)
        self.assertGreater(tf["spin_residual_norm"]/tf["source_norm"], 0.02)

    def test_cross_response_has_rank_twelve_not_sixteen(self):
        self.assertEqual(np.linalg.matrix_rank(self.block["response"], tol=1e-10), 12)

    def test_exact_canonical_schur_and_its_rank_nine(self):
        _, vectors = np.linalg.eigh(model.odd.Q_PHASE)
        p = np.outer(vectors[:, -1], np.eye(4)[0])
        response, _ = model.spin_maps(np.eye(4), p)
        s = response @ np.linalg.solve(model.contorsion_hessian(np.eye(4)), response.T)
        self.assertClose(s, model.canonical_spacelike_schur(0.5))
        self.assertEqual(np.linalg.matrix_rank(s), 9)

    def test_canonical_schur_image_has_four_row_and_three_transverse_conditions(self):
        s = model.canonical_spacelike_schur(0.7)
        for image in s.T:
            obstruction = model.transverse_obstruction(np.eye(4), np.array([0., 0, 0, 0.7]), image.reshape(4, 4))
            self.assertClose(obstruction["row_contraction"], 0)
            self.assertClose(obstruction["transverse_antisymmetric"], 0)

    def test_schur_range_covariant_form_on_the_actual_curved_frame(self):
        _, aq = model.axial_currents(self.psi)
        for image in self.schur["schur"].T:
            obstruction = model.transverse_obstruction(self.g["frame"], aq, image.reshape(4, 4))
            self.assertClose(obstruction["row_contraction"], 0)
            self.assertClose(obstruction["transverse_antisymmetric"], 0)

    def test_clifford_drive_formula_for_generic_complex_probes_and_nonflat_frames(self):
        for seed in (17, 31, 56):
            _, e, p, _, _, _, _ = self.random_data(seed)
            response, source = model.spin_maps(e, p)
            drive = response @ np.linalg.solve(model.contorsion_hessian(e), source)
            self.assertClose(drive.reshape(4, 4), model.dirac_drive_formula(e, p))

    def test_reference_dirac_drive_has_no_schur_null_component(self):
        self.assertLess(np.linalg.norm(self.schur["projected_drive"]), 1e-15)
        self.assertGreater(np.linalg.norm(self.schur["projected_target"]), 0.001)

    def test_reference_target_passes_row_condition_but_fails_transverse_symmetry(self):
        obstruction = self.schur["obstruction"]
        self.assertGreater(obstruction["weighted_axial_square"], 0)
        self.assertClose(obstruction["row_contraction"], 0)
        self.assertGreater(np.linalg.norm(obstruction["transverse_antisymmetric"]), 0.15)

    def test_schur_equation_is_the_actual_elimination_for_nonzero_scale(self):
        coefficient = 2.3
        lam = np.linspace(-0.1, 0.2, 16)
        response, source = model.spin_maps(self.g["frame"], self.psi)
        k = np.linalg.solve(coefficient*self.block["hessian"], -source+response.T @ lam)
        self.assertClose(coefficient*(response @ k-self.schur["target"]),
                         self.schur["schur"] @ lam-self.schur["drive"]-coefficient*self.schur["target"])

    def test_reference_fails_for_different_einstein_coefficients_not_just_unit_scale(self):
        null = self.schur["nullspace"]
        for c in (0.01, 0.5, 1., 10., -1.):
            projected = null.T @ (c*self.schur["target"]+self.schur["drive"])
            self.assertClose(np.linalg.norm(projected), abs(c)*np.linalg.norm(self.schur["projected_target"]))

    def test_saddle_matrix_rank_is_24_plus_schur_rank(self):
        self.assertClose(self.block["matrix"], self.block["matrix"].T)
        self.assertEqual(self.block["rank"], 24+self.schur["rank"])
        self.assertEqual(self.block["rank"], 33)

    def test_report_does_not_mislabel_a_least_squares_vector_as_a_solution(self):
        r = self.report["failed_reference_connection_constraint_attempt"]
        self.assertTrue(r["least_squares_vector_is_not_a_solution_or_a_stability_test"])
        self.assertGreater(r["connection_residual_norm"], 1e-4)
        self.assertGreater(r["constraint_residual_norm"], 1e-3)

    def test_consistent_algebraic_rhs_positive_control_is_solved(self):
        response, source = model.spin_maps(self.g["frame"], self.psi)
        lam = np.linspace(-0.1, 0.1, 16)
        k = np.linalg.solve(self.block["hessian"], -source+response.T @ lam)
        rhs = np.concatenate((-source, -response @ k))
        solution = np.linalg.lstsq(self.block["matrix"], rhs, rcond=1e-11)[0]
        self.assertClose(self.block["matrix"] @ solution, rhs)

    def test_null_axial_projector_case_is_not_silently_used(self):
        with self.assertRaises(ValueError):
            model.transverse_obstruction(np.eye(4), np.array([1., 0, 0, 1]), np.eye(4))

    def test_saved_report_matches_current_diagnostic_and_declares_no_native_completion(self):
        saved = json.loads((ROOT / "analysis/HC_Cross_Cartan_Parent.json").read_text(encoding="utf-8"))
        self.assertEqual(saved["status"], self.report["status"])
        self.assertFalse(saved["main_TeX_changed"])
        self.assertEqual(saved["scale_independent_reference_compatibility"]["Schur_rank"], 9)
        self.assertIn("not a native or full field solution", saved["status"])


if __name__ == "__main__":
    unittest.main()
