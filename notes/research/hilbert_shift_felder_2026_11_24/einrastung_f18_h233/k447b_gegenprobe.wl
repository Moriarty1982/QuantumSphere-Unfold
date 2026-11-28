(* k447b: Wolfram-Gegenprobe zu H233 (Einrastung auf 8 Stellungen). Exakte Eingaben, Reste mit Round auf exakten Gittern.
   Ausgefuehrt ueber den Wolfram-Evaluator; Ausgabe in k447b_out.txt. *)
x = Pi/12 - 2222220470731/10^13; sx = 78/10^8; beta = 549405640974529/10^15; sb = 18/10^5; gl = 1864699764609373/10^15;
th[s2_, e_] := {ArcSin[Sqrt[s2]], e/(2 Sqrt[s2 (1 - s2)])};
q = <|"phi" -> {x, sx}, "xnu" -> {4336/10^5, 213/10^5}, "t12" -> th[3036/10^4, 64/10^4], "t13" -> th[2248/10^5, 56/10^5],
   "t23" -> th[470/1000, 15/1000], "dCP" -> {212 Degree, 34 Degree}, "atanb" -> {ArcTan[beta], sb/(1 + beta^2)}, "asinb" -> {ArcSin[beta], sb/Sqrt[1 - beta^2]}|>;
res = Flatten[Table[With[{v = q[n][[1]], s = q[n][[2]], d = b/2^k},
     With[{m = Round[v/d]}, If[d >= 10 s, {n, b, k, m, N[(v - m d)/s, 6], N[4 s/d], Abs[v - m d] <= 2 s}, Nothing]]],
    {n, Keys[q]}, {b, {Pi/4, Pi/12}}, {k, 0, 8}], 2];
hits = Select[res, Last];
Print["Treffer: ", {#[[1]], #[[2]], #[[3]], #[[4]], #[[5]]} & /@ hits];
Print["Anzahl ", Length[hits], ", lambda = ", Total[res[[All, 6]]], ", phi-Treffer ", Count[hits, {"phi", __}], ", lambda_phi = ", Total[Select[res, #[[1]] == "phi" &][[All, 6]]]];
Print["phi bester Rest (sigma): ", MinimalBy[Select[res, #[[1]] == "phi" &], Abs[#[[5]]] &]];
Print["eindeutige Gitterpunkte je Groesse: ", DeleteDuplicates[{#[[1]], N[#[[4]] #[[2]]/2^#[[3]], 8]} & /@ hits]];
e0 = ArcTanh[beta]; cand = {ArcTan[beta], ArcSin[beta], ArcCos[beta], e0, 2 e0, 1/gl, beta};
rs = Flatten[Table[With[{r = Mod[a, s]}, {N[(r - x)/sx, 6], N[(s - r - x)/sx, 6]}], {a, cand}, {s, {Pi/4, Pi/12}}]];
Print["C: kleinster Abstand in sigma: ", MinimalBy[rs, Abs], "  ; innerhalb 1 %: ", Count[rs, z_ /; Abs[z sx] <= N[x/100]]];
