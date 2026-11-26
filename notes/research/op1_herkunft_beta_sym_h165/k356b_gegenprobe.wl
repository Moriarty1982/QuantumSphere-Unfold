(* k356b: Gegenprobe zu H165 in Wolfram Language, unabhaengig von k356. *)
c[k_] := Sqrt[k (k + 2)/3];
(* K-a: Ziel. Summe bis 400 abgeschnitten (Rest < 10^-200), 40 Stellen *)
z[g_?NumericQ] := Sum[2^(1 - g c[k]), {k, 1, 400}];
gL = g /. FindRoot[z[g] == 1, {g, 19/10}, WorkingPrecision -> 40];
gM = g /. FindRoot[Sum[2 Exp[-Pi g Sqrt[k (k + 2)]], {k, 1, 400}] == 1, {g, 24/100}, WorkingPrecision -> 40];
gT = N[Log[2]/(Pi Sqrt[3]), 40];
b = Sqrt[(gL - 1)/(gL + 1)];
Print["gamma_M = ", N[gM, 30]]; Print["gamma_T = ", N[gT, 30]];
Print["Wurzel Z=1 = ", N[gL, 30], " ; gamma_M/gamma_T - Wurzel = ", N[gM/gT - gL, 5]];
Print["beta = ", N[b, 30], " ; artanh beta = ", N[ArcTanh[b], 30]];
Print["Hopf-Variante: ", Solve[Sum[2 x^(k + 1), {k, 1, Infinity}] == 1 && 0 < x < 1, x], " mit x = 2^(-g/2), also g = ", -2 Log[2, 1/2]];
(* K-b *)
Print["Sum 2 q^k = 1: ", Solve[Sum[2 q^k, {k, 1, Infinity}] == 1 && 0 < q < 1, q]];
Print["Identitaet: Sum_{k>=1} 2 beta^(2k) - (gammaL - 1) mit gammaL=(1+beta^2)/(1-beta^2): ",
  FullSimplify[Sum[2 bb^(2 k), {k, 1, Infinity}] - ((1 + bb^2)/(1 - bb^2) - 1), 0 < bb < 1]];
qc = q /. FindRoot[Sum[2 q^c[k], {k, 1, 400}] == 1, {q, 3/10}, WorkingPrecision -> 30];
qs = q /. FindRoot[Sum[2 q^Sqrt[k (k + 2)], {k, 1, 400}] == 1, {q, 4/10}, WorkingPrecision -> 30];
Print["Exponent c_k: beta = ", N[Sqrt[qc], 12], " ; Kontrolle 2^(-gL/2) = ", N[2^(-gL/2), 12]];
Print["Exponent Sqrt[k(k+2)]: beta = ", N[Sqrt[qs], 12]];
Print["noetiges p = ", N[Log[3]/-Log[b], 12]];
(* K-c *)
p[k_] := 2^(1 - gL c[k]); mean[f_] := Sum[p[k] f[k], {k, 1, 400}];
gsc = g /. FindRoot[2^(1 - g) == Sqrt[(g - 1)/(g + 1)], {g, 186/100}, WorkingPrecision -> 30];
cm = mean[c];
Print["1: ", N[p[1], 12], " gegen beta, rel ", N[p[1]/b - 1, 4]];
Print["2: ", N[gsc, 12], " gegen gammaL, rel ", N[gsc/gL - 1, 4]];
Print["3: ", N[1/cm, 12], " gegen ", N[ArcTanh[1/Sqrt[3]], 12], ", rel ", N[1/cm/ArcTanh[1/Sqrt[3]] - 1, 4]];
Print["4: <k> = ", N[mean[# &], 12], " rel ", N[mean[# &]/gL - 1, 4]];
Print["5: <Sqrt[j/(j+1)]> = ", N[mean[Sqrt[#/(# + 2)] &], 12]];
Print["6: <1/c> = ", N[mean[1/c[#] &], 12]];
Print["7: p1/(1-p1) = ", N[p[1]/(1 - p[1]), 12], " ; gammaL-1 = ", N[gL - 1, 12], " ; 1/beta^2-2 = ", N[1/b^2 - 2, 12]];
Print["8: <c> = ", N[cm, 12], " ; gammaL-1/3 = ", N[gL - 1/3, 12]];
(* K-d *)
Print["Kegel: ", FullSimplify[(1/2)/Sqrt[(1/2) (3/2)]], " ; cos(2 theta) = ", FullSimplify[2 ((1/2)/Sqrt[3/4])^2 - 1], " ; ArcCos[-1/3] in Grad = ", N[ArcCos[-1/3]/Degree, 8]];
