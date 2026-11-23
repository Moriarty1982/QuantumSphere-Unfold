(* H123: zeitlich geordnete Oktant-Auslese auf einer Punktierung vom Spin j (Q1a).
   Vorab-Notiz: llm/Vorab_Notiz_H123_Zeitliche_Oktantauslese.md. Ausgabe: llm/h123_temporal_octant.txt.
   Exakt, wo moeglich; Zaehlregel numerisch mit WorkingPrecision 40. Keine absoluten Pfade. *)

js = Range[1/2, 20, 1/2];

(* Spin-kohaerenter Zustand in Richtung (theta, phi), Basis m = j, j-1, ..., -j; globale Phase irrelevant fuer B *)
pw[x_, 0] := 1; pw[x_, k_] := x^k; (* vermeidet 0^0 an den Polen (Korrektur nach erstem Lauf, Programmierfehler) *)
coh[j_, th_, ph_] := Table[Sqrt[Binomial[2 j, j + m]] pw[Cos[th/2], j + m] pw[Sin[th/2], j - m] Exp[-I m ph], {m, j, -j, -1}];
pole[j_, "z", s_] := If[s == 1, coh[j, 0, 0], coh[j, Pi, 0]];
pole[j_, "x", s_] := If[s == 1, coh[j, Pi/2, 0], coh[j, Pi/2, Pi]];
pole[j_, "y", s_] := If[s == 1, coh[j, Pi/2, Pi/2], coh[j, Pi/2, -Pi/2]];
br[u_, v_] := Conjugate[u] . v;
barg[a_, b_, c_] := br[a, b] br[b, c] br[c, a];

signs = Tuples[{1, -1}, 3]; (* {sz, sx, sy} *)

(* Bargmann fuer tau = +1 (R -> T -> J_B) und tau = -1 (umgekehrt) *)
bT[j_, {sz_, sx_, sy_}, tau_] := Module[{a = pole[j, "z", sz], b = pole[j, "x", sx], c = pole[j, "y", sy]},
   If[tau == 1, barg[a, b, c], barg[a, c, b]]];
formula[j_, {sz_, sx_, sy_}, tau_] := 2^(-3 j) Exp[I tau sz sx sy j Pi/2];

(* Theta_j = d^j(pi) K, d^j(pi)_{m',m} = (-1)^(j-m) delta_{m',-m} *)
dpi[j_] := Table[If[mp == -m, (-1)^(j - m), 0], {mp, j, -j, -1}, {m, j, -j, -1}];
theta[j_, v_] := dpi[j] . Conjugate[v];

Print["== Kontrollen =="];
Print["Theta_j^2 = (-1)^(2j) fuer alle j<=20: ",
  And @@ Table[Simplify[dpi[j] . Conjugate[dpi[j]] == (-1)^(2 j) IdentityMatrix[2 j + 1]], {j, js}]];

(* R_j, T_j, J_B,j bilden extremale auf extremale Zustaende ab (exakt bis j=4, numerisch bis 20) *)
Jz[j_] := DiagonalMatrix[Table[m, {m, j, -j, -1}]];
Jp[j_] := Table[If[mp == m + 1, Sqrt[j (j + 1) - m (m + 1)], 0], {mp, j, -j, -1}, {m, j, -j, -1}];
Jx[j_] := (Jp[j] + ConjugateTranspose[Jp[j]])/2;
Jy[j_] := (Jp[j] - ConjugateTranspose[Jp[j]])/(2 I);
extremalOK[j_, ex_] := Module[{Rm, Tm, Bm, poles},
   {Rm, Tm, Bm} = If[ex, MatrixExp[-I Pi #[j]] & /@ {Jz, Jx, Jy}, MatrixExp[-I Pi N[#[j], 30]] & /@ {Jz, Jx, Jy}];
   poles = Flatten[Table[pole[j, ax, s], {ax, {"z", "x", "y"}}, {s, {1, -1}}], 1];
   And @@ Flatten[Table[
      With[{v = M . p}, If[ex, AnyTrue[poles, FullSimplify[Abs[br[#, v]]] == 1 &], Min[Table[Abs[Abs[br[w, N[v, 30]]] - 1], {w, N[poles, 30]}]] < 10^-12]],
      {M, {Rm, Tm, Bm}}, {p, poles}]]];
Print["Frame-Abbildungen erhalten extremale Zustaende, exakt j<=4: ", And @@ Table[extremalOK[j, True], {j, Range[1/2, 4, 1/2]}]];
Print["Frame-Abbildungen erhalten extremale Zustaende, numerisch j<=20 (1e-12): ", And @@ Table[extremalOK[j, False], {j, js}]];

Print["== H123a =="];
resA = Table[FullSimplify[bT[j, s, tau] - formula[j, s, tau]], {j, js}, {s, signs}, {tau, {1, -1}}];
Print["Reste B_tau - 2^(-3j) e^(i tau eps j pi/2), 40 j x 8 x 2 = ", Length[Flatten[resA]], " Faelle, alle 0: ", AllTrue[Flatten[resA], # === 0 &]];
resRev = Table[FullSimplify[bT[j, s, -1] - Conjugate[bT[j, s, 1]]], {j, js}, {s, signs}];
Print["umgekehrte Reihenfolge = konjugiert, alle 0: ", AllTrue[Flatten[resRev], # === 0 &]];
resTh = Table[With[{a = pole[j, "z", s[[1]]], b = pole[j, "x", s[[2]]], c = pole[j, "y", s[[3]]]},
     FullSimplify[barg[theta[j, a], theta[j, b], theta[j, c]] - Conjugate[barg[a, b, c]]]], {j, js}, {s, signs}];
Print["Theta_j konjugiert B, alle 0: ", AllTrue[Flatten[resTh], # === 0 &]];
resTR = Table[With[{a = pole[j, "z", s[[1]]], b = pole[j, "x", s[[2]]], c = pole[j, "y", s[[3]]]},
     FullSimplify[barg[theta[j, a], theta[j, c], theta[j, b]] - barg[a, b, c]]], {j, js}, {s, signs}];
Print["Zeitumkehr des Protokolls (Reihenfolge + Theta_j) laesst B fest, alle 0: ", AllTrue[Flatten[resTR], # === 0 &]];

Print["== H123b =="];
(* Orientierung m -> -m: sz -> -sz bei festen sx, sy; tau = +1 *)
rowsB = Table[Module[{bp = FullSimplify[bT[j, {1, 1, 1}, 1]], bm = FullSimplify[bT[j, {-1, 1, 1}, 1]]},
    {j, bp, bm, FullSimplify[Abs[bp] == Abs[bm]], FullSimplify[bp != bm]}], {j, js}];
Do[Print["j=", r[[1]], "  B(+j)=", r[[2]], "  B(-j)=", r[[3]], "  |gleich|=", r[[4]], "  unterschieden=", r[[5]]], {r, rowsB}];
(* gleiche Pruefung fuer alle vier (sx,sy) *)
allSxSy = And @@ Flatten[Table[FullSimplify[Abs[bT[j, {1, sx, sy}, 1]] == Abs[bT[j, {-1, sx, sy}, 1]]], {j, js}, {sx, {1, -1}}, {sy, {1, -1}}]];
Print["gleicher Betrag fuer alle (sx,sy): ", allSxSy];
D123 = Select[js, Function[j, And @@ Flatten[Table[FullSimplify[bT[j, {1, sx, sy}, 1] != bT[j, {-1, sx, sy}, 1]], {sx, {1, -1}}, {sy, {1, -1}}]]]];
Print["D123 (unterschiedene j): ", D123];
Print["nicht unterschiedene j: ", Complement[js, D123]];
Print["H123b (alle j unterschieden): ", Length[D123] == Length[js]];

Print["== H123c =="];
(* Eigenwert von R_j = exp(-i pi Jz) auf |j,+j>_z und |j,-j>_z *)
rowsC = Table[{j, Exp[-I Pi j], Exp[I Pi j], FullSimplify[Exp[-I Pi j] != Exp[I Pi j]]}, {j, js}];
DR = Select[rowsC, #[[4]] &][[All, 1]];
Print["Einfenster-Auslese unterscheidet j: ", DR];
Print["genau die halbzahligen j: ", DR === Select[js, !IntegerQ[#] &]];

Print["== H123d =="];
jmax = 4000; prec = 40;
area[j_] := Sqrt[j (j + 1)];
sumRule[g_, gam_?NumericQ] := Sum[g[j] Exp[-2 Pi gam area[j]], {j, 1/2, jmax, 1/2}];
rootOf[g_] := gam /. FindRoot[sumRule[g, gam] == 1, {gam, 0.2, 0.05, 0.5}, WorkingPrecision -> prec];
gA2[j_] := 2;
gM123[j_] := If[MemberQ[D123, j] || j > 20 && !(IntegerQ[j] && EvenQ[j]), 2, 1];
(* fuer j>20 wird die Gesetzmaessigkeit aus H123a (Trennung genau fuer j nicht in 2N) verwendet; ausdruecklich vermerkt *)
Print["Hinweis: fuer 20 < j <= 4000 wird D123 per H123a-Formel fortgesetzt (Trennung genau fuer j nicht in 2N)."];
gammaM = rootOf[gA2];
Print["Kontrolle (A,2): gamma_M = ", N[gammaM, 10], "  |gamma_M - 0.237533| < 1e-6: ", Abs[gammaM - 0.237533] < 10^-6];
gammaT = Log[2]/(Pi Sqrt[3]); (* Wurzel von 2 e^(-2 pi gamma sqrt(3)/2) = 1 *)
Print["gamma_T (S1/2, g=2) = ", N[gammaT, 10], "; j=1/2 in D123: ", MemberQ[D123, 1/2]];
tail = N[2 Sum[Exp[-2 Pi gammaM area[j]], {j, jmax + 1/2, jmax + 50, 1/2}], 20];
Print["Restglied-Abschaetzung jenseits j_max (Groessenordnung): ", ScientificForm[tail, 3]];
gammaM123 = rootOf[gM123];
gL = gammaM123/gammaT; beta = Sqrt[(gL - 1)/(gL + 1)]; mZ = 91.1880`20; mW = mZ gL/Sqrt[1 + gL^2]; OmM = beta^2;
Print["gamma_M' = ", N[gammaM123, 10], "  gamma_L' = ", N[gL, 10], "  beta' = ", N[beta, 8], "  m_W' = ", N[mW, 8], " GeV  Omega_M' = ", N[OmM, 6]];
inBeta = 0.545 <= beta <= 0.570; inMW = Abs[mW - 80.3692] <= 2*0.0133; inOm = Abs[OmM - 0.2975] <= 2*0.0086;
Print["Fenster beta [0.545,0.570]: ", inBeta, "; m_W 80.3692+-2*0.0133: ", inMW, " (Abstand ", N[(mW - 80.3692)/0.0133, 4], " sigma); Omega_M 0.2975+-2*0.0086: ", inOm, " (", N[(OmM - 0.2975)/0.0086, 4], " sigma)"];
Print["H123d traegt (alle drei Fenster): ", inBeta && inMW && inOm];

Print["== Nebenrechnung (kein Kriterium): gebogenes Dreieck =="];
(* Phase phi je Spin 1/2 -> 2 j phi; trennt, wenn 2 j phi nicht in pi Z. phi = 2/3 (Biegung zu phi = 2/3, r16.7) und phi = pi/4 - gammaM/2 (Restbiegung) *)
Print["phi = 2/3: unterschiedene j<=20: ", Length[Select[js, !IntegerQ[Rationalize[2 # (2/3)/Pi, 0]] &]], " von ", Length[js], " (pi irrational: alle)"];
Print["phi = pi/4 - gamma_M/2 = ", N[Pi/4 - gammaM/2, 10], ": kleinster Abstand von 2 j phi zu pi Z ueber j<=20: ",
  N[Min[Table[Abs[2 j (Pi/4 - gammaM/2)/Pi - Round[2 j (Pi/4 - gammaM/2)/Pi]], {j, js}]], 6]];
