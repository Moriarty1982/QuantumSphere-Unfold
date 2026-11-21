(* Symbolic checks of the stationary comparison in frame M. *)
ClearAll["Global`*"];
f = Array[fij, {3, 3}];
grad = Array[gij, {3, 3}];
target = IdentityMatrix[3] + q grad;
ce[e_] := lam Tr[e] IdentityMatrix[3] + 2 mu e;
strain = (Transpose[f].f - Transpose[target].target)/2;
potential = barrier q^2 (1 - q)^2;
energy = Tr[strain.ce[strain]]/2 + potential;
piola = Map[D[energy, #] &, f, {2}];
atTarget = Thread[Flatten[f] -> Flatten[target]];
wells = {0, 1};
Print["Kernel: ", $Version];
Print["Piola derivative residual: ", Expand[piola - f.ce[strain]]];
Print["Cauchy numerator symmetry residual: ",
  Expand[piola.Transpose[f] - f.Transpose[piola]]];
Print["Well energy, Piola and scalar residuals: ",
  Table[
    Expand[{energy, piola, D[energy, q]} /. atTarget /. q -> well],
    {well, wells}
  ]
];
Print["Barrier energy at half switching: ", potential /. q -> 1/2];

xyz = {x, y, z};
phi = p[x, y, z];
u = Grad[phi, xyz];
v = -u/c;
divergence[a_] := Div[a, xyz];
uOuter = Outer[Times, u, u];
vOuter = Outer[Times, v, v];
matrixDiv[a_] := divergence /@ a;
massWeight = rho1 + rho2/c^2;
b = massWeight matrixDiv[uOuter]/(2 rho2);
density1 = -divergence[rho1 u + rho2 v];
density2 = -rho2 divergence[b] +
  divergence[matrixDiv[rho1 uOuter + rho2 vOuter]]/2;
Print["Linear Laplace source residual: ",
  Simplify[density1 - (rho2/c - rho1) Laplacian[phi, xyz]]];
Print["Quadratic mass transport residual: ", Simplify[density2]];

(* Independent weak-form check with an arbitrary test function. *)
probe = h[x, y, z];
probeGrad = Grad[probe, xyz];
probeHess = D[probe, {{x, y, z}, 2}];
pushforward2 = rho2 b.probeGrad +
  Tr[(rho1 uOuter + rho2 vOuter).probeHess]/2;
Print["Second-order weak divergence residual: ",
  Simplify[pushforward2 -
    divergence[massWeight uOuter.probeGrad/2]]];
Print["Newton source residual: ",
  Simplify[Laplacian[4 Pi grav (rho2/c - rho1) phi, xyz] - 4 Pi grav density1]];
