(* k242: Runde v4.10.0-r56, Lambda als Eingabe (Negativ-Schluss). Erkundung, nicht blind. Wolfram Language, exakt wo moeglich. *)

(* (A) Spurfreie (unimodulare) Friedmann-Gleichungen: Lambda als Integrationskonstante.
   Spurfreier Teil der Einstein-Gleichung in flachem FLRW: Hdot = -kappa/2 (rho + p).
   Erhaltung: rhodot = -3 H (rho + p).  Behauptung: d/dt (H^2 - kappa rho/3) = 0. *)
hdotTF = -kappa/2 (rho[t] + p[t]);
rhodot = -3 h[t] (rho[t] + p[t]);
dA = Simplify[D[h[t]^2 - kappa rho[t]/3, t] /. {h'[t] -> hdotTF, rho'[t] -> rhodot}];
Print["(A) d/dt(H^2 - kappa rho/3) unter spurfreier Gleichung und Erhaltung = ", dA];
(* Gegenprobe: jedes konstante L loest H^2 = kappa rho/3 + L/3 mit derselben spurfreien Gleichung *)
sol = DSolve[{h'[t] == -kappa/2 (rho[t] + p[t])}, h, t];
Print["(A') spurfreie Gleichung legt die Konstante nicht fest; DSolve-Loesung enthaelt C[1]: ", FreeQ[sol, C[1]] === False];

(* (B) Verschiebung V -> V + c in der reduzierten M-Lesart L = a(X/2 - V(phi)), X = -g^{mn} d_m phi d_n phi.
   Feldgleichung (homogen, flach FLRW): phi'' + 3H phi' + V'(phi) = 0 haengt nicht von c ab;
   Energie-Impuls: rho = a(phidot^2/2 + V + c), p = a(phidot^2/2 - V - c): Zusatz ist (rho, p) = (a c, -a c), w = -1. *)
lag[c_] := aW (1/2 ph'[t]^2 - (vv[ph[t]] + c));
eom[c_] := D[D[lag[c] sc[t]^3, ph'[t]], t] - D[lag[c] sc[t]^3, ph[t]];
Print["(B) Feldgleichung mit c minus ohne c = ", Simplify[eom[cc] - eom[0]]];
rhoB[c_] := aW (ph'[t]^2/2 + vv[ph[t]] + c); pB[c_] := aW (ph'[t]^2/2 - vv[ph[t]] - c);
Print["(B) Zusatz (rho, p) = ", Simplify[{rhoB[cc] - rhoB[0], pB[cc] - pB[0]}], ", w des Zusatzes = ", Simplify[(pB[cc] - pB[0])/(rhoB[cc] - rhoB[0])]];

(* (C) Die Auslesung Omega_M = beta^2 legt Lambda nicht fest, sondern tauscht es gegen die Epoche.
   rho_M = rhoM0 x^-3 (x = a/a0), rho_L = 3 L/kappa.  Omega_M(x) = rho_M/(rho_M + rho_L). *)
(* Kontrolle mit der in H96 notierten Form: Sum 2 exp(...) = 1 (Gewicht 2 je j) *)
gBI2 = g /. FindRoot[Sum[2 Exp[-2 Pi g Sqrt[(k/2) (k/2 + 1)]], {k, 1, 4000}] == 1, {g, 0.24}, WorkingPrecision -> 30];
gStr = Log[2]/(Pi Sqrt[3]);
gL = gBI2/gStr; b2 = (gL - 1)/(gL + 1);
Print["(C) gamma_BI (Gewicht 2) = ", N[gBI2, 10], ", gamma_L = ", N[gL, 10], ", beta^2 = ", N[b2, 10]];
omegaM[x_, rhoM0_, L_] := rhoM0 x^-3/(rhoM0 x^-3 + 3 L/kappa);
solx = Solve[omegaM[x, rhoM0, L] == bb && x > 0 && rhoM0 > 0 && L > 0 && kappa > 0 && 0 < bb < 1, x, Reals];
Print["(C) Epoche x* mit Omega_M = beta^2, fuer jedes L > 0: ", Simplify[solx]];
(* Lambda in Einheiten von H an dieser Epoche: H*^2 = kappa(rho_M + rho_L)/3, Omega_L = 1 - bb  =>  L = 3 (1 - bb) H*^2 *)
Print["(C) Lambda = 3(1-beta^2) H*^2 = ", N[3 (1 - b2), 8], " H*^2"];
(* Zahl, die die Struktur liefern muesste: Lambda l_P^2 heute, Eingaben Planck 2018 (Literatur, Vorwissen): H0 = 67.4 km/s/Mpc, Omega_L = 0.6847 *)
H0 = 67.4*1000/(3.0856775814913673*10^22); cc = 299792458.; lP = 1.616255*10^-35;
Lam = 3*0.6847*H0^2/cc^2;
Print["(C) Lambda (Planck 2018) = ", ScientificForm[Lam, 4], " m^-2; Lambda l_P^2 = ", ScientificForm[Lam lP^2, 4]];
Print["(C) zum Vergleich mit Omega_L = 1 - beta^2: Lambda l_P^2 = ", ScientificForm[3 (1 - N[b2]) H0^2/cc^2 lP^2, 4]];
(* Wie gross muesste ein Exponent x in e^{-x} sein, um diese Zahl zu geben? *)
Print["(C) -ln(Lambda l_P^2) = ", N[-Log[Lam lP^2], 6], "; in Einheiten 2 Pi sqrt(3)/2 (j=1/2-Exponent): ", N[-Log[Lam lP^2]/(2 Pi Sqrt[3]/2), 6]];
