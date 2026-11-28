(* k456b (Test H240): exakte Gegenprobe fuer B2 an einem rationalen allgemeinen Nullteiler. Produkt wie k253/k321/k453. *)
cj[x_] := Join[{First[x]}, -Rest[x]];
ml[x_, y_] := If[Length[x] == 1, x y,
  Module[{h = Length[x]/2, p, q, r, s},
   p = x[[;; h]]; q = x[[h + 1 ;;]]; r = y[[;; h]]; s = y[[h + 1 ;;]];
   Join[ml[p, r] - ml[cj[s], q], ml[s, p] + ml[q, cj[r]]]]];
ee[i_] := UnitVector[16, i + 1];
Lm[x_] := Transpose[Table[ml[x, ee[j]], {j, 0, 15}]];
a = {0, 1, 1, 1, 1, 0, 0, 0}/2; b = {0, 1, -1, 0, 0, 1, 1, 0}/2; x2 = Join[a, b];
ab = ml[a, b]; one = UnitVector[8, 1]; z8 = ConstantArray[0, 8];
hq = {one, a, b, ab};
blk = Join[Join[#, z8] & /@ hq, Join[z8, #] & /@ hq];
qperp = NullSpace[hq];
Qc = Join[Join[#, z8] & /@ qperp, Join[z8, #] & /@ qperp];
L = Lm[x2]; Cb = Transpose[L];
Print["ab = ", ab, "; H_x orthonormal: ", hq . Transpose[hq] == IdentityMatrix[4]];
Print["Rang L = ", MatrixRank[L], "; C enthaelt H_x + H_x e8: ", MatrixRank[Join[Cb, blk]] == 12];
Print["dim(C cap Komplement) = ", MatrixRank[Cb] + Length[Qc] - MatrixRank[Join[Cb, Qc]]];
K = NullSpace[L];
Print["Kern im Komplement: ", MatrixRank[Join[Qc, K]] == Length[Qc]];
Print["L bildet H_x + H_x e8 in sich ab, Rang dort: ", MatrixRank[L . Transpose[blk]], "; Bild in Block: ", MatrixRank[Join[blk, Transpose[L . Transpose[blk]]]] == 8];
Print["Rang von L auf dem Komplement: ", MatrixRank[L . Transpose[Qc]], "; Bild im Komplement: ", MatrixRank[Join[Qc, Transpose[L . Transpose[Qc]]]] == 8];
