# Independent review: completed high precision first jet

Reviewed `precision_completed_rebuild.py`, `precision_completed_root.py`, and `precision_primitive_rebuild.py` by direct formula inspection. No calculation was rerun and no repository file was changed. This review checks the finite model implementation, not formal integrability or physical validity.

## Formula dictionary and findings

Let j_mu=partial_mu psi, C_nu=j_nu+i A_nu psi, E^a_nu=Re(psi^dagger Q_a C_nu), V=E^{-1}, and F=i sum V^{nu}_a K_a C_nu-hYpsi.

The code uses d_mu psi=j_mu and sets the symmetric second jet partial_mu j_nu to zero in the source part. It consequently obtains d_mu C_nu=i[(partial_mu A_nu)psi+A_nu j_mu]. Its dE contains both differentiated psi^dagger and differentiated C terms. The inverse derivative dV=-V(dE)V is correct. The implemented b_mu differentiates both V and C in F and includes both mass derivatives -(partial_mu h)Ypsi-hYj_mu. Thus b_mu is exactly the lower source term obtained by setting the second jet to zero; no derivative term is visibly omitted.

A=Re/Im realification of psi^dagger Q is correctly [Re(a),-Im(a)] on vectors packed [Re(z),Im(z)]. The conjugate symbol uses realify(-i K_0) in time and realify(+i K_i) in space. Therefore the code's km=A sum V^{mu}_a Hbar_a agrees with the earlier K^mu syzygy convention. G=sum K^mu b_mu is the intended first-order source function. Dropping the second jet is legitimate only because the complete symmetric coefficients K^mu J^nu+K^nu J^mu vanish; the independent saved ten-coefficient cancellation test addresses exactly this issue at its stated seed.

For g=4-(h/2)psi^dagger Zpsi, with Z Hermitian, d_mu g=-(partial_mu h/2)psi^dagger Zpsi-h Re(psi^dagger Zj_mu). This matches C[mu]. No connection term should be inserted into this ordinary scalar derivative.

The derivative variables are 96 real components, grouped by coordinate, then 12 real and 12 imaginary components. `mp.mpc(real,imag)` builds complex field components from these real arguments. Default `mp.diff` differentiates along the real scalar increment; it does not require holomorphic dependence on the packed variables. Consequently `conjugate` and `re` operations are compatible with this use. The central-difference controls are consistent checks of this convention, though two columns are not a complete independent Jacobian validation.

## Newton and claim calibration

The row selection is a float64 numerical diagnostic with absolute tolerance 1e-9, not an exact rank certificate. Subsequent corrections use mpmath normal equations on the 31 selected rows. Squaring the condition number through A A^T warrants watching conditioning in future runs. Here the full 32 residuals are evaluated afterward, so an omitted incompatible row cannot silently pass merely because it was excluded from the solve. The reported residuals support a numerical completed first-jet root, conditional on this implementation and arithmetic, not an exact root or convergence proof.

The scalar-repaired psi is held fixed in the completed solve, but all first derivatives change. The high precision symbolic background is reconstructed rather than promoting the old float64 matrix. This is appropriate. Fixed helper evaluation at SymPy precision 85 is adequate for the present 70-digit calculation; it is a hard ceiling to revise before advertising arbitrarily higher working precision. Default mpmath differentiation may internally use more precision, but it differentiates the already stored numerical constants, not a newly higher-precision background.

## Consequences for Omega

A new completed first-jet root changes the principal completed symbol, higher source functions, and any representatives of their quotients. The former theta or ambient left witness cannot be appended to the new symbol as though it were recomputed there, even when first-jet changes are tiny. Rank agreement alone will not transfer the nonlinear compatibility condition. Rebuild the higher source quotient with a common lower germ, then compare the new covector modulo the original equation rows and a nonzero scale, not entrywise.

The first-jet root alone also does not supply a compatible second or third jet. Before evaluating a new third-jet Omega source at a germ, reconstruct those lower prolongations at the same precision or establish the needed exact projection argument. A symbol-only computation at the first jet can still be informative if it is explicitly labelled frozen-symbol analysis.

No substantive formula error was found in the reviewed expressions. Remaining limitations are numerical rank selection, lack of an exact root certificate and higher-jet reconstruction, and the need for independent validation of the full Jacobian/source quotient. These limitations do not invalidate the narrower finite first-jet result.

## Reuse note

Importing `precision_completed_rebuild.py` executes checks and overwrites `precision-completed-result.json`. This is an execution/provenance side effect, not a mathematical error. Future reusable modules should place diagnostic execution under a main guard or separate pure evaluator construction from result writing, so a symbol calculation does not silently replace a prior timed evidence record.
