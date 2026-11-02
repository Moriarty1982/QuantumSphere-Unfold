import sympy as s
import json
from pathlib import Path
t,x,y,z=s.symbols('t x y z',real=True)
N=s.Integer(16); I=s.I
rho=s.sqrt(x*x+y*y); r=s.sqrt(x*x+y*y+z*z)
v=s.Matrix([x,y,z])/t; gam=1/s.sqrt(1-v.dot(v))
pa=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
z2=s.zeros(2); al=[z2.row_join(p).col_join(p.row_join(z2)) for p in pa]
beta=s.diag(1,1,-1,-1)
chip=s.Matrix([1,I*(x+I*y)/rho])/s.sqrt(2)
chim=s.Matrix([1,-I*(x+I*y)/rho])/s.sqrt(2)
sigv=sum((v[k]*pa[k] for k in range(3)),s.zeros(2))
a=s.sqrt((gam+1)/2); n=N/(2*gam)
U=s.sqrt(n)*s.Matrix.vstack(a*chip,a*gam/(gam+1)*sigv*chip)
W=s.sqrt(n)*s.Matrix.vstack(a*chim,-a*gam/(gam+1)*sigv*chim)
th=s.asin(8*t/N)/2; c=s.cos(th); d=s.sin(th); Delta=s.cos(2*th)
fields=[c*U,d*U,W]
Y=s.Matrix([[0,-I,0],[I,0,0],[0,0,0]])
S=s.Matrix([[0,s.Rational(1,2),0],[s.Rational(1,2),0,0],[0,0,0]])
p=3*c/(2*rho*Delta); q=-3*d/(2*rho*Delta)
G=s.Matrix([[0,0,p],[0,0,q],[p,q,0]])
spin=[-y/rho,x/rho,0]; hm=16*gam/(N*Delta)
points=[{t:1,x:s.Rational(3,5),y:0,z:0},{t:1,x:s.Rational(2,5),y:s.Rational(1,5),z:s.Rational(1,5)}]
derivs=[[f.diff(w) for w in (t,x,y,z)] for f in fields]
results=[]
for pt in points:
 ev=lambda m:s.Matrix(m).subs(pt).evalf(30)
 fs=[ev(f) for f in fields]; psi=s.Matrix.vstack(*fs)
 kin=[]
 for ds in derivs:
  kin.append(I*ev(ds[0])+sum((I*al[k]*ev(ds[k+1]) for k in range(3)),s.zeros(4,1)))
 V=sum((s.kronecker_product(ev(G)*s.sympify(spin[k]).subs(pt),al[k]) for k in range(3)),s.zeros(12))+s.kronecker_product(Y,beta)*hm.subs(pt).evalf(30)
 res=s.Matrix.vstack(*kin)-V*psi
 norms=[float(s.sqrt(s.re(sum(s.conjugate(res[4*k+j])*res[4*k+j] for j in range(4))).evalf(30))) for k in range(3)]
 proj=[float(s.im((fs[k].conjugate().T*res[4*k:4*k+4,0])[0])) for k in range(3)]
 cross=float(s.im((psi.conjugate().T*s.kronecker_product(S,s.eye(4))*res)[0]))
 item={'point':{str(k):str(val) for k,val in pt.items()},'residual_norms_ABC':norms,'imaginary_species_projections':proj,'imaginary_cross_projection':cross}
 results.append(item); print(json.dumps(item),flush=True)
 assert max(norms)>1e-5
 assert max(map(abs,proj+[cross]))<1e-20
Path(__file__).with_suffix('.json').write_text(json.dumps({'convention':'R=i dt psi+i alpha grad psi-V psi; N=16; 30 digit evaluation of analytic derivatives','results':results},indent=2))
print('PASS: nonzero full residual despite vanishing current projections')
