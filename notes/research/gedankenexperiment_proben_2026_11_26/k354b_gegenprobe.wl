(* k354b: Gegenprobe zu H163 in Wolfram Language (exakt, dazu ein NDSolve-Lauf). Ausgefuehrt am 26.11.2026; Ausgabe in k354b_out.txt. *)
Print["1) Newton: Stoss und Zusatzkraft"];
vp2 = vinf^2 + 2/rp; vc2 = 1/rp;
Print["   (v_p/v_c)^2 - (2 + vinf^2 rp) = ", Simplify[vp2/vc2 - (2 + vinf^2 rp)]];
Print["   Zentralkraft fuer Kreis mit v_p: v_p^2/rp geteilt durch Schwerkraft 1/rp^2, minus (2 + vinf^2 rp) = ", Simplify[(vp2/rp)/(1/rp^2) - (2 + vinf^2 rp)]];
Print["   abzugebende Energie v_p^2/2 - v_c^2/2 = ", Simplify[vp2/2 - vc2/2], " ; fuer vinf = 0 gleich -E_Kreis = ", Simplify[-(vc2/2 - 1/rp)]];
Print["2) Auslegung P: b' aus Auslesepunkt und Einflugrichtung"];
e = Sqrt[1 + b^2 v^4]; rpe = (e - 1)/v^2;
Print["   b'^2 - rp^2 (1 - 1/e^2) mit Winkel Pi - ArcCos[-1/e] zwischen Ort und Richtung: ", FullSimplify[(rpe Sin[Pi - ArcCos[-1/e]])^2 - rpe^2 (1 - 1/e^2), {b > 0, v > 0}]];
Print["   b' < rp < b: b'/rp = ", FullSimplify[Sqrt[1 - 1/e^2], {b > 0, v > 0}], " ; rp/b = ", FullSimplify[rpe/b, {b > 0, v > 0}], " ; Reihe b' fuer kleines b: ", Series[rpe Sqrt[1 - 1/e^2], {b, 0, 3}] // Normal];
Print["3) Schwung holen: fernster Punkt"];
Print["   aus Energie und Drehimpuls: ", Solve[{k^2/2 - 1 == vq^2/2 - 1/ra, k == ra vq, ra != 1}, {ra, vq}] // Simplify];
Print["4) Schwarzschild: Kreisbahn mit E = 1"];
ee[r_] := (1 - 2 m/r)^2/(1 - 3 m/r); ll[r_] := m r^2/(r - 3 m);
Print["   E^2 = 1 bei r = ", Solve[ee[r] == 1 && r > 3 m && m > 0, r, Reals] // Simplify, " ; dort L^2 = ", Simplify[ll[4 m]]];
veff[r_, L_] := (1 - 2 m/r) (1 + L^2/r^2);
Print["   V_eff(4m, L = 4m) = ", Simplify[veff[4 m, 4 m]], " , V_eff' = ", Simplify[D[veff[r, 4 m], r] /. r -> 4 m], " , V_eff'' = ", Simplify[D[veff[r, 4 m], {r, 2}] /. r -> 4 m], " (negativ: Maximum, instabil)"];
Print["   innerste stabile Kreisbahn (L^2 minimal): ", Solve[D[ll[r], r] == 0 && r > 3 m && m > 0, r, Reals]];
Print["   E^2 -> unendlich bei r -> 3m; Licht: kritischer Stossparameter^2 = r^2/(1 - 2m/r) bei r = 3m: ", Simplify[r^2/(1 - 2 m/r) /. r -> 3 m]];
Print["   noetige Zusatzkraft: Verhaeltnis L^2(Einfall aus der Ruhe, naechster Punkt r)/L^2(Kreis bei r) = ", ratio = Simplify[(2 m r^2/(r - 2 m))/ll[r]], " ; gleich 1 bei r = ", Solve[ratio == 1, r], " ; Grenzwert r -> unendlich: ", Limit[ratio, r -> Infinity]];
Print["5) addierte Auslesen, gleiche Radien: Im[r E^(I w t) + r E^(-I w t)] = ", Simplify[ComplexExpand[Im[r Exp[I w t] + r Exp[-I w t]]]], " ; Re = ", Simplify[ComplexExpand[Re[r Exp[I w t] + r Exp[-I w t]]]]];
Print["6) numerisch (NDSolve, 30 Stellen): E = 1, L = 4m(1 + 10^-6), m = 1/20"];
Module[{m0 = 1/20, L0, sol, umax, ph},
  L0 = 4 m0 (1 + 10^-6);
  sol = NDSolve[{u''[p] + u[p] == m0/L0^2 + 3 m0 u[p]^2, u[0] == 0, u'[0] == 0, WhenEvent[u'[p] < 0, ph = p; "StopIntegration"]}, u, {p, 0, 100}, WorkingPrecision -> 30, AccuracyGoal -> 20, PrecisionGoal -> 20, MaxSteps -> 10^6][[1]];
  Print["   innerster Radius ", N[1/(u[ph] /. sol)/m0, 10], " m nach ", N[ph/(2 Pi), 6], " Umlaeufen (halbe Bahn)"]];
