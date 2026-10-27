# OP5: exact massive affine branch and the fixed-momentum obstruction

Date: 2026-10-27. Status: conditional analytic construction in the alternative neutral scalar parent; not native OP5 closure. Independent review attempted but unavailable due to an agent usage limit. Exact rational residual checks accompany the derivation.

## Action and conventions

Start from action (12) in HC_Two_Frame_Action_Bridge.md. Keep its fixed reference coframe, fixed n=(-1,0,0,1), Hermitian K=(I,alpha_i), commuting spinor and independent real multiplier density. Add

    - integral d4x (m+gamma h) Psi^dagger beta Psi
    - integral d4x v W(h),  W(h)=C+L h^2, L>0, v=sqrt|det g|.

The mass/Yukawa term uses the reference volume. The potential uses the induced volume. This distinction is essential: this is not conventional metric-coupled Einstein--Dirac theory. Scalar h and its matching penalty are a declared comparison, not an identification with the native operator H_C.

Use compactly supported variations before restricting the fields. With calC^a_mu=partial_mu j^a/2+kappa h j^a n_mu, the equations include

    E=I+calC,
    pi_geom-v W E^(-T)+lambda=0,
    i K^mu partial_mu Psi + V_lambda Psi -(m+gamma h) beta Psi=0,
    V_lambda=[partial_mu lambda_a^mu/2-kappa h lambda_a^mu n_mu]K^a,
    kappa partial_mu[v n_nu F^{mu nu}]-v W'
        -kappa lambda_a^mu n_mu j^a-gamma Psi^dagger beta Psi=0.

The scalar equation here is a density equation. A multiplier density must also be divided by v if the whole equation is divided by v; the old unit-determinant branch concealed this factor.

## Exact common massive branch

Let u=(1,0,0,0), N>0, and take real constant h and

    Psi=sqrt(N) exp(-i omega t+i p z)u,
    j=(N,0,0,0), q=1-kappa N h>0,
    E=I+kappa h j n^T, g=E^T eta E,
    lambda=q W E^(-T), D=kappa h W,
    p=-D, omega=m+gamma h-D.

Then det E=q, v=q. All components of E, g, h and lambda are constant, hence Riemann=0, F=0 and pi_geom=0. The dictionary holds because the real part of the plane-wave derivative bilinear vanishes. All 16 coframe Euler equations hold by the displayed multiplier.

The inverse identity n_mu(E^-1)^mu_a=n_a/q gives lambda_a^mu n_mu=W n_a and V_lambda=D(I-alpha_z). The probe equation reduces exactly to

    [omega+D-m-gamma h]u+[-p-D]alpha_z u=0.

Its adjoint holds as well. The remaining scalar density equation is

    q W'-kappa N W+gamma N=0,
    2Lh-3kappa N Lh^2-kappa N C+gamma N=0.

Thus, for kappa nonzero,

    h=(1 +/- sqrt(Delta))/(3kappa N),
    Delta=1-3kappa^2 N^2 C/L+3kappa gamma N^2/L.

Every root still requires q>0 and any separately imposed sign conditions. For kappa,N,L>0 and gamma>=0, the lower root has h>=0 and q>0 throughout

    gamma/kappa <= C <= gamma/kappa+L/(3kappa^2 N^2).

These are dimensionless model inputs, not measured parameter estimates.

Two exact witnesses, both with kappa=N=L=m=1:

| gamma | C | h | q | W | D | p | omega |
|---|---|---|---|---|---|---|---|
| 0 | 1/4 | 1/6 | 5/6 | 5/18 | 5/108 | -5/108 | 103/108 |
| 1/4 | 1/2 | 1/6 | 5/6 | 19/36 | 19/216 | -19/216 | 103/108 |

The reference current and induced density current are constant and conserved. This is a local infinite plane wave, not a normalized finite wave packet. The metric is flat but its coframe relative to the prescribed reference changes with C. The multiplier balances the potential; an independent vacuum Einstein equation without that reaction would not hold.

## Further step: fixing the probe removes arbitrary accommodation

Eliminate W between the scalar condition and p=-kappa h W:

    W=2Lh q/(kappa N)+gamma/kappa,
    p=-(2L/N)h^2(1-kappa N h)-gamma h,
    C=2Lh/(kappa N)-3Lh^2+gamma/kappa.

Therefore, at fixed N, kappa, L, gamma and fixed momentum p, the allowed h solve a cubic and form a finite set (nonzero cubic coefficient for kappa,L>0). C is then restricted to the corresponding finite set. An open interval of arbitrary C cannot be screened while these probe data remain fixed in this ansatz. Fixing omega adds another constraint; for gamma nonzero, omega=m+gamma h+p already fixes h. This is a boundary-data compatibility condition, not a prediction of the observed cosmological constant.

A stronger local sign check uses the positive lower-root interval 0<=h<=1/(3kappa N):

    dp/dh=-(2L/N)h(2-3kappa N h)-gamma.

It is strictly negative for h>0 and gamma>=0. Thus momentum selects at most one h on that interval. Meanwhile dC/dh=2L/(kappa N)-6Lh is positive below its upper endpoint. The ability to vary C is explicitly purchased by changing the probe momentum. At the root merger the C derivative vanishes; that endpoint is not evidence of dynamical attraction.

For the second witness, change C by deltaC while holding h, N and momentum fixed and recomputing the coframe-required multiplier. Scalar residual changes by -kappa N deltaC; probe residual becomes kappa h deltaC (I-alpha_z)u. The old configuration fails. This is an explicit negative control against universal screening.

Without the penalty (L=0), the scalar condition is C=gamma/kappa. In particular gamma=0 excludes nonzero C on this massive timelike constant-current ansatz. The penalty is doing substantive work.

## Stability and what remains open

At fixed j, the algebraic potential is U(h)=q W(h)+gamma N h, with U''=2L(1-3kappa N h). The lower branch has positive restricted curvature before the merger, and the upper branch has negative restricted curvature. This is not stability of the coupled constrained PDE: kinetic degeneracy, variable currents, geometry and boundary conditions must be included.

The result repairs the earlier massive restoration failure by solving a new common branch instead of freezing the massless background. It does not derive the affine dictionary, native M16/P_C7 representation, charged Gauss sector or operator closure. The reference mass does not supply ordinary induced-metric Dirac stress. No physical value of C, universal vacuum protection, dynamical relaxation or full stability has been established. OP5 remains open.

Reproduce the exact witness, 16-component coframe and four-component probe checks, scalar checks and negative controls with:

    python -B analysis/OP5_Massive_Affine_Branch.py
