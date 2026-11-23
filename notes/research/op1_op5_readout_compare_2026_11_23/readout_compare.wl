(* Vergleich der Auslesebegriffe OP1 (Lesart B) und OP5 (r46/r47). Methoden-Notiz Commit 498f0578. Erkundung, teilweise nicht blind. *)
eta = DiagonalMatrix[{1, -1, -1, -1}];
(* ---- 1. OP1: Feld mit E || B entlang z im Ruhesystem R ---- *)
Fmat[Ev_, Bv_] := {{0, -Ev[[1]], -Ev[[2]], -Ev[[3]]}, {Ev[[1]], 0, -Bv[[3]], Bv[[2]]}, {Ev[[2]], Bv[[3]], 0, -Bv[[1]]}, {Ev[[3]], -Bv[[2]], Bv[[1]], 0}}; (* F_{mu nu} *)
FR = Fmat[{0, 0, E0}, {0, 0, B0}];
boost[dir_, r_] := Module[{L = IdentityMatrix[4], i = dir + 1},
   L[[1, 1]] = Cosh[r]; L[[i, i]] = Cosh[r]; L[[1, i]] = L[[i, 1]] = -Sinh[r]; L];  (* Lambda^mu_nu, aktiver Uebergang ins Beobachtersystem *)
lowerF[L_, F_] := Module[{Linv = Inverse[L]}, Transpose[Linv] . F . Linv];       (* F'_{mu nu} = F_{a b} (L^-1)^a_mu (L^-1)^b_nu *)
EBof[F_] := {{F[[2, 1]], F[[3, 1]], F[[4, 1]]}, {F[[4, 3]], F[[2, 4]], F[[3, 2]]}};
phiOf[F_] := Module[{eb = EBof[F], s}, s = (eb[[1]] + I eb[[2]]) . (eb[[1]] + I eb[[2]]);
   Simplify[Sqrt[ComplexExpand[Abs[s]^2]]/(eb[[1]] . eb[[1]] + eb[[2]] . eb[[2]]), {E0 > 0, B0 > 0, r \[Element] Reals}]];
Print["(1a) phi im Ruhesystem R: ", phiOf[FR]];
Print["(1b) Beobachter quer zur Achse (x), Rapiditaet r: phi = ", Simplify[phiOf[lowerF[boost[1, r], FR]] - Sech[2 r]] == 0 // TrueQ, "  (phi - sech 2r = 0)"];
Print["     |E'|^2 + |B'|^2 = ", Simplify[Total[(EBof[lowerF[boost[1, r], FR]])^2, 2]], "  = (E0^2 + B0^2) cosh 2r ? ",
  Simplify[Total[(EBof[lowerF[boost[1, r], FR]])^2, 2] - (E0^2 + B0^2) Cosh[2 r]] == 0];
(* Energiedichte im Beobachtersystem als T_{mu nu} u^mu u^nu mit u = Vierergeschwindigkeit des Beobachters im System R *)
Fup = Inverse[eta] . FR . Inverse[eta];
Tdn = Table[Sum[FR[[m, a]] FR[[n, b]] Inverse[eta][[a, b]], {a, 4}, {b, 4}] - 1/4 eta[[m, n]] Sum[FR[[a, b]] Fup[[a, b]], {a, 4}, {b, 4}], {m, 4}, {n, 4}];
uObs = {Cosh[r], Sinh[r], 0, 0};
Print["     T_uu = ", Simplify[uObs . Tdn . uObs], ";  2 T_uu - (|E'|^2 + |B'|^2) = ",
  Simplify[2 uObs . Tdn . uObs - Total[(EBof[lowerF[boost[1, r], FR]])^2, 2]]];
Print["     gerade in r? ", Simplify[(phiOf[lowerF[boost[1, r], FR]] /. r -> -r) - phiOf[lowerF[boost[1, r], FR]]] == 0];
Print["(1c) Beobachter entlang der Achse (z): phi = ", phiOf[lowerF[boost[3, r], FR]]];
(* ---- 2. OP5: Zaehler aus r46.3 als Funktion der Rapiditaet, b = tanh r ---- *)
Nax[b_] := 2 (a^2 - 2 a^2 b^2 + a^2 b^4 - a b^2 k3^2 + a b^4 k3^2 + b^4 k3^4)/(3 (1 - b^2)^2);
Ntr[b_] := a^2 (8 - 12 b^2 + 7 b^4 + 4 b^4 Cos[2 ph] + b^4 Cos[4 ph])/(12 (1 - b^2)^2);
nax = Simplify[TrigReduce[Simplify[Nax[Tanh[r]]]]]; ntr = Simplify[TrigReduce[Simplify[Ntr[Tanh[r]]]]];
Print["(2a) OP5 entlang der Achse: N(r) = ", nax, ";  gerade in r? ", Simplify[(nax /. r -> -r) - nax] == 0];
Print["(2b) OP5 quer zur Achse: N(r) = ", ntr, ";  gerade in r? ", Simplify[(ntr /. r -> -r) - ntr] == 0];
Print["(2c) Ruhewert N(0): entlang ", Simplify[nax /. r -> 0], ", quer ", Simplify[ntr /. r -> 0],
  ";  Grenzwert r -> Infinity relativ zu N(0) quer, ph = 0: ", Limit[(ntr /. ph -> 0)/(ntr /. {r -> 0, ph -> 0}), r -> Infinity]];
