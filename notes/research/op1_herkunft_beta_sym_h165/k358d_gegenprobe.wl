(* k358d: Gegenprobe zu k358 mit Wolfram Language (Erkundung). Summe endlich bis k = 400. *)
c[k_] := Sqrt[k (k + 2)/3];
gL = g /. FindRoot[Sum[2^(1 - g c[k]), {k, 1, 400}] == 1, {g, 1.9}, WorkingPrecision -> 30];
bx = Sqrt[(gL - 1)/(gL + 1)]; b7 = 5493482/10000000;
G[b_] := (1 + b^2)/(1 - b^2); mZ = 911880/10000;
mW[b_] := mZ G[b]/Sqrt[1 + G[b]^2];
sens[f_] := Simplify[b D[f[b], b]/f[b]];
Print["gammaL = ", N[gL, 13], "  beta = ", N[bx, 13]];
Print["gammaL^5: ", N[G[bx]^5, 10], " gegen ", N[G[b7]^5, 10]];
Print["mW: ", N[mW[bx], 9], " gegen ", N[mW[b7], 9]];
Print["beta^2: ", N[bx^2, 10], " gegen ", N[b7^2, 10]];
Print["symbolisch dln gammaL/dln beta = ", sens[G], " = ", N[sens[G] /. b -> bx, 6]];
Print["symbolisch dln mW/dln beta = ", sens[mW], " = ", N[sens[mW] /. b -> bx, 6]];
Print["dln artanh/dln beta = ", N[(b/((1 - b^2) ArcTanh[b])) /. b -> bx, 6]];
Print["dln Hopfluecke(beta) = ", N[sens[Function[x, 1/(Sqrt[3] x) - 1]] /. b -> bx, 6]];
Print["z mW PDG2026: ", N[(mW[b7] - 80.3625)/Sqrt[0.0077^2 + (mW[b7] 0.0020/mZ)^2], 4], " -> ", N[(mW[bx] - 80.3625)/Sqrt[0.0077^2 + (mW[bx] 0.0020/mZ)^2], 4]];
