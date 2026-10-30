# All-order symbol structure and the remaining nonlinear existence gap

30 October 2026. Route C, independent of the fitting code. Baseline f0f2b9e; current local evidence fifth-window-result.json. New algebraic derivation, exact minor certificates, bounded numerical tableau check and verified primary-source hypotheses. This document is not a proof of OP5 or regional existence.

## 1. Principal symbol factorization for every covector

Treat the12 complex field components as24 real variables. At a regular first jet set

- B: R4 -> R24, whose columns are the real-packed covariant jets C_mu=D_mu Psi;
- A: R24 -> R4, A(v)_a=Re(Psi† Q_a v);
- E=AB, assumed invertible;
- P=I-B E^-1 A, so P²=P, image P=ker A and kernel P=image B.

Changing first jets by delta C_mu=xi_mu v changes E by A(v) tensor xi. Differentiating the inverse coframe gives

delta F = H(xi)[v-B E^-1 A(v)] = H(xi)P v,

where H(xi)=realify(i sum_a eta_a (I tensor K_a)), eta=xi^T E^-1. The original mass term has no principal contribution. Consequently every principal matrix shares the four-dimensional right kernel image B. In particular det J(xi) vanishes identically: the unreduced24-component system has no noncharacteristic hypersurface in the square-system CK sense. Invertibility of the frozen Dirac factor H(xi) does not make the full symbol invertible.

The symbol is constant-linearly equivalent to H(eta) restricted to ker A plus four kernel directions: any projector with image ker A can be used to inspect its dimensions. This does not identify the four directions with a regional gauge symmetry.

## 2. Complete polynomial left syzygies: a conditional algebraic theorem

Work over k=R (or its complexification), S=k[eta0,eta1,eta2,eta3], with q=eta0²-eta1²-eta2²-eta3². Put D=H(eta). Its Clifford conjugate Dbar satisfies D Dbar=Dbar D=q I. Let ell=(-Im((S_internal tensor I)Psi), Re((S_internal tensor I)Psi)) be a real row. Direct conjugation gives ell D=eta^T A. Define the4x24 linear matrix K=A Dbar. Then

ell D P=0, K D P=0, eta^T K=q ell.

Assumptions: A has row rank4 and K reduced modulo q has rank3 over the fraction field of S/(q). These are nondegeneracy hypotheses, not a claim for singular states.

**Claim.** Under these hypotheses every polynomial row l with l D P=0 has the form l=c ell+w K, c in S, w in S4. The only relations among these five generators are multiples of q ell-eta^T K=0. In graded notation the left-syzygy module M has resolution

0 -> S(-2) -> S direct-sum S(-1)^4 -> M -> 0,

where the first map is t -> (q t,-eta^T t), and the second is (c,w) -> c ell+w K.

**Proof.** Since image P=ker A and A has constant full row rank, l D P=0 means l D=v A for a unique polynomial row v of length4. Multiplication by Dbar yields q l=v K. Reduce modulo q. In the fraction field of R=S/(q), the left kernel of K is one-dimensional and contains eta^T, hence v=f eta^T for some rational f. The ring R is a normal domain: q is irreducible of rank4, its hypersurface is Cohen-Macaulay, and its only singular point is the origin, which has codimension3. Serre's criterion therefore applies. For every height-one prime of R, at least one eta_i is outside that prime; otherwise it would contain the maximal ideal of the origin. Since f eta_i belongs to R, f belongs to every height-one localization. Normality gives f in R. Lift f to c in S and write v=c eta^T+q w. Then q l=q(c ell+w K), so cancellation gives l=c ell+w K.

If c ell+w K=0, multiply by D to obtain (c eta^T+q w)A=0. Full row rank of A implies c eta_i+q w_i=0 for each i. Since q is prime and does not divide eta_i, q divides c. Thus c=q t and w=-eta^T t. This proves exactness and uniqueness of the displayed relation. End proof.

This is a symbol-module statement, not a nonlinear formal-integrability theorem. Its rank hypothesis can be checked by one nonzero3x3 minor at a nonzero null covector: such a minor cannot vanish identically modulo q. The exact test below does this.

## 3. All-order dimension formula, no interpolation needed

Let p>=1 denote the highest field-jet order. Rows of its homogeneous prolonged symbol correspond to24 residual components and monomials of degree p-1 in four variables. The theorem gives the complete dimension of its left kernel:

d_p = C(p+2,3)+4 C(p+1,3)-C(p,3) = p(p+2)(2p-1)/3.

Here binomial coefficients with top<3 are zero. Thus rank A_p =24 C(p+2,3)-d_p, conditionally for every p, not merely the tested p. The deficits are1,8,25,56,105,176 at p=1..6; the corresponding ranks are23,88,215,424,735,1168. This explains the observed rank sequence through degree6. Rank agreement alone was not the proof; the saturation argument above supplies the all-order implication under named hypotheses.

## 4. Source constraints and exact lower-residual terms

Write the total first derivative as

partial_mu F = sum_nu J^nu Psi_nu_mu + b_mu,

where b_mu=F_xmu+F_Psi Psi_mu uses partial derivatives with first jets held fixed. Let K(xi)=sum_mu K^mu xi_mu in the actual coordinate coframe. The polynomial syzygy K(xi)J(xi)=0 cancels the symmetric second jets, giving four first-order functions

G = sum_mu K^mu b_mu = sum_mu K^mu partial_mu F.

The scalar function g=ell F=4-h Psi†(Z tensor beta)Psi/2 contains no first jets. Consequently the8 first-prolongation compatibility rows are generated by the four derivatives of g and the four G rows. Off shell, partial_mu g=ell partial_mu F+(partial_mu ell)F; the second term must not be dropped.

At arbitrary order r, Leibniz gives

ell partial^alpha F = partial^alpha g - sum_(0<beta<=alpha) binom(alpha,beta)(partial^beta ell)partial^(alpha-beta)F,

and

sum_mu K^mu partial^(gamma+e_mu)F = partial^gamma G - sum_mu sum_(0<beta<=gamma) binom(gamma,beta)(partial^beta K^mu)partial^(gamma-beta+e_mu)F.

For |alpha|=p-1 and |gamma|=p-2, the remaining F derivatives on the right have order at most p-2. If all those lower F derivatives vanish, the complete highest-jet compatibility conditions are precisely the indicated derivatives of g and G, modulo their one symbol relation. Thus, at a fixed lower jet satisfying the prior original equations and the module hypotheses, these source tests are necessary and sufficient for solvability of the next *linear highest-jet system*. This is a useful exact stopping/repair contract.

It does not assert that lower jets satisfying all these conditions can be selected coherently at every p. Completing the first-order equation with g,dg,G changes the admissible state/first-jet manifold and its tableau. Its regularity, torsion and projection maps still require analysis. Exact scalar parametrization can remove g and all its derivatives structurally, but cannot by itself remove the four G functions or establish their propagation.

## 5. Exact and finite checks executed

Run `python all_order_criteria_symbol.py` from repository root. The native Clifford coefficients satisfy D Dbar=qI exactly by coefficient comparison. For each of the three decimal-recorded field values, interpreted as exact rational real/imaginary entries, the script constructs exact nonzero4x4 A minors and exact nonzero3x3 K minors at eta=(1,1,0,0). The exact row relation K0+K1=0 bounds null rank by3. These certificates prove the algebraic rank hypotheses at those rational states and on a nonempty open state neighborhood. They do not prove an exact nonlinear root exists in that neighborhood.

A simple rational example Psi=(1,0,...,0) also passes, showing the null-rank condition is generically nonempty. Its physical admissibility is not asserted.

For the canonically equivalent numerical symbol, all three states and four fixed flag choices give restriction dimensions24,47,69,73, hence tableau characters(24,23,22,4). The first symbol kernel has dimension73; its first prolongation has dimension152, equal to24+2*23+3*22+4*4. This is a bounded numerical Cartan-test check of the original homogeneous tableau, not proof that the nonlinear completed EDS is ordinary.

## 6. Verified existence theorems and exact application gaps

### Cauchy-Kovalevskaya

Tsogtgerel Gantumur, *MATH580 Lecture Notes2: The Cauchy-Kovalevskaya Theorem*, dated3 October2011, Theorem18, states analytic existence/uniqueness for a system in normal form partial_n u=f(z,u,partial_1u,...,partial_(n-1)u) with analytic data (zero data in its normalized statement). The proof supplies an analytic majorant. Source authenticated and statement read at the author's official McGill URL: https://www.math.mcgill.ca/gantumur/math580f11/downloads/notes2.pdf .

Application here is conditional. The unreduced symbol is singular for every covector. A legitimate state chart, analytic choice of undetermined components, a solved noncharacteristic subsystem, compatible analytic initial data and propagation of all leftover constraints would have to be constructed. A pointwise time-coframe fixing and numerical time-rank20 are insufficient. The exact missing arrow is: the reduced analytic evolution preserves the full completed constraint set. Merely prescribing controls for undetermined components is not a proof that they are gauge transformations.

### Cartan-Kähler

Robert L. Bryant, *Notes on Exterior Differential Systems*, arXiv1405.3116v1,13 May2014, draft0.30.3 last modified12 May2014, Theorem1, states existence of a real-analytic integral manifold through a Cartan-ordinary integral element for a real-analytic positive-degree EDS. Section1.4 defines ordinary by smoothness and actual local codimension equality with Cartan's polar bound; section2.2 gives the tableau test. Source: https://arxiv.org/html/1405.3116v1 . These notes state the theorem and refer elsewhere for its full proof.

Application here is conditional. One needs an exact integral4-plane on a smooth analytic completed jet manifold and an ordinary flag. Involutivity of the original symbol and torsion absorption at one isolated numerical jet do not ensure projection onto a neighborhood of the lower equation manifold. A sufficient finite check is actual smooth integral-element variety of the polar-predicted codimension; alternatively prove the relevant prolongation projection is locally onto with the completed tableau involutive. Current sampled ranks and approximate high jets identify candidates, not those exact neighborhood hypotheses.

### Direct convergent-coefficient route

There is an elementary sufficient alternative: a single coherent infinite coefficient family solving every residual coefficient, with ||c_alpha||<=M R^(-|alpha|), would converge absolutely on each smaller coordinate polydisc. Indeed the norm sum is bounded by M sum_n C(n+3,3)(r/R)^n=M/(1-r/R)^4. Derivatives converge on smaller radii. Invertibility of E at the base point then persists in some neighborhood, and analyticity forces the residual to vanish. The current moving lower jets do not form such a coherent family, and no uniform M,R estimate is established.

## 7. Algebra source record

The normal-quadric step uses regular local rings being Cohen-Macaulay (tag00NQ, Lemma10.106.3; https://stacks.math.columbia.edu/tag/00NQ ), and the following primary Stacks Project lemmas, statements read on30 October2026: Serre criterion normal iff R1+S2 (tag031S, Lemma10.157.4); regular-sequence quotient of a Cohen-Macaulay local ring remains Cohen-Macaulay (tag02JN, Lemma10.104.2); a finite reflexive module over a Noetherian normal domain is the intersection of its height-one localizations (tag0AVB, Lemma15.24.18, apply to the ring itself). URLs: https://stacks.math.columbia.edu/tag/031S , https://stacks.math.columbia.edu/tag/02JN , https://stacks.math.columbia.edu/tag/0AVB . Polynomial local rings are regular; quotient by the nonzero q is a hypersurface; the rank4 quadric is smooth away from its origin. No full source text was copied into the artifact.

## Conclusion and first unresolved implication

The homogeneous compatibility structure now has a conditional all-order derivation and exact native-state rank certificates. The open part is nonlinear: obtain a regular, formally compatible completed constraint manifold with locally surjective prolongation maps, or a single coherent coefficient family with a convergence bound. This is the actual difference between arbitrarily many separately repaired finite fits and an analytic solution. The core theorem and physical OP5 identification remain outside the established result.
