(* k299b: Gegenprobe zu k299 in Wolfram Language, Quaternionen als 2x2-Matrizen.
   Aufruf: wolframscript -file k299b_gegenprobe.wl > k299b_out.txt *)
e = {IdentityMatrix[2], {{I, 0}, {0, -I}}, {{0, 1}, {-1, 0}}, {{0, I}, {I, 0}}};
q[v_] := v . e; cj[M_] := ConjugateTranspose[M];
comp[M_] := ComplexExpand[{Re[M[[1, 1]]], Im[M[[1, 1]]], Re[M[[1, 2]]], Im[M[[1, 2]]]}];
psi = q[{a Cos[w t], a Sin[w t], b Cos[w t], b Sin[w t]}];
Jt = Simplify[comp[ComplexExpand[cj[psi]] . D[psi, t]], Element[{a, b, w, t}, Reals]];
Print["Z1 J_t auf der Loesung: ", InputForm[Jt]];
psi0 = q[{f Cos[th], 0, f Sin[th], 0}];
Wq = g/2 (W1 e[[2]] + W2 e[[3]] + W3 e[[4]]); Bq = gp/2 Bf e[[2]];
Dv = Wq . psi0 - psi0 . Bq;
J0 = Simplify[comp[ComplexExpand[cj[psi0]] . Dv], Element[{f, th, g, gp, W1, W2, W3, Bf}, Reals]];
Lm = Simplify[ComplexExpand[Det[Dv]]/2 + xi J0[[2]]^2/(2 f^2)];
M4 = Simplify[D[Lm, {{W1, W2, W3, Bf}, 2}]];
Print["Z2 Fassung S, Massenquadrate: ", InputForm[Factor[Simplify[Eigenvalues[M4]]]], " ; Nullvektor: ", InputForm[Simplify[NullSpace[M4]]]];
x = {x0, x1, x2, x3}; v = {v0, v1, v2, v3};
J = Simplify[comp[ComplexExpand[cj[q[x]]] . q[v]], Element[Join[x, v], Reals]];
P = (J[[3]]^2 + J[[4]]^2 - tau^2 J[[2]]^2)^2/(x . x)^2;
lrot[u_, y_] := Simplify[comp[q[u] . q[y]], Element[Join[x, v], Reals]];
dP[u_] := Simplify[D[P, {x}] . lrot[u, x] + D[P, {v}] . lrot[u, v]];
Print["Z3 Fassung F, Aenderung von P unter Linksdrehung um i, j, k: ", {dP[{0, 1, 0, 0}], dP[{0, 0, 1, 0}], dP[{0, 0, 0, 1}]}];
Pv = Expand[(J0[[3]]^2 + J0[[4]]^2 - tau^2 J0[[2]]^2)^2];
Print["Z4 P im Vakuum: zweite Ableitungen bei null: ", Union[Flatten[D[Pv, {{W1, W2, W3, Bf}, 2}] /. {W1 -> 0, W2 -> 0, W3 -> 0, Bf -> 0}]]];
Print["Z5 Zahlen: ", N[With[{k = 1.8644}, {1/k^2, 1/k, k, k^2}], 4], " ; m_s (GeV): ", Sqrt[3 (2 0.652^4 + (0.652^2 + 0.357^2)^2)/(128 Pi^2)] 246.]
