"""Bounded Newton repair of all 32 completed first-jet residuals."""
import precision_completed_rebuild as m
import mpmath as mp,numpy as np,json,time
from pathlib import Path
tic=time.time();v=m.v.copy();history=[];initial=v.copy();selected=None
for iteration in range(3):
 columns=[]
 for col in range(96):
  def f(t):
   z=v.copy();z[col]+=t;return m.evaluate(z)
  columns.append(mp.diff(f,mp.mpf('0')))
 J=mp.matrix([[columns[j][i] for j in range(96)] for i in range(32)])
 if selected is None:
  a=np.array(J.tolist(),float);selected=[]
  for i in range(32):
   if np.linalg.matrix_rank(a[selected+[i]],tol=1e-9)>len(selected):selected.append(i)
  print('independent_rows',len(selected),flush=True)
  if len(selected)!=31:raise RuntimeError('Unexpected completed rank')
 A=mp.matrix([[J[i,j] for j in range(96)] for i in selected]);r=m.evaluate(v);b=mp.matrix([r[i] for i in selected]);dx=-A.T*((A*A.T)**-1)*b;v+=dx;r=m.evaluate(v)
 row={'iteration':iteration+1,'full_R_max':mp.nstr(m.norm(r),24),'F_max':mp.nstr(m.norm(r[:24]),24),'G_max':mp.nstr(m.norm(r[24:28]),24),'dg_max':mp.nstr(m.norm(r[28:]),24)};history.append(row);print(row,flush=True)
result={'contract':'70-digit numerical completed first-jet root repair. psi fixed from scalar chart; all 96 real first derivatives free. Full 32 residuals checked after 31-row Newton updates. No exact/interval or regional certificate, no Omega.','selected_rows':selected,'history':history,'derivative_change_max_real':mp.nstr(m.norm(v-initial),24),'seconds':time.time()-tic,'first_derivatives_real_packed':[mp.nstr(x,70) for x in v],'psi':m.data['psi'],'point':m.data['point']}
(m.ROOT/'precision-completed-root-result.json').write_text(json.dumps(result,indent=2))
