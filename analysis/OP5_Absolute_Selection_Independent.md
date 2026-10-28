# Independent audit: three possible rules for the absolute vacuum contribution

26 October 2026. Base revision:
`a97e32d25b4b66ec2d534bdbc142df7b51883057`.
Bounded analytic audit; no numerical experiment, native adoption or
manuscript change. Metric convention (-+++), and
T_mu_nu=-2/sqrt(-g) delta I_m/delta g^{mu nu}.

## 1. Result and exact scope

Three proposed selection mechanisms have different logical status:

1. Fixed-metric matter/closure stationarity cannot distinguish an added
   constant volume density. This is a limited blindness result, not a
   no-go theorem for every complete matter-gravity construction.
2. A pure scale-compensator quartic can force zero potential at a nonzero
   stationary scale, but that stationary solution requires a simultaneous
   double-zero condition and leaves the scale flat. Allowed quartic
   deformations can destroy that branch; scale stabilization by a log term
   does not generally leave zero vacuum height.
3. Normalizing an entire finite-volume action by its spacetime volume
   really changes the metric variational law and makes it invariant under
   constant matter-density shifts. It is an explicitly nonnative global
   modification, not an implication of state or closure normalization.

The existing `OP5_Native_Pair_Potential_Audit.md` already distinguishes
the zero of an explicitly defined closure penalty from an independent
gravitating constant. `HC_Induced_Gravity_Heat_Kernel.md` likewise records
an induced Einstein coefficient together with a regulator-dependent vacuum
term, and additional field-content assumptions for the tested cancellation.
Neither source currently derives one of the stronger selection laws below
from native M16/P_C7 data.

## 2. Fixed-metric constant-shift test

Let the ordinary matter action be

    I_m[g,Phi]=integral_Omega sqrt(-g) L_m(g,Phi).

Let C be a real constant independent of all varied matter, closure,
comparison and projector data. Replacing L_m by L_m-C yields

    I_m' = I_m-C V_4[g],
    V_4[g]=integral_Omega sqrt(-g).

At fixed metric and fixed domain, for every admissible nonmetric variation
whose constraint set itself does not depend on C,

    delta_Phi I_m'=delta_Phi I_m.

All higher fixed-metric matter variations agree as well. Thus the
stationarity equations, constrained Hessian and local nonmetric stability
tests at the same background are unchanged. This includes a fixed-metric
closure extremization if the constant is independent of its fields.

Metric variation is different:

    T_mu_nu'=T_mu_nu-C g_mu_nu.

With an ordinary Einstein term A R and constant A!=0, this is an actual
change of gravitational source, or a curvature-coefficient change
Delta Lambda=C/(2A) after moving the constant to the geometric side.
The two complete matter-gravity solutions therefore need not have the
same metric or even the same matter solution on their changed metrics.

Limits of the claim matter. If g=g[Phi] is induced and varied with Phi,
then delta_Phi V_4 need not vanish. If C is a field, depends on the
projector, or appears inside a global constraint, it is not the constant
shift tested here. An exact extra symmetry, a fixed volume prescription,
a global constraint or a different metric equation could remove this
blindness. Those require their own derivation.

Also, a constant matter Lagrangian density is not the same operation as
adding C times a field bilinear or changing a Dirac mass matrix by C I.
Such terms depend on varied fields and can change their equations. The
present statement concerns an independent volume density only.

## 3. Scale-compensator quartic: what it actually forces

Take an ordinary real potential

    V(chi,theta)=chi^4 F(theta),    chi>0,

where chi is a scale amplitude, theta dimensionless, and F twice
differentiable. For multiple angular variables replace F' by its gradient.
The fixed-background stationarity equations are

    partial_chi V=4 chi^3 F=0,
    partial_theta V=chi^4 F'=0.

At any nonzero-scale stationary solution they require

    F(theta_*)=0,    F'(theta_*)=0,
    V(chi,theta_*)=0 for every chi>0.

This is a real conditional zero-height identity. It neither proves the
existence of theta_* satisfying both conditions nor selects chi. Its
Hessian at that branch has

    V_chi chi=0,    V_chi theta=0,
    V_theta theta=chi^4 F''(theta_*).

Even F''>0 gives a flat scale direction rather than an isolated fully
stable scale minimum. Kinetic positivity and the other field equations
would additionally be required for a physical stability statement.

An explicit quartic deformation preserves this homogeneity:

    F(theta)->F(theta)+epsilon,
    V->V+epsilon chi^4.

At the original stationary theta_*, the radial derivative becomes
4 epsilon chi^3. For epsilon!=0 the old nonzero-scale branch disappears.
A new branch would require a stationary angular point with F=-epsilon;
that is an extra condition, not guaranteed by the scaling form. Thus
classical homogeneity alone does not protect the simultaneous zero.

If an independent C is permitted in the full theory, V+C has the same
stationary coordinates and Hessian but height C on the zero branch.
An exact full scale symmetry might forbid such a dimensionful independent
term, but that symmetry must include gravity, scales, quantum measure and
counterterms; it is not established by displaying this classical potential.
Even forbidding C would not remove the symmetry-allowed epsilon chi^4
deformation or determine the flat chi modulus.

## 4. Logarithmic scale stabilization does not preserve zero height

For an explicit alternative let

    V=C+chi^4[F(theta)+B log(chi/mu)],
    chi>0,    mu>0,    B constant and independent of theta.

At a nonzero stationary point,

    F'(theta_*)=0,
    4[F(theta_*)+B log(chi_*/mu)]+B=0.

For B!=0 this fixes

    chi_*=mu exp[-F(theta_*)/B-1/4],
    V_*=C-B chi_*^4/4,
    V_chi chi|_*=4B chi_*²,
    V_chi theta|_*=0,    V_theta theta|_*=chi_*^4 F''(theta_*).

For B>0 and F''>0 the potential Hessian is positive in these two
coordinates, but the stationary height is generically nonzero. Choosing
C=B chi_*^4/4 cancels it only by a further matching choice unless a
separate equation enforces that relation. B<0 gives radial instability
in this elementary potential; B=0 returns the quartic conditions.
No native log coefficient, loop calculation or protection law is inferred.

## 5. A different metric law: finite-volume normalized action

Now define an expressly nonnative variational theory on a fixed domain
Omega with finite positive spacetime volume:

    I=integral_Omega sqrt(-g)[A R+L_m],
    V_4=integral_Omega sqrt(-g)>0,
    S_norm=I/V_4,    sigma=I/V_4,

where A is constant and nonzero. Use compactly supported interior metric
variations, so the Einstein-Hilbert boundary variation contributes no
surface term. The entire action/domain/boundary prescription still
matters for the value of I and sigma.

The exact variation is

    delta S_norm=(delta I-sigma delta V_4)/V_4,
    delta V_4=-1/2 integral sqrt(-g)g_mu_nu delta g^{mu nu},
    delta I=integral sqrt(-g)[A G_mu_nu-T_mu_nu/2]delta g^{mu nu}.

Therefore the local metric equation is

    2A G_mu_nu=T_mu_nu-sigma g_mu_nu,
    sigma=<A R+L_m>_Omega,

with sigma a single global value determined by the same solution. It
must not be treated as an arbitrary independent tunable constant. The
matter equations are the ordinary fixed-metric equations multiplied by
1/V_4, provided the denominator does not depend on the matter fields.

Under L_m->L_m-C,

    I->I-C V_4,    S_norm->S_norm-C,
    sigma->sigma-C,    T_mu_nu->T_mu_nu-C g_mu_nu.

Both the complete functional derivatives and T_mu_nu-sigma g_mu_nu are
unchanged. This is genuine constant-shift blindness of the changed
gravitational law, not merely of fixed-metric matter stationarity. It
removes the gravitational response to a uniform density shift by the
new action prescription; it does not calculate the numerical value of C.

## 6. Pure constant branch and global consistency

For pure L_m=-C with no other matter, T_mu_nu=-C g_mu_nu and

    2A G_mu_nu=-(C+sigma)g_mu_nu,
    sigma=A<R>_Omega-C.

The local equation forces R=2(C+sigma)/A, a constant. Inserting that
constant into sigma yields R=2R and hence

    R=0,    sigma=-C,    G_mu_nu=0.

Thus the allowed pure constant branch is Ricci-flat, within the stated
finite-volume variational contract. The constant C may be arbitrary
while its net curvature source vanishes. This is a nontrivial global
consistency result of the modified law, not a native derivation of zero
cosmological constant. It asserts neither existence for arbitrary domain
and boundary data nor uniqueness of the Ricci-flat geometry.

For general matter, let T_tr=g^{mu nu}T_mu_nu. Taking the trace and
averaging gives a useful check:

    -2A<R>=<T_tr>-4sigma,
    sigma=A<R>+<L_m>,
    2A<R>=<T_tr>-4<L_m>,
    sigma=<T_tr>/2-<L_m>.

These are identities on solutions of the normalized theory, not
additional local constraints that can be imposed independently of it.
They reproduce sigma=-C on the pure constant branch and transform
consistently under the constant shift.

## 7. Global and physical caveats of the normalized theory

- On a noncompact or infinite-lifetime spacetime, I and V_4 can both
  diverge. The ratio is then not defined without a limiting/regulator
  prescription; dependence on that prescription must be checked.
- The global domain and boundary data enter sigma. Boundary contributions
  that are locally inert under compact-support variations can still
  affect the global numerator value and hence the ratio prescription.
- Initial-value well-posedness, causality, quantum definition and stability
  of this modified nonlocal/global theory are not established by the
  above classical variation.
- Multiplying or dividing a state probability by its norm is not this
  metric variation. Native state normalization, Markov normalization or
  division by a finite internal trace does not imply S_norm=I/V_4.
- A variable A, an induced metric, a matter-dependent denominator or
  additional constraint fields changes the derivation and must be
  evaluated as its own action.

## 8. Selection law versus matching choice

The fixed-metric rule supplies no absolute selection. The pure quartic
supplies zero height only conditional on an existing nonzero stationary
scale branch, while leaving that scale flat and vulnerable to allowed
quartic deformations. A logarithm can select a stable scale but does not
automatically select zero height. Choosing C afterward is matching/tuning
unless an independent law fixes it.

The normalized action is an actual additional variational law and has
the stated shift-invariant metric response. It would have to be adopted
or derived, with its global meaning specified. Neither the native closure
penalty nor the examined induced-gravity comparison currently establishes
it. These calculations therefore identify what stronger input would do,
not which input the native theory already possesses.

## 9. Verification and input fingerprints

Analytically checked: all fixed-metric versus metric variations, quartic
stationarity and Hessian, logarithmic stationary height and derivatives,
quotient-action variation including its volume sign, the full constant
shift, pure-constant self-consistency and trace-average identities.
No numerical example is used as proof.

| Repository-relative input | SHA-256 |
|---|---|
| `analysis/OP5_Native_Pair_Potential_Audit.md` | `6d3598b9445ce4cd0aac3c2ff947d69fe08bca16d96afb91cb39517e5299a450` |
| `analysis/HC_Induced_Gravity_Heat_Kernel.md` | `3910a1fee31ad4b27fac0445fdc2bb53ed5ff6c8442d52556c76651426c1a340` |

Only this audit note was written. No proposal above is promoted to a
native mechanism, and OP5 is not declared closed.
