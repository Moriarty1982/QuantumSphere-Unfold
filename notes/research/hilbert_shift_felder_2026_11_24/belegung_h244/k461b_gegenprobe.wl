(* k461b (Test H244): exakte Gegenprobe in Wolfram Language, zwei Auswertungen (Teil 1 Muster, Teil 2 Baum).
   Ladungsbasis t_k unabhaengig von k461 von Hand angesetzt und geprueft. *)
(* ---------- Teil 1: Muster ---------- *)
w = Exp[2 Pi I/3]; Dm = DiagonalMatrix[{1,-1,1}];
tk = {{1,-1,1}/Sqrt[3], {1, -w^2, w}/Sqrt[3], {1, -w, w^2}/Sqrt[3]};
T = {{0,0,1},{-1,0,0},{0,-1,0}};
Print["t_k Eigenvektoren: ", Table[Simplify[ComplexExpand[T.tk[[k+1]] - w^k tk[[k+1]]]], {k,0,2}], "; orthonormal: ", Simplify[ComplexExpand[Conjugate[tk].Transpose[tk]]] == IdentityMatrix[3]];
Tb = Transpose[tk];
ws[z_] := RootReduce[ComplexExpand[Abs[ConjugateTranspose[Tb].(Dm.z)]^2]/RootReduce[ComplexExpand[Conjugate[z].z]]];
pats = Select[Tuples[{None,0,1,2},3], Count[#, None] < 3 &];
vec[p_] := p /. {None -> 0, g_Integer :> w^g};
res = Table[{p, ws[vec[p]]}, {p, pats}];
target = {2/3,1/6,1/6};
Mset = Select[res, #[[2]] === target &][[All,1]];
Sset = Select[pats, Mod[Total[DeleteCases[#, None]], 3] == 0 &];
Print["Muster: ", Length[pats], "; |M| = ", Length[Mset], "; |S| = ", Length[Sset], "; |M ∩ S| = ", Length[Intersection[Mset, Sset]], "; M = S: ", Sort[Mset] === Sort[Sset]];
Print["M = ", Mset];
Print["Anteilsklassen: ", Tally[res[[All,2]]]];
Print["Mittel W ueber schliessende Vollbelegungen: ", Mean[ws[vec[#]] & /@ Select[Tuples[{0,1,2},3], Mod[Total[#],3]==0 &]]];
(* ---------- Teil 2: Baum (eigene Auswertung, gleiche tk) ---------- *)
cls[N0_] := Module[{M = ComplexExpand[Transpose[Tb].N0.Tb]}, Table[Simplify[ComplexExpand[Sum[If[Mod[i+j,3]==c, Abs[M[[i+1,j+1]]]^2, 0], {i,0,2},{j,0,2}]], Element[{b,c0},Reals]], {c,0,2}]];
q = cls[{{1,b,c0},{b,1,-b},{c0,-b,1}}];
W0 = Simplify[q[[1]]/Total[q]];
Print["Klassennormen (b, c reell): ", q];
Print["W0(b, c) = ", W0];
Print["W0 = 2/3 genau auf: ", Reduce[W0 == 2/3, {b, c0}, Reals]];
l[d_] := Table[1 + Sqrt[2] Cos[d + 2 Pi k/3], {k,0,2}];
cc[d_] := l[d][[2]] - 1; bb2[d_] := ((l[d][[3]] - l[d][[1]])^2 - cc[d]^2)/8;
Print["Sortierung auf [0, pi/6] geprueft (Stichproben): ", And @@ Table[Ordering[Abs[N[l[d]]]] == {2,3,1}, {d, 0, Pi/6 - 10^-6, Pi/600}]];
Print["b^2(d) = ", FullSimplify[bb2[d]], ";  c(d) = ", FullSimplify[cc[d]]];
w0d = Simplify[W0 /. {b^2 -> bb2[d], c0 -> cc[d]}];
Print["W0 entlang Baum, bei pi/6: ", FullSimplify[w0d /. d -> Pi/6], "; bei pi/12: ", FullSimplify[w0d /. d -> Pi/12], "; bei 0: ", FullSimplify[w0d /. d -> 0]];
Print["Nullstellen W0 - 2/3 auf [0, pi/6]: ", Quiet[Reduce[w0d == 2/3 && 0 <= d <= Pi/6, d]]];
Print["dW0/dd > 0 auf [0, pi/6) (Minimum der Ableitung, 30 Stellen): ", N[MinValue[{D[w0d, d], 0 <= d <= Pi/6}, d], 10]];
