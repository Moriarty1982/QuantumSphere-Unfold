from pathlib import Path
import sympy as s,json
I=s.I;th=s.symbols('theta',real=True)
c=s.cos(th);d=s.sin(th)
Y=s.Matrix([[0,-I,0],[I,0,0],[0,0,0]])
S=s.Matrix([[0,s.Rational(1,2),0],[s.Rational(1,2),0,0],[0,0,0]])
G=s.Matrix([[0,0,c],[0,0,-d],[c,-d,0]])
R=s.simplify(s.eye(3)-2*G*G)
comm=lambda a,b:a*b-b*a
clean=lambda a:a.applyfunc(s.trigsimp)
Rp=R.diff(th)
assert clean(comm(G,R))==s.zeros(3)
# D R = dR+i[A,R]. Solve with A=h Y.
assert clean(Rp-I*comm(Y,R))==s.zeros(3)
# Canonical horizontal connection for any Hermitian involution.
B=clean(I*Rp*R/2)
assert clean(Rp+I*comm(B,R))==s.zeros(3)
assert clean(B+Y)==s.zeros(3)
# It rotates S: not a fixed-readout preserving completion.
assert comm(Y,S)!=s.zeros(3)
assert s.trigsimp(s.trace(S*R)-s.sin(2*th))==0
assert s.trigsimp(s.diff(s.trace(S*R),th)-2*s.cos(2*th))==0
Z=s.diag(1,-1,0)
assert I*comm(S,-Y)/2==Z/2
# Simultaneous constraints: solve arbitrary Hermitian B with dR+i[B,R]=0 and [B,S]=0
# at theta=pi/12, a regular comparison point.
u=s.symbols('u0:9',real=True)
X=s.Matrix([[u[0],u[3]+I*u[4],u[5]+I*u[6]],[u[3]-I*u[4],u[1],u[7]+I*u[8]],[u[5]-I*u[6],u[7]-I*u[8],u[2]]])
pt={th:s.pi/12}
constraints=list((Rp+I*comm(X,R)).subs(pt))+list(comm(X,S))
eq=[s.simplify(part) for z in constraints for part in (s.re(z),s.im(z))]
sol=s.linsolve(eq,u)
assert sol==s.EmptySet
out={'R':str(R),'R_theta':str(Rp),'transport_completion':'A_add=-Y dtheta; dR+i[A_add,R]=0',
'original_connection':'A=s G, [G,R]=0, so D R=dR nonzero for varying theta',
'canonical_completion':str(B),'fixed_S_simultaneous_solution_at_theta_pi_12':str(sol),
'scope':'Internal covariant transport only; not full Dirac symmetry or action-derived connection'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out))
