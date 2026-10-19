# QSC Entry Points

Read this only when working in QuantumSphere-Unfold. Paths below are repository
relative. Check report fingerprints before reuse; this map is a navigation aid,
not authority for the current mathematical status.

- `analysis/HC_Cartan_General_Normal_Chart.py`: general 68-by-56 affine normal
  equations and lower-field packing. Fixed coordinate rows are not a physical
  classification of transported gauge or source modes.
- `analysis/HC_Cartan_First_Compatibility_Source_Gate.py`: extraction of 272
  first primary derivatives from 384 earlier rows, complete left-kernel source
  elimination at the special point, 224 allowed normal higher coordinates.
- `analysis/HC_Cartan_General_First_Source_Gate.py`: translated Taylor jets,
  general directional derivatives, coordinate kernel sections and cached normal
  higher response. Its off-origin source gate is a tangent diagnostic.
- `analysis/HC_Cartan_First_Compatibility_Attribution.py`: full 720-coordinate
  higher response, 52 known rows and nonzero identity sources. The sampled rank
  increase from 160 to 220 after releasing 496 prescribed coordinates is not a
  universal rank identity or a regional existence theorem.
- `analysis/Numerical_Dependencies.py`, `analysis/Numerical_Matrix_Cache.py`:
  scoped numerical services, bounded cache operations and SVD backend injection.

The full higher comparison also contains 1114 residual rows; the 272-row first
stage does not replace that completion. Its model is the added neutral
commuting-spinor odd-cross Einstein--Cartan comparison, not native HC/C7 physics.

Prefer adopting the generic helper in a new sidecar or deliberate revision.
Replacing imports in historical reports invalidates their source fingerprints
and may trigger expensive recomputation; do not migrate them as incidental cleanup.
