# 4.10 draft validation — 30 October 2026

This is an unpublished research draft, not a release or an OP5 closure certificate.

- Full manuscript: MiKTeX pdfTeX 4.23 (MiKTeX 25.12), direct pdflatex, final two passes successful; 1,312 pages. The latexmk wrapper stalled before compilation and was stopped; direct compilation is the verified fallback.
- Final log: zero fatal errors, undefined references, undefined citations, duplicate labels, or pending rerun warnings. The repository research build gate passes using an explicitly labelled direct-build summary.
- Layout: 58 overfull horizontal boxes and zero overfull vertical boxes remain, matching the documented MiKTeX baseline count. These older layout warnings are not resolved by this consolidation. No overfull warning occurs in the new synthesis section. Visual inspection sampled the title, changed legacy qualifications, regularization, new synthesis and original figure, including final pages 162–163; this is not a visual review of all pages.
- Metadata-hygiene unit tests: six passed. Scoped audit of seven affected TeX files: zero errors, 160 warnings, 95 informational findings. Historical version/DOI and draft notices remain; this was not a whole-repository release audit.
- Wolfram exact check: corrected regularization primitive differentiates to the stated integrand for positive argument. At T=0.393 and reference scale mu=1, the finite part is 1.686953464176554392849829545645. The endpoint expansion begins -1/t + 1 - 11t/24. Reference-scale dependence is retained; this is not a physical mass derivation.
- Focused mathematical and notation self-review keeps conditional reconstruction, numerical compatibility, and unproved physical identifications distinct. No whole-manuscript referee certification is asserted.

Build logs, machine-readable counts, summary, metadata audit, rendered inspection pages and PDF hash are retained under the task workspace in v410-consolidation-build/ (metadata audit at its workspace root). The user PDF is Quantum_Sphaera_Companion_v4_10_0_draft.pdf in that workspace. No Zenodo upload or DOI assignment is part of this consolidation. The source consolidation is committed and merged separately at the user's request.

## Recursive calibration follow-up

Full updated manuscript rebuilt with two direct pdflatex passes:1,313 pages. Zero fatal errors, undefined references/citations, duplicate labels or pending rerun warnings;58 older overfull horizontal boxes remain, zero vertical boxes. New pages163–164 visually inspected, including the algorithm and fourth-order residual table. Independent NumPy formal-series checks, scalar gates, frozen failure controls and computation manifests are archived in the dated state-sufficiency directory. The new fourth-order source/outputs pass the evidence-manifest validator. No general recursive convergence or physical validity certificate follows.

Archive integration checks:21 Python files parsed,28 JSON files parsed; all five execution manifests validate with their retained input/output hashes. The portable recursive model re-evaluates all three saved fourth-order results below2.2e-12 in normalized coefficient norm. Independent review scripts were rerun after repository discovery was made portable. These are finite reproducibility/implementation checks, not a proof audit of the entire paper.
