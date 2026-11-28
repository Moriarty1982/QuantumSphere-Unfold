(* k460b (Test H243): exakte Gegenprobe der Z3-Klassen in Wolfram Language.
   Unabhaengig von k460: T-Eigenbasis symbolisch, N-hat(pi/6) exakt, Klassenanteile mit FullSimplify. *)
T = {{0,0,1},{-1,0,0},{0,-1,0}}; w = Exp[2 Pi I/3];
tk = Table[Module[{v = First[NullSpace[T - w^k IdentityMatrix[3]]]}, FullSimplify[v/Sqrt[Simplify[Conjugate[v].v]]]], {k,0,2}];
Tb = Transpose[tk];
chk = Table[FullSimplify[T.tk[[k+1]] - w^k tk[[k+1]]], {k,0,2}];
nhat[d_, sb_] := Module[{l = Table[1 + Sqrt[2] Cos[d + 2 Pi k/3], {k,0,2}], ls, c, b},
  ls = SortBy[N[l, 30] -> l // Thread // Apply[List, #, {1}] &, Abs[First[#]] &][[All, 2]]; c = ls[[1]] - 1;
  b = sb Sqrt[Simplify[((ls[[2]] - ls[[3]])^2 - c^2)/8]]; {{1,b,c},{b,1,-b},{c,-b,1}}];
wM[N0_] := Module[{M = FullSimplify[Transpose[Tb].N0.Tb], tot}, tot = Total[Abs[M]^2, 2];
  FullSimplify[Table[Sum[If[Mod[i+j,3]==c, Abs[M[[i+1,j+1]]]^2, 0], {i,0,2},{j,0,2}], {c,0,2}]/tot]];
wD[D0_] := Module[{M = FullSimplify[ConjugateTranspose[Tb].D0.Tb], tot}, tot = Total[Abs[M]^2, 2];
  FullSimplify[Table[Sum[If[Mod[j-i,3]==c, Abs[M[[i+1,j+1]]]^2, 0], {i,0,2},{j,0,2}], {c,0,2}]/tot]];
E3[i_,j_] := Normal[SparseArray[{{i,j}->1},{3,3}]];
dirs = <|"S+b" -> (E3[1,2]+E3[2,1]-E3[2,3]-E3[3,2])/Sqrt[2], "S+c" -> E3[1,3]+E3[3,1], "S+d" -> E3[2,2],
 "S-p" -> (E3[1,2]+E3[2,1]+E3[2,3]+E3[3,2])/Sqrt[2], "S-q" -> (E3[1,1]-E3[3,3])/Sqrt[2],
 "K+" -> I (E3[1,2]-E3[2,1]+E3[2,3]-E3[3,2])/Sqrt[2], "K-1" -> I (E3[1,3]-E3[3,1]), "K-2" -> I (-E3[1,2]+E3[2,1]+E3[2,3]-E3[3,2])/Sqrt[2]|>;
n0 = Simplify[nhat[Pi/6, 1]];
bdir = {{0,1,0},{1,0,-1},{0,-1,0}}; cdir = {{0,0,1},{0,0,0},{1,0,0}};
v0 = {1,0,1}/Sqrt[2];
Print["t_k Eigenvektoren (Restvektoren): ", chk];
Print["N(pi/6) exakt: ", n0];
Print["W Majorana N(pi/6): ", wM[n0]];
Print["W Majorana b-Richtung: ", wM[bdir]];
Print["W Majorana c-Richtung: ", wM[cdir]];
Print["v0 Gewichte |<t_k,v0>|^2: ", FullSimplify[Abs[ConjugateTranspose[Tb].v0]^2]];
Print["v0 Eigenvektor von N(pi/6): ", FullSimplify[n0.v0 - ((n0.v0).v0) v0]];
Print["W Dirac je Richtung: ", KeyValueMap[#1 -> wD[#2] &, dirs]];
x = 0.0395773407`30;
Print["W Majorana N(pi/6 - x) numerisch: ", N[wM[nhat[Pi/6 - x, 1]], 10]];
