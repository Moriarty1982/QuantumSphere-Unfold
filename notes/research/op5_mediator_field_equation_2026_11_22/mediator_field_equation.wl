(* Erster Feldansatz fuer den gerichteten OP5-Vermittler. Methoden-Notiz Commit 6bad83cb. Erkundung, nicht blind. *)
(* Fourierbild: d_t -> -I w, d_i -> I k_i; x = w^2, q = k1^2 + k2^2 + k3^2, a = k1^2 + k2^2. L = (1/2) Y.M.Y, Y = (eta, Xxx, Xyy, Xxy, S).
   Feldgleichungen (Variation):  (d_t^2 - r_m Lap + m^2) X_ij = g (d_i d_j - kap delta_ij d_t^2) eta,
                                 (d_t^2 - r_s Lap + m_s^2) S = g_s d_t^2 eta,
                                 2 (d_t^2 - Lap + m_H^2) eta = J_h + g (d_i d_j X_ij - kap d_t^2 X_ii) + g_s d_t^2 S. *)
qq = k1^2 + k2^2 + k3^2;
dm = m2 + r qq - x; ds = ms2 + rs qq - x;
V = {-k1^2 + kap x, -k2^2 + kap x, -k1 k2};
M = {{2 (x - qq - mH2), g V[[1]], g V[[2]], 2 g V[[3]], -gs x},
     {g V[[1]], -dm, 0, 0, 0},
     {g V[[2]], 0, -dm, 0, 0},
     {2 g V[[3]], 0, 0, -2 dm, 0},
     {-gs x, 0, 0, 0, -ds}};
Print["(1) Fourier-Gleichungen M.Y = -(J_h, 0, 0, 0, 0): X-Zeile ", Simplify[M[[2]].{eta, Xxx, Xyy, Xxy, S}], " = 0;  S-Zeile ", M[[5]].{eta, Xxx, Xyy, Xxy, S}, " = 0"];
A = M[[2 ;; 5, 2 ;; 5]]; b = M[[1, 2 ;; 5]];
Deff = Simplify[-(M[[1, 1]] - b.Inverse[A].b)];
pol = {k1 -> Sqrt[a] Cos[ph], k2 -> Sqrt[a] Sin[ph]};
med = Simplify[TrigReduce[Expand[(Deff - 2 (mH2 + qq - x)) /. pol]], a >= 0];
Print["    effektiver eta-Operator: 2(m_H^2 + q - x) + (", Collect[Simplify[med], {g, gs}], ")"];
trV = Simplify[TrigReduce[Expand[(V[[1]]^2 + V[[2]]^2 + 2 V[[3]]^2) /. pol]], a >= 0];
Print["    Tr V^2 = ", Expand[trV]];

(* (2) Abgleich mit -gm2 Nm/dm *)
Nm = 2/3 (x^2 - a x + a^2);
eqs = DeleteCases[Thread[Flatten[CoefficientList[Expand[g2 (trV /. kap -> kp) + gs2 x^2 - gm2 Nm], {x, a}]] == 0], True];
sol = Solve[eqs, {g2, kp, gs2}];
Print["(2) bei d_s = d_m: g^2 Tr V^2 + g_s^2 x^2 = g_m^2 N_m identisch fuer ", sol];
Print["    ohne Skalar (g_s = 0): Abgleich nur des a^2- und a x-Koeffizienten: ", Solve[{Coefficient[Expand[g2 trV /. kap -> kp], a, 2] == 2/3 gm2, Coefficient[Coefficient[Expand[g2 trV /. kap -> kp], a, 1], x, 1] == -2/3 gm2}, {g2, kp}],
  "; Rest im x^2-Koeffizienten: ", Simplify[Coefficient[Expand[g2 trV /. kap -> kp], x, 2] - 2/3 gm2 /. {g2 -> 2/3 gm2, kp -> 1/2}]];

(* (3a) Matrix der Zeitableitungen *)
K = {{2, g kap, g kap, 0, -gs}, {g kap, 1, 0, 0, 0}, {g kap, 0, 1, 0, 0}, {0, 0, 0, 2, 0}, {-gs, 0, 0, 0, 1}};
Print["(3a) Hauptminoren der kinetischen Matrix: ", Simplify[Table[Det[K[[1 ;; i, 1 ;; i]]], {i, 5}]]];
Print["     positiv definit genau fuer g^2 kap^2 < 1 und g_s^2 + 2 g^2 kap^2 < 2 (aus den Minoren)"];
Print["     mit den Abgleichwerten (kap = 1/2, g^2 = 2/3 gm2, gs^2 = 1/3 gm2): Det K = ", Simplify[Det[K] /. {kap -> 1/2} /. {g^2 -> 2/3 gm2, gs^2 -> 1/3 gm2}], " -> gm2 < 3"];
(* (3b) statische Energie *)
stat = Simplify[TrigReduce[Expand[(Deff /. x -> 0) /. pol]], a >= 0];
Print["(3b) statischer Operator: ", stat];
Print["     statischer Operator bei a = q (k3 = 0) mal (m2 + r q): ", Expand[Simplify[(stat /. k3 -> 0 /. a -> qv) (m2 + r qv)]]];
Print["     Zaehler (2 r - g^2) q^2 + 2(m2 + r mH2) q + 2 mH2 m2 > 0 fuer alle q >= 0 bei positiven m2, mH2, r genau fuer: ",
  Reduce[ForAll[qv, qv >= 0, (2 r - g^2) qv^2 + 2 (m2 + r mH2) qv + 2 mH2 m2 > 0] && r > 0 && m2 > 0 && mH2 > 0, g, Reals]];
(* (3c) Dispersion auf einem Raster *)
par[gm2v_] := {mH2 -> 2, m2 -> 1, r -> 1/2, ms2 -> 1, rs -> 1/2, kap -> 1/2, g -> Sqrt[2/3 gm2v], gs -> Sqrt[1/3 gm2v]};
check[gm2v_] := Module[{res = {}},
  Do[Module[{det = Det[M /. par[gm2v] /. {k1 -> Sqrt[av], k2 -> 0, k3 -> Sqrt[kz]}], rts},
     rts = x /. NSolve[det == 0, x, WorkingPrecision -> 30];
     AppendTo[res, {av, kz, And @@ (Abs[Im[#]] < 10^-20 && Re[#] > 0 & /@ rts), Min[Re[rts]]}]],
   {av, {0, 1/2, 1, 2, 5, 20, 100}}, {kz, {0, 1, 10}}];
  {AllTrue[res, #[[3]] &], N[Min[res[[All, 4]]], 6], Select[res, ! #[[3]] &][[All, 1 ;; 2]]}];
Do[With[{c = check[gv]}, Print["(3c) g_m^2 = ", gv, ": alle x-Wurzeln reell und positiv: ", c[[1]], ", kleinste Wurzel ", c[[2]], ", Ausnahmen (a, k_z^2): ", c[[3]]]], {gv, {3/100, 1, 7/5, 8/5}}];

(* (4) Anschluss an r37 *)
Print["(4) String r37: Residuum ~ 2a^2 - 2a x + x^2; Feldansatz mit kap = 1/2, g_s = 0: Tr V^2 = ", Expand[trV /. kap -> 1/2], " = (1/2)(2a^2 - 2a x + x^2)"];
Print["    fehlendes Skalargewicht g_s^2/g^2 = ", (1/3)/(2/3)];
