# Joint Probe Response Bound

## Scope

This calculation improves only the 24 real probe equations of the existing
neutral commuting-spinor odd-cross Einstein-Cartan comparison. Fields,
parameters and mathematical equations remain unchanged. It is not a native
HC/C7 identification. Main TeX/PDF and published payloads remain unchanged.

The [refreshed primary enclosure](HC_Cartan_Refreshed_Probe_Bound.md) leaves a
probe tail about 0.0104684 at radius 1/16384, mostly in its kinetic/balance
connection terms. Two separately recorded controls now combine these terms
before taking norms, then factor their shared spin response.

## Off-Shell Algebraic Identity

Write the complex probe as

```text
P = i W^mu (partial_mu psi + S_mu psi) - v M psi
    + (i/2)[partial_mu W^mu - S_mu^dagger W^mu - W^mu S_mu] psi.
```

The connection terms combine exactly into

```text
i W S psi + (i/2)(-S^dagger W - W S) psi
  = (i/2)(W S - S^dagger W) psi.
```

Thus

```text
P = i W^mu partial_mu psi - v M psi
    + (i/2)(partial_mu W^mu) psi
    + (i/2)(W^mu S_mu - S_mu^dagger W^mu) psi.
```

This regrouping requires no field equation, compatibility condition or zero
residual. The algebraic identity itself holds for arbitrary complex W and S.
It does not discard the weight-divergence term or freeze variable weights.

## Variable Weight Factorization

The actual fixed weights satisfy the exact stored identities

```text
FLAT_WEIGHTS_a = I_3 tensor W_a,
Q_WEIGHTS_a = Q tensor W_a,
Q^dagger = Q.
```

These identities are checked before using the factorization. In the existing
model, the volume v, inverse coframe A and multiplier lambda are real, and

```text
W^mu = v sum_a A_mu,a (I_3 tensor W_a)
       + sum_a lambda_a,mu (Q tensor W_a).
```

For the real lower-index connection Omega, let

```text
S_mu = -(1/4) Omega_mu,bc Gamma_b Gamma_c,
R_mu,a = W_a S_mu - S_mu^dagger W_a.
```

The joint connection action is then evaluated as

```text
sum_mu (W^mu S_mu - S_mu^dagger W^mu) psi
 = v sum_mu,a A_mu,a (I_3 tensor R_mu,a) psi
   + sum_mu,a lambda_a,mu (Q tensor R_mu,a) psi.
```

Every factor remains a variable Taylor model, including all volume, inverse,
multiplier and spinor cross terms. The already verified fixed response operator
maps Omega to R with induced component norm two. No new operator constant is
inferred from samples. Complex geometric coefficient models are rejected by
this particular implementation instead of silently applying a real-linear
identity to them.

A generic 12-by-12 implementation of the regrouped response is retained as a
separate control, so the regrouping and factorization gains are distinguishable.

## Recomputed Results

| Quantity | Radius 1/16384 | Radius 1/32768 |
| --- | ---: | ---: |
| Previous probe tail | 0.010468426 | 0.000324966 |
| Generic regrouped probe tail | 0.006641202 | 0.000206159 |
| Factorized probe tail | 0.000292595 | 0.000009082 |
| Previous combined 80-row upper estimate | 0.014767572 | 0.000457947 |
| New combined 80-row upper estimate | 0.010420118 | 0.000322793 |

At the larger radius the new probe tail retains about 1.42e-6 transport,
2.96e-7 mass, 8.69e-6 weight-derivative and 2.82e-4 joint connection uncertainty.
The other 56 equation components and their enclosures are unchanged. The
retained probe coefficient difference from the predecessor has Frobenius norm
about 5.12e-15; the factorized/generic difference is about 1.48e-15. Nonzero
degree-three/four defects remain. No coefficients are fitted again or set to
zero. Curl uncertainty is now dominant, followed by the constraint block.

## Verification And Limits

Nine focused tests cover the identity for arbitrary complex off-shell matrices;
the existing weight factorization with variable geometric factors; uncertain
spinor/connection/weight inputs; a zero multiplier center with nonzero variable
channel action; rejection of complex geometric models; nonzero off-shell
agreement with the original probe evaluator and nonzero multiplier gradients;
input fingerprints; unchanged other 56 components and enclosures; retained
low-order defects; both improvement controls; and original-equation sample
checks. The two radius cases use two local workers.

All physical weight derivatives and approximation tails remain. The complete
nonlinear enclosure is still binary64 without full outward rounding; only the
previous fixed response constant carries an exact arithmetic certificate.
Samples are controls, not whole-region proof. Exact low-order closure, regional
PDE compatibility, convergence, native identification and distance to an exact
solution remain unproved. A bound below one is not an existence threshold.

The executable and saved JSON report share this note's filename stem.
