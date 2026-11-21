(* Symbolic checks for the OP5 modal-label and calibration model. *)
ClearAll["Global`*"];
Print["Kernel: ", $Version];
id = IdentityMatrix[2];
tag = DiagonalMatrix[{1, -1}];
sender = {{1, a}, {b, 1}};
receiver = {{2, c}, {d, 3}};
ref = receiver.sender;
tagged = receiver.tag.sender;
profile = receiver.DiagonalMatrix[{zj, za}].sender;
q = Inverse[ref].profile;
tq = Inverse[ref].tagged;
read[q0_, t0_] := {Tr[(id + t0).q0], Tr[(id - t0).q0]}/2;
Print["Modal trace residual at arbitrary phase gap: ", Simplify[read[q, tq] - {zj, za}]];
Print["Modal trace residual at coincident phases: ", Simplify[(read[q, tq] /. za -> zj) - {zj, zj}]];
errQ = Array[eq, {2, 2}]; errT = Array[et, {2, 2}];
u = DiagonalMatrix[{zj, za}];
Print["Perturbation expansion residual: ", Expand[
  read[u + errQ, tag + errT] - read[u, tag] -
  Diagonal[errQ] - {1, -1} Tr[errT.(u + errQ)]/2]];
Print["Reference modal rank determinant residual: ",
  Expand[Det[{{0, gc}, {os, gs}}] + os gc]];
g[s_] := g0 + g1 s + g2 s^2 + g3 s^3;
mismatch = {{os1 s1, g[s1] - g[0]}, {os1 s2, g[s2] - g[0]}};
Print["Differential data determinant residual: ",
  Expand[Det[mismatch] - os1 s1 s2 (s2 - s1) (g2 + g3 (s1 + s2))]];
lap[f_] := Expand[4 (D[f, s] + s D[f, {s, 2}])/rad^2];
phi = 16 b4 (s - 9 kappa s^2)/rad^2 - b2 (s^2 - 4 kappa s^3) +
  b0 rad^2 (s^3 - 9 kappa s^4/4)/36;
Print["Ordinary radial curvature coefficients residual: ",
  Expand[CoefficientList[lap[phi], s] -
    {64 b4/rad^4, -2304 kappa b4/rad^4 - 16 b2/rad^2,
     b0 + 144 kappa b2/rad^2, -4 kappa b0}]];
