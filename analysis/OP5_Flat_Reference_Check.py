from fractions import Fraction as F
import cmath
import math

# Y=(2t,3x,4y,5z): inverse pullback metric and signal f(3x-2t).
ginv=[-F(1,4),F(1,9),F(1,16),F(1,25)]
k=[-2,3,0,0]
assert sum(ginv[i]*k[i]**2 for i in range(4))==0
# This front has dx/dt=2/3 in x coordinates and dY1/dY0=1.
assert F(3)*F(2,3)/2==1
# Nonzero outer product: every two by two minor vanishes.
v=[1,2,3,4]; q=[2,-3,5,7]
E=[[a*b for b in q] for a in v]
assert all(E[a][i]*E[b][j]-E[a][j]*E[b][i]==0
           for a in range(4) for b in range(4) for i in range(4) for j in range(4))
# For any three modes the third phase difference is dependent.
k1=[0,1,2,3]; k2=[1,0,3,2]; k3=[4,2,1,0]
assert all((k3[i]-k2[i])==(k3[i]-k1[i])-(k2[i]-k1[i]) for i in range(4))
def reading(e1,e2,t):
    a=cmath.exp(-1j*e1*t)/math.sqrt(2)
    b=cmath.exp(-1j*e2*t)/math.sqrt(2)
    return (a.conjugate()*b+b.conjugate()*a).real
for t in [0,.2,.7,2.0]:
    assert abs(reading(2,5,t)-math.cos(3*t))<1e-12
    assert abs(reading(2,5,t)-reading(9,12,t))<1e-12
assert math.isclose(math.sqrt(1-.6**2),.8)
print('PASS: exact pullback null cone, coordinate speed, rank-one minors, three-mode phase dependence; numerical clock and common-offset checks.')
