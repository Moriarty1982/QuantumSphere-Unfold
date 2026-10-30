# Completed high precision restart — checkpoint

The new evaluator reconstructs R=(F,G,dg) analytically from the exact symbolic background, using mpmath at 70 decimal digits and the repaired primitive first jet as input. It avoids feeding the old float64 completed symbol into a high precision solver.

The primitive root did not automatically solve the completed conditions: max G was 9.65e-14 and max dg was 5.46e-14. This is a source compatibility issue distinct from F alone.

`precision_completed_root.py` keeps psi fixed and releases all 96 real first derivatives. mpmath differentiation builds the full 32x96 Jacobian. A float64 row-selection diagnostic picks 31 independent equations; the Newton correction uses 70-digit arithmetic on those rows. Crucially all 32 original residual components are re-evaluated after each update. Thus selection is not treated as an exact rank proof.

The separate `precision_hessian_cancellation.py` checks all ten symmetric Hessian coefficients of sum K^mu d_mu F. Their max magnitude is 3.20e-71, supporting the implemented cancellation of second derivatives from G at this seed. Two independent central-difference column checks decrease their discrepancy by 1e8 when the step changes from 1e-8 to 1e-12, as expected for a second-order difference.

The final Newton history and all repaired first derivatives are in `precision-completed-root-result.json`. This is a numerical first-jet root of the completed system, not a certificate of an exact solution, higher-jet propagation, or a regional field. It changes lower first derivatives, so previous higher-jet witnesses cannot be attached to it without recomputation.

The next dependency is now precise: reconstruct the higher completed source quotient and its Omega covector at this new root, preserving the high precision identities. Degree-5 cohomology is still unresolved. No repository files have been changed in this continuation.
