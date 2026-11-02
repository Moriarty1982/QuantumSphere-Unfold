"""Direct quartic-path control of fourth-jet elimination residual."""
from pathlib import Path
import mpmath as mp,json,itertools
R=Path(__file__).resolve().parent;source=(R/'precision_third_source.py').read_text();injection='''
  for axes,coef in terms:
   alpha=[axes.count(mu) for mu in range(4)];m.psi+=mp.fprod(dx[mu]**alpha[mu] for mu in range(4))*coef
   for mu in range(4):
    if alpha[mu]:js[mu]+=alpha[mu]*mp.fprod(dx[nu]**(alpha[nu]-int(nu==mu)) for nu in range(4))*coef
  vv=mp.matrix'''
source=source.replace(';vv=mp.matrix',injection);ns={'__file__':str(R/'precision_third_source.py'),'__name__':'direct_check'};exec(source,ns);terms=[]
for file,key,degree in [('precision-third-jet-result.json','third_coefficients_real_packed',3),('precision-fourth-elimination-result.json','fourth_coefficients_real_packed',4)]:
 data=json.loads((R/file).read_text());packed=[mp.mpf(x) for x in data[key]]
 for i,a in enumerate(itertools.combinations_with_replacement(range(4),degree)):terms.append((a,mp.matrix([mp.mpc(packed[i*24+k],packed[i*24+k+12]) for k in range(12)])))
ns['terms']=terms;res=json.loads((R/'precision-fourth-elimination-result.json').read_text());res=[mp.mpf(x) for x in res['remaining_residual_real_packed']];triples=list(itertools.combinations_with_replacement(range(4),3));checks=[]
for d in [[1,0,0,0],[1,-2,3,-1]]:
 actual=mp.diff(lambda t:ns['path'](t,d),mp.mpf('0'),3)/6;pred=mp.matrix([sum(res[i*32+k]*mp.fprod(mp.mpf(d[mu])**a.count(mu) for mu in range(4)) for i,a in enumerate(triples)) for k in range(32)]);checks.append({'direction':d,'residual_reconstruction_error_max':mp.nstr(max(abs(v) for v in actual-pred),24),'actual_residual_max':mp.nstr(max(abs(v) for v in actual),24)})
(R/'precision-fourth-direct-check.json').write_text(json.dumps({'contract':'Direct quartic field paths re-evaluate degree3 of full completed R. No prolonged matrix used in direct derivative; same underlying R evaluator.','checks':checks},indent=2));print(checks)
