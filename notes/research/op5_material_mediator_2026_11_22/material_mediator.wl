(* Weg A: optische Mode des Materials als Vermittler. Methoden-Notiz Commit a86479e0. Erkundung, nicht blind. *)
(* Frame M, c = 1. x = w^2, q = |k|^2. Effektiver Operator fuer den Higgs-Radialmodus eta (W2: Zw = 2, c_h = 1):
   D = Zw (mH2 + q - x) + Sum_i k_i^2 Y.Inverse[M_i].Y, M_i Materialmatrix der Komponente i (Vorzeichen aus statischer Energie). *)
pos = {r1 > 0, r2 > 0, kk > 0, K > 0, c > 0, q > 0, x > 0};
Mi[s_] := {{r1 x - K q - s, s}, {s, r2 x - c K q - s}};
Y = {Y1, Y2};

(* (1) isotrop, longitudinal: D_extra = q Y.M^-1.Y *)
extra = Together[q Y.Inverse[Mi[kk]].Y];
dets = Solve[Det[Mi[kk]] == 0, x];
xopt = Select[x /. dets, Simplify[(# /. q -> 0) > 0, pos] &][[1]];
res = Simplify[Limit[(x - xopt) extra, x -> xopt], pos];
res0 = Simplify[SeriesCoefficient[res, {q, 0, 1}], pos];
Print["(1) optischer Pol: x_opt(q->0) = ", Simplify[xopt /. q -> 0, pos], ";  Residuum = q * ", Factor[res0], " + O(q^2)"];
Print["    Lesart: D_extra ~ -Res/(x_opt - x); Gegenstueck g_m^2 N_m = Res; isotrop, Zaehler ~ q (nicht N_m)"];
Print["    Residuum mit Y_a = f_a r_a / v: q * ", Factor[res0 /. {Y1 -> f1 r1/v, Y2 -> f2 r2/v}]];
xac = Select[x /. dets, Simplify[(# /. q -> 0) == 0, pos] &][[1]];
resac = Simplify[SeriesCoefficient[Simplify[Limit[(x - xac) extra, x -> xac], pos], {q, 0, 1}], pos];
Print["    akustischer Pol: Residuum = q * ", Factor[resac], " + O(q^2)"];

(* (2) Haengt das fuehrende statische Glied von r_m ab? *)
Nm = 2/3 (x^2 - ap x + ap^2);
ser = Normal[Series[(gm^2 Nm/(m^2 + rm q - x)) /. x -> 0, {q, 0, 1}]];
Print["(2) statisch: g_m^2 N_m/d_m = ", Expand[ser], " + O(q^2);  fuehrendes Glied ohne r_m: ", FreeQ[ser /. q -> 0, rm]];

(* (3) einachsig: Paarfeder quer kp, laengs kz -> Unendlich; k = (s, 0, t), q = s^2 + t^2 *)
exU = s^2 Y.Inverse[Mi[kp]].Y + 0 + t^2 Limit[Y.Inverse[Mi[kz]].Y, kz -> Infinity];
exU = Together[exU /. q -> s^2 + t^2];
Print["(3) Laengskomponente fuer kz -> Unendlich: ", Simplify[Limit[Y.Inverse[Mi[kz]].Y, kz -> Infinity]]];
posU = {r1 > 0, r2 > 0, kp > 0, K > 0, c > 0, s > 0, t > 0, x > 0};
detU = Solve[Det[Mi[kp]] == 0 /. q -> s^2 + t^2, x];
xoptU = Select[x /. detU, Simplify[(# /. {s -> 0, t -> 0}) > 0, posU] &][[1]];
resU = Simplify[Limit[(x - xoptU) exU, x -> xoptU], posU];
resU0 = Simplify[Normal[Series[resU /. {s -> e s, t -> e t}, {e, 0, 2}]] /. e -> 1, posU];
Print["    optischer Pol: Luecke ", Simplify[xoptU /. {s -> 0, t -> 0}, posU], ";  Residuum (fuehrend) = ", Factor[resU0]];
Print["    haengt nur von s^2 = a_perp ab: ", FreeQ[resU0, t]];

(* (4) statische induzierte Higgsquelle aus der optischen Mode, fuehrend: -eta * Res/x_opt *)
ind = Simplify[-resU0/(xoptU /. {s -> 0, t -> 0}), posU];
Print["(4) statisch induzierte Quelle (optischer Anteil) = eta * ", Factor[ind], ";  Form Delta_perp eta / w0^2 mit Gewicht (Y1/r1 - Y2/r2)^2 mu"];
Print["    Vergleichsmodell: Vermittlerterm statisch (2/3) g_m^2 a_perp^2/m^2, also eine Potenz a_perp mehr"];
