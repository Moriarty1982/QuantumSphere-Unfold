(* k290b (Erkundung, nicht blind): unabhaengige exakte Gegenprobe zu k290 in Wolfram Language.
   Cayley-Dickson mit freien Vorzeichen g: (a,b)(c,d) = (ac + g d* b, d a + b c*). *)
cj[x_] := Join[{x[[1]]}, -Rest[x]];
mul[x_, y_, g_] := If[Length[x] == 1, {x[[1]] y[[1]]},
   Module[{h = Length[x]/2, a, b, c, d, gi = Most[g], gg = Last[g]},
    a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]];
    Join[mul[a, c, gi] + gg mul[cj[d], b, gi], mul[d, a, gi] + mul[b, cj[c], gi]]]];
nrm[x_, g_] := mul[x, cj[x], g][[1]];
inn[x_, y_, g_] := mul[cj[x], y, g][[1]];
com[x_, y_, g_] := mul[x, y, g] - mul[y, x, g];
ass[x_, y_, z_, g_] := mul[mul[x, y, g], z, g] - mul[x, mul[y, z, g], g];
k1[x_, y_, g_] := nrm[x, g] nrm[y, g] - inn[x, y, g]^2;
k2[x_, y_, g_] := nrm[com[x, y, g], g];
k3[x_, y_, z_, g_] := nrm[ass[x, y, z, g], g];
k4[x_, y_, g_] := nrm[mul[x, y, g], g] - nrm[x, g] nrm[y, g];
sy[s_, n_] := Array[Symbol[s <> ToString[#]] &, n, 0];
gs = {g0, g1, g2, g3};
sg[v_] := Join[v[[;; Length[v]/2]], -v[[Length[v]/2 + 1 ;;]]];
e[i_, n_] := UnitVector[n, i + 1];

Print["W1 Normrekursion (Rest, n=1,2,3): ",
  Table[With[{x = sy["x", 2^n], g = gs[[;; n]]},
    Expand[nrm[x, g] - nrm[x[[;; 2^(n - 1)]], Most[g]] + Last[g] nrm[x[[2^(n - 1) + 1 ;;]], Most[g]]]], {n, 3}]];
Print["W2 sigma Automorphismus (n=1,2,3): ",
  Table[With[{x = sy["x", 2^n], y = sy["y", 2^n], g = gs[[;; n]]},
    Union[Expand[sg[mul[x, y, g]] - mul[sg[x], sg[y], g]]]], {n, 3}]];
Print["W3 u(ux) + N(u) x fuer imaginaeres u (n=1,2,3): ",
  Table[With[{x = sy["x", 2^n], u = ReplacePart[sy["u", 2^n], 1 -> 0], g = gs[[;; n]]},
    Union[Expand[mul[u, mul[u, x, g], g] + nrm[u, g] x]]], {n, 3}]];
Print["W3 n=4, rationales Beispiel wie k290: ",
  With[{g = {-1, -1, -1, -1}, u = Join[{0}, {1, -2, 3, 1, 2, -1, 1, 3, -2, 1, 1, 2, -3, 1, 2}/7],
    x = {1, 2, -1, 3, 1, -2, 2, 1, -1, 3, 2, 1, -2, 1, 3, -1}/5},
   nrm[mul[u, mul[u, x, g], g] + nrm[u, g] x, g]/(nrm[u, g]^2 nrm[x, g])]];
Print["W4 K1 auf R: ", Expand[k1[{x0}, {y0}, {}]], " | auf C: ", Factor[k1[sy["x", 2], sy["y", 2], {g0}]]];
Print["W4 K2 auf C: ", Expand[k2[sy["x", 2], sy["y", 2], {g0}]], " | K2(e1,e2) auf H: ", k2[e[1, 4], e[2, 4], {g0, g1}]];
Print["W4 Assoziator auf H: ", Union[Expand[ass[sy["x", 4], sy["y", 4], sy["z", 4], {g0, g1}]]],
  " | K3(e1,e2,e4) auf O: ", k3[e[1, 8], e[2, 8], e[4, 8], {g0, g1, g2}]];
Print["W4 K4 auf O: ", Expand[k4[sy["x", 8], sy["y", 8], {g0, g1, g2}]],
  " | Sedenionen (e1+e10)(e4-e15) = ", Union[mul[e[1, 16] + e[10, 16], e[4, 16] - e[15, 16], {-1, -1, -1, -1}]],
  ", K4 = ", k4[e[1, 16] + e[10, 16], e[4, 16] - e[15, 16], {-1, -1, -1, -1}]];

(* Symmetrie-Algebra in so(N): exakter Rang an rationalen Zufallspunkten, n = 1,2,3 *)
SeedRandom[290];
soBasis[nn_] := Flatten[Table[SparseArray[{{i, j} -> 1, {j, i} -> -1}, {nn, nn}], {i, nn}, {j, i + 1, nn}], 1];
grad[f_, xs_] := Table[Coefficient[f @@ ReplacePart[xs, {i, k} -> xs[[i, k]] + eps], eps, 1], {i, Length[xs]}, {k, Length[xs[[1]]]}];
symDim[n_, terms_, fix_ : None] := Module[{nn = 2^n, g = ConstantArray[-1, n], bas, rows = {}, xs, gr},
   bas = soBasis[nn];
   Do[Do[xs = RandomInteger[{-4, 4}, {t[[1]], nn}]; gr = grad[t[[2]][##, g] &, xs];
      AppendTo[rows, Table[Sum[gr[[i]] . (X . xs[[i]]), {i, t[[1]]}], {X, bas}]], {Length[bas] + 5}], {t, terms}];
   If[fix =!= None, Do[AppendTo[rows, Table[(X . fix)[[r]], {X, bas}]], {r, nn}]];
   Length[bas] - MatrixRank[rows]];
tN = {1, nrm}; tRe = {1, #1[[1]] &}; t1 = {2, k1}; t2 = {2, k2}; t3 = {3, k3};
Print["W5 dim Symmetrie-Algebra, Terme {N,K1}:        n=1,2,3: ", Table[symDim[n, {tN, t1}], {n, 3}]];
Print["W5 dim Symmetrie-Algebra, Terme {N,K1,K2}:     n=1,2,3: ", Table[symDim[n, {tN, t1, t2}], {n, 3}]];
Print["W5 dim Symmetrie-Algebra, Terme {N,K1,K2,K3}:  n=1,2,3: ", Table[symDim[n, {tN, t1, t2, t3}], {n, 3}]];
Print["W5 dazu Re(psi):                               n=1,2,3: ", Table[symDim[n, {tN, t1, t2, t3, tRe}], {n, 3}]];
Print["W5 dazu feste Einheit u = l:                   n=1,2,3: ", Table[symDim[n, {tN, t1, t2, t3, tRe}, e[2^(n - 1), 2^n]], {n, 3}]];

(* Bewegungsregel erster Ordnung fuer H, u = l *)
With[{g = {-1, -1}, u = e[2, 4], p = Table[Symbol["p" <> ToString[i]][t], {i, 0, 3}]},
  Module[{dp = D[p, t], L, el},
   L = 1/2 inn[dp, mul[u, p, g], g] - w/2 nrm[p, g];
   el = Table[D[L, p[[i]]] - D[D[L, dp[[i]]], t], {i, 4}];
   Print["W6 Euler-Lagrange von L1 auf H, aufgeloest: psi' - w u psi = ",
    Simplify[(dp /. First[Solve[el == 0, dp]]) - w mul[u, p, g]]]]];
(* sigma-Identitaet aus k282; W hermitesch, also Conjugate[W] = Transpose[W] *)
With[{W = {{d1, s3 + I v3, s2 - I v2}, {s3 - I v3, d2, s1 + I v1}, {s2 + I v2, s1 - I v1, d3}}},
  Print["W7 Tr(W.Conjugate[W]) - (Tr W^2 - 4|v|^2) = ", Expand[Tr[W . Transpose[W]] - Tr[W . W] + 4 (v1^2 + v2^2 + v3^2)]]];
