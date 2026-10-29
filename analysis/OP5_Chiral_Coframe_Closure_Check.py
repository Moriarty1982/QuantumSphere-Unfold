"""Exact matrix identities; comparison model, not a PDE solution."""
from pathlib import Path
import json
import sympy as s
I=s.I
eye=s.eye
g5=s.zeros(2).row_join(eye(2)).col_join(eye(2).row_join(s.zeros(2)))
beta=s.diag(1,1,-1,-1)
pa=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
alpha=[s.zeros(2).row_join(p).col_join(p.row_join(s.zeros(2))) for p in pa]
T=s.diag(1,1,-1)
S=s.Matrix([[0,s.Rational(1,2),0],[s.Rational(1,2),0,0],[0,0,0]])
Y=s.Matrix([[0,-I,0],[I,0,0],[0,0,0]])
p,q=s.symbols('p q', real=True)
G=s.Matrix([[0,0,p],[0,0,q],[p,q,0]])
kron=s.kronecker_product
H=kron(T,g5); A=kron(G,eye(4)); M=kron(Y,beta)
comm=lambda a,b:a*b-b*a
assert H*H==eye(12)
for K in [eye(4)]+alpha:
    B=kron(S,K)
    assert comm(B,H)==s.zeros(12)
    assert B*H==(B*H).conjugate().T
assert H*A+A*H==s.zeros(12)
assert H*M+M*H==s.zeros(12)
# Exact nonzero angle pi/2, plus symbolic conjugation via anticommutation.
U=(eye(12)+I*H)/s.sqrt(2)
assert s.simplify(U.conjugate().T*A*U-I*A*H)==s.zeros(12)
assert s.simplify(U.conjugate().T*M*U-I*M*H)==s.zeros(12)
# Coframe change at fixed connection is expectation of the Hermitian matrix
# i/2 [B, Udag A U-A]; this is not identically zero.
delta=I*A*H-A
gate=I*comm(kron(S,eye(4)),delta)/2
assert gate==gate.conjugate().T
assert gate!=s.zeros(12)
# Explicit spinor counterexample, p=1 q=0, chi=pi/2.
gate0=gate.subs({p:1,q:0})
w=eye(12)[:,4]+I*eye(12)[:,8]
value=s.simplify((w.conjugate().T*gate0*w)[0])
assert value!=0
c,d,k=s.symbols('c d k', real=True)
F=(c*eye(4)).row_join(s.zeros(4)).col_join((d*eye(4)).row_join(s.zeros(4))).col_join(s.zeros(4).row_join(eye(4)))
for K in [eye(4)]+alpha:
    B=kron(S,K)
    # Separate cos(chi)-1 and sin(chi) coefficients: all angles.
    for change in [A,I*A*H]:
        reduced=F.conjugate().T*(I*comm(B,change)/2).subs({p:k*c,q:-k*d})*F
        assert s.simplify(reduced)==s.zeros(8)
result={
 'status':'PASS: exact SymPy identities',
 'convention':'D=partial+i A; U=exp(i chi T tensor gamma5/2)',
 'derivative_chi_contribution_to_real_cross_coframe':'identically zero',
 'fixed_connection_coframe_invariance':'false in general',
 'proportional_AB_seed':'exact invariance for all angles if psi=(c u,d u,w), p=k c, q=-k d, real c,d,k',
 'counterexample':{'p':1,'q':0,'chi':'pi/2','psi':'e4+i e8 (zero-based)','coframe_delta':str(value)},
 'conjugation':'Udag A U = A cos(chi) + i A H sin(chi)',
 'mass_conjugation':'Udag M U = M cos(chi) + i M H sin(chi)',
 'scope':'matrix algebra only; no native coupling derivation or field evolution'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
