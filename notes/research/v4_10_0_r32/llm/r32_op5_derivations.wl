(* Pruefung der Herleitungen in Anhang B des deutschen Preprints (Gleichungen (39)-(50), Abschnitt 4.4). Exakt, Wolfram Language. *)
X = {x, y, z};
grad[f_] := D[f, {X}];
div[v_] := Sum[D[v[[i]], X[[i]]], {i, 3}];
lap[f_] := Sum[D[f, X[[i]], X[[i]]], {i, 3}];
eps[u_] := (D[u, {X}] + Transpose[D[u, {X}]])/2;
sig[u_, l_, m_] := l Tr[eps[u]] IdentityMatrix[3] + 2 m eps[u];
Lop[u_, l_, m_] := Table[Sum[D[sig[u, l, m][[i, j]], X[[j]]], {j, 3}], {i, 3}];

(* B.1: L(grad S) = K_L grad(Lap S) und div L b = K_L Lap^2 S *)
b1 = Simplify[Lop[grad[S[x, y, z]], l, m] - (l + 2 m) grad[lap[S[x, y, z]]]];
b1b = Simplify[div[Lop[grad[S[x, y, z]], l, m]] - (l + 2 m) lap[lap[S[x, y, z]]]];
Print["(B.1) L(grad S) - K_L grad Lap S = 0: ", b1 === {0, 0, 0}, ";  div L grad S - K_L Lap^2 S = 0: ", b1b === 0];

(* B.3: Lap_perp xi^j = 4 j^2 xi^(j-1)/R^2 mit xi = r^2/R^2 (radial, zwei Dimensionen) *)
lapr[f_] := D[f, {r, 2}] + D[f, r]/r;
xi = r^2/R^2;
Print["(B.3) Lap_perp xi^j: ", Table[Simplify[lapr[xi^j]/(xi^(j - 1)/R^2)], {j, 1, 6}], "  (erwartet 4 j^2 = 4, 16, 36, 64, 100, 144)"];
poly = xi^5 - k xi^6;
l3 = Simplify[Nest[lapr, poly, 3]];
Print["      Lap_perp^3 (xi^5 - k xi^6) = ", Factor[l3], ";  gleich 230400 (xi^2 - 4 k xi^3)/R^6: ", Simplify[l3 - 230400 (xi^2 - 4 k xi^3)/R^6] === 0];
Print["      Lap_perp xi^2 = ", Simplify[lapr[xi^2]], " (also 16 xi/R^2)"];

(* B.4: Gezeitenkontrast auf der Achse, delta f = Lap_perp delta H / m^2, delta H = -A p (xi^2 - 4 k xi^3) im flachen Kern *)
xx = (x^2 + y^2)/R^2;
dH = -A p (xx^2 - 4 k xx^3);
df = (D[dH, {x, 2}] + D[dH, {y, 2}])/m^2;
contr = -1/2 (D[df, {x, 2}] /. {x -> 0, y -> 0});
Print["(B.4) -1/2 d_e^2 delta f auf der Achse = ", Simplify[contr], "  (erwartet 16 A p/(m^2 R^4))"];

(* B.5: Azimutalmittel von d_e^2 delta f bei Radius r, im Verhaeltnis zum Achsenwert *)
avg = Simplify[Integrate[(D[df, {x, 2}] /. {x -> rr Cos[ph], y -> rr Sin[ph]}), {ph, 0, 2 Pi}]/(2 Pi)];
axis = Simplify[D[df, {x, 2}] /. {x -> 0, y -> 0}];
Print["(B.5) Azimutalmittel / Achsenwert = ", Simplify[Expand[avg/axis] /. rr -> R Sqrt[s]], "  (erwartet 1 - 36 k s mit s = xi)"];

(* B.6: planare Kontrolle mit K_m(z) = m/2 Exp[-m |z|] und Traeger von drho in [0, L]; Betrag stueckweise aufgeloest *)
rho[zz_] := zz^2 (L - zz)^2;   (* Beispielprofil mit Traeger [0, L]; die Identitaet ist linear in drho *)
fin[zz_] := Integrate[m/2 Exp[-m (zz - zp)] rho[zp], {zp, 0, zz}] + Integrate[m/2 Exp[-m (zp - zz)] rho[zp], {zp, zz, L}];  (* 0 <= z <= L *)
fleft[zz_] := Integrate[m/2 Exp[-m (zp - zz)] rho[zp], {zp, 0, L}];   (* z <= 0 *)
fright[zz_] := Integrate[m/2 Exp[-m (zz - zp)] rho[zp], {zp, 0, L}];  (* z >= L *)
lhs = Integrate[fin[zz], {zz, 0, L}];
rhs = Integrate[rho[zz], {zz, 0, L}] - (fin[0] + fin[L])/m;
Print["(B.6) int_0^L f - (int drho - (f(0)+f(L))/m) = ", Simplify[lhs - rhs]];
Print["      Auslaeufer: f(z)/f(0) fuer z < 0 = ", Simplify[fleft[zz]/fleft[0]], ";  Stetigkeit f(0): ", Simplify[fleft[0] - fin[0]], ", f(L): ", Simplify[fright[L] - fin[L]]];
Print["      Gesamtintegral: int f ueber R - int drho = ", Simplify[Integrate[fleft[zz], {zz, -Infinity, 0}, Assumptions -> m > 0] + lhs + Integrate[fright[zz], {zz, L, Infinity}, Assumptions -> m > 0] - Integrate[rho[zz], {zz, 0, L}], Assumptions -> m > 0]];

(* B.7: Energiebilanz mit innerer Paarfeder, eindimensionaler Spezialfall (Spannung = Modul * Ableitung) *)
uu = u[t, s]; ww = w[t, s]; dd = d[t, s];
RF = uu - ww - dd;
emech = rho1/2 D[uu, t]^2 + rho2/2 D[ww, t]^2 + K/2 D[uu, s]^2 + cs K/2 D[ww, s]^2 + kk/2 RF^2;
eqs = {D[uu, {t, 2}] -> (K D[uu, {s, 2}] - kk RF)/rho1, D[ww, {t, 2}] -> (cs K D[ww, {s, 2}] + kk RF)/rho2};
flux = K D[uu, s] D[uu, t] + cs K D[ww, s] D[ww, t];
pswitch = -kk RF D[dd, t];
Print["(B.7) d_t e_mech - (d_s F + P_Schalt) auf den Bewegungsgleichungen = ", Simplify[(D[emech, t] /. eqs) - (D[flux, s] + pswitch)]];

(* B.8: Saint-Venant-Kirchhoff, zweite Ordnung des Piola-Tensors bei symmetrischem H *)
Hs = Array[h, {3, 3}]; Hs = (Hs + Transpose[Hs])/2;
C4[e_] := lam Tr[e] IdentityMatrix[3] + 2 mu e;
Pfull[Hm_] := (IdentityMatrix[3] + Hm).C4[(Hm + Transpose[Hm] + Transpose[Hm].Hm)/2];
second = Simplify[Coefficient[Expand[Pfull[ep Hs]], ep, 2]];
NH = lam/2 Tr[Hs.Hs] IdentityMatrix[3] + 3 mu Hs.Hs + lam Tr[Hs] Hs;
Print["(B.8) zweite Ordnung von P bei Verschiebungsgradient eps H gleich N(H): ", Simplify[second - NH] === Table[0, {3}, {3}]];
(* Zweite Komponente: Steifigkeit cs, H_w = -H/cs; quadratischer Anteil cs N(-H/cs) = N(H)/cs *)
Print["      cs N(-H/cs) - N(H)/cs = 0: ", Simplify[cs (NH /. h[i_, j_] :> -h[i, j]/cs) - NH/cs] === Table[0, {3}, {3}]];
