"""Exact non-blind exploration: ground-state selection by two rank-one terms.

No data fit. Run with --result PATH from the repository root.
Checks an entire positive coupling-ratio family, the balanced orbit and
the S-symmetrized control. Physical preparation and mass readout are not inputs.
"""
import argparse
import json
from pathlib import Path
import sympy as sp


def clean(matrix):
    return matrix.applyfunc(sp.simplify)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--result', type=Path, required=True)
    args = parser.parse_args()
    r, x = sp.symbols('r x', positive=True)
    rt3 = sp.sqrt(3)
    omega = (-1+sp.I*rt3)/2
    e = sp.Matrix([1, 0, 0])
    s = sp.ones(3, 1)/rt3
    u = sp.Matrix([0, 1, 1])/sp.sqrt(2)
    B = sp.Matrix.hstack(e, u)
    Q, R = e*e.T, s*s.T
    tau = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    D, S = sp.diag(1, omega, omega**2), sp.diag(1, omega, omega)
    assert clean((sp.eye(3)+D+D**2)/3-Q) == sp.zeros(3)
    assert (sp.eye(3)+tau+tau**2)/3 == R
    M = r*Q+R
    discriminant = (r-sp.Rational(1, 3))**2+sp.Rational(8, 9)
    delta = sp.sqrt(discriminant)
    z = (r-sp.Rational(1, 3))/delta
    nx = 2*sp.sqrt(2)/(3*delta)
    rho2 = sp.Matrix([[1+z, nx], [nx, 1-z]])/2
    rho = B*rho2*B.T
    assert clean(rho*rho-rho) == sp.zeros(3)
    assert sp.simplify(sp.trace(rho)-1) == 0
    lam_plus = (r+1+delta)/2
    assert clean(M*rho-lam_plus*rho) == sp.zeros(3)
    char = x*(x*x-(r+1)*x+2*r/3)
    assert sp.simplify((x*sp.eye(3)-M).det()-char) == 0
    # The analytic positive-ratio argument identifies lam_plus as the top
    # eigenvalue of M, i.e. the ground direction of H=-M.
    fidelity = sp.simplify(sp.trace(rho*S*rho*S.conjugate().T))
    assert sp.simplify(fidelity-(1+3*z*z)/4) == 0
    K = sp.simplify((1+2*fidelity)/3)
    assert sp.simplify(K-(1+z*z)/2) == 0
    target_difference = (3*r+1)*(r-1)/(9*discriminant)
    assert sp.simplify(K-sp.Rational(2, 3)-target_difference) == 0
    sensitivity = sp.simplify(sp.diff(K, r).subs(r, 1))
    assert sensitivity == sp.Rational(1, 3)

    v = sp.Matrix([1+rt3, 1, 1])
    rho_balanced = clean(v*v.T/(v.T*v)[0])
    assert clean(rho.subs(r, 1)-rho_balanced) == sp.zeros(3)
    orbit = [clean(S**j*rho_balanced*(S.conjugate().T)**j) for j in range(3)]
    bargmann = sp.simplify(sp.trace(orbit[0]*orbit[1]*orbit[2]))
    assert sp.simplify(bargmann-(1+sp.I)/4) == 0
    frame = sum(orbit, sp.zeros(3))
    assert sp.simplify((x*sp.eye(3)-frame).det()-x*(x*x-3*x+sp.Rational(3, 2))) == 0
    assert frame.rank() == 2

    H = -M
    averaged = clean(sum((S**j*H*(S.conjugate().T)**j for j in range(3)), sp.zeros(3))/3)
    assert clean(averaged+(r+sp.Rational(1, 3))*Q+sp.Rational(2, 3)*u*u.T) == sp.zeros(3)
    assert clean(averaged.subs(r, 1)*e+sp.Rational(4, 3)*e) == sp.zeros(3, 1)
    energies = [sp.simplify(sp.trace(H.subs(r, 1)*rho_j)) for rho_j in orbit]
    assert sp.simplify(energies[0]+1+1/rt3) == 0
    assert energies[1:] == [-1, -1]
    F = sp.Matrix([[omega**(j*k)/rt3 for k in range(3)] for j in range(3)])
    assert clean(F*Q*F.conjugate().T-R) == sp.zeros(3)
    assert clean(F*R*F.conjugate().T-Q) == sp.zeros(3)

    result = {
        'assertion_tested': 'Symbolic positive coupling-ratio ground projector; S-orbit diagnostic; balanced Bargmann invariant; S-averaged Hamiltonian and orbit rank',
        'domain': 'Exact rational/algebraic expressions over real r=a/b>0; b is the positive energy unit',
        'characteristic_polynomial_of_minus_H': str(char),
        'delta_squared': str(sp.expand(discriminant)),
        'ground_bloch_z': str(z),
        'orbit_fidelity': str(fidelity), 'orbit_K': str(K),
        'K_minus_two_thirds_factored': str(target_difference),
        'dK_dr_at_balance': str(sensitivity),
        'balanced_seed_unnormalized': ['1+sqrt(3)', '1', '1'],
        'balanced_bargmann': str(bargmann),
        'balanced_frame_characteristic_polynomial': 'x*(x**2-3*x+3/2)',
        'balanced_orbit_gram_rank': 2,
        'balanced_orbit_energies': list(map(str, energies)),
        'S_averaged_H': '-(r+1/3)*Q-(2/3)*Pu',
        'Fourier_exchanges_projectors': True,
        'non_claims': ['No native Hamiltonian derived', 'No coefficient equality derived',
                       'No state preparation derived', 'No three-positive-mass spectrum',
                       'K is the orbit diagnostic, not a verified physical mass readout'],
    }
    args.result.parent.mkdir(parents=True, exist_ok=True)
    args.result.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('Exact ratio-family checks passed: K=2/3 iff a=b for positive weights.')
    print('Balanced Bargmann=(1+i)/4; orbit Gram rank=2; S-average loses nontrivial orbit.')


if __name__ == '__main__':
    main()
