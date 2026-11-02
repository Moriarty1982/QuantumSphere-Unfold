"""Affine Omega repair along a refined compatible third-jet direction."""
import os
os.environ['OPENBLAS_NUM_THREADS']='2';os.environ['OMP_NUM_THREADS']='2'
from pathlib import Path
import json,itertools,numpy as np,mpmath as mp,time,hashlib
R=Path(__file__).resolve().parent;tic=time.time();env={'__file__':str(R/'precision_fourth_source.py')};exec((R/'precision_fourth_source.py').read_text().split('values=[]')[0],env);ns=env['ns'];dirs=env['dirs'];W=env['W'];mp.mp.dps=70
jdata=json.loads((R/'precision-completed-symbol-result.json').read_text());jm=[[mp.mpf(x) for x in row] for row in jdata['matrix_decimal']];jf=np.array(jdata['matrix_decimal'],float);low=list(itertools.combinations_with_replacement(range(4),2));high=list(itertools.combinations_with_replacement(range(4),3));look={a:i for i,a in enumerate(high)};A=np.zeros((320,480));entries=[]
for i,a in enumerate(low):
 for mu in range(4):
  col=look[tuple(sorted((*a,mu)))];w=a.count(mu)+1;A[i*32:(i+1)*32,col*24:(col+1)*24]+=w*jf[:,mu*24:(mu+1)*24];entries.append((i,col,mu,w))
def select(A,rank):
 M=A.copy();rp=np.arange(A.shape[0]);cp=np.arange(A.shape[1])
 for k in range(rank):
  i,j=np.unravel_index(np.argmax(abs(M[k:,k:])),M[k:,k:].shape);i+=k;j+=k;M[[k,i]]=M[[i,k]];rp[[k,i]]=rp[[i,k]];M[:,[k,j]]=M[:,[j,k]];cp[[k,j]]=cp[[j,k]];M[k+1:,k+1:]-=np.outer(M[k+1:,k]/M[k,k],M[k,k+1:]);M[k+1:,k]=0
 return rp[:rank],cp[:rank]
rows,cols=select(A,271);inv=np.linalg.inv(A[np.ix_(rows,cols)])
def apply3(x):
 out=[mp.mpf('0') for _ in range(320)]
 for i,col,mu,w in entries:
  for j in range(32):out[i*32+j]+=w*mp.fsum(jm[j][mu*24+k]*x[col*24+k] for k in range(24))
 return out
old=np.load(R/'completion-omega-witness.npz')['third_direction'];u,s,vh=np.linalg.svd(A,full_matrices=True);N=vh[271:].T;df=N@(N.T@old);d=[mp.mpf(float(x)) for x in df]
for _ in range(7):
 rr=apply3(d);dx=-inv@np.array([float(rr[i]) for i in rows])
 for c,x in zip(cols,dx):d[c]+=mp.mpf(float(x))
leak=max(abs(x) for x in apply3(d));base=json.loads((R/'precision-third-jet-result.json').read_text());c0=[mp.mpf(x) for x in base['third_coefficients_real_packed']];b0=[mp.mpf(x) for x in json.loads((R/'precision-fourth-source-result.json').read_text())['source_real_packed']];lam=[mp.mpf(x) for x in json.loads((R/'precision-fourth-left-witness-result.json').read_text())['left_witness']]
def source(step):
 c=[x+step*y for x,y in zip(c0,d)];ns['T3']=[mp.matrix([mp.mpc(c[i*24+k],c[i*24+k+12]) for k in range(12)]) for i in range(20)];vals=[mp.diff(lambda t:ns['path'](t,v),mp.mpf('0'),3)/6 for v in dirs]
 return [sum(mp.mpf(str(W[i,j]))*vals[j][k] for j in range(20)) for i in range(20) for k in range(32)]
b1=source(mp.mpf('1'));delta=[x-y for x,y in zip(b1,b0)];slope=mp.fsum(x*y for x,y in zip(lam,delta));initial=mp.fsum(x*y for x,y in zip(lam,b0));step=-initial/slope;bc=source(step);pred=[x+step*y for x,y in zip(b0,delta)];afferr=max(abs(x-y) for x,y in zip(bc,pred));print('direction leak',mp.nstr(leak,10),'step',mp.nstr(step,18),'affine error',mp.nstr(afferr,10),flush=True)
# Re-eliminate fourth jet against all640 residuals at the corrected third jet.
e4=json.loads((R/'precision-fourth-elimination-result.json').read_text());r4=e4['selected_rows'];c4=e4['selected_columns'];a4=np.load(R/'precision-fourth-elimination.npz')['principal'];inv4=np.linalg.inv(a4[np.ix_(r4,c4)]);four=list(itertools.combinations_with_replacement(range(4),4));l4={a:i for i,a in enumerate(four)}
def apply4(x):
 out=[mp.mpf('0') for _ in range(640)]
 for i,a in enumerate(high):
  for mu in range(4):
   col=l4[tuple(sorted((*a,mu)))];w=a.count(mu)+1
   for j in range(32):out[i*32+j]+=w*mp.fsum(jm[j][mu*24+k]*x[col*24+k] for k in range(24))
 return out
q=[mp.mpf('0') for _ in range(840)]
for _ in range(7):
 r=[x+y for x,y in zip(apply4(q),bc)];dx=-inv4@np.array([float(r[i]) for i in r4])
 for col,x in zip(c4,dx):q[col]+=mp.mpf(float(x))
r=[x+y for x,y in zip(apply4(q),bc)];new=[x+step*y for x,y in zip(c0,d)];out={'contract':'One directional repair of rebuilt compatibility source. Field0..2 fixed; refined third-jet tangent moves thirdcoefficients; fourth coefficients re-solved. Complete residuals retained. No full Omega covector or all-order/exact certificate.','third_direction_lower_equation_leak':mp.nstr(leak,24),'Omega_left_source_before':mp.nstr(initial,24),'Omega_direction_slope':mp.nstr(slope,24),'correction_step':mp.nstr(step,24),'actual_source_affine_prediction_error':mp.nstr(afferr,24),'Omega_left_source_after':mp.nstr(mp.fsum(x*y for x,y in zip(lam,bc)),24),'full640_fourth_completion_residual_max':mp.nstr(max(abs(x) for x in r),24),'third_coefficient_correction_max':mp.nstr(max(abs(step*x) for x in d),24),'third_coefficients_real_packed':[mp.nstr(x,70) for x in new],'fourth_coefficients_real_packed':[mp.nstr(x,70) for x in q],'corrected_source_real_packed':[mp.nstr(x,70) for x in bc],'seconds':time.time()-tic}
(R/'precision-omega-repair-result.json').write_text(json.dumps(out,indent=2));print({k:v for k,v in out.items() if 'packed' not in k},flush=True)
