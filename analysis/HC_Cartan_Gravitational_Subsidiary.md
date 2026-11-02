# A Conditional Gravitational Subsidiary System

This integrates the parent [coordinate Ward derivation](HC_Cartan_Diffeomorphism_Residual_Identity.md),
the [off-shell Lorentz audit](HC_Cartan_Lorentz_Residual_Identity.md) and the
independent [full analytic propagation derivation](HC_Cartan_Constraint_Propagation_Derivation.md).
Only the explicitly added neutral Cartan comparison is addressed. No main
TeX/PDF, action, coupling, native frame or physical scale is changed.

## Conditional Theorem, Not a New Full Solution

Assume on an open region:

- Exact Cartan elimination with compatible derivatives.
- Full real probe equation R=0 and ALL constitutive equations F=C-E=0.
- A sufficiently smooth metric with a quantitatively spacelike slicing.
- The six spatially projected trace-reversed gravitational evolution equations.
- Zero initial gravitational constraints and no incoming constraint boundary flux.

Then the four gravitational constraints propagate as zero. This is a
conditional analytic conclusion from the identities and energy estimate below.
It does not prove that the full parent fields satisfying these hypotheses
exist, or that R and F follow from initial data alone. The saved finite Taylor
fields have nonzero R/F off the origin and do NOT instantiate the theorem's
open-set hypotheses.

## Why the Evolution Choice Matters

On R=F=0, the coframe Euler density gives the symmetric tensor density S with
partial_mu S^{mu nu}+GammaLC^nu_mu,rho S^{mu rho}=0. Set T=S/|det E|.
For unit slice normal n, define H=T(n,n), M_i=-T(n,partial_i) and the spatial
stress projection P. These are Euler residuals, not an additional matter fluid.

Naively taking S^{ij}=0 at a flat normal point gives

    partial_t H + partial_i M_i = 0,
    partial_t M_i = 0.

Its nonzero spatial symbol is nilpotent of rank one with square zero, and
is not diagonalizable. The explicit solution H(t)=H(0)-t div M(0) loses a
spatial derivative. This invalidates the naive same-order positive energy
argument, not the whole parent model or every possible reduction.

Instead use the geometric spatial projection of

    Q^{mu nu} = T^{mu nu} - (1/2) g^{mu nu} trace_g(T).

It implies P^{ij}=H h^{ij}. In a chart with nonzero shift, merely imposing
contravariant Q^{ij}=0 is incorrect: use lower-index Q_ij=0, or equivalently
Q^{ij}+beta^i Q^{0j}+beta^j Q^{i0}+beta^i beta^j Q^{00}=0.
This is a choice of reduced gravitational evolution equations; on zero
constraints it restores the full coframe Euler equation without changing the
parent action. It is not a demonstrated well-posed reduction of all fields.

## Positive Subsidiary Symbol and Full Lower Terms

Write g=-N^2 dt^2+h_ij(dx^i+beta^i dt)(dx^j+beta^j dt), and take U=(H,M_i).
The conditional subsystem has form partial_t U+A^i partial_i U+B U=0, with

    A(xi) = -(beta.xi) I + N [[0, (h^-1 xi).T], [xi, 0]],
    W = diag(1,h^-1) > 0.

W A(xi) is symmetric. Its four speeds are -beta.xi plus/minus N|xi|_h and
the double transport speed -beta.xi. These are characteristics of the residual
subsystem only, not a classification of the full parent's physical modes.

The implementation does not infer B by fitting a jet. It reconstructs
T=H(n n+h_upper)+n M+M n, differentiates the metric-dependent coefficients,
forms the full LC divergence and projects it with rows N^2 delta^nu_0 and
N g_i,nu. This fixes every lapse, shift, volume and connection term. Tests
independently compare to the explicit ADM expressions, with K_ij defined by
-(partial_t-L_beta)h_ij/(2N):

    (partial_t-beta.partial) H + N D_i M^i = 2N K H - 2 M^i D_i N,
    (partial_t-L_beta) M_i + N D_i H = N K M_i - 2 H D_i N.

On the previously recomputed metric ball, the uniform symmetrizer bounds are
approximately 0.9999999940 I <= W <= 1.0000000060 I. Those numbers are finite-
float evaluations of analytic metric inequalities, not interval certificates.
They do not assert that the finite Taylor fields solve the equations nearby.

## Energy and Zero-Constraint Propagation

The positive energy is integral (H^2+h^{ij}M_iM_j)/2 times sqrt(det h).
The independent derivation gives its exact local balance law, including all
acceleration and shift terms, and a bound E'(t)<=C(t)E(t) after excluding
incoming flux. Integrating gives E(t)<=E(0) exp(integral C), hence zero remains
zero. A local shrinking domain can replace a global slab or artificial boundary.

Metric-coefficient first derivatives must be bounded as assumed in that
argument. The small coframe-distance bound alone does not control arbitrary
solution derivatives. It provides uniform positivity, not the missing full
existence theorem or boundary data construction.

## Reproducible Controls and Remaining Work

Thirteen focused tests retain the negative nilpotent control, arbitrary-shift
projection and normalization, metric-dependent coefficient derivatives, full
projected divergence, characteristic speeds, uniform symmetrizer and the exact
local energy identity. The energy test checks general nonzero shift, lapse
gradient and extrinsic curvature, not just a flat frozen symbol.

The coordinate/Lorentz source checks separately retain nonzero R and F, so the
conditional step cannot be silently mistaken for an off-shell source-free law.
The next open obligation is a compatible reduced evolution and propagation
system for those probe/constitutive residuals, with the remaining multiplier
and geometric gauge conditions. Full coupled hyperbolicity and Cauchy existence
remain open. No solved gravitational mechanism or native HC/C7 follows.

```text
python -B analysis/HC_Cartan_Gravitational_Subsidiary.py --output analysis/HC_Cartan_Gravitational_Subsidiary.json
python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_gravitational_subsidiary.py
```

The JSON pins normalized inputs and records the positive symbol, direct
divergence and coefficient-domain controls. The full derivation is linked
above; numerical residual checks do not replace the conditional proof.

Final verification: 2,056 audit tests and 34 separate OP5 checks pass (2,090
total). This stage adds nine coordinate Ward, eight Lorentz residual and
thirteen gravitational subsidiary checks. Full-monolith preservation and
whitespace checks pass. No commit, push or PDF build was performed.
