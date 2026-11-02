from pathlib import Path
import json,time,mpmath as m,sympy as s
base=Path(__file__).resolve().parents[1] / 'OP5_Counterflow_Full_Residual_Check.py';exec(base.read_text(encoding='utf-8-sig').split('results=[]')[0])
raw=json.loads(Path('OP5_Direct_Compatibility_Solve.json').read_text(),parse_float=str)[0]
def convert(a):return m.matrix([[m.mpc(str(s.re(v)),str(s.im(v))) for v in row] for row in s.Matrix(a).tolist()])
def kron(a,b):return m.matrix(a.rows*b.rows,a.cols*b.cols,lambda i,j:a[i//b.rows,j//b.cols]*b[i%b.rows,j%b.cols])
# m.matrix(rows,cols,lambda) is not supported; explicit list form.
def kron(a,b):return m.matrix([[a[i//b.rows,j//b.cols]*b[i%b.rows,j%b.cols] for j in range(a.cols*b.cols)] for i in range(a.rows*b.rows)])
def norm(v):return m.sqrt(sum(abs(a)**2 for a in v))
out=[]
for digits in [30,50,80]:
 for normalized in [False,True]:
  m.mp.dps=digits;start=time.time();K=[convert(s.eye(4))]+[convert(a) for a in al];QQ=[kron(convert(S),a) for a in K];KK=[kron(m.eye(3),a) for a in K];ZB=kron(m.diag([1,-1,0]),convert(beta));hh=m.mpf(5)/(2*m.sqrt(3));theta=m.asin(m.mpf('.5'))/2;pp=3*m.cos(theta)/(2*m.mpf('.6')*m.sqrt(m.mpf('.75')));qq=-3*m.sin(theta)/(2*m.mpf('.6')*m.sqrt(m.mpf('.75')));gg=m.matrix([[0,0,pp],[0,0,qq],[pp,qq,0]]);gauge=[m.zeros(12),m.zeros(12),kron(gg,m.eye(4)),m.zeros(12)];mass=hh*kron(convert(Y),convert(beta))
  psi=m.matrix([m.mpc(*v) for v in raw['field_values_real_imag']]);jets=[m.matrix([m.mpc(*v) for v in raw['all_jets_real_imag'][mu*12:(mu+1)*12]]) for mu in range(4)]
  if normalized:psi*=m.sqrt(8/(hh*m.re((psi.H*ZB*psi)[0])))
  cov=[jets[mu]+1j*gauge[mu]*psi for mu in range(4)];E0=m.matrix([m.re((psi.H*q*cov[0])[0]) for q in QQ]);indices=[64,28,40]
  original=[m.re(z) for jj in jets[1:] for z in jj]+[m.im(z) for jj in jets[1:] for z in jj]
  def evaluate(a,b,c):
   v=original.copy()
   for i,z in zip(indices,[a,b,c]):v[i]=z
   js=[m.matrix([m.mpc(v[mu*12+j],v[36+mu*12+j]) for j in range(12)]) for mu in range(3)];ds=[js[mu]+1j*gauge[mu+1]*psi for mu in range(3)];E=m.matrix([[E0[aa]]+[m.re((psi.H*QQ[aa]*d)[0]) for d in ds] for aa in range(4)]);inv=E**-1;Ps=[sum((inv[mu,aa]*KK[aa] for aa in range(4)),m.zeros(12)) for mu in range(4)];bvec=sum((1j*Ps[mu+1]*ds[mu] for mu in range(3)),m.zeros(12,1))-mass*psi;dt=m.lu_solve(1j*Ps[0],-bvec);C=m.matrix([m.re((psi.H*q*dt)[0])-E0[aa] for aa,q in enumerate(QQ)])
   return C,[dt]+ds,E
  def fun(a,b,c):
   C,_,_=evaluate(a,b,c);return C[1],C[2],C[3]
  root=m.findroot(fun,tuple(original[k] for k in indices),tol=m.mpf(10)**(-(digits-8)),maxsteps=30);C,ds,E=evaluate(*root);actual=m.matrix([[m.re((psi.H*q*ds[mu])[0]) for mu in range(4)] for q in QQ]);inv=actual**-1;R=sum((1j*sum((inv[mu,aa]*KK[aa] for aa in range(4)),m.zeros(12))*ds[mu] for mu in range(4)),m.zeros(12,1))-mass*psi
  out.append({'decimal_digits':digits,'renormalized_state':normalized,'constraint_norm':m.nstr(norm(C),12),'full_residual_norm':m.nstr(norm(R),12),'scalar_input_defect':m.nstr(4-hh*m.re((psi.H*ZB*psi)[0])/2,12),'seconds':time.time()-start});print(out[-1],flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
