"""Finite supplied models for the conditional generation/closure interface.

Numerical regression checks supplement the written proofs. They neither
identify the native pacer nor certify physical lepton masses.
"""
import math
import unittest

import numpy as np


def adjoint(a):
    return a.conj().T


def positive_root(q, inverse=False):
    values, vectors = np.linalg.eigh(q)
    if inverse and min(values) <= 1e-12:
        raise ValueError("Closed seed Gram matrix is not positive definite")
    if min(values) < -1e-12:
        raise ValueError("Matrix is not positive semidefinite")
    roots = np.sqrt(np.maximum(values, 0))
    factors = 1/roots if inverse else roots
    return (vectors*factors) @ adjoint(vectors)


def closed_seeds(p, t):
    return p @ t @ positive_root(adjoint(t) @ p @ t, inverse=True)


def defect_gram(p, r, s):
    b = (np.eye(len(p))-p) @ r @ s
    return b, adjoint(b) @ b


def unitary_dilation(q):
    a, b = positive_root(np.eye(len(q))-q), positive_root(q)
    return np.block([[a, -b], [b, a]])


def cyclic_root(a, r, theta):
    u = np.roll(np.eye(3), 1, axis=0)
    z = r*np.exp(1j*theta)
    return a*np.eye(3)+z*u+z.conjugate()*adjoint(u)


def root_ratio(roots):
    return float(np.sum(np.abs(roots)**2)/np.sum(np.abs(roots))**2)


def spectral_ratio(q):
    values = np.linalg.eigvalsh(q)
    return root_ratio(np.sqrt(np.maximum(values, 0)))


class GenerationCouplingTests(unittest.TestCase):
    def setUp(self):
        self.p = np.diag([1.0]*3+[0.0]*3)
        self.s = np.eye(6)[:, :3]

    def assertMatrixEqual(self, left, right):
        np.testing.assert_allclose(left, right, atol=2e-12, rtol=2e-12)

    def test_projected_normalization_constructs_closed_odd_states(self):
        t = np.eye(9)[:, 3:6]
        c = np.array([0.6, 0.8, 0.6])
        h = np.array([0.8, 0.6, 0.8])
        w = t @ np.diag(c)+np.eye(9)[:, 6:9] @ np.diag(h)
        p = w @ adjoint(w)
        s = closed_seeds(p, t)
        j = np.diag([1.0]*3+[-1.0]*6)
        self.assertMatrixEqual(adjoint(s) @ s, np.eye(3))
        self.assertMatrixEqual(p @ s, s)
        self.assertMatrixEqual(j @ s, -s)
        self.assertMatrixEqual(s, w)

    def test_rank_deficient_projection_cannot_create_three_closed_seeds(self):
        p = np.diag([1.0, 1.0, 0.0, 0.0, 0.0, 0.0])
        with self.assertRaisesRegex(ValueError, "positive definite"):
            closed_seeds(p, self.s)

    def test_gram_normalization_can_mix_original_generation_slots(self):
        n = np.array([1.0, 1.0, 0.0, 1.0, 0.0, 0.0])/math.sqrt(3)
        p = np.eye(6)-np.outer(n, n)
        g = adjoint(self.s) @ p @ self.s
        self.assertGreater(abs(positive_root(g, inverse=True)[0, 1]), 0.1)
        s = closed_seeds(p, self.s)
        self.assertMatrixEqual(adjoint(s) @ s, np.eye(3))
        self.assertMatrixEqual(p @ s, s)

    def test_sector_preservation_commutes_not_anticommutes_with_odd_grading(self):
        j = -np.eye(3)
        a = np.array([[1, 2, 0], [0, 3, 1], [1, 0, 2]])
        self.assertMatrixEqual(j @ a, a @ j)
        self.assertMatrixEqual(j @ a+a @ j, -2*a)
        self.assertGreater(np.linalg.norm(j @ a+a @ j), 1)

    def test_generation_neutral_spectral_operator_gives_equal_slot_norms(self):
        operator = np.kron(np.diag([2.0, 5.0]), np.eye(3))
        states = np.eye(6)[:, 3:6]
        norms = np.sum(abs(operator @ states)**2, axis=0)
        self.assertMatrixEqual(norms, [25.0]*3)

    def test_closed_commutator_expectation_vanishes_but_transition_does_not(self):
        q = np.diag([0.04, 0.25, 0.64])
        r = unitary_dilation(q)
        commutator = r @ self.p-self.p @ r
        self.assertMatrixEqual(adjoint(self.s) @ commutator @ self.s, np.zeros((3, 3)))
        self.assertGreater(np.linalg.norm(commutator @ self.s), 0.5)
        self.assertMatrixEqual(commutator @ self.s, (np.eye(6)-self.p) @ r @ self.s)

    def test_defect_gram_is_the_positive_matrix_of_transition_inner_products(self):
        r = np.arange(36, dtype=float).reshape(6, 6)/17
        b, q = defect_gram(self.p, r, self.s)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(q[i, j], np.vdot(b[:, i], b[:, j]))
        self.assertGreaterEqual(min(np.linalg.eigvalsh(q)), -1e-12)

    def test_exact_closure_preserving_pacer_has_no_defect_coupling(self):
        r = np.diag([1, 2, 3, 4, 5, 6])
        b, q = defect_gram(self.p, r, self.s)
        self.assertMatrixEqual(b, np.zeros((6, 3)))
        self.assertMatrixEqual(q, np.zeros((3, 3)))

    def test_unitary_dilation_realizes_a_nondiagonal_positive_contraction(self):
        root = cyclic_root(0.35, 0.08, 0.7)
        q = adjoint(root) @ root
        r = unitary_dilation(q)
        self.assertMatrixEqual(adjoint(r) @ r, np.eye(6))
        self.assertMatrixEqual(r @ adjoint(r), np.eye(6))
        self.assertMatrixEqual(defect_gram(self.p, r, self.s)[1], q)

    def test_unitarity_alone_does_not_select_koide(self):
        q = np.diag([0.01, 0.09, 0.64])
        r = unitary_dilation(q)
        self.assertMatrixEqual(adjoint(r) @ r, np.eye(6))
        self.assertAlmostEqual(spectral_ratio(q), 0.74/1.44)
        self.assertGreater(abs(spectral_ratio(q)-2/3), 0.1)

    def test_equal_slot_diagonal_does_not_mean_equal_eigenmasses(self):
        q = np.ones((3, 3))/3
        slot_ratio = root_ratio(np.sqrt(np.diag(q)))
        self.assertAlmostEqual(slot_ratio, 1/3)
        # Exact spectrum is (1,0,0); avoid amplifying eigensolver roundoff at zero.
        self.assertMatrixEqual(np.linalg.eigvalsh(q), [0, 0, 1])
        self.assertAlmostEqual(root_ratio([1, 0, 0]), 1)

    def test_basis_change_preserves_spectrum_not_slot_mass_assignment(self):
        q = np.diag([1.0, 4.0, 9.0])
        v = np.array([[1, -1, 0], [1, 1, 0], [0, 0, math.sqrt(2)]])/math.sqrt(2)
        changed = adjoint(v) @ q @ v
        self.assertAlmostEqual(spectral_ratio(q), spectral_ratio(changed))
        self.assertGreater(abs(root_ratio(np.sqrt(np.diag(q)))-root_ratio(np.sqrt(np.diag(changed)))), 0.001)

    def test_cyclic_fourier_spectrum_is_the_brannen_harmonic(self):
        a, r, theta = 1.0, 0.31, 0.7
        l = cyclic_root(a, r, theta)
        expected = sorted(a+2*r*math.cos(theta+2*math.pi*k/3) for k in range(3))
        self.assertMatrixEqual(np.linalg.eigvalsh(l), expected)
        self.assertMatrixEqual(l, adjoint(l))

    def test_carrier_cycle_descends_to_a_cyclic_defect_gram(self):
        u = np.roll(np.eye(3), 1, axis=0)
        w = np.kron(np.eye(2), u)
        l = cyclic_root(0.35, 0.08, 0.7)
        r = unitary_dilation(l @ l)
        self.assertMatrixEqual(w @ self.p, self.p @ w)
        self.assertMatrixEqual(w @ self.s, self.s @ u)
        self.assertMatrixEqual(w @ r, r @ w)
        b, q = defect_gram(self.p, r, self.s)
        self.assertMatrixEqual(b @ u, w @ b)
        self.assertMatrixEqual(q @ u, u @ q)

    def test_positive_cyclic_gram_determines_root_coefficients_without_target_fit(self):
        u = np.roll(np.eye(3), 1, axis=0)
        l = cyclic_root(1.0, 0.31, 0.7)
        positive = positive_root(l @ l)
        a = np.trace(positive)/3
        z = np.trace(adjoint(u) @ positive)/3
        self.assertMatrixEqual(positive, a*np.eye(3)+z*u+z.conjugate()*adjoint(u))
        self.assertAlmostEqual(a.real, 1.0)
        self.assertAlmostEqual(abs(z), 0.31)
        self.assertAlmostEqual(np.angle(z), 0.7)

    def test_converse_includes_rank_deficient_positive_cyclic_gram(self):
        u = np.roll(np.eye(3), 1, axis=0)
        q = np.ones((3, 3))/3
        # Q is a projection, so its exact positive root is itself.
        a = np.trace(q)/3
        z = np.trace(adjoint(u) @ q)/3
        self.assertMatrixEqual(q, a*np.eye(3)+z*u+z*u.T)

    def test_positive_koide_radius_gives_two_thirds(self):
        a, r, theta = 1.0, 1/math.sqrt(2), 2.3
        l = cyclic_root(a, r, theta)
        self.assertGreater(min(np.linalg.eigvalsh(l)), 0)
        self.assertAlmostEqual(spectral_ratio(l @ l), 2/3, places=12)

    def test_cyclic_structure_does_not_select_the_koide_radius(self):
        for r in (0.0, 0.1, 0.3):
            l = cyclic_root(1.0, r, 0.4)
            self.assertAlmostEqual(spectral_ratio(l @ l), 1/3+2*r*r/3)
            self.assertGreater(abs(spectral_ratio(l @ l)-2/3), 0.2)

    def test_negative_root_eigenvalues_require_absolute_values(self):
        r = 1/math.sqrt(2)
        l = cyclic_root(1.0, r, math.pi)
        self.assertLess(min(np.linalg.eigvalsh(l)), 0)
        self.assertGreater(abs(spectral_ratio(l @ l)-(1/3+2*r*r/3)), 0.2)

    def test_real_symmetric_cyclic_matrix_has_a_degenerate_pair(self):
        values = np.linalg.eigvalsh(cyclic_root(1.0, 0.3, 0))
        self.assertMatrixEqual(values, [0.7, 0.7, 1.6])

    def test_complex_cyclic_matrix_splits_eigenvalues_while_slots_remain_equal(self):
        l = cyclic_root(1.0, 0.31, 0.7)
        u = np.roll(np.eye(3), 1, axis=0)
        q = l @ l
        self.assertMatrixEqual(q @ u, u @ q)
        self.assertGreater(min(np.diff(np.linalg.eigvalsh(q))), 0.1)
        self.assertMatrixEqual(np.diag(q), [np.trace(q)/3]*3)
        self.assertAlmostEqual(root_ratio(np.sqrt(np.real(np.diag(q)))), 1/3)

    def test_koide_root_positivity_has_three_narrow_phase_chambers(self):
        for theta in np.linspace(0, 2*math.pi, 721):
            distance = min(abs(math.atan2(math.sin(theta-2*math.pi*j/3),
                                         math.cos(theta-2*math.pi*j/3))) for j in range(3))
            in_chamber = distance <= math.pi/12+1e-12
            roots = np.linalg.eigvalsh(cyclic_root(1.0, 1/math.sqrt(2), theta))
            self.assertEqual(min(roots) >= -1e-12, in_chamber)

    def test_phase_boundary_makes_one_mass_quadratically_small(self):
        boundary = 3*math.pi/4
        a, scale = 2.0, 7.0
        for delta in (1e-3, 1e-5):
            theta = boundary-delta
            root = a*(1+math.sqrt(2)*math.cos(theta))
            mass = scale*root*root
            self.assertGreater(root, 0)
            self.assertLess(abs(mass/(scale*a*a*delta*delta)-1), 2*delta)
        other = [a*(1+math.sqrt(2)*math.cos(boundary+2*math.pi*k/3)) for k in (1, 2)]
        self.assertMatrixEqual(other, [a*(3-math.sqrt(3))/2, a*(3+math.sqrt(3))/2])

    def test_overall_pacer_phase_cancels_for_all_tested_frame_values(self):
        r = unitary_dilation(np.diag([0.04, 0.25, 0.64]))
        b0, q0 = defect_gram(self.p, r, self.s)
        for beta in (0.0, 0.25, 0.5493, 0.8):
            phase = np.exp(1j*math.pi*beta)
            b, q = defect_gram(self.p, phase*r, self.s)
            self.assertMatrixEqual(b, phase*b0)
            self.assertMatrixEqual(q, q0)

    def test_projected_internal_term_cannot_generate_a_complementary_transition(self):
        x = np.arange(36, dtype=float).reshape(6, 6)
        r = self.p @ x @ self.p
        self.assertMatrixEqual(defect_gram(self.p, r, self.s)[0], np.zeros((6, 3)))

    def test_absolute_commutator_expectation_also_loses_a_common_phase(self):
        r = unitary_dilation(np.diag([0.04, 0.25, 0.64]))
        state = np.ones(6)/math.sqrt(6)
        reference = abs(np.vdot(state, (r @ self.p-self.p @ r) @ state))
        self.assertGreater(reference, 0.1)
        for beta in (0.0, 0.25, 0.5493, 0.8):
            shifted = np.exp(1j*math.pi*beta)*r
            value = abs(np.vdot(state, (shifted @ self.p-self.p @ shifted) @ state))
            self.assertAlmostEqual(value, reference)

    def test_relative_phase_cancels_for_orthogonal_transition_channels(self):
        a = np.eye(6)[:, :3]
        b = np.eye(6)[:, 3:]
        self.assertMatrixEqual(adjoint(a) @ b, np.zeros((3, 3)))
        for phase in (1, 1j, np.exp(0.7j)):
            d = a+phase*b
            self.assertMatrixEqual(adjoint(d) @ d, 2*np.eye(3))

    def test_relative_interference_can_change_spectral_mass_ratios(self):
        a = np.diag([1.0, 2.0, 3.0])
        b = np.diag([0.3, 0.1, -0.2])
        q0 = adjoint(a+b) @ (a+b)
        d = a+1j*b
        q1 = adjoint(d) @ d
        self.assertGreater(abs(spectral_ratio(q0)-spectral_ratio(q1)), 0.005)
        self.assertMatrixEqual(q1, adjoint(a) @ a+adjoint(b) @ b+1j*adjoint(a) @ b-1j*adjoint(b) @ a)

    def test_varying_gram_matrix_can_be_only_a_basis_conjugation(self):
        a = np.diag([1.0, 0.0, 3.0])
        b = np.array([[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]])
        q0 = adjoint(a+b) @ (a+b)
        d = a+1j*b
        q1 = adjoint(d) @ d
        self.assertGreater(np.linalg.norm(q0-q1), 1)
        self.assertMatrixEqual(np.linalg.eigvalsh(q0), np.linalg.eigvalsh(q1))
        self.assertAlmostEqual(spectral_ratio(q0), spectral_ratio(q1))

    def test_reference_and_mass_scales_do_not_fix_the_koide_ratio(self):
        q = np.diag([0.04, 0.25, 0.64])
        self.assertAlmostEqual(spectral_ratio(q), spectral_ratio(7*q))
        self.assertAlmostEqual(spectral_ratio(q), spectral_ratio(q/9))

    def test_gram_mass_law_is_not_the_same_as_a_first_order_mass_operator(self):
        omega = np.diag([1.0, 2.0, 3.0])
        q = adjoint(omega) @ omega
        self.assertGreater(abs(spectral_ratio(omega)-spectral_ratio(q)), 0.02)
