(* k375b: unabhaengige Kontrolle der Zentralwerte von k375 (H177) *)
w = Exp[2 Pi I/3];
kd[m_] := Module[{v = Sqrt[m], c, d}, c = v . Conjugate[w^{0, 1, 2}]; d = Mod[Arg[c], 2 Pi/3]; d = Min[d, 2 Pi/3 - d]; {Total[m]/Total[v]^2, d}];
up = {7.04*^-6, 3.56*^-3, 0.967}; dn = {1.54*^-5, 3.06*^-4, 1.630*^-2};
sc[m_, f_] := {m[[1]] f, m[[2]] f, m[[3]]};
k = 1/(16 Pi^2); tmax = Log[1.22*^19/91.1876];
sol = NDSolve[{g1'[t] == k 41/10 g1[t]^3, g2'[t] == -k 19/6 g2[t]^3, g3'[t] == -k 7 g3[t]^3,
    yt'[t] == k yt[t] (9/2 yt[t]^2 - 17/20 g1[t]^2 - 9/4 g2[t]^2 - 8 g3[t]^2), in'[t] == k 3/2 yt[t]^2,
    g1[0] == 0.4613, g2[0] == 0.6517, g3[0] == 1.2198, yt[0] == 0.967, in[0] == 0}, {g1, g2, g3, yt, in}, {t, 0, tmax}, PrecisionGoal -> 12][[1]];
imax = in[tmax] /. sol;
Print["I(M_Planck) = ", NumberForm[imax, 6], ", y_t(M_Planck) = ", NumberForm[yt[tmax] /. sol, 5]];
Do[Print["I = ", NumberForm[i, 5], ": {K_d, delta_d} = ", NumberForm[kd[sc[dn, Exp[i]]], 7], ", {K_u, delta_u} = ", NumberForm[kd[sc[up, Exp[-i]]], 7]], {i, {0, imax}}];
i2 = x /. FindRoot[kd[sc[dn, Exp[x]]][[2]] == 2 kd[sc[up, Exp[-x]]][[2]], {x, 0.03}];
Print["delta_d/delta_u = 2 bei I = ", NumberForm[i2, 5]];
Print["noetiges I: Down auf delta_e/2: ", x /. FindRoot[kd[sc[dn, Exp[x]]][[2]] == 0.2222220470731/2, {x, 0.2}], "; Up auf delta_e/4: ", x /. FindRoot[kd[sc[up, Exp[-x]]][[2]] == 0.2222220470731/4, {x, -0.1}]];
