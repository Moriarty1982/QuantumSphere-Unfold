# Repaired fifth-order completion at high precision

Base repository commit b1214c934ce8ed4094ff572dd94111ac1e7a75c3 was committed and pushed before this continuation. The present files are new workspace research, not yet committed.

The frozen repaired fourth jet failed fifth-order completion. We tested four deterministic random directions in the NEW640x840 fourth-symbol kernel. Each direction was refined against all640 prior equations at70digits, with leakage between9.20e-71 and1.56e-70. Field coefficients throughdegree3 were fixed. Seed3010305 and all four directions/source differences are retained.

The degree4 source is affine in fourth field coefficients at fixed lower data: a field change begins atdegree4 and its first derivative atdegree3, so no product of two changes contributes todegree4. Four separately recomputed sources define a restricted source gate. Its four singular values are0.17059,0.09704,0.02535,0.00958. It spans the particular observed incompatible source to float residual1.65e-10. This does not prove that the full source gate has only rank4 or that arbitrary compatible data extend.

Four left witnesses corresponding to the measured gate are refined against all1344 fifth-symbol columns to errors below6.23e-70. A70-digit4x4 solve gives correction parameters about(582.44,-260.98,997.51,528.52). The maximum real normalized fourth-coefficient change is191.79. This is a substantial change of the selected higher derivatives, not a rounding repair or a physical scale. The parameter-scaled prior-equation leakage is1.56e-67.

The corrected source is recomputed directly, not accepted from a linear prediction. Its difference from the affine prediction is1.00e-63. Re-solving fifth coefficients gives maximum residual2.75e-62 over ALL1120 degree4 completed equations; selected907 rows are below1.72e-66. Therefore the omitted compatibility rows also pass numerically.

Direct evaluations along four coordinate axes and a mixed direction check completed R derivatives throughorder4 on the corrected degree5 field polynomial. The maximum tested normalized residual is3.81e-61, and lower orders remain small. These checks bypass prolonged-matrix assembly but share the analytic R evaluator. Independent formula review is in precision_fifth_gate_review.md.

Conclusion: one common70-digit numerical field jet throughdegree5 now satisfies completed R throughdegree4 after selecting fourth coefficients appropriately, with field0..3 fixed. The earlier frozen-fourth failure is preserved and remains correct for that earlier choice. This is finite compatibility and an improved precision reconstruction, not a general all-order result beyond the earlier low-precision finite-order experiments.

Open: exact/interval certification, full Omega covector at the repaired germ, fifth-degree Spencer rank resolution, uniform growth/convergence, regional and native physical existence. Four successful correction directions for one source do not close these gaps. A next discriminating step is the sixth extension at this common lower germ, or reconstruction of the source-gate law rather than repeated finite fitting.

Commands: python precision_fifth_gate.py; python precision_fifth_gate_repair.py; python precision_fifth_gate_check.py. Files retain actual source recomputations, coefficients, directions, residuals and seeds.
