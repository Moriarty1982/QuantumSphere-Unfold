(* k416b (H206): exakte Wolfram-Gegenkontrolle der struktur-erhaltenden Richtung in der Ebene.
   Massen-Erhaltung = verschwindende Diagonale des Generators in der zirkulanten (T-)Eigenbasis. *)
T = {{0,0,1},{-1,0,0},{0,-1,0}};
E13 = {{0,0,1},{0,0,0},{0,0,0}}; E31 = {{0,0,0},{0,0,0},{1,0,0}};
E12 = {{0,1,0},{0,0,0},{0,0,0}}; E21 = {{0,0,0},{1,0,0},{0,0,0}};
E23 = {{0,0,0},{0,0,1},{0,0,0}}; E32 = {{0,0,0},{0,0,0},{0,1,0}};
K1 = I (E13 - E31);                          (* DIRS["K-1"] *)
K2 = I (-E12 + E21 + E23 - E32)/Sqrt[2];     (* DIRS["K-2"] *)
{vals, vecs} = Eigensystem[T];
vn = Normalize /@ vecs;
diag[M_] := Table[Simplify[Conjugate[vn[[i]]].M.vn[[i]]], {i, 3}];
Print["T-Eigenwerte = ", vals, "  (1, omega, omega^2 = zirkulant)"];
Print["Diag(K1) in T-Basis = ", diag[K1], "  (nicht alle 0 => aendert Massen)"];
Print["Diag(K2) in T-Basis = ", diag[K2], "  (0,0,0 => massenerhaltend)"];
Print["Eindeutigkeit: cos psi*diag(K1) + sin psi*diag(K2) = 0  =>  cos psi = 0  =>  psi = 90 (K2)."];
