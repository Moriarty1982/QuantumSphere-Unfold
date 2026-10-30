from pathlib import Path
import sympy as s,json
v=s.symbols('v',real=True);gam=1/s.sqrt(1-v*v);vel=s.Matrix([v,0,0]);out=[]
def boost(E,B):return ((gam*(E+vel.cross(B))-gam*gam/(gam+1)*vel*(vel.dot(E))).applyfunc(s.simplify),(gam*(B-vel.cross(E))-gam*gam/(gam+1)*vel*(vel.dot(B))).applyfunc(s.simplify))
def G(E,B):return s.Matrix([[E.dot(E),E.dot(B)],[E.dot(B),B.dot(B)]])
a1=s.Matrix([1,0,0]);a2=s.Matrix([0,1,0]);zero=s.zeros(3,1);assert G(a1,zero)==G(a2,zero);assert a1.cross(zero)==a2.cross(zero)
g1=G(*boost(a1,zero));g2=G(*boost(a2,zero));assert g1!=g2
# Generic exact reconstruction in a nondegenerate chart.
for E,B in [(s.Matrix([2,1,0]),s.Matrix([0,1,2])),(s.Matrix([1,2,3]),s.Matrix([2,-1,1]))]:
 gram=G(E,B);aa,cc,bb=gram[0,0],gram[0,1],gram[1,1];Delta=s.sqrt(aa*bb-cc**2);e=E/s.sqrt(aa);q=(B-cc/aa*E)/(Delta/s.sqrt(aa));n=e.cross(q);O=s.Matrix.hstack(e,q,n);canonical=s.Matrix([[s.sqrt(aa),cc/s.sqrt(aa)],[0,Delta/s.sqrt(aa)],[0,0]]);F=s.Matrix.hstack(E,B)
 assert (O.T*O-s.eye(3)).applyfunc(s.simplify)==s.zeros(3);assert s.simplify(O.det())==1;assert (O*canonical-F).applyfunc(s.simplify)==s.zeros(3,2)
 Eb,Bb=boost(E,B);u=(E.dot(E)+B.dot(B))/2;flux=E.cross(B);prediction=gam**2*(u*(1+v*v)-2*vel.dot(flux)-vel.dot(E)**2-vel.dot(B)**2);actual=(Eb.dot(Eb)+Bb.dot(Bb))/2;assert s.simplify(actual-prediction)==0
 out.append({'E':list(map(str,E)),'B':list(map(str,B)),'G':str(gram),'orientation_reconstructs_exactly':True,'energy_boost_formula_verified':True})
result={'flux_alone_insufficient':{'same_G':str(G(a1,zero)),'same_flux':'zero','boosted_G_first':str(g1),'boosted_G_second':str(g2)},'reconstruction_tests':out,'chart':'a=|E|²>0 and det G>0; rank-deficient cases require separate charts/stabilizers; nonzero null electromagnetic fields can have positive-definite Gram matrices','mediator':'G plus O in SO(3), observer relation and calibrated clock. Algebraic local field reconstruction only; not complete GR or quantum evolution.'};Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2));print(result)
