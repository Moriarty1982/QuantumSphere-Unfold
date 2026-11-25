(* k330c (Test H147, Wolfram exakt): g2 = Der(O), su3 = Stabilisator von e7, so3 = Stabilisator des total reellen Raums W3 = span(e1,e2,e3)
   in su3 (Lesart A); Casimir-Eigenwerte auf O und unter ad auf su3. Ausgabe k330c_out.txt. *)
cj[x_] := Prepend[-Rest[x], First[x]];
ml[x_, y_] := If[Length[x] == 1, x y, Module[{h = Length[x]/2, a, b, c, d},
   a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]];
   Join[ml[a, c] - ml[cj[d], b], ml[d, a] + ml[b, cj[c]]]]];
e = IdentityMatrix[8];
Dm = Array[dd, {8, 8}];
eqs = Flatten[Table[Dm . ml[e[[i]], e[[j]]] - ml[Dm . e[[i]], e[[j]]] - ml[e[[i]], Dm . e[[j]]], {i, 8}, {j, 8}]];
ns = NullSpace[Normal[CoefficientArrays[eqs, Flatten[Dm]][[2]]]];
g2 = Partition[#, 8] & /@ ns;
st = NullSpace[Transpose[(# . e[[8]]) & /@ g2]];
su3 = (Total[# g2]) & /@ st;
W3 = e[[{2, 3, 4}]]; PW = Transpose[W3] . W3;
co = NullSpace[Transpose[Flatten[(IdentityMatrix[8] - PW) . # . PW] & /@ su3]];
so3 = (Total[# su3]) & /@ co;
cas = -Total[# . # & /@ Orthogonalize[so3, Tr[#1 . Transpose[#2]] &]];
Print["dim g2, su3, so3: ", {Length[g2], Length[su3], Length[so3]}];
Print["Casimir auf O (8), Eigenwerte: ", Sort[Eigenvalues[cas]], "; auf W3: ", Eigenvalues[cas[[2 ;; 4, 2 ;; 4]]]];
sub = Flatten /@ su3; pinv = PseudoInverse[Transpose[sub]];
ad[X_] := pinv . Transpose[Flatten[X . # - # . X] & /@ su3];
son = Orthogonalize[so3, Tr[#1 . Transpose[#2]] &];
Print["ad-Casimir auf su3, Eigenwerte: ", Sort[Eigenvalues[-Total[ad[#] . ad[#] & /@ son]]]];
