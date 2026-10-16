# Projecting the Native Probe Equation onto the Odd Residual

Date: 2026-10-16. Status: an exact conditional projection formula, an autonomy criterion, finite countermodels and a three-chamber obstruction. The native carrier identification and two-mode extraction are still unspecified. This is the next test after [root-phase dynamics](HC_Root_Phase_Dynamics.md), not a solved native phase law. No main TeX, empirical mass, target phase, new potential or publication operation is used.

## Result

An aligned odd projection does keep the omitted bilinear `X3` zero **by the definition of the output**. That does not mean the output has an autonomous equation or stays in its positive-root angle chamber. Differentiating the extraction retains its time dependence and a term driven by the discarded component. Two full states with the same residual, even with the same unit norm, can have opposite residual angular velocities.

The missing closure condition is now explicit. If the resulting two-real-mode dynamics really is a fixed autonomous linear equation, preserving **all three** admitted chambers forces its generator to be a scalar: it may change the common amplitude, but cannot select a phase. A finite unitary rotation preserves oddness, norm and exact closure of a separate `C7` projector yet leaves the positive-root domain. Thus projecting the mode does not itself solve the invariance problem.

This does not exclude native nonlinear field feedback, a separately selected single chamber, a moving physical frame or an evaluated memory reduction. It identifies the terms that must actually be calculated before any of those possibilities can count as the native mechanism.

The next [collective-action reduction](HC_Collective_Action_Reduction.md) retains phase, amplitude and both complementary canonical partners in the same conservative modal action. A positive regular hidden quadratic block can be eliminated to give exact second-order inertia without dropping its initial-state information. The isotropic example yields a reversible amplitude/phase coupling, not viscosity; a separate normal-equation counterexample shows why restricting an action is not yet full-field closure. Native field profiles, background equations and kinetic matching remain to be evaluated.

## 1. The Time Generator Supplied Formally by the Paper

The retained `sources/research/parts/v470/10_sphaera_and_physics.tex`, `thm:master-field-equation`, contains

```text
(i Gamma^mu D_mu-Omega) Psi=0,
D_mu=partial_mu+B_mu,
B_mu=i A_mu+kappa H_C n_mu+eta(I-P_C7)n_mu,
Omega=m0 I+alpha P_C7 M16 P_C7+beta g_Y T_triad+gamma H_C.
```

The repeated field reading in `16_master_model.tex`, `thm:minimal-mmhc-field-equation`, uses the same architecture, with the triadic coefficient packaged differently. Here `H_C` is the positive mismatch **field**, not the projector `C=(I+J)/2`. The native closure projector `P_C7` is not the odd projector `P_-` either. The coefficient `eta` in the connection is not the relative root-readout weight also called `eta` in the preceding analysis.

On a chosen local time chart with invertible `Gamma^0`, multiplication on the left gives the exact formal rearrangement

```text
partial_t Psi=G Psi,
G=-B_0-(Gamma^0)^(-1) sum_a Gamma^a(partial_a+B_a)
  -i(Gamma^0)^(-1)Omega.
```

No derivative, connection or compensator term was discarded. Turning this formal differential operator into a physical Hamiltonian or finite matrix still requires its common carrier, domains, positive adjoint/metric, boundary conditions, gamma realization and modal reduction. The script checks the rearrangement with arbitrary compatible finite matrices; it does not supply those native choices. If a named constituent is only real-linear, use the real-linear generator below rather than silently treating it as a complex matrix.

There is also an unfilled carrier interface: the HC expression is written for a carrier mode `f`, while the field equation is for `Psi`. The equation does not by itself identify their spaces or construct `f=I_native Psi`. The derivation below keeps that identification and its derivative inside the extraction instead of setting it equal to identity without qualification.

## 2. Exact Projected Equation, Including a Moving Extraction

Assume a declared carrier identification `f=I_native(t) Psi`, an antiunitary involution `J(t)`, and a two-mode map `E(t)` aligned with it, `E J=K_complex E` in the local readout frame. Then

```text
P_-=(I-J)/2,
chi=E P_- f=i r,       r in R^2.
```

The odd projection is real-linear, not generally complex-linear. Write the realified probe as `u`, with real generator `G_R`, and collect the complete extraction in a real map `T_read(t)`:

```text
r=T_read u,
T_read u=-i E P_- I_native Psi.
```

Any local two-mode frame and its inverse are included in this formula. `T_read` is not the triadic field `T_triad`, and `G_R` is a time generator, not a Gram or comparison matrix. The product rule gives

```text
r_dot=(T_read_dot+T_read G_R)u.                         (1)
```

In particular `T_read_dot` includes derivatives of `E`, `I_native`, `J` and the readout frame; `P_minus_dot=-J_dot/2`. Neither a label migration nor projector idempotence licenses dropping these derivatives.

For a full-row-rank two-mode extraction choose a real right inverse `R_s`, `T_read R_s=I2`. A convenient finite choice for declared Euclidean comparisons is `R_s=T_read^T(T_read T_read^T)^(-1)`. Decompose

```text
u=R_s r+z,       T_read z=0,
A_read=T_read_dot+T_read G_R,
K_read=A_read R_s,
q=A_read z.
```

Then the exact output equation is

```text
r_dot=K_read r+q.                                     (2)
```

For a fixed instantaneous linear background, an equation independent of the hidden lift exists for **all** input states if and only if

```text
A_read ker(T_read)=0.                                 (3)
```

Necessity follows by comparing two inputs separated by an arbitrary kernel vector; sufficiency follows directly from (2). A different right inverse redistributes the two terms in (2) but does not change the total derivative or criterion (3). If the physical input states occupy only a specified subspace, the test is on differences of allowed lifts in that subspace, not every arbitrary carrier vector. If the background fields depend nonlinearly on the probe, one must compare their full velocities along the same readout fibres instead; a frozen linear factorization does not establish nonlinear autonomy.

Since the **output** is `chi=i r`, `X3=2Im(conj(chi_1)chi_2)=0` at every time for which the extraction is aligned. The unprojected field need not be odd. This is why the previous freely complex two-mode saddle does not automatically apply to the projected output. It also explains why simply replacing that saddle equation by its compressed generator would lose a term rather than derive a native law.

## 3. A Fixed-Frame Hermitian Example Makes the Missing Term Visible

Use a separately declared positive two-mode realization, fixed `J=conjugation`, and `f_dot=-i H f`, with Hermitian `H`. Split

```text
H=S+iB,       S^T=S real,       B^T=-B real,
f=x+i r.
```

Multiplication gives exactly

```text
x_dot=B x+S r,
r_dot=B r-S x.                                       (4)
```

The compressed generator on the odd part is `B`, but the actual derivative includes `-S x`. Therefore the odd readout is autonomous for all hidden inputs exactly when `S=0`. Equivalently

```text
J H J^(-1)=-H,
```

not `J H J^(-1)=H`. For an antiunitary `J`, its action changes the sign of `i`; commutation with a Hamiltonian is not the same as preservation of its odd subspace at the same time. The inherited unitary and antiunitary conventions cannot be interchanged here. This statement is also distinct from invariance of a complex-linear odd eigenspace in the earlier seed construction.

For an explicit normalized ambiguity witness choose `H=diag(1,2)`, `r=sqrt(0.96)(1/2,sqrt(3)/2)` and `x=+/- (0.2,0)`. Both full states have norm one and exactly the same nonzero residual. Their invariant-phase velocities are nevertheless opposite, `Phi_dot=+/-1.06066017178` in declared dimensionless time. No function of that residual alone can supply both derivatives.

Even `x(0)=0` does not justify deleting the hidden term for later times. With the same real diagonal `H`, one has

```text
r_j(t)=r_j(0)cos(H_jj t),
r_dot(0)=0,
r_ddot(0)=-S^2 r(0).
```

The even component is immediately generated by `x_dot(0)=S r(0)` and returns to the residual at the next order. For a scalar Hamiltonian this is a common-amplitude oscillation, reaching zero residual at `t=pi/(2|H|)` despite unit norm of the full state. It is a test of this residual readout and its fixed real structure, not a prediction that physical lepton masses vanish periodically.

For constant operators one can keep the hidden dynamics exactly rather than guess friction:

```text
x(t)=exp(Bt)x(0)+integral_0^t exp(B(t-s)) S r(s) ds,
r_dot=B r-S exp(Bt)x(0)
      -integral_0^t S exp(B(t-s)) S r(s) ds.            (5)
```

This is a memory equation with an initial-state source. A finite skew `B` generates orthogonal `exp(Bt)`, not an automatically decaying memory kernel. Obtaining an irreversible, local gradient/friction law requires an independently justified coarse-graining, spectrum, bath or other field dynamics. Merely projecting a closed unitary equation does not supply the earlier positive mobility.

## 4. Moving Frames, Positive Damping and the Separate Closure Projector

Let `f=V(t) local_f` with unitary `V`, and `J=V K_complex V*`. In the local frame the Hermitian Hamiltonian is

```text
H_local=V* H V-i V* V_dot.                            (6)
```

The connection term matters even for a common scalar phase. For `H=I` and a frame satisfying `V_dot=-iV`, it cancels the scalar Hamiltonian and leaves constant local residual coordinates. A fixed real structure gives the oscillating residual in section 3 instead. Choosing a real structure to track a solution is not a derivation of the native physical frame; the frame and readout comparison must be transported consistently and specified independently of desired masses.

More generally, for a differentiable real orthogonal projector `P(t)`, preserving an initially projected state under `f_dot=G f` requires

```text
(I-P)G P=P_dot P.                                    (7)
```

Indeed differentiating `(I-P)f=0` yields this condition. For fixed antiunitary odd `P_-` in the special Hamiltonian case it reduces to the sign condition in section 3. For `P_C7`, it is a separate compatibility condition involving the whole generator and a moving closure field. `[M16,P_C7]=0` only controls the Millennium term; it is not automatically (7) for the full connection, triadic field, gamma action and spatial derivatives.

The source **does** contain the temporal piece `-kappa n_0 H_C` in `G`. It cannot be isolated as the complete attenuation law, however: the spatial connection and resonance term contain the same field. Keeping their matrix order gives the full displayed contribution

```text
G_HC=-(Gamma^0)^(-1)[kappa Gamma^mu n_mu+i gamma I] H_C. (7a)
```

Positivity of `H_C` alone does not make the Hermitian part of this generator nonpositive. A sign, gamma/frame, spin/internal commutation and physical-adjoint analysis is needed. For example, on a declared two-dimensional algebraic carrier, `Gamma^0=sigma_z`, `Gamma^1=i sigma_y`, `n=(1,1)` satisfy the `1+1` Clifford identities of signature `(+,-)`. Then `(Gamma^0)^(-1)Gamma.n=I+sigma_x`. With `gamma=0`, `kappa=1`, the positive field `H_C=diag(1,4)` does not commute with that factor; the Hermitian part of `G_HC` has a positive eigenvalue. With a scalar commuting field the same coefficient instead gives semidefinite attenuation. This is a test of missing commutation/adjoint premises, not a native noncommuting spin/internal realization or a claim that a properly factorized native field amplifies norms.

These algebraic signs are not a computed viscosity or time scale. In the minimal exactly closed source system, `H_C=Lambda=0`, so the **whole** contribution (7a) vanishes. The condition `(I-P_C7)Psi=0` also kills its direct on-sector penalty. A nonzero mismatch-field damping cannot then be invoked on that exact sector. Other spatial, connection and coarse-grained field effects require their own evaluation.

A controlled finite specialization is `G=-iH-D`, with Hermitian `H` and positive Hermitian `D`. Write `D=C+iE`, with real symmetric `C` and real skew `E`. The real block equations now have local generator `B-C` and hidden coupling `-(S+E)`. Since a symmetric matrix cannot cancel a skew one, autonomous odd dynamics for all hidden inputs requires

```text
S=0,       E=0,
r_dot=(B-C)r.
```

Its norm derivative is `-2r^T C r<=0`. If `C=cI`, attenuation changes the amplitude but adds no angle force. Anisotropic constant damping can select a direction and preserve a **single** chosen chamber; for example `r_dot=-diag(0,1)r` preserves the chamber centered at zero but fails a boundary guard in each of the other two. A physical choice of one branch would therefore be additional input, not a consequence of positivity alone.

## 5. Exact Angular Velocity and the Three-Chamber Theorem

For any nonzero real residual, including a forced or time-dependent one, set `theta=2 arg(r_1+i r_2)` continuously on its current branch. Direct differentiation gives

```text
(r.r)_dot=2r.r_dot,
theta_dot=2det(r,r_dot)/(r.r),
Phi_dot=6det(r,r_dot)/(r.r).                           (8)
```

At `r=0` neither angle nor a nonzero root scale is defined. One cannot normalize this away in an invariance proof. The three positive-root intervals in `theta` have centers `2pi j/3` and half-width `pi/12`. At a zero-root boundary the derivative of the common amplitude drops out of the zero eigenvalue; its preservation is exactly the inward angular sign condition.

Now assume an autonomous, state-independent real linear law `r_dot=K r` with fixed `2x2` matrix `K`. Define

```text
omega=(K21-K12)/2,
c=(K21+K12)/2,
d=(K22-K11)/2.
```

Equation (8) reduces to

```text
theta_dot=v(theta)=2[omega+c cos(theta)+d sin(theta)]. (9)
```

**Theorem.** If this law preserves the union of all three positive-root chambers for every nonzero admitted initial residual, then `K=aI`. Conversely every such scalar generator preserves all chambers and only changes amplitude. With norm preservation, `K=0`.

**Proof.** Continuity prevents a trajectory from jumping between separated angle intervals. At the left and right endpoints of every interval, invariance requires `v(left)>=0` and `v(right)<=0`. By the intermediate value theorem, each of the three disjoint intervals contains a zero of `v`. A nonzero function of the form `omega+c cos(theta)+d sin(theta)` has at most two distinct zeros modulo `2pi`: if its oscillating amplitude is nonzero, this is the intersection of a cosine with a horizontal line; if that amplitude vanishes, a nonzero constant has no zeros. Therefore `v` vanishes identically. The three coefficients are zero, giving `K12=K21=0` and `K11=K22`. A scalar generator is norm preserving for all residuals only when its real scalar is zero. This proves both directions. Nonzero linear trajectories cannot pass through the origin in finite time to bypass the angle intervals.

The theorem does **not** prohibit a physically selected single chamber, state-dependent coefficients, a larger carrier with retained hidden variables, a nontrivial induced frame, nonlinear field feedback or another readout. For a linear generator that varies with time, the same restriction follows if these guards are demanded at every time for every admitted initial state at that time. It is not an assertion about just one specially prepared trajectory.

There is an explicit finite counterexample to sufficiency of oddness, norm and separate exact closure. On three complex coordinates take

```text
P_C7=diag(1,1,0),       M=diag(1,2,3),
H=diag_block(omega sigma_y,0),       omega>0,
f(0)=i(1/2,sqrt(3)/2,0).
```

Then `[M,P_C7]=[H,P_C7]=0`, the minimal mismatch functional is zero, the state is closed, norm one and conjugation-odd for all times. Nevertheless `theta_dot=2omega`, so it reaches the root boundary at `t=pi/(24omega)` and then leaves. The script continues a little beyond it and obtains a negative signed root while all listed closure conditions remain exact. Reducing `omega` delays but never prevents that exit. This is a finite interface witness, not the actual native sixteen-dimensional Millennium realization, the Riemann clock, or a solution of the full coupled field equations.

## 6. What the Native Operator Must Now Satisfy

Combining (1) and (8) gives an actual evaluation target, not a guessed phase potential:

```text
Phi_dot=6det(r,(T_read_dot+T_read G_R)u)/(r.r).          (10)
```

At `Phi=-pi/4` it must be nonnegative; at `Phi=+pi/4` it must be nonpositive for every physically admitted lift with that boundary residual. The boundary condition must be checked on the specified full state/background, not only on the compressed matrix. Usual uniqueness/regularity and nonzero-residual conditions are still required to turn local guards into a flow-invariance statement.

There is a useful quantitative version. For `r_dot=K r+q`, if an independently established bound gives `||q||<=epsilon||r||`, Cauchy-Schwarz implies

```text
|delta theta_dot|<=2epsilon,
|delta Phi_dot|<=6epsilon.
```

The bounds are attained by a tangential force `q=+/-epsilon A r`, `A=[[0,-1],[1,0]]`. Robust preservation against **all** forces in that ball thus requires the unforced theta velocity to be at least `2epsilon` at every left edge and at most `-2epsilon` at every right edge. The previously added gradient law has zero boundary force; it has no nonzero uniform margin against arbitrary hidden forcing.

For a declared coisometric extraction and a unit-norm full state, the orthogonal kernel decomposition gives

```text
||q||/||r|| <= ||A_read(I-R_s T_read)|| sqrt(1-||r||^2)/||r||.
```

Even unit normalization supplies no uniform relative-force bound as the residual approaches zero. A source/hidden-population bound or lower residual support must be calculated, not inferred from normalization alone.

To recover precisely the earlier constant-norm gradient phase dynamics, the native expression would have to meet

```text
(T_read_dot+T_read G_R)u=-(m/6) F'(Phi) A r,       m>0. (11)
```

If only the angle is matched, an additional radial term `a r` is invisible in (8), but scale support and any changing source ratio still need analysis. Since the coefficient in (11) depends on the phase, it is not a fixed linear two-mode generator. The coupled native fields could in principle provide such dependence; no evaluated native matrix or equation here supplies it yet.

The remaining inputs are now sharply identified: the common field/carrier realization, aligned extraction and its time dependence, the full generator on that domain, allowed hidden lifts/background and the resulting boundary signs. The native `eta=1` metric transfer, transition-Gram equality, physical mass/gauge/current law and scale remain separate obligations. This calculation does not claim that native closure, C5 or a mass spectrum has been solved.

## Reproduction

Run `python -B analysis/HC_Projected_Residual_Dynamics.py --output analysis/HC_Projected_Residual_Dynamics.json`. The 40 tests in `scripts/qsc_audit/tests/test_hc_projected_residual_dynamics.py` cover the native-equation rearrangement and complete HC contribution, realification, exact hidden-term factorization, same-readout ambiguity, Hamiltonian block equations and memory return, moving-frame terms, damping restrictions, angular formula/harmonic structure, closure-preserving escape, robust force bounds, guards and independence from historical masses. The memory integral is checked against exact finite unitary propagation, not a guessed decay law. All examples use already installed NumPy. No package, main-TeX edit, compiler run or Git operation is required for this analysis-only follow-up.
