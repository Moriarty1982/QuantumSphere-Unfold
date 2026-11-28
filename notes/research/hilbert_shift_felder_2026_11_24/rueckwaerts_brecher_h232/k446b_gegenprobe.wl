(* k446b: Wolfram-Gegenprobe zu H232 (Rueckwaertssuche nach dem Brecher).
   A1 symbolisch (Huellkurve), A2 fuehrende Ordnung, B als geschlossenes Gleichungssystem (dI, dR, phi, r) mit FindRoot,
   Globalitaet per Gitter, direkte Rechnung bei r = 2/3|q|, C Verlauf in q.  Ausgefuehrt ueber den Wolfram-Evaluator. *)
x = Pi/12 - 2222220470731/10^13; xnu = 4336/10^5; q = -852/10^4;
vI[d_, p_, r_] := -Cos[2 (d - Pi/4 - p)] + q Cos[3 d] + r Cos[6 d];
vR[d_, p_, r_] := Cos[2 (d - p)] + q Cos[3 d] + r Cos[6 d];
a1 = Simplify[(D[vI[d, p, r], p] /. d -> 5 Pi/4 + oI) + (D[vR[d, p, r], p] /. d -> Pi/2 + oR)];
Print["A1 dE/dphi = ", a1, " ; TrigFactor: ", TrigFactor[a1]];
ca = Cos[3 x - Pi/4]; cb = Sin[3 x]; da = D[Cos[3 t - Pi/4], t] /. t -> x; db = D[Sin[3 t], t] /. t -> x;
c0 = (ca da + cb db)/(da + db); Print["A2 c0 = ", N[c0, 12], "  1/(4c0) = ", N[1/(4 c0), 12]];
eqs = {D[vI[dI, p, r], dI] == 0, D[vR[dR, p, r], dR] == 0,
   (D[vI[d, p, r], p] /. d -> dI) + (D[vR[d, p, r], p] /. d -> dR) == 0, dI == 5 Pi/4 + x};
sol = FindRoot[eqs, {{dI, N[5 Pi/4 + x, 40]}, {dR, N[Pi/2 + x, 40]}, {p, N[x, 40]}, {r, 57/1000}}, WorkingPrecision -> 40];
Print["B r* = ", N[r /. sol, 15], "  r*/|q| = ", N[(r /. sol)/Abs[q], 15], "  phi = ", N[p /. sol, 12], "  off_Re = ", N[(dR /. sol) - Pi/2, 10],
  "  z = ", N(((dR /. sol) - Pi/2 - xnu)/(213/10^5)) // N];
rs = r /. sol; ps = p /. sol;
Print["Kruemmungen: V_Im'' = ", N[D[vI[d, ps, rs], {d, 2}] /. d -> (dI /. sol)], ", V_Re'' = ", N[D[vR[d, ps, rs], {d, 2}] /. d -> (dR /. sol)]];
gI = NMinimize[{vI[d, ps, rs], 0 <= d <= 2 Pi}, d, Method -> "DifferentialEvolution"]; gR = NMinimize[{vR[d, ps, rs], 0 <= d <= 2 Pi}, d, Method -> "DifferentialEvolution"];
Print["global Im ", gI, " vs Daten ", N[vI[dI /. sol, ps, rs]], ";  global Re ", gR, " vs Daten ", N[vR[dR /. sol, ps, rs]]];
eE[pp_?NumericQ] := Module[{g = N[Subdivide[0, 2 Pi, 3000]]}, Min[vI[g, pp, N[rs]]] + Min[vR[g, pp, N[rs]]]];
ph = N[Subdivide[0, 2 Pi/3, 720]]; ev = eE /@ ph; k = Ordering[ev, 3];
Print["E-Gitter beste: ", Transpose[{ph[[k]], ev[[k]]}], "  E(x-Loesung) ~ ", eE[N[ps]], "  Partner pi/4-phi = ", N[Pi/4 - ps]];
sol2 = FindRoot[{D[vI[dI, p, 2/3 Abs[q]], dI] == 0, D[vR[dR, p, 2/3 Abs[q]], dR] == 0, (D[vI[d, p, 2/3 Abs[q]], p] /. d -> dI) + (D[vR[d, p, 2/3 Abs[q]], p] /. d -> dR) == 0},
   {{dI, N[5 Pi/4 + x, 40]}, {dR, N[Pi/2 + x, 40]}, {p, N[x, 40]}}, WorkingPrecision -> 40];
Print["r = 2/3|q|: off_Im = ", N[(dI /. sol2) - 5 Pi/4, 12], "  (x = ", N[x, 12], ", Abstand ", N[((dI /. sol2) - 5 Pi/4 - x)/(78/10^8), 6], " sigma), off_Re = ", N[(dR /. sol2) - Pi/2, 8]];
(* C: Verlauf in q (zweiter Aufruf) *)
res[qq_] := Module[{wI, wR, s},
  wI[d_, p_, r_] := -Cos[2 (d - Pi/4 - p)] + qq Cos[3 d] + r Cos[6 d];
  wR[d_, p_, r_] := Cos[2 (d - p)] + qq Cos[3 d] + r Cos[6 d];
  s = FindRoot[{D[wI[dI, p, r], dI] == 0, D[wR[dR, p, r], dR] == 0, (D[wI[d, p, r], p] /. d -> dI) + (D[wR[d, p, r], p] /. d -> dR) == 0, dI == 5 Pi/4 + x},
    {{dI, N[5 Pi/4 + x, 40]}, {dR, N[Pi/2 + x, 40]}, {p, N[x, 40]}, {r, 0.6674 Abs[qq]}}, WorkingPrecision -> 40];
  {qq, N[(r /. s)/Abs[qq], 10], N[(dR /. s) - Pi/2, 8], N[((dR /. s) - Pi/2 - xnu)/(213/10^5), 4]}];
Print[TableForm[res /@ {-1/10^6, -1/10^4, -1/10^3, -1/100, -3/100, -852/10^4}]];
