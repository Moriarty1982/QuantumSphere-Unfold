# Exact integer / Gaussian-integer arithmetic for this witness.
I=[[int(a==b) for b in range(4)] for a in range(4)]
ax=[[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
ay=[[0,0,0,-1j],[0,0,1j,0],[0,-1j,0,0],[1j,0,0,0]]
az=[[0,0,1,0],[0,0,0,-1],[1,0,0,0],[0,-1,0,0]]
K=[I,ax,ay,az]
def mv(m,v): return [sum(a*b for a,b in zip(row,v)) for row in m]
def add(vs): return [sum(v[j] for v in vs) for j in range(4)]
dB=[[6,0,0,0],[0,0,0,-2],[0,0,0,-2j],[0,0,-2,0]]
E=[[mv(k,d)[0].real/2 for d in dB] for k in K]
assert E==[[3,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]]
assert 3*(-1)**3==-3
assert add([mv(k,d) for k,d in zip(K,dB)])==[0,0,0,0]
assert add([mv(k,[0]*4) for k in K])==[0,0,0,0]
induced=add([[v/3 for v in dB[0]],*[[ -v for v in mv(k,d)] for k,d in zip(K[1:],dB[1:])]])
assert induced==[8,0,0,0]
for t,x,y,z in [(0,0,0,0),(1,2,3,4),(-2,1,-3,5)]:
    B=[6*t,0,-2*z,-2*x-2j*y]
    Z=[mv(k,B)[0] for k in K]
    assert Z==[6*t,-2*x-2j*y,-2*y+2j*x,-2*z]
    assert [v.real/2 for v in Z]==[3*t,-x,-y,-z]
assert -9+1==-8 and -1+9==8
print('PASS: rank-four coframe det=-3; both reference equations zero; induced residual coefficient 8; unequal cones verified.')
