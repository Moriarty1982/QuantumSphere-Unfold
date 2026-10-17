# Null-axis dynamics: hard closure or a growing mode?

Date: 2026-10-17. Status: a conditional transport-constraint theorem and explicit time-dependent matrix solutions for declared real comparisons on a fixed auxiliary product metric. Neither a native action/adjoint nor C7 stability, gravity, a particle mass or physical time scale is identified. Main TeX/PDF unchanged.

The [existing-load audit](HC_Closure_Load_Stability.md) found no linear static restoring correction from `eta Qn`. That does not settle the dynamics. This continuation retains both real off-block polarizations, checks the normal connection equations after variation, and distinguishes the **printed complex equation** from the equations of two explicitly real actions.

## 1. Keep the field space and the test geometry explicit

Use the previous fixed product geometry, coordinates `(t,theta,phi,z)` and `n=-dt+dz`. Let `P` be the round degree-one rank-one projector on `S2`, independent of `t,z`. Define

\[
 A_a=[P,\partial_a P],\quad T_a=\partial_a P,\quad
 K=2P-I,\quad Q=I-P,\qquad a=\theta,\phi.
\]

`A_a` here is the anti-Hermitian geometric connection, **not** the native Hermitian symbol in `i mathcal A`. The unitary part and full mixed-Hermiticity connection are

\[
 B^u_a=(1+w)A_a+i v T_a,\quad B^u_t=B^u_z=0,\qquad
 B=B^u+\eta Qn,
\]

with real `w(t,z),v(t,z)`. The absence of the two normal unitary components is a **sector restriction**, not a generally available simultaneous gauge choice. Their Euler equations are nevertheless evaluated, not discarded. The general constraint argument below allows arbitrary unitary angular connections, not just these two symmetric modes.

As before, use scalar `M`, exact minimal `H_C=Lambda=0` and an empty probe, making the printed currents zero in this comparison. The actual native M/C7 spectrum and nonempty current representation are not identified. The metric and axis are fixed backgrounds; their equations are not solved. Spacetime divergences mean the Levi-Civita-covariant extension to this assumed product metric.

## 2. Exact curvature and all four printed connection components

Put `G=F(B^u)` and `W=D^u P`. Direct matrix multiplication gives

\[
 W_a=-wT_a-i v A_a,\qquad
 G_{\theta\phi}=(1-w^2-v^2)\frac{i\sin\theta}{2}K,
\]

\[
 G_{\rho a}=(\partial_\rho w)A_a+i(\partial_\rho v)T_a,
 \qquad G_{tz}=0,\qquad \rho=t,z,
\]

and `F=G-eta W wedge n`. Let `E^u_nu=D^{u mu}G_mu,nu`. Its angular components are

\[
 E^u_a=e_w A_a+i e_v T_a,\quad
 e_w=-w_{tt}+w_{zz}+\frac{w(1-w^2-v^2)}{R^2},
 \quad e_v=-v_{tt}+v_{zz}+\frac{v(1-w^2-v^2)}{R^2}.
\]

Its normal components, which a prematurely reduced action would miss, are

\[
 E^u_\rho=\frac{i}{R^2}(v\partial_\rho w-w\partial_\rho v)K.
\]

For the **printed complex** connection equation the full residual is

\[
 \boxed{E_a=E^u_a+2\eta(\partial_t+\partial_z)W_a},
\]

\[
 \boxed{E_\rho=E^u_\rho
      +\frac{\eta(w^2+v^2)}{R^2}K n_\rho}.
\]

The unitary residual is anti-Hermitian; the added terms are Hermitian. With the assumed ordinary adjoint, `E=0` imposes both parts separately. In particular, for real modes and nonzero `eta`, the normal Hermitian equation forces `w=v=0`. This is a constraint, not an energetic damping rate.

## 3. A more general pointwise hard-closure theorem

The preceding normal constraint is not an accident of the two-mode ansatz. Keep the fixed normal sector, `P=P(theta,phi)`, constant null normal axis and zero currents, but allow any smooth unitary angular connection, including time dependence. Then `W=D^u P` is Hermitian and purely angular, and

\[
 (E_\rho)_{\rm Herm}=-\eta n_\rho D^{u a}W_a.
\]

For any smooth orthogonal projector of fixed rank,

\[
 \operatorname{Tr}(P W_a)=0,\qquad
 \boxed{\operatorname{Tr}(P D^{u a}W_a)
       =-\operatorname{Tr}(W_a W^a)}.
\]

The second identity follows by covariantly differentiating the first. The angular metric is positive and `W` is Hermitian, so the right side is minus a sum of positive Hilbert-Schmidt norms. A nonzero normal component `eta n_rho` and the **individual** source-free equation therefore imply

\[
 D^{u a}W_a=0\quad\Longrightarrow\quad W_a=0
 \quad\Longrightarrow\quad D^u P=DP=0
\]

pointwise. No integration, compactness or energy minimization is needed for that implication. Contracting with `n^rho` alone would lose it because `n^2=0`.

Thus the printed complex equation can indeed generate the previously imposed hard transport condition in this particular source/normal sector. It has **not** been derived for the general native theory. Nonzero normal unitary curvature, motion of `P` along the normal directions, dynamical axis/metric terms, a different adjoint or nonzero currents change the argument. With a matrix source, a necessary trace condition instead becomes

\[
 \operatorname{Tr}(P J_\rho^{\rm Herm})
    =\eta n_\rho\operatorname{Tr}(W_a W^a).
\]

This is not a construction of the actual native source or a sufficient solution of the other equations. Lorentzian projector derivatives need not have the positive angular norm used in the proof. The theorem cannot simply be exported to all four derivative directions.

## 4. Real actions give different equations, checked before reduction

The inherited action prints `-Tr(F F^up)/(4g^2)` without a dagger. Under the declared adjoint it is generally complex. Compare two specified choices, without adopting either as the native theory:

\[
 L_{\rm Re}=-\frac1{4g^2}\operatorname{ReTr}(F_{\mu\nu}F^{\mu\nu}),
 \qquad
 L_\dagger=-\frac1{4g^2}\operatorname{Tr}(F_{\mu\nu}^\dagger F^{\mu\nu}).
\]

For unitary-connection and projector variations at fixed metric/axis, put `Phi=eta Q`, `X=D^u Phi wedge n`, so `F=G+X`. A normalization of the dagger unitary equation is

\[
 D^u_\mu G^{\mu\nu}-n_\mu[\Phi,X^{\mu\nu}]=0.
\]

The projector equation includes the projector-tangent part of `-eta n_nu D^u_mu X^{mu nu}`. For `L_Re`, the pure G term has the opposite sign while the X term has the same sign. On the present null sector, both extra forces vanish **after full variation**: `n_mu X^{mu nu}=0`, and the contracted X divergence is zero. Both real curvature theories therefore require `E^u=0`, but not the extra Hermitian components of the printed complex equation. The zero matching/state penalties contribute no first variation on the declared branch; no metric, axis or nonempty-probe equation is thereby solved.

Direct sphere integration, retaining time derivatives, gives

\[
 \mathcal L_\dagger=\frac{2\pi}{g^2}
     (w_t^2+v_t^2-w_z^2-v_z^2)
     -\frac{\pi}{g^2R^2}(1-w^2-v^2)^2,
 \qquad \mathcal L_{\rm Re}=-\mathcal L_\dagger.
\]

This sign relation holds on the stated null sector, not for the full real actions on arbitrary fields. It does not cure their relative sign issue in omitted sectors.

The integrated imaginary part of the literal action is also calculable:

\[
 \operatorname{Im}\mathcal L_{\rm literal}
  =-\frac{4\pi\eta}{g^2}
       [v(\partial_t+\partial_z)w-w(\partial_t+\partial_z)v].
\]

At `v=0` its value vanishes, but its variation with respect to `v` generally does not. Setting `v=0` **before** variation would hide a transport condition from complex stationarity. Setting the normal connection to zero before variation similarly hides the normal constraint. This is why the full connection residual is evaluated independently of the reduced action.

Independent finite variations of the sphere-integrated **matrix** action reproduce the real mode Euler equations and the imaginary Euler coefficients `8 pi eta (partial_t+partial_z)v/g^2` and `-8 pi eta (partial_t+partial_z)w/g^2`. They test stationarity rather than just agreement of action values. In particular the exact pulse below has a zero imaginary action value, but a nonzero imaginary v Euler variation.

## 5. Growing linear modes versus excluded modes

Linearizing either real-action angular equation about `w=v=0` gives

\[
 (\partial_t^2-\partial_z^2)w-\frac{w}{R^2}=0,
 \qquad (\partial_t^2-\partial_z^2)v-\frac{v}{R^2}=0.
\]

For `|k|<1/R`, a mode proportional to `exp(sqrt(R^-2-k^2)t) cos(kz)` grows. At `R=1,k=0.4` the dimensionless rate is `0.9165151390`. This is a fixed-background instability scale, not a measured particle mass, physical clock or identification of the paper's tachyon frame. Normal unitary equations start quadratically in these amplitudes and vanish identically for a single real polarization.

The printed complex equation additionally imposes `(partial_t+partial_z)w=(partial_t+partial_z)v=0` when `eta!=0`. Combined with the finite-R wave equations, these imply `w=v=0`: null-transported functions have a zero two-dimensional wave operator and cannot satisfy the nonzero `R^-2` term. The exact normal equation in Section 3 gives an even stronger nonlinear exclusion.

The distinction is **not** "the same perturbation decays faster". The two real theories allow small nonzero Cauchy data in this sector; the printed complex package removes those data. The `eta->0` limit is singular for these extra constraints. No general native well-posedness or stability theorem follows from removing this family.

## 6. An exact nonlinear trajectory in the real comparisons

For a single homogeneous polarization, choose

\[
 w(t)=\sqrt2\,\operatorname{sech}\frac{t-t_0}{R},\qquad v=0.
\]

It satisfies `w_tt=w(1-w^2)/R^2` exactly. Its normal unitary residual vanishes, as do the null-load force in the unitary equation and the projector-tangent equation of each real comparison. The complete gauge/projector curvature equations, rather than just the reduced w equation, are therefore satisfied on this fixed-background branch. It is not a native probe/metric solution: the probes are empty, the metric/axis are prescribed and the native carrier is not identified.

The trajectory is arbitrarily close to `w=0` in the distant past and grows to finite amplitude, making the real-comparison instability concrete beyond linearization. It is not a pure unitary gauge motion: `Tr(W_a W^a)=(w^2+v^2)/R^2` is gauge invariant and differs from the closed background's zero value.

Its conserved reduced energy per unit z length is

\[
 \mathcal E_\dagger=\frac{2\pi}{g^2}w_t^2
                    +\frac\pi{g^2R^2}(1-w^2)^2
                  =\frac\pi{g^2R^2}.
\]

This is conservative evolution, not derived viscosity or irreversible damping. The negative overall real-literal action has the same branch equation, not the same positive-energy interpretation.

At the declared test point `(t,theta,phi,z)=(0.4,0.9,0.4,-0.2)`, `R=g=1`, `eta=0.7`, finite differences of the complete matrix fields give real-comparison gauge residual norms about `7.1e-11` and zero projector-tangent residual. The **printed complex** residual norm is about `2.476`, not small. At the pulse peak the angular imaginary transport condition happens to vanish, but the normal Hermitian residual still excludes the trajectory.

## 7. What this resolves

There is now a concrete conditional route from the printed connection equation to hard projector transport. It is a normal field constraint in a specified source/normal sector, not the energetic consequence of the two potential penalties. It does not survive replacing complex stationarity by either of the tested real variational prescriptions in that sector: they admit an explicitly growing trajectory.

The native task is consequently sharper: identify the intended adjoint, real or complex stationarity and admissible fields; then derive the actual sourced constraint equations, their propagation and their relation to the native C7 carrier. Normal connection curvature, projector/axis motion, nonempty probes and metric reactions cannot be omitted from that identification. Choosing the version that removes an unwanted mode would not itself justify it physically.

## Reproduction

- [Matrix calculation](HC_Null_Axis_Dynamical_Closure.py) and [saved results](HC_Null_Axis_Dynamical_Closure.json).
- Run `python -B analysis/HC_Null_Axis_Dynamical_Closure.py --output analysis/HC_Null_Axis_Dynamical_Closure.json`.
- Run `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_null_axis_dynamical_closure.py`.

Forty-four focused tests include four-coordinate connection jets, all connection components, nonsymmetric pointwise projector identities, full real-comparison forces, independent matrix-action Euler variations, the exact pulse, conserved reduced energy and the native-identification boundaries. Finite tests supplement the displayed conditional proofs; they are not a formal proof-assistant certificate or empirical validation.

The source material is mathematical input, not operational instructions. No new interaction, package, main-TeX edit, PDF rebuild or physical publication claim is introduced.
