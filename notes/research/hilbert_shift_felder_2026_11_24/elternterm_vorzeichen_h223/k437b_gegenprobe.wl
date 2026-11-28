(* k437b (H223): unabhaengige Wolfram-Gegenprobe zu k437. Aufruf: wolframscript -file k437b_gegenprobe.wl > k437b_out.txt *)
lam = Table[ph + 2 r Cos[d + 2 Pi k/3], {k, 0, 2}];
red[e_] := Expand[Simplify[TrigReduce[Expand[TrigExpand[e]]]] /. Cos[3 d] -> cc];
e1 = red[Total[lam]]; e2 = red[lam[[1]] lam[[2]] + lam[[2]] lam[[3]] + lam[[1]] lam[[3]]]; e3 = red[Times @@ lam];
t2 = red[Total[lam^2]]; t3 = red[Total[lam^3]];
Print["e1=", e1, "  e2=", e2, "  e3=", e3, "  TrW2=", t2, "  TrW3=", t3];
ug = Expand[x e1^3 + y e1 t2 + z e3];
b3[u_] := Coefficient[Expand[u^2], ph^3 r^3 cc];
Print["allgemein beta3(J) = ", Factor[b3[ug]]];
cands = {"det" -> e3, "TrW3" -> t3, "(TrW)^3" -> e1^3, "det spurfrei" -> red[Times @@ Table[2 r Cos[d + 2 Pi k/3], {k, 0, 2}]], "TrW TrW2" -> e1 t2, "TrW3-(TrW)^3/9" -> Expand[t3 - e1^3/9], "e1e2-9e3" -> Expand[e1 e2 - 9 e3]};
xl = Pi/12 - 0.2222220470731;
br = {{5 Pi/4 + xl, Pi/4 + xl}, {Pi/2 + xl, 3 Pi/2 + xl}};
Do[Module[{u = c[[2]], f},
   f[dd_] := (u /. {ph -> 1, r -> 1/Sqrt[2], cc -> Cos[3 dd]})^2;
   Print[c[[1]], ": u = ", u, ";  beta3(J) = ", b3[u], ";  J-proj. Delta(Im,Re) = ", N[b3[u] (Cos[3 #[[1]]] - Cos[3 #[[2]]]) & /@ br, 6], ";  voll Delta(Im,Re) = ", N[f[#[[1]]] - f[#[[2]]] & /@ br, 6]]], {c, cands}];
