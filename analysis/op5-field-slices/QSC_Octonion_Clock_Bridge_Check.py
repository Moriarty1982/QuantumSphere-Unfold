from pathlib import Path
import sympy as s,json
v,w,t=s.symbols('v omega t',real=True);gamma=1/s.sqrt(1-v*v)
assert s.simplify(gamma**2-(gamma*v)**2-1)==0
normchange=s.simplify(gamma**2+(gamma*v)**2-1)
tau=s.Function('tau')(t);phase=s.exp(-s.I*w*tau);assert s.simplify(s.diff(phase,t)+s.I*w*s.diff(tau,t)*phase)==0
a,b,c,d,omega1,omega2=s.symbols('a b c d omega1 omega2');M=s.Matrix([[a*c,a*d*s.exp(-s.I*omega2*tau)],[b*c*s.exp(-s.I*omega1*tau),b*d*s.exp(-s.I*(omega1+omega2)*tau)]]);assert s.simplify(M.det())==0
out={'field_embedding':'Chosen complex unit gives real decomposition O = C plus C^3; z=E+iB can be placed in the six-dimensional complement, with frame/orientation data still external or in additional registers.','Lorentz_bilinear_invariant':1,'positive_norm_change':str(normchange),'clock_chain_rule':'d psi/dt = -i omega (d tau/dt) psi','shared_clock_product_state_determinant':str(s.simplify(M.det())),'scope':'Conditional bridge checks; not construction of a native octonionic Lorentz action or a common quantum-gravity clock.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(out)
