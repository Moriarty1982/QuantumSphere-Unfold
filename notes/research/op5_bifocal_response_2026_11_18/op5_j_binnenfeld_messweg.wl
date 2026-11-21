(* Symbolic checks for the ordinary interior field on the A/B path. *)
ClearAll["Global`*"];
Print["Kernel: ", $Version];
radLap[f_] := Expand[4 (D[f, s] + s D[f, {s, 2}])/rad^2];
profile = s^5 - kappa s^6;
column = Expand[rad^6 (b0 Nest[radLap, profile, 2] -
  b2 Nest[radLap, profile, 3] + b4 Nest[radLap, profile, 4])/230400];
expected = 16 b4 (s - 9 kappa s^2)/rad^2 -
  b2 (s^2 - 4 kappa s^3) + b0 rad^2 (s^3 - 9 kappa s^4/4)/36;
Print["Interior potential column residual: ", Expand[column - expected]];
Print["Axial delay and unit-normalized tidal residuals: ",
  Simplify[{column, radLap[column] - 64 b4/rad^4} /. s -> 0]];
Print["Leading finite-beam tidal polynomial residual: ",
  Expand[radLap[16 b4 (s - 9 kappa s^2)/rad^2] -
    64 b4 (1 - 36 kappa s)/rad^4]];

zetaSource = sourceMatch;
gColumn = 4 Pi grav vH zetaSource amp a pInt column;
ordinaryTide = radLap[gColumn] /. s -> 0;
opTide = 16 amp a pInt/(mass^2 rad^4);
Print["Ordinary-to-OP5 tidal ratio residual: ",
  Simplify[ordinaryTide/opTide - 16 Pi grav vH zetaSource mass^2 b4]];

calibration = 36 b2 c3 s^2/(b0 rad^2) + c3 s^3 + c6 s^6;
calH = Nest[radLap, calibration, 3];
calPhi = -4 Pi grav vH zetaSource pInt (b0 Nest[radLap, calibration, 2] -
  b2 calH + b4 radLap[calH]);
Print["Calibration axial delay, massive line, OP5 tide and ordinary tide residuals: ",
  Simplify[{calPhi, radLap[calH], Nest[radLap, calH, 2],
    radLap[calPhi] + 4 Pi grav vH zetaSource pInt b0 2304 c3/rad^6} /. s -> 0]];
Print["Calibration transverse moment residual: ", Simplify[
  (36 b2 c3 moment2/(b0 rad^2) + c3 moment3 + c6 moment6) /.
  c6 -> -(36 b2 c3 moment2/(b0 rad^2) + c3 moment3)/moment6]];

(* Static operator after longitudinal integration and characteristic margin. *)
alpha = kinetic sound + 3 g0sq/2;
poly = Expand[((kinetic gap + alpha q) (rm q + mass^2) -
   2 gmsq q^2/3)/mass^2];
Print["Static transverse drive polynomial residual: ", Simplify[poly -
  (kinetic gap + (alpha + kinetic gap rm/mass^2) q +
    (rm alpha - 2 gmsq/3) q^2/mass^2)]];
b = alpha + 2 gmsq (rm - direction)/3;
j2 = 2 gmsq (rm^2 - rm direction + direction^2)/3;
Print["Transverse stability margin residual: ",
  Simplify[((b - j2/rm) /. direction -> 1) - (rm alpha - 2 gmsq/3)/rm]];
Print["Dimensionless quadratic coefficient in the reference example: ",
  (rm alpha - 2 gmsq/3) /. {kinetic -> 1, sound -> 1/2, rm -> 1/2,
   g0sq -> 3/100, gmsq -> 3/100}];

(* Independent linearized screen curvature calculation. *)
coord = {t, x, y, z};
potential = phi[x, y, z];
metricPerturb = -2 potential IdentityMatrix[4];
curvatureComponent[i_, j_, k_, l_] := (
   D[metricPerturb[[i, l]], coord[[j]], coord[[k]]] +
   D[metricPerturb[[j, k]], coord[[i]], coord[[l]]] -
   D[metricPerturb[[i, k]], coord[[j]], coord[[l]]] -
   D[metricPerturb[[j, l]], coord[[i]], coord[[k]]])/2;
light = {1, 0, 0, 1};
pol = {0, 1, 0, 0};
tidal = Sum[light[[i]] pol[[j]] light[[k]] pol[[l]] curvatureComponent[i, j, k, l],
  {i, 4}, {j, 4}, {k, 4}, {l, 4}];
Print["Ordinary static screen-curvature residual: ",
  Expand[tidal - 2 D[potential, {x, 2}] - D[potential, {z, 2}]]];
Print["Linear null-condition delay residual: ",
  Simplify[SeriesCoefficient[Sqrt[(1 - 2 e potential)/(1 + 2 e potential)], {e, 0, 1}] + 2 potential]];
