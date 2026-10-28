# Torsion source shape and nonzero coframe curvature response

2026-10-27. Conditional continuation of OP5_Torsionful_Geometric_Witness.md. Full action normalization and probe realization remain open.

Use E=I, j^a=(2t,0,0,0), omega^i_0=omega^0_i=dxi/t for t>0. Convention R=domega+omega wedge omega. Define T_a=T^b_ab and the normalized Cartan combination

 A_ab^c=T^c_ab+delta_a^c T_b-delta_b^c T_a.

The torsion trace is T_0=-3/t, T_i=0 and the only independent nonzero components of A are A_0i^j=2 delta_i^j/t. This tests the source tensor shape; the action's gravitational coefficient, spin-current convention and sign must be restored before identifying a physical lambda.

With j_b=(-2t,0,0,0), choose the normalized algebraic multiplier

 lambda_tilde_a^c=diag(0,1/t^2,1/t^2,1/t^2).

Then lambda_tilde_a^c j_b-lambda_tilde_b^c j_a=A_ab^c exactly. The row parallel to j is unconstrained by this wedge map. Thus the existing multiplier-source STRUCTURE can carry the required pure-vector torsion response. This is not a solved connection equation with a multiplier fixed by the full coframe variation. The nonzero Dirac spin source has not been supplied or canceled.

Independently, direct computation of the connection curvature gives

 Ric_ab[omega]=diag(3,1,1,1)/t^2,
 R[omega]=eta^ab Ric_ab=0.

This is not the Levi-Civita Ricci tensor of the flat metric, which vanishes. Nonzero Ricci with zero scalar demonstrates why evaluating the scalar-curvature Lagrangian on the ansatz before variation would miss a coframe equation: its value being zero does not make its unrestricted variation zero. In a first-order geometric action the nonzero curvature response must be balanced by the full probe stress and multiplier reaction. Calling the displayed tensor a derived radiation fluid or an ordinary Einstein solution would be premature.

Result: there is no immediate tensor-shape obstruction to the multiplier supplying this torsion. There remains a simultaneous normalization/source/coframe problem: lambda cannot be chosen independently in both equations, and the actual cross bilinear and spin/stress of the same probes must realize the required values. Absolute vacuum-energy selection and native OP5 closure are not established.

OP5_Torsion_Source_Check.py evaluates every torsion/source component, Ricci tensor and scalar exactly with SymPy. The JSON records the normalized nature of lambda_tilde explicitly.
