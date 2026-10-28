# Independent audit: complete linear equations of the constant affine branch

26 October 2026. Repository base:
`a97e32d25b4b66ec2d534bdbc142df7b51883057`.
Repository read only. This note alone is written in the authorized
visualization workspace. Exact analytical calculation, no simulation,
native promotion or claim of stability of the entire four-spinor/gravity system.

## 1. Result

The proposed one-component perturbation is an invariant subspace of
**all** linearized equations of the specified alternative parent when
its coefficient depends only on t,z. With mu=C kappa h_0,

    delta Psi=a(t,z)w,    w=(1,0,-1,0)^T/sqrt(2),
    delta h=delta E=delta lambda=0,

the exact linear equation is

    i(partial_t-partial_z)a+2mu a=0.

For a=A exp[i(kz-omega t)], omega=-k-2mu. All real k,C,kappa,h_0
give real omega. This shift is not an exponentially growing mode or a
tachyonic instability. Generic transverse dependence couples this single
spinor direction to another one; it cannot be ignored by retaining only
the restricted scalar action.

There is in fact a larger two-component current-dark spinor subspace
with all geometric perturbations still zero at linear order. Its complete
dispersion is real for all real momenta. Neither result proves stability
outside this subspace or at nonlinear order. A restored scalar Dirac
mass already destroys the unchanged background solution.

## 2. Exact parent and constant background

Use action (12) of the repository note
`analysis/HC_Two_Frame_Action_Bridge.md`, with only the constant addition
-C integral sqrt(|g(E)|) described in `analysis/OP5_Affine_Vacuum_Response.md`.
Independent fields remain real E,h,lambda and commuting complex Psi.
The fixed reference coframe is theta=I, n=(-1,0,0,1), K^a=(I,alpha_i),
with standard Pauli off-diagonal alpha_i, and g=E^T eta E, eta=(-+++).
The dictionary and scalar two-form are

    j^a=Psi†K^a Psi,
    calC^a_mu=partial_mu j^a/2+kappa h n_mu j^a,
    F_mu_nu=kappa[(partial_mu h)n_nu-n_mu(partial_nu h)].

The positive-orientation constant background is

    Psi_0=(1,0,1,0)^T/sqrt(2),    j_0=l=(1,0,0,1),
    h=h_0 real constant,
    E_0=I+kappa h_0 l n^T,
    lambda_0,a^mu=C(E_0^(-1))^mu_a.

It is the b_x=b_y=0 member of the prior logarithmic family, with
F_0=exp(kappa_eff kappa h_0)>0. Thus det E_0=1, the induced metric is
constant and flat, and F=0. The reference probe kinetic term remains
the one explicitly fixed in that parent; it has not been replaced by
an induced-metric Dirac kinetic term.

## 3. All independent Euler equations before linearization

The multiplier equation is the complete coframe constraint

    E-I-calC[Psi,h]=0.

Writing pi_geom for the coframe Euler density from the Einstein/scalar
two-form terms, the coframe equation is

    pi_geom-C sqrt(|g|) E^(-T)+lambda=0.

The probe equation and adjoint use the Hermitian matrix

    iK^mu partial_mu Psi+V_lambda Psi=0,
    V_lambda=[partial_mu lambda_a^mu/2
                   -kappa h lambda_a^mu n_mu]K^a.

The scalar equation is

    kappa/sqrt(|g|) partial_mu[sqrt(|g|) n_nu F^{mu nu}]
           -kappa lambda_a^mu n_mu j^a=0.

These are derived with E,h,Psi,lambda independent. A restricted ansatz
is substituted only now. On the background,

    partial_mu lambda_0,a^mu=0,
    lambda_0,a^mu n_mu=C n_a,
    V_0=-mu K.n=mu(I-alpha_z),
    alpha_z Psi_0=Psi_0,    V_0 Psi_0=0.

The coframe vacuum contribution is canceled by lambda_0, while the
scalar multiplier contraction is zero since n.l=0. Thus the constant
background is a solution for every real C in this declared parent.

## 4. Complete linear consistency of the proposed channel

The explicit spinor w is orthogonal to Psi_0 and satisfies

    alpha_z w=-w,    K.n w=-2w,
    Psi_0†K^a w=0 for every a=0,1,2,3.

Consequently delta j^a=Psi_0†K^a(delta Psi)
+(delta Psi)†K^a Psi_0=0 for arbitrary complex a. This is an algebraic
zero, so every derivative of delta j also vanishes even for varying a.

Now check each equation, not only the scalar projected probe equation:

- **Multiplier/constraint:** delta calC=partial(delta j)/2
  +kappa h_0 n delta j+kappa n j_0 delta h=0. Hence delta E=0
  satisfies every component of the linearized coframe constraint.
- **Coframe:** pi_geom depends on E,h, not on the reference probe.
  Its variation is zero for delta E=delta h=0. The variation of the
  vacuum coframe density is also zero for delta E=0. Thus delta lambda=0
  satisfies the complete coframe Euler equation.
- **Scalar:** delta F=0 and delta g=0. The remaining linear multiplier
  terms are -kappa(delta lambda).n.j_0-kappa lambda_0.n.delta j=0.
  Hence the complete scalar equation is satisfied.
- **Probe/adjoint:** delta V_lambda=0. The only equation left is
  iK.partial(delta Psi)+V_0(delta Psi)=0 and its Hermitian adjoint.

For a(t,z), alpha_z w=-w then gives

    [i(partial_t-partial_z)a+2mu a]w=0.

There is no omitted first-order source for h,E or lambda in this channel.
At second order j does change, so zero geometric backreaction is not
established beyond linear order.

## 5. Dispersion, transport and what is not an instability

The plane-wave convention a=A exp[i(kz-omega t)] gives

    omega+k+2mu=0.

The general solution is

    a(t,z)=exp(2i mu t) A_0(z+t).

Its magnitude is transported unchanged:

    (partial_t-partial_z)|a|²=0.

Thus there is no exponential growth in this channel for real parameters;
appropriate periodic, decaying or no-incoming-flux longitudinal boundary
conditions also conserve its longitudinal L² norm. The velocity -1 is
relative to the fixed reference kinetic coordinates, not an assertion
that this characteristic is null for the independently induced g_0.

The sign of the earlier second-variation term by itself did not imply
exponential growth in this first-order complex kinetic system. Nor does
a negative real frequency prove instability. Energy boundedness, other
spinor sectors, gravitational constraints and nonlinear dynamics remain
separate questions.

Within this isolated channel the constant frequency offset can be
removed by a time-dependent phase of a. A frequency shift at specified
reference momentum is therefore not by itself a basis-independent
mass gap or a measurement of C. Comparisons with the other fields,
boundary conditions and specified observables are required.

## 6. Transverse dependence and an optional closed two-component extension

Define v=alpha_x w=(0,-1,0,1)^T/sqrt(2). In the declared standard
Pauli representation,

    alpha_y w=i v,    alpha_z v=v,
    alpha_x v=w,    alpha_y v=-i w,
    Psi_0†K^a v=0 for every a.

The residual of the single-direction ansatz with general a(t,x,y,z)
has an additional v component

    i(partial_x+i partial_y)a.

It vanishes only with the additional condition
(partial_x+i partial_y)a=0. Thus generic transverse dependence leaves
the one-component subspace. For a real transverse Fourier wavevector
this condition requires k_x=k_y=0; special local complex analytic
envelopes are a different restricted possibility.

Keeping both w and v gives delta Psi=a w+b v. Both directions are
current-dark at first order, so the same full geometric checks of
section 4 apply for arbitrary spacetime-dependent a,b. In this basis
the alpha matrices restrict to sigma_x,sigma_y,-sigma_z, and the two
equations are

    i(partial_t-partial_z)a+i(partial_x-i partial_y)b+2mu a=0,
    i(partial_t+partial_z)b+i(partial_x+i partial_y)a=0.

For exp[i(k.x-omega t)] their Hermitian Hamiltonian is

    H_dark(k)=-mu I+k_x sigma_x+k_y sigma_y-(k_z+mu)sigma_z,
    omega_+/-=-mu +/- sqrt(k_x²+k_y²+(k_z+mu)²).

This verifies the absence of exponential Fourier growth throughout
this two-component decoupled linear sector, including the degenerate
crossing at k=(0,0,-mu). It is not the complete constrained-system
dispersion. The constant shifts can also be removed in this isolated
linear block by delta Psi=exp[i mu(t-z)]chi, yielding the corresponding
free reference Weyl equation for chi. That field redefinition does not
remove the constant volume term from the full parent action.

## 7. Restoring a scalar Dirac mass fails already at the background

Add a scalar reference Dirac mass through -m barPsi Psi, with
barPsi=Psi†beta and beta=diag(1,1,-1,-1). The K-form Euler equation
becomes

    iK.partial Psi+V_lambda Psi-m beta Psi=0.

Since beta Psi_0=w, the unchanged background now has residual

    -m w,

which is nonzero for m!=0. The vacuum-shaped reaction still annihilates
Psi_0 and cannot cancel this residual for any value of C. Moreover
beta w=Psi_0; the mass mixes the original aligned direction and the
opposite w direction rather than preserving the massless dark channel.

This establishes failure of the unchanged background with the specified
lambda_C after restoring this mass. It does not exclude a different
massive background or additional nonvacuum multiplier components solving
a changed set of equations. A mass-like Yukawa coefficient m+gamma h_0
has the same obstruction when nonzero. A stability calculation about
such a restored theory must first find an actual restored solution;
linearizing about the present non-solution would not be valid.

### 7.1 Standard factorized mass/transverse compatibility check

This separate algebraic test does not assert the complete parent reduces
to the following generator. On a standard positive internal tensor
spinor carrier let Pi_+=(I+alpha_z)/2 and Pi_-=(I-alpha_z)/2. For real
momenta and an internal Hermitian M commuting with spin matrices, set

    B=alpha_x k_x+alpha_y k_y+beta M,
    H_std=alpha.k+beta M-2D Pi_-,    D real scalar.

The standard Clifford anticommutators give

    {B,alpha_z}=0,
    B²=(k_x²+k_y²)I+M².

If Pi_+ psi=psi, all diagonal spin terms drop out of Pi_-H_std psi
and B psi lies in Pi_-. Hence

    ||Pi_-H_std Pi_+ psi||²
      =(k_x²+k_y²)||psi||²+||M psi||².

For nonzero psi this vanishes exactly when k_x=k_y=0 and M psi=0.
An invertible positive mass has no such nonzero state; a Hermitian mass
with a kernel can admit the corresponding longitudinal kernel states.
There is no cancellation between transverse momentum and mass in this
positive norm identity. A diagonal spin penalty -2D Pi_- cannot alter
the off-diagonal conclusion.

An independently factorized closure projector P_C7 tensor I_spin,
acting only internally, permits both f tensor Psi_0 and f tensor w
whenever f is in its selected internal range. Thus internal closure
alone does not discard the spin direction that sees the vacuum-shaped
reaction. A spin-dependent or nonfactorized closure law would be extra
input and is not excluded by this simple factorized check.

## 8. Domain, provenance and checked scope

The calculation is local on the constant-profile branch. A one-component
t,z-dependent perturbation is understood per transverse area or on a
declared transverse box; it is not a localized finite-energy perturbation
on all R³. Plane waves are dispersion probes. Compactly supported
variational derivation of the full equations remains valid, and admissible
evolution/boundary data must be specified separately.

Checked analytically: all four current cross terms, every independent
linearized field equation, the sign of the multiplier potential and
frequency shift, characteristic transport, transverse coupling, the
two-component Hermitian spectrum and the restored mass residual.
No complete nonlinear stability or native physical spectrum is claimed.

Sources read from the read-only repository:

| Repository-relative path | SHA-256 |
|---|---|
| `analysis/HC_Two_Frame_Action_Bridge.md` | `bd5649a5d5bc219b7f2878085a059b5d5344f5705bedb3ea63c59f874355725d` |
| `analysis/OP5_Affine_Vacuum_Response.md` | `57d5592ff6ff78acb5ab592611a0e92a7ab14e89cc2c9fbaf11f9b2ec43c9f75` |

Only the authorized visualization-workspace note was written. Neither
the repository nor its Git state was changed.
