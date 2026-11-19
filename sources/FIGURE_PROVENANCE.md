# Figure provenance

Run `python tools/generate_op5_figures.py` from the repository root with
NumPy, Pillow (10.1 or later) and ReportLab installed.

The restored v3841 Julia files are newly computed diagnostic figures.
Appendix C.9 specifies the four residual scales and the anti-rational
map. The renderer uses homogeneous coordinates, a common window of
±1.8 on both axes, 432 × 432 initial conditions, 120 steps and a chordal
distance threshold of 10⁻⁵ to the tracked cycle. The circle marks the
unit horizon. This protocol is documented here so differences from the
historical renderer can be traced. See the [historical release](https://zenodo.org/records/19423689)
for the publication context.

The three historical v3862 frame-flicker figures still need the original
benchmark trace and fit parameters or the original embedded artwork.
The new OP5 geometry figure is for the current draft editions. Its model
curves are based on the bifocal analysis in
[the radial probe note](../notes/research/op5_bifocal_response_2026_11_18/Sondenform.md).
The left panel uses the exact Coulomb contour through the same major
vertex as the distance ellipse, and the right panel uses the leading
Yukawa coefficient. Neither panel contains measured data.
