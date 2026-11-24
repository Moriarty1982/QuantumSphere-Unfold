(* k257b: exakte Kontrolle von M(chi, dnu) aus H126 (Wolfram-MCP-Kern, 24.11.2026; Ausgabe k257b_out.txt) *)
cd[x_List, y_List] := If[Length[x] == 1, x y, Module[{h = Length[x]/2, a1, b1, c1, d1, cj},
   cj[v_] := Prepend[-Rest[v], First[v]];
   a1 = x[[;; h]]; b1 = x[[h + 1 ;;]]; c1 = y[[;; h]]; d1 = y[[h + 1 ;;]];
   Join[cd[a1, c1] - cd[cj[d1], b1], cd[d1, a1] + cd[b1, cj[c1]]]]];
cj16[v_] := Prepend[-Rest[v], First[v]];
e[i_] := UnitVector[16, i + 1];
tens[X7_, t_] := Join[{0}, Cos[t] X7, {0}, Sin[t] X7];
e1 = UnitVector[7, 1]; e2 = UnitVector[7, 2];
g[k_] := e[0]/Sqrt[3] + Sqrt[2/3] tens[e1, 2 Pi k/3];
psi[c_, d_] := (e[0] + tens[Cos[c] e1 + Sin[c] e2, d])/Sqrt[2];
ip[x_, y_] := With[{z = cd[cj16[x], y]}, z[[1]] + I z[[9]]];
M[c_, d_] := Table[ip[g[j], cd[psi[c, d], cd[psi[c, d], g[k]]]], {j, 0, 2}, {k, 0, 2}];
Mass[c_, d_] := Table[ip[g[j], cd[cd[psi[c, d], psi[c, d]], g[k]]], {j, 0, 2}, {k, 0, 2}];
Ms = FullSimplify[M[c, d], Element[{c, d}, Reals]];
Print["Eigenwerte von M M^dag (symbolisch): ", FullSimplify[Eigenvalues[Ms . ConjugateTranspose[Ms]], Element[{c, d}, Reals]]];
Print["M - M_assoz (symbolisch): ", FullSimplify[Ms - Mass[c, d], Element[{c, d}, Reals]]];
Do[Print["Punkt ", p, ": Eigenwerte ", Simplify[Eigenvalues[N[M @@ (p Degree), 20] . ConjugateTranspose[N[M @@ (p Degree), 20]]]]], {p, {{30, 0}, {90, 45}, {137, 200}}}];
