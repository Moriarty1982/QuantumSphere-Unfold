(* k351b: Gegenprobe zu H160 in Wolfram Language (unabhaengig von k351).
   1) Bahnstuecke: Formel ueber den Exzentrizitaetsvektor gegen NDSolve mit WhenEvent am Punkt groesster Annaeherung.
   2) Parabolischer Grenzfall exakt (nachtraeglich, gehoert zu k351c).
   3) Kreisbedingung exakt.  4) Eine Zeile zu H161 K-c.
   Ausgefuehrt am 26.11.2026 ueber den Wolfram-Kernel (zustandslos); Ausgabe in k351b_out.txt. *)
peri[p_, v_] := Module[{res = {}, t},
  NDSolve[{x''[t] == -x[t]/(x[t]^2 + y[t]^2)^(3/2), y''[t] == -y[t]/(x[t]^2 + y[t]^2)^(3/2),
     x[0] == p[[1]], y[0] == p[[2]], x'[0] == v[[1]], y'[0] == v[[2]],
     WhenEvent[x[t] x'[t] + y[t] y'[t] > 0, res = {x[t], y[t]}; "StopIntegration"]}, {x, y}, {t, 0, 200},
    WorkingPrecision -> 30, AccuracyGoal -> 20, PrecisionGoal -> 20, MaxSteps -> 10^6];
  res];
periF[p_, v_] := Module[{r = Norm[p], h, ev, e, q},
  h = p[[1]] v[[2]] - p[[2]] v[[1]];
  ev = {v[[2]] h, -v[[1]] h} - p/r; e = Norm[ev]; q = h^2/(1 + e);
  If[p . v >= 0 && v . v/2 - 1/r >= 0, p, q ev/e]];
Print["1) Bahnstueck: Formel (Exzentrizitaetsvektor) gegen NDSolve mit WhenEvent am Punkt groesster Annaeherung"];
tests = {{"Regel B, a=2", {2, 0}, {-13/10, 9/10}, Function[r, Sqrt[2/r - 1/2]]},
   {"Regel V, v0=1/2", {3/2, 1/5}, {-1, -6/5}, Function[r, 1/2]},
   {"Regel E, vinf=1", {1, 1/2}, {-2, 1}, Function[r, Sqrt[1 + 2/r]]},
   {"parabolisch", {1, 0}, {Cos[2], Sin[2]}, Function[r, Sqrt[2/r]]}};
Do[Module[{p1 = SetPrecision[tt[[2]], 30], p2 = SetPrecision[tt[[3]], 30], sp, a, b},
   sp[p_, q_] := tt[[4]][Norm[p]] (q - p)/Norm[q - p];
   a = Norm[periF[p1, sp[p1, p2]] - peri[p1, sp[p1, p2]]]; b = Norm[periF[p2, sp[p2, p1]] - peri[p2, sp[p2, p1]]];
   Print["   ", tt[[1]], ": |Formel - NDSolve| = ", ScientificForm[N[a, 3]], " , ", ScientificForm[N[b, 3]],
     " ; neue Radien ", N[Norm[periF[p1, sp[p1, p2]]], 8], " , ", N[Norm[periF[p2, sp[p2, p1]]], 8]]], {tt, tests}];
Print["2) Parabolischer Grenzfall exakt (symmetrisch, r1 = r2 = 1, Winkel d zwischen den Punkten):"];
p1 = {1, 0}; p2 = {Cos[d], Sin[d]};
v = Sqrt[2] (p2 - p1)/Sqrt[(p2 - p1) . (p2 - p1)];
h = p1[[1]] v[[2]] - p1[[2]] v[[1]];
ev = {v[[2]] h, -v[[1]] h} - p1;
q = FullSimplify[h^2/2, 0 < d < Pi];
Print["   neuer Radius q = L^2/2 = ", InputForm[q], " ;  q - Cos[d/2]^2 = ", FullSimplify[q - Cos[d/2]^2, 0 < d < Pi]];
Print["   Exzentrizitaet^2 - 1 = ", FullSimplify[ev . ev - 1, 0 < d < Pi]];
Print["   Richtung des neuen Punktes minus Richtung von P2: ", FullSimplify[ev - p2, 0 < d < Pi]];
Print["   => P1' = Cos[d/2]^2 P2 und spiegelbildlich P2' = Cos[d/2]^2 P1: Winkel bleibt d, Radius mal Cos[d/2]^2"];
Print["3) Kreisbedingung: tangentialer Start an beiden Punkten verlangt (P2-P1).P1 = 0 und (P1-P2).P2 = 0; Summe + |P1-P2|^2 = ",
  Simplify[({a, b} - {c, e}) . {c, e} + ({c, e} - {a, b}) . {a, b} + ({a, b} - {c, e}) . ({a, b} - {c, e})], " , also nur fuer P1 = P2"];
Print["4) K-c exakt (H161): P(Y=+1) nach Z-Ergebnis |0>: ", Abs[Conjugate[{1, I}/Sqrt[2]] . {1, 0}]^2, " ; nach |1>: ", Abs[Conjugate[{1, I}/Sqrt[2]] . {0, 1}]^2];
