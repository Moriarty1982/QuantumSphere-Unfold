# Counterflow connection: source/coframe compatibility and remaining A/B gate

2026-10-27. Exact local algebra following OP5_Native_Exchange_And_Selector_Feedback.md. All claims conditional on the existing classical comparison fields; no native action derivation.

## Local contract

At a point rotate spatial axes so v=v e_x, spin=e_y, 0<v<1. Choose rest spinors chi_+=(1,i)/sqrt(2), chi_-=(1,-i)/sqrt(2). Write U=(a I+b alpha_x)(chi_+,0), W=(a I-b alpha_x)(chi_-,0), a^2-b^2=1, 2ab=gamma v. Fields are sqrt(n)(c U,d U,W), with c=cos theta, d=sin theta, n gamma=N/2. This is the previous inverse-specified witness theta=asin(8t/N)/2.

Take only one internal connection component A_y=G, with Hermitian real flavor matrix

G=[[0,0,p],[0,0,q],[p,q,0]], A_0=A_x=A_z=0.

Hamiltonian interaction is alpha_y G. The cross selector remains S_AB=S_BA=1/2. Exact four-component matrix multiplication gives

source_C=-4nab(pc+qd)=-N v(pc+qd),
delta E_y^y=-nab(pd+qc),
all other delta E_mu^a=0.

Thus a nonzero selector commutator need not produce a nonzero coframe correction on these fields. This is an explicit example of the weaker expectation-value cancellation identified in the preceding note.

## Simultaneous source and geometry gate

Let L=3/(2tv), Delta=c^2-d^2=cos(2theta). The two requirements are

pc+qd=L, pd+qc=0.

For Delta nonzero they have the unique real solution

p=L c/Delta, q=-L d/Delta.

It supplies source_C=-3N/(2t) and leaves the entire cross coframe correction zero at the point. The original theta branch has Delta>0 inside 0<t<N/8. Coefficients grow without bound as v tends to zero or Delta tends to zero; no extension through these limits is established. In a smooth local spin/boost frame away from these boundaries the same algebra can be imposed pointwise. It does not solve derivatives of the connection or its field equations.

At equal A/B amplitudes Delta=0, the two rows of the gate become dependent and a nonzero L is incompatible. The variable-amplitude freedom is essential here.

## The next necessary condition already fails for this connection alone

The individual prescribed currents are

J_A=(N/2)c^2(1,x/t), J_B=(N/2)d^2(1,x/t).

Their required divergences are

D_A=-Ncd theta_dot+3N c^2/(2t),
D_B=+Ncd theta_dot+3N d^2/(2t).

The fitted connection supplies

Q_A=Nvpc=3N c^2/(2t Delta),
Q_B=Nvqd=-3N d^2/(2t Delta).

They sum to the correct 3N/(2t), but individually disagree. In particular

D_A-Q_A=-Ncd theta_dot - (3N c^2/(2t))(1/Delta-1)<0

throughout 0<theta<pi/4, theta_dot>0. B has the opposite residual. Therefore this minimal connection cannot solve the full probe equations even though it passes both the C-sector source and coframe tests.

A separate A/B Hamiltonian h sigma_y would repair these two density equations if h=theta_dot+3cd/(t Delta), but its implementation matters. If introduced as A_0=h sigma_y, it adds a coframe correction

delta E_0^a=-(h/2)(J_A^a-J_B^a)=-(h N Delta/4)(1,v)^a,

so it cannot simply be appended while retaining E=I. Other operator choices or additional cancellations have not been ruled out. No arbitrary fitted exchange is being promoted to a native law.

## Evidence and scope

SymPy exact Dirac-matrix algebra verified every coframe correction component and the C source, and verified the inverse two-by-two gate. The individual-current residual follows by exact differentiation of the specified currents. Full spinor equations, gauge curvature/action response, gravitational stress and native projected representation remain unverified. OP5 remains open. The result isolates a coupled source/geometry/population constraint rather than proving a general impossibility. Local uncommitted note.
