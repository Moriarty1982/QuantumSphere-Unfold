(* Mittel ueber einen gespiegelten Vertex (x -> -x) statt Zeitumkehr. Methoden-Notiz Commit 10e483e1. *)
(* Konventionen wie r39/r40: J_ab = D_a D_b - c eta_ab Box, D = (-I w, I k1, I k2), x = w^2, a = k1^2 + k2^2, k1 = Sqrt[a] Cos[ph]. *)
etaS = DiagonalMatrix[{1, -1, -1}];
Jof[wv_, k1v_, k2v_, cc_] := Module[{Dv = {-I wv, I k1v, I k2v}, box},
   box = Sum[etaS[[i, i]] Dv[[i]]^2, {i, 3}];
   Table[Dv[[i]] Dv[[j]] - cc etaS[[i, j]] box, {i, 3}, {j, 3}]];
pol = {k1 -> Sqrt[a] Cos[ph], k2 -> Sqrt[a] Sin[ph], w -> Sqrt[x]};
Nm = 2/3 (x^2 - a x + a^2);
J = Jof[w, k1, k2, 1];
JT = Jof[-w, k1, k2, 1];     (* Zeitumkehr an einem Vertex *)
JP = Jof[w, -k1, k2, 1];     (* Spiegelung x -> -x an einem Vertex *)
nn[A_, B_] := Simplify[TrigReduce[Expand[Sum[A[[i, j]] B[[i, j]], {i, 3}, {j, 3}] /. pol]], {x >= 0, a >= 0}];
NT = Simplify[(nn[J, J] + nn[J, JT])/2];
NP = Simplify[(nn[J, J] + nn[J, JP])/2];
Print["(3) Mittel mit Zeitumkehr, c = 1: ", Collect[NT, {x, a}], ";  - 3 N_m = ", Simplify[NT - 3 Nm]];
Print["    Mittel mit Spiegelung x -> -x, c = 1: ", Collect[NP, {x, a}], ";  - 3 N_m = ", Simplify[NP - 3 Nm]];
Print["    Spiegelung, Richtung ph = 0 (k entlang Gegenstrom): ", Simplify[NP /. ph -> 0], ";  ph = Pi/2: ", Simplify[NP /. ph -> Pi/2], ";  ph = Pi/4: ", Simplify[NP /. ph -> Pi/4]];
Print["    Spiegelung, Winkelmittel ueber ph: ", Simplify[Integrate[NP, {ph, 0, 2 Pi}]/(2 Pi)], ";  proportional zu N_m? ",
  Solve[DeleteCases[Thread[Flatten[CoefficientList[Expand[Integrate[NP, {ph, 0, 2 Pi}]/(2 Pi) - lam Nm], {x, a}]] == 0], True], lam]];
