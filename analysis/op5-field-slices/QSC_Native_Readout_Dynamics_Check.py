from pathlib import Path
import sympy as s,json
v=s.symbols('v',real=True);g=1/s.sqrt(1-v*v);V=s.Matrix([v,0,0])
def boost(E,B):
 return s.simplify(g*(E+V.cross(B))-g*g/(g+1)*V*(V.dot(E))),s.simplify(g*(B-V.cross(E))-g*g/(g+1)*V*(V.dot(B)))
def gram(E,B):return s.Matrix([[E.dot(E),E.dot(B)],[E.dot(B),B.dot(B)]])
first=(s.Matrix([1,0,0]),s.zeros(3,1));second=(s.Matrix([0,1,0]),s.zeros(3,1));assert gram(*first)==gram(*second)
rows=[]
for tag,pair in [('parallel',first),('transverse',second)]:
 E,B=boost(*pair);G=gram(E,B);rho=(G/s.trace(G)).applyfunc(s.simplify);I=s.simplify(E.dot(E)-B.dot(B));J=s.simplify(E.dot(B));assert I==1 and J==0
 rows.append({'case':tag,'rho_after':str(rho),'rho_beta_3_5':str(rho.subs(v,s.Rational(3,5)).applyfunc(s.simplify)),'invariant_E2_minus_B2':str(I),'invariant_EdotB':str(J)})
assert rows[0]['rho_after']!=rows[1]['rho_after']
Path(__file__).with_suffix('.json').write_text(json.dumps({'same_input_Gram':str(gram(*first)),'same_observer_boost':'along x with speed v, |v|<1','results':rows,'implication':'No single-valued observer boost map of the native Gram state alone for all allowed field orientations. Full field plus observer restores defined readout.','non_claims':['No prediction of native QSC temporal generator','No proof of octonion carrier embedding or unified action']},indent=2));print(rows)
