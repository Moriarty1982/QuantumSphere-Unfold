"""Check symmetric Hessian cancellation independently of G source construction."""
import precision_completed_rebuild as m
import mpmath as mp,json
p=m.psi;j=m.js;cov=[j[mu]+mp.j*m.conn[mu]*p for mu in range(4)];E=mp.matrix([[mp.re((p.conjugate().T*m.Q[a]*cov[mu])[0]) for mu in range(4)] for a in range(4)]);V=E**-1
B=mp.matrix([[m.realvec(cov[mu])[i] for mu in range(4)] for i in range(24)]);P=mp.eye(24)-B*V*m.A
H=[m.realmat(mp.j*k) for k in m.K];J=[sum((V[mu,a]*H[a] for a in range(4)),mp.zeros(24))*P for mu in range(4)];L=[m.A*sum((V[mu,a]*m.Hb[a] for a in range(4)),mp.zeros(24)) for mu in range(4)]
errors=[]
for mu in range(4):
 for nu in range(mu,4):errors.append(m.norm(L[mu]*J[nu]+(L[nu]*J[mu] if mu!=nu else mp.zeros(4,24))))
out={'contract':'All ten symmetric second-jet coefficients in sum K^mu d_mu F cancel at the high precision first-jet seed. Does not certify other higher identities.','digits':70,'max_symmetric_hessian_coefficient':mp.nstr(max(errors),24),'all_ten_errors':[mp.nstr(v,24) for v in errors]}
(m.ROOT/'precision-hessian-cancellation-result.json').write_text(json.dumps(out,indent=2));print(out)
