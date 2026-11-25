(* k258b (Test H130, Kontrolle iii): Abschluss, Alternativitaet und Normmultiplikativitaet der gefundenen Unteralgebren exakt,
   mit symbolischen Koeffizienten. Konvention des Turms wie k253. *)
cj[x_] := Join[{x[[1]]}, -Rest[x]];
cd[x_, y_] := If[Length[x] == 1, x*y, Module[{h = Length[x]/2, a, b, c, d}, a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]];
    Join[cd[a, c] - cd[cj[d], b], cd[d, a] + cd[b, cj[c]]]]];
id = IdentityMatrix[16]; e[i_] := id[[i + 1]];
tab = Table[cd[id[[i]], id[[j]]], {i, 16}, {j, 16}];
mul[x_, y_] := Sum[x[[i]] y[[j]] tab[[i, j]], {i, 16}, {j, 16}];
basis[u_, a_, b_, c_, d_] := Join[{e[0], u}, Table[a e[k] + b mul[e[7], e[k]] + mul[c e[k] + d mul[e[7], e[k]], e[8]], {k, 1, 6}]];
check[name_, B_] := Module[{prods, closed, xs, ys, x, y, alt, nrm},
  prods = Flatten[Table[mul[B[[p]], B[[q]]], {p, 8}, {q, 8}], 1];
  closed = MatrixRank[Join[B, prods]] == MatrixRank[B] == 8;
  xs = Array[\[FormalA], 8]; ys = Array[\[FormalB], 8]; x = xs . B; y = ys . B;
  alt = Simplify[Expand[mul[mul[x, x], y] - mul[x, mul[x, y]]]];
  nrm = Simplify[Expand[mul[x, y] . mul[x, y] - (x . x) (y . y)]];
  Print[name, ": abgeschlossen ", closed, "; Alternator identisch 0: ", AllTrue[alt, # === 0 &], "; Normdefekt identisch 0: ", nrm === 0,
    "; Alternator-Komponenten ungleich 0: ", Count[alt, Except[0]]]];
check["O_0   (u = e7)", basis[e[7], 1, 0, 0, 0]];
check["O_120 (u = -e7/2 + Sqrt[3] e15/2)", basis[-e[7]/2 + Sqrt[3]/2 e[15], -1/2, 0, Sqrt[3]/2, 0]];
check["O_240 (u = -e7/2 - Sqrt[3] e15/2)", basis[-e[7]/2 - Sqrt[3]/2 e[15], -1/2, 0, -Sqrt[3]/2, 0]];
check["B_+   (u = e8, V = x + (e7 x) e8)", basis[e[8], 1, 0, 0, 1]];
check["B_-   (u = e8, V = x - (e7 x) e8)", basis[e[8], 1, 0, 0, -1]];
