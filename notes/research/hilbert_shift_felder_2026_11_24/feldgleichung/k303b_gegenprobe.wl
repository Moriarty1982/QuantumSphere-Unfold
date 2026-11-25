(* k303b: Gegenprobe zu k303 in Wolfram Language. Aufruf: wolframscript -file k303b_gegenprobe.wl > k303b_out.txt *)
mW = 80.37; mZ = 91.19; mt = 172.6; mh = 125.2; v = 246.22; M = 4;
sm = 6 mW^4 + 3 mZ^4 - 12 mt^4;
mhOf[k_] := Module[{s = M (2 k v^2)^2 + sm}, Sign[s] Sqrt[Abs[s]/(8 Pi^2 v^2)]];
ks = k /. First[Solve[M (2 k v^2)^2 + sm == mh^2 8 Pi^2 v^2 && k > 0, k]];
Print["kappa* = ", ks, "  m_S = ", Sqrt[2 ks] v];
Print["kmin = ", Sqrt[-sm/M]/(2 v^2)];
v1 = (12 mt^2 - 6 mW^2 - 3 mZ^2)/M/(2 v^2); v2 = (12 mt^2 - 6 mW^2 - 3 mZ^2 - 3 mh^2)/M/(2 v^2);
v3 = k /. FindRoot[3 (M (2 k v^2)^2 + sm)/(8 Pi^2 v^2) + 6 mW^2 + 3 mZ^2 + M 2 k v^2 - 12 mt^2 == 0, {k, 0.6}];
Print["Veltman V1, V2, V3: ", {v1, v2, v3}, "  m_h: ", mhOf /@ {v1, v2, v3}];
Print["Unitaritaet: ", N[Pi], " m_h = ", mhOf[N[Pi]]];
mu = 0.3018; k1 = (1 + mu^2)/(1 - mu^2); gL = (1 + mu)/(1 - mu);
Print["1/cos2theta = ", k1, " = (gL+1/gL)/2 = ", (gL + 1/gL)/2, "  Abweichung ", 100 (k1/ks - 1), " %  m_h = ", mhOf[k1]];
Print["symbolisch (gL+1/gL)/2 - (1+m^2)/(1-m^2) mit gL=(1+m)/(1-m): ", Simplify[((1 + m)/(1 - m) + (1 - m)/(1 + m))/2 - (1 + m^2)/(1 - m^2)]];
g2 = 4 mW^2/v^2; gp2 = 4 (mZ^2 - mW^2)/v^2; yt2 = 2 mt^2/v^2;
Print["16 kappa*^2 - (8 Pi^2 mh^2/v^2 - 3/8 g2^2 - 3/16 (g2+gp2)^2 + 3 yt2^2) = ", 16 ks^2 - (8 Pi^2 mh^2/v^2 - 3/8 g2^2 - 3/16 (g2 + gp2)^2 + 3 yt2^2)];
Print["beta(l3) geeicht, Nullstellen: ", Solve[4 l^2 + l (6 yt2 - 3 (3 g2 + gp2)) + 3/4 (3 g2^2 + gp2^2 - 2 g2 gp2) == 0, l, Reals]];
