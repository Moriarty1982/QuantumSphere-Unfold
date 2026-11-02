import sympy as s,json
from pathlib import Path
x=s.symbols('t x y z', real=True); t,a,b,z=x
V=s.Matrix([1,-a/t,-b/t,-z/t]); W=s.Matrix([0,-a*z/(a*a+b*b),-b*z/(a*a+b*b),1])
def bracket(A,B): return (B.jacobian(x)*A-A.jacobian(x)*B).applyfunc(s.simplify)
def div(A): return s.simplify(sum(s.diff(A[i],x[i]) for i in range(4)))
checks={'bracket_V_W':bracket(V,W)==W/t,'commuting_rescaled_pair':bracket(V,W/t)==s.zeros(4,1),'div_V':div(V)==-3/t,'div_W':div(W)==0,'div_W_over_t':div(W/t)==0}
assert all(checks.values()),checks
out={'checks':checks,'domain':'t != 0, x^2+y^2 > 0','method':'exact SymPy symbolic simplification','non_claims':['No physical Hilbert space or native dynamics established']}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out))
