(* k333b (H150): unabhaengige Gegenprobe in Wolfram Language zu k333_vorzeichen_2a_b.py.
   Ausgefuehrt ueber den Wolfram-Cloud-Kernel in zwei Aufrufen (Teil 1: beta-Funktionen, Abschneidung, HC; Teil 2: Fluss). *)
(* Teil 1 *)
betas[nA_, nB_] := Module[{x = Array[xx, nA], y = Array[yy, nB], A, B, V, H, rhs, sol},
  A = x . x; B = y . y; V = la A^2 + k A B + lb B^2;
  H = D[V, {Join[x, y], 2}]; rhs = Expand[Tr[H . H]/2];
  sol = First@SolveAlways[rhs == ba A^2 + bk A B + bb B^2, Join[x, y]];
  {Factor[ba /. sol], Factor[bk /. sol], Factor[bb /. sol], Coefficient[Expand[Tr[H]], xx[1]^2], Coefficient[Expand[Tr[H]], yy[1]^2]}];
Do[Print["n = ", p, ": ", betas @@ p], {p, {{1, 1}, {2, 2}, {1, 2}, {1, 7}}}];
b11 = betas[1, 1];
Print["n=1 symmetrisch, 16pi^2 dr/dt * lambda: ", Factor[(b11[[2]] l - r l b11[[1]]) /. {la -> l, lb -> l, k -> r l}]/l];
b22 = betas[2, 2];
Print["n=2 symmetrisch: ", Factor[(b22[[2]] l - r l b22[[1]]) /. {la -> l, lb -> l, k -> r l}]/l];
b12 = betas[1, 2];
Vq = cL/2 (b12[[4]] Cos[t]^2 + b12[[5]] Sin[t]^2) f^2 + f^4 (la Cos[t]^4 + k Cos[t]^2 Sin[t]^2 + lb Sin[t]^4) /. {la -> l, lb -> l};
Print["Abschneidung: stationaer bei cos 2t = ", Solve[Simplify[D[Vq, t]/Sin[2 t] /. t -> ArcCos[c]/2] == 0, c]];
Print["HC: ", CoefficientRules[Expand[eta (BB - m^2 AA)^2], {AA, BB}]];
(* Teil 2 *)
flow[y0_, eqs_] := Module[{e = None, sol},
  sol = NDSolve[Join[eqs, {la[0] == y0[[1]], k[0] == y0[[2]], lb[0] == y0[[3]], WhenEvent[k[s] + 2 Sqrt[la[s] lb[s]] == 0, {e = s, "StopIntegration"}]}], {la, k, lb}, {s, 0, 10}, WorkingPrecision -> 25, PrecisionGoal -> 12];
  {e, (1 + Sqrt[la[e]/lb[e]])/3 /. First[sol]}];
e12 = {la'[s] == -4 (k[s]^2 + 18 la[s]^2), k'[s] == -8 k[s] (2 k[s] + 3 la[s] + 4 lb[s]), lb'[s] == -2 (k[s]^2 + 40 lb[s]^2)};
e17 = {la'[s] == -2 (7 k[s]^2 + 36 la[s]^2), k'[s] == -8 k[s] (2 k[s] + 3 la[s] + 9 lb[s]), lb'[s] == -2 (k[s]^2 + 60 lb[s]^2)};
e22 = {la'[s] == -4 (k[s]^2 + 20 la[s]^2), k'[s] == -16 k[s] (k[s] + 2 la[s] + 2 lb[s]), lb'[s] == -4 (k[s]^2 + 20 lb[s]^2)};
Print["(1,2) Start (1/5,-1/5,1/5): ", N[flow[{1/5, -1/5, 1/5}, e12], 10]];
Print["(1,7) Start (1/5,-1/5,1/5): ", N[flow[{1/5, -1/5, 1/5}, e17], 10]];
Print["(2,2) Start (1/5,-1/5,1/5): ", N[flow[{1/5, -1/5, 1/5}, e22], 10]];
