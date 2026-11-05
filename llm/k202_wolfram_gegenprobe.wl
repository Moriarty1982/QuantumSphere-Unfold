(* k202: H87 - Wolfram-Gegenprobe zu H86 und Abfall der Beimischung bei grossem k Delta.
   Ausgefuehrt ueber den Wolfram-Connector (Wolfram Language Evaluator), 5. November 2026.
   Ergebnisse siehe Ergebnis_H87_Wolfram_Gegenprobe_Abfall.md. *)

(* H87c: scharfer Uebergang symbolisch *)
sol = First@Solve[{A + B == c + d, -b (-I w A + I w B) == a (-I w c + I w d)}, {c, d}] /. {A -> 0, B -> 1};
C0 = Simplify[c /. sol]; D0 = Simplify[d /. sol];
al = Simplify[C0/Sqrt[b/a] /. b -> x a, {a > 0, x > 0}]; be = Simplify[D0/Sqrt[b/a] /. b -> x a, {a > 0, x > 0}];
{C0, D0, al, be, Simplify[al^2 - be^2]}

(* H87a: direkte Integration auf der reellen Achse, WorkingPrecision 30 (tanh-Profil, Delta = 2, Drehsinn +) *)
bs = 10000/18203; x = bs^2; a = 1/(1 + x); b = x/(1 + x); dl = 2; L = 40;
f[kD_] := Module[{k = kD/dl, s, ch, dch},
  s = NDSolve[{y''[t] == -(Log[a/b] - I Pi) (1/(2 dl)) Sech[t/dl]^2 y'[t] - k^2 y[t],
     y[-L] == Exp[-I k L], y'[-L] == I k Exp[-I k L]}, y, {t, -L, L}, WorkingPrecision -> 30, MaxSteps -> Infinity];
  ch = y[L] /. First[s]; dch = y'[L] /. First[s]; Abs[(ch - dch/(I k))/2 Exp[I k L]]];
f /@ {2, 4, 6, 8}

(* H87b: Integration entlang tau = x + i h, h = hf * Pi Delta/2 < Pi Delta/2 (unterhalb der Singularitaet von sech^2).
   Analytische Koeffizienten, Randwerte bei Re tau -> +-oo unveraendert; gut konditioniert. *)
x0 = bs^2; aN = N[1/(1 + x0)]; bN = N[x0/(1 + x0)]; dlN = 2.; Lc = Log[aN/bN] - I Pi;
cc[kD_, hf_] := Module[{k = kD/dlN, h = hf Pi dlN/2, LL = 60., s, tt, ch, dch},
  s = NDSolve[{y''[xx] == -(Lc/(2 dlN)) Sech[(xx + I h)/dlN]^2 y'[xx] - k^2 y[xx],
     y[-LL] == Exp[I k (-LL + I h)], y'[-LL] == I k Exp[I k (-LL + I h)]}, y, {xx, -LL, LL},
    PrecisionGoal -> 12, AccuracyGoal -> 60, MaxSteps -> Infinity];
  tt = LL + I h; ch = y[LL] /. First[s]; dch = y'[LL] /. First[s]; Abs[(ch - dch/(I k))/2 Exp[I k tt]]];
{cc[4, 0.8], cc[8, 0.8], cc[8, 0.9]}
ks = {10, 15, 20, 25, 30};
{cc[#, 0.9] & /@ ks, cc[#, 0.95] & /@ ks}
