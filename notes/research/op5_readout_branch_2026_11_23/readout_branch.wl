(* Zweig B: Rahmen u und Achse n als Daten der Auslese. Methoden-Notiz Commit bb7274a1. Erkundung, teilweise nicht blind (B2, B3). *)
(* Ebene Welle exp(-I w t + I k.x): d_mu -> I Pl_mu mit Pl = (-w, k1, k2, k3). Konvention der Riemann-Linearisierung wie
   OP5_J_Lokale_Antriebswirkung.md: R_{mu al nu be} = 1/2 (d_al d_nu g_{mu be} + d_mu d_be g_{al nu} - d_mu d_nu g_{al be} - d_al d_be g_{mu nu}). *)
eta = DiagonalMatrix[{1, -1, -1, -1}];
gs = Table[Symbol["g" <> ToString[Min[i, j]] <> ToString[Max[i, j]]], {i, 0, 3}, {j, 0, 3}];
gvars = DeleteDuplicates[Flatten[gs]];
Riem[Pl_] := Table[-1/2 (Pl[[al]] Pl[[nu]] gs[[mu, be]] + Pl[[mu]] Pl[[be]] gs[[al, nu]] - Pl[[mu]] Pl[[nu]] gs[[al, be]] - Pl[[al]] Pl[[be]] gs[[mu, nu]]),
   {mu, 4}, {al, 4}, {nu, 4}, {be, 4}];
(* Quelle S^{rs}: Kopplung L = 1/2 g_{rs} S^{rs} h; aus L/h = F[g] linear: S^{rs} = 2 dF/dg_rs fuer r = s, dF/dg_rs fuer r != s (jede gemischte Komponente einmal) *)
src[F_] := Table[With[{v = gs[[r, s]]}, If[r == s, 2 D[F, v], D[F, v]]], {r, 4}, {s, 4}];
fp[S1_, S2_] := Module[{S1l = eta . S1 . eta}, Total[Flatten[S1l S2]] - Tr[eta . S1] Tr[eta . S2]/3];
contr[R_, A_, u_] := Sum[A[[mu, nu]] u[[al]] u[[be]] R[[mu, al, nu, be]], {mu, 4}, {al, 4}, {nu, 4}, {be, 4}];
PiProj[u_, n_] := -Inverse[eta] + Outer[Times, u, u] - Outer[Times, n, n];

(* ---------- B1: Ruhesystem ---------- *)
Pl = {-w, k1, k2, k3}; R = Riem[Pl];
u0 = {1, 0, 0, 0}; n0 = {0, 0, 0, 1};
Sfull = Simplify[src[-contr[R, PiProj[u0, n0], u0]]];
Sbif = Module[{S = ConstantArray[0, {4, 4}], Pk = {k1, k2, 0}},
   S[[1, 1]] = -(k1^2 + k2^2); Do[S[[1, i + 1]] = S[[i + 1, 1]] = -w Pk[[i]], {i, 3}];
   Do[S[[i + 1, j + 1]] = -w^2 DiagonalMatrix[{1, 1, 0}][[i, j]], {i, 3}, {j, 3}]; S];
Print["(B1a) kovariante Auslese-Kopplung im Ruhesystem gleich der bifokalen Quelle? ", Simplify[Sfull - Sbif] === ConstantArray[0, {4, 4}],
  "  (Quotient S/S_bif an (0,0): ", Simplify[Sfull[[1, 1]]/Sbif[[1, 1]]], ")"];
Print["      Zerlegung: Pi u u R = -R_uu - E_nn identisch? ",
  Simplify[contr[R, PiProj[u0, n0], u0] - (-contr[R, Inverse[eta], u0] - contr[R, Outer[Times, n0, n0], u0])] === 0];
SRic = Simplify[src[contr[R, Inverse[eta], u0]]];      (* aus  h R_uu  *)
SE = Simplify[src[contr[R, Outer[Times, n0, n0], u0]]];  (* aus  h E_nn  *)
Print["      Quelle aus h R_uu: ", SRic // MatrixForm // InputForm];
Print["      Quelle aus h E_nn: ", SE // MatrixForm // InputForm];
cl[e_] := Simplify[Expand[e] /. w -> Sqrt[x] /. k1 -> Sqrt[a - k2^2], {x >= 0, a >= 0}];
Print["(B1c) FP-Zaehler: gesamt ", Factor[cl[fp[Sfull, Sfull]]], ";  R_uu-Anteil ", Factor[cl[fp[SRic, SRic]]], ";  E_nn-Anteil ", Factor[cl[fp[SE, SE]]],
  ";  Kreuzterm 2x ", Factor[cl[2 fp[SRic, SE]]]];
Print["      Erhaltung: p_mu S^{mu nu} fuer R_uu-Anteil ", Simplify[(Pl . SRic)], ";  E_nn-Anteil ", Simplify[(Pl . SE)]];

(* ---------- B2: Orientierung ---------- *)
Print["(B2) Quelle unter u -> -u unveraendert? ", Simplify[src[-contr[R, PiProj[-u0, n0], -u0]] - Sfull] === ConstantArray[0, {4, 4}],
  ";  FP-Zaehler unter w -> -w unveraendert? ", Simplify[(fp[Sfull, Sfull] /. w -> -w) - fp[Sfull, Sfull]] === 0];

(* ---------- B3: Rolle von r_m ---------- *)
stat = gm2 (2/3 a^2)/(m2 + rm q);
Print["(B3) statischer Zaehler/Nenner bei x = 0: ", stat, ";  Reihe in q: ", Normal[Series[stat, {q, 0, 1}]]];
Print["     r38.2 bei r_m = 1, g_m^2 = 3/100: geisterfrei (g_m^2 < 3): ", 3/100 < 3, ";  statisch stabil (g_m^2 <= 3 r_m): ", 3/100 <= 3];

(* ---------- B4: Detektorbewegung ---------- *)
Pls = {0, k1, k2, k3}; Rs = Riem[Pls];   (* statische Quelle im Ruhesystem der Praeparation *)
gam = 1/Sqrt[1 - b^2];
cases = {
   {"Bewegung entlang der Achse n", gam {1, 0, 0, b}, gam {b, 0, 0, 1}},
   {"Bewegung quer zur Achse (x)", gam {1, b, 0, 0}, {0, 0, 0, 1}}};
Do[Module[{uu = c[[2]], nn = c[[3]], S, N4},
   S = Simplify[src[-contr[Rs, PiProj[uu, nn], uu]]];
   N4 = Simplify[fp[S, S] /. {k1 -> Sqrt[a] Cos[ph], k2 -> Sqrt[a] Sin[ph]}];
   Print["(B4) ", c[[1]], ": Pruefung u.u = ", Simplify[uu . eta . uu], ", n.n = ", Simplify[nn . eta . nn], ", u.n = ", Simplify[uu . eta . nn]];
   Print["     N(b) = ", Factor[Simplify[TrigReduce[N4]]]];
   Print["     Reihe bis b^2: ", Simplify[TrigReduce[Normal[Series[N4, {b, 0, 2}]]]], ";  b = 0: ", Simplify[N4 /. b -> 0]]],
  {c, cases}];
