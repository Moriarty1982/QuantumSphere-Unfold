import sympy as s
from pathlib import Path
import json
t,x=s.symbols('t x',real=True)
f=(5+3*s.cos(16*t))/8
Y=s.Matrix([s.sin(16*t)*(s.Rational(1,16)+x*x), f*x])
z=[t,x]; J=Y.jacobian(z)
# Evaluate derivatives at t=0 before inversion to keep exact checks small.
J0=J.subs(t,0); inv0=J0.inv()
dJ=[J.diff(a).subs(t,0) for a in z]
G=[inv0*a for a in dJ]
dG={}
for m in range(2):
 for n in range(2):
  dG[m,n]=-inv0*dJ[m]*inv0*dJ[n]+inv0*J.diff(z[m]).diff(z[n]).subs(t,0)
R=s.simplify(dG[0,1]-dG[1,0]+G[0]*G[1]-G[1]*G[0])
assert R==s.zeros(2)
assert s.simplify(G[0][1,0]+96*x)==0
assert J0==s.diag(1+16*x*x,1)
# Unit-tangent reference-rest line, interpreted with induced proper time at t=0.
a=s.simplify(96*x/(1+16*x*x)**2)
report={'slice':'y=z=0; exact t=0 identities for all x','J0':str(J0),'Gamma_t':str(G[0]),'Gamma_x':str(G[1]),'R_tx':str(R),'relative_acceleration_magnitude_signed':str(a),'example_x_1_10':str(a.subs(x,s.Rational(1,10)))}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
