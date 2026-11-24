(* k273b (Erkundung, nicht blind, 24.11.2026): exakte Kontrolle zu k273 Teil A, Wolfram-MCP-Kernel.
   Teil 1: allgemeine 2x2-Unitaere: Im(V11 V22 V12* V21*) = 0.
   Teil 2: Standardparametrisierung 3x3: Unitaritaet, J und Im(V_ij V_kl V*_il V*_kj) = J sum eps_ikm eps_jln fuer alle 81 Indizes. *)
u2 = {{Cos[t] Exp[I a], Sin[t] Exp[I b]}, {-Sin[t] Exp[I c], Cos[t] Exp[I (b + c - a)]}};
Simplify[ComplexExpand[Im[u2[[1,1]] u2[[2,2]] Conjugate[u2[[1,2]]] Conjugate[u2[[2,1]]]]]]
r12 = {{Cos[x1], Sin[x1], 0}, {-Sin[x1], Cos[x1], 0}, {0, 0, 1}}; r23 = {{1, 0, 0}, {0, Cos[x3], Sin[x3]}, {0, -Sin[x3], Cos[x3]}};
r13 = {{Cos[x2], 0, Sin[x2] Exp[-I d]}, {0, 1, 0}, {-Sin[x2] Exp[I d], 0, Cos[x2]}};
v = r23.r13.r12; re = {x1, x2, x3, d} \[Element] Reals;
uni = FullSimplify[ComplexExpand[ConjugateTranspose[v].v], re];
j3 = FullSimplify[ComplexExpand[Im[v[[1,1]] v[[2,2]] Conjugate[v[[1,2]]] Conjugate[v[[2,1]]]]], re];
eps = LeviCivitaTensor[3];
ident = FullSimplify[ComplexExpand[Flatten[Table[Im[v[[i,j]] v[[k,l]] Conjugate[v[[i,l]]] Conjugate[v[[k,j]]]] - j3 Sum[eps[[i,k,m]] eps[[j,l,n]], {m,3},{n,3}], {i,3},{j,3},{k,3},{l,3}]]], re];
{uni == IdentityMatrix[3], j3, Union[ident]}
