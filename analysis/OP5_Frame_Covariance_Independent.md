# OP5: independent frame-covariance check

Date: 2026-10-25. Base revision: `f2de387d66d6ab2da00ef28a14305729910d7ef1`.
Scope: a bounded derivation from the stated spectral expressions, not a new
physical model, a proof of OP5, or a verification of the infinite zero sum.
This note does not change any manuscript or release.

## Source contract

- Original balance: `sources/research/parts/v470/23_physical_readouts.tex`,
  label `def:tr-balance` (line 457): the cutoff integral is identified with
  `beta_sym^2 * ell_P^2`.
- Original finite-part prescription: same file, `rem:regularization-B`
  (line 767); integrated zero sum at `def:theta-sum-B` (line 838).
- Corrected decomposition and action caveat:
  `sources/research/parts/v480-post-release-layers.tex`,
  `subsec:v480-r05-trace-decomposition` (line 605),
  `subsec:v480-r05-einstein-reading` (line 640).
- Scale/readout distinction: `sources/research/parts/v490-post-release-layers.tex`,
  `subsec:v490-r18-two-classes` (line 2609).
- Reference R versus photon P: same file,
  `subsec:v490-r24-corrections` (line 3499), especially r24.3.
- Existing OP5 frame audit: same file, `subsec:v490-r61-results` (line 7803).

## 1. A conjugate spectral change of coordinate

Fix any positive, finite number `a`. A passive rescaling of frequencies is

\[
\omega'_n=a\omega_n.
\]

Preservation of each spectral phase forces its conjugate coordinate to obey

\[
t'=t/a,\qquad L'=L/a,\qquad dt'=dt/a,
\qquad \omega'_nt'=\omega_nt.
\]

For a finite sum (or a consistently regularized distribution), therefore,

\[
\Sigma'(t')=\Sigma(at'),\qquad
\int_0^{L'}\Sigma'(t')\,dt'
=a^{-1}\int_0^L\Sigma(t)\,dt.
\]

More generally, a declared additional amplitude weight `b` gives
`Sigma'(t')=b Sigma(at')` and an integral weight `b/a`.
The transformation of a spectral density is separately fixed by counting:

\[
N'(w')=N(w'/a),\qquad \rho'(w')=a^{-1}\rho(w'/a).
\]

None of these rules requires selecting between the finite numerical factors
`gamma_L` and `exp(eta)`; they hold for either if it is a genuine passive
rescaling. The direction matters: `omega'=omega/g` means `a=1/g`, so its
conjugate time interval becomes `L'=g L`, not `L'=g^(-3/2)L`.

This does not prove that the author's Planck-length law is false. A Planck
length with independently assigned weight 3/2 need not be the conjugate time
coordinate of a frequency with weight 1. It proves that identifying the two
intervals requires an additional conversion law (including the role of `c`
and the dimensionless normalization), which is not supplied by their names.
Changing such a physical cutoff is a change of observable, not just a
coordinate description of the same observable.

## 2. The full corrected decomposition must be transported

Write the r05 expression, conditionally on its spectral interpretation, as

\[
\Sigma(t)=M(t)-P(t)-Z(t),\quad
M(t)=e^{t/2},\quad
P(t)=e^{-t/2}\sum_{n\ge2}\Lambda(n)\delta(t-\log n),\quad
Z(t)=\frac{e^{-t/2}}{e^{2t}-1}.
\]

Its conjugate pullback is

\[
M'(t')=e^{at'/2},\qquad
Z'(t')=\frac{e^{-at'/2}}{e^{2at'}-1},
\]
\[
P'(t')=\frac1a e^{-at'/2}
\sum_{n\ge2}\Lambda(n)\delta(t'-\log(n)/a).
\]

Thus it is inconsistent to transform only the frequencies while leaving the
old prime locations, the old exponential terms, or the integration measure
untouched. The decomposition transforms as a whole, and its distributional
identity remains an identity. This does not imply a particular vacuum energy.

Spectral qualification: r05 writes `rho=1/2+i gamma` while also saying that no
assumption about real parts is made. For arbitrary nontrivial zeros the
explicit-formula trace after multiplication by `exp(-t/2)` is
`sum_rho exp((rho-1/2)t)`, not automatically `sum exp(i gamma t)`. The latter
needs a critical-line/RH interpretation or a specifically restricted model.
The covariance argument above applies to finite spectral sums directly and
to an already defined distribution; it does not prove that spectral premise.

## 3. Endpoint finite parts and their scale

For `F(t)=c/t+O(1)` near zero define, with a declared positive reference scale
`mu`,

\[
I_\mu(L)=\lim_{\epsilon\downarrow0}
\left[\int_\epsilon^L F(t)\,dt
+c\log(\epsilon/\mu)\right].
\]

Let `F'(t')=b F(at')`, so `c'=bc/a`. If also `mu'=mu/a`, direct substitution
gives

\[
I'_{\mu'}(L/a)=\frac ba I_\mu(L).
\]

If instead the same numerical reference scale is imposed in both frames,
the result is

\[
I'_\mu(L/a)=\frac ba\,[I_\mu(L)-c\log a].
\]

The logarithmic extra term comes from holding the subtraction scale fixed.
It is a change in the specified subtraction scheme, not a free consequence
of passive covariance. It cannot be tuned to close OP5 without an independent
physical prescription for that scale and any finite counterterm.

The corrected identity is explicitly stated only for `t>0`. It does not
uniquely determine a distributional extension through `t=0`: distributions
supported at the origin are invisible on that open half-line. In particular,
an endpoint-supported counterterm can change an endpoint integral without
changing that identity. A sharp cutoff indicator is also not the smooth test
function used to state the distributional formula. A regulated pairing and
its endpoint extension must be specified before a finite target value is
meaningful.

### A defect in the printed original prescription

The original `R=-exp(-t/2)/(exp(t)-1)` has the expansion

\[
R(t)=-\frac1t+1-\frac{11}{24}t+\frac18t^2+O(t^3).
\]

Thus `F=1+R` has `c=-1`. Its convergent endpoint subtraction is
`integral_epsilon^L F - log(epsilon/mu)`. The printed prescription instead
adds `+log epsilon`: the sum diverges as `2 log epsilon` to negative infinity.
Also, the printed constant term in the expansion of R is not the expansion
of the displayed R. Consequently the quoted old finite number is not
established by that displayed prescription. This does not invalidate the
separate numerical value of a specifically defined zero sum; it invalidates
using the displayed finite-part identity as its justified target.

For the corrected `F=M-Z` below the first prime at `log 2`,

\[
F(t)=-\frac1{2t}+\frac74+\frac{t}{48}
+\frac9{32}t^2+O(t^3),
\]

so its subtraction coefficient is `c=-1/2`. Even after a sign correction,
the old and new finite parts are different mathematical observables.
These two series were checked with SymPy in this audit; the sign follows
directly by integrating `c/t` and does not depend on numerical precision.

## 4. What can and cannot change from a passive frame transition

Let a well-defined original balance be `I_mu(L)=B`, and define
`Delta=I_mu(L)-B`. A covariant transport must use `B'=(b/a)B` and the same
transformed subtraction convention. Then

\[
\Delta'=\frac ba\Delta.
\]

For finite nonzero `a,b`, zero versus nonzero is invariant. A new root can
only arise here by changing the cutoff, subtraction convention, target,
state-dependent readout, or spectral/model input. Such a change may be worth
studying, but is not a mere coordinate correction.

In particular, if `B=q L^2`, coordinate covariance requires
`q'=ab q`, since `L'=L/a`. Simply retaining the same numerical `q=beta_sym^2`
while transforming L is not generally covariant. The manuscript describes
`beta_sym^2` as a readout depending on the state/frame; hence its identification
with a coefficient of this integral needs an explicit physical bridge, not
just a square on both sides.

The historical label "photon frame" is also material. r24 identifies that
finite target with reference R, while the photon P of Convention F is a
different, limiting state. A singular limit `a -> 0` or `a -> infinity` is
outside this invertible-coordinate argument. Sending a positive discrepancy
to zero in a limit does not give a finite-frame equality, nor by itself a
well-defined limiting physical observable. A photon-P claim needs its own
limiting state, pairing, units, subtraction and physical-meaning analysis.

## Outcome and exact missing inputs

**Structural result:** a complete invertible passive transformation cannot
repair a failed well-defined balance of the same observable. An incomplete
transformation in the historical OP5 expression is possible and identifiable,
but repairing it does not by itself establish a physical cancellation.

**Not decided:** whether a newly and independently defined R- or P-frame
observable satisfies a physically justified replacement of OP5. The current
ingredients do not uniquely define that replacement.

Needed inputs are: (1) the spectral premise and distribution/test-function
pairing, (2) an explicit identification of the integration variable and
physical cutoff including units, (3) fixed subtraction scale and finite
counterterms, (4) a target with the correct transformation law and a physical
map to Lambda rather than just an untyped beta-squared readout, and (5) any
singular P-limit separately from the finite M-to-R transition.

This was a separate derivation in a child-agent session. It is an audit of the
transport logic, not an independent certified literature or physical review.

## Additional conditional spectral normalization check

The following strengthens the structural result only for a precisely stated
spectral model. Assume:

1. The relevant zeros, with multiplicity, have `rho=1/2+i gamma`, with their
   conjugates. For the actual zeta spectrum this is an RH-dependent premise;
   finite tables of critical-line ordinates do not prove it for all zeros.
2. The classical explicit formula for `sum_rho x^rho/rho` is interpreted in
   symmetric zero-height order, with its usual value away from prime powers.
3. The paired Hadamard product for xi supplies the absolutely convergent
   identity below. These are external leaves, not proved by this note.

For `0<a<log 2`, set `x=exp(a)` and

\[
F(a)=x-\log(2\pi)-\tfrac12\log(1-x^{-2}),\qquad
S(a)=2\lim_{Y\to\infty}\sum_{0<\gamma\le Y}
\frac{\sin(a\gamma)}{\gamma}.
\]

Pairing the terms in the explicit formula gives

\[
S(a)=e^{-a/2}F(a)
-\sum_{\gamma>0}\frac{\cos(a\gamma)}{1/4+\gamma^2}
+\frac12\sum_{\gamma>0}\frac{\sin(a\gamma)}
{\gamma(1/4+\gamma^2)}.
\]

The two correction sums converge absolutely. In particular, the paired
Hadamard product and the value of the logarithmic derivative at zero give

\[
A:=\sum_{\gamma>0}\frac1{1/4+\gamma^2}
=-\frac{\xi'(0)}{\xi(0)}
=1+\frac{\gamma_E}{2}-\frac12\log(4\pi).
\]

One way to see the sign is the paired factor
`(1-s/rho)(1-s/(1-rho))=1-s(1-s)/(rho(1-rho))`;
its logarithmic derivative at zero is `-1/(rho(1-rho))`.
Expansion of the elementary first term and dominated convergence in the two
absolutely convergent corrections therefore yield

\[
\lim_{a\downarrow0}\left[S(a)+\tfrac12\log a\right]
=-C,\qquad C=\frac{\log(2\pi)+\gamma_E}{2}.
\]

On the open prime-free interval the corrected distributional trace implies
`S'=M-Z`, in the sense of distributions. Hence S differs by a constant from
the smooth primitive there. The small-a limit fixes this constant; this is
not an arbitrary finite-part choice once symmetric spectral normalization
has been adopted.

Define the explicitly chosen finite part

\[
J_1(a)=\lim_{\epsilon\downarrow0}
\left[\int_\epsilon^a(M-Z)(t)\,dt-\tfrac12\log\epsilon\right].
\]

An elementary closed form is obtained by writing `u=exp(a/2)`:

\[
H(a)=2u-\frac2u+rac12\log\frac{u+1}{u-1}-\arctan u,
\qquad J_1(a)=H(a)-\log2+\frac\pi4.
\]

Indeed, differentiating H with respect to u gives
`2+2/u^2-1/(u^2-1)-1/(u^2+1)`. Multiplication by `du/da=u/2`
simplifies to `u-1/[u(u^4-1)]=M(a)-Z(a)`.
Also `H(a)+(1/2)log(a)` tends to `log2-pi/4`.
It follows, under assumptions 1--3, that

\[
\boxed{S(a)=J_1(a)-C,\qquad 0<a<\log2.}
\]

This identity avoids extrapolating a finite zero table or claiming an
unproved numerical tail bound. It still carries the spectral and summation
premises above. In particular, it does not justify reusing the old OP5
regularized target. The finite part J_1 and the symmetrically normalized
spectral primitive S differ by the fixed constant C, and identifying either
with a physical Lambda target is an additional obligation.

The parent investigation checked primary excerpts of Conrey's 2003 AMS
article for the explicit psi formula and the Clay proceedings `cmip06.pdf`
for paired Hadamard factorization. Those external leaves are reported as
conditional here; this child review did not independently authenticate or
audit a complete source proof.
