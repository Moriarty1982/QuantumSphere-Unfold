(* Symbolic checks for the local OP5 action. *)
ClearAll["Global`*"];
Print["Kernel: ", $Version];

(* Vary the metric at fixed densitized material current. *)
flow = Array[j, 4];
metric = DiagonalMatrix[{-1, 1, 1, 1}] + h Array[gg, {4, 4}];
clockAction = lambda (clockDerivative - Sqrt[-flow.metric.flow]);
clockVariation = Table[
  D[clockAction, gg[i, k], h] /. h -> 0,
  {i, 4}, {k, 4}
];
clockExpected = lambda Outer[Times, flow, flow]/
  (2 Sqrt[flow[[1]]^2 - Rest[flow].Rest[flow]]);
Print["Clock Hilbert variation residual: ", Simplify[clockVariation - clockExpected]];

(* The independent material and clock labels define the force one-form. *)
coords = {q, y1, y2, y3};
raw = {0, a1[q, y1, y2, y3], a2[q, y1, y2, y3], a3[q, y1, y2, y3]};
curv = Table[D[raw[[k]], coords[[i]]] - D[raw[[i]], coords[[k]]], {i, 4}, {k, 4}];
along = curv.{rate, 0, 0, 0};
Print["Adapted one-form force residual: ",
  Expand[along + rate D[raw, q]]];
topologicalCoupling = Array[jr, 4].raw;
Print["One-form metric variation residual: ", D[topologicalCoupling, h]];

(* Strain pullback, rest-frame stress and inverse metric prescription. *)
f = {{2, 1, 0}, {0, 3, 1}, {0, 0, 1}};
v = {1/7, 1/11, 1/13};
ident = IdentityMatrix[3];
gradX = Inverse[f];
binv = Transpose[f].Inverse[ident - Outer[Times, v, v]].f;
bmat = gradX.(ident - Outer[Times, v, v]).Transpose[gradX];
printB = Simplify[bmat.binv - ident];
properDensity = Sqrt[Det[bmat]];
lmat = Transpose[gradX].binv;
sigma = {{ss11, ss12, ss13}, {ss12, ss22, ss23}, {ss13, ss23, ss33}};
target = Inverse[lmat].sigma.Transpose[Inverse[lmat]]/properDensity;
strain = (target - lam Tr[target] ident/(3 lam + 2 mu))/(2 mu);
gStar = binv - 2 strain;
recoveredStrain = (binv - gStar)/2;
recovered = properDensity lmat.(lam Tr[recoveredStrain] ident + 2 mu recoveredStrain).Transpose[lmat];
Print["Inverse strain residual: ", printB];
Print["Spatial stress from adjusted metric residual: ", Simplify[recovered - sigma]];
Print["Proper reference-volume density residual: ",
  FullSimplify[properDensity - Sqrt[1 - v.v]/Det[f]]];
direction = {{1, -1, 2}, {-1, 0, 3}, {2, 3, 1}};
varStrain = (D[Inverse[bmat + z direction], z] /. z -> 0)/2;
elasticEnergy[ee_] := lam Tr[ee]^2/2 + mu Tr[ee.ee];
energyVariation = D[elasticEnergy[recoveredStrain + z varStrain], z] /. z -> 0;
Print["Elastic metric variation residual: ",
  Simplify[energyVariation + Tr[binv.target.binv.direction]/2]];

(* Check the retained material and carrier energy together in the laboratory. *)
vel = e Array[vel1, 3] + e^2 Array[vel2, 3];
drift = e^2 Array[dv, 3];
carrierDensity = r + e car1 + e^2 car2;
matrixDensity = mat + e mat1 + e^2 mat2;
work = e^2 el;
powerFlux = r drift;
firstStress = e sigma;
gate = powerFlux - firstStress.vel;
trunc[expr_] := Simplify[Normal[Series[expr, {e, 0, 2}]]];
Print["Laboratory stored energy and kinetic energy residual: ",
  trunc[(matrixDensity + work)/Sqrt[1 - vel.vel] +
    (carrierDensity - work - (r + mat) vel.vel/2)/Sqrt[1 - (vel + drift).(vel + drift)] -
    matrixDensity - carrierDensity]];
Print["Counterflow disappears when drift supplies elastic power: ",
  Simplify[Map[trunc, gate /. Thread[Array[dv, 3] -> sigma.Array[vel1, 3]/r]]]];
