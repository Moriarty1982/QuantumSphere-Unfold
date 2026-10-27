# Connection reaction of the constrained cross readout

2026-10-27. Continuation after checkpoint cf9e16718beb420afc5b93ce38ef905fd9fa8347. Exact multiplier variation within a declared independent-Lorentz-connection parent; not a complete native variational solution.

## Parent and variation convention

Let E and antisymmetric Lorentz connection omega_mu^{ab} be independent. Assume compatible bilinears and a parallel internal selector, so the cross readout is C^a_mu=(1/2)D_mu j^a. Add to a first-order geometric plus probe action

 S_constraint=integral d4x lambda_a^mu[E^a_mu-(1/2)(partial_mu j^a+omega_mu^a_b j^b)].

Here lambda is a real density; j is held fixed during the independent connection variation. Lower Lorentz indices with eta. Direct variation gives

 delta_omega S_constraint
 =-(1/4) integral d4x (lambda_a^mu j_b-lambda_b^mu j_a) delta omega_mu^{ab},

with summation over all antisymmetric index pairs. If instead coefficients are defined only for a<b, the coefficient is doubled. This specifies the convention and avoids attributing a numerical factor to an undefined spin-current convention.

Define pi_ab^mu and s_ab^mu to be the coefficients of delta omega_mu^{ab} in the geometric and probe variations in the SAME full-index convention. The connection equation is

 pi_ab^mu+s_ab^mu-(1/4)(lambda_a^mu j_b-lambda_b^mu j_a)=0.

For ordinary nondegenerate Einstein-Cartan/Palatini geometry the geometric connection variation is a torsion-dependent expression. On a torsion-free compatible branch that contribution vanishes; hence the necessary condition is

 s_ab^mu=(1/4)(lambda_a^mu j_b-lambda_b^mu j_a).

The constraint reaction is therefore not optional. Its value must follow from the coframe equation together with probe stress, vacuum and other geometric contributions, rather than being freely chosen to cancel spin. No full coframe equation or native spin representation has been solved here.

## Elementary necessary control

If the probe spin coefficient vanishes on a proposed torsion-free state, the condition reduces to lambda^mu wedge j=0 for every mu. At a point with j!=0 this requires each Lorentz covector lambda_a^mu to be proportional to j_a; therefore lambda, viewed as a four by four matrix, has rank at most one. Any candidate with spin zero and a full-rank multiplier reaction fails this torsion-free connection equation immediately. This rank statement is algebraic and applies also to a nonzero null j.

For example a pure volume-term coframe reaction proportional to det(E)E^-T is full rank when its coefficient is nonzero. Under the simultaneous additional assumptions of zero probe spin and no other coframe stresses/reactions modifying that multiplier, it cannot satisfy the torsion-free condition with nonzero j. This is a restricted negative control, not a no-go for vacuum terms with general probe stress, nonzero spin or torsion.

## Coupled integrability

The dictionary independently implies T^a=(1/2)R^a_b j^b. One must solve that relation AND the connection equation above. Setting T=0 first requires both R j=0 and spin/constraint balance. Allowing T!=0 may avoid the earlier torsion-free restriction but supplies a new coupled problem, not a proof that it has a solution. Calling the result ordinary torsion-free GR before these equations are solved would be premature.

## Next concrete obligation

Choose the native-compatible real probe action and its adjoint, calculate s_ab^mu and the full coframe reaction lambda from that SAME action, then test whether the torsion-free balance is possible or torsion is required. The result so far identifies a previously omitted source and a fast algebraic rejection test. It does not select an absolute vacuum coefficient or close OP5.
