(* k203: H88 - unabhaengige Herleitung der W1-Feldgleichungen mit Wolfram (Connector, 5. November 2026).
   Konventionen wie Wirkung_W1_Dixon_U1.md: eta = diag(1,-1,-1,-1), sigmabar^a = (1, -sigma_i),
   D_mu = d_mu + (1/8) omega_mu ab (sigma^a sigmabar^b - sigma^b sigmabar^a) + i q A_mu J. *)

s0 = IdentityMatrix[2]; sig = {s0, PauliMatrix[1], PauliMatrix[2], PauliMatrix[3]};
sbar = {s0, -PauliMatrix[1], -PauliMatrix[2], -PauliMatrix[3]}; eta = DiagonalMatrix[{1, -1, -1, -1}]; et = {1, -1, -1, -1};

(* H88a: Erzeuger. Verhaeltnis zum Vektor-Erzeuger (eta^{bc} sbar^a - eta^{ac} sbar^b) *)
test[gen_] := Module[{res = {}},
  Do[Module[{S = gen[a, b], lhs, rhs},
     Do[lhs = ConjugateTranspose[S].sbar[[c]] + sbar[[c]].S;
       rhs = eta[[b, c]] sbar[[a]] - eta[[a, c]] sbar[[b]];
       AppendTo[res, If[Norm[Flatten[rhs]] == 0, If[Norm[Flatten[lhs]] == 0, "0=0", "lhs!=0"],
         Simplify[Total[Flatten[lhs*Conjugate[rhs]]]/Total[Flatten[rhs*Conjugate[rhs]]]]]], {c, 4}]], {a, 4}, {b, 4}];
  DeleteDuplicates[res]];
genW1[a_, b_] := 1/4 (sig[[a]].sbar[[b]] - sig[[b]].sbar[[a]]);
genAlt[a_, b_] := 1/4 (sbar[[a]].sig[[b]] - sbar[[b]].sig[[a]]);
{test[genW1], test[genAlt]}   (* Ergebnis: W1 {"0=0", -1} einheitlich; Alt {"0=0", 1, -1} nicht kovariant *)

(* H88b: Torsion aus den Definitionen, zwei Weyl-Spinoren, alle 24 Kontorsionskomponenten *)
sg[a_, b_] := 1/4 (sig[[a]].sbar[[b]] - sig[[b]].sbar[[a]]);
pairs = Subsets[Range[4], {2}];
vars = Flatten[Table[k[m, p[[1]], p[[2]]], {m, 4}, {p, pairs}]];
kl[m_, a_, b_] := Which[a == b, 0, a < b, k[m, a, b], True, -k[m, b, a]];
rsc = Sum[(et[[a]] kl[a, a, c] et[[c]] et[[b]] kl[b, c, b] - et[[a]] kl[b, a, c] et[[c]] et[[b]] kl[a, c, b]), {a, 4}, {b, 4}, {c, 4}];
op = I Sum[sbar[[m]].(1/2 Sum[kl[m, a, b] sg[a, b], {a, 4}, {b, 4}]), {m, 4}];
mk[p_, q_, r_, s_] := {{p + I q, r + I s}, {p - I q, r - I s}};
{ps1, pd1} = mk[p1, q1, r1, s1]; {ps2, pd2} = mk[p2, q2, r2, s2];
lint = ComplexExpand[Re[pd1.op.ps1 + pd2.op.ps2]];
ltot = rsc/(2 kap) + lint;
sol = Solve[Thread[D[ltot, {vars}] == 0], vars];
leff = Expand[ltot /. First[sol]];
jv = Table[ComplexExpand[pd1.sbar[[a]].ps1 + pd2.sbar[[a]].ps2], {a, 4}]; jj = Expand[Sum[et[[a]] jv[[a]]^2, {a, 4}]];
{Simplify[leff + 3/16 kap jj], Simplify[leff/jj]}   (* Ergebnis: {0, -3 kap/16} *)

(* H88c: Weyl-Gleichung per Variationsableitung (psi, psi^dagger unabhaengig; A konstant; c = Strom der uebrigen Zustaende) *)
Needs["VariationalMethods`"];
X = {t, x, y, z};
f = {f1[t, x, y, z], f2[t, x, y, z]}; g = {g1[t, x, y, z], g2[t, x, y, z]};
Av = {A0, A1, A2, A3}; cv = {c0, c1, c2, c3};
kin = 1/2 (g.(I Sum[sbar[[m]].D[f, X[[m]]], {m, 4}]) - (I Sum[D[g, X[[m]]].sbar[[m]], {m, 4}]).f);
gauge = -q J Sum[Av[[m]] g.sbar[[m]].f, {m, 4}];
jw = Table[g.sbar[[a]].f, {a, 4}];
four = -3/16 kap Sum[et[[a]] (jw[[a]] + cv[[a]])^2, {a, 4}];
lag = kin + gauge + four;
eqs = Table[VariationalMethods`VariationalD[lag, g[[i]], X], {i, 2}];
jlw = Table[et[[a]] (jw[[a]] + cv[[a]]), {a, 4}];
target = I Sum[sbar[[m]].D[f, X[[m]]], {m, 4}] - q J Sum[Av[[m]] sbar[[m]].f, {m, 4}] - 3 kap/8 Sum[jlw[[a]] sbar[[a]].f, {a, 4}];
Simplify[eqs - target]   (* Ergebnis: {0, 0} *)

(* H88d: Ward. Weyl-Gleichung i sbar.d psi = M psi; M hermitesch => d_mu j^mu = 0 auf Loesungen *)
fe = {u1 + I v1, u2 + I v2}; ge = {u1 - I v1, u2 - I v2};
jle = Table[et[[a]] (ComplexExpand[ge.sbar[[a]].fe] + cv[[a]]), {a, 4}];
M = q J Sum[Av[[m]] sbar[[m]], {m, 4}] + 3 kap/8 Sum[jle[[a]] sbar[[a]], {a, 4}];
ComplexExpand[M - ConjugateTranspose[M]] // Simplify   (* Ergebnis: Nullmatrix *)
