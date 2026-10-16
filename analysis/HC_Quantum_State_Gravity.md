# Quantum-State Sources and a Sourced Null HC Comparison

Date: 2026-10-16. Status: exact scalar source identities, a first-order massive interference response and a local solution of an explicitly enlarged neutral parent. This is not a native HC operator identification, a derivation of particle masses or a complete renormalized semiclassical solution. The main TeX is unchanged by this continuation.

## Result

The question "could quantum properties, rather than a mass number alone, determine curvature?" has a precise, limited affirmative answer: states with the same field mass and total energy can have different local stress tensors. A relative phase can change that tensor and its gravitational response; an overall constant phase cannot. This uses the usual stress coupling, not an extra coupling to a physically unobservable phase.

Two distinct constructions are kept separate:

1. A massive free complex scalar has a phase-coherent one-particle superposition, its dephased mixture, and an exact, conserved flat-space stress difference. An explicit metric perturbation solves all **linearized** Einstein components for that difference. This does not solve the positive homogeneous source or the full nonlinear massive problem.
2. An additional minimally coupled **massless** scalar can source the previously declared neutral HC parent. Its source changes the transverse profile equation from Laplace to Helmholtz form after the exponential substitution. A positive local cosine branch solves all equations of that enlarged action, including the background-dependent axis equation. It is not the native massive triadic matter sector.

Neither construction shows that genuinely quantum correlations are the sole origin of gravitation. The same phase-sensitive stress can occur in classical coherent waves. The original mass parameter, Newton coupling and native HC dictionary are not derived.

## 1. A Source From a Common Metric-Dependent Action

Use signature `(-,+,+,+)` and dimensionless comparison units. Declare a complex scalar field with

```text
S_phi=-integral sqrt|g| [g^{mu nu} partial_mu phi* partial_nu phi+m^2 |phi|^2],

(Box_g-m^2)phi=0,
T_mu_nu=2 Re(partial_mu phi* partial_nu phi)
        -g_mu_nu [|d phi|_g^2+m^2 |phi|^2].                       (1)
```

The two real components have the normalization of this complex action, without an additional factor `1/2`. Varying the inverse metric before imposing any null ansatz gives `delta S_phi=-integral sqrt|g| T_mu_nu delta g^{mu nu}/2`. Varying the complex field gives its Klein--Gordon equation. Direct differentiation gives the off-shell identity

```text
nabla^mu T_mu_nu=2 Re([(Box_g-m^2)phi]* partial_nu phi).             (2)
```

Thus the source is covariantly conserved on shell. It is not an independently chosen phase force. Writing `phi=A exp(i S)` shows its amplitude gradients and phase gradients explicitly:

```text
T_mu_nu=2 partial_mu A partial_nu A+2 A^2 partial_mu S partial_nu S
        -g_mu_nu[(d A)^2+A^2(d S)^2+m^2 A^2].                     (3)
```

A constant common phase changes none of (1)--(3). A spacetime-dependent phase is not a free gauge equivalence of this ungauged scalar action; adding a gauge symmetry would require its connection and covariant derivatives. Relative phases between modes of the same field can change (3). Independent orthogonal fields with a diagonal uncoupled kinetic action instead have a sum of stresses, without such cross terms. An ART/QFT label alone does not authorize interference in the native stress.

## 2. Actual Quantum States With Fixed Mass and Energy

On a flat periodic box of side `2 pi`, volume `V=(2 pi)^3`, choose two positive-frequency modes

```text
p=(-E,1,0,0),     q=(-E,0,1,0),     E=sqrt(1+m^2),     m=0.6,
u_r(x)=exp(i p_r.x)/sqrt(2 E V),
c=(sqrt(0.8),sqrt(0.2) exp(i delta)).                              (4)
```

They obey `p^2=q^2=-m^2`. Compare the normalized particle state `|psi>=c_1 |1_p>+c_2 |1_q>` with its mixture of populations `0.8,0.2`. Both have one particle, the same field mass and the same total energy `E`. Their number covariance is respectively `N_rs=conj(c_r)c_s` and its diagonal part. With a flat-vacuum normal ordering and no antiparticle occupation, the particle-sector stress expectation is

```text
<:T_mu_nu:>=sum_rs N_rs u_r* u_s C_rs,mu nu,
C_rs,mu nu=p_r,mu p_s,nu+p_s,mu p_r,nu
            -eta_mu_nu (p_r.eta.p_s+m^2).                         (5)
```

**Proof.** Expand the free complex field into particle annihilators and antiparticle creators. After the stated vacuum subtraction, the populated particle contribution is `a_r^dagger a_s`; applying the derivatives in (1) gives (5). The independent finite-Fock-space test constructs both annihilator matrices, the one-particle state and the normal-ordered quadratic stress operator. It does not infer the quantum expectation merely by assigning a classical field name.

The one-particle field mean is zero, even though (5) is nonzero. The function `f=sum c_r u_r` reproduces its quadratic stress, but is **not** that state's field expectation. A bosonic coherent state with the same mode amplitudes has the same number covariance and the same normal-ordered mean stress, while its higher moments differ. Equal mean stresses do not identify quantum states or certify the validity of a mean-source gravitational approximation.

At the box origin, in the declared dimensionless normalization:

```text
m                         = 0.6 for all delta
mean particle number      = 1 for all delta
total box energy          = 1.16619037896906 for all delta
T_00(delta=0)             = 0.007079798430679832
T_00(delta=pi)            = 0.00232305886006682
T_00(dephased mixture)    = 0.004701428645373326
```

The interference integrates to zero over the box. This changes the local energy distribution, not the total energy or the mass parameter. Averaging uniformly over relative phase gives the mixture. Common rephasing leaves `N` and every stress component unchanged.

## 3. A Controlled Massive Gravitational Response

Let `delta T` denote the coherent stress minus the mixture stress, not the complete positive source. Define `Q=q-p=(0,-1,1,0)`, so `Q^2=2`. Equation (5) gives

```text
delta T=2 Re(conj(c_1)c_2 u_1* u_2) C_12,
Q^mu delta T_mu_nu=0,       Box delta T=-Q^2 delta T.              (6)
```

Here `u_r` in (4) does not include `c_r`. The conservation follows directly from `p^2=q^2=-m^2`: contracting the two outer products in `C_12` with `Q` cancels its metric term. In harmonic gauge the trace-reversed perturbation has the particular solution

```text
Box bar_h_mu_nu=-2 kappa_eff delta T_mu_nu,
bar_h_mu_nu=2 kappa_eff delta T_mu_nu/Q^2,
h_mu_nu=bar_h_mu_nu-eta_mu_nu Tr_eta(bar_h)/2.                      (7)
```

The written conservation identity enforces the harmonic gauge. Independent evaluation of the full linear Einstein tensor verifies `G^(1)=kappa_eff delta T`, with sample residual about `3.07e-19` at `kappa_eff=0.2`. Expanding the nonlinear Levi--Civita calculation at successively smaller perturbations independently confirms first-order convergence.

This is a zero-mean **difference response**, not an exact nonlinear metric for the massive state. The diagonal, positive, spatially homogeneous source has not been solved on the flat periodic background. In fact substituting the complete stress into (7) leaves precisely `-kappa_eff T_mixture`. Infinite plane waves/periodic boundaries do not supply an isolated asymptotically flat object. Curved-space mode corrections and source backreaction are higher-order obligations, not absent equations.

## 4. An Exact Sourced Extension of the Neutral Null Parent

Take the explicit [derived-background parent](HC_Derived_Background_Curved_Parent.md), with independent fields `Psi,E,h,u,lambda,zeta`, its fixed reference-Dirac action, `Theta=dY[Psi]`, `u=n.Y[Psi]`, and scalar two-form `F=kappa dh wedge du`. Add an **independent** complex scalar `phi` and the massless action (1) using the same effective metric `g(E)` as the Einstein and two-form terms:

```text
S_new=S_old+S_phi[g(E),phi],     m_phi=0.                          (8)
```

No `phi=f(u)` restriction is inserted before variation. The independent metric equation now contains `T_F+T_phi`, and the added field has its full Klein--Gordon equation. The previous `h,u`, constraints and probe reactions retain their forms because `phi` is independently varied, not a prescribed functional of `u` off shell.

Only afterward set `phi=f(u)` and use, in the `Y` chart,

```text
u=-Y^0+Y^3,     g=eta+2 kappa h(u,Y^1,Y^2) du tensor du,
rho(u)=2 |f'(u)|^2,     T_phi=rho(u) du tensor du.                 (9)
```

The null covector `du` is parallel. Functions of `u` obey `Box_g f(u)=0`. The HC two-form loses the longitudinal term `h_u du wedge du`, so its stress remains `kappa^2 |grad_perp h|^2 du tensor du`. The unrestricted Einstein tensor is `G=-kappa Delta_perp h du tensor du`, even for `u`-dependent `h`. All other Einstein components vanish. The full equation therefore requires

```text
Delta_perp h+kappa_eff kappa |grad_perp h|^2
    =-kappa_eff rho(u)/kappa.                                    (10)
```

This changes the source equation; appending matter to the old unsourced logarithmic solution would not work. Put `a=kappa_eff kappa != 0` and `w=exp(a h)`. Direct differentiation yields

```text
(Delta_perp+kappa_eff^2 rho(u)) w=0.                             (11)
```

For `kappa_eff>0`, one positive local witness is

```text
w=F0 cos(kappa_eff sqrt(rho(u)) Y^1),
h=log(w)/(kappa_eff kappa),     F0>0,
|kappa_eff sqrt(rho(u)) Y^1|<pi/2.                              (12)
```

The square-root expression is evaluated on a positive-flux patch. An identically zero source admits the constant positive harmonic `w=F0`. The cosine zero is a boundary of this local branch, not a demonstrated physical horizon or singularity of the native theory. Other boundary data give other Helmholtz solutions; (12) is not uniquely selected by the source.

**Remaining equations.** Writing `p=dh`, `q=du`, one still has `q^2=p.q=0` and `div(p^2 q)=0`, since all data are independent of the conjugate null coordinate. Hence both allowed HC scalar equations hold, including the varied axis-potential equation. A freely varied covector axis would still have a nonzero algebraic reaction: the declared field space matters. Set `E=(I+kappa h l n^T)Theta`, `lambda=zeta=0`; the two constraints hold, the independent metric equation has just been solved, and the original reference-Dirac probes stay on shell with zero multiplier reaction. Pulling all fields back through the nondegenerate `Y[Psi]` preserves the equations, rather than adding components from different frames.

At the previous cross-readout sample `(0.01,0.02,-0.03,0.01)`, `kappa=0.4`, `kappa_eff=1`, the independent curvature computation gives Einstein residual about `1.80e-11`, matching its pullback cancellation error. The reference-Dirac residual is `1.38e-15`, Klein--Gordon residual about `9.10e-13`, and both HC scalar residuals are below `4e-16`. These are coordinate implementation checks; the identities above establish the branch. The near-degenerate cross chart amplifies numerical cancellation as in the previous analysis.

For an explicit phase comparison choose

```text
f(u)=0.3 exp(-i u)+0.1 exp(i delta) exp(-2 i u),
rho(u)=2[0.3^2+0.2^2+2(0.3)(0.2) cos(delta-u)].                 (13)
```

The mode populations are fixed. At `u=0`, `rho=0.5` for `delta=0` and `rho=0.02` for `delta=pi`. At `Y^1=0`, where the HC transverse gradient vanishes, the coordinate Ricci coefficient changes by a factor of 25. This number belongs to these chosen dimensionless amplitudes, not a physical prediction or a source-free gravitational effect. Interference changes the actual local stress.

## 5. Why This Is Not Yet the Native Massive Solution

The exact construction has **added a scalar carrier**. It has not derived that carrier from the native triadic spinors. In particular the old massive reference probes still do not gravitate as ordinary matter through `g(E)` in this action. Only the newly declared scalar has the common metric-dependent matter coupling. The previous native HC-current span and microscopic/effective light-cone obstructions remain; none of their hypotheses was repaired by this extra field.

Nor may the exact null wave be relabeled massive. For unchanged `phi=f(u)`,

```text
(Box_g-m^2)f(u)=-m^2 f(u),
delta T_mu_nu=-m^2 |f|^2 g_mu_nu.                               (14)
```

For nonzero `m,f`, both the scalar equation and the purely null stress shape fail. The added transverse stress cannot be balanced by the old pure-null Einstein tensor. This excludes that unchanged ansatz, not every massive solution, nonminimal action or different geometry. The massive construction in Sections 2--3 and the exact massless null branch are different results and must not be combined into a claimed exact massive solution.

The actual native next step is to derive an allowed common metric/readout and stress operator for the original probes, including their mass/Yukawa, gauge, closure and projector reactions, then solve the resulting coupled equations. Declaring mass to be emergent does not determine any of these operators or remove their stress. No physical mass, Newton constant, equivalence principle or quantum origin of geometry has been computed here.

## 6. Quantum Interpretation and Literature Boundary

For a free scalar on a **fixed** geometry, displacing a zero-mean reference state by a smooth classical solution gives

```text
<T>_displaced,ren-<T>_reference,ren=T_classical[f].               (15)
```

This follows by shifting the field operator by `f`: the linear terms vanish in the zero-mean reference and the quadratic c-number term is (1). State-independent local subtraction terms cancel in this difference. A complex scalar can be treated as two real fields with the stated normalization. Suitable states, smooth solutions and local/Hadamard admissibility are assumptions; the infinite plane-wave examples are not normalizable whole-space coherent wave packets.

Equation (15) does **not** set the reference vacuum stress to zero on a curved geometry. A fully renormalized semiclassical solution also needs its geometry-dependent reference stress, renormalized gravitational counterterms, state preparation and a controlled stress-fluctuation regime. None was evaluated for (12). A one-particle state and a coherent state can share (5) but have different fluctuations; the finite tests do not certify mean-source gravity for either physical system.

Relevant external foundations, not native-theory certificates:

- [Hu and Verdaguer, *Stochastic Gravity: Theory and Applications*, Section 3.1](https://arxiv.org/html/0802.0658v1#S3.SS1): a semiclassical solution requires the geometry, field equation and admissible state together, with a conserved renormalized stress expectation; local curvature counterterms and stress fluctuations matter.
- [Ahmed, Lima and Martin-Martinez, *Semiclassical gravity beyond coherent states*, Sections II--IV](https://arxiv.org/html/2310.16289v1): scalar stress, mode quantization, coherent-state displacement and the distinction between stress means and higher moments. Its conclusions about selected quantum states do not validate the native HC sector or our unevaluated curved reference state.

These established tools motivate the declared comparison. The Helmholtz reduction and the two-mode examples above are worked out explicitly here. No new claim that phase-sensitive gravity is unknown in standard physics is made.

## 7. Reproduction

`python -B analysis/HC_Quantum_State_Gravity.py --output analysis/HC_Quantum_State_Gravity.json` reproduces the numerical report. Thirty-two focused tests cover independent metric and field variations, the off-shell Ward identity, finite-Fock operators, state/mode normalization, phase invariance and dephasing, fixed total energy, all linear Einstein components and nonlinear first-order convergence, sourced profile jets and all enlarged-parent equations, plus mass-restoration and missing-source negative controls. They use the existing NumPy installation.

The proofs and first-order versus exact scope remain essential. These tests are not an empirical result or a proof-assistant certificate. No new main-paper theorem or release claim is adopted.
