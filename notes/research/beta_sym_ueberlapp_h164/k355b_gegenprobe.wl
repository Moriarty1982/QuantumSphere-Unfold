(* k355b: Gegenprobe zu H164 in Wolfram Language, exakt (unabhaengig von k355: Aberrationsformel fuer Bloch-Vektoren statt SL(2,C)-Matrix).
   Ausgefuehrt am 26.11.2026; Ausgabe in k355b_out.txt. *)
$Assumptions = 0 < b < 1;
Print["1) Paar (K1, S): |<S|K1>| = ", FullSimplify[Abs[{0, 1} . {Sqrt[1 - b^2], b}]], " ; theta = Pi - theta_H: Cos[(Pi - 2 ArcSin[b])/2] - b = ", FullSimplify[Cos[(Pi - 2 ArcSin[b])/2] - b]];
gL = (1 + b^2)/(1 - b^2); eps = ArcTanh[b];
Print["2) gamma der Relativgeschwindigkeit 2b/(1+b^2) minus gamma_L = ", FullSimplify[1/Sqrt[1 - (2 b/(1 + b^2))^2] - gL], " ; Sech[2 eps] - 1/gamma_L = ", FullSimplify[Sech[2 eps] - 1/gL]];
thH = 2 ArcSin[b]; nN = {0, 0, 1}; nS = {0, 0, -1}; nK = {Sin[thH], 0, Cos[thH]};
u = FullSimplify[(nK + nS)/Sqrt[(nK + nS) . (nK + nS)]];
ab[n_] := Module[{par = n . u}, FullSimplify[((n - par u) Sqrt[1 - b^2] + (par - b) u)/(1 - b par)]];
iN = ab[nN]; iS = ab[nS]; iK = ab[nK];
Print["3) Bilder: K1'.S' = ", FullSimplify[iK . iS], " (Gegenpunkte) ; |N'|^2 = ", FullSimplify[iN . iN]];
Print["   N'.K1' = ", FullSimplify[iN . iK], " ; minus 1/gamma_L = ", FullSimplify[iN . iK - 1/gL], " ; minus Cos[2 ArcTan[b]] = ", FullSimplify[iN . iK - Cos[2 ArcTan[b]]]];
Print["   N'.S' = ", FullSimplify[iN . iS], " ; plus 1/gamma_L = ", FullSimplify[iN . iS + 1/gL]];
Print["   vorher: N.K1 = ", FullSimplify[nN . nK], " = 1 - 2 b^2"];
Print["4) Besetzungen von K1' bezueglich der Achse N': (1 + N'.K1')/2 = ", FullSimplify[(1 + iN . iK)/2], " ; Materie-Zustand 1/(1 + b^2): Differenz ", FullSimplify[(1 + iN . iK)/2 - 1/(1 + b^2)]];
Print["5) Mischung der zwei Auslesen: Laenge^2 von (nK + nS)/2 = ", FullSimplify[(nK + nS) . (nK + nS)/4], " ; gleich 1/gamma_L^2 fuer b = ", NSolve[b^3 + b^2 + b - 1 == 0 && 0 < b < 1, b, 10]];
d = Pi - 2 ArcSin[1/Sqrt[3]] - ArcCos[-1/3];
Print["6) Hopf-Wert b = 1/Sqrt[3]: Cos[Pi - 2 ArcSin[1/Sqrt[3]]] = ", FullSimplify[Cos[Pi - 2 ArcSin[1/Sqrt[3]]]], " ; Differenz zum Tetraederwinkel numerisch ", N[d, 30], " ; gamma_L = ", gL /. b -> 1/Sqrt[3], " ; N'.K1' = ", FullSimplify[(iN . iK) /. b -> 1/Sqrt[3]]];
Print["7) Zahlen: b = 0.5493482: N'.K1' = ", N[(iN . iK) /. b -> 0.5493482, 8], " , Winkel ", N[ArcCos[(iN . iK) /. b -> 0.5493482] 180/Pi, 8], " Grad"];
