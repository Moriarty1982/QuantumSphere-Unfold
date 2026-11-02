# High precision primitive restart

Checkpoint after commit 3d818f4. Run: `python precision_primitive_rebuild.py`.

The fixed comparison model is reconstructed from its symbolic background and decimal-recorded lower data at 40 and 70 digits. Analytic identities AP=0, P^2=P, ell J=0 and ell F=g are evaluated directly, without converting the old rounded symbol matrix to high precision.

At 70 digits, the original recorded first jet has max complex field residual 1.52345e-14 and scalar residual 1.00445e-15. The scalar chart repairs Re(psi_0) by 3.79823e-16. Four Newton steps then adjust the 96 real first derivative components, with max complex component change 2.11284e-14. One redundant real F row is omitted according to the largest component of ell, and the analytic full principal Jacobian gives a minimum-norm correction on the remaining 23 rows. All 24 real equations are checked afterward.

Full max complex F residual is 7.34e-71 at 70 digits and 1.43e-40 at 40 digits. The scalar and symbol identity errors track the working precision. Both runs have the same displayed derivative correction. The coframe determinant remains about 13.63456.

This establishes a useful numerical restart for F and g only. It does NOT solve the completed G,dg constraints, establish convergence, rebuild Omega, or resolve the degree-5 Spencer question. Lower data were explicitly changed; this is not a frozen-data compatibility result. No interval or exact root certificate is claimed. The precise repaired coefficients are saved separately for both precisions.

Next prerequisite: reconstruct the completed first-order system and its derivative constraints with the same precision, and repair those before computing the higher source quotient. The existing Omega witness must not be reused as if it were recomputed at this new first jet.
