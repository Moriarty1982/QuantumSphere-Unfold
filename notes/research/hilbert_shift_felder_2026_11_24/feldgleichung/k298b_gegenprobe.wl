(* k298b: Gegenprobe zu k298 (Test H132) in Wolfram Language, Quaternionen als 2x2-Matrizen, Norm = Determinante.
   Aufruf: wolframscript -file k298b_gegenprobe.wl > k298b_out.txt *)
e = {IdentityMatrix[2], {{I, 0}, {0, -I}}, {{0, 1}, {-1, 0}}, {{0, I}, {I, 0}}};
q[v_] := v . e; nrm[M_] := ComplexExpand[Det[M]];
psi0 = q[{f Cos[th], 0, f Sin[th], 0}]; qi = e[[2]];
D1 = gL L qi . psi0 - gR R psi0 . qi;
M2 = Simplify[Expand[nrm[D1]/2]];
Mm = Simplify[D[M2, {{L, R}, 2}]];
Print["Y1 Massenmatrix (L, R): ", InputForm[Mm], " ; Det - 4 gL^2 gR^2 A B: ", Simplify[Det[Mm] - 4 gL^2 gR^2 f^4 Cos[th]^2 Sin[th]^2]];
evs = Simplify[Eigenvalues[Mm /. gR -> gL] /. th -> ArcTan[mu], Assumptions -> 0 < mu < 1 && f > 0 && gL > 0];
Print["Y2 gL = gR, tan th = mu: Eigenwerte ", InputForm[evs], " ; Verhaeltnis ", InputForm[Simplify[Min[evs]/Max[evs], Assumptions -> 0 < mu < 1]]];
Print["Y3 kleines mu: ", InputForm[Simplify[Series[(gL^2 + gR^2 - Sqrt[(gL^2 + gR^2)^2 - 4 gL^2 gR^2 (1 - ((1 - mu^2)/(1 + mu^2))^2)]) f^2/2, {mu, 0, 3}], Assumptions -> gL > 0 && gR > 0]]];
Print["Y4 Verhaeltnis haengt an gR/gL (gR = 2 gL, cos 2th = 1/2): ", N[Min[#]/Max[#] &[Eigenvalues[Mm /. {gR -> 2 gL, th -> Pi/6}]]], " gegen gL = gR: ", N[Min[#]/Max[#] &[Eigenvalues[Mm /. {gR -> gL, th -> Pi/6}]]]];
Wq = g/2 (W1 e[[2]] + W2 e[[3]] + W3 e[[4]]); Bq = gp/2 Bf e[[2]];
D2 = Wq . psi0 - psi0 . Bq;
M4 = Simplify[D[Expand[nrm[D2]/2], {{W1, W2, W3, Bf}, 2}]];
Print["Y5 SU(2) x U(1): Eigenwerte ", InputForm[Simplify[Eigenvalues[M4]]]];
x = {x0, x1, x2, x3}; V = eta ((x2^2 + x3^2) - mu^2 (x0^2 + x1^2))^2;
lmul[v_, w_] := Module[{m = q[v] . q[w]}, {Re[m[[1, 1]]], Im[m[[1, 1]]], Re[m[[1, 2]]], Im[m[[1, 2]]]}];
Print["Y6 Aenderung von V unter Linksdrehung um j: ", InputForm[Factor[Simplify[D[V, {x}] . ComplexExpand[lmul[{0, 0, 1, 0}, x]], Element[x, Reals]]]]];
Print["Y7 Zahlen mu = (1.8644-1)/(2.8644): ", N[With[{m = (1.8644 - 1)/(1.8644 + 1)}, {m, 2/(1 + m^2), 2 m^2/(1 + m^2), Sqrt[m^2]}], 4]];
