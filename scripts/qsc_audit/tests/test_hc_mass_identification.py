"""Exact finite operator examples for the conditional HC/mass interface.

The examples test the written claims; none is a recovered native coupling.
"""
from fractions import Fraction as Q
from itertools import product
import math
import unittest


def matrix(rows):
    return tuple(tuple(Q(x) for x in row) for row in rows)


def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def transpose(a):
    return tuple(zip(*a))


def mm(a, b):
    return tuple(tuple(sum(x*y for x, y in zip(row, col))
                       for col in transpose(b)) for row in a)


def mv(a, v):
    return tuple(sum(x*y for x, y in zip(row, v)) for row in a)


def combine(a, b, ca=1, cb=1):
    return tuple(tuple(ca*x+cb*y for x, y in zip(ra, rb))
                 for ra, rb in zip(a, b))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def koide(roots):
    return dot(roots, roots)/sum(roots)**2


def cycle(values):
    return values[1:] + values[:1]


def j_state(state):
    return tuple(x if i < 3 else -x for i, x in enumerate(state))


def residual_mass(state, coupling, scale=Q(3)):
    # J=diag(I_3,-I_3); the last three entries are P_- state's coordinates.
    output = mv(coupling, state[3:])
    return scale*dot(output, output)


class HCMassIdentificationTests(unittest.TestCase):
    def test_antiunitary_average_is_only_real_linear(self):
        compensator = lambda z: (z+z.conjugate())/2
        z = 2+3j
        self.assertEqual(compensator(2*z), 2*compensator(z))
        self.assertNotEqual(compensator(1j*z), 1j*compensator(z))
        self.assertEqual(compensator(3j), 0)

    def test_odd_input_is_annihilated(self):
        j = matrix(((1, 0, 0), (0, -1, 0), (0, 0, -1)))
        c = combine(eye(3), j, Q(1, 2), Q(1, 2))
        for a, b in product(range(-3, 4), repeat=2):
            state = (0, a, b)
            self.assertEqual(mv(j, state), tuple(-x for x in state))
            self.assertEqual(mv(c, state), (0, 0, 0))

    def test_projection_output_is_not_orthogonal_to_nonzero_input(self):
        state, projected = (Q(2), Q(3)), (Q(2), Q(0))
        self.assertEqual(dot(projected, state), dot(projected, projected))
        self.assertNotEqual(dot(projected, state), 0)

    def test_kernel_invariant_coisometry_descends_orthogonally(self):
        n = (Q(2, 3), Q(2, 3), Q(1, 3))
        outer = tuple(tuple(x*y for y in n) for x in n)
        j3 = combine(eye(3), outer, 1, -2)
        j = tuple(row+(Q(0),) for row in j3) + ((Q(0), Q(0), Q(0), Q(-1)),)
        b = matrix(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)))
        jm = mm(mm(b, j), transpose(b))
        self.assertEqual(mm(b, transpose(b)), eye(3))
        self.assertEqual(mm(j, j), eye(4))
        self.assertEqual(jm, transpose(jm))
        self.assertEqual(mm(jm, jm), eye(3))
        self.assertEqual(mm(b, j), mm(jm, b))
        c = combine(eye(4), j, Q(1, 2), Q(1, 2))
        cm = combine(eye(3), jm, Q(1, 2), Q(1, 2))
        self.assertEqual(mm(b, c), mm(cm, b))

    def test_noninvariant_kernel_breaks_the_descent(self):
        j = matrix(((0, 0, 0, 1), (0, 1, 0, 0),
                    (0, 0, 1, 0), (1, 0, 0, 0)))
        b = matrix(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)))
        k = (0, 0, 0, 1)
        compressed = mm(mm(b, j), transpose(b))
        self.assertEqual(mv(b, k), (0, 0, 0))
        self.assertNotEqual(mv(mm(b, j), k), (0, 0, 0))
        self.assertNotEqual(mm(compressed, compressed), eye(3))
        self.assertNotEqual(mm(b, j), mm(compressed, b))

    def test_arbitrary_similarity_does_not_preserve_root_metric(self):
        j = matrix(((0, 1, 0), (1, 0, 0), (0, 0, 1)))
        b = matrix(((2, 0, 0), (0, 1, 0), (0, 0, 1)))
        inverse = matrix(((Q(1, 2), 0, 0), (0, 1, 0), (0, 0, 1)))
        jm = mm(mm(b, j), inverse)
        self.assertEqual(mm(jm, jm), eye(3))
        self.assertEqual(mm(b, j), mm(jm, b))
        self.assertNotEqual(mm(transpose(jm), jm), eye(3))

    def test_fixed_seed_descends_to_equal_roots(self):
        j = matrix(((1, 0, 0, 0), (0, 1, 0, 0),
                    (0, 0, 1, 0), (0, 0, 0, -1)))
        b = matrix(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)))
        seed = (Q(1), Q(1), Q(1), Q(0))
        c = combine(eye(4), j, Q(1, 2), Q(1, 2))
        self.assertEqual(mv(j, seed), seed)
        self.assertEqual(koide(mv(mm(b, c), seed)), Q(1, 3))

    def test_fitted_projection_reproduces_any_nonnegative_roots(self):
        for values in ((1, 2, 3), (1, 1, 1), (1, 0, 4), (0, 0, 5)):
            x = tuple(map(Q, values))
            c = tuple(tuple(a*b/dot(x, x) for b in x) for a in x)
            j = combine(c, eye(3), 2, -1)
            self.assertEqual(mm(j, j), eye(3))
            self.assertEqual(mm(transpose(j), j), eye(3))
            alpha_for_ones = dot(x, x)/sum(x)
            self.assertEqual(tuple(alpha_for_ones*y for y in mv(c, (1, 1, 1))), x)
            h = sum(map(sum, j))/3
            self.assertEqual(koide(x), 2/(3*(1+h)))

    def test_equivariant_nonlinear_readout_keeps_fixed_input_constant(self):
        readout = lambda state: tuple(Q(x*x) for x in state)
        for state in product(range(-2, 3), repeat=3):
            self.assertEqual(readout(cycle(state)), cycle(readout(state)))
        for a in (1, 2, 7):
            output = readout((a, a, a))
            self.assertEqual(koide(output), Q(1, 3))

    def test_common_frame_scale_does_not_create_a_hierarchy(self):
        for beta in (Q(1, 4), Q(5493, 10000), Q(3, 4)):
            roots = tuple(beta*x for x in (Q(2),)*3)
            self.assertEqual(koide(roots), Q(1, 3))
            asymmetric = (Q(1), Q(2), Q(5))
            self.assertEqual(koide(tuple(beta*x for x in asymmetric)), koide(asymmetric))

    def test_closed_triole_bound_on_complex_amplitudes(self):
        for a, b, c, d in product(range(-2, 3), repeat=4):
            z = (complex(a, b), complex(c, d), -complex(a+c, b+d))
            if any(z):
                value = koide(tuple(map(abs, z)))
                self.assertGreaterEqual(value, 1/3-1e-14)
                self.assertLessEqual(value, 1/2+1e-14)

    def test_closed_triole_endpoints_and_mass_scale(self):
        self.assertEqual(koide((Q(1), Q(0), Q(1))), Q(1, 2))
        z = (1, complex(-0.5, math.sqrt(3)/2), complex(-0.5, -math.sqrt(3)/2))
        self.assertAlmostEqual(koide(tuple(map(abs, z))), 1/3, places=13)
        roots = (Q(1), Q(2), Q(3))
        self.assertEqual(koide(roots), koide(tuple(7*x for x in roots)))

    def test_triangle_bound_does_not_apply_to_independent_mass_couplings(self):
        z = (Q(1), Q(1), Q(-2))
        self.assertEqual(sum(z), 0)
        factors = (Q(1), Q(2), Q(4))
        roots = tuple(f*abs(a) for f, a in zip(factors, z))
        self.assertGreater(koide(roots), Q(1, 2))

    def test_residual_readout_is_positive_and_zero_on_fixed_input(self):
        d = matrix(((1, 1, 0), (0, 2, 0), (0, 0, 3)))
        fixed, odd = (1, 2, 3, 0, 0, 0), (0, 0, 0, 1, 2, 3)
        self.assertEqual(residual_mass(fixed, d), 0)
        self.assertGreater(residual_mass(odd, d), 0)

    def test_residual_readout_has_J_dual_invariance(self):
        d = matrix(((1, 1, 0), (0, 2, 0), (0, 0, 3)))
        for state in ((1, 2, 3, 4, 5, 6), (0, 0, 0, 1, 0, 2)):
            self.assertEqual(residual_mass(state, d), residual_mass(j_state(state), d))

    def test_isotropic_frame_residuals_have_equal_masses(self):
        beta = Q(5493, 10000)
        d = combine(eye(3), eye(3), beta, 0)
        states = tuple((0, 0, 0)+row for row in eye(3))
        masses = tuple(residual_mass(state, d) for state in states)
        self.assertEqual(masses, (3*beta*beta,)*3)

    def test_zero_frame_in_isotropic_ansatz_makes_ratio_undefined(self):
        d = matrix(((0, 0, 0),)*3)
        states = tuple((0, 0, 0)+row for row in eye(3))
        self.assertEqual(tuple(residual_mass(state, d) for state in states), (0, 0, 0))
        with self.assertRaises(ZeroDivisionError):
            koide((Q(0),)*3)

    def test_unfixed_residual_coupling_can_fit_arbitrary_masses(self):
        states = tuple((0, 0, 0)+row for row in eye(3))
        for roots in ((1, 2, 5), (3, 3, 3), (1, 0, 7)):
            d = matrix([[roots[i] if i == j else 0 for j in range(3)] for i in range(3)])
            masses = tuple(residual_mass(state, d, scale=Q(1)) for state in states)
            self.assertEqual(masses, tuple(x*x for x in roots))
