(* k304b: Gegenprobe zu k304 (H135) in Wolfram Language. Aufruf: wolframscript -file k304b_gegenprobe.wl > k304b_out.txt *)
mW = 80.37; mZ = 91.19; mt = 172.6; v = 246.22;
g2 = 4 mW^2/v^2; gp2 = 4 (mZ^2 - mW^2)/v^2; yt2 = 2 mt^2/v^2;
cW = g2/4; cZ = (g2 + gp2)/4; ct = yt2/2;
bB[k_] := (4 (2 k)^2 + 6 cW^2 + 3 cZ^2 - 12 ct^2)/(64 Pi^2);
aA[k_] := (4 (2 k)^2 (Log[2 k] - 3/2) + 6 cW^2 (Log[cW] - 5/6) + 3 cZ^2 (Log[cZ] - 5/6) - 12 ct^2 (Log[ct] - 3/2))/(64 Pi^2);
ff[k_] := bB[k] Exp[-2 aA[k]/bB[k]];
finf = Exp[3]/(16 Pi^2);
Print["F_inf = ", N[finf], "  Limes k->Infinity: ", Limit[bB[k] Exp[-2 aA[k]/bB[k]], k -> Infinity] // N];
Print["F/F_inf bei 0.6, 1.2039, 3.1416, 10: ", ff /@ {0.6, 1.2039, 3.1416, 10.}/finf];
kmin = k /. FindRoot[bB[k] == 0, {k, 0.4}];
Print["kmin = ", kmin, "  Nullstellen von F'(k) auf (kmin, 40): ", Quiet[NSolve[D[ff[k], k] == 0 && kmin + 0.001 < k < 40, k, Reals]]];
Print["min F' auf Gitter: ", Min[Table[ff'[k], {k, kmin + 0.002, 40, 0.01}]]];
Print["ohne SM: F = ", Simplify[(4 (2 k)^2/(64 Pi^2)) Exp[-2 (Log[2 k] - 3/2)], k > 0]];
s = NDSolve[{a'[t] == 8 (kk[t]^2 + 12 a[t]^2)/(16 Pi^2), kk'[t] == 16 kk[t] (kk[t] + 3 a[t] + 3 c[t])/(16 Pi^2), c'[t] == 8 (kk[t]^2 + 12 c[t]^2)/(16 Pi^2), a[0] == 0, kk[0] == 1.2039, c[0] == 0}, {a, kk, c}, {t, -5, 3}];
Print["Fluss t=-5,-2,3: ", ({a[#], kk[#], c[#]} /. First[s]) & /@ {-5, -2, 3}];
