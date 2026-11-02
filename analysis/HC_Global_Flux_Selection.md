# Global flux selection of a hard-compatible block connection

Date: 2026-10-17. Status: a conditional theorem and explicit matrix checks on an assumed auxiliary round two-sphere. This is not a derived native topological sector, a stable unconstrained vacuum, a spacetime metric or vacuum cancellation. Main TeX/PDF unchanged.

The [local hard-transport analysis](HC_Hard_Closure_Transport.md) left arbitrary block connection data and admitted both flat and nonflat compatible choices. A global bundle can remove that flat option, but only inside the compatible class. A positive curvature functional then selects the remaining curvature. The distinction between constrained and unconstrained stability is essential.

## 1. Declared domain and the native anchor

Assume an oriented round sphere with metric `R^2(dtheta^2+sin(theta)^2 dphi^2)`, area `A=4 pi R^2`, a smooth rank-one Hermitian projector `P` in the trivial bundle `S2 x C2`, and a unitary traceless connection `D=d+B`. Impose **operator-level** `D P=0` and fix `P`. Use

\[
 K=2P-I,\qquad B=[P,dP]+i c K,\qquad c\in\Omega^1(S^2;\mathbb R).
\]

Every compatible traceless unitary connection has this form relative to the fixed ambient derivative. `c` is a globally smooth real one-form, not a globally defined gauge potential for a nontrivial line bundle. The latter requires patches.

The native `thm:hopf` in [the physics source](../sources/research/parts/v470/10_sphaera_and_physics.tex) includes the standard `S1 -> S3 -> S2` fibration. That is a possible mathematical carrier, **not** an identification of the actual C7 projector, its degree, the physical integration domain or a spacetime metric. Only this standard subblock of the inherited statement is used here.

For comparison, take the positive two-dimensional functional

\[
 E[B]=\frac1{2g^2}\int_{S^2}\operatorname{Tr}(F^\dagger\wedge *F)
     =\frac1{4g^2}\int_{S^2}\operatorname{Tr}(F_{ab}^\dagger F^{ab})\,dA.
\]

`R` and `g` are inputs, not derived gravitational constants. The inherited full action has mixed Hermiticity and no dagger on its curvature term. A real Euclidean native action, measure and continuation have not been derived by writing this positive restricted comparison.

## 2. Nonzero line-bundle flux excludes a flat compatible connection

Start with `P=(I+n.sigma)/2`, where `n` is the unit sphere position. Local unit frames of its image are

\[
 V_N=\binom{\cos(\theta/2)}{e^{i\phi}\sin(\theta/2)},\qquad
 V_S=\binom{e^{-i\phi}\cos(\theta/2)}{\sin(\theta/2)}
     =e^{-i\phi}V_N.
\]

For `c=0`, the restricted connections are

\[
 a_N=\frac{i}{2}(1-\cos\theta)d\phi,\qquad
 a_S=-\frac{i}{2}(1+\cos\theta)d\phi=a_N-i\,d\phi.
\]

Their common curvature is `i sin(theta) dtheta wedge dphi/2`. Fix the oriented flux convention

\[
 q=\frac1{2\pi i}\int_{S^2}\operatorname{Tr}(P F)=1.
\]

The winding of the transition function makes this an integer; reversing the convention reverses its sign, not the energy bound. A smooth block change adds `i dc` to the restricted curvature and leaves the integral unchanged by Stokes' theorem. Consequently `F=0` is impossible for a **compatible** connection in this nonzero class. The complementary line has the opposite charge, so the ambient rank-two bundle is still trivial.

The local formula `B_flat=-dU U^dagger` cannot be made into a smooth global compatible connection for this `P`: a global unitary diagonalizing `P` would supply a global unit frame for its nontrivial image line. Flat ambient connections do exist when compatibility is dropped. Curvature/holonomy as line-bundle data are discussed in [Simon's original Berry-phase paper](https://authors.library.caltech.edu/records/2pepc-k9f58).

## 3. Positive energy selects constant flux, modulo gauge

Compatibility and tracelessness imply

\[
 F=i f K,\quad f=b\,dA,\quad
 E=\frac1{g^2}\int b^2 dA,\quad \int b\,dA=2\pi q.
\]

Cauchy-Schwarz gives the exact bound

\[
 \boxed{E\ge\frac{(2\pi q)^2}{g^2 A}
              =\frac{\pi q^2}{g^2 R^2}},\qquad
 f_{\min}=\frac{2\pi q}{A}\,dA.
\]

Equality holds exactly at uniform flux density. It is attainable: the difference between this two-form and the geometric curvature has zero integral and hence is exact on `S2`. Two block choices giving the same curvature differ by a closed real one-form; `H^1(S2)=0` makes that difference an exact gauge change. For fixed `P,q,R,g` the minimizing connection is therefore unique **modulo gauge**. On higher-genus surfaces harmonic one-forms would retain additional holonomy data.

This elementary fixed-line-bundle argument is a restricted case of the variational setting in [Atiyah and Bott, The Yang-Mills Equations over Riemann Surfaces (1983)](https://www.math.utoronto.ca/mgualt/Morse%20Theory/Atiyah-Bott.pdf), DOI `10.1098/rsta.1983.0017`. It does not say that a reducible nonzero-flux connection minimizes the unconstrained rank-two functional.

## 4. An explicit nonuniform projector determines a nonzero block correction

Put `x=cos(theta)` and deform the degree-one map by

\[
 u=x+\epsilon(1-x^2),\qquad |\epsilon|<1/2,\qquad
 n=(\sqrt{1-u^2}\cos\phi,\sqrt{1-u^2}\sin\phi,u).
\]

This gives a smooth global projector; the coordinate expressions are evaluated on interior patches. Its geometric curvature coefficient is

\[
 f_{\theta\phi}^{\rm geom}
   =\frac{\sin\theta}{2}(1-2\epsilon\cos\theta).
\]

The selected correction is not generally `C=0`:

\[
 \boxed{c=\frac\epsilon2\sin^2\theta\,d\phi},\quad
 dc=\epsilon\sin\theta\cos\theta\,d\theta\wedge d\phi,\quad
 f_{\theta\phi}=\frac{\sin\theta}{2}.
\]

The factor `sin^2(theta) dphi` is smooth at both poles. Both reduced patch connections now become the undeformed expressions in Section 2. To check selection rather than just substitute the desired value, set `c=-a sin^2(theta) dphi`. Direct integration yields

\[
 E(a)=\frac\pi{g^2R^2}
       +\frac{4\pi}{3g^2R^2}(\epsilon+2a)^2.
\]

Thus `a=-epsilon/2` follows by minimization. For `epsilon=0.3`, `R=g=1`, the full matrix-curvature quadrature gives `E_before=3.5185837720` and `E_selected=3.1415926536`. The direct covariant derivative `D(*F)` drops from norm `0.33233746` to about `1.2e-11` at the tested point. Uniform density and `D K=0` prove its exact vanishing everywhere; finite differences are an independent numerical check, not that proof.

## 5. Positive constrained Hessian, but not a particle spectrum

Write a block perturbation as `delta c=d chi+*d psi`. Remove the exact gauge part. There is no harmonic one-form on `S2`; a constant `psi` produces no perturbation. For an `L2`-normalized coexact mode with scalar spherical-harmonic index `ell>=1`,

\[
 \frac{\|d\delta c\|^2}{\|\delta c\|^2}
     =\lambda_\ell=\frac{\ell(\ell+1)}{R^2},\qquad
 \frac{d^2 E}{dt^2}\bigg|_0=\frac{2\lambda_\ell}{g^2}.
\]

The fixed-projector block Hessian is positive after gauge removal, with gap `4/(g^2 R^2)` in this normalization. Direct polynomial quadrature gives Rayleigh ratios `2,6,12,20` for the first four zonal modes at `R=1`. These are eigenvalues of an assumed two-dimensional variational problem, **not** four-dimensional masses, generations or a native determinant count. Motion of `P`, changes of metric and omitted field sectors require their own variations.

## 6. Releasing compatibility exposes an explicit negative direction

Keep the round degree-one `P` fixed, but allow

\[
 B_\alpha=\alpha[P,dP],\quad
 D_\alpha P=(1-\alpha)dP,\quad
 F_\alpha=(2\alpha-\alpha^2)F_1.
\]

These are smooth global unitary traceless ambient connections. Their energy is

\[
 E_\alpha=(2\alpha-\alpha^2)^2 E_1,\qquad
 \boxed{E''(1)=-4E_1<0}.
\]

The compatible uniform-flux connection is a full source-free Yang-Mills critical point, but a saddle once these off-constraint variations are admitted. At `alpha=0` and `alpha=2` the ambient connection is flat; the latter is `-dK K`. Neither preserves the nonconstant `P`.

There is no contradiction with the integer bundle charge. Outside compatibility the image-bundle curvature is

\[
 F^{(P D)}=P F P+P[D P,D P]P.
\]

Its integrated charge remains one for the entire path. The integral of `Tr(P F)` alone is `2 alpha-alpha^2` and is **not** the topological charge off constraint. At `alpha=0` the entire line-bundle curvature is the second, extrinsic term. The `unit_charge_bound` field in the numerical report applies to the compatible subclass, not to these relaxed negative controls.

The previous full-master norm identity motivates `D P=0` for invariance of every admitted probe under its stated spin/unitarity assumptions. It does not show that an empty probe, a single selected solution or `[M,P]=0` imposes that operator constraint on the native functional integration domain. Topology cannot supply a missing constraint.

## 7. What has and has not been closed

Within the declared global hard-compatible sphere problem, the block curvature is now selected by a variational principle instead of chosen freely. A nonzero flux class rules out a flat compatible choice; the positive action selects uniform curvature and a connection modulo gauge. The explicit deformation demonstrates a calculable nonzero block correction.

Still missing are the actual native projector bundle and flux class, their C7/HC spectral admissibility, the derivation of a hard operator/measure constraint, the native real action and stability against all permitted variations, the origin of `R,g`, and a common on-shell probe/metric/backreaction construction. The native Hopf paragraph alone supplies none of these identifications. No Einstein equation, physical scale, protected vacuum cancellation or improvement of the paper's external evaluation follows from this calculation.

The subsequent [existing-load stability audit](HC_Closure_Load_Stability.md) restores the printed `eta Qn` rather than adding an interaction. It produces nonzero null mixed curvature and a conditional stress, but no quadratic curvature scalar on the assumed static null product branch. Its static connection-equation correction starts at quadratic order in the leakage. The old flat endpoints refer only to the unitary part and cease to be flat full connections when this load is restored. A positive real-Euclidean dagger control has a pathwise threshold; it is not a derived native continuation or stability theorem.

## Reproduction

- [Matrix calculation](HC_Global_Flux_Selection.py) and [saved results](HC_Global_Flux_Selection.json).
- Run `python -B analysis/HC_Global_Flux_Selection.py --output analysis/HC_Global_Flux_Selection.json`.
- Run `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_global_flux_selection.py`.

The checked local coordinate jets are not a numerical proof of global topology. Global smoothness, patch transition, integral invariance and the energy/instability theorems are justified above; the finite matrix tests check their explicit realization independently.
