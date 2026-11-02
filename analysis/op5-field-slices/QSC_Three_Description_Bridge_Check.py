from pathlib import Path
import sympy as s,json
u,x,y,z,e=s.symbols('u x y z eta',real=True);X=s.Matrix([[u+z,x-s.I*y],[x+s.I*y,u-z]]);B=s.diag(s.exp(e/2),s.exp(-e/2));Y=B*X*B
assert s.simplify(Y.det()-X.det())==0
normal=lambda M:s.simplify(M/s.trace(M))
assert (normal(B*normal(X)*B)-normal(Y)).applyfunc(s.simplify)==s.zeros(2)
# Rotations keep trace and normalized purity; boosts generally do not.
identity=s.eye(2);pure=normal(B*identity*B);purity=s.simplify(s.trace(pure*pure));expected=(1+s.tanh(e)**2)/2
assert s.simplify((purity-expected).rewrite(s.exp))==0
out={'carrier':'Positive nonzero Hermitian 2x2 matrices, chosen local complex/spin frame','determinant':str(s.factor(X.det())),'commuting_normalization_diagram':True,'boosted_unpolarized_purity':str(expected),'example_eta_1':float(expected.subs(e,1)),'non_claims':['Not a complete ART state or full QSC octonion embedding','SL(2,C) normalized congruence is not generally unitary quantum evolution','Shared rank/determinant sign is not a physical mass-purity identification']}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(out)
