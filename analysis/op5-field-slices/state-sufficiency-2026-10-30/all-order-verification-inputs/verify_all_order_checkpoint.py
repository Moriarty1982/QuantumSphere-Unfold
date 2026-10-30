"""Verify stored finite assertions; not proof/region certification. python verify_all_order_checkpoint.py."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time,platform,sys,numpy as np
ROOT=Path(__file__).resolve().parent
names=['sixth-frozen-third-result.json','sixth-series-review-result.json','fifth-window-result.json','scalar_parametrization_order7_result.json','scalar_chart_fit_order4_point0.json','scalar_chart_fit_order5_point0.json','all-order-source-constraints-result.json','all_order_criteria_symbol-result.json','completed-tableau-result.json','completed-symbol-tower-result.json','completion-identity-result.json','completed_review_full_gate_result.json','completed_review_full_nearby_result.json','completion-omega-probe-result.json','omega-augmented-symbol-result.json','omega-spencer-result.json','all_order_criteria_completion_review-result.json']
paths=[ROOT/n for n in names]+[Path(__file__).resolve()]
hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
started=datetime.now(timezone.utc).isoformat();tic=time.perf_counter();data={n:json.loads((ROOT/n).read_text()) for n in names};checks=[]
six=data[names[0]];old=data['fifth-window-result.json']
assert len(six['results'])==3
for r,seed in zip(six['results'],old['results']):
 assert r['top_rank']==1168 and r['repair_rank']==1439
 assert max(r['full_raw_residual_blocks'].values())<5e-9
 lookup={tuple(a):v for a,v in zip(r['multiindices'],r['coefficients_real_imag'])}
 assert all(lookup[tuple(a)]==v for a,v in zip(seed['multiindices'],seed['coefficients_real_imag']) if sum(a)<=3)
checks.append('sixth finite jets: all3 retain complete thirdjet and raw residual blocks below5e-9')
for r in data['sixth-series-review-result.json']['results']:
 assert max(max(q['F_coefficient_difference_by_degree']) for q in r['direction_checks'])<1e-10
checks.append('sixth independent directional coefficient discrepancy below1e-10')
for r in data['scalar_parametrization_order7_result.json']['results']:
 assert float(r['q_minus_target_max_coefficient'])<1e-60
 assert float(r['sqrt_square_error_max_coefficient'])<1e-60
 assert float(r['chart_guards']['radicand_central'])>0
checks.append('scalar formal chart throughorder7 at70digits satisfies recorded exact algebra truncation and positive centralguard')
for n in ['scalar_chart_fit_order4_point0.json','scalar_chart_fit_order5_point0.json']:
 r=data[n];assert max(b['actual_derivative_norm'] for b in r['full_F_blocks'].values())<1e-8
 assert max(b['actual_derivative_norm'] for b in r['scalar_g_blocks'].values())<1e-9
checks.append('integrated scalar chart p4/p5point0 simultaneously passes recorded F/g tolerances')
assert data['all_order_criteria_symbol-result.json']['Clifford_coefficients_exact'] is True
for r in data['all-order-source-constraints-result.json']['results']:
 assert r['identity_rank']==8 and r['left_projector_difference']<1e-10
checks.append('original eight source identities span recorded complete first leftspace')
for r in data['completion-identity-result.json']['results']:
 assert r['identity_rank']==15 and r['projector_difference']<1e-10 and r['source_identity_norm']<1e-10
checks.append('completed15 source identities span first completedleftspace and annihilate source atall3germs')
for r in data['completed-tableau-result.json']['results']:
 assert [r['g1_dimension'],r['g2_dimension'],r['g3_dimension']]==[65,127,209]
tower=data['completed-symbol-tower-result.json']['results'];assert [r['dimension'] for r in tower]==[65,127,209,312,437,585]
checks.append('completed numerical symbol tower through6 retained, genericflag equality fromthird symbol only')
gate=data['completed_review_full_gate_result.json'];assert gate['full_tangent_dimension']==92 and gate['gate_norm']<1e-10
checks.append('full92direction tangent projection gate recorded below1e-10')
omega=data['completion-omega-probe-result.json'];assert omega['gate_singular_values'][0]>.1 and omega['gate_singular_values'][1]<1e-8
for r in omega['perturbation_controls']:
 assert r['lower_completed_change']<1e-9 and r['best_completed_fourth_residual']>1e-4
 assert r['corrected_best_fourth_residual']<1e-7
checks.append('nontrivialOmega rank1 signal and lower-preserving incompatible perturbations retained with successful scalar repair')
assert [r['dimension'] for r in data['omega-augmented-symbol-result.json']['results']]==[208,308,427,565]
sp=data['omega-spencer-result.json']['results'];assert all(t['H2_dimension']==0 for r in sp[:2] for t in r['tests'])
assert min(t['H2_dimension'] for t in sp[-1]['tests'])<0
checks.append('augmentedsymbol finite dimensions retained; higherSpencer numerical rank explicitly inconclusive, no acyclicity/no-go certified')
assert all(hashlib.sha256(p.read_bytes()).hexdigest()==hashes[str(p)] for p in paths)
result={'contract':'Static and numerical verification of retained artifacts only; no fit rerun, no exact nonlinear root/rank/existence certification. Original run hashes preserved where available; this record timestamps checkpoint verification rather than missing originalrunstart metadata.','started_at':started,'seconds':time.perf_counter()-tic,'software':{'python':platform.python_version(),'numpy':np.__version__},'inputs_sha256':hashes,'inputs_unchanged':True,'checks':checks,'outcome':'recorded finite checks passed; full all-order nonlinear existence remains open'}
(ROOT/'all-order-checkpoint-verification.json').write_text(json.dumps(result,indent=2));print(json.dumps(result['checks'],indent=2))
