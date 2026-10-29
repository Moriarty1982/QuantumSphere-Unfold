from pathlib import Path
import json
import numpy as np
src=Path(__file__).with_name('OP5_Counterflow_Full_Residual_Check.py')
exec(src.read_text(encoding='utf-8-sig').split('results=[]')[0])
arr=lambda m:np.array(m.tolist(),complex).reshape(-1)
pack=lambda a:np.r_[a.real,a.imag]
out=[]
for pt in points:
 ev=lambda m:s.Matrix(m).subs(pt).evalf(30)
 psi=s.Matrix.vstack(*[ev(f) for f in fields])
 V=sum((s.kronecker_product(ev(G)*s.sympify(spin[j]).subs(pt),al[j]) for j in range(3)),s.zeros(12))+s.kronecker_product(Y,beta)*hm.subs(pt).evalf(30)
 spatial=s.Matrix.vstack(*[sum((al[j]*ev(ds[j+1]) for j in range(3)),s.zeros(4,1)) for ds in derivs])
 vel=-spatial-I*V*psi
 cv=c.subs(pt).evalf(30);dv=d.subs(pt).evalf(30)
 b= cv*vel[4:8,0]-dv*vel[:4,0]
 uu=ev(U);ww=ev(W)
 als=sum((al[j]*s.sympify(spin[j]).subs(pt) for j in range(3)),s.zeros(4))
 formula=hm.subs(pt).evalf(30)*beta*uu+I*(d*p-c*q).subs(pt).evalf(30)*als*ww
 assert np.linalg.norm(arr(b-formula))<1e-12
 # all initial theta spatial derivatives vanish in prescribed chart
 target=pack(arr(b));uv=arr(uu)
 def fit(columns):
  mat=np.column_stack([pack(a) for a in columns])
  coef,_,rank,sv=np.linalg.lstsq(mat,target,rcond=1e-12)
  residual=target-mat@coef
  assert np.linalg.norm(mat.T@residual)<1e-9
  return {'rank':int(rank),'coefficients':coef.tolist(),'singular_values':sv.tolist(),'residual_norm2':float(residual@residual),'target_norm2':float(target@target)}
 realfit=fit([uv])
 complexfit=fit([uv,1j*uv])
 # altered initial spatial jets: theta_t u+sum theta_i alpha_i u=source
 relaxed=fit([uv]+[arr(a*uu) for a in al])
 phase_relaxed=fit([uv]+[arr(a*uu) for a in al]+[1j*uv])
 phase_normal_bound=float(np.vdot(uv,arr(b)).imag**2/np.vdot(uv,uv).real)
 assert abs(relaxed['residual_norm2']-phase_normal_bound)<1e-9
 assert phase_relaxed['residual_norm2']<1e-20
 fixed=arr(b-th.diff(t).subs(pt).evalf(30)*uu)
 out.append({'point':{str(k):str(vv) for k,vv in pt.items()},'fixed_theta_rate_residual_norm2':float(np.vdot(fixed,fixed).real),'real_proportional_time_only':realfit,'complex_proportional_time_only':complexfit,'released_spatial_theta_jets':relaxed,'imaginary_overlap_lower_bound':phase_normal_bound,'released_spatial_theta_and_relative_phase':phase_relaxed})
 print(json.dumps(out[-1]),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
