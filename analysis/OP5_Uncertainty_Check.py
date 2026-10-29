"""Exact finite-dimensional checks; no quantization of the native theory assumed."""
import json, sys
from pathlib import Path
import sympy as s
t,q=s.symbols('theta q', real=True)
c,d=s.cos(t),s.sin(t)
I=s.eye(3)
R=s.Matrix([[-s.cos(2*t),s.sin(2*t),0],[s.sin(2*t),s.cos(2*t),0],[0,0,-1]])
S=s.Matrix([[0,s.Rational(1,2),0],[s.Rational(1,2),0,0],[0,0,0]])
Y=s.Matrix([[0,-s.I,0],[s.I,0,0],[0,0,0]])
Z=s.diag(1,-1,0)
def simp(x): return s.trigsimp(s.expand_trig(s.expand(x)))
def zero(x):
    if isinstance(x,s.MatrixBase): return all(simp(v)==0 for v in x)
    return simp(x)==0
checks={}
def check(name,expression):
    checks[name]=zero(expression)
    assert checks[name], (name,expression)
check('R_involution',R*R-I)
check('R_S_commutator',R*S-S*R+s.I*s.cos(2*t)*Y)
check('S_Y_commutator',S*Y-Y*S-s.I*Z)
check('transport_trace',s.trace(S*R)-s.sin(2*t))
n=s.Matrix([c,-d,0]); v=s.Matrix([c,d,0]); z=s.Matrix([0,0,1])
check('n_exact_R_eigenvector',R*n+n)
def moments(rho,A,B):
    ev=lambda X:simp(s.trace(rho*X))
    va=simp(ev(A*A)-ev(A)**2); vb=simp(ev(B*B)-ev(B)**2)
    comm=ev(A*B-B*A)/(2*s.I)
    cov=simp(ev((A*B+B*A)/2)-ev(A)*ev(B))
    return dict(varA=va,varB=vb,comm_half_i=simp(comm),cov=cov,
                schrodinger_slack=simp(va*vb-comm**2-cov**2))
rn=n*n.T
nr=moments(rn,R,S); ny=moments(rn,S,Y)
check('R_eigenstate_zero_variance',nr['varA'])
check('R_S_zero_bound',nr['comm_half_i'])
check('S_variance',nr['varB']-s.cos(2*t)**2/4)
check('S_Y_nonzero_bound',ny['comm_half_i']-s.cos(2*t)/2)
check('S_Y_saturation',ny['schrodinger_slack'])
# Actual proportional AB sector, arbitrary weight q in [0,1]. Coherences
# with C do not contribute to these block-diagonal observables/products.
rho=q*v*v.T+(1-q)*z*z.T
actual=moments(rho,R,S)
check('actual_family_R_S_zero_Robertson_bound',actual['comm_half_i'])
check('actual_S_variance',actual['varB']-(q-q*q*s.sin(2*t)**2)/4)
# Even full J=R tensor gamma5 has zero expected commutator with S tensor I:
# the AB contraction v^T [R,S] v vanishes, for every Dirac spinor u.
check('full_J_S_AB_contraction', (v.T*(R*S-S*R)*v)[0])
f=s.symbols('f',real=True)
check('central_shift_no_R_effect',(f*I)*R-R*(f*I))
check('central_shift_no_S_effect',(f*I)*S-S*(f*I))
# A concrete curvature-bearing scalar connection A_y=x, A_x=0.
# D=partial+iA: [D_x,D_y] psi=i psi, despite commuting scalar potentials.
x,y=s.symbols('x y', real=True); psi=s.Function('psi')(x,y)
Dx=lambda w:s.diff(w,x)
Dy=lambda w:s.diff(w,y)+s.I*x*w
check('central_differential_curvature',Dx(Dy(psi))-Dy(Dx(psi))-s.I*psi)
out={'assertion_tested':'Exact identities for R,S,Y and proportional AB states; scalar differential countercontrol.',
     'domain':'real theta; 0<=q<=1; ordinary positive Hilbert inner product',
     'checks':checks,'R_S_eigenstate':{k:str(v) for k,v in nr.items()},
     'S_Y_eigenstate':{k:str(v) for k,v in ny.items()},
     'actual_family_R_S':{k:str(v) for k,v in actual.items()},
     'non_claims':['No native physical quantization','No derivation of OP5 curvature source','No regional solution']}
(Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_suffix('.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
