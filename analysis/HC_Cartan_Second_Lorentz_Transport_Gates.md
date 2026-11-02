# Second Lorentz Transport Gates at the Prepared Normal Point

Date: 2026-10-18. Bounded independent sidecar for the declared neutral
commuting-spinor Cartan comparison, with the existing action and couplings
fixed. The proposed second Lorentz gate is correct under the hypotheses
below. At the loaded point its 18-by-12 map has numerical rank 12; its
restriction to the original six-dimensional normal curl image has rank 6.
This is a conditional point obstruction, not a regional closure theorem.

## Identity, Signs, and Full Second Derivative

Use the conventions of `HC_Cartan_Lorentz_Residual_Identity.py` and its
companion note. Internal indices are a,b=0,...,3, coordinate indices are
mu,r,s=0,...,3, and i,j=1,2,3 are spatial. Define

```text
F^a_mu = C[Q]^a_mu - E^a_mu,
F1[r] = partial_r F,       F2[r,s] = partial_r partial_s F,
FE1[r] = partial_r FE,     FE2[r,s] = partial_r partial_s FE,
R1[r] = partial_r R,       R2[r,s] = partial_r partial_s R.
```

In particular, `F^a_0` below means the temporal constitutive column, not the
value of the entire residual. All colon products are componentwise sums
over internal and coordinate indices; there is no extra metric in them.
For a constant Lorentz generator J,

```text
eta = diag(-1,1,1,1),     J.T eta + eta J = 0,
S_J = -(eta J)_ab Gamma^a Gamma^b / 4,
delta E = J E,   delta psi = S_J psi,   delta lambda = -J.T lambda.

0 = FE:(J E) + 2 Re[(S_J psi)^dagger R] + F:(J.T lambda).       (1)
```

The last sign is positive because the multiplier Euler expression is -F.
R is the full complex probe Euler density; the dagger contracts all spinor
and flavor components. The algebraic Cartan connection must be eliminated
as a field expression with compatible derivatives, so (1) holds off shell
near the point. A connection Euler value set to zero only at the point
does not supply this premise.

Differentiate (1) twice BEFORE setting any residual to zero. For commuting
coordinate derivatives and fixed J, the full result is

```text
0 = FE2[r,s]:(J E)
  + FE1[r]:(J partial_s E) + FE1[s]:(J partial_r E)
  + FE:(J partial_r partial_s E)
  + 2 Re[(S_J partial_r partial_s psi)^dagger R
         + (S_J partial_r psi)^dagger R1[s]
         + (S_J partial_s psi)^dagger R1[r]
         + (S_J psi)^dagger R2[r,s]]
  + F2[r,s]:(J.T lambda)
  + F1[r]:(J.T partial_s lambda)
  + F1[s]:(J.T partial_r lambda)
  + F:(J.T partial_r partial_s lambda).                       (2)
```

Every displayed product has a plus sign. For distinct r,s, each cross
product occurs once; there is no factor 2 multiplying either individual
cross product. Complex conjugation remains on the differentiated spinor
factor. No derivative of J or S_J occurs.

## Exact Conditional Point Theorem

Let compatible smooth field jets at p satisfy the off-shell identity (1),
and suppose the following hold exactly:

```text
At p: E=I, dE=0, F=R=FE=0, R1=FE1=0;
      partial_j F^a_mu=0 for every j,a,mu;
      lambda_a^i=0 for every a and spatial i;
      R2[0,j]=0 and FE2[0,j]=0 for j=1,2,3.

On an open region containing p: F^a_0=0 for every a.
```

The regional temporal-column equation implies, in particular,
`F1[r,a,0]=F2[r,s,a,0]=0` at p. It does NOT imply that F2 in a spatial
constitutive column vanishes. Define

```text
X_ai = F1[0,a,i],
ell_a = lambda_a^0,
L[j,a,i] = partial_j lambda_a^i at p.
```

Thus F1[0] has only its three spatial columns X, and F1[j]=0 at p.
Specializing (2) to (r,s)=(0,j) kills every FE and R product by the stated
residual hypotheses. The term containing F itself vanishes, and the
cross term with F1[j] vanishes. Moreover

```text
(J.T lambda)_a^mu = sum_b J_ba lambda_b^mu,
F2[0,j]:(J.T lambda)
  = sum_a,b F2[0,j,a,0] J_ba ell_b = 0.                       (3)
```

Equation (3) uses only the zero spatial multiplier VALUE at p and the
vanishing temporal column of F2. Arbitrary spatial columns of F2[0,j]
are allowed. Therefore for each of the six generators and each j,

```text
0 = X:(J.T partial_j lambda)
  = sum_i,a,b X_ai J_ba L[j,b,i].                            (4)
```

Here the first colon is understood by embedding X in a 4-by-4 array with
zero temporal column. Let G be the 18-by-12 coefficient map in (4). If G
is injective, then X=0 exactly. Equivalently, injectivity restricted to any
specified admissible curl subspace suffices to kill X in that subspace.
This proves the conditional theorem without assuming full F2=0.

Normality E=I,dE=0 matches the prepared point but is not needed for this
particular cancellation when FE=FE1=FE2[0,j]=0. Only mixed R2 and FE2 are
used; no pure second derivative residual equation is needed. For a strictly
point-jet version, the regional temporal-column premise can be weakened to
its first derivatives and the three mixed F2[0,j,a,0] equalities at p.

For clarity about the source terms, retain all the other hypotheses but
allow mixed FE2,R2 and temporal-column F2. Then the exact remaining equation
is

```text
(Gx)_(J,j) = -FE2[0,j]:(J E)
             -2 Re[(S_J psi)^dagger R2[0,j]]
             -sum_a,b F2[0,j,a,0] J_ba ell_b.                 (5)
```

Thus the homogeneous conclusion depends on these sources vanishing. If
spatial multiplier values are nonzero, spatial-column F2 terms must also
be restored. No claim is made that the lower equations imply the needed
mixed R2 and FE2 hypotheses.

## Numerical Map at the Actual Loaded Point

A read-only Python import with bytecode disabled called exactly
`HC_Cartan_Constitutive_First_Closure.neighborhood.load_data()`, including
its existing source-fingerprint checks. No higher continuation or large
coupled solve was run. The multiplier value is

```text
lambda = [ .01 0 0 0
           .02 0 0 0
          -.03 0 0 0
           .04 0 0 0 ].
```

The numerical 18-by-12 map is specified completely by the following three
4-by-3 blocks and the row rule below. Digits are rounded for display:

```text
L1 = [ .492870890962455 -.343642577779710 -.189028382242832
      -.164182685340567 -.140168352665902 -.412819812759908
      -.179708260405778 -.291943887261579 -.095834453221101
      -.332160665213301 -.230656882585612  .122708646781855 ]

L2 = [-.452890609097214 -.044750702102523  .677203118416211
      -.361635083489547 -.904092723051778  .764413659666902
      -.238213951409737 -.433162479909406  .382511569357068
      -.213293281498536 -.343324315762616  .127430085131010 ]

L3 = [-.213627797710005  .223597753799557  .425515970295943
       .366198612356860  .264206356726097 -1.044171437306167
      -.616746408092464 -.475163835054020  .739782940709603
      -.354103411049649  .250896009998521 -.038564871865147 ].
```

Here `Lj = point["multiplier_first"][j,:,1:]`: derivative direction is the
first index, the coordinate vector index is last. Use column-major-in-X,
or equivalently pair-major-in-curl, ordering

```text
x = (X_01,X_11,X_21,X_31, X_02,X_12,X_22,X_32,
     X_03,X_13,X_23,X_33).T.
```

Generators are in pair order (01),(02),(03),(12),(13),(23), with
`J=eta A`, `A_ab=+1,A_ba=-1`, matching the Lorentz audit. Rows are
generator-major, then j=1,2,3. For each spatial column i, the four entries
in row (ab,j) of G are zero except

```text
G[(ab,j), 4*(i-1)+a] = -eta_bb Lj[b,i],
G[(ab,j), 4*(i-1)+b] =  eta_aa Lj[a,i].                      (6)
```

The i in Lj above labels spatial columns 1,2,3. In particular the first
row (01,j=1) is

```text
[ .164182685340567 -.492870890962455 0 0
  .140168352665902  .343642577779710 0 0
  .412819812759908  .189028382242832 0 0 ].
```

Equations (6) and the three displayed blocks specify all 216 entries,
including the boost signs. No additional eta multiplies lambda or X.

The singular values of G, in descending order, are

```text
2.282503836941482, 2.233317102342708, 1.756361002517175,
1.558745945780437, 0.999176139336721, 0.973470832140230,
0.883594646789211, 0.731564263218608, 0.636758679391269,
0.475450196558246, 0.438605668121351, 0.085746538241773.
```

With absolute rank tolerance 1e-10, rank(G)=12 and dim ker(G)=0.
The smallest singular value is well separated from that tolerance.

## Restriction to the Original Normal Curl Image

Use the existing `spatial.normal_curl_system(prepared,point)`, accessed
through the first-closure module. This rebuilds only the original
56-variable normal block. Let A be its first 56 rows, C its final twelve
mixed curl rows, K=`original_kernel`, and B=C K=`induced_curl`. This is
the ORIGINAL normal kernel, not `normal_basis` with the spinor first jet
and temporal multiplier derivative fixed, and not a prolonged kernel.

| Map | Shape | Numerical rank |
| --- | --- | ---: |
| A | 56 by 56 | 34 |
| K | 56 by 22 | 22 |
| B | 12 by 22 | 6 |
| G | 18 by 12 | 12 |
| G B | 18 by 22 | 6 |
| vertical_stack(A,G C) | 74 by 56 | 40 |

The six nonzero singular values of B are

```text
38.205060112669514, 29.521668728987480, 29.521668728987464,
14.455195826976976, 4.627893576800732, 4.627893576800709.
```

The six nonzero singular values of G B are

```text
55.019653035235540, 36.983701617489686, 22.795707206268485,
8.548447143723049, 6.554584179901617, 5.151987947419479.
```

The largest omitted singular values are about 5.85e-13 for B and 5.78e-13
for G B. For an orthonormal basis Q of image(B), the singular values of
G Q are

```text
2.133790679033745, 1.819126706947007, 1.378527129586540,
0.961794581288872, 0.712459203409226, 0.354260476055957.
```

Thus image(B) intersect ker(G) has numerical dimension zero. The 22 normal
kernel directions retaining the gate have dimension 16, all with zero
curl response; the six independent original curl responses are excluded.
This statement concerns linear responses at fixed lower/spatial data.
The loaded affine mixed-curl offset has norm 1.80e-14, not a certified
exact zero. Adding the earlier three coordinate gates W adds no rank:
rank(vertical_stack(W,G))=12 and rank(vertical_stack(W,G) B)=6.

Minimal reconstruction of the gate, after importing the first-closure
module as f, is

```python
prepared, point, jets, extras, report = f.neighborhood.load_data()
eta = f.transport.cartan.ETA
generators = []
for a, b in f.transport.cartan.PAIRS:
    lower = np.zeros((4, 4))
    lower[a, b], lower[b, a] = 1, -1
    generators.append(eta @ lower)
G = np.array([
    (J.T @ point["multiplier_first"][j])[:, 1:].T.reshape(-1)
    for J in generators for j in range(1, 4)
])
system = f.spatial.normal_curl_system(prepared, point)
B = system["induced_curl"]
```

The loaded first-closure source (LF-normalized) has SHA256
`4d4e21781e909b4634b267d3af959667bfaec0557280af03a35d616854b1f22a`;
the raw `HC_Cartan_Next_Joint_Completion.json` has SHA256
`259e7358b88fbaae09c54499aace8ec00066c29f34994c1b7e0f71dce1225d78`.
These identify this calculation, not an exact or interval certificate.

## Scope and Regional Caveat

The exact theorem is conditional on injectivity and exact residual
hypotheses; the reported ranks support injectivity of the stored floating
map. This calculation does not certify that the loaded finite jet satisfies
all of those hypotheses exactly, or that a compatible continuation exists.

Zero spatial multiplier VALUE is a special point locus. Indeed the loaded
spatial derivatives of those columns have norm 2.569383067037422. The
spatial multiplier columns therefore cannot vanish identically on an open
neighborhood with this same first jet. If one instead imposes that regional
vanishing, all the Lj blocks vanish and this gate has rank zero. If the
columns become nonzero away from p, the discarded spatial F2 contraction
returns. A continuous full-rank coefficient map alone does not remove
that source term.

Accordingly this avoids full F2=0 at the prepared point by using the
regional temporal-F equation and the special multiplier value there.
It establishes no homogeneous regional transport system, uniqueness from
zero initial data, or constraint propagation. Different multiplier
backgrounds require recomputing the gate; this point calculation makes no
claim about the parent's independent Ward-only counterexample.

Only this Markdown note was written. No new action coupling, main TeX,
saved numerical report, agent operation, or Git operation was introduced.
