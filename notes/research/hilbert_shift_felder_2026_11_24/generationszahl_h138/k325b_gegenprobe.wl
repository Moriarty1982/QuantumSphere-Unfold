(* k325b (Test H142, Wolfram exakt): Kern und gestauchte Ladung fuer zwei Viererauswahlen auf HS(5), Orientierung v = a (x) b.
   Konvention wie k253. Ausgabe k325b_out.txt. Indizes 1-basiert (Python-Index + 1). *)
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
run[idx_] := Module[{Bs, Qc, QV, Phi, ker, Qk},
  Bs = basis /@ vv[[idx]];
  Qc = Table[Module[{u = vec[UnitVector[7, 7], vv[[idx[[k]]]]]}, Simplify[Bs[[k]] . (IdentityMatrix[32]/2 - I/6 Lm[u] - I/3 Rm[u]) . Transpose[Bs[[k]]]]], {k, 4}];
  QV = ArrayFlatten[Table[If[i == j, Qc[[i]], 0], {i, 4}, {j, 4}]];
  Phi = Join[Sequence @@ (Transpose /@ Bs), 2];
  ker = Orthogonalize[NullSpace[Phi]];
  Qk = Simplify[ker . QV . Transpose[ker]];
  {Length[ker], Sort[Simplify[Eigenvalues[Qk]]]}];
Print["Auswahl (0,1,5,8) [Indizes 1-basiert 1,2,6,9]: dim Kern, Spektrum: ", run[{1, 2, 6, 9}]];
Print["Kontrolle Sedenion-Tripel + f120(x)f0 (0,1,2,3): ", run[{1, 2, 3, 4}]];
