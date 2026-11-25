(* k327b (Test H144, Wolfram exakt): Sektorgroessen der Rest-Leptonen. Exakter Eigenvektor x mit Phi.x = 0 und QV.x = q x (q = 0, 1);
   N = x.x (alle Koordinaten, bilinear), s = N - Summe der e0-Anteile^2 (nur Imaginaerteil), beide durch |x|^2. Dazu die Einzelkopie.
   Definitionen cj, ml, ee, f, vv, vec, basis, Lm, Rm wie k326b_gegenprobe.wl. Ausgabe k327b_out.txt. *)
sec[idx_] := Module[{m = Length[idx], Bs, Qc, QV, Phi},
  Bs = basis /@ vv[[idx]];
  Qc = Table[Module[{u = vec[UnitVector[7, 7], vv[[idx[[k]]]]]}, Simplify[Bs[[k]] . (IdentityMatrix[32]/2 - I/6 Lm[u] - I/3 Rm[u]) . Transpose[Bs[[k]]]]], {k, m}];
  QV = ArrayFlatten[Table[If[i == j, Qc[[i]], 0], {i, m}, {j, m}]];
  Phi = Join[Sequence @@ (Transpose /@ Bs), 2];
  Table[Module[{ns = NullSpace[Join[Phi, QV - q IdentityMatrix[8 m]]], x, nn},
     x = ns[[1]]; nn = FullSimplify[ComplexExpand[x . Conjugate[x]]];
     {q, Length[ns], FullSimplify[ComplexExpand[x . x]/nn], FullSimplify[ComplexExpand[(x . x - Sum[x[[8 j + 1]]^2, {j, 0, m - 1}])]/nn]}], {q, {0, 1}}]];
Print["H142-Auswahl [1,2,6,9] {q, dim Eigenraum in K, N/|x|^2, s/|x|^2}: ", InputForm[sec[{1, 2, 6, 9}]]];
Print["H143-Auswahl [1,2,4,6,8]: ", InputForm[sec[{1, 2, 4, 6, 8}]]];
Print["Einzelkopie [1]: ", InputForm[Module[{Bs = basis[vv[[1]]], u = vec[UnitVector[7, 7], vv[[1]]], q8, ev},
   q8 = Bs . (IdentityMatrix[32]/2 - I/6 Lm[u] - I/3 Rm[u]) . Transpose[Bs];
   Table[ev = NullSpace[q8 - q IdentityMatrix[8]][[1]]; {q, Simplify[(ev . ev - ev[[1]]^2)/(ev . Conjugate[ev])]}, {q, {0, 1}}]]]];
