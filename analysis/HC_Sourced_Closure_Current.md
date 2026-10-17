# Sourced closure: current typing and a charged massless branch

Date: 2026-10-17. Status: conditional trace/source identities and an explicit local charged massless probe--connection solution for declared real comparisons. This is not a native massive C7 realization, global finite-energy solution, derived physical adjoint or gravitational completion. Main TeX/PDF unchanged.

The [dynamical closure theorem](HC_Null_Axis_Dynamical_Closure.md) used an empty probe. This continuation inserts an actual nonzero probe, checks its matrix current and solves its Dirac equation together with a sourced connection equation. It first exposes why source **type and phase** must be fixed before extending the earlier theorem.

## 1. The source in the native text is not yet a gauge-current dictionary

At `thm:resonance-field-eq`, the [retained native field package](../sources/research/parts/v470/10_sphaera_and_physics.tex) writes

\[
 D^\mu F_{\mu\nu}=J^{(\Psi)}_\nu+J^{(C_7)}_\nu+J^{(HC)}_\nu,
 \quad J^{(\Psi)}_\nu=\bar\Psi\Gamma_\nu\Psi,
\]

with the last two sources defined as gradients of `Tr(M P)` and `Tr(H_C M)`. The displayed probe bilinear and trace gradients are scalars. Their insertion into the matrix equation, generator projection and phase relative to `B^u=i mathcal A` are not supplied by those expressions alone. A scalar identity lift, an unprojected internal matrix current, and a generator-projected Lie-algebra current are different interpretations.

For this calculation use the ordinary factorized spin adjoint from the [real-probe audit](HC_Real_Probe_Current_Closure.md), with `K^mu=beta Gamma^mu` Hermitian and `K^0=I`. For internal rows and spin columns,

\[
 j^\mu=\Psi(K^\mu)^T\Psi^\dagger,\qquad
 S=\Psi\beta^T\Psi^\dagger.
\]

The matrix currents are Hermitian, `j^0` is positive semidefinite and `Tr(j^0)=||Psi||^2`. If `P Psi=Psi`, then `j=P j P`. These facts depend on the stated adjoint and on unprojected matrix currents, not on an evaluated native C7/gauge representation. The examples are classical/effective commuting amplitudes, not renormalized quantum current expectations.

## 2. A fixed-M hard-closure identity removes the two printed gradient sources

For a smooth projector, `dP` is off-diagonal in its `P/Q` splitting. If `M` is fixed and `[M,P]=0`, it is block-diagonal, so

\[
 \boxed{\partial_\nu\operatorname{Tr}(M P)
          =\operatorname{Tr}(M\partial_\nu P)=0}.
\]

This does not require `M` to be scalar or its eigenvalues nondegenerate. If `M` varies, retain `Tr((partial_nu M)P)`; it cannot be dropped. Exact minimal closure also gives `H_C=0` identically, so its printed trace-gradient current vanishes. These identities concern the printed gradients, not every possible Noether current from a different action or a separate background reaction.

Under the fixed-M hard assumptions, the literal source must consequently be supplied by the probe itself, unless further interactions/current terms are specified.

## 3. A general trace-reality obstruction under direct Hermitian insertion

Let `B=B^u+Phi n`, with `B^u` anti-Hermitian, `Phi=kappa H_C+eta Q` Hermitian, real coefficients and real `n`. The trace of a commutator vanishes, hence

\[
 \operatorname{ReTr}F
 =d[(\operatorname{Tr}\Phi)n]
 =d[(\kappa\operatorname{Tr}H_C+\eta\operatorname{rank}Q)n].
\]

At hard closure, fixed rank and constant eta, a closed axis one-form `dn=0` therefore gives

\[
 \boxed{\operatorname{ReTr}(D^\mu F_{\mu\nu})=0}.
\]

This trace identity does not assume a traceless unitary connection, a sphere, static fields or `DP=0`. Under the stated positive-time adjoint it prevents a nonzero **direct Hermitian** probe current, or a real scalar identity lift of that current, from being the sole right side. Lowering the time index changes its sign, not its nonzero real trace. The fixed-M gradient identities above rule out those two printed gradients as a cancellation on this branch.

The conclusion is conditional on that particular reading. A current already multiplied by `i`, an indefinite/different adjoint, variable HC trace, a nonclosed axis or other reactions can change it. A traceless gauge projection `j -> j-Tr(j)I/N` also removes this trace test, but loses positivity and generally `P` support; the actual gauge algebra must be identified before using either property. This is not a universal native impossibility theorem.

## 4. A variable null axis fixes the trace but not necessarily the source block

There is a stronger block statement **if compatible transport has been imposed or derived**. With `D^u P=0`, hard `H_C=0` and arbitrary real axis form,

\[
 F=G+\eta Q\,dn,\qquad [G,P]=0,\qquad
 \operatorname{Herm}(D^\mu F_{\mu\nu})
     =\eta Q\nabla^\mu(dn)_{\mu\nu}.
\]

The Hermitian response is entirely in `Q`, whereas the unprojected closed probe current is in `P`. It cannot source that closed current by direct Hermitian insertion. This block obstruction remains even when the trace obstruction is relaxed by a varying axis. It does not apply unchanged to generator-projected currents, noncompatible connections or a nonzero compensator with a P block.

For an explicit control keep the previous product metric and put `n=f(z)(-dt+dz)`, `f=1+c z^2/2`. The axis is still null everywhere, but `dn` is nonzero. The load has

\[
 \operatorname{Herm}(D.F)_t=-\eta c Q.
\]

With `c=rho/eta`, its trace equals that of the intended `j_t=-rho P` for rank-one P,Q. Nevertheless the matrix mismatch has norm `sqrt(2)rho`. At `rho=0.4` it is `0.565685425`. Matching the trace or preserving nullness alone is not a matrix solution. The axis profile here is a negative control, not a derived axis equation or proposed repair.

## 5. The consistent unitary-source phase follows from a common real action

In the ordinary unitary convention `B^u=i mathcal A`, a real symmetric probe action couples as `-Tr(mathcal A_mu j^mu)`. Independent matrix variations reproduce `delta L_probe/delta mathcal A_mu=-j^mu`.

For the dagger bosonic action with coefficient `1/g^2`, its unitary field equation on the compatible constant-axis branch is

\[
 \boxed{D^{u\mu}G_{\mu\nu}=i g^2 j_\nu}.
\]

The real part of the printed literal curvature action has the opposite pure-unitary sign and gives `D^u G=-i g^2 j` for the same probe interaction. These source phases and signs follow from each stated common action, not from selecting the result one prefers. Neither real action recovers all the extra Hermitian equations of the printed complex package automatically. Inserting an `i` only on its right side is not a completed native action repair.

The example below needs an allowed central unitary component as well as the compatible geometric connection. A purely traceless connection cannot support the nonzero trace of the unprojected current without a Lie-algebra projection or other flux data. The allowed comparison carrier is U(2); it is not identified with the native gauge algebra.

## 6. A nonempty charged probe and its own connection can be solved together

Retain the fixed metric `-dt^2+R^2 dOmega^2+dz^2`, round degree-one `P`, `H_C=0` and constant null axis. On an interior polar chart take

\[
 B^u=[P,dP]+i aP,\quad a_t=0,\quad
 a_z=s g^2\rho(tz-t^2/2),\qquad \rho\ge0,
\]

where `s=+1` denotes the dagger comparison and `s=-1` the real-literal one. Then `DP=0` and

\[
 G=G_{\rm sphere}+iP\,da,\quad
 (da)_{tz}=s g^2\rho(z-t),\quad
 D^\mu F_{\mu\nu}=s i g^2\rho P(-dt+dz)_\nu.
\]

Unlike a homogeneous no-flux ansatz, this connection has a nonzero trace electric flux whose derivative supplies the central Gauss source.

Use the **same** local probe to generate that current:

\[
 S_0=s g^2\rho(t^2z/2-t^3/3),\qquad
 \Psi_N=V_N\sqrt\rho\,e^{-iS_0-i\phi/2}
               \frac{(0,1,0,-1)}{\sqrt2}.
\]

The spinor and internal orders are those of the prepared four-component Dirac comparison. `V_N` is the Hopf image-line frame from the global-flux note. The south image frame satisfies `V_S=e^{-i phi}V_N`; replacing the spin phase by `exp(+i phi/2)` gives the same coordinate field on the overlap. The polar spin frame itself is singular at the poles. This overlap check is **not** a claimed full global spinor construction or a finite-energy boundary solution.

Compute the spin connection from the same coframe `diag(1,R,R sin(theta),1)`. The angular spin contribution cancels the restricted monopole connection and the half-angle phase. The remaining normal transport vanishes because

\[
 (\partial_t+\partial_z)S_0=a_t+a_z,
 \qquad \alpha^z(0,1,0,-1)^T=(0,1,0,-1)^T.
\]

Here F denotes the **internal gauge/closure curvature**. The Levi-Civita spin connection is additional transport in the Dirac operator; its Lorentz curvature is not included as another internal gauge source. This is the usual separated structure of the declared comparison, not a derived identification of the native full `[D,D]` with these two pieces.

Thus the full **massless** Dirac equation, including the sphere spin connection, is satisfied. The ordered eta load also annihilates this exactly closed probe, so using it in that probe equation changes nothing on this branch. Direct currents are

\[
 j^t=\rho P,\quad j^z=\rho P,\quad j^\theta=j^\phi=0,
 \qquad S=\Psi\beta^T\Psi^\dagger=0.
\]

They are nonzero, null, covariantly conserved and give exactly the connection source above. A null **current of a massless Dirac comparison** is not a photon rest frame or a derived native particle identification. The construction introduces no scalar matter. The assumption `Omega=0` is not obtained from the actual native Millennium/triadic resonance.

A free term `omega(t-z)` may be added to S0 without changing these field equations or currents. Thus the sourced construction does not select a physical frequency or absolute energy scale. On a bounded local patch that freedom can also change the phase's temporal gradient without changing the density.

For context, angular Dirac zero modes with gauge backgrounds on spheres are studied in [Liu, Zhang and Duan, Fermionic Zero Modes in Gauge and Gravity Backgrounds on a Sphere (2007)](https://arxiv.org/html/0709.4369v4). That paper uses a different dimensional setting and does not prove this coupled source solution. Here the four-dimensional spin connection, angular cancellation and sourced field equation are evaluated directly; no index or generation count is imported.

## 7. Full variation checks and the limits of the branch

For these real comparisons the curvature Hermitian part is zero when the axis is constant and `DP=0`. Therefore its first projector/HC variation against anti-Hermitian G vanishes. The state and HC matching penalties have zero first variation on the closed matching branch; a real HC Yukawa term has source S=0 here. These statements use independent unitary connection, projector and compensator variations before substitution, rather than varying a shortened action in which `B^u=[P,dP]+i aP` has already been imposed. They do not supply metric or axis equations, an actual native field dictionary or quantum sources.

At `(t,theta,phi,z)=(0.4,0.9,0.4,-0.2)`, `R=g=1`, `eta=0.7`, `rho=0.4`:

- The full spin-covariant massless Dirac residual has norm about `4.7e-17`.
- Independent curved-coordinate differentiation gives a matrix connection residual about `2.6e-11` against `i g^2 j`.
- Direct Hermitian insertion of the same current instead leaves residual `0.8`.
- Restoring scalar mass `0.6` without changing the fields leaves Dirac residual `0.3794733192=0.6 sqrt(rho)`.

In particular S=0 does not license adding a mass: the mass action can have zero value and still a nonzero probe variation. The construction is a local charged **massless** branch, not a massive repair. Its density, coupling and radius are free comparison inputs. The normal direction carries homogeneous matter and an electric field growing with `z-t`; no global finite total energy is claimed. Stress backreaction is not solved, so the product metric is prescribed, not reconstructed from the probe or Einstein equations.

## Outcome and Reproduction

Nonempty matter makes the missing current dictionary consequential: direct Hermitian and action-derived unitary insertions are not interchangeable. The fixed-M closure gradients do not repair a trace mismatch, and a variable null axis can match a trace in the wrong projector block. A properly typed source nevertheless admits an explicit same-probe charged massless solution in the declared real comparison, so the audit is not a universal exclusion of sourced compatible transport.

The native next obligations are the actual gauge generators and adjoint/action, nonzero mass/triadic resonance, allowed C7 carrier, sourced constraint propagation beyond the fixed sector, global charge/spinor data and metric/axis backreaction. No native action is silently selected or publication claim promoted.

The subsequent [massive HC continuation](HC_Massive_Soft_Closure.md) changes the probe and field profiles together rather than restoring mass in the unchanged chiral solution. A local independent-soft-HC branch solves massive Dirac, charged gauge and HC equations with a nonzero scalar source and explicit existence bounds. A separate hard-dependent real comparison eliminates H=Lambda before variation and retains its equality-constraint reaction, instead of imposing the soft HC equation as well. Both remain declared local comparisons; the native domain, mass/triadic/gauge dictionary and geometric backreaction are not identified.

- [Calculation](HC_Sourced_Closure_Current.py) and [saved results](HC_Sourced_Closure_Current.json).
- Run `python -B analysis/HC_Sourced_Closure_Current.py --output analysis/HC_Sourced_Closure_Current.json`.
- Run `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_sourced_closure_current.py`.

Forty-four focused tests include actual probe/spin/gauge jets, independent current and real-load variations, full sourced matrix equations, the trace-matched wrong-block control, mass restoration and global/native-scope boundaries. They supplement the explicit conditional derivations, not a native empirical or proof-assistant certificate.

No package installation, main-TeX edit, PDF rebuild or Git operation is required for this follow-up.
