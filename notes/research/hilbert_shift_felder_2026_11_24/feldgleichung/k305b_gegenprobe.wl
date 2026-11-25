(* k305b: Gegenprobe zu k305 (H136) in Wolfram Language. Aufruf: wolframscript -file k305b_gegenprobe.wl > k305b_out.txt *)
mW = 80.37; mZ = 91.19; mt = 172.6; v = 246.22; mu = 0.3018; th0 = ArcTan[mu]; ks = 1.2039;
g2 = 4 mW^2/v^2; gp2 = 4 (mZ^2 - mW^2)/v^2; yt2 = 2 mt^2/v^2; cW = g2/4; cZ = (g2 + gp2)/4; ct0 = yt2/2;
cS[th_, k1_, k2_] := 2 (k1 Cos[th]^2 + k2 Sin[th]^2); ct[th_] := ct0 (Cos[th]/Cos[th0])^2;
bB[th_, k1_, k2_] := (4 cS[th, k1, k2]^2 + 6 cW^2 + 3 cZ^2 - 12 ct[th]^2)/(64 Pi^2);
aA[th_, k1_, k2_] := (4 cS[th, k1, k2]^2 (Log[cS[th, k1, k2]] - 3/2) + 6 cW^2 (Log[cW] - 5/6) + 3 cZ^2 (Log[cZ] - 5/6) - 12 ct[th]^2 (Log[ct[th]] - 3/2))/(64 Pi^2);
ff[th_, k1_, k2_] := bB[th, k1, k2] Exp[-2 aA[th, k1, k2]/bB[th, k1, k2]];
k1of[d_] := ks - d Sin[th0]^2;
dF[d_?NumericQ] := (D[ff[t, k1of[d], k1of[d] + d], t] /. t -> th0);
sol = d /. FindRoot[dF[d], {d, -1.2, -1.6}];
Print["k2-k1 = ", sol, "  k1 = ", k1of[sol], "  k2 = ", k1of[sol] + sol];
Print["zweite Ableitung: ", D[ff[t, k1of[sol], k1of[sol] + sol], {t, 2}] /. t -> th0];
Print["Steigung kappa_eff: ", sol Sin[2 th0], "  Regel: ", 2 Sin[2 th0]/Cos[2 th0]^2, "  1/cos(2 th0) = ", 1/Cos[2 th0]];
Print["Vorzeichen von dF auf k2-k1 = -3 ... 3 (Schritt 0.25): ", Sign[Table[dF[d], {d, -3, 3, 0.25}]]];
qm[p_, q_] := {p[[1]] q[[1]] - p[[2]] q[[2]] - p[[3]] q[[3]] - p[[4]] q[[4]], p[[1]] q[[2]] + p[[2]] q[[1]] + p[[3]] q[[4]] - p[[4]] q[[3]], p[[1]] q[[3]] - p[[2]] q[[4]] + p[[3]] q[[1]] + p[[4]] q[[2]], p[[1]] q[[4]] + p[[2]] q[[3]] - p[[3]] q[[2]] + p[[4]] q[[1]]};
e = IdentityMatrix[4]; Lm[u_] := Transpose[Table[qm[e[[u]], e[[k]]], {k, 4}]]; Rm = Transpose[Table[qm[e[[k]], e[[2]]], {k, 4}]];
xs = Array[x, 4]; a1 = x[1]^2 + x[2]^2; b1 = x[3]^2 + x[4]^2;
lie[X_, p_] := Expand[(X . xs) . D[p, {xs}]];
Print["A1-B unter L_j: ", lie[Lm[3], a1 - b1], "   A1+B unter L_j: ", lie[Lm[3], a1 + b1], "   A1-B unter L_i, R_i: ", {lie[Lm[2], a1 - b1], lie[Rm, a1 - b1]}];
