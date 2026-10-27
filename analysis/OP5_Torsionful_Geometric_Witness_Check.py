import sympy as s
t=s.symbols('t',positive=True)
# Matrices omega_mu^a_b in the coordinate coframe.
W=[s.zeros(4) for _ in range(4)]
for i in range(1,4): W[i][i,0]=W[i][0,i]=1/t
eta=s.diag(-1,1,1,1); j=s.Matrix([2*t,0,0,0])
for mu in range(4):
 assert eta*W[mu]+W[mu].T*eta==s.zeros(4)
 derivative=s.diff(j,t) if mu==0 else s.zeros(4,1)
 assert derivative+W[mu]*j==2*s.eye(4)[:,mu]
for mu in range(4):
 for nu in range(4):
  R=(s.diff(W[nu],t) if mu==0 else s.zeros(4))-(s.diff(W[mu],t) if nu==0 else s.zeros(4))+W[mu]*W[nu]-W[nu]*W[mu]
  T=W[mu][:,nu]-W[nu][:,mu]
  assert s.simplify(R*j/2-T)==s.zeros(4,1)
  assert (j.T*eta*T)[0]==0
assert W[1][1,0]!=0
print('PASS: Lorentz compatibility, all covariant-vector components, all torsion-curvature integrability components, and j contraction.')
