(* k380b: unabhaengige Kontrolle von J^2 auf O und S (eigene Cayley-Dickson-Multiplikation) *)
cj[x_] := Prepend[-Rest[x], First[x]];
mul[x_, y_] := If[Length[x] == 1, x y, Module[{h = Length[x]/2, a, b, c, d}, a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]]; Join[mul[a, c] - mul[cj[d], b], mul[d, a] + mul[b, cj[c]]]]];
res = Table[Module[{e = IdentityMatrix[n], J, J2}, J = Transpose[Table[mul[e[[8]], cj[e[[i]]]], {i, n}]]; J2 = J . J; {Diagonal[J2], J2 === DiagonalMatrix[Diagonal[J2]], Transpose[J] . J === IdentityMatrix[n]}], {n, {8, 16}}];
Print[res]
