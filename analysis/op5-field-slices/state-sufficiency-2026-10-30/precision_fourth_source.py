"""Cubic completed source using Wolfram-verified exact interpolation weights."""
from pathlib import Path
import json,mpmath as mp,sympy as s,hashlib,time
R=Path(__file__).resolve().parent;tic=time.time();setup={'__file__':str(R/'precision_third_jet_check.py')};exec((R/'precision_third_jet_check.py').read_text().split('checks=[]')[0],setup);ns=setup['ns'];mp.mp.dps=70
wf=json.loads((R/'wolfram-cubic-interpolation.json').read_text());dirs=wf['directions'];triples=[[i-1 for i in t] for t in wf['triples']];exponents=[[a.count(mu) for mu in range(4)] for a in triples]
M=s.Matrix([[s.prod(s.Integer(d[mu])**a[mu] for mu in range(4)) for a in exponents] for d in dirs]);W=s.Matrix([[s.Rational(str(v)) for v in row] for row in wf['inverse']]);assert M.det()==wf['determinant']==-64;assert W*M==s.eye(20)
values=[]
for i,d in enumerate(dirs):
 values.append(mp.diff(lambda t:ns['path'](t,d),mp.mpf('0'),3)/6)
coeff=mp.matrix([[sum(mp.mpf(str(W[i,j]))*values[j][k] for j in range(20)) for k in range(32)] for i in range(20)])
checks=[]
for d in [[1,-2,3,-1],[2,1,-1,3]]:
 actual=mp.diff(lambda t:ns['path'](t,d),mp.mpf('0'),3)/6;pred=mp.matrix([sum(coeff[i,k]*mp.fprod(mp.mpf(d[mu])**exponents[i][mu] for mu in range(4)) for i in range(20)) for k in range(32)]);checks.append({'direction':d,'max_reconstruction_error':mp.nstr(max(abs(v) for v in actual-pred),24)})
out={'contract':'Degree3 normalized completed R source at common repaired third field jet, fourth field jet zero. Uses exact Wolfram-verified interpolation, locally checked by rational SymPy matrix identity and two extra directions. No fourth-jet elimination, Omega value or all-order proof yet.','digits':70,'triples':triples,'source_real_packed':[mp.nstr(coeff[i,k],70) for i in range(20) for k in range(32)],'source_max':mp.nstr(max(abs(v) for v in coeff),24),'checks':checks,'seconds':time.time()-tic,'input_sha256':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ['wolfram-cubic-interpolation.json','precision-third-jet-result.json','precision-second-jet-result.json','precision-completed-root-result.json']}}
(R/'precision-fourth-source-result.json').write_text(json.dumps(out,indent=2));print({k:v for k,v in out.items() if k!='source_real_packed'},flush=True)
