(* k297b: Gegenprobe zu k297 in Wolfram Language. Aufruf: wolframscript -file k297b_gegenprobe.wl > k297b_out.txt *)
vars = {x0, x1, x2, x3}; A = x0^2 + x1^2; B = x2^2 + x3^2;
V = eta (B - mu^2 A)^2;
Print["W1 Koeffizienten (A^2, A B, B^2): ", InputForm[Coefficient[Expand[eta (b - mu^2 a)^2], #] & /@ {a^2, a b, b^2}]];
pt = {x0 -> f/Sqrt[1 + mu^2], x1 -> 0, x2 -> mu f/Sqrt[1 + mu^2], x3 -> 0};
Print["W2 V, Gradient, Hesse-Eigenwerte auf der flachen Richtung: ", InputForm[Simplify[{V, D[V, {vars}], Eigenvalues[D[V, {vars, 2}]]} /. pt]]];
Print["W3 Tausch: V(A<->B) - eta mu^4 (B - A/mu^2)^2 = ", Simplify[(V /. {x0 -> x2, x1 -> x3, x2 -> x0, x3 -> x1}) - eta mu^4 (B - A/mu^2)^2]];
mH2 = 8 eta mu^2 phi^2; V1 = mH2^2/(64 Pi^2) (Log[mH2/M^2] - 3/2);
s = First[Solve[D[V1, phi] == 0 && phi > 0, phi, Assumptions -> {eta > 0, mu > 0, M > 0}]];
Print["W4 Minimum phi^2 = ", InputForm[Simplify[phi^2 /. s]], " ; m_s^2/m_H^2 = ", InputForm[Simplify[(D[V1, {phi, 2}]/mH2) /. s]], " ; V1 = ", InputForm[Simplify[V1 /. s]]];
bA = 4 (ka^2 + 20 lA^2); bK = 16 ka (ka + 2 lA + 2 lB); bB = 4 (ka^2 + 20 lB^2);
Print["W5 d rho/dt auf der flachen Flaeche: ", InputForm[Factor[Simplify[((bB lA - bA lB)/lA^2) /. ka -> -2 Sqrt[lA lB] /. lB -> rho lA, Assumptions -> lA > 0 && rho > 0]]],
  " ; d(kappa + 2 Sqrt[lamA lamB])/dt: ", InputForm[Factor[Simplify[(bK + (bA lB + bB lA)/Sqrt[lA lB]) /. ka -> -2 Sqrt[lA lB] /. lB -> rho lA, Assumptions -> lA > 0 && rho > 0]]]];
Print["W6 Zahlen: ", N[{mu, mu^2, mu^-4, 8 mu^2, mu^2/Pi^2, ArcCos[(1 - mu^2)/(1 + mu^2)]/Degree} /. mu -> (1.8644 - 1)/(1.8644 + 1), 4]];
