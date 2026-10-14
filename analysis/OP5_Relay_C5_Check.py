"""Reproducible C5 reachability diagnostics, not a native OP5 certificate.

Run without arguments for analytic-model tests. --data accepts JSON with
real, norm-whitened `residual`, `response` and optional `guard_response`.
The response columns are evaluated control derivatives, not sector labels.
No physical control bounds or nonlinear guard invariance are assumed.
Requires NumPy and mpmath.
"""

import argparse
import json
from pathlib import Path
import unittest

import mpmath as mp
import numpy as np


def real_array(value):
    if np.iscomplexobj(value):
        raise ValueError("Represent complex controls by real quadrature columns.")
    result = np.asarray(value, dtype=float)
    if not np.all(np.isfinite(result)):
        raise ValueError("Inputs must be finite.")
    return result


def rank_from_singular_values(values, shape):
    if len(values) == 0 or values[0] == 0:
        return 0
    cutoff = max(shape) * np.finfo(float).eps * values[0]
    return int(np.count_nonzero(values > cutoff))


def reachability(residual, response, guard_response=None):
    """Compute the unbounded-control minimum of the linearized squared score."""
    r = real_array(residual)
    j = real_array(response)
    if r.ndim != 1 or j.ndim != 2 or j.shape[0] != r.size:
        raise ValueError("Expected residual (n,) and response (n,k).")
    score = float(r @ r)
    if score <= 0 or not np.isfinite(score):
        raise ValueError("The score ratio requires a finite, nonzero residual.")
    controls = j.shape[1]
    basis = np.eye(controls)
    if guard_response is not None:
        guard = real_array(guard_response)
        if guard.ndim != 2 or guard.shape[1] != controls:
            raise ValueError("Expected guard_response (m,k).")
        if guard.size:
            _, values, vh = np.linalg.svd(guard, full_matrices=True)
            rank = rank_from_singular_values(values, guard.shape)
            basis = vh[rank:].T
    allowed = j @ basis
    if allowed.shape[1]:
        u, values, _ = np.linalg.svd(allowed, full_matrices=False)
        rank = rank_from_singular_values(values, allowed.shape)
        projection = u[:, :rank] @ u[:, :rank].T
    else:
        rank = 0
        projection = np.zeros((r.size, r.size))
    remainder = r - projection @ r
    minimum = float(remainder @ remainder)
    ratio = minimum / score
    return {
        "status": "linearized_numeric_diagnostic_only",
        "allowed_rank": rank,
        "residual_dimension": r.size,
        "initial_score": score,
        "minimum_linearized_score": minimum,
        "minimum_score_ratio": ratio,
        "reachable_score_fraction": 1.0 - ratio,
        "three_quarter_margin": 0.75 - ratio,
        "controls_assumed_unbounded": True,
        "nonlinear_guards_verified": False,
        "native_readout_identified": False,
    }


def lens_residual(a, c, angle):
    x = mp.cos(angle) - mp.mpf("1.5") * mp.sin(angle)
    y = mp.sin(angle) + mp.mpf("1.5") * mp.cos(angle)
    points = [(mp.mpf(2), mp.mpf(0)), (mp.mpf(0), mp.sqrt(3)), (x, y)]
    return mp.matrix([
        mp.sqrt((px + c) ** 2 + py ** 2)
        + mp.sqrt((px - c) ** 2 + py ** 2) - 2 * a
        for px, py in points
    ])


def lens_diagnostic(steps=12):
    """Construct a local inverse on declared samples, not original scan data."""
    with mp.workdps(80):
        normal = mp.matrix([-1, -4, 5]) / mp.sqrt(42)
        target = mp.mpf("0.001") * normal

        def solve(wanted, seed):
            def equations(a, c, angle):
                return tuple(lens_residual(a, c, angle) - wanted)
            return mp.findroot(equations, tuple(seed), tol=mp.mpf("1e-65"),
                               maxsteps=40)

        point = solve(target, (2, 1, 0))
        initial = lens_residual(*point)
        jac = mp.matrix([
            [-2, 0], [-2, 1], [-2, mp.mpf(4) / 5]
        ])
        augmented = mp.matrix([
            [-2, 0, 0], [-2, 1, 0], [-2, mp.mpf(4) / 5, mp.mpf(2) / 5]
        ])
        assert mp.norm(jac.T * normal) < mp.mpf("1e-70")
        assert abs(mp.det(augmented) + mp.mpf(4) / 5) < mp.mpf("1e-70")
        score = mp.fsum(v * v for v in initial)
        initial_score = score
        amplitude_factor = mp.sqrt(3) / 2
        max_ratio_error = mp.mpf(0)
        max_radius_error = mp.mpf(0)
        for _ in range(steps):
            target *= amplitude_factor
            point = solve(target, point)
            residual = lens_residual(*point)
            new_score = mp.fsum(v * v for v in residual)
            max_ratio_error = max(max_ratio_error, abs(new_score / score - mp.mpf(3) / 4))
            score = new_score
            a, c, angle = point
            assert mp.mpf("1.9") < a < mp.mpf("2.1")
            assert mp.mpf("0.9") < c < mp.mpf("1.1")
            assert abs(angle) < mp.mpf("0.1")
            x = mp.cos(angle) - mp.mpf("1.5") * mp.sin(angle)
            y = mp.sin(angle) + mp.mpf("1.5") * mp.cos(angle)
            max_radius_error = max(max_radius_error, abs(x * x + y * y - mp.mpf(13) / 4))
        assert max_ratio_error < mp.mpf("1e-50")
        assert max_radius_error < mp.mpf("1e-70")
        return {
            "status": "constructed_lens_model_not_native_data",
            "two_parameter_rank": 2,
            "augmented_jacobian_determinant": "-4/5",
            "initial_score": mp.nstr(initial_score, 18),
            "steps": steps,
            "score_ratio_per_step": "3/4",
            "final_score": mp.nstr(score, 18),
            "maximum_ratio_error": mp.nstr(max_ratio_error, 8),
            "maximum_squared_radius_error": mp.nstr(max_radius_error, 8),
            "guard_scope": "fixed-origin radial distance only",
            "native_relay_generates_rotation": "not established",
        }


def frame_guard_diagnostic(beta=0.5493):
    """Test an explicitly assumed clock/weight realization and its HC guard."""
    beta = float(beta)
    if not np.isfinite(beta) or not 0 < beta < 1:
        raise ValueError("Expected a finite 0 < beta < 1.")
    weight = beta * beta
    phase = np.pi * beta
    duality = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    hc = (np.eye(3) + duality) / 2
    parity = np.array([[1, 1, 0], [1, -1, 0], [0, 0, np.sqrt(2)]]) / np.sqrt(2)
    spectral_basis = np.array([
        [np.sqrt(weight), np.sqrt(1 - weight)],
        [np.sqrt(1 - weight), -np.sqrt(weight)],
    ])
    spectral_phase = np.diag([np.exp(1j * phase), np.exp(-1j * phase)])
    even_transport = spectral_basis @ spectral_phase @ spectral_basis.T
    parity_transport = np.eye(3, dtype=complex)
    parity_transport[np.ix_([0, 2], [0, 2])] = even_transport
    transport = parity.T @ parity_transport @ parity
    visible = np.array([1, 1, 0]) / np.sqrt(2)
    output = transport @ visible
    raw_phase = np.diag([np.exp(1j * phase), np.exp(-1j * phase), 1])
    raw_output = raw_phase @ visible
    ratios = [float(abs(np.vdot(visible, np.linalg.matrix_power(transport, n) @ visible)) ** 2)
              for n in range(1, 5)]
    odd_output = (np.eye(3) - hc) @ output
    raw_odd_output = (np.eye(3) - hc) @ raw_output
    return {
        "status": "assumed_internal_spectral_model_not_native_identification",
        "beta": beta,
        "assumed_visible_spectral_weight": weight,
        "assumed_opposite_spectral_phase": phase,
        "one_step_visible_score_ratio": ratios[0],
        "fixed_transport_visible_ratios_at_steps_1_to_4": ratios,
        "second_step_score_divided_by_first": ratios[1] / ratios[0],
        "full_charge_ratio": float(np.vdot(output, output).real),
        "fixed_duality_commutator_norm": float(np.linalg.norm(transport @ duality - duality @ transport)),
        "hc_odd_leakage": float(np.vdot(odd_output, odd_output).real),
        "raw_opposite_frame_phase_hc_leakage": float(np.vdot(raw_odd_output, raw_odd_output).real),
        "fresh_history_score_ratios": [ratios[0] ** n for n in range(1, 5)],
        "fresh_history_available_in_native_carrier": "not established",
        "native_c4_c6_guards_verified": False,
        "native_c5_readout_identified": False,
    }


def finite_history_diagnostic(horizon=20, beta=0.5493):
    """Autonomous unitary conveyor: no return up to a specified finite horizon."""
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 1:
        raise ValueError("Expected a positive integer history horizon.")
    frame_guard_diagnostic(beta)
    w = beta ** 2
    phase = np.pi * beta
    a = np.cos(phase) + 1j * (2 * w - 1) * np.sin(phase)
    b = 2j * np.sqrt(w * (1 - w)) * np.sin(phase)
    scatter = np.eye(horizon + 1, dtype=complex)
    scatter[:2, :2] = [[a, b], [b, np.conjugate(a)]]
    advance = np.zeros_like(scatter)
    advance[0, 0] = 1
    for slot in range(1, horizon):
        advance[slot, slot + 1] = 1
    advance[horizon, 1] = 1
    transport = advance @ scatter
    # Protected and forbidden test registers are independent of the chosen carrier.
    extended = np.eye(horizon + 3, dtype=complex)
    extended[:horizon + 1, :horizon + 1] = transport
    gate = np.diag([1] * (horizon + 2) + [0])
    state = np.zeros(horizon + 3, dtype=complex)
    state[0] = 1
    state[-2] = 3 + 4j
    q = abs(a) ** 2
    max_relative_error = 0.0
    max_charge_error = 0.0
    max_incoming = 0.0
    for step in range(1, horizon + 1):
        max_incoming = max(max_incoming, abs(state[1]))
        state = extended @ state
        max_relative_error = max(max_relative_error, abs(abs(state[0]) ** 2 / q ** step - 1))
        max_charge_error = max(max_charge_error,
                               abs(np.vdot(state[:horizon + 1], state[:horizon + 1]).real - 1))
        assert state[-2] == 3 + 4j
        assert state[-1] == 0
    horizon_score = float(abs(state[0]) ** 2)
    return_state = extended @ state
    return_score = float(abs(return_state[0]) ** 2)
    error_budget = (np.sqrt(0.75) - np.sqrt(q)) / np.sqrt(1 - q)
    return {
        "status": "finite_unitary_model_not_native_gate_identification",
        "horizon": horizon,
        "fit_plus_history_dimension_per_complex_fit_direction": horizon + 1,
        "carrier_unitarity_error": float(np.linalg.norm(transport.conj().T @ transport - np.eye(horizon + 1))),
        "model_gate_commutator_error": float(np.linalg.norm(extended @ gate - gate @ extended)),
        "maximum_incoming_amplitude_during_horizon": float(max_incoming),
        "maximum_relative_visible_score_error": float(max_relative_error),
        "maximum_fit_plus_history_charge_error": float(max_charge_error),
        "visible_score_at_horizon": horizon_score,
        "visible_score_at_first_recirculation": return_score,
        "protected_test_register_unchanged": True,
        "forbidden_test_register_unexcited": True,
        "incoming_to_visible_amplitude_budget": float(error_budget),
        "oldest_packet_reflection_bound_at_first_return": float(error_budget * q ** (horizon / 2) / np.sqrt(1 - q)),
        "native_readout_and_guards_identified": False,
    }


def outgoing_port_diagnostic():
    """Verify a local conservative amplitude port, including nonempty input."""
    with mp.workdps(80):
        beta = mp.mpf("0.5493")
        weight = beta ** 2
        phase = mp.pi * beta
        a = mp.cos(phase) + 1j * (2 * weight - 1) * mp.sin(phase)
        q = abs(a) ** 2
        rate = -mp.log(q)  # The declared sampling time is one model time unit.
        omega = -mp.arg(a)
        k = rate / 2 + 1j * omega
        rho = mp.mpf("0.2") + mp.mpf("0.7") * 1j
        initial = mp.mpf("0.7") - mp.mpf("0.2") * 1j
        incoming_scale = mp.mpf("0.3") + mp.mpf("0.4") * 1j
        end = mp.mpf("1.3")

        def incoming(t):
            return incoming_scale * mp.exp(-rho * t)

        def visible(t):
            return (mp.exp(-k * t) * initial - mp.sqrt(rate) * incoming_scale
                    * (mp.exp(-rho * t) - mp.exp(-k * t)) / (k - rho))

        def outgoing(t):
            return incoming(t) + mp.sqrt(rate) * visible(t)

        balance = (abs(visible(end)) ** 2
                   + mp.quad(lambda t: abs(outgoing(t)) ** 2, [0, end])
                   - abs(initial) ** 2
                   - mp.quad(lambda t: abs(incoming(t)) ** 2, [0, end]))
        back_rate = rate / 2 - 1j * omega

        def recovered(t):
            return (mp.exp(back_rate * (t - end)) * visible(end)
                    + mp.sqrt(rate) * mp.quad(
                        lambda s: mp.exp(back_rate * (t - s)) * outgoing(s), [t, end]))

        inverse_error = max(abs(recovered(t) - visible(t))
                            for t in [mp.mpf(0), mp.mpf("0.2"), mp.mpf("0.9"), end])
        assert abs(balance) < mp.mpf("1e-70")
        assert inverse_error < mp.mpf("1e-70")
        assert abs(mp.exp(-k) - a) < mp.mpf("1e-70")
        return {
            "status": "causal_norm_conserving_amplitude_port_not_native_physics",
            "sampling_time": "one declared model time unit",
            "lambda_times_tau": mp.nstr(rate, 20),
            "omega_times_tau": mp.nstr(omega, 20),
            "frame_amplitude_matched": True,
            "nonempty_input_balance_error": mp.nstr(abs(balance), 8),
            "finite_window_inverse_error": mp.nstr(inverse_error, 8),
            "native_channel_spectrum_and_rate": "not established",
            "physical_energy_identified_with_norm": False,
        }


def shared_channel_diagnostic():
    """Conditional one-channel damping, not evaluated native vertices."""
    with mp.workdps(35):
        beta = mp.mpf("0.5493")
        w = beta**2
        q = 1 - 4*w*(1-w)*mp.sin(mp.pi*beta)**2
        rate = -mp.log(q)

        def transfer(delta, time):
            a = mp.matrix([[-rate/2, -1j*delta], [-1j*delta, 0]])
            root = mp.sqrt(rate**2/16 - delta**2)
            z = a + rate/4 * mp.eye(2)
            factor = time if root == 0 else mp.sinh(root*time)/root
            return mp.exp(-rate*time/4) * (mp.cosh(root*time)*mp.eye(2) + factor*z)

        gamma = mp.matrix([[rate, 0], [0, 0]])
        delta = mp.mpf("0.1")
        t = transfer(delta, 1)
        gram = mp.matrix(2)
        for i in range(2):
            for j in range(2):
                def integrand(s):
                    u = transfer(delta, s)
                    return (u.H * gamma * u)[i, j]
                gram[i, j] = mp.quad(integrand, [0, 1])
        balance = t.H*t + gram - mp.eye(2)
        hermitian_gram = np.array(gram.tolist(), dtype=complex)
        eigenvalues = np.linalg.eigvalsh(hermitian_gram)
        dark_scores = {}
        for d in ("0", "0.01", "0.1"):
            state = transfer(mp.mpf(d), 20) * mp.matrix([0, 1])
            dark_scores[d] = float(mp.re((state.H*state)[0]))
        return {
            "native_identification_certified": False,
            "assumption": "one flat outgoing channel, equal vertices, positive current metric",
            "bright_one_step_score_ratio": float(q),
            "zero_detuning_dark_score_ratio": dark_scores["0"],
            "minimum_initial_bright_fraction_for_three_quarter_score": float(1/(4*(1-q))),
            "finite_time_flux_balance_error": str(max(abs(x) for x in balance)),
            "detuning_0_1_one_step_minimum_gram_eigenvalue": float(eigenvalues[0]),
            "detuning_0_1_one_step_worst_score_ratio": float(1-eigenvalues[0]),
            "initial_dark_score_at_time_20_by_detuning": dark_scores,
            "detuning_0_1_hc_commutator_norm_if_J_swaps_probes": float(2*mp.sqrt(2)*delta),
        }


def hc_even_supply_diagnostic():
    """Source-shaped even block with an assumed outgoing Markov load."""
    with mp.workdps(35):
        rate = mp.mpf(1)
        coupling = mp.mpf("0.1")

        def transfer(detuning, time, k=coupling, gamma=rate):
            d = gamma/2 + 1j*detuning
            a = mp.matrix([[0, -1j*k], [-1j*k, -d]])
            root = mp.sqrt(d**2/4 - k**2)
            factor = time if root == 0 else mp.sinh(root*time)/root
            return mp.exp(-d*time/2) * (mp.cosh(root*time)*mp.eye(2) + factor*(a+d/2*mp.eye(2)))

        # Order: even probe, odd probe, even intermediate component.
        j = np.diag([1.0, -1.0, 1.0])
        h = np.array([[0, 0, 0.1], [0, 0.7, 0], [0.1, 0, 2.0]])
        damping = np.diag([0.0, 0.0, 1.0])
        final = transfer(mp.mpf(2), 20)
        emitted = mp.quad(lambda s: rate*abs(transfer(mp.mpf(2), s)[1, 0])**2, [0, 20])
        retained = abs(final[0, 0])**2 + abs(final[1, 0])**2
        scores = {}
        slow_rates = {}
        for detuning in ("0", "2"):
            delta = mp.mpf(detuning)
            t = transfer(delta, 20)
            scores[detuning] = float(abs(t[0, 0])**2)
            d = rate/2 + 1j*delta
            s = -d/2 + mp.sqrt(d**2/4-coupling**2)
            slow_rates[detuning] = {
                "exact_eigenmode_score_decay_rate": float(-2*mp.re(s)),
                "weak_coupling_rate": float(rate*coupling**2/(delta**2+rate**2/4)),
            }
        closed_first = transfer(mp.mpf(0), mp.pi/2, k=mp.mpf(1), gamma=mp.mpf(0))
        closed_return = transfer(mp.mpf(0), mp.pi, k=mp.mpf(1), gamma=mp.mpf(0))
        return {
            "native_identification_certified": False,
            "parameters": "model units: outgoing rate 1, even coupling 0.1, detuning 0 or 2",
            "hamiltonian_fixed_J_commutator_norm": float(np.linalg.norm(h@j-j@h)),
            "outgoing_load_fixed_J_commutator_norm": float(np.linalg.norm(damping@j-j@damping)),
            "odd_sector_leakage": float(np.linalg.norm(h[[1], :][:, [0, 2]])),
            "prepared_visible_score_at_time_20": scores,
            "slow_eigenmode_rates": slow_rates,
            "retained_plus_emitted_balance_error": str(abs(retained+emitted-1)),
            "hidden_only_input_visible_score_at_time_20_detuning_2": float(abs(final[0, 1])**2),
            "closed_two_mode_visible_score_at_pi_over_2": float(abs(closed_first[0, 0])**2),
            "closed_two_mode_visible_score_at_pi": float(abs(closed_return[0, 0])**2),
            "actual_C5_extraction_and_C4_C6_guards": "not identified",
        }


def invariant_supply_certificate(gamma=1, coupling=0.1, detuning=2,
                                 eigenmode_score=0.5, tolerance=1):
    """Repeated visible contraction on an invariant preparation cone."""
    values = (gamma, coupling, detuning, eigenmode_score, tolerance)
    if not all(np.isfinite(float(value)) for value in values):
        raise ValueError("All cone parameters must be finite.")
    if gamma <= 0 or coupling <= 0 or not 0 < eigenmode_score < 0.75 or tolerance <= 0:
        raise ValueError("Need positive load/coupling/tolerance and eigenmode score in (0,0.75).")
    with mp.workdps(65):
        g, k, delta, target, epsilon = map(lambda x: mp.mpf(str(x)), values)
        d = g/2 + 1j*delta
        root = mp.sqrt(d**2/4-k**2)
        slow, fast = -d/2+root, -d/2-root
        if root == 0 or mp.re(slow) >= 0:
            raise ValueError("This certificate needs distinct decaying poles.")
        time = mp.log(target)/(2*mp.re(slow))
        z = 1j*slow/k
        u, v = mp.exp(slow*time), mp.exp(fast*time)
        feed = -1j*k*(u-v)/(slow-fast)
        upper = abs(u)+abs(feed)*epsilon
        lower = abs(u)-abs(feed)*epsilon
        invariant = lower > 0 and abs(v) <= lower
        contractive = upper**2 <= mp.mpf("0.75")
        size = 1+abs(z)+epsilon
        perturbation_budget = max(mp.mpf(0), min(
            (mp.sqrt(mp.mpf("0.75"))-upper)/size,
            epsilon*(lower-abs(v))/size**2)) if invariant and contractive else mp.mpf(0)
        readout_budget = max(mp.mpf(0),
                             (mp.sqrt(mp.mpf("0.75"))-upper)
                             /(mp.sqrt(mp.mpf("0.75"))+upper))

        # Exact upper/lower extremizers plus interior phase samples.
        worst = mp.mpf(0)
        least = mp.inf
        phases = [mp.exp(2j*mp.pi*n/24) for n in range(24)]
        phases += [u/abs(u)*mp.conj(feed)/abs(feed),
                   -u/abs(u)*mp.conj(feed)/abs(feed)]
        for phase in phases:
            a, eta = mp.mpf(1), epsilon*phase
            initial_norm = abs(a)**2+abs(z*a+eta)**2
            for step in range(20):
                next_a, next_eta = u*a+feed*eta, v*eta
                ratio = abs(next_a/a)**2
                worst, least = max(worst, ratio), min(least, ratio)
                if invariant and abs(next_eta) > epsilon*abs(next_a)*(1+mp.mpf("1e-55")):
                    raise AssertionError("The analytically certified cone was left.")
                if contractive and ratio > mp.mpf("0.75")*(1+mp.mpf("1e-55")):
                    raise AssertionError("The analytically certified contraction failed.")
                a, eta = next_a, next_eta
            final_norm = abs(a)**2+abs(z*a+eta)**2
            if final_norm > initial_norm*(1+mp.mpf("1e-55")):
                raise AssertionError("Outgoing evolution increased the retained norm.")
        empty_hidden_eta = -z
        a, eta = mp.mpf(1), empty_hidden_eta
        empty_max = mp.mpf(0)
        for step in range(20):
            next_a, next_eta = u*a+feed*eta, v*eta
            empty_max = max(empty_max, abs(next_a/a)**2)
            a, eta = next_a, next_eta
        return {
            "native_identification_certified": False,
            "model_parameters": dict(zip(("gamma", "coupling", "detuning", "eigenmode_score", "tolerance"), map(float, values))),
            "sampling_time": float(time),
            "invariant_graph_b_over_a": {"real": float(mp.re(z)), "imag": float(mp.im(z))},
            "cone_invariant": bool(invariant),
            "three_quarter_visible_contraction_certified_on_cone": bool(invariant and contractive),
            "uniform_step_score_upper_bound": float(upper**2),
            "uniform_step_score_lower_bound": float(max(mp.mpf(0), lower)**2),
            "maximum_tested_step_score_ratio": float(worst),
            "minimum_tested_step_score_ratio": float(least),
            "cone_extremizer_sample_count": len(phases),
            "tested_steps_without_hidden_reset": 20,
            "empty_hidden_preparation_in_cone": bool(abs(z) <= epsilon),
            "empty_hidden_preparation_maximum_step_ratio": float(empty_max),
            "separate_per_entry_transfer_perturbation_budget": float(perturbation_budget),
            "separate_relative_residual_dictionary_error_budget": float(readout_budget),
            "budgets_may_be_combined_without_recalculation": False,
            "native_dictionary_guards_and_spectral_error": "not evaluated",
        }


class ReachabilityTests(unittest.TestCase):
    def test_unreachable_direction(self):
        j = [[-2, 0], [-2, 1], [-2, 0.8]]
        result = reachability([-1, -4, 5], j)
        self.assertAlmostEqual(result["minimum_score_ratio"], 1.0)
        self.assertEqual(result["allowed_rank"], 2)

    def test_quarter_fraction_is_enough_with_unbounded_controls(self):
        result = reachability([0.5, np.sqrt(0.75)], [[1], [0]])
        self.assertAlmostEqual(result["minimum_score_ratio"], 0.75)

    def test_insufficient_fraction(self):
        result = reachability([np.sqrt(0.2), np.sqrt(0.8)], [[1], [0]])
        self.assertGreater(result["minimum_score_ratio"], 0.75)

    def test_guard_can_remove_the_new_direction(self):
        j = [[-2, 0, 0], [-2, 1, 0], [-2, 0.8, 0.4]]
        result = reachability([-1, -4, 5], j, [[0, 0, 1]])
        self.assertEqual(result["allowed_rank"], 2)
        self.assertAlmostEqual(result["minimum_score_ratio"], 1.0)

    def test_full_response(self):
        j = [[-2, 0, 0], [-2, 1, 0], [-2, 0.8, 0.4]]
        result = reachability([-1, -4, 5], j)
        self.assertEqual(result["allowed_rank"], 3)
        self.assertLess(result["minimum_score_ratio"], 1e-25)

    def test_zero_and_nonfinite_rejected(self):
        for r in ([0, 0], [np.nan, 1]):
            with self.assertRaises(ValueError):
                reachability(r, [[1], [0]])

    def test_construction(self):
        result = lens_diagnostic()
        self.assertEqual(result["steps"], 12)

    def test_internal_frame_transport_preserves_hc(self):
        result = frame_guard_diagnostic()
        self.assertAlmostEqual(result["full_charge_ratio"], 1.0)
        self.assertLess(result["fixed_duality_commutator_norm"], 1e-14)
        self.assertLess(result["hc_odd_leakage"], 1e-28)
        self.assertAlmostEqual(result["one_step_visible_score_ratio"], 0.1772980923276492)

    def test_raw_frame_assignment_fails_hc(self):
        result = frame_guard_diagnostic()
        self.assertAlmostEqual(result["raw_opposite_frame_phase_hc_leakage"], 0.9762032204173116)

    def test_fixed_frame_transport_is_not_repeated_contraction(self):
        result = frame_guard_diagnostic()
        self.assertGreater(result["second_step_score_divided_by_first"], 1.0)
        self.assertNotAlmostEqual(result["fixed_transport_visible_ratios_at_steps_1_to_4"][1],
                                  result["fresh_history_score_ratios"][1])

    def test_invalid_frame_input_rejected(self):
        for beta in (0, 1, np.nan):
            with self.assertRaises(ValueError):
                frame_guard_diagnostic(beta)

    def test_twenty_step_unitary_history(self):
        result = finite_history_diagnostic()
        self.assertLess(result["carrier_unitarity_error"], 1e-13)
        self.assertEqual(result["maximum_incoming_amplitude_during_horizon"], 0.0)
        self.assertLess(result["maximum_relative_visible_score_error"], 1e-12)
        self.assertLess(result["maximum_fit_plus_history_charge_error"], 1e-13)
        self.assertLess(result["model_gate_commutator_error"], 1e-14)
        self.assertTrue(result["protected_test_register_unchanged"])

    def test_finite_history_recirculates_after_horizon(self):
        result = finite_history_diagnostic()
        self.assertLess(result["visible_score_at_horizon"], 1e-14)
        self.assertGreater(result["visible_score_at_first_recirculation"], 0.6)

    def test_invalid_history_horizon(self):
        for horizon in (0, -1, 1.5, True):
            with self.assertRaises(ValueError):
                finite_history_diagnostic(horizon)

    def test_outgoing_port_conservation_and_inverse(self):
        result = outgoing_port_diagnostic()
        self.assertTrue(result["frame_amplitude_matched"])
        self.assertLess(float(result["nonempty_input_balance_error"]), 1e-70)
        self.assertLess(float(result["finite_window_inverse_error"]), 1e-70)

    def test_shared_channel_has_exact_dark_state_without_detuning(self):
        result = shared_channel_diagnostic()
        self.assertEqual(result["zero_detuning_dark_score_ratio"], 1.0)
        self.assertGreater(result["minimum_initial_bright_fraction_for_three_quarter_score"], 0.25)

    def test_detuning_flux_balance_and_slow_dark_decay(self):
        result = shared_channel_diagnostic()
        self.assertLess(float(result["finite_time_flux_balance_error"]), 1e-30)
        self.assertGreater(result["detuning_0_1_one_step_minimum_gram_eigenvalue"], 0)
        self.assertGreater(result["detuning_0_1_one_step_worst_score_ratio"], 0.75)
        scores = result["initial_dark_score_at_time_20_by_detuning"]
        self.assertGreater(scores["0.01"], scores["0.1"])
        self.assertLess(scores["0.01"], 1.0)

    def test_probe_detuning_is_not_fixed_hc_even_if_J_swaps_probes(self):
        result = shared_channel_diagnostic()
        self.assertGreater(result["detuning_0_1_hc_commutator_norm_if_J_swaps_probes"], 0.28)

    def test_supply_coupling_and_detuning_can_stay_hc_even(self):
        result = hc_even_supply_diagnostic()
        self.assertEqual(result["hamiltonian_fixed_J_commutator_norm"], 0.0)
        self.assertEqual(result["outgoing_load_fixed_J_commutator_norm"], 0.0)
        self.assertEqual(result["odd_sector_leakage"], 0.0)
        self.assertLess(float(result["retained_plus_emitted_balance_error"]), 1e-30)

    def test_even_detuning_suppresses_decay_but_hidden_supply_breaks_uniform_readout_bound(self):
        result = hc_even_supply_diagnostic()
        scores = result["prepared_visible_score_at_time_20"]
        self.assertGreater(scores["2"], scores["0"])
        self.assertGreater(scores["2"], 0.75)
        self.assertLess(scores["0"], 0.75)
        self.assertGreater(result["hidden_only_input_visible_score_at_time_20_detuning_2"], 0)

    def test_closed_even_supply_returns_visible_amplitude(self):
        result = hc_even_supply_diagnostic()
        self.assertLess(result["closed_two_mode_visible_score_at_pi_over_2"], 1e-30)
        self.assertAlmostEqual(result["closed_two_mode_visible_score_at_pi"], 1.0)

    def test_invariant_cone_proves_repeated_visible_contraction(self):
        result = invariant_supply_certificate()
        self.assertTrue(result["cone_invariant"])
        self.assertTrue(result["three_quarter_visible_contraction_certified_on_cone"])
        self.assertLess(result["maximum_tested_step_score_ratio"], 0.75)
        self.assertAlmostEqual(result["maximum_tested_step_score_ratio"],
                               result["uniform_step_score_upper_bound"])
        self.assertGreater(result["uniform_step_score_lower_bound"], 0)

    def test_empty_hidden_state_needs_no_reset_in_certified_cone(self):
        result = invariant_supply_certificate()
        self.assertTrue(result["empty_hidden_preparation_in_cone"])
        self.assertLess(result["empty_hidden_preparation_maximum_step_ratio"], 0.75)
        self.assertGreater(result["separate_per_entry_transfer_perturbation_budget"], 0)
        self.assertGreater(result["separate_relative_residual_dictionary_error_budget"], 0)

    def test_overlarge_cone_is_not_certified(self):
        result = invariant_supply_certificate(tolerance=100)
        self.assertFalse(result["three_quarter_visible_contraction_certified_on_cone"])

    def test_invalid_cone_parameters_rejected(self):
        for kwargs in ({"gamma": 0}, {"coupling": 0}, {"eigenmode_score": 0.75},
                       {"tolerance": -1}, {"detuning": np.nan},
                       {"gamma": 4, "coupling": 1, "detuning": 0}):
            with self.assertRaises(ValueError):
                invariant_supply_certificate(**kwargs)

    def test_supply_graph_matches_independent_matrix_exponential(self):
        result = invariant_supply_certificate()
        with mp.workdps(45):
            k, d = mp.mpf("0.1"), mp.mpf("0.5")+2j
            slow = -d/2+mp.sqrt(d**2/4-k**2)
            z = 1j*slow/k
            time = mp.log(mp.mpf("0.5"))/(2*mp.re(slow))
            matrix = mp.matrix([[0, -1j*k], [-1j*k, -d]])
            graph = mp.matrix([1, z])
            error = mp.expm(matrix*time)*graph-mp.exp(slow*time)*graph
            self.assertLess(float(max(abs(x) for x in error)), 1e-40)
            self.assertAlmostEqual(float(time), result["sampling_time"])

    def test_transfer_error_budget_preserves_cone_and_step_bound(self):
        result = invariant_supply_certificate()
        with mp.workdps(35):
            k, d = mp.mpf("0.1"), mp.mpf("0.5")+2j
            slow = -d/2+mp.sqrt(d**2/4-k**2)
            z = complex(1j*slow/k)
            matrix = mp.matrix([[0, -1j*k], [-1j*k, -d]])
            t = np.array(mp.expm(matrix*result["sampling_time"]).tolist(), dtype=complex)
        rng = np.random.default_rng(513)
        budget = result["separate_per_entry_transfer_perturbation_budget"] * 0.99
        for index in range(128):
            perturbation = budget*np.exp(2j*np.pi*rng.random((2, 2)))
            eta = np.exp(2j*np.pi*rng.random())
            state = (t+perturbation)@np.array([1, z+eta])
            self.assertLessEqual(abs(state[0])**2, 0.75)
            self.assertLessEqual(abs(state[1]-z*state[0]), abs(state[0]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path)
    parser.add_argument("--cone-data", type=Path)
    args = parser.parse_args()
    if args.data and args.cone_data:
        parser.error("Choose one diagnostic input mode.")
    if args.cone_data:
        data = json.loads(args.cone_data.read_text(encoding="utf-8"))
        print(json.dumps(invariant_supply_certificate(**data), indent=2))
    elif args.data:
        data = json.loads(args.data.read_text(encoding="utf-8"))
        print(json.dumps(reachability(data["residual"], data["response"],
                                      data.get("guard_response")), indent=2))
    else:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(ReachabilityTests)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        if not result.wasSuccessful():
            raise SystemExit(1)
        print(json.dumps({"lens_diagnostic": lens_diagnostic(),
                          "frame_guard_diagnostic": frame_guard_diagnostic(),
                          "finite_history_diagnostic": finite_history_diagnostic(),
                          "outgoing_port_diagnostic": outgoing_port_diagnostic(),
                          "shared_channel_diagnostic": shared_channel_diagnostic(),
                          "hc_even_supply_diagnostic": hc_even_supply_diagnostic(),
                          "invariant_supply_certificate": invariant_supply_certificate()}, indent=2))


if __name__ == "__main__":
    main()
