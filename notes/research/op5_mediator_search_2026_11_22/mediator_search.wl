(* Vermittler-Suche fuer den OP5-Fall. Methoden-Notiz Commit a3443d99. Erkundung, nicht blind. *)

(* (1) Konnektoren aus k185: p_M = m (Cosh, Sinh), Tachyonbild p_T = m (Sinh, +-Cosh), Signatur (+,-) *)
msq[q_] := q[[1]]^2 - q[[2]]^2;
pM = m {Cosh[e], Sinh[e]};
pTgeg = m {Sinh[e], -Cosh[e]};   (* gegenlaeufig *)
pTmit = m {Sinh[e], Cosh[e]};    (* mitlaufend *)
etaSym = ArcTanh[0.5494];
Do[Module[{q = c[[2]]},
   Print["(1) ", c[[1]], ": q^2 = ", FullSimplify[msq[q]], ",  v = q1/q0 = ", FullSimplify[q[[2]]/q[[1]]],
    ",  bei eta_sym: q^2/m^2 = ", NumberForm[N[msq[q]/m^2 /. e -> etaSym], 5], ", |v| = ", NumberForm[N[Abs[q[[2]]/q[[1]]] /. e -> etaSym], 5]]],
  {c, {{"Paar gegenlaeufig", pM + pTgeg}, {"Uebergang gegenlaeufig", pM - pTgeg}, {"Paar mitlaufend", pM + pTmit}, {"Uebergang mitlaufend", pM - pTmit}}}];

(* (2) Zwei Kontinua mit Paarfeder, longitudinal, ebene Welle Exp[i(q z - w t)]; alle Parameter positiv *)
pos = {r1 > 0, r2 > 0, k > 0, K > 0, c > 0, q > 0};
Mmat = {{r1 w2 - K q^2 - k, k}, {k, r2 w2 - c K q^2 - k}};
branches = Simplify[w2 /. Solve[Det[Mmat] == 0, w2], pos];
at0 = Simplify[branches /. q -> 0, pos];
Print["(2) Zweige bei q = 0: ", at0];
opt = Pick[branches, Simplify[# > 0, pos] & /@ at0, True][[1]];
ac = Pick[branches, Simplify[# == 0, pos] & /@ at0, True][[1]];
gap = Simplify[opt /. q -> 0, pos];
vopt = Simplify[SeriesCoefficient[opt, {q, 0, 2}], pos];
vac = Simplify[SeriesCoefficient[ac, {q, 0, 2}], pos];
Print["    optischer Zweig: Luecke w0^2 = ", gap, ";  v_opt^2 = ", vopt, ";  akustisch: v_ak^2 = ", vac];
ev = Simplify[NullSpace[Mmat /. {q -> 0, w2 -> gap}], pos];
Print["    Eigenvektor der optischen Mode bei q = 0 (u, w): ", ev, ";  r1 u + r2 w = ", Simplify[{r1, r2}.First[ev]]];
cpl = Simplify[{Y1, Y2}.First[ev]];
Print["    Kopplung an delta J_h = Y1 d_z u + Y2 d_z w proportional zu ", cpl, ";  null genau fuer Y1/r1 = Y2/r2: ", Simplify[cpl /. Y2 -> Y1 r2/r1]];
