# Frame-Factorized Cartan Solve

## Scope

This calculation establishes an algebraic frame factorization of the Cartan
Hessian in the existing neutral commuting-spinor odd-cross Einstein-Cartan
comparison. It does not identify native HC/C7 physics, change fields or refit
coefficients. Main TeX/PDF and published payloads remain unchanged.

The [centered inverse action](HC_Cartan_Centered_Inverse_Action_Bound.md)
improves fixed-center matrix bounds, but the derivative of the variable Hessian
still contributes substantial uncertainty. The present calculation avoids
forming that variable 24-by-24 inverse by using a checked frame transformation.

## Algebraic Identity

Let E be the coframe matrix, A=E^-1 and v its positive volume. In the existing
24-component ordering define B(A)=A^T tensor I_6. With H0 the Cartan Hessian
at A=I and v=1, the identity is

```text
H(A,v) = v B(A)^T H0 B(A).
```

Consequently, for invertible E and nonzero v,

```text
H(A,v)^-1 = v^-1 (E^T tensor I_6) H0^-1 (E tensor I_6),
k = v^-1 (E^T tensor I_6) H0^-1 (E tensor I_6) f.
```

This is not a frozen-Hessian approximation or an assumption that spacetime is
flat. Only the frame-independent matrix H0 is fixed. The entire coframe and
volume dependence remains in the surrounding factors, including every
physical derivative and approximation tail.

The determinant identity also follows:

```text
det H = v^24 (det A)^12 det H0.
```

For the physical volume v=|det E| this becomes det H=v^12 det H0. Since H0 is
invertible, this algebraic block has no additional loss of invertibility for
a nonsingular coframe and nonzero volume within this comparison model. This
does not establish regularity of the full differential system, rule out
curvature singularities, or prove a regional solution.

Invertibility is not uniform conditioning: the factorization only gives the
conditional bound ||H^-1||_2 <= ||E||_2^2 ||H0^-1||_2 / v. This factor can still
be large near frame degeneracy or small volume.

## Exact Coefficient Certificate

Both sides of the Hessian identity are homogeneous quadratic polynomials in
the sixteen entries of A. The stored curvature-Hessian coefficient tensor has
integer entries. The executable compares all sixteen squared-entry
coefficients and all 120 mixed-entry coefficients, using the direct contraction
and the proposed B(A)^T H0 B(A) construction. These 136 checks cover the entire
quadratic polynomial, not selected numerical frames.

The checks use signed integer arithmetic with a conservative intermediate
bound, including mixed-term sums and differences. Inputs are rejected if that
bound cannot exclude int64 overflow. Corrupted/nonintegral coefficient tensors
are rejected. The flat inverse is separately computed and verified in rational
arithmetic; its entries are exactly representable half-integers. A singular
flat Hessian is rejected.

The full coefficient identity is valid for every A; the inverse identity
additionally requires nonsingularity and nonzero volume. Independent rational,
nonidentity frames are checked against the direct Hessian as controls.

## Derivatives And Tails

The variable factors E tensor I_6 and E^T tensor I_6 are built from the known
coframe and physical coframe derivative models. Their Frobenius remainder
factor is bounded by sqrt(6). The scalar reciprocal volume is enclosed with
the existing Neumann model and differentiated as d(v^-1)=-v^-1 (dv) v^-1.

Matrix/vector actions use the previously certified centered matrix bounds.
The product rule differentiates every frame, source and reciprocal-volume
factor. No derivative of an unknown value tail is taken. The method does not
drop volume derivatives, assume constant frames or replace the source by a
constraint value.

## Recomputed Results

| Quantity | Radius 1/16384 | Radius 1/32768 |
| --- | ---: | ---: |
| Previous constraint tail | 0.000041522 | 0.000001274 |
| New constraint tail | 0.000039406 | 0.000001230 |
| Previous probe tail | 0.000098280 | 0.000003013 |
| New probe tail | 0.000093003 | 0.000002903 |
| Previous coframe tail | 0.001004658 | 0.000030933 |
| New coframe tail | 0.000781271 | 0.000024301 |
| Previous curl tail | 0.002154855 | 0.000066429 |
| New curl tail | 0.001588055 | 0.000049071 |
| Previous combined 80-row upper estimate | 0.002379942 | 0.000073351 |
| New combined 80-row upper estimate | 0.001772712 | 0.000054850 |

All four blocks are recomputed with the same frame-factorized connection and
the latest readout formulas. Connection derivative tail bounds at the larger
radius decrease from the previous range 7.52e-5 through 8.72e-5 to the new
range 3.57e-5 through 4.77e-5. The retained 80-row coefficient difference from regrouping is
about 1.64e-15 in Frobenius norm. Nonzero degree-three/four defects remain;
none is fitted again or replaced by zero.

## Verification And Remaining Gap

Nine focused tests cover all quadratic coefficient checks and the exact flat
inverse; an independent rational nonidentity frame and inverse; corrupted,
nonintegral, singular and overflow-prone coefficients; frame-lift and volume
domain guards; arbitrary curved off-shell solves and their four derivatives;
uncertain frame/volume/source/derivative inputs; independent original
connection jets on a nonzero background; fingerprints and proof scope; and
original-equation neighborhood controls. Two local workers recompute the two
radius cases.

The algebraic factorization and flat inverse have exact certificates. The
complete nonlinear bound is still binary64 without full outward rounding.
Original-equation samples are controls, not whole-region proof. Exact low-order
closure, regional PDE compatibility, convergence, native identification and
distance to an exact solution remain unproved. A smaller majorant is not a
smaller actual residual of the unchanged fields.

The executable and saved JSON report share this note's filename stem.
