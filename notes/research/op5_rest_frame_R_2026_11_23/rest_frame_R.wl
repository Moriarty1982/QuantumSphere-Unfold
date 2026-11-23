(* Kann das Feldruhesystem R aus OP1 die Verlangsamung tragen? Methoden-Notiz Commit a306f879. Erkundung, nicht blind. *)
eta = DiagonalMatrix[{1, -1, -1, -1}];
Fmat[Ev_, Bv_] := {{0, -Ev[[1]], -Ev[[2]], -Ev[[3]]}, {Ev[[1]], 0, -Bv[[3]], Bv[[2]]}, {Ev[[2]], Bv[[3]], 0, -Bv[[1]]}, {Ev[[3]], -Bv[[2]], Bv[[1]], 0}};
FR = Fmat[{0, 0, E0}, {0, 0, B0}];
boost[dir_, r_] := Module[{L = IdentityMatrix[4], i = dir + 1}, L[[1, 1]] = Cosh[r]; L[[i, i]] = Cosh[r]; L[[1, i]] = L[[i, 1]] = -Sinh[r]; L];
lowerF[L_, F_] := Module[{Linv = Inverse[L]}, Transpose[Linv] . F . Linv];
(* ---- 1. Symmetrie ---- *)
Print["(1a) Boost entlang der Achse aendert F? ", Simplify[lowerF[boost[3, r], FR] - FR] =!= ConstantArray[0, {4, 4}]];
Print["     Boost quer zur Achse aendert F? ", Simplify[lowerF[boost[1, r], FR] - FR] =!= ConstantArray[0, {4, 4}]];
Kz = {{0, 0, 0, 1}, {0, 0, 0, 0}, {0, 0, 0, 0}, {1, 0, 0, 0}};   (* Erzeuger des Boosts entlang z, wirkt auf kontravariante Vektoren *)
Jz = {{0, 0, 0, 0}, {0, 0, -1, 0}, {0, 1, 0, 0}, {0, 0, 0, 0}};  (* Drehung um z *)
Sg = Table[Symbol["s" <> ToString[Min[i, j]] <> ToString[Max[i, j]]], {i, 4}, {j, 4}];
cond = Flatten[{Kz . Sg + Sg . Transpose[Kz], Jz . Sg + Sg . Transpose[Jz]}];
sol = Solve[Thread[cond == 0], DeleteDuplicates[Flatten[Sg]]];
Print["(1b) invariante symmetrische Tensoren S^{mu nu}: ", MatrixForm[Sg /. First[sol]] // InputForm];
Fup = Inverse[eta] . FR . Inverse[eta];
Tdn = Table[Sum[FR[[m, a]] FR[[n, b]] Inverse[eta][[a, b]], {a, 4}, {b, 4}] - 1/4 eta[[m, n]] Sum[FR[[a, b]] Fup[[a, b]], {a, 4}, {b, 4}], {m, 4}, {n, 4}];
Tup = -Inverse[eta] . Tdn . Inverse[eta];   (* Vorzeichen so, dass T^00 = Energiedichte > 0 *)
Print["(1c) Energie-Impuls-Tensor des Feldes T^{mu nu} = ", Simplify[Tup] // InputForm, ";  invariant? ",
  Simplify[Flatten[{Kz . Tup + Tup . Transpose[Kz], Jz . Tup + Tup . Transpose[Jz]}]] === ConstantArray[0, 32]];
(* ---- 2. effektive Ausbreitung G = eta^-1 + lam T ---- *)
G = Inverse[eta] + lam Tup;
vax = Simplify[-G[[4, 4]]/G[[1, 1]]]; vtr = Simplify[-G[[2, 2]]/G[[1, 1]]];
Print["(2a) G = eta^-1 + lam T: Geschwindigkeit^2 entlang der Achse ", vax, ", quer ", vtr];
Ginv = Sg /. First[sol];
Print["(2b) allgemeiner invarianter Tensor: Geschwindigkeit^2 entlang der Achse = -S^33/S^00 = ", Simplify[-Ginv[[4, 4]]/Ginv[[1, 1]]]];
rho = (E0^2 + B0^2)/2;
lamq = Solve[(vtr /. lam -> L0/rho) == 1/2, L0];
Print["     quer auf 1/2 verlangsamt fuer lam rho = ", lamq];
(* ---- 3. Kegelgrenze mit r(alpha) = alpha * 1/2 + (1 - alpha) * 1 ---- *)
Aof[Z_, gm2_] := Z - 2 gm2/3;
bof[Z_, ch2_, gm2_, rm_, al_] := Z ch2 + 2 gm2/3 (rm - al);
j0sq[g02_, al_] := g02 al^2/2;
jmsq[gm2_, rm_, al_] := 2 gm2/3 (rm^2 - rm al + al^2);
speeds[Z_, ch2_, g02_, gm2_, r0_, rm_, al_] := Module[{AA = Aof[Z, gm2], Kh},
   Kh = DiagonalMatrix[{1/Sqrt[AA], 1, 1}];
   Eigenvalues[N[Kh . {{bof[Z, ch2, gm2, rm, al], Sqrt[j0sq[g02, al]], Sqrt[jmsq[gm2, rm, al]]}, {Sqrt[j0sq[g02, al]], r0, 0}, {Sqrt[jmsq[gm2, rm, al]], 0, rm}} . Kh, 30]]];
rOf[al_] := al/2 + (1 - al);
Do[Module[{tab = Table[{al, Max[speeds[1, ch2, 3/100, 3/100, rOf[al], rOf[al], al]]}, {al, 0, 1, 1/20}]},
   Print["(3) c_h^2 = ", ch2, ": groesstes Geschwindigkeitsquadrat ", Max[tab[[All, 2]]], " bei alpha = ", First[MaximalBy[tab, Last]][[1]],
    ";  alpha = 0: ", tab[[1, 2]], ";  alpha = 1: ", tab[[-1, 2]], ";  Grenze verletzt fuer alpha in ", Select[tab, #[[2]] > 1 &][[All, 1]]]],
  {ch2, {1/2, 1}}];
Print["    bei alpha = 0: j_0^2 = ", j0sq[3/100, 0], ", j_m^2 = ", jmsq[3/100, 1, 0], " (r = 1 entlang der Achse)"];
