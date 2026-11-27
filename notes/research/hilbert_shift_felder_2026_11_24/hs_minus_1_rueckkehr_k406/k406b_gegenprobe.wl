(* k406b: Gegenprobe mit Wolfram Language (exakt), n = 1..5. Ausgabe in k406b_out.txt.
   n = 6 ueberschreitet mit der rekursiven Multiplikation das Zeitlimit des Kerns (60 s); dafuer k406c (zweite Python-Suche). *)
cj[x_] := Join[{x[[1]]}, -Rest[x]];
mul[x_, y_] := If[Length[x] == 1, x*y, Module[{h = Length[x]/2, a, b, c, d}, a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]]; Join[mul[a, c] - mul[cj[d], b], mul[d, a] + mul[b, cj[c]]]]];
Lm[n_, i_] := Module[{N0 = 2^n, e}, e = IdentityMatrix[N0]; Transpose[Table[mul[e[[i + 1]], e[[k]]], {k, N0}]]];
Rm[n_, i_] := Module[{N0 = 2^n, e}, e = IdentityMatrix[N0]; Transpose[Table[mul[e[[k]], e[[i + 1]]], {k, N0}]]];
Print["k406b: groesste Menge antikommutierender L_(e_i), n = 1..5 (FindClique), dazu Radon-Hurwitz - 1"];
rh[N0_] := Module[{b = IntegerExponent[N0, 2]}, 8 Quotient[b, 4] + 2^Mod[b, 4]];
Do[Module[{N0 = 2^n, Ls, g, cl, w}, Ls = Table[Lm[n, i], {i, 1, N0 - 1}];
  g = Graph[Range[N0 - 1], Flatten[Table[If[Ls[[i]] . Ls[[j]] + Ls[[j]] . Ls[[i]] == ConstantArray[0, {N0, N0}], UndirectedEdge[i, j], Nothing], {i, N0 - 1}, {j, i + 1, N0 - 1}]]];
  cl = If[n == 1, {1}, First[FindClique[g]]]; w = Dot @@ Ls[[cl]];
  Print["n = ", n, ": a = ", Length[cl], ", rho - 1 = ", rh[N0] - 1, ", omega.omega = ", If[w . w == IdentityMatrix[N0], "+1", If[w . w == -IdentityMatrix[N0], "-1", "?"]], ", omega Skalar: ", Which[w == IdentityMatrix[N0], "+1", w == -IdentityMatrix[N0], "-1", True, "nein"], ", Spur omega = ", Tr[w]]], {n, 1, 5}];
Print["HS(3): L1...L7 = -1: ", Dot @@ Table[Lm[3, i], {i, 7}] == -IdentityMatrix[8], "; R1...R7 = +1: ", Dot @@ Table[Rm[3, i], {i, 7}] == IdentityMatrix[8]];
Print["HS(2): L1 L2 L3 = -1: ", Dot @@ Table[Lm[2, i], {i, 3}] == -IdentityMatrix[4], "; R1 R2 R3 = +1: ", Dot @@ Table[Rm[2, i], {i, 3}] == IdentityMatrix[4]];
Print["omega^2 in Cl(0,a) = (-1)^(a(a+1)/2), a = 0..16: ", Table[(-1)^(a (a + 1)/2), {a, 0, 16}]];
Print["a mod 8 fuer a = n + 4, n = 3..20: ", Table[Mod[n + 4, 8], {n, 3, 20}]];
