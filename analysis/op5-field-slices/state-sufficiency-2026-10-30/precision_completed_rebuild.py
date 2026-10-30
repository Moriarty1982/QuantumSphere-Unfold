"""High precision completed first-jet source reconstruction, fixed comparison."""
from pathlib import Path
import json,mpmath as mp,sympy as s,numpy as np,time,hashlib
ROOT=Path(__file__).resolve().parent
helper={"__file__":str(ROOT/'precision_primitive_rebuild.py')};exec((ROOT/'precision_primitive_rebuild.py').read_text().split('\nresults=[]')[0],helper)
ns=helper['ns'];mat=helper['mat'];cm=helper['cm'];realmat=helper['realmat'];realvec=helper['realvec'];norm=helper['norm']
mp.mp.dps=70;tic=time.time();seed=ROOT/'precision-first-jet-70.json';data=json.loads(seed.read_text());pos=[s.Rational(v) for v in data['point']];coords=[ns[v] for v in ['t','x','y','z']];subs=dict(zip(coords,pos))
psi=mp.matrix([mp.mpc(*v) for v in data['psi']]);js=[mp.matrix([mp.mpc(*v) for v in row]) for row in data['first_derivatives']]
K=[mat(s.kronecker_product(s.eye(3),v)) for v in [s.eye(4)]+ns['al']];Q=[mat(s.kronecker_product(ns['S'],v)) for v in [s.eye(4)]+ns['al']];Y=mat(s.kronecker_product(ns['Y'],ns['beta']));Z=mat(s.kronecker_product(s.diag(1,-1,0),ns['beta']))
h=cm(ns['hm'].subs(subs)).real;dh=[cm(ns['hm'].diff(x).subs(subs)).real for x in coords]
cs=[s.zeros(12)]+[s.kronecker_product(ns['G']*v,s.eye(4)) for v in ns['spin']];conn=[mat(v.subs(subs)) for v in cs];dc=[[mat(v.diff(x).subs(subs)) for v in cs] for x in coords]
Hb=[realmat(-mp.j*K[0])]+[realmat(mp.j*v) for v in K[1:]]
A=mp.matrix([[mp.re(v) for v in (psi.conjugate().T*q)]+[-mp.im(v) for v in (psi.conjugate().T*q)] for q in Q])
def evaluate(v):
 j=[mp.matrix([mp.mpc(v[mu*24+k],v[mu*24+k+12]) for k in range(12)]) for mu in range(4)]
 cov=[j[mu]+mp.j*conn[mu]*psi for mu in range(4)];E=mp.matrix([[mp.re((psi.conjugate().T*Q[a]*cov[mu])[0]) for mu in range(4)] for a in range(4)]);V=E**-1
 F=sum((mp.j*V[mu,a]*K[a]*cov[mu] for mu in range(4) for a in range(4)),mp.zeros(12,1))-h*Y*psi
 G=mp.zeros(4,1);C=mp.zeros(4,1)
 for mu in range(4):
  dv=[mp.j*(dc[mu][nu]*psi+conn[nu]*j[mu]) for nu in range(4)]
  dE=mp.matrix([[mp.re((j[mu].conjugate().T*Q[a]*cov[nu]+psi.conjugate().T*Q[a]*dv[nu])[0]) for nu in range(4)] for a in range(4)]);dV=-V*dE*V
  b=sum((mp.j*K[a]*(dV[nu,a]*cov[nu]+V[nu,a]*dv[nu]) for nu in range(4) for a in range(4)),mp.zeros(12,1))-dh[mu]*Y*psi-h*Y*j[mu]
  km=A*sum((V[mu,a]*Hb[a] for a in range(4)),mp.zeros(24));G+=km*realvec(b)
  C[mu]=-.5*dh[mu]*mp.re((psi.conjugate().T*Z*psi)[0])-h*mp.re((psi.conjugate().T*Z*j[mu])[0])
 return mp.matrix(list(realvec(F))+list(G)+list(C))
v=mp.matrix([x for row in js for x in realvec(row)])
if __name__ == "__main__":
 r=evaluate(v);out={'contract':'High precision analytic R=(F,G,dg) first-jet reconstruction; no higher jet or Omega computed. Fixed psi from scalar repair; no second derivatives used in b_mu, annihilated by principal syzygy.','initial_F_max':mp.nstr(norm(r[:24]),22),'initial_G_max':mp.nstr(norm(r[24:28]),22),'initial_dg_max':mp.nstr(norm(r[28:]),22)}
 print(out,flush=True)
 # Finite bounded derivative check at two columns, step convergence against mpmath differentiation.
 checks=[]
 for col in [0,37]:
  def f(t):
   vv=v.copy();vv[col]+=t;return evaluate(vv)
  d=mp.diff(f,mp.mpf('0'));tests=[]
  for step in ['1e-8','1e-12']:
   e=mp.mpf(step);fd=(f(e)-f(-e))/(2*e);tests.append({'step':step,'error':mp.nstr(norm(fd-d),20)})
  checks.append({'column':col,'controls':tests})
 out['derivative_controls']=checks;out['seconds']=time.time()-tic;out['seed_sha256']=hashlib.sha256(seed.read_bytes()).hexdigest()
 (ROOT/'precision-completed-result.json').write_text(json.dumps(out,indent=2));print(checks,flush=True)
 
