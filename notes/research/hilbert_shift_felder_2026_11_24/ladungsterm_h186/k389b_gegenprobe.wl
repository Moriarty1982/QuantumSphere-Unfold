(* k389b (H186): exakte Gegenprobe im reduzierten Modell. Quaternion-Unteralgebra {1, U, n, Un} von O mit komplexen Koeffizienten (C (x) H),
   Vakuum diagonal (l1, l2, l3), Farbstoerung x im Eintrag (1, 2). Hesse-Eigenwerte = Frequenzquadrate (+: eine Ladung, -: die andere). *)
qm[a_, b_] := {a[[1]] b[[1]] - a[[2]] b[[2]] - a[[3]] b[[3]] - a[[4]] b[[4]], a[[1]] b[[2]] + a[[2]] b[[1]] + a[[3]] b[[4]] - a[[4]] b[[3]], a[[1]] b[[3]] - a[[2]] b[[4]] + a[[3]] b[[1]] + a[[4]] b[[2]], a[[1]] b[[4]] + a[[2]] b[[3]] - a[[3]] b[[2]] + a[[4]] b[[1]]};
qc[a_] := {a[[1]], -a[[2]], -a[[3]], -a[[4]]}; z4 = {0, 0, 0, 0}; uu = {0, 1, 0, 0};
mm[X_, Y_] := Table[Sum[qm[X[[i, j]], Y[[j, k]]], {j, 3}], {i, 3}, {k, 3}];
jo[X_, Y_] := (mm[X, Y] + mm[Y, X])/2; tr[X_] := Sum[X[[i, i, 1]], {i, 3}];
pu[X_] := Map[{#[[1]], #[[2]], 0, 0} &, X, {2}];
dq[x_] := -I/6 qm[uu, x] - I/3 qm[x, uu];
dop[X_] := Table[Which[i == j, z4, Mod[j - i, 3] == 1, dq[X[[i, j]]], True, qc[dq[X[[j, i]]]]], {i, 3}, {j, 3}];
x = {0, 0, p + I q, r + I s};
W = {{{l1, 0, 0, 0}, eps x, z4}, {eps qc[x], {l2, 0, 0, 0}, z4}, {z4, z4, {l3, 0, 0, 0}}};
Wq = {{{l1, 0, 0, 0}, eps (x /. {q -> -q, s -> -s}), z4}, {eps qc[x /. {q -> -q, s -> -s}], {l2, 0, 0, 0}, z4}, {z4, z4, {l3, 0, 0, 0}}};
c2[f_] := Simplify[ComplexExpand[Re[Coefficient[Expand[f], eps, 2]]]];
hs[f_] := Module[{c = c2[f]}, Eigenvalues[D[c, {{p, q, r, s}, 2}]] // Simplify];
Print["c1 Tr Wq DW: Hesse-Eigenwerte ", hs[tr[jo[Wq, dop[W]]]]];
Print["c2 Tr (Wq DW) Wu: ", hs[tr[jo[jo[Wq, dop[W]], pu[W]]]]];
Print["c4 Tr (Wq DW) o (Wu Wuq): ", hs[tr[jo[jo[Wq, dop[W]], jo[pu[W], pu[Wq]]]]]];
Print["c7 Tr (Wq Wu) o (DW Wuq): ", hs[tr[jo[jo[Wq, pu[W]], jo[dop[W], pu[Wq]]]]]];
Print["c11 Tr (Wq DW) o (W Wq): ", hs[tr[jo[jo[Wq, dop[W]], jo[W, Wq]]]]];
Print["Referenz Tr (W Wq) Wu: ", hs[tr[jo[jo[W, Wq], pu[W]]]]];
