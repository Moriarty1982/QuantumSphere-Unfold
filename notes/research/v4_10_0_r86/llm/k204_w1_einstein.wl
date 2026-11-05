(* k204: H89 - Einstein-Gleichung von W1 in Teilen (Wolfram-Connector, 5./6. November 2026).
   Konventionen wie k203: eta = diag(1,-1,-1,-1), sigmabar^a = (1,-sigma_i), Sigma^{ab} = 1/4 (sigma^a sigmabar^b - sigma^b sigmabar^a),
   D_mu psi = d_mu psi + 1/2 omega_{mu ab} Sigma^{ab} psi (omega mit unteren Frame-Indizes, ohne eta-Faktoren). *)

et = {1, -1, -1, -1}; eta = DiagonalMatrix[et]; X = {t, x, y, z};
s0 = IdentityMatrix[2]; sig = {s0, PauliMatrix[1], PauliMatrix[2], PauliMatrix[3]}; sbar = {s0, -PauliMatrix[1], -PauliMatrix[2], -PauliMatrix[3]};

(* H89a: Vierbein-Variation von e*L4 bei festen psi *)
Ev = Array[E0, {4, 4}];
L4 = -3/16 kap (j0^2 - j1^2 - j2^2 - j3^2);
Tup = Table[-(1/Det[Ev]) D[Det[Ev] L4, E0[a, mu]], {mu, 4}, {a, 4}] /. Thread[Flatten[Ev] -> Flatten[IdentityMatrix[4]]];
Simplify[eta.Tup - 3/16 kap (j0^2 - j1^2 - j2^2 - j3^2) eta]   (* Ergebnis: Nullmatrix *)

(* H89b: homogener Zustand, zwei Weyl-Felder mit entgegengesetztem Spin *)
En = 3 kap n/8;
p1 = Sqrt[n/2] Exp[-I En t] {1, 0}; p2 = Sqrt[n/2] Exp[-I En t] {0, 1};
cj[v_] := ComplexExpand[Conjugate[v], {}, TargetFunctions -> {Re, Im}];
asm = {n > 0, kap > 0, t \[Element] Reals};
jv = Simplify[ComplexExpand[Table[cj[p1].sbar[[a]].p1 + cj[p2].sbar[[a]].p2, {a, 4}]], asm];
jl = et*jv;
eom = Simplify[Table[I sbar[[1]].D[p, t] - 3 kap/8 Sum[jl[[a]] sbar[[a]].p, {a, 4}], {p, {p1, p2}}], asm];
TbelR = Simplify[ComplexExpand[Table[Sum[Re[I/2 (cj[p].(et[[mu]] sbar[[mu]]).D[p, X[[nu]]] + cj[p].(et[[nu]] sbar[[nu]]).D[p, X[[mu]]])], {p, {p1, p2}}], {mu, 4}, {nu, 4}]], asm];
Lkin = Simplify[ComplexExpand[Sum[Re[cj[p].(I sbar[[1]].D[p, t])], {p, {p1, p2}}]], asm];
Ltot = Simplify[Lkin - 3/16 kap Sum[et[[a]] jv[[a]]^2, {a, 4}]];
{jv, eom, Lkin, Ltot, Simplify[TbelR - eta Ltot]}   (* Ergebnis: {n,0,0,0}, 0, 3 kap n^2/8, 3 kap n^2/16, diag(3 kap n^2/16) -> rho = p *)

(* H89c: Vierbein-Variation 1. Ordnung um flach mit torsionsfreiem Spinzusammenhang; Spinoren fest (Loesung eingesetzt) *)
Sg[a_, b_] := 1/4 (sig[[a]].sbar[[b]] - sig[[b]].sbar[[a]]);
Hs = Table[hh[a, m], {a, 4}, {m, 4}];             (* h^a_mu *)
hlD[a_, m_, n_] := et[[a]] dh[a, m, n];            (* d_n h_{a m} *)
pairs = Subsets[Range[4], {2}];
wv = Flatten[Table[w[m, p[[1]], p[[2]]], {m, 4}, {p, pairs}]];
wl[m_, a_, b_] := Which[a == b, 0, a < b, w[m, a, b], True, -w[m, b, a]];
eqs = Flatten[Table[hlD[a, nu, mu] - hlD[a, mu, nu] + wl[mu, a, nu] - wl[nu, a, mu] == 0, {a, 4}, {mu, 4}, {nu, mu + 1, 4}]];
wsol = First@Solve[eqs, wv];
Om[m_] := 1/2 Sum[(wl[m, a, b] /. wsol) Sg[a, b], {a, 4}, {b, 4}];
OmD[m_] := ComplexExpand[ConjugateTranspose[Om[m]]];
ph[k_] := k[[1]] t - k[[2]] x - k[[3]] y - k[[4]] z;
uvec[k_] := First@NullSpace[Sum[sbar[[m]] (I D[Exp[-I ph[k]], X[[m]]]/Exp[-I ph[k]]), {m, 4}]];
k1 = {1, 0, 0, 1}; k2 = {2, 2, 0, 0};
f = uvec[k1] Exp[-I ph[k1]] + 3 uvec[k2] Exp[-I ph[k2]];
g = ComplexExpand[Conjugate[f]];
Einv = IdentityMatrix[4] - eps Hs; dete = 1 + eps Tr[Hs];
lag = dete 1/2 Sum[Einv[[m, a]] (I g.sbar[[a]].(D[f, X[[m]]] + eps Om[m].f) - I (D[g, X[[m]]] + eps g.OmD[m]).sbar[[a]].f), {a, 4}, {m, 4}];
L1 = Coefficient[Expand[lag], eps, 1];
V = Table[D[L1, hh[a, m]] - Sum[D[D[L1, dh[a, m, n]], X[[n]]], {n, 4}], {a, 4}, {m, 4}];
Vl = Table[V[[a, m]] et[[m]], {a, 4}, {m, 4}];
Tb = Table[I/4 (g.(et[[mu]] sbar[[mu]]).D[f, X[[nu]]] + g.(et[[nu]] sbar[[nu]]).D[f, X[[mu]]] - D[g, X[[nu]]].(et[[mu]] sbar[[mu]]).f - D[g, X[[mu]]].(et[[nu]] sbar[[nu]]).f), {mu, 4}, {nu, 4}];
pts = {{t -> 0.3, x -> 0.7, y -> -0.2, z -> 1.1}, {t -> -1.3, x -> 0.1, y -> 2.2, z -> -0.4}};
Table[{Max[Abs[N[(Vl - Tb) /. p]]], Max[Abs[N[(Vl + Tb) /. p]]], Max[Abs[N[(Vl - Transpose[Vl]) /. p]]], Max[Abs[N[Tb /. p]]]}, {p, pts}]
(* Ergebnis: {{92., 7e-15, 0., 46.}, {68.2, 5e-15, 0., 34.1}} -> Vl = -Tb, symmetrisch *)
