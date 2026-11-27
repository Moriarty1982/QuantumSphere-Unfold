(* k414b (H204): exakte Wolfram-Gegenkontrolle der Ladungs-kovarianten Operatoralgebra.
   Baut L_U (Linksmult. mit U=e7) exakt aus der Oktonion-Multiplikation, verifiziert
   L_U^2=-1 (also (iL_U)^2=+1), die beiden minimalen Idempotente P_up,P_dn (P^2=P,
   Orthogonalitaet, Vollstaendigkeit, Spuren) und das je erzwungene (B,D)/ (D/B). *)

(* --- Oktonion-Multiplikation (Cayley-Dickson, Basis e0..e7) --- *)
conj[x_] := Join[{x[[1]]}, -x[[2 ;;]]];
mul[x_, y_] := Module[{n = Length[x], h, a, b, c, d},
  If[n == 1, Return[x*y]]; h = n/2;
  a = x[[1 ;; h]]; b = x[[h + 1 ;; n]]; c = y[[1 ;; h]]; d = y[[h + 1 ;; n]];
  Join[mul[a, c] - mul[conj[d], b], mul[d, a] + mul[b, conj[c]]]];
ev[i_] := UnitVector[8, i + 1];
(* L_U auf den 6 Farbrichtungen (Komponenten e1..e6), U = e7 *)
LUfull = Transpose[Table[mul[ev[7], ev[j]], {j, 0, 7}]];
LU = LUfull[[2 ;; 7, 2 ;; 7]];                 (* 6x6, exakt ganzzahlig *)
Print["L_U^2 = -1 (6x6) ? ", LU.LU == -IdentityMatrix[6]];

(* Farbblock 36-dim = (Re/Im: 2) x (3 Farbpaare) x (6 Richtungen).  i und L_U: *)
J2 = {{0, -1}, {1, 0}};
Ii  = KroneckerProduct[J2, IdentityMatrix[18]];
LUc = KroneckerProduct[IdentityMatrix[2], KroneckerProduct[IdentityMatrix[3], LU]];
iLU = Ii.LUc;
I36 = IdentityMatrix[36];
Print["(i L_U)^2 = 1 (36x36) ? ", iLU.iLU == I36];

Pup = (I36 + iLU)/2; Pdn = (I36 - iLU)/2;
Print["P_up^2 = P_up ? ", Pup.Pup == Pup, "   P_dn^2 = P_dn ? ", Pdn.Pdn == Pdn];
Print["P_up + P_dn = 1 ? ", Pup + Pdn == I36, "   P_up.P_dn = 0 ? ", Pup.Pdn == 0*I36];
Print["Spur P_up = ", Tr[Pup], "   Spur P_dn = ", Tr[Pdn]];

(* Abstrakte 2-dim Algebra: in der Ladungsbasis ist iL_U = diag(+1 auf Up, -1 auf Down).
   Fuer einen l_k^2-Operator O gilt b_up=<O>_up, b_down=<O>_down; B=(b_up+b_down)/2,
   D=(b_up-b_down)/2.  Exakte Werte je 'einzelner Darstellung': *)
bd[bu_, bd0_] := {(bu + bd0)/2, (bu - bd0)/2};
Print["O=1      (b_up,b_down)=(1,1)  -> (B,D)=", bd[1, 1],  "  D/B=", bd[1, 1][[2]]/bd[1, 1][[1]]];
Print["O=iL_U   (b_up,b_down)=(1,-1) -> (B,D)=", bd[1, -1], "  (B=0, D/B=oo)"];
Print["O=P_up   (b_up,b_down)=(1,0)  -> (B,D)=", bd[1, 0],  "  D/B=", bd[1, 0][[2]]/bd[1, 0][[1]]];
Print["O=P_dn   (b_up,b_down)=(0,1)  -> (B,D)=", bd[0, 1],  "  D/B=", bd[0, 1][[2]]/bd[0, 1][[1]]];
Print["=> einzelne Darstellungen erzwingen D/B in {0,+1,-1,oo}; Datenwert 1.0085 nicht darunter."];

(* Kontrolle, dass die 36-dim Realisierung dieselben erzwungenen Werte liefert:
   mittlere Diagonale von O auf dem +1- bzw -1-Eigenraum von iL_U. *)
upProj = Pup; dnProj = Pdn;
avg[O_, P_] := Tr[P.O.P]/Tr[P];
checkBD[O_, nm_] := Module[{bu, bdn, B, D},
  bu = avg[O, upProj]; bdn = avg[O, dnProj];
  B = (bu + bdn)/2; D = (bu - bdn)/2;
  Print["  36-dim  ", nm, ": (B,D)=", {B, D}, If[B =!= 0, "  D/B=" <> ToString[D/B], "  B=0"]]];
checkBD[I36, "O=1   "]; checkBD[iLU, "O=iL_U"]; checkBD[Pup, "O=P_up"]; checkBD[Pdn, "O=P_dn"];
Print["Kontrolle fertig."];
