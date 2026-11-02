"""Direct full residual controls of corrected fifth-degree field polynomial."""
from pathlib import Path
import json,mpmath as mp,math
R=Path(__file__).resolve().parent;t=(R/'precision_omega_repair_check.py').read_text().split('checks=[]')[0];t=t.replace("('precision-omega-repair-result.json','fourth_coefficients_real_packed',4)","('precision-fifth-gate-repair-result.json','fourth_coefficients_real_packed',4),('precision-fifth-gate-repair-result.json','fifth_coefficients_real_packed',5)");env={'__file__':str(R/'precision_omega_repair_check.py')};exec(t,env);ns=env['ns'];checks=[]
for d in [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,-2,3,-1]]:
 vals=[]
 for order in range(5):
  value=mp.diff(lambda t:ns['path'](t,d),mp.mpf('0'),order)/math.factorial(order);vals.append(mp.nstr(max(abs(x) for x in value),24))
 checks.append({'direction':d,'normalized_R_orders0_through4_max':vals})
print(checks)
(R/'precision-fifth-gate-direct-check.json').write_text(json.dumps({'contract':'Direct polynomial field paths throughdegree5, analytic completedR evaluated with full background. Five directions and residualorders0..4. Same evaluator; not universal/exact or independent implementation.','checks':checks},indent=2))
