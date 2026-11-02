"""Direct quadratic completed-residual check on repaired cubic field."""
from pathlib import Path
import json,mpmath as mp,itertools,hashlib
R=Path(__file__).resolve().parent;data=json.loads((R/'precision-third-jet-result.json').read_text());packed=[mp.mpf(x) for x in data['third_coefficients_real_packed']]
text=(R/'precision_third_source.py').read_text();injection='''
  for ii,axes in enumerate(triples):
   alpha=[axes.count(mu) for mu in range(4)];coef=T3[ii];mon=mp.fprod(dx[mu]**alpha[mu] for mu in range(4));m.psi+=mon*coef
   for mu in range(4):
    if alpha[mu]:js[mu]+=alpha[mu]*mp.fprod(dx[nu]**(alpha[nu]-int(nu==mu)) for nu in range(4))*coef
  vv=mp.matrix'''
text=text.replace(';vv=mp.matrix',injection);ns={'__file__':str(R/'precision_third_source.py'),'__name__':'direct_check'};exec(text,ns)
# Parse decimal coefficients only after the helper establishes 70-digit context.
packed=[mp.mpf(x) for x in data['third_coefficients_real_packed']];ns['triples']=[tuple(v) for v in data['triples']];ns['T3']=[mp.matrix([mp.mpc(packed[i*24+k],packed[i*24+k+12]) for k in range(12)]) for i in range(20)]
checks=[]
for d in [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,1,1,1],[1,-2,3,-1]]:
 value=mp.diff(lambda t:ns['path'](t,d),mp.mpf('0'),2);checks.append({'direction':d,'full_R_second_directional_derivative_max':mp.nstr(max(abs(v) for v in value),24)})
print(checks)
(R/'precision-third-jet-direct-check.json').write_text(json.dumps({'contract':'Direct second directional derivatives of original completed R along cubic field paths, no prolonged matrix or row selection. Six directions, same analytic evaluator; not independent evaluator or all directional certification.','checks':checks,'third_jet_sha256':hashlib.sha256((R/'precision-third-jet-result.json').read_bytes()).hexdigest()},indent=2))
