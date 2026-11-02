from pathlib import Path
import sympy as s,json
I=s.I;rx=s.Matrix([[0,1],[1,0]]);rz=s.diag(1,-1);cp=(s.eye(2)+rx)/2;ca=s.Rational(3,5);sa=s.Rational(4,5);rotation=s.Matrix([[ca,sa],[-sa,ca]])
def chart(F):
 G=F.T*F;a=G[0,0];c=G[0,1];b=G[1,1];D=s.sqrt(a*b-c*c);f0=s.Matrix([[s.sqrt(a),c/s.sqrt(a)],[0,D/s.sqrt(a)],[0,0]]);e=F[:,0]/s.sqrt(a);q=(F[:,1]-c/a*F[:,0])/(D/s.sqrt(a));O=s.Matrix.hstack(e,q,e.cross(q));return G,f0,O
rows=[]
for E,B in [(s.Matrix([2,1,0]),s.Matrix([0,1,2])),(s.Matrix([1,2,3]),s.Matrix([2,-1,1]))]:
 F=s.Matrix.hstack(E,B);z=E+I*B;G,f0,O=chart(F)
 for name,M,znew in [('duality',rotation,(ca+I*sa)*z),('J_B',rx,I*s.conjugate(z)),('T',rz,s.conjugate(z)),('HC',cp,(z+I*s.conjugate(z))/2)]:
  full=s.Matrix.hstack(znew.applyfunc(s.re),znew.applyfunc(s.im));mapped=O*f0*M;assert (full-mapped).applyfunc(s.simplify)==s.zeros(3,2);Gp=(M.T*G*M).applyfunc(s.simplify);assert (full.T*full-Gp).applyfunc(s.simplify)==s.zeros(2)
  if Gp.det()!=0:
   _,newf0,K=chart(f0*M);Onew=(O*K).applyfunc(s.simplify);assert (Onew*newf0-full).applyfunc(s.simplify)==s.zeros(3,2);kind='rank2 orientation updated'
  else:
   axis=(O*(f0*M)[:,0]/s.sqrt(Gp[0,0])).applyfunc(s.simplify);recon=axis*s.Matrix([[s.sqrt(Gp[0,0]),Gp[0,1]/s.sqrt(Gp[0,0])]]);assert (recon-full).applyfunc(s.simplify)==s.zeros(3,2);kind='rank1 direction chart'
  rows.append({'operation':name,'matrix_diagram_commutes':True,'chart':kind,'rho_output':str((Gp/s.trace(Gp)).applyfunc(s.simplify))})
# Vanishing selected port is outside normalized-state domain.
F=s.Matrix.hstack(s.Matrix([1,0,0]),s.Matrix([-1,0,0]));assert F*cp==s.zeros(3,2)
Path(__file__).with_suffix('.json').write_text(json.dumps({'checks':rows,'zero_port_normalization_defined':False,'non_claims':['Structural operations are not a derived common physical time generator','No full octonionic product compatibility established']},indent=2));print(rows)
