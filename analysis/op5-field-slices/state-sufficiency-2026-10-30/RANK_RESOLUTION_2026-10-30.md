# Recursive rank resolution checkpoint — 2026-10-30

## Tested assertion and scope
Frozen real symbol of the fixed comparison model, augmented by the recorded Omega covector. This is a finite numerical symbol diagnostic, not nonlinear formal integrability, regional existence, or physical validation.

Command: `python recursive_spencer_basis.py` (Python 3.12, NumPy, float64).
Authoritative input hash is stored in `recursive-spencer-result.json`.
The implementation uses factorial-balanced symmetric coordinates and forms each higher symbol as the common kernel of the four contractions into the preceding symbol complement. Orders 2 and 3 are initialized from the direct row-equilibrated completed symbol. Rank selection is 1e-9 relative; no expected dimension is forced.

## Observed result
Dimensions at degrees 2..6 are 127, 208, 308, 427, 565, agreeing with the direct construction. Recursive constraint matrices have clean retained/discarded gaps through degree 6 (last retained degree-6 singular value about 3.05e-5, next about 3.05e-12).

The Spencer complex product norms at degrees 3,4,5 are 6.02e-12, 1.05e-11, 1.51e-11, improving on the original raw direct construction. At degrees 3 and 4, H^(p,2) rank arithmetic gives zero for every tested cutoff 1e-8 through 1e-11.

Degree 5 remains unresolved: the computed dimension is 1 at cutoffs 1e-8 and 1e-9, zero at 1e-10, and minus one at 1e-11. The negative value cannot describe exact cohomology and diagnoses numerical inconsistency at that resolution. Incoming singular values near the boundary include 8.04e-10 and 1.17e-10; neither can currently be declared an exact zero or a true nonzero.

The existing independent balanced-coordinate outputs also retain cutoff dependence. Thus coordinate scaling alone does not settle this issue. Recursive SVD stabilizes the construction but still defines a nearby numerical tableau when the input covector and initial symbol are rounded.

## Consequence and next discriminating step
No new fifth-degree obstruction is established. Nor is fifth-degree acyclicity established. The earlier nontrivial third-jet Omega source remains a separate, independently checked numerical result.

Further ordinary float64 rank sweeps are unlikely to discriminate these alternatives. The next useful calculation must preserve the algebraic differential identities while reconstructing the initial symbol and Omega at higher precision, or derive a symbolic module presentation with exact syzygies. Merely converting the rounded NPZ arrays to high-precision numbers would not restore identities already lost in their construction. The necessary first subproblem is to reconstruct Omega from the underlying source/left-kernel calculation with a consistent precision and normalization, rather than treating its stored decimals as exact PDE data.

No repository files were changed, and no commit or push was performed.
