(* Symbolic checks of a forced dust carrier in the material frame M. *)
ClearAll["Global`*"];
coords = {x, y, z};
potential = phi[x, y, z];
schedule = s[t];
u = Grad[potential, coords];
v = e D[schedule, t] u;
sigma = e rho D[schedule, {t, 2}] potential IdentityMatrix[3];
flux = sigma.v;
shift = e^2 rho D[schedule, t]^2 Grad[potential^2/2, coords]/(2 r0);
en = e^2 en2[t, x, y, z];
nMass = -en + r0 Div[shift, coords];
power = D[en, t] - Div[flux, coords];

Print["Kernel: ", $Version];
Print["Carrier drift and energy conversion residuals: ", Expand[{
  r0 D[shift, t] - flux,
  nMass - r0 Div[shift, coords] + en,
  D[nMass, t] + power
}]];

(* Lab tensor with number measure pushed forward at fixed coordinate time. *)
genericV = e Array[vv, 3] + e^2 Array[ww, 3];
genericDrift = e^2 Array[drift, 3];
density = r0 + e r1 + e^2 r2;
trunc[a_] := Expand[Normal[Series[a, {e, 0, 2}]]];
fourVector[w_] := Prepend[w, 1];
dust[m_, w_] := m Outer[Times, fourVector[w], fourVector[w]]/Sqrt[1 - w.w];
dustDifference = Map[trunc, dust[density + e^2 deltaR, genericV + genericDrift] -
  dust[density, genericV], {2}];
expectedDust = ArrayFlatten[{
  {{{e^2 deltaR}}, {r0 genericDrift}},
  {Transpose[{r0 genericDrift}], ConstantArray[0, {3, 3}]}
}];
Print["Dust lab tensor residual: ", Expand[dustDifference - expectedDust]];

(* Rest-frame spatial stress boosted using velocity orthogonality. *)
symStress = e {{aa, ab, ac}, {ab, bb, bc}, {ac, bc, cc}};
boostedStress = ArrayFlatten[{
  {{{genericV.symStress.genericV}}, {symStress.genericV}},
  {Transpose[{symStress.genericV}], symStress}
}];
Print["Stress time component and orthogonality residuals: ",
  {trunc[boostedStress[[1, 1]]],
   Expand[boostedStress.DiagonalMatrix[{-1, 1, 1, 1}].fourVector[genericV]]}];
reservoirPressure = e symStress;
lift[spatial_] := ArrayFlatten[{
  {{{genericV.spatial.genericV}}, {spatial.genericV}},
  {Transpose[{spatial.genericV}], spatial}
}];
Print["Retuned quadratic spatial stress residual: ",
  Module[{f = DiagonalMatrix[{f1, f2, f3}], pullback, strain, pushforward},
    pullback = Det[f] Inverse[f].reservoirPressure.Transpose[Inverse[f]];
    strain = (pullback - lam Tr[pullback] IdentityMatrix[3]/(3 lam + 2 mu))/(2 mu);
    pushforward = f.(lam Tr[strain] IdentityMatrix[3] + 2 mu strain).Transpose[f]/Det[f];
    Simplify[reservoirPressure - pushforward]
  ]];
Print["Quadratic pressure energy and flux orders: ",
  Map[trunc, First[lift[reservoirPressure]]]];

acc = Grad[e D[schedule, {t, 2}] rho potential, coords];
forceR = r0 acc/rho + D[flux, t];
forceS = (rho - r0) acc/rho - acc - D[flux, t];
energyR = r0 v.acc/rho + Div[flux, coords] - D[en, t];
energyS = D[en, t] - r0 v.acc/rho - Div[flux, coords];
Print["Local momentum reaction residual: ", Expand[forceR + forceS]];
Print["Local energy reaction and rest-power residuals: ",
  {Expand[energyR + energyS], trunc[energyR - v.forceR + power]}];
Print["Integrated-motion representative ends at rest when s' and s'' vanish: ",
  Expand[{shift, D[shift, t], D[flux, t], nMass} /.
    {s'[t] -> 0, s''[t] -> 0, en2[t, x, y, z] -> 0}]];
