(* k275b (Erkundung, nicht blind, 24.11.2026): exakte Kontrolle zu k275 C/E, Wolfram-MCP-Kernel.
   Je Oktonion-Richtung wirkt X -> R X R^T auf H3(C) = Sym (reell, Spin 2 + Spin 0) + i Antisym (Spin 1).
   (1) Casimir auf Sym und Antisym. (2) Farbneutrale Ebene span(1,e7) ~ C: L_e7 je Platz = Eintrag x_k -> i x_k (Konjugat -> -i);
   Kommutator mit so(3). (3) Farbtriplett-Paar (e_a, e7 e_a): beide imaginaer, L_e7 dreht zwischen ihnen; Kommutator mit so(3). *)
gens = {{{0,0,0},{0,0,-1},{0,1,0}}, {{0,0,1},{0,0,0},{-1,0,0}}, {{0,-1,0},{1,0,0},{0,0,0}}};
symB = Join[{IdentityMatrix[3]/Sqrt[3]}, {{{1,0,0},{0,-1,0},{0,0,0}}/Sqrt[2], {{1,0,0},{0,1,0},{0,0,-2}}/Sqrt[6], {{0,1,0},{1,0,0},{0,0,0}}/Sqrt[2], {{0,0,1},{0,0,0},{1,0,0}}/Sqrt[2], {{0,0,0},{0,0,1},{0,1,0}}/Sqrt[2]}];
antB = {{{0,0,0},{0,0,-1},{0,1,0}}, {{0,0,1},{0,0,0},{-1,0,0}}, {{0,-1,0},{1,0,0},{0,0,0}}}/Sqrt[2];
act[g_, m_] := g.m + m.Transpose[g];
rep[g_, basis_] := Table[Tr[Transpose[basis[[i]]].act[g, basis[[j]]]], {i, Length[basis]}, {j, Length[basis]}];
cas[basis_] := Eigenvalues[-Sum[rep[g, basis].rep[g, basis], {g, gens}]];
toReal[m_] := Join[Table[Tr[Transpose[symB[[k]]].Re[m]], {k, 6}], Table[Tr[Transpose[antB[[k]]].Im[m]], {k, 3}]];
fromReal[v_] := v[[1 ;; 6]].symB + I v[[7 ;; 9]].antB;
kk = {{0, I, -I}, {-I, 0, I}, {I, -I, 0}};
jm = Transpose[Table[toReal[kk fromReal[UnitVector[9, k]]], {k, 9}]];
rg[g_] := Transpose[Table[toReal[act[g, fromReal[UnitVector[9, k]]]], {k, 9}]];
{cas[symB], cas[antB], Max[Abs[Flatten[jm]]], Table[Max[Abs[Flatten[rg[g].jm - jm.rg[g]]]], {g, gens}],
 Module[{r2 = Table[ArrayFlatten[{{rg[g][[7 ;; 9, 7 ;; 9]], 0}, {0, rg[g][[7 ;; 9, 7 ;; 9]]}}], {g, gens}], j2 = ArrayFlatten[{{0, -IdentityMatrix[3]}, {IdentityMatrix[3], 0}}]}, Table[Max[Abs[Flatten[r.j2 - j2.r]]], {r, r2}]]}
