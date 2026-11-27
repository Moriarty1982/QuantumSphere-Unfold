(* k393b: Gegenprobe zu k393 in Wolfram Language. Formel fuer die gyroskopisch gekoppelten Frequenzquadrate exakt; Stichprobe gegen die Daten.
   Ausgabe: k393b_out.txt *)
M = {{ha - om^2 - x, -2 I om Sqrt[x]}, {2 I om Sqrt[x], hb - om^2 - x}};
char = Expand[Det[M]];
Print["Charakteristische Gleichung in x = Omega^2: ", Collect[char, x], " = 0"];
target = {(ha + hb)/2 + om^2 - Sqrt[(ha - hb)^2/4 + 2 om^2 (ha + hb)], (ha + hb)/2 + om^2 + Sqrt[(ha - hb)^2/4 + 2 om^2 (ha + hb)]};
Print["Rest gegen die Formel der Vorab-Notiz (eingesetzt): ", Simplify[char /. x -> # & /@ target]];
Print["Produkt minus (ha - om^2)(hb - om^2): ", Simplify[Times @@ target - (ha - om^2) (hb - om^2)], "; Summe: ", Simplify[Total[target]]];
Print["Grenzfall ha = hb = h: ", Simplify[target /. {ha -> h, hb -> h}, Assumptions -> {h > 0, om > 0}]];
l = Sort[Table[1 + Sqrt[2] Cos[2/9 + 2 Pi k/3], {k, 0, 2}], N[#1, 30] < N[#2, 30] &];
f9 = N[{l[[3]] (l[[1]] + l[[2]]), l[[2]] (l[[1]] + l[[3]]), l[[1]] (l[[2]] + l[[3]])}, 30];
spec[w_] := Sort[{f9[[3]], (f9[[1]] + f9[[2]])/2 + w - Sqrt[(f9[[1]] - f9[[2]])^2/4 + 2 w (f9[[1]] + f9[[2]])], (f9[[1]] + f9[[2]])/2 + w + Sqrt[(f9[[1]] - f9[[2]])^2/4 + 2 w (f9[[1]] + f9[[2]])]}];
m = {154/10^7, 306/10^6, 1630/10^5}; s = {2/10^7, 4/10^6, 9/10^5}; r = m[[1 ;; 2]]/m[[3]]; sr = r Sqrt[(s[[1 ;; 2]]/m[[1 ;; 2]])^2 + (s[[3]]/m[[3]])^2];
dev[w_?NumericQ] := Module[{sp = spec[w]}, Max[Abs[(sp[[1 ;; 2]]/sp[[3]] - r)/sr]]];
tab = Table[{w, dev[w]}, {w, 163/100, 164/100, 1/20000}]; best = First[SortBy[tab, Last]];
Print["Stichprobe Down, Omega^2 = m, +f9, Ebene (1,2): f9 = ", N[f9, 8], "; bester Abstand ", N[best[[2]], 4], " sigma bei w = ", N[best[[1]], 7], "; Spektrum ", N[spec[best[[1]]], 6]];
