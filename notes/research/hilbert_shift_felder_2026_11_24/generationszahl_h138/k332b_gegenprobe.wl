(* k332b (H149): unabhaengige Gegenprobe in Wolfram Language zu k332_theta_delta.py *)
(* H149a *)
z = Cos[t] + I Sin[t];
Print["Re Psi^2: ", Simplify[ComplexExpand[Re[z^2]]]];
Print["J(Psi) = U conj(Psi): ", ComplexExpand[I Conjugate[z]], "  ; J^2 - 1: ", Simplify[ComplexExpand[I Conjugate[I Conjugate[z]] - z]]];
Print["Fixpunkt: ", Solve[Cos[t] == Sin[t] && 0 <= t < Pi, t]];
(* H149b *)
psi = {Cos[t], Sin[t] Cos[d], Sin[t] Sin[d]};
nn = Simplify[psi . psi]; re = psi[[1]];
v = Sum[c[p, q] nn^p re^q, {p, 0, 4}, {q, 0, 4 - p}];
Print["dV/ddelta fuer V(N, Re): ", Simplify[D[v, d]]];
(* H149c *)
v4 = m0/2 Cos[t]^2 + m1/2 Sin[t]^2 + a Cos[t]^4 + b Cos[t]^2 Sin[t]^2 + cc Sin[t]^4;
Print["dV/dtheta bei pi/4: ", Simplify[D[v4, t] /. t -> Pi/4]];
vJ = v4 /. {m1 -> m0, cc -> a};
Print["mit Tausch: ", Simplify[D[vJ, t] /. t -> Pi/4], " ; zweite Ableitung: ", Simplify[D[vJ, {t, 2}] /. t -> Pi/4]];
Print["k291 (m0 = 0): V - konst = ", Simplify[TrigReduce[(vJ /. m0 -> 0) - (vJ /. {m0 -> 0, t -> Pi/8})]]];
Print["HC: K(arctan beta^2) = ", N[1/(3 Cos[ArcTan[0.5493^2]]^2), 8], " ; K(arctan beta^-2) = ", N[1/(3 Cos[ArcTan[0.5493^-2]]^2), 8]];
(* H149d *)
ck = Table[Cos[t]/Sqrt[3] + Sqrt[2/3] Sin[t] Cos[d - 2 Pi k/3], {k, 0, 2}];
Print["Tr W: ", Simplify[Total[ck]], " ; Tr W^2: ", Simplify[TrigReduce[Total[ck^2]]]];
nw = Simplify[TrigReduce[Times @@ ck] /. t -> Pi/4];
Print["N(W) bei theta = pi/4: ", nw];
Print["N(W) = 0 bei: ", Reduce[nw == 0 && 0 <= d <= Pi/3, d]];
Print["Massen bei delta = pi/12: ", Simplify[(ck /. {t -> Pi/4, d -> Pi/12})^2]];
(* H149e und nicht gewertet *)
ml = {0.51099895, 105.6583755, 1776.93};
amp[dd_?NumericQ] := Sort[(ck /. {t -> Pi/4, d -> dd})^2];
ratio[dd_?NumericQ] := amp[dd][[2]]/amp[dd][[1]];
dfit = dd /. FindRoot[ratio[dd] == ml[[2]]/ml[[1]], {dd, 0.22}];
Print["delta_fit: ", N[dfit, 10]];
Print["Kandidaten relativ: ", N[{Pi/12, ArcTanh[0.5493]/3, 0.237533, ArcTan[0.5493^2]}/dfit - 1, 4]];
Print["CT-002 relativ: ", N[(Pi/12 - 0.237533/6)/dfit - 1, 3], " ; arccos(pi/4)/3 = ", N[ArcCos[Pi/4]/3, 8], " ; -4 cos(2/3) = ", N[-4 Cos[2/3], 8]];
