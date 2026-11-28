(* k452b: unabhaengige Wolfram-Gegenprobe zu k452. Cayley-Dickson-Produkt mit Vorzeichenfolge gs, symbolische Normprobe fuer HS(2), HS(3). *)
cj[x_] := Prepend[-Rest[x], First[x]];
mul[x_, y_, gs_] := If[Length[x] == 1, x y,
  Module[{h = Length[x]/2, a, b, c, d, g = Last[gs], in = Most[gs]},
   {a, b, c, d} = {x[[;; h]], x[[h + 1 ;;]], y[[;; h]], y[[h + 1 ;;]]};
   Join[mul[a, c, in] + g mul[cj[d], b, in], mul[d, a, in] + mul[b, cj[c], in]]]];
nrm[x_, gs_] := First[mul[x, cj[x], gs]];
e[n_, i_] := UnitVector[n, i + 1];
av = Array[A, 4]; bv = Array[B, 4];
r2 = Expand[nrm[mul[av, bv, {-1, -1}], {-1, -1}] - nrm[av, {-1, -1}] nrm[bv, {-1, -1}]];
a8 = Array[P, 8]; b8 = Array[Q, 8];
r3 = Expand[nrm[mul[a8, b8, {-1, -1, -1}], {-1, -1, -1}] - nrm[a8, {-1, -1, -1}] nrm[b8, {-1, -1, -1}]];
sig2 = Table[nrm[e[4, i], gs], {gs, Tuples[{-1, 1}, 2]}, {i, 0, 3}];
x = e[16, 1] + e[16, 10]; y = e[16, 4] - e[16, 15]; g4 = {-1, -1, -1, -1};
Print["HS(2) N(ab)-N(a)N(b) symbolisch: ", r2];
Print["HS(3) N(ab)-N(a)N(b) symbolisch: ", r3];
Print["Normform-Diagonale HS(2) fuer g-Folgen ", Tuples[{-1, 1}, 2], ": ", sig2];
Print["HS(2) e1e2, e2e1: ", mul[e[4, 1], e[4, 2], {-1, -1}], " ", mul[e[4, 2], e[4, 1], {-1, -1}]];
Print["HS(3) (e1e2)e4, e1(e2e4): ", mul[mul[e[8, 1], e[8, 2], {-1, -1, -1}], e[8, 4], {-1, -1, -1}], " ", mul[e[8, 1], mul[e[8, 2], e[8, 4], {-1, -1, -1}], {-1, -1, -1}]];
Print["HS(4) (e1+e10)(e4-e15) = ", mul[x, y, g4], "  N(x), N(y) = ", nrm[x, g4], ", ", nrm[y, g4]];
(* Teil 2 (zweiter Aufruf): Clifford-Bedingung der Linksmultiplikationen (Feldgleichung erster Ordnung) und Radon-Hurwitz *)
anti[n_] := Module[{N0 = 2^n, gs = ConstantArray[-1, n], L},
   L = Table[Transpose[Table[mul[UnitVector[N0, i + 1], UnitVector[N0, k + 1], gs], {k, 0, N0 - 1}]], {i, 1, N0 - 1}];
   Max[Flatten@Table[Abs[L[[a]].L[[b]] + L[[b]].L[[a]] + 2 KroneckerDelta[a, b] IdentityMatrix[N0]], {a, N0 - 1}, {b, N0 - 1}]]];
rho[m_] := Module[{k = IntegerExponent[m, 2], a, b}, {a, b} = QuotientRemainder[k, 4]; 8 a + 2^b];
Print["max |L_i L_j + L_j L_i + 2 delta|: HS(1..4) = ", Table[anti[n], {n, 1, 4}]];
Print["rho(N)-1 fuer N = 1,2,4,...,64: ", Table[rho[2^n] - 1, {n, 0, 6}], "  noetig N-1: ", Table[2^n - 1, {n, 0, 6}]];
