(* k283b (Test H128, Kontrolle v): exakte Rechnung der Massenform K fuer n = 3, 4.
   Orthogonalbasis E_a der Spurform mit Normquadraten g_a (1 auf der Diagonale, 2 daneben); alles rational.
   K(W) = Sum_b (1/g_b) ||[L_b, L_W]||^2, Operatornorm in der Spurform. Feldvektoren mit Normquadrat 2 (K ist daher das Doppelte der Python-Werte). *)
cj[x_] := Join[{x[[1]]}, -Rest[x]];
cd[x_, y_] := If[Length[x] == 1, x*y, Module[{h = Length[x]/2, a, b, c, d}, a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]];
    Join[cd[a, c] - cd[cj[d], b], cd[d, a] + cd[b, cj[c]]]]];
pos = {{2, 3}, {3, 1}, {1, 2}};
run[n_] := Module[{d = 2^n, nn, id, T, B, A2, P, J, g, L, kform, tr2, vec, res, rows, x, y, Lx, Ly, z, M},
  nn = 3 + 3 d; id = IdentityMatrix[d];
  T = Table[cd[id[[i]], id[[j]]], {i, d}, {j, d}];
  B = ConstantArray[0, {nn, 3, 3, d}];
  Do[B[[k, k, k, 1]] = 1, {k, 3}];
  Do[B[[3 + (k - 1) d + p, pos[[k, 1]], pos[[k, 2]]]] = id[[p]]; B[[3 + (k - 1) d + p, pos[[k, 2]], pos[[k, 1]]]] = cj[id[[p]]], {k, 3}, {p, d}];
  (* P[a,i,b,j,r] = Sum_{k,p,q} B[a,i,k,p] B[b,k,j,q] T[p,q,r] *)
  A2 = Flatten[Transpose[B . Transpose[T, {2, 1, 3}], {3, 1, 4, 2, 5}], {{1, 2}}]; (* [(k,p), b, j, r] *)
  P = Flatten[B, {{1}, {2}, {3, 4}}] . A2;                                          (* [a, i, b, j, r] *)
  J = Table[Join[Table[P[[a, k, b, k, 1]], {k, 3}], Flatten[Table[P[[a, pos[[k, 1]], b, pos[[k, 2]]]], {k, 3}]]], {a, nn}, {b, nn}];
  J = (J + Transpose[J, {2, 1, 3}])/2;
  g = Join[{1, 1, 1}, ConstantArray[2, 3 d]];
  L = Table[Transpose[J[[a]]], {a, nn}];   (* L[[a]][[c, b]] = (E_a o E_b)_c *)
  kform[w1_, w2_] := Module[{l1 = w1 . L, l2 = w2 . L}, Sum[With[{c1 = L[[b]] . l1 - l1 . L[[b]], c2 = L[[b]] . l2 - l2 . L[[b]]},
       Total[(Transpose[c1*c2] . g)/g]/g[[b]]], {b, nn}]];
  tr2[w_] := Tr[(w . L) . (w . L)];
  vec[i_] := UnitVector[nn, i];
  res = <|"n" -> n, "dim" -> nn,
    "K(S, x1 reell)" -> kform[vec[4], vec[4]], "K(S, diag(1,-1,0))" -> kform[vec[1] - vec[2], vec[1] - vec[2]],
    "K(V, u=e7)" -> kform[vec[3 + 8], vec[3 + 8]], "Mischterm K(S,V)" -> kform[vec[4], vec[3 + 8]], "Tr L^2 (S, V e7)" -> {tr2[vec[4]], tr2[vec[3 + 8]]}|>;
  If[n == 4, res = Join[res, <|"K(V, u=e8)" -> kform[vec[3 + 9], vec[3 + 9]], "K(V, u=e15)" -> kform[vec[3 + 16], vec[3 + 16]],
      "K(V, u=(e1+e10)/sqrt2)" -> kform[vec[3 + 2] + vec[3 + 11], vec[3 + 2] + vec[3 + 11]]/2|>]];
  res];
Print[AbsoluteTiming[run[3]]]; Print[AbsoluteTiming[run[4]]];
