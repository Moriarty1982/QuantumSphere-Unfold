from pathlib import Path
import json,numpy as np
src=Path(__file__).with_name('OP5_Counterflow_Full_Residual_Check.py')
exec(src.read_text(encoding='utf-8-sig').split('results=[]')[0])
phase=json.loads(Path(__file__).with_name('OP5_Self_Consistent_AB_Gate_Check.json').read_text())
arr=lambda m:np.array(m.tolist(),complex)
out=[]
for pt,datum in zip(points,phase):
 ev=lambda m:s.Matrix(m).subs(pt).evalf(30)
 psi=s.Matrix.vstack(*[ev(f) for f in fields]);ps=arr(psi).reshape(-1)
 V=sum((s.kronecker_product(ev(G)*s.sympify(spin[j]).subs(pt),al[j]) for j in range(3)),s.zeros(12))+s.kronecker_product(Y,beta)*hm.subs(pt).evalf(30)
 old=arr(s.Matrix.vstack(*[sum((I*K*ev(ds[mu]) for mu,K in enumerate([s.eye(4)]+al)),s.zeros(4,1)) for ds in derivs])-V*psi).reshape(-1)
 cv=float(c.subs(pt));dv=float(d.subs(pt))
 B=np.diag([-dv/cv,cv/dv,0])
 Bh=B-np.trace(B)/3*np.eye(3)
 lv=np.array(datum['relaxed_phase_covector'])
 km=[np.eye(4)]+[arr(a) for a in al]
 results={}
 for name,gen in [('diagonal',B),('traceless',Bh)]:
  delta=-sum((lv[mu]*np.kron(gen,km[mu])@ps for mu in range(4)),np.zeros(12,complex))
  new=old+delta
  for mu in range(4):
   for K in km:
    change=np.vdot(ps,np.kron(arr(S),K)@(1j*lv[mu]*np.kron(gen,np.eye(4))@ps)).real
    assert abs(change)<1e-10
  assert np.linalg.norm(cv*new[4:8]-dv*new[:4])<1e-10
  results[name]={'trace':float(np.trace(gen)),'full_residual_norm2':float(np.vdot(new,new).real),'ABC_norms':[float(np.linalg.norm(new[4*j:4*j+4])) for j in range(3)]}
 out.append({'point':datum['point'],'original_norm2':float(np.vdot(old,old).real),'variants':results})
 print(json.dumps(out[-1]))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
