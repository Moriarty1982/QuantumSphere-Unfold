(* k443b: Wolfram-Gegenprobe zu H229 (J bei Ordnung 6 gelockert, volles N^2).
   1) delta-Teil von N^2 bei K = 2/3 symbolisch.  2) Teil c geschlossen: w* aus der Stationaritaet im Im-Sektor, Re-Versatz per FindRoot.
   3) Teil b: globale Minima von E(phi; w) fuer einige w, Gitter in delta (vektorisiert) plus FindMinimum; N vor Sort.
   Aufruf: wolframscript -file k443b_gegenprobe.wl > k443b_out.txt *)
nn = ph^3 - 3 ph r^2 + 2 r^3 Cos[3 d];
n2 = Collect[TrigReduce[Expand[nn^2]], {Cos[3 d], Cos[6 d]}, Factor];
Print["1) N^2 = ", n2];
Print["1) delta-Teil bei ph = Sqrt2 r, geteilt durch 2 r^6: ", Simplify[TrigReduce[(Coefficient[n2, Cos[3 d]] Cos[3 d] + Coefficient[n2, Cos[6 d]] Cos[6 d]) /. ph -> Sqrt[2] r]/(2 r^6)]];

x = Pi/12 - 2222220470731/10^13; xnu = 4336/10^5; sxnu = 213/10^5;
g[d_] := -2 Sqrt[2] Cos[3 d] + Cos[6 d];
vIm[d_, p_, w_] := -Cos[2 (d - Pi/4 - p)] + w g[d];
vRe[d_, p_, w_] := Cos[2 (d - p)] + w g[d];
(* 2) Teil c (Datenzweige als Minima: Im 5pi/4 + phi ~ pi/12 - phi, Re pi/2 + phi ~ pi/6 - phi).
   Erste Fassung setzte delta = pi/12 - x direkt an (kein Minimum des Sektorpotentials); vor der Auswertung korrigiert. *)
Print["2) g'(5pi/4) = ", Simplify[g'[5 Pi/4]], ",  g''(5pi/4) = ", Simplify[g''[5 Pi/4]], ";  g'(pi/2) = ", Simplify[g'[Pi/2]]];
offIm[w_?NumericQ] := (t /. FindMinimum[-Cos[2 (t - Pi/4)] + w g[t], {t, N[5 Pi/4] + 0.01}, WorkingPrecision -> 30][[2]]) - 5 Pi/4;
offRe[w_?NumericQ] := (t /. FindMinimum[Cos[2 t] + w g[t], {t, N[Pi/2] + 0.01}, WorkingPrecision -> 30][[2]]) - Pi/2;
Do[Print["2) w = ", w, ": Im-Versatz (phi=0) = ", N[offIm[w], 6], ",  Re-Versatz = ", N[offRe[w], 8]], {w, {1/1000, 1/100, 1/10, 1, 3}}];
dI = 5 Pi/4 + x;
wst = -(D[-Cos[2 (dd - Pi/4)], dd] /. dd -> dI)/(g'[dI]);
Print["2) formales w fuer Im-Versatz x (Stationaritaet bei 5pi/4 + x): ", N[wst, 10], " (negativ = unbeschraenkt, ausgeschlossen)"];
(* 3) Teil b (so ausgefuehrt) *)
gridD = N[Subdivide[0, 2 Pi, 1500]];
emin[c_, a_, p_, w_] := Module[{v = -a Cos[2 (gridD - c - p)] + w g[gridD], k}, k = Ordering[v, 1][[1]];
   FindMinimum[-a Cos[2 (t - c - p)] + w g[t], {t, gridD[[k]]}][[1]]];
eE[p_?NumericQ, w_] := emin[N[Pi/4], 1., p, w] + emin[0., -1., p, w];
Do[Module[{ph = N[Subdivide[0, Pi/3, 240]][[;; -2]], ev, k, pm},
   ev = eE[#, w] & /@ ph; k = Ordering[ev, 1][[1]];
   pm = Quiet[p /. FindMinimum[eE[p, w], {p, ph[[k]]}][[2]]];
   Print["3) w = ", w, ": globales Minimum von E bei phi = ", Mod[pm, N[Pi/3]], " ; Gitterbester ", ph[[k]], " (pi/12 = ", N[Pi/12], ", pi/8 = ", N[Pi/8], ", pi/6 = ", N[Pi/6], ")"]],
  {w, {0.001, 0.1, 1., 3.}}];
