(* k254b (Erkundung, nicht blind): endlicher Teil von Aut(S). Gesucht alle Automorphismen der Sedenionen, die mit der
   diagonalen G2-Wirkung vertauschen: 1 -> 1, e8 -> lam e8, (Im a, Im b) -> M (Im a, Im b) mit 2x2-Matrix M.
   Ausgefuehrt ueber den Wolfram-MCP-Kern am 24.11.2026; Ausgabe in k254b_out.txt *)
cd[x_List, y_List] := If[Length[x] == 1, x y, Module[{h = Length[x]/2, a1, b1, c1, d1, cj},
   cj[v_] := Prepend[-Rest[v], First[v]];
   a1 = x[[;; h]]; b1 = x[[h + 1 ;;]]; c1 = y[[;; h]]; d1 = y[[h + 1 ;;]];
   Join[cd[a1, c1] - cd[cj[d1], b1], cd[d1, a1] + cd[b1, cj[c1]]]]];
e = IdentityMatrix[16];
f[v_] := Module[{a = v[[;; 8]], b = v[[9 ;;]], r = ConstantArray[0, 16]},
  r[[1]] = a[[1]]; r[[9]] = lam b[[1]];
  r[[2 ;; 8]] = m11 a[[2 ;; 8]] + m12 b[[2 ;; 8]];
  r[[10 ;; 16]] = m21 a[[2 ;; 8]] + m22 b[[2 ;; 8]]; r];
eqs = DeleteDuplicates[DeleteCases[Flatten[Table[Expand[f[cd[e[[i]], e[[j]]]] - cd[f[e[[i]]], f[e[[j]]]]], {i, 16}, {j, 16}]], 0]];
sol = Solve[(And @@ Thread[eqs == 0]) && m11 m22 - m12 m21 != 0, {lam, m11, m12, m21, m22}, Reals];
mats = {{m11, m12}, {m21, m22}} /. sol;
Print["Anzahl G2-vertraeglicher Automorphismen von S: ", Length[sol]];
Do[Print["  lam = ", lam /. s, ", M = ", {{m11, m12}, {m21, m22}} /. s, ", Ordnung ", Min[Select[Range[6], MatrixPower[{{m11, m12}, {m21, m22}} /. s, #] == IdentityMatrix[2] &]], ", det M = ", Det[{{m11, m12}, {m21, m22}} /. s]], {s, sol}];
Print["abgeschlossen: ", SubsetQ[mats, Flatten[Table[a . b, {a, mats}, {b, mats}], 1]], "; kommutativ: ", AllTrue[Tuples[mats, 2], #[[1]] . #[[2]] == #[[2]] . #[[1]] &], "; Charakter Spur: ", Tr /@ mats];
