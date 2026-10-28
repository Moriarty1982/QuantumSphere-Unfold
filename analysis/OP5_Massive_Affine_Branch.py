"""Exact rational checks; witnesses support, but do not replace, the analytic proof."""
from fractions import Fraction as Q

def check(gamma, C, W, D):
    h, q, m, N, k = Q(1,6), Q(5,6), Q(1), Q(1), Q(1)
    p, omega = -D, m+gamma*h-D
    n, j = [-1,0,0,1], [N,0,0,0]
    E = [[Q(a==mu)+k*h*j[a]*n[mu] for mu in range(4)] for a in range(4)]
    inv = [[Q(mu==a)-k*h*j[mu]*n[a]/q for a in range(4)] for mu in range(4)]
    for a in range(4):
        for b in range(4):
            assert sum(E[a][r]*inv[r][b] for r in range(4)) == Q(a==b)
    lam = [[q*W*inv[mu][a] for mu in range(4)] for a in range(4)]
    for a in range(4):
        for mu in range(4):
            assert -q*W*inv[mu][a]+lam[a][mu] == 0
    contracted = [sum(lam[a][mu]*n[mu] for mu in range(4)) for a in range(4)]
    assert contracted == [W*x for x in n]
    assert W == C+h*h and D == k*h*W
    # alpha_z u=(0,0,1,0); beta u=u in the standard Dirac representation.
    residual = [omega+D-m-gamma*h, 0, -p-D, 0]
    assert residual == [0,0,0,0]
    assert q*2*h-k*N*W+gamma*N == 0
    assert p == -2*h*h*q-gamma*h
    assert C == 2*h-3*h*h+gamma
    assert omega == Q(103,108)
    assert 2*(1-3*h) > 0  # restricted potential curvature only
    delta = Q(1,100)
    assert q*2*h-k*N*(W+delta)+gamma*N == -delta
    shifted = [omega+k*h*(W+delta)-m-gamma*h, 0, -p-k*h*(W+delta), 0]
    assert shifted == [h*delta,0,-h*delta,0] and any(shifted)
    return {'gamma':str(gamma), 'C':str(C), 'scalar':'0', 'probe':'0', 'coframe':'0', 'fixed_data_control':'nonzero as required'}

if __name__ == '__main__':
    import json
    print(json.dumps([check(Q(0),Q(1,4),Q(5,18),Q(5,108)),
                      check(Q(1,4),Q(1,2),Q(19,36),Q(19,216))], indent=2))
