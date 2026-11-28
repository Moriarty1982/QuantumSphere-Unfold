(* k457b (Test H241): exakte/symbolische Gegenprobe. Produkt wie k253/k321/k453-k456. *)
cj[x_] := Join[{First[x]}, -Rest[x]];
ml[x_, y_] := If[Length[x] == 1, x y,
  Module[{h = Length[x]/2, p, q, r, s},
   p = x[[;; h]]; q = x[[h + 1 ;;]]; r = y[[;; h]]; s = y[[h + 1 ;;]];
   Join[ml[p, r] - ml[cj[s], q], ml[s, p] + ml[q, cj[r]]]]];
pp = Join[{0}, Array[P, 7]]; qq = Join[{0}, Array[Q, 7]];
uu[t_, x_] := Join[Cos[t] x, Sin[t] x];
pq = ml[pp, qq]; dot = Rest[pp] . Rest[qq]; cr = ReplacePart[pq, 1 -> 0];
lhs = ml[uu[a, pp], uu[b, qq]];
rhs = -dot (Cos[b - a] UnitVector[16, 1] + Sin[b - a] UnitVector[16, 9]) + uu[-(a + b), cr];
Print["Identitaet u_a(p) u_b(q) = -(p.q)[cos(b-a) + sin(b-a) e8] + u_-(a+b)(p x q), symbolisch: Rest = ", Union[Simplify[TrigExpand[lhs - rhs]]]];
Print["Realteil von pq = -(p.q): ", Simplify[pq[[1]] + dot]];
Print["|Komponente von u_(-2t) senkrecht zu u_t|^2 = ", Simplify[1 - Cos[-2 t - t]^2]];
Print["Zahl der geordneten Paare verschiedener Einheiten e_a, e_b (a,b=1..7) mit |e_a x e_b| = 1: ", Count[Flatten[Table[If[i != j, Norm[ReplacePart[ml[UnitVector[8, i + 1], UnitVector[8, j + 1]], 1 -> 0]], 0], {i, 7}, {j, 7}]], 1]];
Print["Summe ueber v_k (Paritaet): ", Simplify[Total[{{1, 0}, {-1/2, Sqrt[3]/2}, {-1/2, -Sqrt[3]/2}}]]];
a0 = {0, 1, 1, 1, 1, 0, 0, 0}/2; b0 = {0, 1, -1, 0, 0, 1, 1, 0}/2; z8 = ConstantArray[0, 8];
hq = {UnitVector[8, 1], a0, b0, ml[a0, b0]};
blk = Join[Join[#, z8] & /@ hq, Join[z8, #] & /@ hq];
cop[v_] := Join[{UnitVector[16, 1]}, Table[Join[v[[1]] UnitVector[8, i + 1], v[[2]] UnitVector[8, i + 1]], {i, 7}]];
vs = {{1, 0}, {-1/2, Sqrt[3]/2}, {-1/2, -Sqrt[3]/2}};
Print["dim(B_x cap V_k) exakt: ", Table[8 + 8 - MatrixRank[Join[blk, cop[v]]], {v, vs}]];
Print["B_x abgeschlossen: ", MatrixRank[Join[blk, Flatten[Table[ml[blk[[i]], blk[[j]]], {i, 8}, {j, 8}], 1]]] == 8];
