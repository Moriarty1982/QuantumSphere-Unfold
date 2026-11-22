(* Warum koppeln H_0i nicht? Methoden-Notiz Commit 0e57242a. Erkundung, teilweise nicht blind (K1, K4). *)
(* Konventionen wie r39 (single_tensor.wl): d_t -> -I w, d_i -> I k_i, x = w^2, a = k1^2 + k2^2; Achse senkrecht zu (t, x, y).
   J_ab = D_a D_b - c eta_ab Box, eta = diag(1, -1, -1). Austauschzaehler als geordnete Doppelsumme; r39: N(c, w). *)
etaS = DiagonalMatrix[{1, -1, -1}];
Jof[wv_, cc_] := Module[{Dv = {-I wv, I k1, I k2}, box},
   box = Sum[etaS[[i, i]] Dv[[i]]^2, {i, 3}];
   Table[Dv[[i]] Dv[[j]] - cc etaS[[i, j]] box, {i, 3}, {j, 3}]];
pol = {k1 -> Sqrt[a] Cos[ph], k2 -> Sqrt[a] Sin[ph]};
cl[e_] := Simplify[TrigReduce[Expand[e /. pol /. w -> Sqrt[x]]], {x >= 0, a >= 0}];
Nm = 2/3 (x^2 - a x + a^2);
propTo[e_, vars_] := Module[{eqs = DeleteCases[Thread[Flatten[CoefficientList[Expand[e - lam Nm], {x, a}]] == 0], True]},
   Solve[eqs, Join[vars, {lam}]]];
J = Jof[w, c];
Print["(0) r39-Basis: N(c, w) = ", Collect[cl[Sum[If[i == 1 && j > 1 || j == 1 && i > 1, w0, 1] J[[i, j]]^2, {i, 3}, {j, 3}]], {x, a}]];

(* ---------- K1: Fierz-Pauli in D = 3 ---------- *)
Dv = {-I w, I k1, I k2};
Dup = etaS . Dv;                       (* D^a *)
Pup = Inverse[etaS] + Outer[Times, Dup, Dup]/m2;   (* P^ab = eta^ab - p^a p^b/m^2, p_a = I D_a *)
Jup = Inverse[etaS] . J . Inverse[etaS];
JPJ = Sum[J[[a1, b1]] (1/2 (Pup[[a1, c1]] Pup[[b1, d1]] + Pup[[a1, d1]] Pup[[b1, c1]]) - 1/2 Pup[[a1, b1]] Pup[[c1, d1]]) J[[c1, d1]],
   {a1, 3}, {b1, 3}, {c1, 3}, {d1, 3}];
k1n = cl[JPJ];
Print["(K1) Fierz-Pauli-Zaehler J.Pi.J (D = 3, Pol bei x = a + m^2): ", Factor[k1n]];
Print["     bei c = 1: ", Simplify[k1n /. c -> 1], ";  am Pol x = a + m^2: ", Factor[Simplify[k1n /. x -> a + m2]]];
Print["     proportional zu N_m fuer ein c (m^2 als freier Parameter)? ",
  Module[{e = Numerator[Together[k1n]], dd = Denominator[Together[k1n]]},
    Solve[DeleteCases[Thread[Flatten[CoefficientList[Expand[e - lam Nm dd], {x, a, m2}]] == 0], True], {c, lam}]]];

(* ---------- K2: H_0i als Hilfsfelder ueber E_ij ---------- *)
(* Variablen y = (h00, h01, h02, h11, h12, h22), konjugiert yb. Geordnete Summen: Vielfachheit 2 fuer Nichtdiagonale. *)
yv = {h00, h01, h02, h11, h12, h22}; ybv = {b00, b01, b02, b11, b12, b22};
Hm[v_] := {{v[[1]], v[[2]], v[[3]]}, {v[[2]], v[[4]], v[[5]]}, {v[[3]], v[[5]], v[[6]]}};
Hy = Hm[yv]; Hb = Hm[ybv];
kv = {k1, k2};
dd = m2 + r q - x;                      (* d_m; q = |k|^2 einschliesslich k_z *)
Eij = Table[-I w Hy[[i + 1, j + 1]] - I kv[[i]] Hy[[1, j + 1]] - I kv[[j]] Hy[[1, i + 1]], {i, 2}, {j, 2}];
Ebij = Table[I w Hb[[i + 1, j + 1]] + I kv[[i]] Hb[[1, j + 1]] + I kv[[j]] Hb[[1, i + 1]], {i, 2}, {j, 2}];
Lkin = (1/2 (x - r q - m2) h00 b00 + 1/2 Sum[Eij[[i, j]] Ebij[[i, j]], {i, 2}, {j, 2}]
   - 1/2 (r q + m2) Sum[Hy[[i + 1, j + 1]] Hb[[i + 1, j + 1]], {i, 2}, {j, 2}] - 1/2 mu (2 h01 b01 + 2 h02 b02));
Mk = -2 Table[D[Lkin, ybv[[i]], yv[[j]]], {i, 6}, {j, 6}] /. w -> Sqrt[x];
mult = {1, 2, 2, 1, 2, 1}; sgn = {1, -1, -1, 1, 1, 1};
Jy = {J[[1, 1]], J[[1, 2]], J[[1, 3]], J[[2, 2]], J[[2, 3]], J[[3, 3]]};
Vk[cc_, wgt_] := mult sgn (Jy /. c -> cc) {1, wgt, wgt, 1, 1, 1};
exK2[cc_, wgt_] := Module[{mm = Mk /. k2 -> 0, vv = Vk[cc, wgt] /. k2 -> 0},
   Simplify[(vv /. k1 -> Sqrt[a] /. w -> Sqrt[x]) . Inverse[mm /. k1 -> Sqrt[a]] . (vv /. k1 -> Sqrt[a] /. w -> Sqrt[x])]];
base0 = Simplify[cl[Sum[If[i == 1 && j > 1 || j == 1 && i > 1, 0, 1] (J /. c -> 1)[[i, j]]^2, {i, 3}, {j, 3}]]/dd];
e2 = exK2[1, 1];
Print["(K2) Austausch mit E_ij, Steifigkeit mu, c = 1: ", Factor[e2]];
Print["     Differenz zum Ziel 3 N_m/d_m (w = 0 aus r39): ", Factor[Simplify[e2 - base0]]];
Print["     Grenzwert mu -> Infinity: ", Simplify[Limit[e2, mu -> Infinity] - base0]];
Print["     mu = 0 (Eichinvarianz der E-Struktur): ", Factor[Simplify[e2 /. mu -> 0]]];
Print["     Pole in x (Nenner): ", Factor[Denominator[Together[e2]]]];
Print["     mu, fuer das die Differenz identisch verschwindet: ",
  Solve[DeleteCases[Thread[Flatten[CoefficientList[Numerator[Together[e2 - base0]], {x, a, q}]] == 0], True], mu]];

(* ---------- K3: Zeitumkehr-Paritaet der Vertizes ---------- *)
Jr = Jof[-w, c];
Print["(K3) J_ab(-w) - J_ab(w) = ", Simplify[Jr - J], ";  J_ab(-w) + J_ab(w) fuer 0i: ", Simplify[{Jr[[1, 2]] + J[[1, 2]], Jr[[1, 3]] + J[[1, 3]]}]];

(* ---------- K4: Mittel ueber die relative Zeitorientierung ---------- *)
Nsame = cl[Sum[J[[i, j]] J[[i, j]], {i, 3}, {j, 3}]];
Nrev = cl[Sum[J[[i, j]] Jr[[i, j]], {i, 3}, {j, 3}]];
Np = Collect[Expand[p Nsame + (1 - p) Nrev], {x, a}];
Print["(K4) gleiche Orientierung N_same = ", Collect[Nsame, {x, a}], ";  umgekehrt N_rev = ", Collect[Nrev, {x, a}]];
Print["     Mittel p N_same + (1-p) N_rev = ", Np];
Print["     gleich N(c, w = 2p - 1) aus r39? ",
  Simplify[Np - cl[Sum[If[i == 1 && j > 1 || j == 1 && i > 1, 2 p - 1, 1] J[[i, j]]^2, {i, 3}, {j, 3}]]] == 0];
Print["     N = lam N_m: ", propTo[Np, {c, p}]];
Print["     bei c = 1: ", propTo[Np /. c -> 1, {p}]];
Print["     Lorentz-Fall p = 0 (umgekehrt), c = 1: ", Factor[Np /. {c -> 1, p -> 0}], ";  feste Orientierung p = 1: ", Factor[Np /. {c -> 1, p -> 1}]];
Jt = Jof[I w, c];   (* Gegenprobe: Tachyon-Abbildung w -> I w an einem Vertex *)
Ntach = Collect[cl[Sum[J[[i, j]] Jt[[i, j]], {i, 3}, {j, 3}]], {x, a}];
Print["     Gegenprobe Tachyon-Abbildung an einem Vertex: N = ", Ntach, ";  reell? ", Simplify[Im[Ntach /. {x -> 2, a -> 1, c -> 1}] == 0]];
Print["     Mittel Tachyon mit gleicher Orientierung, c = 1: ", Collect[Expand[(Nsame + Ntach)/2 /. c -> 1], {x, a}]];
