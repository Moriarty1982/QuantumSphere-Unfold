# Does the existing closure load stabilize projector transport?

Date: 2026-10-17. Status: exact conditional curvature, penalty and static-residual identities, checked in a finite product realization. This is not a full native stability theorem or a derived C7/metric/Wick-rotation identification. Main TeX/PDF unchanged.

The [global-flux analysis](HC_Global_Flux_Selection.md) selected a compatible connection, but found a negative direction once `D P=0` was relaxed. Before adding any new stabilizer, this continuation restores the **already printed** load `eta (I-P)n_mu` and checks whether the native penalties directly control that direction.

## 1. What the printed penalties do, and what they do not do

The [native variational block](../sources/research/parts/v470/10_sphaera_and_physics.tex), `thm:variational-form`, prints

\[
 U_{C_7}=\lambda_C\|Q\Psi\|^2,\qquad
 U_{HC}=\lambda_H\|H-\Lambda[M,P]\|^2,\qquad Q=I-P.
\]

The minimal `Lambda` depends on `M,P`, not on the connection. On a matching branch `H=Lambda` the second penalty is zero. At exact algebraic closure `[M,P]=0`, `Lambda=H=0`. A connection variation with `P,M,Psi` fixed and `Q Psi=0` leaves **both** penalties zero, even if it changes `D P`. This remains true at arbitrary finite positive penalty coefficients.

For an explicit comparison choose `M=0.6 I` and the previous round rank-one projector. This degenerate operator commutes with every `P`. It is not an evaluated native Millennium matrix. A nonzero normalized instantaneous probe in `im P` confirms that this is not merely the empty-probe zero of `U_C7`; it is not presented as a solution of the sourced master system.

The earlier full-master normal operator has the same issue. Adding `eta Q n` does not change `Q(D P)P`, because `[Q,P]=0`, or act directly on a closed probe, because `Q Psi=0`. For the round sphere and the orthonormal spin-factorized realization used here,

\[
 \|\mathcal N\|_F^2=\frac{2(1-\alpha)^2}{R^2}
\]

along `B^u_alpha=alpha[P,dP]`, with block-preserving scalar resonance. This norm is independent of `eta`. It measures operator leakage, not a newly derived energy term. Finite potential penalties on state amplitudes are not themselves a hard projector-transport constraint. Backreaction, a restricted domain or quantum corrections might still change the full result and have not been excluded.

## 2. Restore the closure load on a declared product geometry

To keep the null axis explicit, use the assumed product metric and coordinates

\[
 ds^2=-dt^2+R^2(d\theta^2+\sin^2\theta\,d\phi^2)+dz^2,
 \qquad n=-dt+dz,\qquad n^2=0.
\]

This is a test geometry, not the native bilinear metric. `P` is the round sphere projector and is independent of `t,z`. Define

\[
 B^u_\alpha=\alpha[P,dP],\quad W=D^u_\alpha P=(1-\alpha)dP,
 \quad B=B^u_\alpha+\eta Qn.
\]

`B^u` is anti-Hermitian; the real `eta Qn` load is Hermitian. The full connection is therefore not silently treated as a unitary one. Since `n` is constant and the load's wedge square vanishes,

\[
 \boxed{F=G+X,\quad G=F(B^u_\alpha),\quad X=-\eta W\wedge n},
 \qquad G=(2\alpha-\alpha^2)F(B^u_1).
\]

The added curvature is nonzero when `eta` and `1-alpha` are nonzero. In particular, the old flat **unitary-part** endpoints `alpha=0,2` are not flat full connections after the load is restored.

## 3. Null quadratic contraction is not zero field or zero stress

Here `G` has only angular components, `X` has one angular and one normal component, and `n.W=0`. Therefore their curvature contractions have no mixed term. For either literal or dagger contraction, the load's quadratic scalar vanishes:

\[
 \operatorname{Tr}(X_{\mu\nu}X^{\mu\nu})
 =\operatorname{Tr}(X_{\mu\nu}^\dagger X^{\mu\nu})=0.
\]

For example, the dagger expression is `2 eta^2[n^2 Tr(W_mu W^mu)-Tr((n.W)^2)]`, and both terms vanish. Thus the sphere integral of the static curvature contraction is independent of `eta` along this family. This does **not** prove zero energy, no backreaction or stability: a scalar contraction alone is not a Hamiltonian or a full field variation.

An explicit negative control makes that distinction quantitative. For the **declared alternative** action `L_dagger=-Tr(F^dagger F^up)/(4g^2)`, vary the metric holding the covariant field strength and `n_mu` fixed before evaluating the null background. The load contribution is

\[
 T^{X}_{\mu\nu}
  =\frac1{g^2}\operatorname{ReTr}(X_{\mu\lambda}^\dagger X_\nu{}^\lambda)
  =\frac{\eta^2(1-\alpha)^2}{g^2R^2}n_\mu n_\nu.
\]

It is nonzero, traceless and directed along the null axis. At `R=g=1`, `eta=0.7`, `alpha=0.8`, its sphere-integrated `T00` is `0.2463008640`, despite the zero load scalar. This stress is from a stated dagger/metric comparison; it is not a native stress identification, an on-shell Einstein source, or the energy of a completed system with the axis dynamics included. Enforcing nullness during metric variation instead requires its constraint reactions or the actual metric dependence of `n`.

Nonzero null gauge fields with vanishing scalar invariants are also studied in [Kuchynka, Gauge fields with vanishing scalar invariants (2020)](https://arxiv.org/html/1902.07281v3), DOI `10.1088/1361-6382/ab4360`. That is context for the scalar-versus-field distinction, not an identification of this mixed-Hermiticity, generally off-shell example with that paper's Yang-Mills or universal/VSI solutions. We have not checked all higher invariants.

## 4. Check the printed connection equation, not just the action value

Use an empty probe, scalar `M` and `H=0`, so the three printed currents vanish in this finite comparison. Interpret the spacetime divergence as the Levi-Civita-covariant extension to the assumed product metric; that extension is not a derived microscopic geometry. Covariant coordinate differentiation of the **printed complex** equation then gives

\[
 D^\mu F_{\mu\nu}=\mathcal E^G_\nu
             +\frac{\eta(1-\alpha)^2}{R^2}K n_\nu,
 \qquad K=2P-I,
\]

where the angular anti-Hermitian part is

\[
 \mathcal E^G_\theta
  =-\frac{i(2\alpha-\alpha^2)(1-\alpha)}{R^2\sin\theta}\,\partial_\phi P,
 \qquad
 \mathcal E^G_\phi
  =\frac{i(2\alpha-\alpha^2)(1-\alpha)\sin\theta}{R^2}\,\partial_\theta P.
\]

The useful intermediate identity is

\[
 D^{u\,a}_\alpha D^u_{\alpha a}P
       =-\frac{(1-\alpha)^2}{R^2}K.
\]

At `alpha=1` the full residual vanishes. Away from it, the static load contribution is quadratic in `1-alpha`, whereas the angular residual starts linearly and is independent of `eta`. Hence this calculation supplies no `eta`-dependent **linear static angular restoring correction**. At `alpha=0,2` the load contribution is generally nonzero, so those restored endpoints are not new source-free solutions.

The implementation differentiates `sqrt(|g|) F^{mu nu}`, adds the full matrix commutator and lowers the remaining index. Its error against the displayed formula is approximately `3.1e-11` at the declared point. The product-metric Christoffel/density terms are not omitted.

This is not a time-dependent stability theorem. Electric/normal constraints, probe reactions and the real action must be evaluated together for that. In particular, a real dagger action is not automatically equivalent to the printed complex resonance equation; the [earlier action audit](HC_Null_Axis_Action_Check.md) already distinguished those choices.

## 5. Why a positive Euclidean threshold cannot be imported silently

For a separate control, replace the metric by `dt_E^2+R^2 dOmega^2+dz^2` while keeping the same real normal covector. This is **not** a derived Wick rotation of the real null background: the real Euclidean vector has `|n_E|^2>0`. Direct integration gives

\[
 E_{\dagger,E}(\alpha)
 =\frac\pi{g^2R^2}(2\alpha-\alpha^2)^2
   +\frac{2\pi\eta^2|n_E|^2}{g^2}(1-\alpha)^2.
\]

Consequently its second variation at `alpha=1` is

\[
 E''_{\dagger,E}(1)=\frac{4\pi}{g^2R^2}
                     (\eta^2|n_E|^2R^2-1).
\]

Along this single path, negative curvature disappears when `eta^2 |n_E|^2 R^2>=1`. At equality the leading variation is positive quartic. This is not a full-field stability threshold or a particle mass. With `n_E=(-1,0,0,1)`, its dimensionless boundary is `|eta|R=1/sqrt(2)`, but neither factor is a native measured quantity here.

There is a second, independent distinction. If the no-dagger expression is kept with its printed minus sign on this real Euclidean slice, the load has the **opposite** sign:

\[
 E_{-\mathrm{literal},E}(\alpha)
 =\frac\pi{g^2R^2}(2\alpha-\alpha^2)^2
   -\frac{2\pi\eta^2|n_E|^2}{g^2}(1-\alpha)^2,
\]

so its second derivative is always negative in this direction. The notation denotes a diagnostic static Euclidean functional, not a justified continuation of the native action. A positive load penalty follows from the dagger comparison and real Euclidean axis together, not from the mere presence of `eta Qn` in the original derivative.

## 6. Result and next native obligations

The existing terms have now been tested instead of supplemented. Algebraic HC matching and `Q Psi` penalties do not directly constrain connection leakage at fixed closed data. The closure load does see that leakage through an additional null curvature and a conditional nonzero stress, but the scalar contraction is degenerate and its static printed-equation correction starts at quadratic order along this path. A positive Euclidean control can lift the path only under declared action/axis choices.

What remains is specific: fix the native internal adjoint and real action, derive its connection/projector equations with the actual allowed variations, establish whether hard `D P=0` belongs to the physical domain, and perform a full time-dependent constrained stability calculation with all sources. The scalar `M`, auxiliary round sphere, fixed axis, empty probe and independent metric are comparison assumptions; their actual C7 admissibility and physical scales still require identification. No universal failure of stabilization by every possible native probe or quantum background is proved.

The subsequent [dynamical closure calculation](HC_Null_Axis_Dynamical_Closure.md) evaluates two real off-block polarizations and retains the normal equations. In the same zero-current/normal sector, the printed complex equation forces hard `D P=0` through a pointwise positive projector identity. The two declared real actions do not impose that Hermitian normal equation there and admit an exact growing-and-returning pulse. Independent matrix-action Euler variations show why a zero imaginary action value is not sufficient for complex stationarity. This is a conditional constraint theorem, not a selected native action or full sourced stability result.

## Reproduction

- [Matrix calculation](HC_Closure_Load_Stability.py) and [saved results](HC_Closure_Load_Stability.json).
- Run `python -B analysis/HC_Closure_Load_Stability.py --output analysis/HC_Closure_Load_Stability.json`.
- Run `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_closure_load_stability.py`.

No additional interaction, package, main-TeX edit, publication claim or PDF rebuild is introduced.
