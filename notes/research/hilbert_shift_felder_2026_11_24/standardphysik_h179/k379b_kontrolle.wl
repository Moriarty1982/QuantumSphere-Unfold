(* k379b: unabhaengige Kontrolle der Zentralwerte von k379 (H179) *)
w = Exp[2 Pi I/3];
kd[m_] := Module[{v = Sqrt[m], c, d, k, rho}, c = v . Conjugate[w^{0, 1, 2}]; d = Mod[Arg[c], 2 Pi/3]; d = Min[d, 2 Pi/3 - d]; k = Total[m]/Total[v]^2; rho = Sqrt[3 k - 1]; {k, d, rho, ArcTan[rho]/Degree, ArcCos[-1/(Sqrt[2] rho)] - 2 Pi/3 - d}];
lep = {0.51099895*^-3, 105.6583755*^-3, 1776.93*^-3}; dn = {1.54*^-5, 3.06*^-4, 1.630*^-2};
gj = lep {3, 1/3, 1};
f[i_] := {dn[[1]] Exp[i], dn[[2]] Exp[i], dn[[3]]};
dr[i_] := Module[{q = f[i]}, {(3 q[[2]]/lep[[2]])/(q[[3]]/lep[[3]]), (q[[1]]/(3 lep[[1]]))/(q[[3]]/lep[[3]])}];
Print[N[{kd[gj], kd[f[0]], kd[f[0.12302]], dr[0], dr[0.12302]}, 7]]
