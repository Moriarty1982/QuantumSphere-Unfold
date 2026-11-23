(* H122: Bestimmt die Auslese ihren Rahmen selbst? Vorab-Notiz llm/Vorab_Notiz_H122_Auslese_Extremum.md (Commit d861db0e).
   OP1: Q_F(u) = |E'|^2 + |B'|^2 fuer F mit E || B || z. OP5: transverse Gezeitenauslese von r46 (Funktionen unveraendert aus
   notes/research/op5_readout_branch_2026_11_23/readout_branch.wl), statische Moden, Detektorrahmen (u, n) = reiner Boost von (u_p, e_z).
   Der Wolfram-Kern des MCP ist zustandslos; die Bloecke 1-5 wurden einzeln ausgefuehrt, jeder mit der Praeambel P.
   Ausgabe: llm/h122_readout_extremum.txt *)

(* ===== Block 1: OP1 (H122a) ===== *)
dv = {Sin[th] Cos[ph], Sin[th] Sin[ph], Cos[th]};
boostEB[E_, B_, v_, d_] := Module[{g = 1/Sqrt[1 - v^2], vv = v d},
   {g (E + Cross[vv, B]) - (g - 1) (E . d) d, g (B - Cross[vv, E]) - (g - 1) (B . d) d}];
{Ep, Bp} = boostEB[{0, 0, E0}, {0, 0, B0}, Tanh[et], dv];
QF = Simplify[Ep . Ep + Bp . Bp, Assumptions -> Element[{th, ph, et}, Reals]];
Print["(a) Q_F - Q_F(0) = ", FullSimplify[TrigReduce[QF - (E0^2 + B0^2)], Assumptions -> Element[{th, ph, et}, Reals]]];
Print["(a) entlang z (th=0): ", Simplify[QF /. th -> 0], " ; quer (th=Pi/2): ", Simplify[QF /. th -> Pi/2, Assumptions -> Element[{et, ph}, Reals]]];
Print["(a) Hessesche in (eta*d) bei 0: ", Simplify[D[QF /. th -> th, {et, 2}] /. et -> 0]];

(* ===== Praeambel P (Bloecke 2-5): r46-Funktionen und Detektorrahmen ===== *)
eta = DiagonalMatrix[{1, -1, -1, -1}];
gs = Table[Symbol["g" <> ToString[Min[i, j]] <> ToString[Max[i, j]]], {i, 0, 3}, {j, 0, 3}];
Riem[Pl_] := Table[-1/2 (Pl[[al]] Pl[[nu]] gs[[mu, be]] + Pl[[mu]] Pl[[be]] gs[[al, nu]] - Pl[[mu]] Pl[[nu]] gs[[al, be]] - Pl[[al]] Pl[[be]] gs[[mu, nu]]), {mu, 4}, {al, 4}, {nu, 4}, {be, 4}];
src[F_] := Table[With[{v = gs[[r, s]]}, If[r == s, 2 D[F, v], D[F, v]]], {r, 4}, {s, 4}];
fp[S1_, S2_] := Module[{S1l = eta . S1 . eta}, Total[Flatten[S1l S2]] - Tr[eta . S1] Tr[eta . S2]/3];
contr[R_, A_, u_] := Sum[A[[mu, nu]] u[[al]] u[[be]] R[[mu, al, nu, be]], {mu, 4}, {al, 4}, {nu, 4}, {be, 4}];
PiProj[u_, n_] := -Inverse[eta] + Outer[Times, u, u] - Outer[Times, n, n];
Lam[b_, d_] := Module[{g = 1/Sqrt[1 - b^2]}, Join[{Join[{g}, g b d]}, Table[Join[{g b d[[i]]}, Table[KroneckerDelta[i, j] + (g - 1) d[[i]] d[[j]], {j, 3}]], {i, 3}]]];
Rs = Riem[{0, k1, k2, k3}];          (* in Block 5: Riem[{0, k1, k2, 0}] *)
d2 = {Sin[t], 0, Cos[t]};
L2 = Lam[b, d2]; uu = L2 . {1, 0, 0, 0}; nn = L2 . {0, 0, 0, 1};
S = src[-contr[Rs, PiProj[uu, nn], uu]];

(* ===== Block 2: Kontrollen und modeweise (H122b/c, Stufe i) ===== *)
Print["Kontrolle Rahmen: u.u = ", Simplify[uu . eta . uu], ", n.n = ", Simplify[nn . eta . nn], ", u.n = ", Simplify[uu . eta . nn]];
Ngen = Simplify[fp[S, S], Assumptions -> 0 < b < 1];
N0 = Simplify[Ngen /. b -> 0];
Print["Kontrolle N(0) = ", Factor[N0]];
Print["Kontrolle r46.3 entlang, Reihe: ", Simplify[Normal[Series[Ngen /. t -> 0, {b, 0, 2}]]]];
dN = Together[Ngen - N0];
Print["(b,i) N - N0 entlang (t=0): ", Factor[Simplify[dN /. t -> 0]]];
Print["(b,i) N - N0 quer (t=Pi/2): ", Factor[Simplify[dN /. t -> Pi/2]]];
Print["(b,i) Mode k=(1,0,1), b=1/2: entlang ", N[dN /. {t -> 0, k1 -> 1, k2 -> 0, k3 -> 1, b -> 1/2}], " ; quer ", N[dN /. {t -> Pi/2, k1 -> 1, k2 -> 0, k3 -> 1, b -> 1/2}]];

(* ===== Block 3: isotropes Mittel (Stufe iii), |k| = 1; <k_i k_j k_l k_m> = (dd + dd + dd)/15 ===== *)
Ngen = Expand[fp[S, S]];
mon = CoefficientRules[Ngen, {k1, k2, k3}];
Print["Kontrolle: Grade der Monome in k: ", Union[Total /@ mon[[All, 1]]]];
iso4[{e1_, e2_, e3_}] := Which[Mod[e1, 2] == 1 || Mod[e2, 2] == 1 || Mod[e3, 2] == 1, 0, Max[e1, e2, e3] == 4, 3/15, True, 1/15];
Niso = Total[(iso4[#[[1]]] #[[2]]) & /@ mon];
dNiso = Factor[Simplify[TrigReduce[Niso - (Niso /. b -> 0)], Assumptions -> 0 < b < 1]];
Print["(b,iii) isotrop (K=1): N0 = ", Simplify[Niso /. b -> 0], " ; N - N0 = ", dNiso];
Print["(b,iii) entlang (t=0): ", Factor[Simplify[dNiso /. t -> 0]], " ; quer (t=Pi/2): ", Factor[Simplify[dNiso /. t -> Pi/2]]];
Print["(b,iii) b=1/2, t = 0, Pi/6, Pi/4, Pi/3, Pi/2: ", N[Table[dNiso /. b -> 1/2, {t, {0, Pi/6, Pi/4, Pi/3, Pi/2}}]]];

(* ===== Block 4: Azimutmittel (Stufe ii), k1 = Sqrt[a] Cos, k2 = Sqrt[a] Sin ===== *)
Ngen = Expand[fp[S, S]];
avg[e1_, e2_] := If[OddQ[e1] || OddQ[e2], 0, Integrate[Cos[x]^e1 Sin[x]^e2, {x, 0, 2 Pi}]/(2 Pi)];
mon2 = CoefficientRules[Ngen, {k1, k2}];
Naz = Total[(avg @@ #[[1]]) a^(Total[#[[1]]]/2) #[[2]] & /@ mon2];
dNaz = Factor[Simplify[TrigReduce[Naz - (Naz /. b -> 0)], Assumptions -> 0 < b < 1 && a > 0]];
Print["(b,ii) entlang (t=0): ", Factor[Simplify[dNaz /. t -> 0]], " ; quer (t=Pi/2): ", Factor[Simplify[dNaz /. t -> Pi/2]]];
Print["(b,ii) a=1, k3=1, b=1/2: entlang ", N[dNaz /. {t -> 0, a -> 1, k3 -> 1, b -> 1/2}], " ; quer ", N[dNaz /. {t -> Pi/2, a -> 1, k3 -> 1, b -> 1/2}]];
Print["(b,ii) a=1, k3=0, b=1/2: entlang ", N[dNaz /. {t -> 0, a -> 1, k3 -> 0, b -> 1/2}], " ; quer ", N[dNaz /. {t -> Pi/2, a -> 1, k3 -> 0, b -> 1/2}]];

(* ===== Block 5 (nachtraeglich, nicht in der Vorab-Notiz): Praeparation nur quer zur Achse, k3 = 0, Azimutmittel ===== *)
(* Praeambel mit Rs = Riem[{0, k1, k2, 0}] *)
Ngen = Expand[fp[S, S]];
mon2 = CoefficientRules[Ngen, {k1, k2}];
Naz = Total[(avg @@ #[[1]]) a^(Total[#[[1]]]/2) #[[2]] & /@ mon2];
f = Simplify[(Naz - (Naz /. b -> 0))/a^2 /. a -> 1];
Print["(Zusatz) k3 = 0, Azimutmittel, bei t = 0: ", Simplify[f /. t -> 0, Assumptions -> 0 < b < 1]];
Print["(Zusatz) Reihe in b bis b^2: ", Simplify[Normal[Series[f, {b, 0, 2}]]]];
tab = Table[N[f /. {t -> tt, b -> bb}], {tt, 0, Pi/2, Pi/16}, {bb, {1/10, 3/10, 1/2, 7/10, 9/10, 99/100}}];
Print["(Zusatz) Raster t = 0..Pi/2 (Schritt Pi/16) x b = 0.1,0.3,0.5,0.7,0.9,0.99: Minimum ", Min[tab], ", Minimum ohne t=0: ", Min[Rest[tab]], ", Zeile t=0: ", First[tab]];
