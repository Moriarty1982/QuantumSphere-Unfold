(* k360b / Test H162: exakte Gegenprobe in Wolfram Language, unabhaengig aufgebaut (Cayley-Dickson-Rekursion). *)
cj[v_] := Join[{v[[1]]}, -Rest[v]];
cd[x_, y_] := If[Length[x] == 1, x*y, Module[{h = Length[x]/2, a, b, c, d},
   a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]];
   Join[cd[a, c] - cd[cj[d], b], cd[d, a] + cd[b, cj[c]]]]];
e[n_, k_] := UnitVector[n, k + 1];
Lm[n_, x_] := Transpose[Table[cd[x, e[n, b]], {b, 0, n - 1}]];
Rm[n_, x_] := Transpose[Table[cd[e[n, b], x], {b, 0, n - 1}]];
I16 = IdentityMatrix[16];
(* Derivationen von O exakt, su(3)_c = Stabilisator von e7, diagonal auf beide Haelften *)
vars = Flatten[Array[dd, {8, 8}]]; Dm = Array[dd, {8, 8}];
eqs = Flatten[Table[Dm . cd[e[8, i], e[8, j]] - cd[Dm . e[8, i], e[8, j]] - cd[e[8, i], Dm . e[8, j]], {i, 0, 7}, {j, 0, 7}]];
ns = NullSpace[Normal[CoefficientArrays[eqs, vars][[2]]]];
g2 = Table[ArrayReshape[v, {8, 8}], {v, ns}];
stab = NullSpace[Transpose[Table[d . e[8, 7], {d, g2}]]];
su3 = Table[ArrayFlatten[{{#, 0}, {0, #}}] &[Sum[cc[[k]] g2[[k]], {k, Length[g2]}]], {cc, stab}];
Print["dim g2 = ", Length[g2], "; dim su(3)_c = ", Length[su3]];
(* Projektoren *)
HN = {1, 8, 9, 16}; COL = Complement[Range[16], HN];
P0 = DiagonalMatrix[Table[If[MemberQ[HN, k], 1, 0], {k, 16}]]; Pc = I16 - P0;
L16[x_] := Lm[16, x]; R16[x_] := Rm[16, x];
QS = I16/2 - (I/6) L16[e[16, 7]] - (I/3) R16[e[16, 7]];
ev = Eigensystem[QS[[2 ;; 7, 2 ;; 7]]];
v3 = Table[PadRight[PadLeft[ev[[2, k]], 7], 16], {k, Flatten[Position[ev[[1]], 2/3]]}];
psi = Module[{p = IdentityMatrix[16], c = -1/2, s = Sqrt[3]/2}, Do[p[[i + 1, i + 1]] = c; p[[i + 1, i + 9]] = -s; p[[i + 9, i + 1]] = s; p[[i + 9, i + 9]] = c, {i, 1, 7}]; p];
V = Transpose[Join[v3, (psi . #) & /@ v3, (psi . psi . #) & /@ v3]];
P3 = Simplify[V . PseudoInverse[V]]; P3b = Pc - P3;
Print["R_x vertauschen mit su(3)_c: ", AllTrue[R16 /@ {e[16, 7], e[16, 8], e[16, 15]}, Function[r, AllTrue[su3, Simplify[r . # - # . r] == 0*I16 &]]]];
Print["Rang P3 = ", MatrixRank[P3], "; P3 vertauscht mit su(3)_c: ", AllTrue[su3, Simplify[P3 . # - # . P3] == 0*I16 &]];
Q[u_] := P0 . (I16/2 - (I/2) L16[u]) . P0 + (2/3) P3 + (1/3) P3b;
ax[a_, b_, c_] := a e[16, 7] + b e[16, 8] + c e[16, 15];
Rf = R16 /@ {e[16, 7], e[16, 8], e[16, 15]};
barg[G_] := Module[{Ps}, Ps = Table[Module[{J = (I/2) g, n = Length[g]}, IdentityMatrix[n]/2 + J], {g, G}];
   Simplify[Tr[Ps[[1]] . Ps[[2]] . Ps[[3]]]/Tr[Ps[[1]]]]];
blk[m_, idx_] := m[[idx, idx]];
Print["[R7,R8] + 2 R15 = 0 auf H_n: ", blk[Rf[[1]] . Rf[[2]] - Rf[[2]] . Rf[[1]] + 2 Rf[[3]], HN] == 0*IdentityMatrix[4],
  "; [R7,R8] - 2 R15 = 0 farbig: ", blk[Rf[[1]] . Rf[[2]] - Rf[[2]] . Rf[[1]] - 2 Rf[[3]], COL] == 0*IdentityMatrix[12]];
Print["Bargmann Leptonen = ", barg[blk[#, HN] & /@ Rf], "; Quarks = ", barg[blk[#, COL] & /@ Rf]];
cases = {{"e7", ax[1, 0, 0]}, {"-e7/2 + (Sqrt3/2) e15", ax[-1/2, 0, Sqrt[3]/2]}, {"e8 (Q_*)", ax[0, 1, 0]}, {"(2 e7 + e8 + 2 e15)/3", ax[2/3, 1/3, 2/3]}};
Do[Module[{q = Simplify[Q[cs[[2]]]], cp},
   cp = Factor[CharacteristicPolynomial[q, x]];
   Print["u = ", cs[[1]], ": char. Polynom = ", cp];
   Print["   [Q,su3] = 0: ", AllTrue[su3, Simplify[q . # - # . q] == 0*I16 &], "; conj(Q) = 1 - Q: ", Simplify[Conjugate[q] - (I16 - q)] == 0*I16,
     "; [R_x,Q] = 0: ", AllTrue[Rf, Simplify[q . # - # . q] == 0*I16 &], "; [Q,psi] = 0: ", Simplify[q . psi - psi . q] == 0*I16];
   Print["   O_0: Leck^2 = ", Simplify[Total[Flatten[Abs[q[[9 ;; 16, 1 ;; 8]]]^2]]], "; |Q_u - Q_S|^2 auf O_0 = ",
     Simplify[Total[Flatten[Abs[(q - QS)[[1 ;; 8, 1 ;; 8]]]^2]]]]], {cs, cases}];
(* allgemeine Achse symbolisch: L_u^2 = -1 und [L_u, R_x] = 0 auf H_n *)
Module[{lu = blk[L16[ax[ua, ub, uc]], HN]},
  Print["symbolisch: L_u^2 auf H_n (Diagonale, mit uc^2 = 1 - ua^2 - ub^2) = ", Diagonal[Simplify[Expand[lu . lu] /. uc^2 -> 1 - ua^2 - ub^2]],
   "; Nebendiagonale null: ", Simplify[Expand[lu . lu] - DiagonalMatrix[Diagonal[Expand[lu . lu]]]] === ConstantArray[0, {4, 4}],
   "; [L_u, R_x] = 0 auf H_n: ", AllTrue[Rf, Flatten[Expand[lu . blk[#, HN] - blk[#, HN] . lu]] === ConstantArray[0, 16] &]]];
