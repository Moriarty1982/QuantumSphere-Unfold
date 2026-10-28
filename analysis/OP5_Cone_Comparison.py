from pathlib import Path
import math,json,xml.etree.ElementTree as ET
out=Path(__file__).parent
rows=[]
for u in [0,.25,.5,.75,.95]:
 d=math.cos(math.pi*u/2); f=(5+3*d)/8; v=d/f; K=f/d
 rows.append(dict(time_fraction=u,cone_speed_ratio=v,K=K,mu=(d-f)/(d+f),half_log_K=.5*math.log(K)))
assert all(rows[i]['cone_speed_ratio']>rows[i+1]['cone_speed_ratio'] for i in range(4))
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="660" viewBox="0 0 1100 660">','<rect width="1100" height="660" fill="#f8fafc"/>','<style>text{font-family:Segoe UI,Arial;fill:#172438;font-size:15px}.small{font-size:12px}.title{font-size:23px;font-weight:600}</style>']
def text(x,y,s,cl=''):svg.append(f'<text x="{x}" y="{y}" class="{cl}">{s}</text>')
def line(x,y,a,b,col='#cbd5e1',w=1):svg.append(f'<line x1="{x}" y1="{y}" x2="{a}" y2="{b}" stroke="{col}" stroke-width="{w}"/>')
text(35,36,'Zwei lokale Lichtkegel im selben Koordinatensystem','title')
text(35,62,'Zeitachse x=y=z=0 · Referenz: blau · erzeugte Geometrie: orange · c=1')
for i,r in enumerate(rows):
 cx=120+i*215; cy=240; L=72; v=r['cone_speed_ratio']
 line(cx-83,cy,cx+83,cy);line(cx,cy+83,cx,cy-83)
 for sign in [-1,1]:
  line(cx-sign*L,cy+L,cx+sign*L,cy-L,'#2563eb',2)
  line(cx-sign*v*L,cy+L,cx+sign*v*L,cy-L,'#ea580c',3)
 text(cx-65,124,f"t/t* = {r['time_fraction']:.2f}")
 text(cx-69,342,f"Kegelbreite: {v:.3f}")
text(40,385,'Kegelbreite d/f');text(580,385,'Lokale Verzerrung ½ ln(K) — kein Raumzeit-Abstand')
for x0,y0,W,H,kind,maxy in [(55,585,450,170,'v',1),(595,585,450,170,'D',2)]:
 line(x0,y0,x0+W,y0,'#64748b');line(x0,y0,x0,y0-H,'#64748b')
 pts=[]
 for j in range(199):
  u=j/200; d=math.cos(math.pi*u/2); f=(5+3*d)/8
  val=d/f if kind=='v' else .5*math.log(f/d)
  pts.append(f'{x0+W*u:.3f},{y0-H*val/maxy:.3f}')
 svg.append('<polyline points="'+' '.join(pts)+'" fill="none" stroke="#ea580c" stroke-width="3"/>')
 text(x0-15,y0+20,'0');text(x0+W-10,y0+20,'1');text(x0+W/2-25,y0+38,'t / t*')
 text(x0-28,y0-H+5,str(maxy))
text(35,650,'t* = π/32: Coframe wird auf der Achse singulär. Skizzen sind lokale Tangentialkegel, keine Signalbahnen.','small')
svg.append('</svg>')
content='\n'.join(svg);ET.fromstring(content)
(out/'OP5_Cone_Comparison.svg').write_text(content,encoding='utf-8')
(out/'OP5_Cone_Comparison.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(json.dumps(rows,indent=2))
