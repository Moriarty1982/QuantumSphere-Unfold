"""Check the native coframe formula without promoting null stress matching to full closure."""
from pathlib import Path
import importlib.util
import json
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("hc_geometry", ROOT / "analysis/HC_Bilinear_Geometry_Bridge.py")
bridge = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bridge)


class HCBilinearGeometryBridgeTests(unittest.TestCase):
    def setUp(self):
        self.rng = np.random.default_rng(214)
        self.kappa = 0.4
        self.point = np.array([0.0, 0.2, 0.3, 0.0])

    def assertClose(self, actual, expected, atol=3e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-9)

    def profile(self, point=None):
        return bridge.logarithmic_profile((self.point if point is None else point)[1:3], self.kappa, 1.0)

    def geometry(self, point=None):
        p = self.profile(point)
        return bridge.null_geometry(p["amplitude"], p["gradient"], p["hessian"], self.kappa)

    def generic_probe(self):
        psi = self.rng.normal(size=(3, 4))+1j*self.rng.normal(size=(3, 4))
        derivatives = self.rng.normal(size=(4, 3, 4))+1j*self.rng.normal(size=(4, 3, 4))
        raw = self.rng.normal(size=(4, 3, 3))+1j*self.rng.normal(size=(4, 3, 3))
        gauge = (raw+raw.conj().swapaxes(-1, -2))/2
        weights, beta = bridge.spin_weights()
        hc = np.diag([0.7, 0.8, 0.9])
        return psi, derivatives, gauge, hc, weights, beta

    def test_declared_four_spinor_matrices_have_a_consistent_3_plus_1_clifford_convention(self):
        weights, beta = bridge.spin_weights()
        gamma = beta @ weights
        for a in range(4):
            for b in range(4):
                self.assertClose(gamma[a] @ gamma[b]+gamma[b] @ gamma[a], -2*bridge.ETA[a, b]*np.eye(4))

    def test_timelike_current_spinor_realizes_the_given_current(self):
        weights, _ = bridge.spin_weights()
        for _ in range(10):
            spatial = self.rng.normal(size=3)
            current = np.r_[np.linalg.norm(spatial)+1, spatial]
            state, _ = bridge.timelike_current_spinor(current)
            self.assertClose([np.vdot(state, k @ state).real for k in weights], current)

    def test_current_spinor_jacobian_matches_independent_finite_differences(self):
        current, step = np.array([5.0, 0.4, 0.6, -1.0]), 1e-5
        _, jacobian = bridge.timelike_current_spinor(current)
        for mu, delta in enumerate(step*np.eye(4)):
            plus, minus = bridge.timelike_current_spinor(current+delta)[0], bridge.timelike_current_spinor(current-delta)[0]
            self.assertClose((plus-minus)/(2*step), jacobian[mu], atol=4e-11)

    def test_unsupported_spacelike_or_past_current_is_rejected(self):
        for current in [[-2, 0, 0, 0], [1, 2, 0, 0], [1, 1, 0, 0]]:
            with self.assertRaises(ValueError):
                bridge.timelike_current_spinor(current)

    def test_real_coframe_is_half_current_gradient_plus_hc_rank_one_update(self):
        fields = self.generic_probe()
        reading = bridge.probe_coframe(*fields, bridge.N_COV, self.kappa)
        expected = reading["baseline"]+self.kappa*np.outer(reading["direction"], bridge.N_COV)
        self.assertClose(reading["coframe"], expected)
        psi, derivatives, _, _, weights, _ = fields
        for a, k in enumerate(weights):
            for mu, derivative in enumerate(derivatives):
                derivative_current = np.vdot(derivative, psi @ k.T)+np.vdot(psi, derivative @ k.T)
                self.assertClose(reading["baseline"][a, mu], derivative_current.real/2)

    def test_pure_internal_unitary_gauge_field_drops_from_this_factorized_real_coframe(self):
        fields = list(self.generic_probe())
        with_gauge = bridge.probe_coframe(*fields, bridge.N_COV, self.kappa)
        fields[2] = np.zeros_like(fields[2])
        without_gauge = bridge.probe_coframe(*fields, bridge.N_COV, self.kappa)
        self.assertClose(with_gauge["coframe"], without_gauge["coframe"])

    def test_hc_survives_in_coframe_even_when_its_i_weighted_probe_term_is_purely_imaginary(self):
        fields = list(self.generic_probe())
        reading = bridge.probe_coframe(*fields, bridge.N_COV, self.kappa)
        without_hc = bridge.probe_coframe(*fields, bridge.N_COV, 0)
        self.assertGreater(np.linalg.norm(reading["coframe"]-without_hc["coframe"]), 0.1)
        psi, derivatives, gauge, hc, weights, beta = fields
        literal = bridge.probe.literal_probe_density(psi, derivatives, gauge, hc, weights, beta, bridge.N_COV, self.kappa)
        zero = bridge.probe.literal_probe_density(psi, derivatives, gauge, hc, weights, beta, bridge.N_COV, 0)
        self.assertAlmostEqual((literal-zero).real, 0)

    def test_same_constructive_probe_gives_identity_baseline_and_aligned_hc_direction(self):
        h = self.profile()["amplitude"]
        reading = bridge.constructive_probe(self.point, h, self.kappa)
        self.assertClose(reading["baseline"], np.eye(4))
        self.assertClose(reading["direction"], h*bridge.L_VECTOR)
        self.assertClose(reading["coframe"], np.eye(4)+self.kappa*h*np.outer(bridge.L_VECTOR, bridge.N_COV))
        self.assertGreaterEqual(np.linalg.eigvalsh(reading["hc"])[0], 0)

    def test_constructed_current_is_the_coordinate_map_on_a_local_patch(self):
        for point in [self.point, [0.1, -0.2, 0.3, 0.2], [-0.1, 0.1, 0.2, 0.1]]:
            reading = bridge.constructive_probe(point, 0.7, self.kappa)
            self.assertClose(reading["frame_current"], 2*(np.array(point)+[3, 0, 0, 0]))
            self.assertClose(reading["baseline"], np.eye(4))

    def test_aligned_hc_is_geometrically_active_but_direct_probe_transport_dark(self):
        reading = bridge.constructive_probe(self.point, self.profile()["amplitude"], self.kappa)
        frame_n = np.linalg.solve(reading["coframe"].T, bridge.N_COV)
        self.assertClose(frame_n, bridge.N_COV)
        slash = np.einsum("a,aij->ij", frame_n, reading["weights"])
        self.assertClose(reading["hc"] @ reading["psi"] @ slash.T, np.zeros_like(reading["psi"]))
        self.assertGreater(np.linalg.norm(reading["direction"]), 1)
        self.assertGreater(np.linalg.norm(reading["hc"] @ reading["psi"] @ reading["spin_metric"].T), 1)

    def test_local_common_phase_change_does_not_change_this_real_coframe(self):
        fields = list(self.generic_probe())
        original = bridge.probe_coframe(*fields, bridge.N_COV, self.kappa)
        psi, derivatives = fields[:2]
        phase, phase_gradient = np.exp(0.3j), self.rng.normal(size=4)
        fields[0] = phase*psi
        fields[1] = phase*(derivatives+1j*phase_gradient[:, None, None]*psi)
        changed = bridge.probe_coframe(*fields, bridge.N_COV, self.kappa)
        self.assertClose(changed["coframe"], original["coframe"])

    def test_internal_basis_change_preserves_coframe_and_metric(self):
        fields = list(self.generic_probe())
        original = bridge.probe_coframe(*fields, bridge.N_COV, self.kappa)
        raw = self.rng.normal(size=(3, 3))+1j*self.rng.normal(size=(3, 3))
        u, _ = np.linalg.qr(raw)
        fields[0], fields[1] = u @ fields[0], u @ fields[1]
        fields[2], fields[3] = u @ fields[2] @ u.conj().T, u @ fields[3] @ u.conj().T
        changed = bridge.probe_coframe(*fields, bridge.N_COV, self.kappa)
        self.assertClose(changed["metric"], original["metric"])

    def rank_one_data(self):
        background = np.eye(4)+0.1*self.rng.normal(size=(4, 4))
        direction = self.rng.normal(size=4)
        n = background.T @ bridge.N_COV
        return background, direction, n

    def test_general_rank_one_metric_expansion(self):
        data = self.rank_one_data()
        reading = bridge.rank_one_update(*data, self.kappa)
        self.assertClose(reading["metric"], reading["expanded_metric"])

    def test_rank_one_determinant_and_volume_factor(self):
        background, direction, n = self.rank_one_data()
        reading = bridge.rank_one_update(background, direction, n, self.kappa)
        self.assertClose(np.linalg.det(reading["coframe"]), np.linalg.det(background)*reading["determinant_factor"])
        self.assertClose(np.linalg.det(reading["metric"]), np.linalg.det(reading["baseline_metric"])*reading["determinant_factor"]**2)

    def test_rank_one_inverse_and_null_preservation(self):
        reading = bridge.rank_one_update(*self.rank_one_data(), self.kappa)
        self.assertClose(reading["inverse_metric"], np.linalg.inv(reading["metric"]))
        self.assertAlmostEqual(reading["baseline_null_square"], 0)
        self.assertAlmostEqual(reading["updated_null_square_prediction"], 0)

    def test_null_square_transformation_also_holds_for_nonnull_covectors(self):
        background, direction, _ = self.rank_one_data()
        n = self.rng.normal(size=4)
        reading = bridge.rank_one_update(background, direction, n, 0.1)
        self.assertClose(n @ np.linalg.solve(reading["metric"], n), reading["updated_null_square_prediction"])

    def test_hc_only_rank_one_coframe_cannot_supply_four_dimensions(self):
        hc_only = self.kappa*np.outer(bridge.L_VECTOR, bridge.N_COV)
        self.assertEqual(np.linalg.matrix_rank(hc_only), 1)
        self.assertEqual(np.linalg.det(hc_only), 0)

    def test_singular_rank_one_denominator_is_not_a_valid_metric(self):
        direction = np.array([1.0, 0, 0, 0])
        with self.assertRaises(ValueError):
            bridge.rank_one_update(np.eye(4), direction, [1, 0, 0, 0], -1)

    def test_aligned_null_metric_has_lorentz_signature_and_fixed_volume(self):
        nn = np.outer(bridge.N_COV, bridge.N_COV)
        for h in [-5, -1, 0, 1, 5]:
            g = bridge.null_geometry(h, [0, 0], np.zeros((2, 2)), self.kappa)["metric"]
            self.assertClose(g, bridge.ETA+2*self.kappa*h*nn)
            self.assertAlmostEqual(np.linalg.det(g), -1)
            self.assertEqual(np.count_nonzero(np.linalg.eigvalsh(g) < 0), 1)
            self.assertAlmostEqual(bridge.N_COV @ np.linalg.solve(g, bridge.N_COV), 0)

    def test_constructed_probe_and_independently_computed_null_metric_agree(self):
        reading = bridge.constructive_probe(self.point, self.profile()["amplitude"], self.kappa)
        self.assertClose(reading["metric"], self.geometry()["metric"])

    def test_null_axis_is_parallel_in_the_specific_transverse_metric(self):
        geometry = self.geometry()
        self.assertClose(np.einsum("a,abc->bc", bridge.N_COV, geometry["connection"]), np.zeros((4, 4)))

    def test_metric_jets_match_independent_profile_differences(self):
        geometry, step = self.geometry(), 1e-5
        for axis, delta in enumerate(step*np.eye(4)):
            plus, minus = self.geometry(self.point+delta), self.geometry(self.point-delta)
            self.assertClose((plus["metric"]-minus["metric"])/(2*step), geometry["metric_first"][axis], atol=4e-11)
            self.assertClose((plus["metric_first"]-minus["metric_first"])/(2*step), geometry["metric_second"][axis], atol=4e-11)

    def test_christoffel_derivatives_match_independent_metric_jet_evaluations(self):
        geometry, step = self.geometry(), 1e-5
        for axis, delta in enumerate(step*np.eye(4)):
            plus, minus = self.geometry(self.point+delta), self.geometry(self.point-delta)
            self.assertClose((plus["connection"]-minus["connection"])/(2*step), geometry["connection_derivative"][axis], atol=2e-11)

    def test_full_riemann_tensor_matches_the_closed_null_profile_formula(self):
        gradient, hessian = np.array([0.2, -0.1]), np.array([[0.1, 0.03], [0.03, -0.2]])
        geometry = bridge.null_geometry(0.7, gradient, hessian, self.kappa)
        h, n = np.zeros((4, 4)), bridge.N_COV
        h[1:3, 1:3] = hessian
        expected = np.empty((4, 4, 4, 4))
        for a, b, c, d in np.ndindex((4, 4, 4, 4)):
            expected[a, b, c, d] = self.kappa*(n[a]*n[d]*h[b, c]+n[b]*n[c]*h[a, d]
                                               -n[a]*n[c]*h[b, d]-n[b]*n[d]*h[a, c])
        self.assertClose(geometry["lower_riemann"], expected)

    def test_riemann_symmetries_and_first_bianchi_identity(self):
        riemann = self.geometry()["lower_riemann"]
        self.assertClose(riemann, -riemann.swapaxes(0, 1))
        self.assertClose(riemann, -riemann.swapaxes(2, 3))
        self.assertClose(riemann, riemann.transpose(2, 3, 0, 1))
        self.assertClose(riemann+riemann.transpose(0, 3, 1, 2)+riemann.transpose(0, 2, 3, 1), 0*riemann)

    def test_ricci_is_null_and_scalar_curvature_zero(self):
        geometry = self.geometry()
        self.assertClose(geometry["ricci"], geometry["ricci_coefficient"]*np.outer(bridge.N_COV, bridge.N_COV))
        self.assertAlmostEqual(geometry["scalar"], 0)
        self.assertClose(geometry["einstein"], geometry["ricci"])

    def test_zero_scalar_curvature_and_zero_kretschmann_do_not_mean_flatness(self):
        geometry = self.geometry()
        inverse, riemann = np.linalg.inv(geometry["metric"]), geometry["lower_riemann"]
        kretschmann = np.einsum("abcd,ae,bf,cg,dh,efgh", riemann, inverse, inverse, inverse, inverse, riemann)
        self.assertAlmostEqual(kretschmann, 0)
        self.assertGreater(np.linalg.norm(riemann), 0.009)

    def test_anholonomic_coframe_is_not_by_itself_evidence_of_curvature(self):
        gradient = np.array([0.2, -0.1])
        geometry = bridge.null_geometry(0.7, gradient, np.zeros((2, 2)), self.kappa)
        self.assertGreater(np.linalg.norm(geometry["metric_first"]), 0.1)
        self.assertClose(geometry["riemann"], np.zeros((4, 4, 4, 4)))

    def test_curvature_action_stress_matches_the_positive_null_tensor(self):
        geometry = self.geometry()
        expected = geometry["stress_coefficient"]*np.outer(bridge.N_COV, bridge.N_COV)
        self.assertClose(geometry["hc_stress"], expected)
        self.assertAlmostEqual(geometry["hc_curvature_squared_trace"], 0)
        for vector in self.rng.normal(size=(5, 4)):
            self.assertGreaterEqual(vector @ expected @ vector, 0)

    def test_null_stress_is_covariantly_conserved_in_the_chosen_metric(self):
        geometry, p = self.geometry(), self.profile()
        inverse = np.linalg.inv(geometry["metric"])
        up_stress = inverse @ geometry["hc_stress"] @ inverse
        coefficient_gradient = np.zeros(4)
        coefficient_gradient[1:3] = 2*self.kappa**2*p["hessian"] @ p["gradient"]
        n_up = inverse @ bridge.N_COV
        partial = (coefficient_gradient @ n_up)*n_up
        gamma = geometry["connection"]
        divergence = partial+np.einsum("mml,ln->n", gamma, up_stress)+np.einsum("nml,ml->n", gamma, up_stress)
        self.assertClose(divergence, np.zeros(4))

    def test_logarithmic_profile_derivatives_match_finite_differences(self):
        profile, step = self.profile(), 1e-5
        for axis in range(2):
            delta = np.zeros(4)
            delta[axis+1] = step
            plus, minus = self.profile(self.point+delta), self.profile(self.point-delta)
            self.assertClose((plus["amplitude"]-minus["amplitude"])/(2*step), profile["gradient"][axis], atol=3e-11)
            self.assertClose((plus["gradient"]-minus["gradient"])/(2*step), profile["hessian"][axis], atol=3e-11)

    def test_logarithmic_profile_solves_the_transverse_nonlinear_matching_equation(self):
        for xy in [[0.2, 0.3], [1, -1], [-1, 0.5]]:
            profile = bridge.logarithmic_profile(xy, self.kappa, 1, slope=[0.1, 0.2])
            residual = np.trace(profile["hessian"])+profile["a"]*(profile["gradient"] @ profile["gradient"])
            self.assertAlmostEqual(residual, 0)
            self.assertGreater(profile["amplitude"], 0)

    def test_conditional_full_einstein_tensor_matches_hc_stress_but_is_nonflat(self):
        for coupling, gravitational, trace in [(0.4, 1, 1), (0.2, 0.7, 2), (0.5, 2, 1.2)]:
            p = bridge.logarithmic_profile(self.point[1:3], coupling, gravitational, trace)
            geometry = bridge.null_geometry(p["amplitude"], p["gradient"], p["hessian"], coupling, trace)
            self.assertClose(geometry["einstein"], gravitational*geometry["hc_stress"])
            self.assertGreater(np.linalg.norm(geometry["lower_riemann"]), 0)

    def test_harmonic_metric_profile_does_not_match_its_nonzero_hc_stress(self):
        geometry = bridge.null_geometry(0.7, [0.02, -0.03], [[0.1, 0], [0, -0.1]], self.kappa)
        self.assertClose(geometry["ricci"], np.zeros((4, 4)))
        self.assertGreater(np.linalg.norm(geometry["hc_stress"]), 0.0004)

    def test_geometric_hc_source_is_the_finite_variation_of_the_bilinear_metric(self):
        fields = list(self.generic_probe())
        psi, _, _, hc, weights, beta = fields
        reading = bridge.probe_coframe(*fields, bridge.N_COV, self.kappa)
        raw = self.rng.normal(size=(3, 3))+1j*self.rng.normal(size=(3, 3))
        direction = (raw+raw.conj().T)/2
        residual = self.rng.normal(size=(4, 4))
        residual = (residual+residual.T)/2
        source = bridge.geometric_hc_source(psi, weights, beta, reading["coframe"], residual, bridge.N_COV, self.kappa)
        step = 1e-5
        fields[3] = hc+step*direction
        plus = bridge.probe_coframe(*fields, bridge.N_COV, self.kappa)["metric"]
        fields[3] = hc-step*direction
        minus = bridge.probe_coframe(*fields, bridge.N_COV, self.kappa)["metric"]
        derivative = np.einsum("ab,ab", residual, plus-minus)/(4*step)
        self.assertClose(derivative, np.trace(source @ direction).real, atol=2e-7)

    def test_restricting_to_null_metric_variations_loses_a_nonzero_einstein_residual(self):
        geometry = bridge.null_geometry(0.7, [0.02, -0.03], [[0.1, 0], [0, -0.1]], self.kappa)
        residual = geometry["einstein"]-geometry["hc_stress"]
        inverse = np.linalg.inv(geometry["metric"])
        raised = inverse @ residual @ inverse
        self.assertGreater(np.linalg.norm(residual), 0.0004)
        self.assertClose(np.einsum("ab,ab", raised, geometry["restricted_metric_tangent"]), 0)

    def test_all_hc_metric_source_directions_can_miss_the_same_null_residual(self):
        geometry = bridge.null_geometry(0.7, [0.02, -0.03], [[0.1, 0], [0, -0.1]], self.kappa)
        fields = bridge.constructive_probe(self.point, 0.7, self.kappa)
        inverse = np.linalg.inv(geometry["metric"])
        residual = inverse @ (geometry["einstein"]-geometry["hc_stress"]) @ inverse
        source = bridge.geometric_hc_source(fields["psi"], fields["weights"], fields["spin_metric"],
                                             fields["coframe"], residual, bridge.N_COV, self.kappa)
        self.assertClose(source, np.zeros((3, 3)))

    def test_constructive_geometry_is_not_claimed_to_solve_the_nonzero_probe_gauss_source(self):
        fields = bridge.constructive_probe(self.point, self.profile()["amplitude"], self.kappa)
        self.assertGreater(fields["unsatisfied_zero_gauge_Gauss_source_norm"], 5)

    def same_frame_data(self):
        fields = bridge.constructive_probe(self.point, self.profile()["amplitude"], self.kappa)
        dcov = fields["derivatives"]+self.kappa*bridge.N_COV[:, None, None]*(fields["hc"] @ fields["psi"])
        gamma = fields["spin_metric"] @ fields["weights"]
        image = 0.6*fields["psi"]+0.2*fields["hc"] @ fields["psi"]
        return fields, dcov, gamma, image

    def test_same_frame_trace_identity_detects_an_exact_nonzero_master_residual(self):
        fields, dcov, gamma, image = self.same_frame_data()
        result = bridge.induced_dirac_contraction(fields["psi"], dcov, gamma, fields["spin_metric"], image)
        self.assertClose(result["coframe"], fields["coframe"])
        self.assertClose(result["coframe_trace"], 4)
        self.assertClose(result["scalar_mass"].imag, 0)
        self.assertClose(result["scalar_residual"].imag, 4)

    def test_same_frame_coordinate_gammas_obey_the_induced_clifford_relation(self):
        fields, dcov, gamma, image = self.same_frame_data()
        result = bridge.induced_dirac_contraction(fields["psi"], dcov, gamma, fields["spin_metric"], image)
        inverse_metric = np.linalg.inv(fields["metric"])
        for mu in range(4):
            for nu in range(4):
                a, b = result["coordinate_gamma"][mu], result["coordinate_gamma"][nu]
                self.assertClose(a @ b+b @ a, -2*inverse_metric[mu, nu]*np.eye(4))

    def test_any_real_central_or_yukawa_coefficient_leaves_the_trace_obstruction(self):
        fields, dcov, gamma, _ = self.same_frame_data()
        for mass, yukawa in [(0, 0), (0.6, 0.2), (-1, 2), (10, -3)]:
            image = mass*fields["psi"]+yukawa*fields["hc"] @ fields["psi"]
            result = bridge.induced_dirac_contraction(fields["psi"], dcov, gamma, fields["spin_metric"], image)
            self.assertClose(result["scalar_residual"].imag, 4)

    def test_trace_obstruction_does_not_require_factorization_of_the_mass_operator(self):
        fields, dcov, gamma, _ = self.same_frame_data()
        size = fields["psi"].size
        raw = self.rng.normal(size=(size, size))+1j*self.rng.normal(size=(size, size))
        weighted_mass = (raw+raw.conj().T)/2
        full_adjoint = np.kron(np.eye(3), fields["spin_metric"])
        image = np.linalg.solve(full_adjoint, weighted_mass @ fields["psi"].reshape(-1)).reshape(3, 4)
        result = bridge.induced_dirac_contraction(fields["psi"], dcov, gamma, fields["spin_metric"], image)
        self.assertClose(result["scalar_mass"].imag, 0)
        self.assertClose(result["scalar_residual"].imag, 4)

    def test_finite_real_coframe_normalization_changes_the_number_not_the_contradiction(self):
        fields, dcov, gamma, image = self.same_frame_data()
        for scale in [0.5, 1, 2, -1]:
            result = bridge.induced_dirac_contraction(fields["psi"], dcov, gamma, fields["spin_metric"], image, scale)
            self.assertClose(result["coframe_trace"], 4)
            self.assertClose(result["scalar_residual"].imag, 4/scale)
            self.assertGreater(result["residual_norm_lower_bound"], 0)

    def test_internal_hermitian_gauge_fields_cannot_cancel_the_same_frame_imaginary_residual(self):
        fields, dcov, gamma, image = self.same_frame_data()
        original = bridge.induced_dirac_contraction(fields["psi"], dcov, gamma, fields["spin_metric"], image)
        raw = self.rng.normal(size=(4, 3, 3))+1j*self.rng.normal(size=(4, 3, 3))
        gauge = (raw+raw.conj().swapaxes(-1, -2))/2
        changed = bridge.induced_dirac_contraction(fields["psi"], dcov+1j*gauge @ fields["psi"], gamma,
                                                   fields["spin_metric"], image)
        self.assertClose(changed["coframe"], original["coframe"])
        self.assertClose(changed["scalar_residual"].imag, 4)

    def test_cauchy_bound_gives_a_strictly_positive_same_frame_residual_norm(self):
        fields, dcov, gamma, image = self.same_frame_data()
        result = bridge.induced_dirac_contraction(fields["psi"], dcov, gamma, fields["spin_metric"], image)
        self.assertClose(result["residual_norm_lower_bound"], 4/np.sqrt(6))
        self.assertGreaterEqual(result["residual_norm"], result["residual_norm_lower_bound"])

    def test_constant_probe_phase_does_not_change_the_trace_identity(self):
        fields, dcov, gamma, image = self.same_frame_data()
        phase = np.exp(0.3j)
        result = bridge.induced_dirac_contraction(phase*fields["psi"], phase*dcov, gamma,
                                                  fields["spin_metric"], phase*image)
        self.assertClose(result["scalar_residual"].imag, 4)

    def test_nonreal_mass_image_can_escape_the_real_mass_hypothesis_but_is_not_a_native_fix(self):
        fields, dcov, gamma, image = self.same_frame_data()
        first = bridge.induced_dirac_contraction(fields["psi"], dcov, gamma, fields["spin_metric"], image)
        changed = bridge.induced_dirac_contraction(fields["psi"], dcov, gamma, fields["spin_metric"], 1j*first["slash"])
        self.assertClose(changed["probe_residual"], np.zeros_like(image))
        self.assertClose(changed["scalar_mass"].imag, 4)

    def test_reference_gamma_master_equation_does_not_imply_the_same_induced_gamma_identification(self):
        psi, dcov, _, _, weights, beta = self.generic_probe()
        gamma, image = beta @ weights, 0.6*psi
        spatial = sum(dcov[mu] @ gamma[mu].T for mu in range(1, 4))
        dcov[0] = (-spatial-1j*image) @ np.linalg.inv(gamma[0]).T
        reference_residual = 1j*sum(derivative @ g.T for derivative, g in zip(dcov, gamma))-image
        self.assertClose(reference_residual, np.zeros_like(psi))
        result = bridge.induced_dirac_contraction(psi, dcov, gamma, beta, image)
        self.assertEqual(np.linalg.matrix_rank(result["coframe"]), 4)
        self.assertClose(result["scalar_residual"].imag, 4)
        self.assertGreater(result["residual_norm"], 0.1)

    def test_induced_current_divergence_matches_finite_volume_current_differences(self):
        fields = bridge.constructive_probe(self.point, self.profile()["amplitude"], self.kappa)
        gradient = np.r_[0, self.profile()["gradient"], 0]
        de = self.kappa*np.einsum("l,a,m->lam", gradient, bridge.L_VECTOR, bridge.N_COV)
        balance = bridge.coordinate_current_balance(fields["frame_current"], 2*np.eye(4), fields["coframe"], de)
        step, divergence = 1e-5, 0.0
        for mu, delta in enumerate(step*np.eye(4)):
            values = []
            for point in [self.point+delta, self.point-delta]:
                changed = bridge.constructive_probe(point, self.profile(point)["amplitude"], self.kappa)
                volume = abs(np.linalg.det(changed["coframe"]))
                values.append(volume*np.linalg.solve(changed["coframe"], changed["frame_current"])[mu])
            divergence += (values[0]-values[1])/(2*step)
        self.assertClose(divergence/balance["volume"], balance["divergence"], atol=3e-10)
        self.assertClose(balance["divergence"], 8)

    def test_any_transverse_aligned_h_profile_leaves_the_divergence_eight(self):
        for h, gradient in [(0, [0, 0]), (0.7, [0.2, -0.3]), (1.5, [-1, 2])]:
            fields = bridge.constructive_probe(self.point, h, self.kappa)
            de = self.kappa*np.einsum("l,a,m->lam", np.r_[0, gradient, 0], bridge.L_VECTOR, bridge.N_COV)
            balance = bridge.coordinate_current_balance(fields["frame_current"], 2*np.eye(4), fields["coframe"], de)
            self.assertClose(balance["divergence"], 8)

    def test_nonlinear_gradient_coframe_has_the_same_invariant_divergence_obstruction(self):
        coordinates = np.array([0.1, 0.2, -0.1, 0.3])
        y = np.exp(coordinates)+np.array([4, 0, 0, 0])
        jacobian = np.diag(np.exp(coordinates))
        de = np.zeros((4, 4, 4))
        for a in range(4):
            de[a, a, a] = np.exp(coordinates[a])
        balance = bridge.coordinate_current_balance(2*y, 2*jacobian.T, jacobian, de)
        self.assertClose(balance["divergence"], 8)

    def test_gauge_commutators_have_zero_trace_and_cannot_cancel_central_current_divergence(self):
        fields = bridge.constructive_probe(self.point, self.profile()["amplitude"], self.kappa)
        frame = bridge.probe.probe_currents(fields["psi"], fields["weights"], fields["spin_metric"])["gauge"]
        current = np.einsum("ma,aij->mij", np.linalg.inv(fields["coframe"]), frame)
        raw = self.rng.normal(size=(4, 3, 3))+1j*self.rng.normal(size=(4, 3, 3))
        gauge = (raw+raw.conj().swapaxes(-1, -2))/2
        commutator = 1j*np.sum(gauge @ current-current @ gauge, axis=0)
        self.assertClose(np.trace(commutator), 0)

    def test_leaving_the_transverse_profile_can_fix_continuity_but_not_the_same_frame_trace(self):
        fields, dcov, gamma, image = self.same_frame_data()
        s = bridge.N_COV @ (self.point+np.array([3, 0, 0, 0]))
        gradient = np.zeros(4)
        gradient[0] = 4/(self.kappa*s)
        de = self.kappa*np.einsum("l,a,m->lam", gradient, bridge.L_VECTOR, bridge.N_COV)
        balance = bridge.coordinate_current_balance(fields["frame_current"], 2*np.eye(4), fields["coframe"], de)
        self.assertClose(balance["divergence"], 0)
        result = bridge.induced_dirac_contraction(fields["psi"], dcov, gamma, fields["spin_metric"], image)
        self.assertClose(result["scalar_residual"].imag, 4)

    def test_same_frame_check_rejects_degenerate_coframe_and_zero_normalization(self):
        fields, dcov, gamma, image = self.same_frame_data()
        with self.assertRaises(ValueError):
            bridge.induced_dirac_contraction(fields["psi"], np.zeros_like(dcov), gamma, fields["spin_metric"], image)
        with self.assertRaises(ValueError):
            bridge.induced_dirac_contraction(fields["psi"], dcov, gamma, fields["spin_metric"], image, 0)
        with self.assertRaises(ValueError):
            bridge.coordinate_current_balance(np.ones(4), np.eye(4), np.zeros((4, 4)), np.zeros((4, 4, 4)))

    def test_report_exposes_the_stronger_same_frame_and_current_obstructions(self):
        report = bridge.evaluate()["follow_through_current_and_same_frame_obstruction"]
        self.assertClose(report["example_covariant_divergence"], 8)
        self.assertClose(report["sample_Im_barPsi_R"], 4)
        self.assertGreater(report["sample_probe_residual_norm"], report["sample_residual_norm_lower_bound"])
        self.assertIn("does not yet fix", report["not_a_global_no_go_for_the_paper"])

    def test_bad_metric_jets_and_zero_volume_are_rejected(self):
        geometry = self.geometry()
        with self.assertRaises(ValueError):
            bridge.metric_curvature(np.zeros((4, 4)), geometry["metric_first"], geometry["metric_second"])
        bad = geometry["metric_second"].copy()
        bad[0, 1, 2, 3] = 1
        with self.assertRaises(ValueError):
            bridge.metric_curvature(geometry["metric"], geometry["metric_first"], bad)

    def test_logarithmic_solution_is_guarded_by_its_local_domain_and_nonzero_couplings(self):
        with self.assertRaises(ValueError):
            bridge.logarithmic_profile([0, 0], 0, 1)
        with self.assertRaises(ValueError):
            bridge.logarithmic_profile([0, 0], 0.4, 1, intercept=-1)
        with self.assertRaises(ValueError):
            bridge.logarithmic_profile([0, 0], 0.4, 1, trace_t_squared=0)

    def test_report_keeps_the_exact_closure_and_missing_field_equation_boundaries(self):
        report = bridge.evaluate()
        json.dumps(report, allow_nan=False)
        self.assertFalse(report["main_TeX_changed"])
        self.assertTrue(report["same_probe_constructive_local_witness"]["probe_gauge_projector_and_matching_equations_not_solved"])
        self.assertTrue(report["native_scope_boundary"]["no_native_G_Newton_mass_phase_gravitational_bath_or_full_solution_derived"])
        self.assertGreater(report["same_probe_constructive_local_witness"]["unsatisfied_zero_gauge_Gauss_source_norm"], 5)

    def test_saved_report_reproduces_the_calculation(self):
        saved = json.loads((ROOT / "analysis/HC_Bilinear_Geometry_Bridge.json").read_text(encoding="utf-8"))
        self.assertEqual(saved, bridge.evaluate())


if __name__ == "__main__":
    unittest.main()
