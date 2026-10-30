"""Direct directional derivative check of repaired second jet."""
from pathlib import Path
import json,mpmath as mp,hashlib
R=Path(__file__).resolve().parent;ns={'__file__':str(R/'precision_second_jet.py')};exec((R/'precision_second_jet.py').read_text().split('b=mp.matrix')[0],ns)
m=ns['m'];v=ns['v'].copy();r=json.loads((R/'precision-second-jet-result.json').read_text());pairs=[tuple(p) for p in r['pairs']];c=[mp.mpf(x) for x in r['second_coefficients_real_packed']];checks=[]
for mu in range(4):
 H=mp.matrix([ (2 if mu==nu else 1)*c[pairs.index(tuple(sorted((mu,nu))))*24+k] for nu in range(4) for k in range(24)])
 def path(t):
  try:ns['v']=v+t*H;return ns['coordinate'](t,mu)
  finally:ns['v']=v
 d=mp.diff(path,mp.mpf('0'));checks.append({'direction':mu,'full_R_derivative_max':mp.nstr(m.norm(d),24)})
print(checks)
(R/'precision-second-jet-direct-check.json').write_text(json.dumps({'contract':'Direct differentiation along four coordinate jet paths, without assembling the prolonged symbol or applying row selection. Same analytic R evaluator; not a wholly independent evaluator.','checks':checks,'second_jet_sha256':hashlib.sha256((R/'precision-second-jet-result.json').read_bytes()).hexdigest()},indent=2))
