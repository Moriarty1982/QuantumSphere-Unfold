# Two Frames, a Common Action and an Explicitly Modified Local Branch

Date: 2026-10-16. Status: exact conditional trace/variation identities and a local solution of an explicitly changed neutral massless parent model. This is not a native solution, an adopted coframe correction or a new main-TeX section.

## Result

Separating microscopic and effective frames does not automatically remove the [previous trace obstruction](HC_Bilinear_Geometry_Bridge.md). Keeping the unchanged real bilinear coframe and the same reference-frame master equation with real mass bilinear requires a **zero mixed frame trace**. It excludes coframes close to the reference identity in their declared common spin frame, but is not an invariant lower bound on metric curvature or a no-go for all distinct frames.

A multiplier action makes the needed common variation explicit. It does not automatically imply an independent Einstein equation: its multiplier can balance the metric Euler tensor and react back on the probe.

One genuine change can be tested constructively: replace the coframe dictionary `E=C[Psi,H]` by the affine dictionary `E=theta+C[Psi,H]`, with a fixed reference coframe `theta`. A constant null-current massless probe then realizes the same curved null metric without the old expanding current. In a declared **neutral scalar-HC parent**, a positive affine harmonic function generates a local family satisfying every declared Euler--Lagrange equation. Restoring the native mass/Yukawa term, charged gauge source or zero-target matching penalty invalidates this unchanged family. The extra background and omitted sectors are real changes, not a tensor-tag activation or a completed native derivation.

## 1. What Two Different Frames Actually Require

Let `theta^a_mu` be a real invertible reference coframe, `f=theta^(-1)`, and use a common specified spin frame:

```text
Gamma_ref^mu=f_a^mu Gamma^a,
E^a_mu=s Re[bar(Psi)Gamma^a D_mu Psi],      s real and nonzero,
R_ref=(i Gamma_ref^mu D_mu-Omega)Psi,
w=bar(Psi)Omega Psi.
```

Taking the imaginary part gives the exact identity

```text
Im[bar(Psi)R_ref]=Tr(E theta^(-1))/s-Im w.                 (1)
```

**Proof.** Contract the coframe definition with the real inverse reference frame. The contraction equals `s Re[bar(Psi)Gamma_ref^mu D_mu Psi]`. Multiplication of the residual by the same adjoint, followed by `Im(iz)=Re z`, proves (1).

Thus real `w` and the unchanged on-shell microscopic equation require

```text
A=E theta^(-1),       Tr A=0.                            (2)
```

For an ordinary four-dimensional real matrix, Cauchy and the spectral norm inequality give

```text
4=|Tr(A-I)| <= 2 ||A-I||_F <= 4 ||A-I||_op.              (3)
```

Consequently `||A-I||_F>=2` and `||A-I||_op>=1`. In particular `E=c theta` cannot satisfy (2) for nonzero `c`. The numbers refer to this dimensionless relative coframe, not a physical gravitational strength or Planck distance. Simultaneous coordinate changes preserve `A`; a common spin-frame basis change conjugates it. Ordinary Euclidean frame norms are not Lorentz-invariant metric distances.

An essential negative control is `A=diag(1,1,-1,-1)`: its trace is zero, determinant is one, and `A^T eta A=eta`. A large relative coframe change need not mean a different metric. Independent rotations of the two spin frames cannot be made without also declaring how their gamma matrices and probe dictionary are compared.

The script also constructs a full-rank reference on-shell **first jet** with trace approximately `1.55e-15` and probe residual approximately `6.71e-16`. It solves the reference equation at one point by choosing its time derivative; it is not a global field solution or a constructive solution of all geometry equations. It confirms why the same-induced-frame exclusion must not be generalized to every reference-frame interpretation.

Simple averaging does not erase (2): with a common fixed reference comparison and real on-shell bilinears, linear averaging commutes with this trace. A genuinely different coarse-graining, changed equation or independent collective observable needs an evaluated map, not just a new name for the same coframe.

## 2. A Parent Action Exposes the Backreaction

For fixed external `theta` and a chosen background `Ebg`, define a candidate parent

```text
S_parent=S_micro[Psi;theta]+S_geom[E,H]
         +integral d^4x lambda_a^mu (E^a_mu-Ebg^a_mu-C^a_mu[Psi,H]).       (4)
```

`lambda` is a real multiplier **density**. `S_geom` includes the metric-dependent HC action, not only the Einstein term. All fields, adjoints, boundaries and functional versus independent HC rules must be declared. This is a variational construction, not a claim that the native complex ordered action already has this real form.

Writing `pi_E=delta S_geom/delta E`, independent variations give

```text
E-Ebg-C=0,
pi_E+lambda=0,
EL_micro-(D_Psi C)^*lambda=0,
EL_H,geom-(D_H C)^*lambda=0.                              (5)
```

The adjoint of `DC` includes integrations by parts when `C` uses derivatives. Eliminating `E` and `lambda` yields precisely the composite-action chain rule, for example

```text
EL_Psi,composite=EL_micro+(D_Psi C)^*pi_E.                 (6)
```

Equations (5) do **not** force `pi_E=0`: a nonzero multiplier can balance it. Conversely, taking an Einstein solution with `pi_E=0` also requires the probe and HC equations, and fixes `lambda=0`. This identifies exactly what must be checked rather than discarding normal equations after imposing an ansatz.

For a fixed Hermitian scalar/internal factorization with one scalar HC direction, the phase-blind dictionary is

```text
C^a_mu=s partial_mu j^a/2+s kappa h n_mu j^a,
j^a=Psi^dagger K^a Psi,       (K^a)^dagger=K^a.           (7)
```

Its multiplier coupling, integrated by parts, is

```text
-lambda.C = Psi^dagger V_lambda Psi + total derivative,
V_lambda=s[(partial_mu lambda_a^mu)/2-kappa h lambda_a^mu n_mu]K^a.       (8)
```

This weight is Hermitian for real `lambda,h,n,kappa,s`. A real mass-like reaction therefore does not automatically supply the missing imaginary mass bilinear of the original same-derivative trace test. When curvature contributes through a **phase-blind** `C`, it also does not create an extra central phase current. A different real probe law may drop the ordered HC term, as already shown in the [current analysis](HC_Real_Probe_Current_Closure.md); that is a different equation and must not be substituted into (1) with the old derivative unnoticed.

The periodic variational test checks (8) by independently varying `-lambda.C` and comparing to its Euler derivative, including the spatial derivative of `lambda`. A nonlinear finite parent/composite example independently checks the signs in (5)--(6).

## 3. A Background Coframe Changes the Identity, Not Just Its Notation

Now make the explicit additional choice

```text
E=theta+s Re[bar(Psi)Gamma^a D_mu Psi].                  (9)
```

For the reference master equation, (1) becomes

```text
Im[bar(Psi)R_ref]=[Tr(E theta^(-1))-4]/s-Im w.             (10)
```

If the induced inverse frame is instead used in that same algebraic equation, its corresponding identity is

```text
Im[bar(Psi)R_induced]=[4-Tr(E^(-1)theta)]/s-Im w.          (11)
```

The background contraction is the actual change. It is absent from the inherited `E=C` definition. An affine coframe can now be nondegenerate with zero bilinear term, and can admit small traceless relative corrections. It does not by itself solve a probe equation or derive where `theta` comes from. No literal background coframe term was found in the retained reconstruction; the earlier geometry note listed it only as a possible model change. It must not be presented as an already established consequence of the QAM namespace shift or tensor activation.

## 4. An Explicit Local Solution of a Modified Neutral Parent

There is a nontrivial example where the new possibility can be carried through **all equations of its declared action**, not only an Einstein/stress comparison. It deliberately does not restore the native charged/mass/closure package.

Fix the Cartesian reference coframe `theta=I` and covector `n=(-1,0,0,1)`. Independent variables are a real nonsingular coframe `E`, a real scalar `h`, one commuting complex four-spinor `Psi` and real multiplier density `lambda`. The fixed data `theta,n,K^a` are not varied. Set `g=E^T eta E` and

```text
S = integral d^4x (i/2)[Psi^dagger K^mu partial_mu Psi
                       -(partial_mu Psi^dagger)K^mu Psi]
    +integral d^4x sqrt|g| [R(g)/(2 kappa_eff)-F_mu_nu F^mu_nu/4]
    +integral d^4x lambda_a^mu(E^a_mu-theta^a_mu-C^a_mu),

F_mu_nu=kappa[(partial_mu h)n_nu-n_mu partial_nu h],
C^a_mu=Re[Psi^dagger K^a partial_mu Psi]+kappa h n_mu Psi^dagger K^a Psi.  (12)
```

This is a neutral scalar-HC two-form, **not** an independent electromagnetic/Yang--Mills connection coupled to a charged spinor. There is no gauge `A` variation or Gauss equation in this deliberately smaller field space. There are no mass, Yukawa, matching-penalty or projector fields. The probe kinetic term uses the fixed reference volume and gamma matrices, not the induced metric. These choices specify an alternative classical effective comparison; they do not define the native theory or quantum fermion expectation values.

Use `K^a=(I,alpha_i)` and `beta,Gamma^a` as in the prior explicit four-spinor test. With `l=(1,0,0,1)`, choose

```text
Psi=(1,0,1,0)/sqrt(2) constant,       j^a=l^a,
lambda=0,
E=I+kappa h l n^T,
h=log(F0+b_x x+b_y y)/(kappa_eff kappa),
F0+b_x x+b_y y>0,       kappa!=0,       kappa_eff>0.      (13)
```

Restrict further to `h>=0` if a positive compensator amplitude is desired. The coefficients are independent dimensionless inputs, not fitted lepton data or a derived Newton/Planck scale.

**Coframe/multiplier equations.** The constant spinor has zero derivative and null current `l`, so `C=kappa h l n^T` and the entire 16-component coframe constraint holds. `det E=1`, `det g=-1`, and `g=eta+2 kappa h nn^T` has the same null axis. The coframe Euler equation follows from the independent metric equation below when `lambda=0`.

**Probe and adjoint equations.** The massless reference equation is satisfied by constant `Psi`; its conjugate is also satisfied. All multiplier forces vanish because `lambda` and its derivatives vanish. In this chosen null-spin alignment even the ordered HC transport annihilates the probe, since `(Gamma.n)Psi=0`. This is not a claim about arbitrary spinors, a varying induced spin connection or the native massive equation.

**Scalar HC equation.** Vary `h` at fixed independent `E,n` before substituting (13). Its equation is

```text
EL_h=kappa/sqrt|g| partial_mu[sqrt|g| n_nu F^{mu nu}]
       -kappa lambda_a^mu n_mu j^a=0.                  (14)
```

On the transverse null branch, `n^2=0`, `n.partial h=0`, and `n_nu F^{mu nu}=0` identically throughout the patch. Both terms in (14) therefore vanish. The script also evaluates the full curved-density derivative, including inverse-metric derivatives, instead of only substituting a flat principal symbol.

**Independent metric/coframe equations.** Vary the full metric before imposing the null profile. As in the earlier geometry calculation,

```text
G_mu_nu=-kappa Delta_perp h n_mu n_nu,
T_mu_nu=kappa^2 |grad_perp h|^2 n_mu n_nu.
```

Equation `G=kappa_eff T` is equivalent to `Delta_perp exp(kappa_eff kappa h)=0`; (13) satisfies it exactly. The free reference probe action has no `E` dependence and the multiplier vanishes, so these are all metric stresses of (12). No uncomputed probe stress was discarded from this specified action. Since the metric equation is satisfied, `pi_E=0` and the full coframe Euler equation `pi_E+lambda=0` follows as well.

**Current.** The actual phase current of (12) is the reference current `j=l`, which is constant and conserved. Even the induced coordinate current is `E^(-1)l=l` on this branch, with determinant one, so its induced divergence also vanishes. The old divergence `8` belonged to the different varying-current construction `j=2(x+c)`; it is not subtracted by hand here.

For `kappa=0.4`, `kappa_eff=1`, `F0=2`, `b=(0.1,0)`, and `(x,y)=(0.2,0.3)`, the report gives

```text
h                                      = 1.7577437785327834
probe residual norm                    = 0
coframe constraint residual norm       = 2.22e-16
independent Einstein residual norm     = 2.92e-18
coframe Euler residual norm            = 4.90e-18
curved scalar HC Euler residual        = -1.04e-18
both current divergences               = 0
Riemann component norm (not invariant)  = 0.009802960494069222
```

The exact formulas prove the local family; these numbers check their implementation. Nonzero curvature distinguishes this from a flat background-only example. Local compactly supported variations and a valid positive-harmonic patch are assumed. Global boundaries, well-posedness, energy bounds, stability and a physical microscopic interpretation are not established. In particular the scalar null kinetic operator remains degenerate. Prescribed background coframe and axis data are not solved dynamical fields.

## 5. Why This Does Not Yet Solve the Paper

The example answers a narrow existence question: an explicitly changed, background-supported dictionary can coexist with a common real action, conserved probe and curved HC-supported geometry. It does not justify that dictionary from the native MM/HC/QAM data.

Three immediate restoration tests make the gap quantitative at the same sample point:

- Restoring `Omega=m I+gamma h I` with `m=0.6,gamma=0.2` gives probe residual norm `0.9515487557065566`; its mass-like HC image is not null-transport-dark.
- Restoring a charged probe with zero gauge field and commuting HC gives a positive central Gauss source norm `1`; the old missing charged equation has not been solved by calling the scalar model neutral.
- Restoring `-lambda_H(h-0)^2` with `lambda_H=0.5` gives additional scalar Euler residual `-1.7577437785327834`. Choosing a varying target equal to `h` instead requires its own native functional and background reactions; it is not a free fix.

Also, nonzero `h` is not the minimal exact-closure `H_C=0` branch. The native generation embedding, mass law, projector reactions, physical adjoint, coupling scales, relation to the photon-clock sector and derivation or replacement of the added background remain unresolved. The negative result of the main Section 8 is unchanged: it concerns the unshifted coframe and same-frame real-bilinear equation, not (9) or (12).

The next native step is therefore to decide whether an affine collective coframe can actually be derived, or whether another explicitly justified microscopic/effective readout replaces it, and then restore the mass, gauge and closure sectors together. The existence example is a comparison for that work, not permission to silently change the main paper.

## 6. Reproduction

`python -B analysis/HC_Two_Frame_Action_Bridge.py --output analysis/HC_Two_Frame_Action_Bridge.json` reproduces the report. The 32 focused checks cover mixed/affine trace identities, relative-frame bounds and Lorentz negative control, reference on-shell first jets, multiplier variation, composite/independent equations, all equations of the local neutral branch, nonzero curvature, conserved currents and restoration failures. They use the existing NumPy installation and written derivations, not a proof assistant or empirical validation. The main TeX and its 1,037-page PDF are unchanged by this follow-up.

## 7. Source-Backed Background Follow-Through

The subsequent [background-origin analysis](HC_Background_Coframe_Origin.md) evaluates what can supply `theta` without simply declaring an identity. It derives the exact background/fluctuation expansion with mandatory cross terms, and constructs a nondegenerate ART background and nondegenerate prepared ART/QFT cross-readouts from an exact Hermitian three-channel reference-Dirac solution. The third channel mediates the interaction and balances the channel phase-current exchange. The inherited total coframe is still degenerate in the sample, and neither the native background/readout selection nor the common gravitational action is derived. Forty-four checks distinguish this conditional provenance from an adopted affine correction or native closure.
