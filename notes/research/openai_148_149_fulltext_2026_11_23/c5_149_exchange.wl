(* C5 / OpenAI-Familie 149 (Permanenz schwach reversibler Massenwirkungssysteme), Erkundung 23.11.2026.
   Austausch zwischen Materie-Frame (x = C5_M) und Tachyon-Frame (1 - x = C5_T); Gegenstueck zur Kragenrekursion C5_M^(n) = (3/4)^n.
   Ausgabe: c5_149_exchange_stdout.txt. Der erste Versuch als ein einziger Block brach mit einem Serverfehler des Konnektors ab
   und wurde in die Teile unten zerlegt. *)

(* (a) linear, schwach reversibel: M <-> T *)
DSolve[{x'[t] == -k1 x[t] + k2 (1 - x[t]), x[0] == x0}, x[t], t]
s1 = (E^(-(k1*t) - k2*t)*(-k2 + E^((k1 + k2)*t)*k2 + k1*x0 + k2*x0))/(k1 + k2);
Print["(a) M<->T: Grenzwert = ", Limit[s1, t -> Infinity, Assumptions -> k1 > 0 && k2 > 0], " ; Kontrolle Dgl: ", Simplify[D[s1, t] - (-k1 s1 + k2 (1 - s1))], " ; s1(0) = ", Simplify[s1 /. t -> 0]];
Print["(a) Untergrenze: min(x0, k2/(k1+k2)) > 0, da s1 monoton zwischen x0 und k2/(k1+k2): s1 = k2/(k1+k2) + (x0 - k2/(k1+k2)) E^(-(k1+k2) t) -> ", Simplify[s1 - (k2/(k1 + k2) + (x0 - k2/(k1 + k2)) E^(-(k1 + k2) t))]];
(* (b) linear, einseitig: M -> T *)
s2 = x0 E^(-k t);
Print["(b) M->T: C5_M = x0 E^(-k t), > 0 fuer jedes endliche t, Grenzwert ", Limit[s2, t -> Infinity, Assumptions -> k > 0]];
(* (c) nichtlinear, schwach reversibel: M + T <-> 2T *)
Print["(c) M+T<->2T: Gleichgewichte von (1-x)(-k1 x + k2 (1-x)) = 0: ", Solve[(1 - x) (-k1 x + k2 (1 - x)) == 0, x]];
(* (d) nichtlinear, einseitig: M + T -> 2T *)
s4 = x0/(x0 + (1 - x0) E^(k t));
Print["(d) M+T->2T: Kontrolle Dgl x' = -k x (1-x): ", Simplify[D[s4, t] + k s4 (1 - s4)], " ; s4(0) = ", Simplify[s4 /. t -> 0], " ; Grenzwert ", Limit[s4, t -> Infinity, Assumptions -> k > 0 && 0 < x0 < 1]];

(* numerische Kontrollen *)
solc = NDSolveValue[{x'[t] == (1 - x[t]) (-2 x[t] + (1 - x[t])), x[0] == 10^-6}, x, {t, 0, 40}, WorkingPrecision -> 30];
Print["(c) k1=2,k2=1,x0=1e-6: min x = ", N[Min[Table[solc[t], {t, 0, 40, 1/10}]], 6], ", x(40) = ", N[solc[40], 10], " (k2/(k1+k2) = 1/3)"];
eqs = {m'[t] == -1 m[t] + 2 tt[t] - 3 m[t]^2 + 1 m[t] tt[t] + 0.5 p[t] - 0.7 m[t],
   tt'[t] == 1 m[t] - 2 tt[t] + 3 m[t]^2 - 1 m[t] tt[t] - 1.5 tt[t] + 0.2 p[t],
   p'[t] == 1.5 tt[t] - 0.2 p[t] - 0.5 p[t] + 0.7 m[t]};
(* Reaktionen: M<->T (1, 2), 2M<->M+T (3, 1), T<->P (1.5, 0.2), P->M 0.5, M->P 0.7; schwach reversibel *)
sol3 = NDSolveValue[Join[eqs, {m[0] == 10^-5, tt[0] == 0.99, p[0] == 10^-5 - 0.00002 + 0.01}], {m, tt, p}, {t, 0, 60}];
Print["Drei-Frame-Netz, schwach reversibel: min M = ", Min[Table[sol3[[1]][t], {t, 0, 60, 0.05}]], ", M(60) = ", sol3[[1]][60], ", Summe(60) = ", sol3[[1]][60] + sol3[[2]][60] + sol3[[3]][60]];
Print["Summe(0) = ", 10^-5 + 0.99 + 10^-5 - 0.00002 + 0.01];

(* endliche Null braucht nicht-Lipschitz-Dynamik am Nullpunkt (klassisch) *)
xs = (Sqrt[x0] - c t/2)^2;
Print["x' = -c Sqrt[x]: Loesung (Sqrt[x0] - c t/2)^2 fuer t <= t*, Kontrolle: ", Simplify[D[xs, t] + c Sqrt[xs], Assumptions -> c > 0 && x0 > 0 && 0 <= t < 2 Sqrt[x0]/c], " ; Nullzeit t* = ", Solve[Sqrt[x0] - c t/2 == 0, t]];
Print["x' = -c x: x0 E^(-c t) == 0 loesbar fuer endliches t? ", Reduce[x0 E^(-c t) == 0 && x0 > 0 && c > 0, t, Reals]];
Print["S = N^2 bei N = t - t0: S(t0) = 0, S'(t0) = ", D[(t - t0)^2, t] /. t -> t0, " (doppelte Nullstelle, kein monotoner Abstieg ueber t0 hinaus)"];
