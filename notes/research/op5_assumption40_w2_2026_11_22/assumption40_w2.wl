(* Annahme (40) aus W2? Methoden-Notiz Commit a9b61787. Erkundung, nicht blind. Signatur (+,-,-,-) fuer die Feldgleichung. *)

(* (1) Radialmodus: Phi = (0, hW) in unitaerer Eichung, |Phi| = hW, L = (d_t hW)^2 - (grad hW)^2 - V(hW) - hW Sum y n *)
V[h_] := -mu^2 h^2 + lam h^4;
vev = Sqrt[mu^2/(2 lam)];
Print["(1) V'(v) = ", Simplify[V'[vev], {mu > 0, lam > 0}], ";  V''(v) = ", Simplify[V''[vev], {mu > 0, lam > 0}]];
(* Euler-Lagrange fuer hW: 2 (d_t^2 - Lap) hW + V'(hW) + Sum y n = 0; linear in eta um v *)
lin = Series[V'[vev + ep eta], {ep, 0, 1}] // Normal // Simplify[#, {mu > 0, lam > 0}] &;
Print["    V'(v + eta) linear = ", lin /. ep -> 1];
Print["    => 2 (d_t^2 - Lap) eta + 4 mu^2 eta = J_h,  J_h = -Sum y n;  m_H^2 = 2 mu^2, kinetischer Faktor Z_W = 2"];
(* Fourierform: 2 (q - x + m_H^2) eta = J_h *)
W2op = 2 (q - x + mH2);

(* (2) Lineare Mischung mit der Metrik, minimal: T_munu = 2 d_mu h d_nu h - g_munu [ (dh)^2 - V(h) ]; linear in eta: -g_munu (-V'(v) eta) *)
T1 = -(-V'[vev] eta);
Print["(2) minimal: linearer Anteil von T (proportional zu g_munu) = ", Simplify[T1, {mu > 0, lam > 0}], "  (keine lineare eta-Metrik-Mischung im Vakuum)"];
(* Mit xi R |Phi|^2 = xi R hW^2: linearer Term in eta *)
xiTerm = Coefficient[Expand[xi Rcurv (vev + eta)^2], eta, 1];
Print["    mit xi R |Phi|^2: linearer Term = ", Simplify[xiTerm, {mu > 0, lam > 0}], "  (Mischung proportional zu xi v)"];
(* Lineare Kopplung an ein massives Vektorfeld (Z-Boson): (m_Z^2/v^2)(v + eta)^2 Z.Z ist in Z quadratisch *)
zTerm = Coefficient[Expand[(mZ2/vev^2) (vev + eta)^2 Zsq], eta, 1];
Print["    Kopplung eta an Z-Boson: ", Simplify[zTerm, {mu > 0, lam > 0}], " * eta, quadratisch in Z (Zsq = Z_mu Z^mu): keine lineare Mischung"];

(* (3) Koeffizientenvergleich des skalaren OP5-Operators mit dem W2-Operator (g_m = 0) *)
OP5scal = Z (Om2 + ch2 q - x) + 3/2 g02 (q - x);
sol = Solve[Thread[CoefficientList[OP5scal - W2op, {q, x}] == 0] // Flatten // DeleteCases[#, True] &, {Z, ch2, Om2}];
Print["(3) Bedingungen fuer OP5-Skalar = W2-Radialmodus: ", sol];
Print["    insbesondere c_h^2 = ", ch2 /. First[sol], " ;  minimal (xi = 0) ist g0 = 0, also Z = 2, Omega^2 = m_H^2"];
chosen = {Z -> 1, ch2 -> 1/2, g02 -> 3/100};
Print["    gesetzte Daten Z = 1, c_h^2 = 1/2, g0^2 = 3/100: Koeffizient von q = ", Coefficient[OP5scal /. chosen, q], ", von -x = ", -Coefficient[OP5scal /. chosen, x], "  (gleich nur bei Lorentz-Invarianz)"];

(* (4) Gerichteter Kanal: N_m/d_m mit d_m = m^2 + r_m q - x; W2 hat keinen linear an eta gekoppelten massiven Vermittler (2), also g_m = 0 *)
Kfull = Z (x - Om2 - ch2 q) - 3 g02 (q - x)/2 + gm2 Nm/dm;
Print["(4) Kern ohne gerichteten Kanal (g_m = 0): ", Simplify[Kfull /. gm2 -> 0], " ;  der gerichtete Kontrast (r32.4) lebt im Vermittler-Sektor N_m/d_m"];
Print["    Lorentz-invariantes massives Feld in W2 haette r_m = 1; gesetzt ist r_m = 1/2 (unterluminal): kein W2-Gegenstueck"];
