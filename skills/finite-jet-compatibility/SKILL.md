---
name: finite-jet-compatibility
description: Diagnose scientific finite-jet or constrained linear systems by eliminating free higher derivatives, identifying source gates, and attributing compatibility residuals to identities. Use for PDE prolongation and pointwise-to-regional proof gaps, not ordinary data analysis or as a physical validity certificate.
---

# Finite-Jet Compatibility

Turn repeated numerical compatibility checks into reproducible diagnostics without
promoting a pointwise calculation into a regional or physical theorem.

## Fix the Mathematical Contract

Identify the equations, derivative order, packing and real/complex conventions,
fixed lower data, free higher data, prescribed tangential data, source coordinates
and coordinate/gauge conditions. Do not release prescribed data silently to make
a fit succeed. Keep the frozen-data failure as a control when testing a new germ.

Use existing authoritative field evaluators and fingerprinted matrices. Preserve
historical sidecars and their fingerprints unless their revision is requested.
In QuantumSphere-Unfold, read [references/qsc-map.md](references/qsc-map.md) for
the relevant entry points; those project-specific dimensions are not universal.

## Eliminate Before Identifying Sources

For A z + B q + b=0, find the complete left kernel L of A, then inspect the gate
L^H B. Source visibility before eliminating z is not source identifiability.
An economy SVD omits left directions for tall matrices; use a complete U there.
For wide matrices economy U is already complete. Use conjugate transposes for
complex systems. Record singular values, cutoffs, dimensions and the full residual.

An injective source gate gives uniqueness only for compatible prescribed data.
Test the remaining projected residual as well. Six left compatibility rows and
six right-kernel source directions are not identified by equal dimensions.

The executable helper [scripts/compatibility.py](scripts/compatibility.py) provides
`eliminate`, `fit_sources` and `attribute_left_space`. It accepts an optional injected
`services.svd` backend; NumPy is the only required library. Read
[references/tool-contract.md](references/tool-contract.md) for inputs and CLI usage.
These are numerical diagnostics, not symbolic rank or interval certificates.

## Attribute the Remainder

Construct candidate identity rows K with their actual right sides h. In particular,
differentiate L F=0 as L dF=-(dL)F; do not drop lower residual sources off shell.
Check K A, the row-space/left-kernel projector difference, K b-h and reconstruction
of the incompatible component by K^+h. Matching ranks alone do not identify spaces.
Nonorthogonal row-family norms are not additive residual components.

Compare nested free-variable choices when useful: normal-only versus released
tangential higher data, time-only versus all derivatives, source-fixed versus
source-adjusted. Report which inputs changed. Re-evaluate the unprojected field
equations after a correction rather than accepting a projected fit alone.

For numerical derivatives, compare step sizes and use an independent analytic or
existing evaluator at a shared point. Where highest-jet dependence is polynomial,
differentiate that dependence separately to avoid small-step rank noise. Do not
claim a rank gap is resolved when its scale overlaps observed derivative errors.

## Preserve the Proof Boundary

Distinguish finite linear compatibility, numerical finite-jet completion, sampled
chart regularity, uniform estimates, exact identities, regional existence and
physical identification. A float majorant is not outward-rounded certification.
An augmented inverse does not guarantee compatible right-hand sides or exact
normal rank. A sampled tangent gate is not automatically an affine source law.

Pointwise corrections at different coordinates need not be derivatives of one
field. Check integrability and constraint propagation separately. After repairing
a lower condition, revisit the other retained orders; solving the first
prolongation does not certify the full higher system.

Use bounded local workers for independent point diagnostics and the existing
cache/DI services for expensive matrices. Cache builders must return the provider's
actual output contract (in QSC, a nonempty string-keyed array dictionary). Fingerprints
identify input state, not mathematical equivalence. This skill grants no permission
to commit, push, update issues, publish, or change model assumptions.
