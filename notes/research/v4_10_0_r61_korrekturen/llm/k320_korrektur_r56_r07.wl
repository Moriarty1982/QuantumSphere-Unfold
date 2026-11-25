(* k320: Runde v4.10.0-r61, Korrektur zu r56.4 (Normierung rho_Lambda) und r07.4 (Wurzel in beta_sym). Erkundung, nicht blind. Wolfram Language, exakt. *)
(* (A) r56.4 mit der ueblichen Normierung rho_L = L/kappa, H^2 = kappa rho/3 *)
omega[x_, L_, norm_] := rhoM0 x^-3/(rhoM0 x^-3 + norm L/kappa);
assum = rhoM0 > 0 && L > 0 && kappa > 0 && 0 < bb < 1 && x > 0;
solA = Solve[omega[x, L, 1] == bb && assum, x, Reals];
Print["(A) x*^3 mit rho_L = L/kappa: ", Simplify[(x /. First[solA])^3, assum]];
hA = kappa (rhoM0 x^-3 + L/kappa)/3 /. First[solA];
Print["(A) Lambda/H*^2 mit rho_L = L/kappa: ", FullSimplify[L/hA, assum]];
(* (B) dieselbe Rechnung mit rho_L = 3 L/kappa, wie in r56.4 geschrieben *)
solB = Solve[omega[x, L, 3] == bb && assum, x, Reals];
Print["(B) x*^3 mit rho_L = 3L/kappa: ", Simplify[(x /. First[solB])^3, assum]];
hB = kappa (rhoM0 x^-3 + 3 L/kappa)/3 /. First[solB];
Print["(B) Lambda/H*^2 mit rho_L = 3L/kappa: ", FullSimplify[L/hB, assum]];
(* (C) Zahl: beta^2 aus gamma_L *)
gT = Log[2]/(Pi Sqrt[3]); gL = 1.864699765;
b2 = (gL - 1)/(gL + 1);
Print["(C) (gamma_L-1)/(gamma_L+1) = ", NumberForm[b2, 10], "; 3(1-beta^2) = ", NumberForm[3 (1 - b2), 10], "; (1-beta^2) = ", NumberForm[1 - b2, 10]];
(* (D) r07.4: beta_sym mit und ohne Wurzel *)
Print["(D) Sqrt[(gL-1)/(gL+1)] = ", NumberForm[Sqrt[b2], 10], "; ohne Wurzel = ", NumberForm[b2, 10], "; Quadrat davon = ", NumberForm[b2^2, 10]];
(* (E) Unabhaengigkeit vom Vorfaktor N bleibt: gamma_* = N kappa, Verhaeltnis frei von N, also auch jede Funktion des Verhaeltnisses *)
Print["(E) D[Sqrt[(N k1/(N k2) - 1)/(N k1/(N k2) + 1)], N] = ", Simplify[D[Sqrt[(N k1/(N k2) - 1)/(N k1/(N k2) + 1)], N]]];
