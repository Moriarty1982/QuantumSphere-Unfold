"""Completed principal symbol reconstructed at the 70-digit repaired first jet."""
import precision_completed_rebuild as m
import mpmath as mp,numpy as np,json,time,hashlib
from datetime import datetime,timezone
tic=time.time();started=datetime.now(timezone.utc).isoformat();rootfile=m.ROOT/'precision-completed-root-result.json';root=json.loads(rootfile.read_text());v=mp.matrix([mp.mpf(x) for x in root['first_derivatives_real_packed']]);columns=[]
for col in range(96):
 def f(t):
  z=v.copy();z[col]+=t;return m.evaluate(z)
 columns.append(mp.diff(f,mp.mpf('0')))
J=mp.matrix([[columns[j][i] for j in range(96)] for i in range(32)]);a=np.array(J.tolist(),float);sv=np.linalg.svd(a,compute_uv=False)
keep=root['selected_rows'];omitted=[i for i in range(32) if i not in keep];A=mp.matrix([[J[i,j] for j in range(96)] for i in keep]);b=mp.matrix([[J[i,j] for j in range(96)] for i in omitted]);coef=b*A.T*((A*A.T)**-1);identity=b-coef*A
# Precision cross-check at a second working precision, unchanged decimal input.
checks=[]
for col in [0,37,95]:
 with mp.workdps(45):
  def f(t):
   z=v.copy();z[col]+=t;return m.evaluate(z)
  low=mp.diff(f,mp.mpf('0'))
 checks.append({'column':col,'difference_45_vs_70_digits':mp.nstr(max(abs(low[i]-J[i,col]) for i in range(32)),24)})
old=np.load(m.ROOT/'completion-omega-witness.npz')['completed_first_symbol']
result={'contract':'Numerical completed first-order symbol at repaired 70-digit R root. Symbol only, not source/Omega reconstruction or all-order proof.','started_at_utc':started,'runtime_seconds':time.time()-tic,'digits':70,'root_residual_max':mp.nstr(m.norm(m.evaluate(v)),24),'rank_cutoff_tests':[{'rcond':c,'rank':int(sum(sv>sv[0]*c))} for c in [1e-8,1e-10,1e-12]],'last_singular_values':sv[-4:].tolist(),'largest_singular_value':float(sv[0]),'omitted_row_identity_error':mp.nstr(m.norm(identity),24),'precision_checks':checks,'max_float_difference_from_old_symbol':float(np.max(np.abs(a-old))),'root_sha256':hashlib.sha256(rootfile.read_bytes()).hexdigest(),'matrix_decimal':[[mp.nstr(J[i,j],70) for j in range(96)] for i in range(32)]}
(m.ROOT/'precision-completed-symbol-result.json').write_text(json.dumps(result,indent=2));np.savez_compressed(m.ROOT/'precision-completed-symbol.npz',completed_first_symbol=a)
print({k:v for k,v in result.items() if k!='matrix_decimal'},flush=True)
