# Independent audit: an affine null branch with an arbitrary constant volume term

26 October 2026. Base revision:
`a97e32d25b4b66ec2d534bdbc142df7b51883057`.
Exact analytical audit of the expressly alternative parent action (12)
and local solution (13) in `analysis/HC_Two_Frame_Action_Bridge.md`.
No native promotion, simulation, manuscript change or Git mutation.

## 1. Result

**The proposed extension works for every real constant C on this specific
local branch.** Keep the same coframe, scalar profile and constant spinor,
and replace the original zero multiplier by

    lambda_a^mu=C sqrt(|g|) (E^(-1))^mu_a.

The coframe equation, complete probe/adjoint equations and scalar equation
all remain satisfied under arbitrary compactly supported first variations
of the full declared independent fields. This is not merely substituting
det E=1 before variation.

However, this is branch-local screening by a changed multiplier reaction,
not elimination of C from the full theory or selection of its value.
A pointwise normalized compactly supported spinor perturbation gives a
nonzero C-dependent constrained second variation. Thus the branch does
not establish an off-branch protection law, stability or quantum immunity.

## 2. Exact action and branch being audited

Use precisely the source's independent real nonsingular E, real scalar h,
commuting complex spinor Psi and real multiplier density lambda. The
fixed data theta=I, n_mu=(-1,0,0,1), K^a=(I,alpha_i), kappa and kappa_eff
are not varied. In the source's convention g=E^T eta E, eta=(-+++),

    S_0=S_probe,ref[Psi]
       +integral sqrt(|g|)[R/(2 kappa_eff)-F_mu_nu F^mu_nu/4]
       +integral lambda_a^mu(E^a_mu-theta^a_mu-calC^a_mu),
    F_mu_nu=kappa[(partial_mu h)n_nu-n_mu(partial_nu h)],
    calC^a_mu=Re(Psi†K^a partial_mu Psi)
                 +kappa h n_mu j^a,
    j^a=Psi†K^a Psi.

The different symbol calC distinguishes the coframe dictionary from the
new scalar volume-density parameter C. Fixed Hermitian K^a gives the
exact identity Re(Psi†K^a partial_mu Psi)=partial_mu j^a/2.

Add only

    S_C=S_0-C integral sqrt(|g(E)|),    C real constant.

The unchanged branch fields are

    Psi_0=(1,0,1,0)^T/sqrt(2),    j_0=l=(1,0,0,1),
    E_0=I+kappa h l n^T,
    h=log(F_0+b_x x+b_y y)/(kappa_eff kappa),
    F_0+b_x x+b_y y>0,    kappa!=0,    kappa_eff>0.

The profile depends on transverse coordinates x,y only. It is the
logarithm of a positive affine harmonic function, not itself generally
harmonic. The source establishes that this branch with lambda=0 solves
all equations of S_0. The present calculation independently evaluates
every additional C-dependent first variation without restricting the
allowed variation before deriving its Euler derivative.

## 3. Coframe variation and the required multiplier

On the orientation-preserving neighborhood of E_0,

    delta sqrt(|g|)=sqrt(|g|)(E^(-1))^mu_a delta E^a_mu.

Consequently the added coframe Euler density is

    (pi_C)_a^mu=-C sqrt(|g|)(E^(-1))^mu_a.

The old geometric coframe Euler derivative vanishes at E_0. Since the
multiplier term contributes +lambda_a^mu, the full coframe equation
pi_geom+pi_C+lambda=0 is solved exactly by the stated lambda_C. This
holds for all independent coframe variations, not only variations of
the rank-one branch parameters.

Varying lambda still imposes the complete coframe constraint. It is
unchanged because E_0, Psi_0 and h are unchanged. Lambda is an independent
field when varying the action; its displayed dependence on the branch
E_0 is its solution value, not a prescription to vary lambda with E.

## 4. Branch identities for the multiplier

Because n.l=0, the matrix determinant and inverse identities give

    det E_0=1,    sqrt(|g_0|)=1,
    (E_0^(-1))^mu_a=delta^mu_a-kappa h l^mu n_a,
    lambda_a^mu=C(delta^mu_a-kappa h l^mu n_a).

Here tangent and coordinate components are identified by the fixed
reference coframe theta=I, so n_a has the same array (-1,0,0,1).
The transverse profile satisfies l^mu partial_mu h=0. Hence

    partial_mu lambda_a^mu=0,
    lambda_a^mu n_mu=C n_a,
    lambda_a^mu n_mu j_0^a=C n.l=0.

The spin alignment also gives

    (n_a K^a)Psi_0=(-I+alpha_z)Psi_0=0.

Its Hermitian conjugate vanishes as well. Nullity of the vector current
alone would not automatically prove this spinor kernel identity; the
explicit chosen spinor and K matrices do.

## 5. Probe and adjoint variations are genuinely unrestricted

For arbitrary complex delta Psi at fixed E,h,lambda,

    delta calC^a_mu=partial_mu(delta j^a)/2
                       +kappa h n_mu delta j^a,
    delta j^a=delta Psi†K^a Psi+Psi†K^a delta Psi.

After integration by parts of the compactly supported variation,

    delta(-integral lambda.calC)
       =integral [partial_mu lambda_a^mu/2
                    -kappa h lambda_a^mu n_mu]delta j^a.

Thus the added Hermitian probe matrix is

    V_lambda=[partial_mu lambda_a^mu/2
                   -kappa h lambda_a^mu n_mu]K^a
             =-C kappa h n_a K^a.

It annihilates Psi_0. Its adjoint annihilates the conjugate row, so both
independent probe/adjoint Euler equations remain satisfied. The constant
spinor already solves the original massless reference kinetic equation.
The volume term has no direct Psi variation while E is independent;
its complete reaction is the multiplier contribution just evaluated.

No condition delta Psi in the positive-alpha_z eigenspace was imposed.
The kernel property at the background makes the first Euler derivative
zero for arbitrary complex probe variations, including transverse ones.

## 6. Scalar variation

At fixed independent E the new volume term has no direct h variation.
The multiplier addition contributes

    delta_h S_lambda=-integral kappa lambda_a^mu n_mu j^a delta h.

This is zero at the background by section 4. The original scalar
geometric equation remains the one established by the source and
vanishes on the unchanged transverse null branch. Therefore the entire
h equation, not only its restriction to changes of the logarithmic
profile parameters, remains satisfied.

No additional metric, projector, charge or mass equations are hidden:
the parent action being tested deliberately contains no charged internal
gauge field, mass/Yukawa term or native closure-projector field. Adding
those would be a new restoration test, not an equation already solved.

## 7. Constrained volume first variation: a cross-check

Eliminate the multiplier constraint only after deriving the independent
equations. The composite volume obeys

    delta V_4=integral sqrt(|g|)(E^(-1))^mu_a
       [partial_mu(delta j^a)/2
        +kappa h n_mu delta j^a+kappa n_mu j^a delta h].

At the branch, the derivative term integrates to zero because
partial_mu[sqrt(|g|)(E^(-1))^mu_a]=0. The delta h term vanishes by
n.j=0. The remaining term is kappa integral h n_a delta j^a, which
vanishes for every probe variation because (n.K)Psi_0=0 and its adjoint.
This confirms the full first-variation result. Merely observing V_4 is
constant along the original h-profile family would not have established it.

## 8. Normalized perturbation shows C-dependent fluctuations

Choose w=(1,0,-1,0)^T/sqrt(2). Then w†Psi_0=0, ||w||=1,
(n.K)w=-2w, and all cross current matrix elements
Psi_0†K^a w vanish. Let f(x) be a real smooth compactly supported function
inside the positive logarithmic patch and use the pointwise normalized
path

    Psi_epsilon=cos(epsilon f)Psi_0+sin(epsilon f)w,
    j_epsilon=cos²(epsilon f)l+sin²(epsilon f)l_minus,
    l_minus=(1,0,0,-1).

Keep h fixed and impose the exact coframe constraint on the path,
E_epsilon=I+calC[Psi_epsilon,h]. Norm is one pointwise for every epsilon.
At epsilon=0,

    delta j=0,    delta E=0,
    delta²j=2f²(l_minus-l),    n.(l_minus-l)=-2.

For sufficiently small epsilon the coframe stays nonsingular and in
the same orientation throughout the compact support. Since its first
variation vanishes, the second volume derivative contains only the
trace of delta²E; there is no quadratic first-determinant term. Integration
by parts using the same inverse-coframe divergence identity gives

    d² V_4/d epsilon²|_0
      =kappa integral h n_a delta²j^a
      =-4 kappa integral h f²,
    d²(-C V_4)/d epsilon²|_0
      =+4 C kappa integral h f².

The factor and sign can also be checked by the rank-one determinant
lemma. Put d=l_minus-l and r_epsilon=sin²(epsilon f). Then

    E_epsilon=E_0+d[partial r_epsilon/2+kappa h n r_epsilon]^T,
    E_0^(-1)d=d+2kappa h l.

The derivative contributions to the integrated determinant are boundary
terms because l.partial h=0. The exact compactly supported volume change
is therefore -2kappa integral h sin²(epsilon f) within the orientation
neighborhood, whose second derivative is the expression above.

The multiplier term vanishes identically along this constrained path,
so this is also the additional C-dependent part of the full constrained
action Hessian. Other original action terms contribute their own Hessian.
A nonzero expression shows fluctuation sensitivity to C; it is not by
itself a proof of stable or unstable evolution for this constrained,
degenerate-kinetic parent. Pointwise state normalization does not remove it.

## 9. Boundary and interpretation limits

All integrations by parts assume compactly supported variations inside
a smooth positive-profile patch, or boundary data eliminating the stated
surface terms. A finite patch may be used to define V_4; on an infinite
domain the compactly supported volume difference and its derivatives
are the relevant local quantities. No infinite unregulated total volume
is needed for the variation test.

Changing C changes the solved multiplier by a generally nonzero amount.
The vacuum coframe source is balanced by that constraint reaction. The
unmodified Einstein equation without the multiplier would not hold for
the same metric after adding C; the balance is in the complete parent
coframe equation. The result does not choose C or prove it unobservable
in every process of the theory.

The fixed reference coframe, fixed null axis, fixed-reference probe
kinetic term, massless spin alignment and deliberately reduced field
content are load-bearing. The source's native mass, gauge and matching
restoration tests already fail on the unchanged original branch; the
present C screening does not repair those missing sectors. Global
existence, boundary completion, attractor selection, positive energy
bounds, perturbative stability and quantum/renormalization protection
remain unproved.

## 10. Verification and source fingerprint

Analytically checked: determinant/inverse identities, independent full
coframe variation, multiplier divergence, probe and conjugate kernel
equations, scalar variation, the unrestricted composite first variation
and the normalized compactly supported second variation with its factor
and sign. No restriction to the branch was made before deriving the
independent Euler derivatives.

Source SHA-256:

`analysis/HC_Two_Frame_Action_Bridge.md`

`bd5649a5d5bc219b7f2878085a059b5d5344f5705bedb3ea63c59f874355725d`.

Only this audit note was written. The result is an exact classical
existence family of the specified alternative affine parent, not a
native solution or an all-configuration constant-shift symmetry.
