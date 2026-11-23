(* OP1 / OpenAI-Familie 148 (Entropieraten-Dimensionsformel), Erkundung 23.11.2026.
   Lauf 1: Zaehlgleichungen als Moran-Gleichungen in natuerlichen Einheiten r_j = Exp[-2 Pi a(j)], a(j) = Sqrt[j(j+1)].
   Lauf 2: H(G_n)/(n chi) fuer ein abgeschnittenes System (Skalen j = 1/2, 1) mit vier Kopplungsarten der Kopien |j,+j>, |j,-j>.
   Ein verworfener Zwischenlauf (Translationen t = 0 bei mehreren Skalen, dadurch gemeinsame Fixpunkte und unbeabsichtigte
   Ueberlappungen) ist in der Ausgabedatei vermerkt. Ausgabe: op1_148_moran_overlap_stdout.txt *)

(* ---------- Lauf 1 ---------- *)
a[j_] := Sqrt[j (j + 1)];
js = Range[1/2, 200, 1/2];
F[w_, g_?NumericQ] := Total[w /@ js * Exp[-2 Pi g a /@ js]];
gM = g /. FindRoot[F[2 &, g] == 1, {g, 0.24}, WorkingPrecision -> 30];
gT = Log[2]/(Pi Sqrt[3]);
g1 = g /. FindRoot[F[1 &, g] == 1, {g, 0.16}, WorkingPrecision -> 30];
gP = g /. FindRoot[F[(2 # + 1) &, g] == 1, {g, 0.27}, WorkingPrecision -> 30];
Print["gamma_M (Gewicht 2, DL)       = ", N[gM, 12]];
Print["gamma_T (nur j=1/2, Gewicht 2) = ", N[gT, 12]];
Print["gamma_P (Gewicht 2j+1, GM/ENP) = ", N[gP, 12]];
Print["gamma_1 (|j,+j> und |j,-j> exakt ueberlappt, Gewicht 1) = ", N[g1, 12]];
Print["T mit exakter Ueberlappung: eine Abbildung, Attraktor ein Punkt, Dimension 0"];
Print["Verhaeltnisse: gM/gT = ", N[gM/gT, 10], "  g1/gT = ", N[g1/gT, 10], "  g1/gM = ", N[g1/gM, 10]];
Print["Abbruchkontrolle jmax=200: Rest der Summe bei gM ~ ", N[2 Exp[-2 Pi gM a[400/2 + 1/2]], 3]];
p = Flatten[Table[{Exp[-2 Pi gM a[j]], Exp[-2 Pi gM a[j]]}, {j, js}]];
r = Flatten[Table[{Exp[-2 Pi a[j]], Exp[-2 Pi a[j]]}, {j, js}]];
H = -Total[p Log[p]]; chi = -Total[p Log[r]];
Print["Summe p = ", N[Total[p], 15], "   H(p)/chi = ", N[H/chi, 15], "   gamma_M = ", N[gM, 15]];
pm = Table[2 Exp[-2 Pi gM a[j]], {j, js}]; rm = Table[Exp[-2 Pi a[j]], {j, js}];
Print["Gewicht 2 mit p_M, aber +-j identifiziert: h/chi = H(p_merged)/chi = ", N[(-Total[pm Log[pm]])/(-Total[pm Log[rm]]), 12], "  (<= gamma_1 = ", N[g1, 12], " als Maximum ueber p)"];
pOpt = Table[Exp[-2 Pi g1 a[j]], {j, js}];
Print["Maximum ueber p im ueberlappten System (p = r^gamma_1): h/chi = ", N[(-Total[pOpt Log[pOpt]])/(-Total[pOpt Log[rm]]), 12]];

(* ---------- Lauf 2 ---------- *)
scales = {1/2, 1};
gTr = g /. FindRoot[Total[2 Exp[-2 Pi g a /@ scales]] == 1, {g, 0.2}, WorkingPrecision -> 40];
rr[j_] := Exp[-2 Pi a[j]]; pj[j_] := Exp[-2 Pi gTr a[j]];
tp[j_] := Sqrt[2]/(3 + 2 j); tm[j_] := Sqrt[5]/(4 + 3 j);
cases = {
  "verschieden" -> Flatten[Table[{{rr[j], pj[j], tp[j]}, {rr[j], pj[j], tm[j]}}, {j, scales}], 1],
  "gespiegelt" -> Flatten[Table[{{rr[j], pj[j], tp[j]}, {-rr[j], pj[j], tm[j]}}, {j, scales}], 1],
  "identisch" -> Flatten[Table[{{rr[j], pj[j], tp[j]}, {rr[j], pj[j], tp[j]}}, {j, scales}], 1],
  "gespiegelt, gleiches Zentrum" -> Flatten[Table[{{rr[j], pj[j], tp[j]}, {-rr[j], pj[j], tp[j] (1 + rr[j])/(1 - rr[j])}}, {j, scales}], 1]};
comp[{r1_, t1_}, {r2_, t2_}] := {r1 r2, r1 t2 + t1};
key[w_] := Round[N[Fold[comp, {1, 0}, w[[All, {1, 3}]]], 50]/{10^-35, 10^-35}];
rate[ms_, n_] := Module[{assoc = GroupBy[Tuples[ms, n], key -> (Times @@ #[[All, 2]] &), Total]},
   N[-Total[(# Log2[#]) & /@ Values[assoc]]/n, 10]];
chiL[ms_] := N[-Total[(#[[2]] Log2[Abs[#[[1]]]]) & /@ ms], 12];
Print["gamma (abgeschnitten, j<=1) = ", N[gTr, 10]];
Do[With[{c = First[cs], ms = Last[cs]},
   Print[c, ": H(G_n)/(n chi), n=1..4: ", Table[rate[ms, n]/chiL[ms], {n, 1, 4}]]], {cs, cases}];
Print["Fixpunkt phi_+ (j=1/2): ", N[tp[1/2]/(1 - rr[1/2]), 8], "  Fixpunkt phi_- gleiches Zentrum: ", N[(tp[1/2] (1 + rr[1/2])/(1 - rr[1/2]))/(1 + rr[1/2]), 8]];
