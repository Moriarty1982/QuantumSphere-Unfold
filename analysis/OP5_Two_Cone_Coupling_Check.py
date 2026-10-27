import sympy as s
import math
w,a,b,e=s.symbols('w a b e',real=True)
M=s.Matrix([[a,e],[e,b]])
assert s.expand((M-w*s.eye(2)).det()-((w-a)*(w-b)-e*e))==0
v=8*math.cos(math.pi/4)/(5+3*math.cos(math.pi/4))
for k in [0,1,10,10000]:
 a=k*k+1; b=v*v*k*k+1; e=.2
 root=math.sqrt((a-b)**2+4*e*e)
 lo=(a+b-root)/2; hi=(a+b+root)/2
 assert lo>0 and hi>0
 if k==10000:
  assert abs(math.sqrt(hi)/k-1)<1e-7
  assert abs(math.sqrt(lo)/k-v)<1e-7
print({'v_readout_in_reference_units':v,'reference_speed_in_readout_units':1/v,'checks':'characteristic polynomial exact; stable sample; large-k convergence sample'})
