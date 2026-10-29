from pathlib import Path
import numpy as np,json
base=Path(__file__).with_name('OP5_Sector_Transport_Full_Equation_Check.py')
# Reuse its declared field evaluator only; no historical output is overwritten.
exec(base.read_text().split('out=[]')[0])
pack=lambda w:np.r_[w.real,w.imag]
out=[]
for pt in points:
 ev=lambda m:s.Matrix(m).subs(pt).evalf(30)
 psi=arr(s.Matrix.vstack(*[ev(f) for f in fields])).reshape(-1)
 ds=[arr(s.Matrix.vstack(*[ev(dfs[mu]) for dfs in derivs])).reshape(-1) for mu in range(4)]
 km=[np.eye(4)]+[arr(a) for a in al]
 vv=np.array([float(vj.subs(pt)) for vj in v]);E=np.eye(4);E[0,0]=2;E[1:,0]=vv
 inv=np.linalg.inv(E);Ps=[sum((inv[mu,a]*km[a] for a in range(4)),np.zeros((4,4),complex)) for mu in range(4)]
 q0=float(th.diff(t).subs(pt));Am=[-q0*arr(Y)]+[float(s.sympify(spin[j]).subs(pt))*arr(ev(G)) for j in range(3)]
 mass=float(hm.subs(pt))*np.kron(arr(Y),arr(beta))@psi
 res=sum((1j*np.kron(np.eye(3),Ps[mu])@ds[mu]-np.kron(Am[mu],Ps[mu])@psi for mu in range(4)),np.zeros(12,complex))-mass
 cv=float(c.subs(pt));dv=float(d.subs(pt))
 n=np.array([cv,-dv,0]);m=np.array([dv,cv,0]);zv=np.array([0,0,1])
 basis=[np.outer(m,m),np.outer(n,n),np.outer(zv,zv),(np.outer(n,zv)+np.outer(zv,n))/np.sqrt(2),1j*(np.outer(n,zv)-np.outer(zv,n))/np.sqrt(2)]
 R=np.eye(3)-2*(np.outer(n,n)+np.outer(zv,zv))
 assert all(np.linalg.norm(B@R-R@B)<1e-12 for B in basis)
 M=np.zeros((24,20));Q=np.zeros((16,20))
 for mu in range(4):
  for j,B in enumerate(basis):
   col=5*mu+j;M[:,col]=pack(-np.kron(B,Ps[mu])@psi)
   w=1j*np.kron(B,np.eye(4))@psi
   for a in range(4):Q[4*mu+a,col]=np.vdot(psi,np.kron(arr(S),km[a])@w).real
 Uq,sq,Vhq=np.linalg.svd(Q,full_matrices=True)
 rankq=int(np.sum(sq>1e-11));Z=Vhq[rankq:].T
 assert np.linalg.norm(Q@Z)<1e-10
 summaries={}
 for name,L in [('sector_only',np.eye(20)),('sector_and_coframe',Z)]:
  A=M@L;coef,_,rank,sv=np.linalg.lstsq(A,-pack(res),rcond=1e-12);coeff=L@coef
  remainder=pack(res)+M@coeff
  assert np.linalg.norm(A.T@remainder)<1e-9
  full=res.copy()
  for mu in range(4):
   C=sum((coeff[5*mu+j]*basis[j] for j in range(5)),np.zeros((3,3),complex))
   full-=np.kron(C,Ps[mu])@psi
  assert np.linalg.norm(pack(full)-remainder)<1e-10
  summaries[name]={'rank':int(rank),'singular_values':sv.tolist(),'coefficients':coeff.tolist(),'residual_norm2':float(remainder@remainder),'coframe_change_norm':float(np.linalg.norm(Q@coeff))}
 out.append({'point':{str(k):str(vv) for k,vv in pt.items()},'coframe_constraint_rank':rankq,'remaining_parameters':Z.shape[1],'coframe_singular_values':sq.tolist(),'original_norm2':float(np.vdot(res,res).real),'fits':summaries})
 print(json.dumps(out[-1]))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
