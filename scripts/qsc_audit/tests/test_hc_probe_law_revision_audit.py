"""Probe-version provenance, curved real-action variation and same-coframe current gate."""
import importlib.util
import json
from pathlib import Path
import re
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "probe_law_revision_audit", ROOT / "analysis/HC_Probe_Law_Revision_Audit.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCProbeLawRevisionAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = model.cone_data()
        cls.report = model.evaluate()
        cls.saved = json.loads((ROOT / "analysis/HC_Probe_Law_Revision_Audit.json").read_text(encoding="utf-8"))

    def assertClose(self, actual, expected, atol=2e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-10)

    def random_data(self, seed=14, size=4):
        rng = np.random.default_rng(seed)
        psi = rng.normal(size=size)+1j*rng.normal(size=size)
        derivative = rng.normal(size=(4, size))+1j*rng.normal(size=(4, size))
        matrices = rng.normal(size=(10, size, size))+1j*rng.normal(size=(10, size, size))
        hermitian = (matrices+matrices.conj().swapaxes(-1, -2))/2
        return psi, derivative, hermitian[:4], matrices[4:8], hermitian[8], hermitian[9]

    def test_all_audited_source_anchors_exist(self):
        self.assertTrue(all(v["all_anchors_found"] for v in self.report["audited_sources"].values()))

    def test_active_entrypoint_includes_both_legacy_and_qualifying_sections(self):
        text = (ROOT / "sources/research/v480-companion.tex").read_text(encoding="utf-8")
        for record in self.report["audited_sources"]["entrypoint"]["anchors"]:
            self.assertIn(r"\input{"+record+"}", text)

    def test_later_synthesis_repeats_the_ordered_master_differential_law(self):
        text = (ROOT / self.report["audited_sources"]["later_synthesis"]["path"]).read_text(encoding="utf-8")
        block = text.split(r"\label{thm:minimal-mmhc-field-equation}")[1].split(r"\end{theorem}")[0]
        self.assertIn(r"\bigl(i\Gamma^\mu\mathcalD_\mu-\Omega\bigr)\Psi=0", re.sub(r"\s+", "", block))

    def test_later_fluid_block_retains_kernel_not_an_alternative_primary_equation(self):
        text = (ROOT / self.report["audited_sources"]["later_hypotheses"]["path"]).read_text(encoding="utf-8")
        block = text.split(r"\label{thm:theorem-level-shadow-fluid-type-readout}")[1].split(r"\end{theorem}")[0]
        self.assertIn("cannot replace the primary kernel-level transport equations", block)
        self.assertIn(r"\bigl(i\Gamma^\mu\mathcal{D}_\mu - \Omega\bigr)\Psi = 0", block)

    def test_hypothesis_distinguishes_visible_defect_from_deeper_generator(self):
        text = (ROOT / self.report["audited_sources"]["later_hypotheses"]["path"]).read_text(encoding="utf-8")
        block = text.split(r"\label{hyp:frame-dependent-defect-readout}")[1].split(r"\end{proposition}")[0]
        self.assertIn("Hypothesis-grade", block)
        self.assertIn("without forcing", block)
        self.assertIn(r"\mathbf{H}_C", block)

    def test_current_qualification_does_not_silently_replace_ordered_law(self):
        text = (ROOT / self.report["audited_sources"]["current_qualification"]["path"]).read_text(encoding="utf-8")
        self.assertIn("This is a change of probe law", text)
        self.assertIn("not already a common solved field system", text)

    def test_deeper_meta_field_equation_is_explicitly_deferred_in_later_source(self):
        text = (ROOT / self.report["audited_sources"]["later_hypotheses"]["path"]).read_text(encoding="utf-8")
        self.assertIn("What remains unproved is the stronger claim", text)
        self.assertIn(r"\mathfrak E_{\mathrm{HC}}=0", text)

    def test_saved_canonical_source_hashes_guard_semantic_provenance(self):
        for role, record in self.report["audited_sources"].items():
            self.assertEqual(record["canonical_LF_sha256"], self.saved["audited_sources"][role]["canonical_LF_sha256"])
            self.assertEqual(record["anchors"], self.saved["audited_sources"][role]["anchors"])

    def test_real_density_equals_explicit_symmetric_action(self):
        psi, derivative, k, b, w, _ = self.random_data()
        covariant = derivative+b @ psi
        ordered = np.einsum("i,mij,mj->", psi.conj(), k, covariant)
        explicit = 0.5j*(ordered-ordered.conjugate())-np.vdot(psi, w @ psi)
        self.assertAlmostEqual(model.action_density(psi, derivative, k, b, w), explicit.real)
        self.assertLess(abs(explicit.imag), 1e-12)

    def test_general_compatibility_defect_is_hermitian(self):
        data = model.real_operator(*self.random_data())
        self.assertClose(data["defect"], data["defect"].conj().T)

    def test_real_EL_differs_from_ordered_EL_by_derived_defect(self):
        args = self.random_data(size=8)
        data = model.real_operator(*args)
        self.assertClose(data["symmetric"]-data["ordered"], 0.5j*data["defect"] @ args[0])

    def test_off_shell_phase_Ward_identity_for_noncommuting_matrix_backgrounds(self):
        for seed in range(5):
            args = self.random_data(seed, size=8)
            data = model.real_operator(*args)
            self.assertAlmostEqual(data["current_divergence"], 2*np.vdot(args[0], data["symmetric"]).imag, places=10)

    def test_independent_integrated_action_variation_matches_derived_EL(self):
        result = self.report["independent_periodic_action_check"]
        self.assertLess(result["analytic_variation_error"], 1e-11)
        self.assertLess(result["finite_difference_variation_error"], 2e-8)

    def test_omitting_defect_fails_the_same_action_variation(self):
        self.assertGreater(self.report["independent_periodic_action_check"]["unchanged_ordered_equation_variation_error"], 0.08)

    def test_periodic_Ward_identity_is_independent_of_equations_of_motion(self):
        self.assertLess(self.report["independent_periodic_action_check"]["Ward_identity_max_error"], 2e-12)

    def test_periodic_variation_is_stable_on_a_different_grid(self):
        result = model.periodic_variation_check(49)
        self.assertLess(result["analytic_variation_error"], 1e-11)
        self.assertClose(result["derived_EL_variation"], self.report["independent_periodic_action_check"]["derived_EL_variation"])

    def test_flat_internal_unitary_connection_has_no_defect(self):
        psi, derivative, _, b, w, _ = self.random_data()
        b = 1j*b[:, :1, :1].real*np.eye(4)
        result = model.real_operator(psi, derivative, model.K_FRAME, b, w, np.zeros((4, 4)))
        self.assertClose(result["defect"], 0)

    def test_real_action_cancels_factorized_HC_transport(self):
        args = self.random_data(size=8)
        psi, derivative = args[:2]
        k = np.array([np.kron(np.eye(2), a) for a in model.K_FRAME])
        h = np.kron(np.diag([0.4, 0.7]), np.eye(4))
        n = np.array([-1., 0, 0, 1])
        b = 0.3*n[:, None, None]*h
        result = model.real_operator(psi, derivative, k, b, args[4], np.zeros((8, 8)))
        without = model.real_operator(psi, derivative, k, np.zeros_like(b), args[4], np.zeros((8, 8)))
        self.assertClose(result["symmetric"], without["symmetric"])
        self.assertGreater(np.linalg.norm(result["ordered"]-without["ordered"]), 0.1)

    def test_noncommuting_HC_leaves_commutator_not_ordered_product(self):
        psi, derivative, _, _, w, h = self.random_data()
        n = np.array([-1., 0, 0, 1])
        b = 0.3*n[:, None, None]*h
        slash = np.einsum("m,mij->ij", n, model.K_FRAME)
        base = 1j*np.einsum("mij,mj->i", model.K_FRAME, derivative)-w @ psi
        result = model.real_operator(psi, derivative, model.K_FRAME, b, w, np.zeros((4, 4)))
        self.assertClose(result["symmetric"], base+0.15j*(slash @ h-h @ slash) @ psi)

    def test_cone_full_real_coframe_reconstructs_its_own_geometry(self):
        self.assertClose(self.data["reconstructed"], self.data["frame"])
        self.assertEqual(np.linalg.matrix_rank(self.data["reconstructed"]), 4)

    def test_cone_spatial_columns_come_from_spin_not_probe_spatial_gradients(self):
        self.assertClose(self.data["derivative"][1:], 0)
        for i in range(1, 4):
            self.assertClose(self.data["bundle"]["spin"][i], model.K_FRAME[i]/2)

    def test_curved_geometry_is_nonflat_with_exact_Ricci_formula(self):
        curvature = self.data["bundle"]["curvature"]
        self.assertClose(curvature["ricci"], np.diag([0., 2, 2, 2]))
        self.assertAlmostEqual(curvature["scalar"], 6/self.data["time"]**2)
        self.assertGreater(np.linalg.norm(curvature["riemann"]), 1)

    def test_metric_gamma_and_volume_compatibility_have_zero_defect(self):
        self.assertClose(self.data["operator"]["defect"], 0)
        self.assertLess(np.linalg.norm(self.data["bundle"]["gamma_compatibility"]), 1e-12)

    def test_adding_density_term_twice_is_not_a_probe_correction(self):
        op = self.data["operator"]
        wrong = op["ordered"]+0.5j*self.data["divergence"] @ self.data["psi"]
        self.assertGreater(np.linalg.norm(wrong-op["symmetric"]), 1)

    def test_curved_probe_trace_obstruction_survives_compatible_spin_transport(self):
        value = np.vdot(self.data["psi"], self.data["operator"]["symmetric"])
        self.assertAlmostEqual(value.imag, 4)
        self.assertClose(self.data["operator"]["symmetric"], (2j/self.data["time"]-self.data["mass"])*self.data["psi"])

    def test_same_result_at_other_cone_times_and_real_masses(self):
        for time, mass in ((0.7, 0), (2.3, -0.4), (3.2, 1.1)):
            data = model.cone_data(time, mass)
            self.assertClose(data["reconstructed"], data["frame"])
            self.assertAlmostEqual(np.vdot(data["psi"], data["operator"]["symmetric"]).imag, 4)

    def test_homothetic_current_covariant_derivative_is_twice_identity(self):
        self.assertClose(self.data["covariant_current_first"], 2*np.eye(4))

    def test_induced_current_divergence_is_eight_not_conserved(self):
        self.assertAlmostEqual(self.data["operator"]["current_divergence"], 8)
        self.assertAlmostEqual(np.trace(self.data["covariant_current_first"]), 8)

    def test_nonzero_curvature_annihilates_homothetic_current(self):
        result = np.einsum("abcd,b->acd", self.data["bundle"]["curvature"]["riemann"], self.data["coordinate_current"])
        self.assertClose(result, 0)

    def test_current_is_gradient_of_frame_norm_over_four(self):
        j_lower = self.data["bundle"]["metric"] @ self.data["coordinate_current"]
        norm_gradient = np.array([-8*self.data["time"], 0, 0, 0])
        self.assertClose(j_lower, norm_gradient/4)

    def test_correct_half_density_transport_preserves_equation(self):
        result = model.half_density_control(self.data)
        self.assertClose(result["operator"]["symmetric"], result["scaled_original_residual"])

    def test_correct_half_density_transport_preserves_coframe(self):
        result = model.half_density_control(self.data)
        self.assertClose(result["coframe"], self.data["frame"])
        self.assertAlmostEqual(result["normalized_imaginary_trace"], 4)

    def test_naive_half_density_rewrite_changes_the_dictionary(self):
        result = model.half_density_control(self.data)
        self.assertAlmostEqual(result["naive_coframe"][0, 0], 4)
        self.assertGreater(np.linalg.norm(result["naive_coframe"]-self.data["frame"]), 2.9)

    def test_actual_curved_background_Dirac_solution_exists_but_fails_coframe(self):
        result = model.background_dirac_control(self.data)
        self.assertLess(np.linalg.norm(result["operator"]["symmetric"]), 1e-12)
        self.assertAlmostEqual(result["operator"]["current_divergence"], 0)
        self.assertGreater(np.linalg.norm(result["coframe"]-self.data["frame"]), 1)

    def test_on_shell_background_control_has_exact_different_coframe(self):
        result = model.background_dirac_control(self.data)
        time = self.data["time"]
        target = time**(-3)*np.diag([-1.5/time, 0.5, 0.5, 0.5])
        self.assertClose(result["coframe"], target)

    def test_local_rephasing_keeps_composite_constraint_fixed(self):
        rng = np.random.default_rng(441)
        for _ in range(5):
            phase, gradient = np.exp(1j*rng.normal()), rng.normal(size=4)
            psi = phase*self.data["psi"]
            derivative = phase*(self.data["derivative"]+1j*gradient[:, None]*self.data["psi"])
            covariant = derivative+self.data["bundle"]["spin"] @ psi
            self.assertClose(model.coframe(psi, covariant), self.data["reconstructed"])

    def test_Dirac_local_phase_action_variation_is_only_standard_current(self):
        data = self.data
        gradient = np.array([0.2, 0.4, -0.3, 0.1])
        changed = data["derivative"]+1j*gradient[:, None]*data["psi"]
        args = data["weights"], data["bundle"]["spin"], data["mass"]*model.BETA
        difference = model.action_density(data["psi"], changed, *args)-model.action_density(data["psi"], data["derivative"], *args)
        self.assertAlmostEqual(difference, -data["coordinate_current"] @ gradient)

    def test_curved_multiplier_reaction_is_hermitian_and_phase_neutral(self):
        rng = np.random.default_rng(445)
        weight = model.multiplier_weight(rng.normal(size=(4, 4)), rng.normal(size=(4, 4, 4)), self.data["bundle"])
        self.assertClose(weight, weight.conj().T)
        self.assertAlmostEqual(np.vdot(self.data["psi"], weight @ self.data["psi"]).imag, 0)

    def test_multiplier_reaction_contains_curved_connection_term(self):
        multiplier = np.zeros((4, 4))
        multiplier[1, 1] = 1
        weight = model.multiplier_weight(multiplier, np.zeros((4, 4, 4)), self.data["bundle"])
        self.assertClose(weight, -model.K_FRAME[0]/2)

    def test_surviving_projector_can_have_zero_visible_defect(self):
        result = model.projection_control(self.data)
        self.assertAlmostEqual(np.linalg.norm(result["texture"]["P"]), 1)
        self.assertLess(np.linalg.norm(result["visible_hc"]), 1e-28)

    def test_comparison_core_is_spectral_projector_not_an_inserted_HC_load(self):
        result = model.projection_control(self.data)
        p, mass = result["texture"]["P"], result["mass"]
        self.assertClose(p @ p, p)
        self.assertClose(p.conj().T, p)
        self.assertClose(mass @ p, self.data["mass"]*p)
        self.assertClose((np.eye(2)-p) @ mass, (self.data["mass"]+0.6)*(np.eye(2)-p))

    def test_prepared_projector_connection_preserves_closed_subbundle(self):
        result = model.projection_control(self.data)
        t = result["texture"]
        covariant = t["P_first"]+t["connection"] @ t["P"]-t["P"] @ t["connection"]
        self.assertClose(covariant, 0)

    def test_isometric_compressed_connection_remains_antihermitian(self):
        result = model.projection_control(self.data)
        connection = result["reduced"]["connection"]
        self.assertClose(connection+connection.conj().swapaxes(-1, -2), 0)

    def test_internal_bundle_curvature_is_nonzero_but_real_coframe_unchanged(self):
        result = model.projection_control(self.data)
        self.assertGreater(np.linalg.norm(result["reduced"]["curvature"]), 0.16)
        self.assertClose(result["coframe"], self.data["frame"])

    def test_curved_full_and_projected_probe_operators_intertwine(self):
        result = model.projection_control(self.data)
        self.assertLess(result["lift_error"], 1e-12)
        self.assertAlmostEqual(result["imaginary_full_trace"], 4)

    def test_same_spectral_projector_does_not_determine_internal_connection_curvature(self):
        curved, flat = model.projection_control(self.data), model.projection_control(self.data, mix=1)
        self.assertClose(curved["texture"]["P"], flat["texture"]["P"])
        self.assertLess(np.linalg.norm(flat["reduced"]["curvature"]), 1e-12)
        self.assertClose(flat["coframe"], self.data["frame"])
        self.assertAlmostEqual(flat["imaginary_full_trace"], 4)

    def test_real_coframe_projection_identity_is_not_special_to_cone_polarization(self):
        rng = np.random.default_rng(719)
        data = dict(self.data)
        data["psi"] = rng.normal(size=4)+1j*rng.normal(size=4)
        data["derivative"] = rng.normal(size=(4, 4))+1j*rng.normal(size=(4, 4))
        result = model.projection_control(data)
        expected = model.coframe(data["psi"], data["derivative"]+data["bundle"]["spin"] @ data["psi"])
        self.assertClose(result["coframe"], expected)

    def test_invalid_times_grids_and_shapes_are_rejected(self):
        for time in (0, -1, np.inf, np.nan):
            with self.assertRaises(ValueError):
                model.cone_data(time)
        for count in (16, 66, True, 19.5):
            with self.assertRaises(ValueError):
                model.periodic_fixture(count)
        args = list(self.random_data())
        args[0] = np.zeros((1, 4))
        with self.assertRaises(ValueError):
            model.real_operator(*args)

    def test_nonhermitian_mass_or_kinetic_weights_are_not_silently_realified(self):
        for index in (2, 4, 5):
            args = list(self.random_data())
            args[index] = args[index]+1j*np.eye(4)
            with self.assertRaises(ValueError):
                model.real_operator(*args)

    def test_report_retains_changed_scope_and_native_obligations(self):
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertIn("OFF-SHELL", self.report["status"])
        self.assertTrue(self.report["phase_blind_composite_constraint"]["not_a_no_go_for_all_native_readouts_adjoint_choices_or_quantum_completions"])
        self.assertTrue(self.report["on_shell_fixed_cone_control"]["does_not_solve_the_joint_reconstruction"])

    def test_saved_results_track_stable_exact_claims_and_tolerant_numerics(self):
        for key in ("status", "source_conclusions", "fixed_background_real_action", "main_TeX_changed"):
            self.assertEqual(self.saved[key], self.report[key])
        for key in ("scalar_curvature", "imaginary_probe_trace", "phase_current_divergence", "compatibility_defect_norm"):
            self.assertClose(self.saved["curved_same_coframe_control"][key], self.report["curved_same_coframe_control"][key])
        self.assertLess(self.saved["independent_periodic_action_check"]["analytic_variation_error"], 1e-11)


if __name__ == "__main__":
    unittest.main()
