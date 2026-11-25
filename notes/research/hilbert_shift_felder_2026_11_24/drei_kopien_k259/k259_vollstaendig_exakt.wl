(* k259 (Erkundung, nicht blind, 25.11.2026): Vollstaendigkeit der Suche aus H130 exakt.
   Gesucht: alle su(3)_c-stabilen Unteralgebren A = span(1, u) + V der Sedenionen, u = u7 e7 + u8 e8 + u15 e15, |u| = 1.
   V durchlaeuft CP^1 in zwei Karten. Karte 1: V = {x + ((c + d J) x) e8}, J = L_e7, x in span(e1..e6). Karte 2: V = {x e8}.
   Abschluss <=> fuer alle Basisprodukte w: Singulett-Imaginaerteil parallel zu u (Kreuzprodukt 0) und Triplett-Teil senkrecht auf V-senkrecht. *)
cj[x_] := Join[{x[[1]]}, -Rest[x]];
cd[x_, y_] := If[Length[x] == 1, x*y, Module[{h = Length[x]/2, a, b, c, d}, a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]];
    Join[cd[a, c] - cd[cj[d], b], cd[d, a] + cd[b, cj[c]]]]];
id = IdentityMatrix[16]; e[i_] := id[[i + 1]];
tab = Table[cd[id[[i]], id[[j]]], {i, 16}, {j, 16}];
mul[x_, y_] := Sum[x[[i]] y[[j]] tab[[i, j]], {i, 16}, {j, 16}];
jj[x_] := mul[e[7], x]; r8[x_] := mul[x, e[8]];
uu = u7 e[7] + u8 e[8] + u15 e[15];
cross[w_] := Cross[{w[[8]], w[[9]], w[[16]]}, {u7, u8, u15}];
v1 = Table[e[k] + r8[c e[k] + d jj[e[k]]], {k, 6}];
p1 = Table[-(c e[k] - d jj[e[k]]) + r8[e[k]], {k, 6}];
v2 = Table[r8[e[k]], {k, 6}]; p2 = Table[e[k], {k, 6}];
eqs[v_, p_] := Module[{B = Join[{uu}, v], prods},
  prods = Flatten[Table[mul[B[[i]], B[[j]]], {i, 7}, {j, 7}], 1];
  DeleteCases[DeleteDuplicates[Expand[Flatten[Table[Join[cross[w], p . w], {w, prods}]]]], 0]];
e1 = eqs[v1, p1]; e2 = eqs[v2, p2];
Print["Karte 1: ", Length[e1], " Gleichungen; Karte 2: ", Length[e2]];
s1 = Reduce[And @@ Thread[e1 == 0] && u7^2 + u8^2 + u15^2 == 1, {u7, u8, u15, c, d}, Reals];
s2 = Reduce[And @@ Thread[e2 == 0] && u7^2 + u8^2 + u15^2 == 1, {u7, u8, u15}, Reals];
Print["Karte 1: ", InputForm[s1]]; Print["Karte 2: ", s2];
