(* k395b / k396b: Gegenprobe mit Wolfram Language (exakt, wo moeglich). Ausgabe in k395b_out.txt *)
Print["k395b: Schleife L3"]; x[b_] := (1 - b)/(1 + b); f3[b_] := Simplify[(1 - x[b]) ((1 - x[b])/(1 + x[b])) b + x[b]]; Print["f3 = ", f3[b], "; Rest gegen (2b^3-b+1)/(1+b): ", Simplify[f3[b] - (2 b^3 - b + 1)/(1 + b)]];
Print["Fixpunkte: ", Solve[f3[b] == b, b]]; Print["Steigungen bei 1/2 und 1: ", {D[f3[b], b] /. b -> 1/2, D[f3[b], b] /. b -> 1}];
Print["zweite Ableitung bei 1/2: ", D[f3[b], {b, 2}] /. b -> 1/2];
f2[b_, c_] := (1 - x[b]) c b + x[b]; Print["L2 Fixpunkte allgemein: ", Simplify[Solve[f2[b, c] == b, b]]]; Print["L2, c = 1/2: ", Solve[f2[b, 1/2] == b, b]];
gL = g /. FindRoot[Sum[2^(1 - g Sqrt[k (k + 2)/3]), {k, 1, 600}] == 1, {g, 1.8}, WorkingPrecision -> 30];
Print["gamma_L = ", N[gL, 15], "; beta_sym = ", N[Sqrt[(gL - 1)/(gL + 1)], 15]];
c0 = c /. First[Solve[f2[1/gL, c] == 1/gL, c]]; Print["L2 trifft 1/gamma_L bei cos 2alpha = ", N[c0, 10], ", alpha = ", N[ArcCos[c0]/2/Degree, 8], " Grad"];
Print["k396b"]; gH = g /. First[Solve[Sum[2^(1 - g (k + 1)/2), {k, 1, Infinity}] == 1 && g > 0, g, Reals]]; Print["glatt: gamma = ", gH];
da = NSum[2^-k (Sqrt[k (k + 2)/3] - (k + 1)/2), {k, 1, Infinity}, WorkingPrecision -> 25]; Print["<delta a> = ", N[da, 10], "; <a> = ", Sum[2^-k (k + 1)/2, {k, 1, Infinity}]];
Print["erste Ordnung 1/gamma - 1/2 = ", N[(2 da/(3/2))/4, 10], "; voll = ", N[1/gL - 1/2, 10]];
Print["p_1 = ", N[2^(1 - gL), 12], "; beta_sym - p_1 = ", N[Sqrt[(gL - 1)/(gL + 1)] - 2^(1 - gL), 8]];
Print["gamma mit p_1 = beta: ", g /. FindRoot[2^(1 - g) == Sqrt[(g - 1)/(g + 1)], {g, 1.86}, WorkingPrecision -> 20]];
Print["gestoerte Schleife, Gedaechtnis m: Fixpunktbedingung (2b-1)(b+1) = m (b-1); m fuer 1/gamma_L: ", N[(2 b - 1) (b + 1)/(b - 1) /. b -> 1/gL, 10]];
