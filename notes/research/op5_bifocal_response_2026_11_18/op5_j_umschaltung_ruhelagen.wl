(* Exact checks of material transport and the retarded mechanical comparison. *)
ClearAll["Global`*"];
xyz = {x, y, z};
xt = Prepend[xyz, t];
profile = phi[x, y, z];
u = Grad[profile, xyz];
v = -u/c;
first = {u, v};
shape = {profile, -profile/c};
mass = {rho1, rho2};
outer[a_] := Outer[Times, a, a];
matrixDiv[a_] := (Div[#, xyz] & /@ a);
moment = rho1 outer[u] + rho2 outer[v];
secondStress = {ConstantArray[0, {3, 3}], moment/(2 rho2)};
second = matrixDiv /@ secondStress;
s = schedule[t];
h = correction[t];
cauchy = Table[mass[[a]] (e D[s, {t, 2}] shape[[a]] IdentityMatrix[3] +
  e^2 (D[h, {t, 2}] secondStress[[a]] - s D[s, {t, 2}] outer[first[[a]]])), {a, 2}];
force = Table[mass[[a]] (e D[s, {t, 2}] first[[a]] +
  e^2 (D[h, {t, 2}] second[[a]] - s D[s, {t, 2}] matrixDiv[outer[first[[a]]]])), {a, 2}];
aField = e s (rho1 - rho2/c) profile;

density = -e s Div[rho1 u + rho2 v, xyz] +
  e^2 Div[s^2 matrixDiv[moment]/2 - h rho2 second[[2]], xyz];
current = e D[s, t] (rho1 u + rho2 v) +
  e^2 (D[h, t] rho2 second[[2]] - s D[s, t] matrixDiv[moment]);
flux = e^2 D[s, t]^2 moment - Total[cauchy];
g = (s^2 - h)/2;
Print["Kernel: ", $Version];
Print["Separate force balance residual: ", Simplify[(matrixDiv /@ cauchy) - force]];
Print["Stress symmetry residual: ", Simplify[cauchy - (Transpose /@ cauchy)]];
Print["General timing, density/current/stress residuals: ", Simplify[{
  density + Laplacian[aField, xyz] - e^2 g Div[matrixDiv[moment], xyz],
  current - Grad[D[aField, t], xyz] + e^2 D[g, t] matrixDiv[moment],
  flux + D[aField, {t, 2}] IdentityMatrix[3] - e^2 D[g, {t, 2}] moment
}]];
Print["Local conservation residuals: ", Simplify[{
  D[density, t] + Div[current, xyz], D[current, t] + matrixDiv[flux]
}]];

eta = DiagonalMatrix[{-1, 1, 1, 1}];
potential = retarded[t, x, y, z];
wave[f_] := D[f, {t, 2}] - Laplacian[f, xyz];
lowerSource[f_] := ArrayFlatten[{
  {{{-Laplacian[f, xyz]}}, {-Grad[D[f, t], xyz]}},
  {Transpose[{-Grad[D[f, t], xyz]}], -D[f, {t, 2}] IdentityMatrix[3]}
}];
barMetric = 16 Pi grav lowerSource[potential];
metric = barMetric - eta Tr[eta.barMetric]/2;
gauge = {-16 Pi grav D[potential, t], 0, 0, 0};
gaugeTensor = Table[D[gauge[[i]], xt[[j]]] + D[gauge[[j]], xt[[i]]], {i, 4}, {j, 4}];
Print["Retarded wave equation residual: ",
  Expand[Map[wave, barMetric, {2}] - 16 Pi grav lowerSource[wave[potential]]]];
Print["Trace reversal and gauge residual: ",
  Expand[metric - 8 Pi grav wave[potential] IdentityMatrix[4] - gaugeTensor]];
