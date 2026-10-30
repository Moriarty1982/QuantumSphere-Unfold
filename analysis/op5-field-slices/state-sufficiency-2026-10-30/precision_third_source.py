"""Reconstruct completed second-derivative source with third jet zero."""
import precision_completed_rebuild as m
import mpmath as mp,sympy as s,json,itertools,time
R=m.ROOT;tic=time.time();root=json.loads((R/'precision-completed-root-result.json').read_text());second=json.loads((R/'precision-second-jet-result.json').read_text());v=mp.matrix([mp.mpf(x) for x in root['first_derivatives_real_packed']]);p0=m.psi.copy();pairs=[tuple(x) for x in second['pairs']];cc=[mp.mpf(x) for x in second['second_coefficients_real_packed']]
j0=[mp.matrix([mp.mpc(v[mu*24+k],v[mu*24+k+12]) for k in range(12)]) for mu in range(4)];H={pair:mp.matrix([mp.mpc(cc[i*24+k],cc[i*24+k+12])*(2 if pair[0]==pair[1] else 1) for k in range(12)]) for i,pair in enumerate(pairs)}
# Compile only distinct nonzero background expressions. This preserves the
# coordinate dependence to every order used by differentiation.
exprs=[m.ns['hm']]+[m.ns['hm'].diff(x) for x in m.coords]+[z for mat in m.cs for z in mat]+[z for x in m.coords for mat in m.cs for z in mat.diff(x)]
unique=list(dict.fromkeys(exprs));lookup={z:i for i,z in enumerate(unique)};fun=s.lambdify(m.coords,unique,modules='mpmath',cse=True);indexes=[lookup[z] for z in exprs];point=[mp.mpf(str(x)) for x in m.pos]
orig={k:getattr(m,k) for k in ['psi','h','dh','conn','dc','A']}
def path(t,direction):
 try:
  dx=[t*x for x in direction];m.psi=p0+sum((dx[mu]*j0[mu] for mu in range(4)),mp.zeros(12,1))+sum((dx[mu]*dx[nu]*H[(mu,nu)]*(mp.mpf('.5') if mu==nu else 1) for mu,nu in pairs),mp.zeros(12,1))
  js=[j0[mu]+sum((dx[nu]*H[tuple(sorted((mu,nu)))] for nu in range(4)),mp.zeros(12,1)) for mu in range(4)];vv=mp.matrix([z for row in js for z in m.realvec(row)])
  values=fun(*[point[mu]+dx[mu] for mu in range(4)]);values=[values[i] for i in indexes];m.h=values[0];m.dh=values[1:5];off=5
  m.conn=[]
  for i in range(4):m.conn.append(mp.matrix([[values[off+i*144+a*12+b] for b in range(12)] for a in range(12)]))
  off+=576;m.dc=[[mp.matrix([[values[off+(mu*4+nu)*144+a*12+b] for b in range(12)] for a in range(12)]) for nu in range(4)] for mu in range(4)]
  m.A=mp.matrix([[mp.re(z) for z in (m.psi.conjugate().T*q)]+[-mp.im(z) for z in (m.psi.conjugate().T*q)] for q in m.Q]);return m.evaluate(vv)
 finally:
  for k,z in orig.items():setattr(m,k,z)
if __name__=='__main__':
 diagonal=[];sources={}
 for mu in range(4):
  d=[int(i==mu) for i in range(4)];value=mp.diff(lambda t:path(t,d),mp.mpf('0'),2);diagonal.append(value);sources[(mu,mu)]=value/2
 for mu,nu in pairs:
  if mu==nu:continue
  d=[int(i in (mu,nu)) for i in range(4)];value=mp.diff(lambda t:path(t,d),mp.mpf('0'),2);sources[(mu,nu)]=(value-diagonal[mu]-diagonal[nu])/2
 out={'contract':'Degree-two normalized completed R source at repaired second jet, with third field derivatives set to zero. Full symbolic background via mpmath; second directional derivatives and polarization. No higher compatibility claim yet.','pairs':pairs,'source_real_packed':[mp.nstr(x,70) for pair in pairs for x in sources[pair]],'seconds':time.time()-tic,'R0_max':mp.nstr(m.norm(path(mp.mpf('0'),[0]*4)),24)}
 (R/'precision-third-source-result.json').write_text(json.dumps(out,indent=2));print('third source saved',out['seconds'],out['R0_max'],flush=True)
