# A massive charged continuation: independent versus dependent HC

Date: 2026-10-17. Status: conditional local massive Dirac--gauge--HC constructions on the prescribed product geometry. A reference soft branch has explicit local existence bounds. A hard-dependent comparison is kept separate. No native mass spectrum, C7 realization, physical action choice, global finite-energy solution, stability or gravitational backreaction is derived. Main TeX/PDF unchanged.

The [charged massless branch](HC_Sourced_Closure_Current.md) failed when a mass was restored without changing its fields. Here the probe profile, electrostatic potential and HC response are solved together. The essential distinction is whether HC is independently varied or eliminated through `H_C=Lambda` before variation. One must not silently impose both sets of equations without their constraint reaction.

## 1. Same carrier, but two longitudinal amplitudes

Retain the comparison U(2) carrier, unit-flux projector `P` and local Hopf frame `V_N`, constant `n=-dt+dz`, ordinary spin adjoint and prescribed metric `-dt^2+R^2 dOmega^2+dz^2`. Internal gauge curvature and external Levi-Civita spin curvature remain distinct.

Choose a **stationary, zero-longitudinal-current** ansatz

\[
 \Psi=V_N e^{-i\omega t-i\phi/2}(0,u(z),0,i v(z)),\qquad
 B^u=[P,dP]+i a(z)P\,dt,\qquad H_C=h(z)P,
\]

with real u,v,a,h. The full mixed connection is `B=B^u+(kappa H_C+eta Q)n`. Let the real probe resonance in this comparison be `m I+gamma H_C`, with a **given** bare mass `m>0`. The actual Millennium/triadic resonance and its physical units have not been identified with these parameters. The angular cancellation and spin connection are those checked in the massless note; both longitudinal amplitudes stay in the same angular spin polarization.

The currents computed from this same probe are

\[
 j^t=\rho P,\quad j^z=j^\theta=j^\phi=0,\qquad
 S=\sigma P,\qquad \rho=u^2+v^2,\quad\sigma=u^2-v^2.
\]

Thus the current is timelike and the scalar source is generally nonzero. It cannot be discarded just because it vanished in the previous chiral branch. `DP=0` still holds for the constructed connection.

## 2. Derive one common real comparison before substituting the ansatz

Use the real symmetric probe action and dagger bosonic curvature pairing from the earlier comparison, with coefficient `1/g^2`. Take HC to be **independent** for the soft branch, with the already printed finite matching penalty `lambda Tr[(H_C-Lambda)^2]`. Choose fixed scalar M, so the minimal target is `Lambda=0`. Keep the real Yukawa coupling `-gamma Tr(H_C S)`.

The unitary gauge equation has source `i g^2 j`. The HC equation includes

\[
 \frac\kappa{g^2}n^\nu D^{u\mu}X_{\mu\nu}
                 -2\lambda H_C-\gamma S=0,
 \qquad X=F(B)-F(B^u).
\]

For the present ansatz `X_tz=kappa h' P`; the unitary gauge/HC commutator force vanishes because all longitudinal matrices commute with P. The full spin-covariant Dirac, gauge and independent HC equations reduce to

\[
 \boxed{u'=(\omega-a+m+\gamma h)v,\qquad
 v'=(m+\gamma h-\omega+a)u},
\]

\[
 \boxed{a''=-g^2(u^2+v^2),\qquad
 h''=-\frac{g^2}{\kappa^2}\,[2\lambda h+\gamma(u^2-v^2)]}.
\]

All angular and normal connection components are checked after full variation. The independent projector's curvature reaction can be nonzero as an unconstrained matrix, but is diagonal in P/Q and has zero **projector-tangent** part. Its normal part is a constraint reaction, not an omitted tangent equation. The state-closure penalty vanishes. The minimal target has zero first variation on this scalar-M closed branch, so its matching chain rule adds no missing tangent source.

After dividing out the common sphere factor and omitting a constant sphere-curvature term, the stationary action density is

\[
 L_z=(\omega-a)\rho+uv'-vu'-(m+\gamma h)\sigma
           +\frac{a'^2+\kappa^2h'^2}{2g^2}-\lambda h^2.
\]

Its Euler equations reproduce the four displayed equations, but the verification also uses the unreduced four-dimensional matrix fields. In particular, the `h'^2` sign comes from the **null-axis** curvature functional, not an inserted isotropic scalar kinetic term. Existence of this stationary branch is not a proof of temporal stability or positive physical energy.

## 3. A local solution with nonzero mass, charge and HC source

As dimensionless comparison data choose

\[
 (m,\omega,g,\kappa,\gamma,\lambda)=(0.6,0.9,0.8,0.7,0.4,0.3),
\]
\[
 (u,v,a,a',h,h')\big|_{z=0}=(0.5,0.1,0,0.03,0.2,0).
\]

These are inputs, not a fit or a parameter-free physical prediction. The six first-order equations have a polynomial right side. A direct Picard box supplies a local existence/uniqueness argument independent of the numerical profile.

Take the closed coordinate box with radius 0.1 about these initial data. On it,

\[
 0.4\le u\le0.6,\quad0\le v\le0.2,\quad
 -0.1\le a\le0.1,\quad -0.07\le a'\le0.13,
 \quad0.1\le h\le0.3,\quad |h'|\le0.1.
\]

Componentwise bounds on the vector field are `(0.344,0.216,0.13,0.256,0.1,0.444082)`, with the last entry rounded upward. The Jacobian infinity norm is at most 2.01. On `|z|<=0.2`, the Picard map therefore moves at most `0.2*0.444082<0.1` and has contraction constant at most `0.402<1`. It maps the continuous box-valued functions into themselves and is a contraction. This proves a unique local solution in the box; analyticity follows from the polynomial equations.

In particular the exact local solution has `h>=0.1`, `sigma>=0.12` and a nonzero effective mass `m+gamma h>=0.64` on that interval. This positivity is not inferred merely by sampling the series. The argument concerns these stated rational comparison inputs, not a native physical interval or a proof-assistant/interval-arithmetic certificate.

The positive initial h is an explicit assumption. Starting the **independent** stationary system instead at `h=h'=0` with positive gamma sigma gives `h''<0`, so its local spatial profile goes negative. That is not an admissible positive compensator without further constraint treatment. It is also not a temporal-instability argument: z is the independent variable here. The reference construction does not derive a physical preparation from the zero-HC boundary.

The code generates Taylor coefficients by polynomial convolution at 60-digit working precision. At order 32 the maximum ODE defect at the two interval endpoints is about `3.7e-40`. This finite approximation is checked against the separate installed `mpmath.odefun` implementation; its residual is not substituted for the existence argument.

## 4. A conserved spatial first integral

The reduced stationary equations imply

\[
 \rho'=4(m+\gamma h)uv,\qquad
 \sigma'=4(\omega-a)uv.
\]

Direct differentiation then proves

\[
 \boxed{I_z=-(\omega-a)\rho+(m+\gamma h)\sigma
             +\frac{a'^2+\kappa^2h'^2}{2g^2}+\lambda h^2
             =\mathrm{constant}}.
\]

Its value for the reference data is `-0.058096875`. It is a **spatial stationary first integral**, not a temporal energy, damping law or stability theorem. It provides an additional action/conservation check unrelated to making a numerical residual small.

## 5. Check the original fields and identify what is still not solved

At `(t,theta,phi,z)=(0.4,0.9,0.4,0.15)` the independent full-field checks give approximate residual norms

- Real massive Dirac equation: `8.0e-17`.
- Sourced unitary gauge equation: `1.9e-11`.
- Independent soft-HC equation: `5.7e-12`.
- Allowed projector-tangent equation: `3.9e-12`.

Here `rho=0.2790933731`, `sigma=0.2652414887`, `h=0.1967796129`. The HC Yukawa source is nonzero, and HC differs from the target `Lambda=0`. The soft branch solves the finite-penalty comparison, **not** the hard equality `H_C=Lambda`.

Two deliberately retained failures prevent a false native identification. Keeping the original ordered HC transport in the probe equation gives residual norm `0.1029124463`; the real probe action does not contain that ordered Hermitian transport. Imposing the printed full complex connection equation even after the unitary source phase is supplied leaves an additional Hermitian residual about `0.2049502749`. The real action and the printed complex equation remain distinct theories in this realization.

The nonzero unconstrained projector reaction has norm about `0.2241643632`, while its tangent projection vanishes. Requiring the unconstrained gradient itself to vanish would impose another, different field space. Metric and axis variations, global spinor patching and finite-energy boundary data have not been solved.

## 6. Do not conflate hard elimination with an extra soft equation

If an **independently varied** HC equation is retained and `H_C=0` is then additionally demanded, nonzero gamma requires `S=0`. In this stationary zero-current real-amplitude ansatz that means `u^2=v^2`. On any nonzero interval the Dirac equations force `a=omega`; Gauss' equation then forces `rho=0`. Thus that combination of demands excludes the nonzero branch. This is a restricted overconstraint result, not a no-go for all massive probes or for every dependent-HC theory.

There is a different valid comparison: eliminate the hard identity `H_C=Lambda=0` **before** variation. HC is then not an independent degree of freedom, so its soft Euler equation is not imposed. The remaining massive Dirac--gauge system has

\[
 u'=(\omega-a+m)v,\quad v'=(m-\omega+a)u,
 \quad a''=-g^2\rho.
\]

The code constructs this hard-dependent branch with initial `(u,v,a,a')=(0.5,0.1,0,0.03)`. The coupling gamma is still 0.4, not turned off; its H term vanishes on the eliminated domain. Massive probe and gauge residuals are again approximately `7.1e-17` and `1.9e-11`. If the excluded independent-H equation is nevertheless evaluated, its nonzero residual is about `0.1057464572`.

A separate four-coordinate Picard box of radius 0.1 gives vector-field bounds `(0.32,0.24,0.13,0.256)` and Jacobian bound 1.81. On the same `|z|<=0.2` interval its displacement is at most 0.064 and contraction constant at most 0.362. Local existence of this hard reduction does not depend on importing the soft branch's positive-H box.

A formal multiplier parent expresses the same distinction. Add `Tr[Z(H_C-Lambda)]` to enforce the equality, rather than silently supplementing an independent theory with it. On this branch the H equation determines `Z=gamma S`. The multiplier is an equality-constraint reaction, not a newly derived physical reservoir or an invented externally prescribed compensating source. Since the minimal Lambda has zero first variation at exact scalar-M closure, this multiplier introduces no omitted first-order M/P chain reaction in the example. No such parent is silently inserted into the main paper.

The hard reduction's ordered HC transport also vanishes because H=0; the remaining source/real-action dictionary, actual native resonance and all geometric identifications are still conditional. The distinction between hard and soft domains must therefore be settled from the native construction, not from a preference for one numerical branch.

## Outcome and Reproduction

Massive charged probes need not be excluded by the previous massless ansatz failure. Allowing the fields to respond gives local massive branches, but their HC equations differ fundamentally with the chosen domain. The independent soft branch responds to the scalar source; the hard-dependent branch carries an excluded-direction constraint reaction instead of an independent HC evolution. Neither derives physical masses, the native carrier, a stable fluid, Einstein dynamics or the actual hard/soft choice.

- [Calculation](HC_Massive_Soft_Closure.py) and [saved results](HC_Massive_Soft_Closure.json).
- Run `python -B analysis/HC_Massive_Soft_Closure.py --output analysis/HC_Massive_Soft_Closure.json`.
- Run `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_massive_soft_closure.py`.

Forty-four focused checks cover the polynomial/Taylor system, the separate mpmath solver, explicit Picard bounds, spatial conservation, full spin/gauge/HC jets and equations, independent action variations, positivity and the hard-dependent constraint reaction. They supplement the displayed conditional local proof; they are not a native physical or proof-assistant certificate.

No package installation, main-TeX edit, PDF rebuild, publication activation or Git operation is introduced by this analysis.

The subsequent [triadic Gauss-compatibility calculation](HC_Triadic_Gauss_Compatibility.md) tests the next noncentral resonance term. It derives the remaining spatial gauge constraint and its matrix-torque propagation, gives an explicit initial-data failure, and lifts the prepared positive triadic eigenmode onto the same hard-dependent curved branch. Its new mass input has a separate local existence box; it is not identified with native M16/C7 or a measured spectrum.
