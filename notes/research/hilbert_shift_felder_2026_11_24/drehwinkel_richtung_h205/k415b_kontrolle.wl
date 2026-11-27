(* k415b (H205): exakte Wolfram-Gegenkontrolle der Drehwinkel-Richtung. *)
r2 = Sqrt[2];
A1 = {{0,0,1},{0,0,0},{-1,0,0}};                 (* reeller Teil von K1 = i(E13-E31) *)
A2 = ({{0,-1,0},{1,0,1},{0,-1,0}})/r2;           (* reeller Teil von K2 = i(-E12+E21+E23-E32)/sqrt2 *)
axis[A_] := {A[[3,2]], A[[1,3]], A[[2,1]]};      (* Dualvektor: A_ij = eps_ijk a_k *)
a1 = axis[A1]; a2 = axis[A2];
v0 = {1,0,1}/r2;
Print["a1 = ", a1, "   a2 = ", a2];
Print["a1.v0 = ", Simplify[a1.v0], "   a2.v0 = ", Simplify[a2.v0]];
Nmat = {{1,b,c},{b,1,-b},{c,-b,1}};
Print["Nhat.v0 - (1+c) v0 = ", Simplify[Nmat.v0 - (1+c) v0], "  (v0 ist Eigenvektor fuer ALLE b,c)"];
up = {0,1,0}; um = {1,0,-1}/r2;
Print["a1 = u+ ? ", Simplify[a1-up]==={0,0,0}, "   a2 = -u- ? ", Simplify[a2+um]==={0,0,0}];
bis = (a1+a2)/r2;
Print["bis.up = ", Simplify[bis.up], "   bis.um = ", Simplify[bis.um]];
Print["|bis.up| == |bis.um| (exakte 45-Grad-Halbierung) ? ", Simplify[Abs[bis.up]-Abs[bis.um]]==0];
Print["Rang[{a1,a2}] = ", MatrixRank[{a1,a2}], "   a1.a2 = ", Simplify[a1.a2]];
Print["Rang[{a1,a2,v0}] = ", MatrixRank[{a1,a2,v0}], "  (3 => v0 nicht in span{a1,a2}; span = Ebene senkrecht v0)"];
