(* k326b (Test H143, Wolfram exakt): Kern, exaktes Spektrum der gestauchten Ladung und dim R0 fuer je eine Fuenferauswahl je Klasse
   aus k326 (transportierte Orientierung v = a (x) b). Konvention wie k325b. Indizes 1-basiert (Python-Index + 1). Ausgabe k326b_out.txt. *)
cj[x_] := Prepend[-Rest[x], First[x]];
ml[x_, y_] := If[Length[x] == 1, x y, Module[{h = Length[x]/2, a, b, c, d},
   a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]];
   Join[ml[a, c] - ml[cj[d], b], ml[d, a] + ml[b, cj[c]]]]];
ee = IdentityMatrix[32];
f = {{1, 0}, {-1/2, Sqrt[3]/2}, {-1/2, -Sqrt[3]/2}};
vv = Table[Flatten[Outer[Times, f[[a]], f[[b]]]], {a, 3}, {b, 3}] // Flatten[#, 1] &;
vec[a_, v_] := Module[{x = ConstantArray[0, 32]}, Do[x[[8 k + 2 ;; 8 k + 8]] = v[[k + 1]] a, {k, 0, 3}]; x];
basis[v_] := Join[{ee[[1]]}, Table[vec[UnitVector[7, i], v], {i, 7}]];
Lm[x_] := Transpose[Table[ml[x, ee[[j]]], {j, 32}]]; Rm[x_] := Transpose[Table[ml[ee[[j]], x], {j, 32}]];
run[idx_] := Module[{m = Length[idx], Bs, Qc, QV, Phi, ker, Qk, r0},
  Bs = basis /@ vv[[idx]];
  Qc = Table[Module[{u = vec[UnitVector[7, 7], vv[[idx[[k]]]]]}, Simplify[Bs[[k]] . (IdentityMatrix[32]/2 - I/6 Lm[u] - I/3 Rm[u]) . Transpose[Bs[[k]]]]], {k, m}];
  QV = ArrayFlatten[Table[If[i == j, Qc[[i]], 0], {i, m}, {j, m}]];
  Phi = Join[Sequence @@ (Transpose /@ Bs), 2];
  ker = Simplify[Orthogonalize[NullSpace[Phi]]];
  Qk = Simplify[ker . QV . ConjugateTranspose[ker]];
  r0 = Length[NullSpace[Append[Transpose[vv[[idx]]], ConstantArray[1, m]]]];
  {Length[ker], r0, Sort[RootReduce[Eigenvalues[Qk]]]}];
