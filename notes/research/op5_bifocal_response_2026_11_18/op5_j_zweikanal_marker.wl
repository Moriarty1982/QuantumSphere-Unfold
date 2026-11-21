ClearAll["Global`*"];
Print["Kernel: ", $Version];
id = IdentityMatrix[2];
zero = ConstantArray[0, {2, 2}];
p = DiagonalMatrix[{p1, p2}];
k = DiagonalMatrix[{k1, k2}];
rootD = DiagonalMatrix[{d1, d2}];
ass = p1 > 0 && p2 > 0 && k1 > 0 && k2 > 0;
rel = {d1 -> Sqrt[p1 k1], d2 -> Sqrt[p2 k2]};
w = ArrayFlatten[{{Inverse[rootD], Inverse[rootD]}, {I rootD, -I rootD}}];
v = {{v11, v12}, {v21, v22}};
free = ArrayFlatten[{{zero, Inverse[p]}, {-p.k.k, zero}}];
interaction = ArrayFlatten[{{zero, zero}, {-v, zero}}];
weighted = Inverse[rootD].v.Inverse[rootD];
block = ArrayFlatten[{{I weighted/2, I weighted/2}, {-I weighted/2, -I weighted/2}}];
Print["Free traveling basis residual: ", FullSimplify[
 (Inverse[w].free.w - ArrayFlatten[{{I k, zero}, {zero, -I k}}]) /. rel, ass]];
Print["Flux-normalized interaction block residual: ", Simplify[Inverse[w].interaction.w - block]];
g = (free + interaction) /. v21 -> v12;
jflux = ArrayFlatten[{{zero, id/(2 I)}, {-id/(2 I), zero}}];
Print["Lossless flux residual: ", FullSimplify[
 ConjugateTranspose[g].jflux + jflux.g,
 ass && Element[{v11, v22, v12}, Reals]]];
born = {{u1^2, u1 u2 s}, {u1 u2 s, u2^2}};
Print["Born rank determinant residual: ", Expand[Det[born] - u1^2 u2^2 (1 - s^2)]];
t = {{tj, off1}, {off2, ta}};
q = DiagonalMatrix[{zj, za}];
Print["General marker modal trace residual: ", Together[
 {(Tr[t.q] - ta Tr[q])/(tj - ta), (tj Tr[q] - Tr[t.q])/(tj - ta)} - {zj, za}]];
Print["Illustrative mass scale in eV at 1 m: ",
 N[Sqrt[4 (360329/10^6) (1973269804/10^16)], 9]];
