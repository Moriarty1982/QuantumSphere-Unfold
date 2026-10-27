# Standalone direct component checks of the first-jet witness.
I=[[int(a==b) for b in range(4)] for a in range(4)]
ax=[[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
ay=[[0,0,0,-1j],[0,0,1j,0],[0,-1j,0,0],[1j,0,0,0]]
az=[[0,0,1,0],[0,0,0,-1],[1,0,0,0],[0,-1,0,0]]
def mv(m,v):return [sum(a*b for a,b in zip(row,v)) for row in m]
K=[I,ax,ay,az]
dB=[[2,0,0,0],[0,0,0,2],[0,0,0,2j],[0,0,2,0]]
E=[[mv(k,d)[0].real/2 for d in dB] for k in K]
assert E==I
kin=[1j*sum(mv(k,d)[a] for k,d in zip(K,dB)) for a in range(4)]
assert kin==[8j,0,0,0]
assert sum(E[a][a] for a in range(4))==8/2
# Frozen continuation at (t,x,y,z)=(0,1,0,0): A equation is violated.
B=[0,0,0,2]
assert [8j*b for b in B]==[0,0,0,16j]
print('PASS: identity coframe, sourced B equation, trace 4; frozen continuation fails A equation as expected.')
