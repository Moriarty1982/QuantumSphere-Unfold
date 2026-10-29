from pathlib import Path
import json,itertools,numpy as np,torch as T,html
# Load definitions only, then restore saved coefficients: no retraining.
ns={};exec(Path('OP5_Multimode_Causal_Field_Check.py').read_text().split('train=T.tensor')[0],ns)
saved=json.loads(Path('OP5_Multimode_Causal_Field_Check.json').read_text());ns['params'].data.copy_(T.tensor(saved['coefficients_real_imag']));compute=ns['compute'];center=np.array(saved['center']);radius=saved['radius'];axes=['t','x','y','z'];eta=np.diag([-1,1,1,1]);steps=np.linspace(-radius,radius,9);slices=[]
for i,j in itertools.combinations(range(4),2):
 pos=np.tile(center,(81,1));pos[:,i]+=np.tile(steps,9);pos[:,j]+=np.repeat(steps,9)
 with T.no_grad():r,E,q,psi=compute(T.tensor(pos))
 E=E.numpy();g=np.einsum('nai,ab,nbj->nij',E,eta,E);ginv=np.linalg.inv(g);res=np.linalg.norm(r.numpy(),axis=1);area2=g[:,i,i]*g[:,j,j]-g[:,i,j]**2
 # All six components of the full frame bivector, including time-space parts.
 biv=np.array([[ee[a,i]*ee[b,j]-ee[b,i]*ee[a,j] for a,b in itertools.combinations(range(4),2)] for ee in E]); signed=-np.sum(biv[:,:3]**2,axis=1)+np.sum(biv[:,3:]**2,axis=1)
 assert np.max(abs(signed-area2))<1e-8
 cross=np.cross(E[:,1:,i],E[:,1:,j]);crossnorm=np.linalg.norm(cross,axis=1)
 if i>0:assert np.max(abs(np.sum(cross**2,axis=1)-np.sum(biv[:,3:]**2,axis=1)))<1e-8
 mixed=g[:,i,j]/np.sqrt(abs(g[:,i,i]*g[:,j,j]))
 slices.append({'axes':[axes[i],axes[j]],'coordinates':pos.tolist(),'residual':res.tolist(),'inverse_g00':ginv[:,0,0].tolist(),'normalized_mixed_metric':mixed.tolist(),'signed_area_squared':area2.tolist(),'area_magnitude':np.sqrt(abs(area2)).tolist(),'full_bivector_components':biv.tolist(),'spatial_projection_cross_products':cross.tolist(),'spatial_cross_norm':crossnorm.tolist(),'min_abs_detE':float(np.min(abs(np.linalg.det(E))))})
summary=[{'axes':r['axes'],'max_residual':max(r['residual']),'max_g00':max(r['inverse_g00']),'min_abs_detE':r['min_abs_detE'],'min_area':min(r['area_magnitude'])} for r in slices]
Path(__file__).with_suffix('.json').write_text(json.dumps({'contract':'Six 9x9 slices of saved field, no retraining. Physical-frame bivectors include all time-space components. Spatial cross products are projections, not a replacement for Lorentzian area.','center':center.tolist(),'radius':radius,'summaries':summary,'slices':slices},indent=2))
columns=[('residual','Gleichungsrest'),('inverse_g00','g^00 (negativ: raumartige t-Schnitte)'),('normalized_mixed_metric','Gemischter Metrikanteil'),('area_magnitude','Lorentz-Flächenbetrag')]
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1220" height="1580" viewBox="0 0 1220 1580"><rect width="1220" height="1580" fill="#101826"/><g font-family="Arial" fill="#e6edf3">','<text x="35" y="32" font-size="23">OP5 · sechs Raumzeitschnitte, jeweils 9 × 9 Punkte</text>','<text x="35" y="58" font-size="14">Gespeichertes Näherungsfeld · Zentrum (1; 0,6; 0; 0) · Achsenabweichung ±0,01 · keine erneute Anpassung</text>']
for col,(key,label) in enumerate(columns):
 vals=np.concatenate([r[key] for r in slices]);lo=float(vals.min());hi=float(vals.max())
 svg.append(f'<text x="{85+col*280}" y="90" font-size="13">{html.escape(label)}</text>')
 for row,data in enumerate(slices):
  xx=85+col*280;yy=120+row*231;values=np.array(data[key]).reshape(9,9)
  if col==0:svg.append(f'<text x="16" y="{yy+90}" font-size="17">{data["axes"][0]}–{data["axes"][1]}</text>')
  for v in range(9):
   for u in range(9):
    f=(values[v,u]-lo)/(hi-lo+1e-30);red=int(35+210*f);green=int(160-90*f);blue=int(210-140*f)
    svg.append(f'<rect x="{xx+u*20}" y="{yy+(8-v)*20}" width="19" height="19" fill="rgb({red},{green},{blue})"><title>{values[v,u]:.8g}</title></rect>')
  svg.append(f'<text x="{xx}" y="{yy+199}" font-size="12">{values.min():.4g} … {values.max():.4g}</text>')
  svg.append(f'<text x="{xx}" y="{yy+216}" font-size="11">horizontal {data["axes"][0]}, vertikal {data["axes"][1]}</text>')
 svg.append(f'<text x="{85+col*280}" y="1534" font-size="12">Gemeinsame Farbskala: {lo:.4g} … {hi:.4g}</text>')
svg.append('<text x="35" y="1564" font-size="13">Flächenbetrag aus vollständigem Bivektor; räumliche Kreuzprodukte und alle Komponenten stehen in der JSON-Datei.</text></g></svg>')
content=''.join(svg);Path('OP5_Slices_9x9.svg').write_text(content);Path('OP5_Slices_9x9.html').write_text('<!doctype html><meta charset="utf-8"><title>OP5 Schnitte</title>'+content)
print(json.dumps(summary,indent=2))
