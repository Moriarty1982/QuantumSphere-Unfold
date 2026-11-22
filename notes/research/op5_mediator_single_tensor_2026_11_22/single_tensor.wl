(* Skalar als Zeit-Zeit-Komponente eines Tensors auf dem Unterraum (t, x, y). Methoden-Notiz Commit 538b11d6. Erkundung, nicht blind. *)
(* Fourierbild: d_t -> -I w, d_i -> I k_i, also d_a d_b -> D_a D_b mit D = (-I w, I k1, I k2); x = w^2, a = k1^2 + k2^2.
   J_ab = d_a d_b eta - c eta_ab Box eta, eta_ab = diag(1, -1, -1), Box = d_t^2 - d_x^2 - d_y^2.
   Austauschzaehler N = Sum_ab wt_ab J_ab^2 (geordnete Doppelsumme; wt_0i = wt_i0 = w, sonst 1). *)
Dv = {-I w, I k1, I k2};
etaS = DiagonalMatrix[{1, -1, -1}];
box = Sum[etaS[[i, i]] Dv[[i]]^2, {i, 3}];
J = Table[Dv[[i]] Dv[[j]] - c etaS[[i, j]] box, {i, 3}, {j, 3}];
wt = {{1, w0, w0}, {w0, 1, 1}, {w0, 1, 1}};
pol = {w -> Sqrt[x], k1 -> Sqrt[a] Cos[ph], k2 -> Sqrt[a] Sin[ph]};
cl[e_] := Simplify[TrigReduce[Expand[e /. pol]], {x >= 0, a >= 0}];
Print["(0) Box -> ", cl[box], ";  J_00 -> ", cl[J[[1, 1]]], ";  J_11 + J_22 -> ", cl[J[[2, 2]] + J[[3, 3]]], ";  J_0i^2 summiert -> ", cl[J[[1, 2]]^2 + J[[1, 3]]^2]];
Nw = cl[Sum[wt[[i, j]] J[[i, j]]^2, {i, 3}, {j, 3}]];
Print["(1) N(c, w) = ", Collect[Expand[Nw], {x, a}]];
Nm = 2/3 (x^2 - a x + a^2);
eqs = DeleteCases[Thread[Flatten[CoefficientList[Expand[Nw - lam Nm], {x, a}]] == 0], True];
Print["    N = lam N_m identisch fuer: ", Solve[eqs, {c, w0, lam}]];
Print["    mit w = 1 (Zeit-Quer-Komponenten gekoppelt): ", Solve[eqs /. w0 -> 1, {c, lam}]];
Print["    mit w = 0 (entkoppelt): ", Solve[eqs /. w0 -> 0, {c, lam}]];
Print["    allgemein w(c), lam(c): ", Simplify[Solve[eqs, {w0, lam}]]];

(* (2) Erhaltung *)
cons = Table[Sum[etaS[[i, i]] Dv[[i]] J[[i, b]], {i, 3}], {b, 3}];
Print["(2) p^a J_ab = ", Simplify[cons], ";  null genau fuer ", Solve[Simplify[cons[[1]]] == 0, c]];

(* (3) Vergleich mit r38 und dem String *)
Jc1 = J /. c -> 1;
Print["(3) c = 1: J_00 -> ", cl[Jc1[[1, 1]]], ",  J_ij -> ", cl[Jc1[[2, 2]]] , " (xx), ", cl[Jc1[[2, 3]]], " (xy); Spur -> ", cl[Jc1[[2, 2]] + Jc1[[3, 3]]]];
(* r38 mit g_m = 1: g^2 = 2/3, kap = 1/2, g_s^2 = 1/3; Einzelfeld: g'^2 = lam^-1 * (2/3) * ... siehe Ausgabe (1) *)
Print["    r38: Vertex S = -g_s x, Spur X = g (x - a); Normquadrat (S, X-Spur/Sqrt[2]) = ", Expand[1/3 x^2 + 2/3 (x - a)^2/2],
  ";  Spurfreier Anteil r38: g^2 a^2/2 = ", 2/3 a^2/2];
Print["    Einzelfeld c = 1, g'^2 = 1/3: Normquadrat (H_00, H-Spur/Sqrt[2]) = ", Expand[1/3 (cl[Jc1[[1, 1]]]^2 + cl[Jc1[[2, 2]] + Jc1[[3, 3]]]^2/2)],
  ";  spurfreier Anteil: ", Simplify[1/3 cl[(Jc1[[2, 2]] - Jc1[[3, 3]])^2/2 + 2 Jc1[[2, 3]]^2]]];
Print["    Stringvertex (r37, am Pol 2 w1^2 = x/2): k_i k_j - (x/2) delta_ij; Einzelfeld c = 1: -k_i k_j - (x - a) delta_ij"];

(* (4) Stabilitaet fuer c = 1, w = 0 *)
gp2 = gm2/3;
Print["(4a) kinetische Mischung: Koeffizienten von x in J_00, J_11, J_22, J_12: ", {Coefficient[cl[Jc1[[1, 1]]], x], Coefficient[cl[Jc1[[2, 2]]], x], Coefficient[cl[Jc1[[3, 3]]], x], Coefficient[cl[Jc1[[2, 3]]], x]},
  ";  Det K = 2 - 2 g'^2 = ", 2 - 2 gp2, " > 0 genau fuer gm2 < 3"];
statN = Simplify[(Nw /. {c -> 1, w0 -> 0}) /. x -> 0];
Print["(4b) statischer Zaehler g'^2 N(x = 0) = ", Simplify[gp2 statN], "  (Vergleichsmodell: (2/3) gm2 a^2) -> gleiche Schranke gm2 <= 3 r_m"];
qq = k1^2 + k2^2 + k3^2; dm = m2 + r qq - x;
Vx = cl /@ {Jc1[[1, 1]], Jc1[[2, 2]], Jc1[[3, 3]], Jc1[[2, 3]]};
Mfull[gm2v_] := Module[{gp = Sqrt[gm2v/3], v = {Jc1[[1, 1]], Jc1[[2, 2]], Jc1[[3, 3]], Jc1[[2, 3]]} /. {w -> Sqrt[x]}},
   {{2 (x - qq - mH2), gp v[[1]], gp v[[2]], gp v[[3]], 2 gp v[[4]]},
    {gp v[[1]], -dm, 0, 0, 0}, {gp v[[2]], 0, -dm, 0, 0}, {gp v[[3]], 0, 0, -dm, 0}, {2 gp v[[4]], 0, 0, 0, -2 dm}}];
check[gm2v_] := Module[{res = {}},
  Do[Module[{det = Det[Mfull[gm2v] /. {mH2 -> 2, m2 -> 1, r -> 1/2} /. {k1 -> Sqrt[av], k2 -> 0, k3 -> Sqrt[kz]}], rts},
     rts = x /. NSolve[det == 0, x, WorkingPrecision -> 30];
     AppendTo[res, {av, kz, And @@ (Abs[Im[#]] < 10^-20 && Re[#] > 0 & /@ rts), Min[Re[rts]]}]],
   {av, {0, 1/2, 1, 2, 5, 20, 100}}, {kz, {0, 1, 10}}];
  {AllTrue[res, #[[3]] &], N[Min[res[[All, 4]]], 6], Select[res, ! #[[3]] &][[All, 1 ;; 2]]}];
Do[With[{cc = check[gv]}, Print["(4c) g_m^2 = ", gv, ": alle x-Wurzeln reell und positiv: ", cc[[1]], ", kleinste Wurzel ", cc[[2]], ", Ausnahmen: ", cc[[3]]]], {gv, {3/100, 1, 7/5, 8/5}}];
