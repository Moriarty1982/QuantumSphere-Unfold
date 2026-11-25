(* k321b (Test H138, Wolfram-Gegenprobe): exakte Abschlussbedingung fuer O_v = span{1} + Im(O) (x) v in A_n, n = 4, 5.
   Konvention wie k253: (a,b)(c,d) = (ac - conj(d) b, d a + b conj(c)). Ausgabe: k321b_out.txt.
   n = 6 lief im MCP-Kernel nicht innerhalb von 60 s (Groebner/Solve in 8 Variablen); dort nur Python k321. *)
cj[x_] := Prepend[-Rest[x], First[x]];
ml[x_, y_] := If[Length[x] == 1, x y, Module[{h = Length[x]/2, a, b, c, d},
   a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]];
   Join[ml[a, c] - ml[cj[d], b], ml[d, a] + ml[b, cj[c]]]]];
(* Bedingungen: Singulett-Anteile e_{8k}, k >= 1, verschwinden; Blockanteile W (7 x m) sind parallel zu v (2x2-Minoren) *)
eqs[n_] := Module[{nn = 2^n, m = 2^(n - 3), v, emb, all = {}, z, w},
  v = Array[Subscript[t, #] &, m];
  emb[i_] := Module[{x = ConstantArray[0, nn]}, Do[x[[8 k + i + 1]] = v[[k + 1]], {k, 0, m - 1}]; x];
  Do[z = Expand[ml[emb[i], emb[j]]];
     all = Join[all, Table[z[[8 k + 1]], {k, 1, m - 1}]];
     w = Table[z[[8 k + l + 1]], {l, 1, 7}, {k, 0, m - 1}];
     all = Join[all, Flatten[Table[w[[l, k]] v[[q]] - w[[l, q]] v[[k]], {l, 7}, {k, m}, {q, k + 1, m}]]],
   {i, 1, 7}, {j, 1, 7}];
  {v, DeleteCases[Union[Expand[all]], 0]}];
{v4, e4} = eqs[4];
Print["n=4 Gleichungen: ", Factor[e4]];
Print["n=4 Loesungen: ", Reduce[Join[Thread[e4 == 0], {v4 . v4 == 1}], v4, Reals]];
{v5, e5} = eqs[5];
s5 = v5 /. Solve[Join[Thread[e5 == 0], {v5 . v5 == 1}], v5, Reals];
reps = DeleteDuplicates[s5, (#1 == -#2 || #1 == #2) &];
Print["N_5 = ", Length[reps]];
Print[InputForm[reps]];
g = Abs[Outer[Dot, reps, reps, 1]] // Simplify;
gr = SimpleGraph[AdjacencyGraph[Boole[Map[# == 0 &, g, {2}]]]];
Print["o_5 = ", Length[First[FindClique[gr]]], "; 4er-Cliquen: ", Length[FindClique[gr, {4}, All]], "; Rang v: ", MatrixRank[reps]];
emb5[v_, i_] := Module[{x = ConstantArray[0, 32]}, Do[x[[8 k + i + 1]] = v[[k + 1]], {k, 0, 3}]; x];
alt[v_] := Module[{b = Table[emb5[v, i], {i, 1, 7}]},
  Max[Abs[Flatten[Table[Simplify[ml[ml[b[[i]], b[[i]]], b[[j]]] - ml[b[[i]], ml[b[[i]], b[[j]]]]], {i, 7}, {j, 7}]]]]];
a = alt /@ reps;
Print["exakter Alternator je Kopie: ", a];
okt = Flatten[Position[a, 0]];
Print["oktonionisch: ", Length[okt], "; Rang: ", MatrixRank[reps[[okt]]], "; |v.w|: ",
  Union[Flatten[Table[Abs[reps[[okt[[i]]]] . reps[[okt[[j]]]]], {i, Length[okt]}, {j, i + 1, Length[okt]}]]]];
