(* k424b: Wolfram-Gegenprobe zu H211 (k424). Normalen n_k = D^k n_0, Drehung um die z-Achse, Schritt ph, Neigung ch. *)
nrm[k_] := RotationMatrix[k ph, {0, 0, 1}] . {Sin[ch], 0, Cos[ch]};
Print["(1) Formelrest: ", FullSimplify[Table[nrm[j] . nrm[k] - (Cos[ch]^2 + Sin[ch]^2 Cos[(j - k) ph]), {j, 0, 4}, {k, 0, 4}]] // Flatten // Union];
c[s_, chi_, phi_] := Cos[chi]^2 + Sin[chi]^2 Cos[s phi];
Print["(2) chi = ArcCos[1/Sqrt[3]], Schritt Pi/4: ", FullSimplify[Table[c[s, ArcCos[1/Sqrt[3]], Pi/4], {s, 1, 4}]]];
Print["    chi = Pi/4: ", FullSimplify[Table[c[s, Pi/4, Pi/4], {s, 1, 4}]]];
Print["    chi = Pi/2: ", FullSimplify[Table[c[s, Pi/2, Pi/4], {s, 1, 4}]]];
en[chi_?NumericQ, phi_, n_] := Sum[(n - s)/Sqrt[1 - c[s, chi, phi]^2], {s, 1, n - 1}];
Do[
  r = FindMinimum[en[x, case[[1]], case[[2]]], {x, 1.1}, AccuracyGoal -> 12, PrecisionGoal -> 12];
  Print["(3) Schritt ", case[[1]], ", ", case[[2]], " Baender: chi* = ", NumberForm[(x /. r[[2]])/Degree, 9], " Grad, E = ", NumberForm[r[[1]], 9],
    ", Winkel ", NumberForm[Table[ArcCos[Abs[c[s, x /. r[[2]], case[[1]]]]]/Degree, {s, 1, case[[2]] - 1}], 5]],
  {case, {{Pi/4, 5}, {2 Pi/5, 5}, {Pi/4, 8}}}];
