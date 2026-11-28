(* k453b: unabhaengige Wolfram-Gegenprobe zu H237 (drei Aufrufe wegen 60-s-Grenze des Kerns). *)
cj[x_] := Prepend[-Rest[x], First[x]];
mul[x_, y_] := If[Length[x] == 1, x y, Module[{h = Length[x]/2, a, b, c, d}, {a, b, c, d} = {x[[;; h]], x[[h + 1 ;;]], y[[;; h]], y[[h + 1 ;;]]}; Join[mul[a, c] - mul[cj[d], b], mul[d, a] + mul[b, cj[c]]]]];
n = 16; ee = IdentityMatrix[n];
LB = Table[Transpose[Table[mul[ee[[i]], ee[[k]]], {k, n}]], {i, n}];
(* Aufruf 1: Kopien und ein Winkel ohne Unteralgebra *)
waveW[U_] := Module[{Ls = (#.LB) & /@ U, Ks}, Ks = Flatten[Table[Ls[[a]].Ls[[b]] + Ls[[b]].Ls[[a]] + 2 KroneckerDelta[a, b] IdentityMatrix[n], {a, Length[U]}, {b, a, Length[U]}], 1];
   {Max[Abs[N[Flatten[Ks]]]], Length[NullSpace[N[Join @@ Ks], Tolerance -> 10^-9]]}];
copy[v0_, v1_] := Table[v0 ee[[i + 1]] + v1 ee[[i + 9]], {i, 1, 7}];
Print["V1: ", waveW[copy[1, 0]], "  V2: ", waveW[copy[-1/2, Sqrt[3]/2]], "  V3: ", waveW[copy[-1/2, -Sqrt[3]/2]], "  theta=Pi/7: ", waveW[copy[Cos[Pi/7], Sin[Pi/7]]]];
(* Aufruf 2 und 3: ganz Im S und die 15 Basis-Unteralgebren der Dimension 8 (exakt) *)
K[a_, b_] := LB[[a + 1]].LB[[b + 1]] + LB[[b + 1]].LB[[a + 1]] + 2 KroneckerDelta[a, b] IdentityMatrix[n];
Wdim[s_] := Length[NullSpace[Join @@ Flatten[Table[K[a, b], {a, s}, {b, s}], 1]]];
Print["ganz Im S: dim W = ", Wdim[Range[15]], ", W = ", NullSpace[Join @@ Flatten[Table[K[a, b], {a, 15}, {b, 15}], 1]]];
grp[g_] := Union[Table[BitXor @@ Pick[g, IntegerDigits[k, 2, 3], 1], {k, 0, 7}]];
G8 = Union[Select[grp /@ Subsets[Range[15], {3}], Length[#] == 8 &]];
Print["8-dim Basis-Unteralgebren: ", Length[G8]];
Print[{#, Wdim[DeleteCases[#, 0]]} & /@ G8];
