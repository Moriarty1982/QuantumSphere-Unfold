(* Weg B: Vakuumhintergrund als Traeger des gerichteten Vermittlers. Methoden-Notiz Commit 9f91c274. Erkundung, nicht blind. *)
(* Metrik diag(1,-1,-1,-1), p^mu = (w, k1, k2, k3), x = w^2, a = k1^2 + k2^2, q = a + k3^2, p^2 = x - q. *)
eta = DiagonalMatrix[{1, -1, -1, -1}];
p = {w, k1, k2, k3}; pl = eta.p;
cl[e_] := Simplify[TrigReduce[Expand[e /. {w -> Sqrt[x], k1 -> Sqrt[a] Cos[ph], k2 -> Sqrt[a] Sin[ph]}]], {x >= 0, a >= 0}];
psq = pl.p;

(* (1) Lorentz-invariant: Polarisationssummen, Zaehler am Pol p^2 = M^2 *)
P = -Inverse[eta] + Outer[Times, p, p]/M^2;
n1 = Simplify[pl.P.pl];
Print["(1) Spin 0: Zaehler (2 A v)^2, konstant; Pol bei p^2 = M^2 mit konstantem Residuum, nicht gerichtet"];
Print["    Spin 1 (Proca, J = p): Zaehler = ", Factor[n1], ";  am Pol: ", Simplify[n1 /. k3 -> Sqrt[w^2 - k1^2 - k2^2 - M^2]]];
Print["    Spin 1 Austausch Zaehler/(p^2 - M^2) = ", Simplify[n1/(psq - M^2)], "  (Kontaktterm, kein Pol)"];
pPp = Simplify[pl.P.pl];
n2 = Simplify[pPp^2 - (1/3) pPp^2];
Print["    Spin 2 (Fierz-Pauli, J = p p): Zaehler = (2/3) (p.P.p)^2 = ", Factor[n2], ";  Nullstelle am Pol der Ordnung 2"];

(* (2) Hintergrund: Rahmen u, Achse n; T = u u, S = Querprojektor (obere Indizes) *)
T = DiagonalMatrix[{1, 0, 0, 0}]; S = DiagonalMatrix[{0, 1, 1, 0}];
c4[A_] := Sum[A[[i, j, k, l]] pl[[i]] pl[[j]] pl[[k]] pl[[l]], {i, 4}, {j, 4}, {k, 4}, {l, 4}];
t4[f_] := Table[f[i, j, k, l], {i, 4}, {j, 4}, {k, 4}, {l, 4}];
TT = t4[T[[#1, #2]] T[[#3, #4]] &];
B = t4[(T[[#1, #3]] S[[#2, #4]] + T[[#1, #4]] S[[#2, #3]] + S[[#1, #3]] T[[#2, #4]] + S[[#1, #4]] T[[#2, #3]])/2 &];
G = t4[(S[[#1, #3]] S[[#2, #4]] + S[[#1, #4]] S[[#2, #3]])/2 - S[[#1, #2]] S[[#3, #4]]/2 &];
Dd = t4[S[[#1, #2]] S[[#3, #4]]/2 &];
Ee = t4[T[[#1, #2]] S[[#3, #4]] + S[[#1, #2]] T[[#3, #4]] &];
Print["(2) Spin 1 quer (Summe S): Zaehler = ", cl[pl.S.pl]];
Print["    Spin 2 Bausteine: TT -> ", cl[c4[TT]], ", B -> ", cl[c4[B]], ", G -> ", cl[c4[G]], ", D -> ", cl[c4[Dd]], ", E -> ", cl[c4[Ee]]];
Print["    Spin 2 quer, spurfrei (G): ", cl[c4[G]], ";  quer mit Spur (G + D): ", cl[c4[G + Dd]]];
Nm = 2/3 (x^2 - a x + a^2);
gen = cl[c4[al TT + be B + ga G + de Dd + ep Ee]];
sol = Solve[Thread[CoefficientList[gen - Nm, {x, a}] == 0], {al, ga, ep}];
Print["    Allgemeine Summe = ", Collect[gen, {x, a}], ";  gleich N_m fuer ", sol];
(* Positivitaet: Bloecke TT/D (2x2 mit Mischung Sqrt[2] ep), B, G *)
blk = {{al, Sqrt[2] ep}, {Sqrt[2] ep, de}};
cond = Reduce[{be >= 0, ga >= 0, de >= 0, al >= 0, Det[blk] >= 0} /. First[sol], {be, de}, Reals];
Print["    positive Polarisationssumme mit N_m genau fuer: ", cond];
Print["    Randpunkt be = 1/3, de = 4/3: ", First[sol] /. {be -> 1/3, de -> 4/3}, ", Det = ", Det[blk] /. First[sol] /. {be -> 1/3, de -> 4/3}];
(* Lorentzscher (2+1)-Unterraum ohne Longitudinalterm *)
etaP = DiagonalMatrix[{1, -1, -1, 0}];
Lz = t4[(etaP[[#1, #3]] etaP[[#2, #4]] + etaP[[#1, #4]] etaP[[#2, #3]])/2 - cc etaP[[#1, #2]] etaP[[#3, #4]] &];
Print["    (2+1)-Lorentz-Summe: ", Factor[cl[c4[Lz]]], ";  N_m - (2/3)(x - a)^2 = ", Factor[Nm - 2/3 (x - a)^2]];
