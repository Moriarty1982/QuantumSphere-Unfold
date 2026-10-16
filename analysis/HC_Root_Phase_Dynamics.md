# Does the Existing Phase Energy Preserve the Root Chamber?

Date: 2026-10-16. Status: a conditional dynamical follow-through of the [explicit root-readout audit](HC_Root_Readout.md), not a native evolution, physical lifetime or mass prediction. No main TeX, release, empirical mass or target phase is changed. The assumed isometric readout and the independent-positive-compensator completion retain their prior qualifications.

## Result

The earlier fixed-radius phase energy is exactly the same spectral energy on the normalized quadratic odd-mode branch. Its **added overdamped phase-gradient law** preserves each positive-root chamber and attracts nonzero interior phases to a same-sign minimum. Thus a mathematically consistent restricted-domain dynamics exists without fitting another phase potential.

That statement is not automatic physical stability. The boundary force is **zero**, not a strictly inward hard wall. An added inertial phase law admits finite-energy escape unless suitable initial-energy or dissipation conditions hold. A different, canonical complex two-mode extension of the same energy leaves the real/odd bilinear plane whenever the angular force is nonzero. At the selected phase its linearization is a hyperbolic saddle, because the previously identified radial descent is accessible as a relative complex-phase perturbation even at fixed mode norm.

The distinctions matter: neither the overdamped law nor the unconstrained canonical extension has been derived from the native equations. If `chi` is always an aligned extraction of `P_- f`, its oddness is kinematic and the freely complex canonical extension is not its induced evolution. One must calculate the projected dynamics instead. This is a concrete choice of missing physical structure, not a general no-go theorem for HC.

The following [projected-residual derivation](HC_Projected_Residual_Dynamics.md) now performs the exact projection of the formal native time generator, retaining the moving extraction and the discarded-component force. It supplies the autonomy criterion and angular boundary test. Fixed linear autonomous two-mode dynamics cannot preserve all three chambers with a nontrivial phase velocity; even a closed odd unitary rotation can exit. Native nonlinear feedback or an independently selected branch is not excluded, but its extraction, operator action and hidden state remain unevaluated.

## 1. Exact Dictionary Between the Two Candidate Phases

Retain the candidate `eta=1` and an aligned odd mode

```text
chi=i b(cos(theta/2),sin(theta/2)),       b>0.
```

The quadratic coordinates are `X0=b^2`, `X1=b^2 cos(theta)`, `X2=b^2 sin(theta)`, `X3=0`. Direct substitution gives

```text
L=b^2 I/sqrt(3)+b^2[exp(i theta)U+exp(-i theta)U*]/sqrt(6),
Tr L^2=2b^4,
B=L/(sqrt(2)b^2)
 =[I+(exp(i theta)U+exp(-i theta)U*)/sqrt(2)]/sqrt(6).
```

This is precisely the previous cyclic root with `a=1/sqrt(6)`, `r=1/sqrt(12)`. In chamber `j` write

```text
Phi=3theta-2pi j,       j=0,1,2,       |Phi|<=pi/4,
Q=L^2/Tr L^2=B_j(Phi)^2.
```

The earlier matrix convention uses `j=1`. The other chambers permute the three Fourier roots; the equally populated, symmetric spectral energy is unchanged. This identifies two coordinates **on the present candidate**, not its native extraction or the inherited beta-to-phase law. Amplitude normalization does not derive a mass scale.

The [source/backreaction calculation](HC_Source_Backreaction.md), sections 3--4, supplies the static energy

```text
F(Phi;k)=E_eff/(lambda_H t^2)=sum_i f_k(q_i),
f_k(q)=q^2                 for q<=k,
       2kq-k^2            for q>=k,
k=g/(2lambda_H t).
```

Here `t` is the fixed closure scale, **not time**. This energy requires an independently varied positive compensator `H`, not the native exact identity `H_C=Lambda`. The strict interval

```text
k_low=(33-23sqrt(2))/12 < k < k_high=(2-sqrt(3))/4
```

has minima `+/-Phi_star(k)`, with positive angular curvature. The previously proved radius and scale descent are not removed by the dictionary.

## 2. The Boundary Is a Stationary Point, Not a Hard Wall

At `Phi=+pi/4`, the normalized Gram eigenvalues are

```text
q_small=0,
q_middle=(2-sqrt(3))/4=k_high,
q_large=1-k_high.
```

For a fixed `k` strictly in the interval above, only the smallest mode is clamped in a neighborhood of that edge. Consequently

```text
F=q_small^2+2k(1-q_small)-2k^2,
F'=2(q_small-k)q_small'.
```

The small root itself vanishes at the edge, so `q_small'=0`. Its second derivative is `q_small''=1/27`: the root derivative there is `-1/(3sqrt(6))`, and `q''=2(root')^2` at a zero root. The same result holds at the reflected edge. Hence

```text
F(+/-pi/4)=2k-2k^2,
F'(+/-pi/4)=0,
F''(+/-pi/4)=-2k/27<0.
```

The curvature formula assumes a **strictly** interior `k`; at the endpoint an active-set change prevents taking that second-derivative formula uniformly in both parameters. Inside the chamber, a phase approaching an edge is driven back by a pure energy-gradient law. Exactly at the edge, however, its force vanishes.

## 3. A Conditional Invariant Overdamped Flow

Add, explicitly, the one-dimensional law

```text
dPhi/dtau=-m F'(Phi),       m>0.
```

Neither the positive mobility nor its time unit is derived by minimizing a static energy. In physical units a law `dtheta/dT=-mu_theta partial_theta E` would give `dPhi/dT=-9mu_theta lambda_H t^2 F'`; that conversion is not a calculation of the coefficient.

The reduced derivative is locally Lipschitz. One may see this from the smooth finite matrix family and the Lipschitz positive spectral projection in the minimized energy; the individual scalar `f_k'` are continuous and piecewise linear. Since both endpoints are equilibria, uniqueness of the first-order evolution prevents crossing them. The closed chamber is forward invariant; an interior trajectory cannot reach and cross an endpoint in finite time.

The previous phase-force sign proof is sufficient for the attractor statement. For `0<Phi<Phi_star`, `F'<0`, and for `Phi_star<Phi<pi/4`, `F'>0`. Thus every positive interior initial phase converges monotonically toward `Phi_star`; negative phases converge toward `-Phi_star`. The center and edges are unstable stationary points. Energy obeys

```text
dF/dtau=-m(F')^2<=0.
```

The mode-space lift is explicit:

```text
dchi/dtau=(Phi_dot/6) A chi,
A=[[0,-1],[1,0]].
```

It preserves both `||chi||` and fixed-conjugation oddness. It therefore stays on the assumed constant-radius Koide branch when its initial phase is admitted. It is not a derivation of native dissipative dynamics, a method preparing the initial branch, or proof of stability against additional degrees of freedom.

For an added phase drift `b(Phi)`, endpoint preservation requires `b(-pi/4)>=0` and `b(pi/4)<=0`. Because the unperturbed endpoint force is zero, any nonzero constant drift violates one of these guards, however small. Other native probe/curvature forces cannot simply be omitted in a full invariance claim.

## 4. Inertia Changes the Initial-Data Requirement

An independently postulated collective mechanical law is instead

```text
I Phi_ddot+Gamma Phi_dot+F'=0,       I>0, Gamma>=0,
E_mech=I Phi_dot^2/2+F,
dE_mech/dtau=-Gamma Phi_dot^2.
```

For an initial phase inside the chamber, the sufficient condition

```text
E_mech(initial)<F_edge=2k-2k^2
```

prevents an edge from ever becoming energetically accessible. With damping this condition need not be necessary: energy initially above the edge may dissipate before an attempted crossing. A phase initially at the edge with outward nonzero velocity can nevertheless leave immediately, despite `F'=0` there. Static stationarity is not an inertial reflecting wall.

At the illustrative, unfitted `k=0.05` and dimensionless `I=1`:

| Quantity | Conditional value |
| --- | ---: |
| `Phi_star` | `0.487058671539` |
| `F_min` | `0.0948912352574` |
| `F_edge` | `0.095` |
| `Delta F=F_edge-F_min` | `0.000108764742582` |
| Critical speed at the minimum, `sqrt(2Delta F/I)` | `0.0147488808106` |

These are dimensionless data. The physical energy gap would be `lambda_H t^2 Delta F` if that static normalization were justified. No physical lifetime, temperature, speed or mass is obtained without the missing energy and kinetic units.

There is also an explicit escape counterexample, not just an absence of proof. Start at the positive minimum with outward velocity `sqrt(2.2Delta F/I)` and no damping. Its energy is `F_min+1.1Delta F>F_edge`. The previously proved monotonic increase of `F` from this minimum to the edge ensures that its velocity never vanishes along that path. At the edge its speed remains `sqrt(0.2Delta F/I)>0`; the travel time is bounded above by `(pi/4-Phi_star)/sqrt(0.2Delta F/I)`. For the example that bound is about `63.97` in the declared dimensionless time. Thus this finite barrier does not exclude escape for arbitrary initial kinetic energy. The barrier tends to zero as `k` approaches `k_high` from below.

## 5. The Same Energy Does Not Define the Same Complex-Mode Evolution

To test a different possible physical interpretation, let `rho` be a nonzero positive two-mode matrix and extend the same readout by

```text
L(rho)=Tr(rho) E0+Tr(sigma_z rho) E1+Tr(sigma_x rho) E2,
c=Tr L^2,
Q(rho)=L^2/c,
F(rho)=sum_i f_k(eigenvalue_i Q).
```

This extension is used to compute a local tangent near the admitted pure real plane. A signed `L` outside that domain is not being called a physical principal root. Here `Q` is a generation Gram matrix while `rho` is the two-mode internal matrix; their sizes and physical roles are different.

The exact first variation is elementary. Put

```text
V=gradient_Q F=2 min(Q,kI),
G_L=[L V+V L-2Tr(VQ)L]/c,
H=gradient_rho F=h0 I2+hz sigma_z+hx sigma_x,
h0=Tr(G_L E0),       hz=Tr(G_L E1),       hx=Tr(G_L E2).
```

The last term in `G_L` comes from differentiating the normalization `c`; dropping it would give a different energy gradient. `H` is a real symmetric matrix. Add the **different** canonical two-mode evolution

```text
rho_dot=-i[H,rho].
```

It preserves trace, purity and `F`, rather than decreasing `F`. For a pure trace-one input write

```text
rho=[I+X1 sigma_z+X2 sigma_x+X3 sigma_y]/2.
```

On the aligned plane `X1=cos(theta)`, `X2=sin(theta)`, `X3=0`, the commutator gives

```text
X3_dot=2(hz X2-hx X1)
      =-2 partial_theta F
      =-6 F'(Phi).
```

Thus whenever the angular energy slope is nonzero, the canonical flow leaves the plane whose bilinear identity supplied Koide. A common amplitude phase does not change `rho` or `X3`, so this is not removable by a state-only phase convention. While `L` remains positive, for short dimensionless time `epsilon` one has

```text
2/3-K=X3^2/3
     =12[F'(Phi_initial)]^2 epsilon^2+O(epsilon^3).
```

At `k=0.05`, `Phi_initial=0.3`, the exact initial derivative is approximately `F'=-0.000495987392269` and `X3_dot=0.00297592435362`. Finite matrix differentiation reproduces both signs and the factor of six. This calculation does not identify this mode evolution with the native probe equation.

## 6. The Angular Minimum Is a Saddle in This Canonical Extension

At `Phi_star`, `F'=0`, so the real pure density is stationary under the canonical law. To test stability, introduce the independent relative-phase coordinate `y=X3`:

```text
X1=sqrt(1-y^2)cos(theta),
X2=sqrt(1-y^2)sin(theta),
X3=y.
```

These are still pure trace-one matrices; no change in probe norm or physical transfer `eta=1` has been made. But the normalized generation-root radius becomes

```text
s(y)=r/a=sqrt(1-y^2)/sqrt(2).
```

The old radial descent is therefore available as a transverse perturbation. Since `s'(0)=0` and `s''(0)=-1/sqrt(2)`, the exact Hessian entries at the angular minimum are

```text
F_PhiPhi>0,
F_yy=-(1/sqrt(2)) F_s<0,
F_Phi_y=0.
```

The strict sign of `F_s` can be seen without a fit. At the stationary branch both small Gram modes are below `k`, the largest is above it, and the angular derivative vanishes. Using the independent `(Phi,s)` variation of the two small `q_i`, an increase in `s` moves the small-root pair away from the fixed-trace minimum. More explicitly, with `theta=(2pi+Phi)/3`, each small-mode eigenvalue at `s=1/sqrt(2)` is

```text
q_i=(1+2s cos(theta+2pi i/3))^2/(3+6s^2),
partial_s q_i=[4cos(theta+2pi i/3)(1+2s cos(theta+2pi i/3))
              -12s q_i]/(3+6s^2)<0.
```

Their root coefficients are positive and their two cosines are negative throughout the strict positive-root chamber. Since `q_i<k`, the energy identity `F=2k-3k^2+sum_(q_i<k)(k-q_i)^2` then gives `F_s=-2sum_(q_i<k)(k-q_i)partial_s q_i>0`. This proves the transverse negative curvature throughout the strict interior-selection branch, not just at the numerical example.

The canonical coordinate equations follow from the same commutator:

```text
Phi_dot=6 F_y,       y_dot=-6 F_Phi.
```

Linearizing at `(Phi_star,0)` gives

```text
J=[[0,6F_yy],[-6F_PhiPhi,0]],
eigenvalues(J)=+/-6sqrt(-F_PhiPhi F_yy).
```

At the illustrative threshold, `F_PhiPhi=0.00529273379816`, `F_yy=-0.00525092784768`, and the rates are approximately `+/-0.0316307362937`. They are dimensionless. The stationary point is a hyperbolic saddle for this canonical extension, despite its positive angular curvature. This is consistent with energy conservation: a positive angular quadratic contribution can exchange against the negative transverse one.

If an independently derived correction is even in `y`, stationary at the same phase, and leaves the angular curvature positive, local positive definiteness would require its extra transverse curvature to exceed `-F_yy` (about `0.00525093` in this normalization at the example). If there is a mixed Hessian term, positive determinant must also be checked. This is a **test target**, not a supplied repair: no fitted stiffness or new potential was added. Damping alone does not turn an energy saddle into a full energy minimum.

## 7. Native Interpretation and Next Requirement

The native action cited in `Phase_Selection_Derivation.md`, section 1, does not yet identify `chi`, its kinetic law or an induced real-structure constraint. Its other probe/curvature phase forces also remain unevaluated. A static compensator minimization supplies none of those missing ingredients by itself.

There are consequently distinct research routes:

- If `chi=E_native P_- f` with an independently established intertwining `E_native J=K_complex E_native`, then `X3=0` is kinematic. The canonical complex extension above is not the projected evolution of that residual unless this is separately proved. One still needs its actual induced angular law and a proof that the admitted angular chamber is preserved.
- If `chi` is a freely complex canonical two-mode background with exactly the auxiliary energy computed here, the real plane is not generally invariant and the selected point is a saddle. An independently derived constraint or additional transverse restoring interaction is required; imposing one does not derive its native origin.
- If the phase is a collective mechanical coordinate, a kinetic metric, initial-energy bound or evaluated dissipation must be supplied. Energy below the finite edge barrier is sufficient for trapping in the reduced model, not a native preparation mechanism.

All routes still require the native extraction, independent metric transfer, equality with the actual transition Gram, mass/gauge/current matching, radius/scale support and the other full-field variations. The present results neither select the empirical phase nor repair the Planck-scale readout, exact closure or OP5/C5. No publication or Git operation is performed.

## Reproduction

`python -B analysis/HC_Root_Phase_Dynamics.py --output analysis/HC_Root_Phase_Dynamics.json` reproduces the report. The 37 tests in `scripts/qsc_audit/tests/test_hc_root_phase_dynamics.py` cover the exact phase/root/Gram dictionary, boundary derivatives, gradient directions and odd-mode lift, a monotone implicit-flow check, inertial energy and escape conditions, the canonical matrix gradient and conserved quantities, generated relative phase, transverse radius/Hessian and the saddle linearization. Finite differences and sample trajectories supplement the written algebra; they are not substitutes for a native dynamical derivation. Existing NumPy is used without installing a package.
