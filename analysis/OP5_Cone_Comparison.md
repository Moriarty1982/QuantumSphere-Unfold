# Cone comparison and limited Teichmueller analogy

2026-10-27. Uses the exact reference solution of OP5_Two_Probe_Exchange_Evolution.md, not a solution of the self-induced coupled system.

On the central time axis, the reference metric is eta and readout metric g=diag(-d^2,f^2,f^2,f^2), with d=cos(16t), f=(5+3d)/8. Restrict 0<=t<t*=pi/32, where d,f>0. The readout null tangent speed in the SAME reference chart is v=d/f=8d/(5+3d). Since dv/dd=40/(5+3d)^2>0 and d decreases, v decreases strictly for t>0. The cone remains centered and rotationally symmetric on this axis; it narrows without tilting. Off-axis mixed metric components generally occur, so the axis statement must not be generalized to the full patch.

The relative tensor eta^-1 g has eigenvalues (d^2,f^2,f^2,f^2). Equality of cones here requires d^2=f^2. Their ratio is unaffected by a common coordinate change of the two metrics or a positive conformal rescaling of g. In this positive interval equality holds only at t=0. Each metric separately is flat where the readout map is invertible, but they are different metrics under the fixed physical identification of events. Local tangent cone slopes are not integrated null trajectories.

For an auxiliary EUCLIDEAN 2D comparison of the tangent map on (t,x), F=diag(d,f), the singular-value distortion is K=f/d, the Beltrami coefficient with z=t+ix is mu=(d-f)/(d+f), and D=(1/2)ln K. These are exact local linear-map quantities under the stipulated Euclidean comparison. Classical Teichmueller distance instead requires marked Riemann surfaces and optimization over an admissible map class; no such data or optimization have been supplied here. Therefore D is NOT asserted to be a Teichmueller distance or a Lorentz-invariant physical distance. The ratio v=1/K is directly useful for the on-axis comparison.

At t->t* from below, d->0, v->0 and K->infinity. The readout coframe loses rank at the endpoint; the endpoint is not a Lorentz metric and must not be interpreted as physical light stopping or a demonstrated gravitational singularity. The SVG plots stop before this endpoint. All quantities are dimensionless example values, not experimental predictions.

Sources for the mathematical scope: Gardiner and Lakic, Quasiconformal Teichmueller Theory, https://doi.org/10.1090/surv/076 (marked conformal structures); Kapovich, https://www.math.ucdavis.edu/~kapovich/RFG/book.pdf , section 5.4 (infimum of half-log maximal quasiconformal dilatation). The particular cone and local linear-map formulas here are derived directly from the displayed diagonal matrices.

Artifacts: OP5_Cone_Comparison.svg, OP5_Cone_Comparison.json and OP5_Cone_Comparison.py. Standard-library numerical sampling, monotonic ordering check and XML parsing completed. Figure shows local axis tangent cones, not off-axis or global evolution. Teichmueller methods do not repair the failed self-induced field equation.
