(* k328c (Test H145, Wolfram exakt): iota_k als Algebren-Isomorphismus; Zerlegung K = (D0 (x) e0) + (R (x) Im O) fuer die H142-Auswahl
   [1,2,6,9] (Python 0,1,5,8); Summe c^3 auf der Koeffizientenlinie; Anteil des Produkts (c o c)(x)w im Kern.
   Definitionen cj, ml, ee, f, vv, vec, basis wie k326b_gegenprobe.wl. Ausgabe k328c_out.txt. *)
iota[y_, v_] := y[[1]] ee[[1]] + Sum[y[[i + 1]] vec[UnitVector[7, i], v], {i, 7}];
isoErr = Max[Abs[Flatten[Table[Simplify[ml[iota[UnitVector[8, i], vv[[5]]], iota[UnitVector[8, j], vv[[5]]]] - iota[ml[UnitVector[8, i], UnitVector[8, j]], vv[[5]]]], {i, 8}, {j, 8}]]]];
Print["iota fuer Kopie 5 (f120(x)f120) exakt Algebren-Isomorphismus, max Fehler: ", isoErr];
idx = {1, 2, 6, 9}; m = 4; V = vv[[idx]];
Phi = Join[Sequence @@ (Transpose /@ (basis /@ V)), 2];
K = NullSpace[Phi];
D0 = NullSpace[{ConstantArray[1, m]}]; R = NullSpace[Transpose[V]]; R0 = NullSpace[Append[Transpose[V], ConstantArray[1, m]]];
place[c_, comp_] := Flatten[Table[UnitVector[8, comp + 1] c[[k]], {k, m}]];
Kf = Join[place[#, 0] & /@ D0, Flatten[Table[place[c, i], {c, R}, {i, 7}], 1]];
Print["dim K, dim Formel, Rang der Vereinigung: ", {Length[K], Length[Kf], MatrixRank[Join[K, Kf]]}];
Print["R, R0 (exakt): ", {R, R0}, "; Summe c^3: ", Simplify[Total[R0[[1]]^3]]];
w = Array[ww, 8];
prod = Flatten[Table[R0[[1, k]]^2 w, {k, m}]];
Print["Anteil von (c o c)(x)w in K (exakt, w beliebig): ", Simplify[Orthogonalize[K] . prod]];
