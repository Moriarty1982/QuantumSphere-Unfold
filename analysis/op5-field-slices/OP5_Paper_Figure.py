from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
root=Path(__file__).parent;data=json.loads((root/'OP5_Slices_9x9_Check.json').read_text());cols=[('residual','Equation residual'),('inverse_g00','Inverse metric g00'),('normalized_mixed_metric','Mixed metric component'),('area_magnitude','Lorentzian area magnitude')]
c=canvas.Canvas(str(root/'OP5_Slices_9x9_Paper.pdf'),pagesize=(595,860));c.setTitle('OP5: six 9 by 9 slices of a multimode comparison field');c.setFont('Helvetica-Bold',13);c.drawString(26,834,'OP5: six 9 x 9 slices of one approximate field');c.setFont('Helvetica',8);c.drawString(26,817,'Centre (t,x,y,z) = (1, 0.6, 0, 0); axis offsets +/-0.01; saved coefficients, no refitting.')
for j,(key,title) in enumerate(cols):
 allvals=[v for row in data['slices'] for v in row[key]];lo=min(allvals);hi=max(allvals);xx=48+j*135
 c.setFont('Helvetica',7);c.drawString(xx,795,title)
 for n,row in enumerate(data['slices']):
  yy=680-n*112;vals=row[key]
  if j==0:c.setFont('Helvetica-Bold',9);c.drawString(17,yy+38,'-'.join(row['axes']))
  for iy in range(9):
   for ix in range(9):
    val=vals[iy*9+ix];f=(val-lo)/(hi-lo+1e-30);c.setFillColor(Color((35+210*f)/255,(160-90*f)/255,(210-140*f)/255));c.rect(xx+ix*9,yy+iy*9,8.8,8.8,stroke=0,fill=1)
  c.setFillColorRGB(0,0,0);c.setFont('Helvetica',7);c.drawString(xx,yy-11,f'{min(vals):.4g} to {max(vals):.4g}');c.setFont('Helvetica',6.5);c.drawString(xx,yy-21,f"horizontal: {row['axes'][0]}; vertical: {row['axes'][1]}")
 c.setFont('Helvetica',6.5);c.drawString(xx,79,f'Shared colour range: {lo:.4g} to {hi:.4g}')
c.setFont('Helvetica',8);c.drawString(26,49,'Area includes time-space bivector components; spatial cross products alone are insufficient.');c.drawString(26,35,'All sampled coframes are invertible and g00 < 0. Residuals are nonzero; no exact solution is claimed.');c.save()
