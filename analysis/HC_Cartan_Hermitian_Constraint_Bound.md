# Hermitian Constraint Bound

## Scope

This calculation changes only the enclosure of the 16 constitutive/constraint
equations in the existing neutral commuting-spinor odd-cross Einstein-Cartan
comparison. Fields, fixed parameters and mathematical equations remain
unchanged. It does not identify native HC/C7 physics. Main TeX/PDF and published
payloads remain unchanged.

The [projector readout calculation](HC_Cartan_Projector_Readout_Bound.md)
leaves a constraint tail about 0.00588671 at radius 1/16384. That bound still
passes through the full covariant spinor jet before taking its bilinear
readout. Here the connection part is grouped before norms, using the same
Hermitian response and fixed-map certificates already verified for the curls.

## Off-Shell Identity

For a fixed Hermitian matrix H, arbitrary S and the same spinor on both sides,

```text
conjugate(psi^dagger H S psi) = psi^dagger S^dagger H psi,
Im(psi^dagger H S psi)
  = (1/2) Im[psi^dagger (H S - S^dagger H) psi].
```

This is an algebraic identity, not a field equation. It does not require the
constraint or any residual to vanish. Hermiticity is essential; the analogous
formula is not generally valid for non-Hermitian H or two unrelated spinors.
The implementation verifies the existing fixed channel selector Q and frame
weights W_a are Hermitian.

With H_a=Q tensor W_a and the channel-diagonal spin connection, the unchanged
constraint is therefore evaluated as

```text
C_a,mu = Im[psi^dagger Q W_a partial_mu psi]
       + (1/2) Im[psi^dagger Q response_a(Omega_mu) psi]
       - e_a,mu.
```

The second term uses the previously verified centered readout with its exact
projector-map norm. Every variable-spinor deviation term remains, including
the quadratic contribution when the fixed spinor center is zero. The partial
spinor derivative term and the complete coframe value tail remain as well.
No coframe component is replaced by its constraint value, no low-order error
is set to zero, and no connection derivative is needed by this identity.

## Recomputed Results

| Quantity | Radius 1/16384 | Radius 1/32768 |
| --- | ---: | ---: |
| Previous constraint tail | 0.005886709 | 0.000182719 |
| New constraint tail | 0.000119442 | 0.000003707 |
| Previous combined 80-row upper estimate | 0.009564382 | 0.000296301 |
| New combined 80-row upper estimate | 0.007539119 | 0.000233285 |

At the larger radius the new tail retains about 5.15e-6 partial-spinor readout,
1.14e-4 joint connection readout and 3.77e-13 coframe uncertainty. The other
64 equation components and their enclosures remain unchanged. The retained
coefficient difference from regrouping is about 3.33e-15 in Frobenius norm;
nonzero fourth-degree constraint defects remain explicit.

Curl uncertainty, about 0.00670511, now clearly dominates the combined bound,
followed by coframe uncertainty about 0.00343219. The improved constraint bound
does not reduce the actual residual of the unchanged fields.

## Verification And Remaining Gap

Eight focused tests cover the Hermitian identity and a non-Hermitian negative
control; variable-polynomial agreement with the original readout; zero-center
spinor deviations and the complete coframe tail; uncertain spinor, derivative,
connection and coframe inputs; nonzero off-shell agreement with the independent
original equations; input fingerprints; unchanged other 64 components and
enclosures; retained low-order defects; all three tail contributions; and
original-equation samples at both radii. The two radius cases use two local
workers.

The algebraic identity is exact, and the previously verified fixed-map
constants remain authoritative. The full nonlinear bound is still binary64
without complete outward rounding. Samples are controls, not whole-region
proof. Exact low-order closure, regional PDE compatibility, convergence, native
identification and distance to an exact solution remain unproved. A smaller
bound or crossing an arbitrary numerical threshold is not an existence proof.

The executable and saved JSON report share this note's filename stem.
