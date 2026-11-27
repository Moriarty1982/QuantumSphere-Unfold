(* k390b (H187): exakte Gegenprobe im reduzierten Modell. Quaternion-Unteralgebra {1, U, n, Un} von O mit komplexen Koeffizienten,
   Vakuum diagonal (l1, l2, l3), Farbstoerung x im Eintrag (1, 2); dritter Eigenwert l3 = l_k. Hesse-Eigenwerte = Frequenzquadrate. *)
qm[a_, b_] := {a[[1]] b[[1]] - a[[2]] b[[2]] - a[[3]] b[[3]] - a[[4]] b[[4]], a[[1]] b[[2]] + a[[2]] b[[1]] + a[[3]] b[[4]] - a[[4]] b[[3]], a[[1]] b[[3]] - a[[2]] b[[4]] + a[[3]] b[[1]] + a[[4]] b[[2]], a[[1]] b[[4]] + a[[2]] b[[3]] - a[[3]] b[[2]] + a[[4]] b[[1]]};
qc[a_] := {a[[1]], -a[[2]], -a[[3]], -a[[4]]}; z4 = {0, 0, 0, 0}; uu = {0, 1, 0, 0}; one = {1, 0, 0, 0};
mm[X_, Y_] := Table[Sum[qm[X[[i, j]], Y[[j, k]]], {j, 3}], {i, 3}, {k, 3}];
jo[X_, Y_] := (mm[X, Y] + mm[Y, X])/2; tr[X_] := Sum[X[[i, i, 1]], {i, 3}];
id3 = Table[If[i == j, one, z4], {i, 3}, {j, 3}];
cr[A_, B_] := jo[A, B] - tr[A] B/2 - tr[B] A/2 + (tr[A] tr[B] - tr[jo[A, B]]) id3/2; sh[A_] := cr[A, A];
pu[X_] := Map[{#[[1]], #[[2]], 0, 0} &, X, {2}];
dq[x_] := -I/6 qm[uu, x] - I/3 qm[x, uu];
dop[X_] := Table[Which[i == j, z4, Mod[j - i, 3] == 1, dq[X[[i, j]]], True, qc[dq[X[[j, i]]]]], {i, 3}, {j, 3}];
x = {0, 0, p + I q, r + I s}; xq = x /. {q -> -q, s -> -s};
W = {{{l1, 0, 0, 0}, eps x, z4}, {eps qc[x], {l2, 0, 0, 0}, z4}, {z4, z4, {l3, 0, 0, 0}}};
Wq = {{{l1, 0, 0, 0}, eps xq, z4}, {eps qc[xq], {l2, 0, 0, 0}, z4}, {z4, z4, {l3, 0, 0, 0}}};
c2[f_] := Simplify[ComplexExpand[Re[Coefficient[Expand[f], eps, 2]]]];
hs[f_] := Module[{c = c2[f]}, Factor[Eigenvalues[D[c, {{p, q, r, s}, 2}]]]];
Print["Adjunkte der Diagonale: ", Table[sh[W /. eps -> 0][[i, i, 1]], {i, 3}]];
Print["a3 Tr (W x Wq) Wu: ", hs[tr[jo[cr[W, Wq], pu[W]]]]];
Print["a4 Tr (W x Wq) (Wu Wuq): ", hs[tr[jo[cr[W, Wq], jo[pu[W], pu[Wq]]]]]];
Print["a5 Tr (W x Wq) Wu#: ", hs[tr[jo[cr[W, Wq], sh[pu[W]]]]]];
Print["a7 Tr (W x Wu) (Wq x Wuq): ", hs[tr[jo[cr[W, pu[W]], cr[Wq, pu[Wq]]]]]];
Print["d1 Tr (Wq x DW) Wu: ", hs[tr[jo[cr[Wq, dop[W]], pu[W]]]]];
Print["d3 Tr (Wq x DW) Wu#: ", hs[tr[jo[cr[Wq, dop[W]], sh[pu[W]]]]]];
Print["d4 Tr (DW x Wu) (Wq x Wuq): ", hs[tr[jo[cr[dop[W], pu[W]], cr[Wq, pu[Wq]]]]]];
