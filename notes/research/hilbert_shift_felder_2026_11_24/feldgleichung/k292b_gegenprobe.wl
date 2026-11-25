(* k292b (Erkundung, nicht blind): unabhaengige Gegenprobe zu k292 in Wolfram Language, Quaternionen als 2x2-Matrizen. *)
f[z_, zb_] := a z + b zb;
Print["X1 mu, K: ", {D[f[z, zb], zb]/D[f[z, zb], z], Simplify[(1 + b/a)/(1 - b/a)], Simplify[(1 + (g - 1)/(g + 1))/(1 - (g - 1)/(g + 1))]}];
psi = {(a + b) Cos[w t], (a - b) Sin[w t]};
Print["X2 N - (a^2+b^2+2ab Cos[2wt]): ", Simplify[psi . psi - (a^2 + b^2 + 2 a b Cos[2 w t])], ", Zeitmittel: ", Simplify[w/(2 Pi) Integrate[psi . psi, {t, 0, 2 Pi/w}], w > 0]];
e = {(a + b) Cos[th[t]], (a - b) Sin[th[t]]}; L = 1/2 D[e, t] . D[e, t];
el = D[L, th[t]] - D[D[L, th'[t]], t];
Print["X3 Euler-Lagrange-Rest bei theta = w t: ", Simplify[el /. {th''[t] -> 0, th'[t] -> w, th[t] -> w t}]];
s = PauliMatrix /@ {1, 2, 3}; qi = I s[[3]]; qj = I s[[2]]; ex[x_] := Cos[x] IdentityMatrix[2] + Sin[x] qi;
p2 = a ex[w t] + b qj . ex[-w t];
Print["X4 psi - e^{iwt}(a + b j): ", Simplify[p2 - ex[w t] . (a IdentityMatrix[2] + b qj)], ", N = ", Simplify[Det[p2]]];
ip[x_, y_] := Simplify[ComplexExpand[Re[Tr[ConjugateTranspose[x] . y]]/2]];
Print["X5 psi' - w i psi: ", Simplify[D[p2, t] - w qi . p2], ", Ladung links: ", ip[D[p2, t], qi . p2], ", rechts: ", Factor[ip[D[p2, t], p2 . qi]]];
