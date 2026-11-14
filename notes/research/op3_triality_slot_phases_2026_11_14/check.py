"""Exact, non-blind exploration of colour-centralizing triality phase triples.

Run from the repository root with --result PATH. No data fits or external input.
Cayley-Dickson convention follows k69_test_h17.py; no research module executes
on import. The 512 tensor equations include zero as well as nonzero entries.
"""
import argparse
import json
from pathlib import Path
import sympy as sp


def qmul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return sp.Matrix([a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
                      a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e])


def qc(x):
    return sp.diag(1, -1, -1, -1)*x


def omul(x, y):
    a, b, c, d = x[:4, :], x[4:, :], y[:4, :], y[4:, :]
    return (qmul(a, c)-qmul(qc(d), b)).col_join(qmul(d, a)+qmul(b, qc(c)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--result', type=Path, required=True)
    args = parser.parse_args()
    eye = sp.eye(8)
    basis = [eye[:, k] for k in range(8)]
    L = sp.Matrix.hstack(*(omul(basis[7], x) for x in basis))
    R = sp.Matrix.hstack(*(omul(x, basis[7]) for x in basis))
    J0, Jc = (L+R)/2, (L-R)/2
    assert L*R == R*L and L*L == -eye and R*R == -eye
    assert J0.T == -J0 and Jc.T == -Jc
    assert J0*Jc == sp.zeros(8)
    assert -J0*J0 == sp.diag(1, 0, 0, 0, 0, 0, 0, 1)
    assert -Jc*Jc == eye+J0*J0
    Q = eye/2-sp.I*L/6-sp.I*R/3
    assert J0*Q == Q*J0 and Jc*Q == Q*Jc
    assert Q*(basis[0]+sp.I*basis[7]) == sp.zeros(8, 1)
    assert Q*(basis[0]-sp.I*basis[7]) == basis[0]-sp.I*basis[7]

    # Build the trilinear tensor from exact signed basis multiplication.
    products = {(i, j): omul(basis[i], basis[j]) for i in range(8) for j in range(8)}
    tensor = {(i, j, k): omul(products[i, j], basis[k])[0]
              for i in range(8) for j in range(8) for k in range(8)}
    variables = sp.symbols('a0 b0 a1 b1 a2 b2', real=True)
    generators = [variables[2*s]*J0+variables[2*s+1]*Jc for s in range(3)]
    equations = []
    for i in range(8):
        for j in range(8):
            for k in range(8):
                equations.append(sum(generators[0][m, i]*tensor[m, j, k]
                                     + generators[1][m, j]*tensor[i, m, k]
                                     + generators[2][m, k]*tensor[i, j, m]
                                     for m in range(8)))
    matrix, rhs = sp.linear_eq_to_matrix(equations, variables)
    assert rhs == sp.zeros(512, 1)
    reduced, pivots = matrix.rref()
    rank = len(pivots)
    assert rank == 4
    beta0, beta1 = sp.symbols('beta0 beta1', real=True)
    beta = [beta0, beta1, -beta0-beta1]
    alpha = [beta[2]-beta[1], beta[0]-beta[2], beta[1]-beta[0]]
    candidate = sp.Matrix([v for pair in zip(alpha, beta) for v in pair])
    assert matrix*candidate == sp.zeros(512, 1)
    assert candidate.jacobian([beta0, beta1]).rank() == 2
    # Thus this two-dimensional family is the full nullspace of this ansatz.

    def weights(a):
        assert sum(a) == 0
        return [(a[(i+1) % 3]-a[(i-1) % 3])/3 for i in range(3)]

    def order(turns):
        return int(sp.ilcm(*(sp.denom(x) for x in turns)))

    # All phase angles below are in turns, i.e. angle/(2*pi).
    d_alpha = [sp.Rational(0), sp.Rational(1, 3), -sp.Rational(1, 3)]
    d_beta = weights(d_alpha)
    s_alpha = [-sp.Rational(2, 9), sp.Rational(1, 9), sp.Rational(1, 9)]
    s_beta = weights(s_alpha)
    assert d_beta == [sp.Rational(2, 9), -sp.Rational(1, 9), -sp.Rational(1, 9)]
    assert s_beta == [0, sp.Rational(1, 9), -sp.Rational(1, 9)]
    assert order(d_alpha+d_beta) == order(s_alpha+s_beta) == 9
    assert [sp.Mod(3*x, 1) for x in d_beta] == [sp.Rational(2, 3)]*3
    assert [sp.Mod(3*x, 1) for x in s_alpha] == [sp.Rational(1, 3)]*3
    # Exact S fails already on neutral inputs (1,1,1): Re(omega^2)=-1/2.
    assert sp.cos(4*sp.pi/3) == -sp.Rational(1, 2)

    result = {
        'assertion_tested': 'Exact kernel of all 512 triality tensor equations in six phase generators; charge commutators; rational phase orders',
        'domain': 'Q for tensor and ranks, Q(i) for charge, Q/Z for finite phases',
        'tensor_equations': len(equations), 'unknowns': len(variables),
        'rank': rank, 'kernel_dimension': 6-rank,
        'nonzero_rref_rows': [[str(x) for x in reduced.row(i)] for i in range(rank)],
        'parameterization': {'alpha': [str(x) for x in alpha], 'beta': [str(x) for x in beta]},
        'D': {'neutral_turns': list(map(str, d_alpha)), 'colour_turns': list(map(str, d_beta)),
              'full_order': order(d_alpha+d_beta), 'cube_colour_turns_mod_1': [str(sp.Mod(3*x, 1)) for x in d_beta]},
        'projective_S': {'neutral_turns': list(map(str, s_alpha)), 'colour_turns': list(map(str, s_beta)),
                         'full_order': order(s_alpha+s_beta)},
        'exact_S_neutral_counterexample': '-1/2 versus 1',
        'charge_commutators': 'zero, exact',
        'non_claims': ['No mass prediction or parameter selection', 'No Fourier lift',
                       'No full Lorentz, chirality, or Standard Model bridge',
                       'Six-parameter ansatz only; finite completeness is argued separately in the note'],
    }
    args.result.parent.mkdir(parents=True, exist_ok=True)
    args.result.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(f'Exact tensor: {len(equations)} equations, rank {rank}, kernel dimension {6-rank}.')
    print('D lifts with order 9; S only projectively; Q commutators vanish exactly.')


if __name__ == '__main__':
    main()
