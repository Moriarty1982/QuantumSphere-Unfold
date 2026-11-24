(* k253b (Erkundung, nicht blind): HS(0)->HS(1)->HS(2) als Feldkonfigurationen, exakt.
   Ausgefuehrt ueber den Wolfram-MCP-Kern am 24.11.2026; Ausgabe in k253b_out.txt *)
$Assumptions = {a > 0, b >= 0, w > 0, th \[Element] Reals, t \[Element] Reals};
psi = a Exp[I w t] + b Exp[-I w t];
x = ComplexExpand[Re[psi]]; y = ComplexExpand[Im[psi]];
area = Simplify[1/2 Integrate[x D[y, t] - y D[x, t], {t, 0, 2 Pi/w}]];
Print["HS(1) umlaufene Flaeche A = ", area];
Lz = Simplify[x D[y, t] - y D[x, t]];
Print["HS(1) Drehimpuls/U(1)-Ladung L = ", Lz];
Print["HS(1) Grenzfall b=a (HS(0), Linie): A = ", area /. b -> a, ", Bahn = ", Simplify[{x, y} /. b -> a]];
Print["Bewegungsgleichung psi'' + w^2 psi = ", Simplify[D[psi, {t, 2}] + w^2 psi]];
Print["Zeitumkehr: psi(-t) - (b e^{iwt} + a e^{-iwt}) = ", Simplify[(psi /. t -> -t) - (b Exp[I w t] + a Exp[-I w t])]];
chi[ph_] := {Cos[th/2], Exp[I ph] Sin[th/2]};
conn = Simplify[ComplexExpand[Im[Conjugate[chi[ph]] . D[chi[ph], ph]]]];
hol = Simplify[Integrate[conn, {ph, 0, 2 Pi}]];
Print["HS(2) Berry-Phase um Breitenkreis: gamma = -", hol, " ; Raumwinkel Omega = ", Simplify[2 Pi (1 - Cos[th])], " ; gamma/Omega = ", Simplify[-hol/(2 Pi (1 - Cos[th]))]];
cd[x_List, y_List] := If[Length[x] == 1, x y, Module[{h = Length[x]/2, a1, b1, c1, d1, cj},
   cj[v_] := Prepend[-Rest[v], First[v]];
   a1 = x[[;; h]]; b1 = x[[h + 1 ;;]]; c1 = y[[;; h]]; d1 = y[[h + 1 ;;]];
   Join[cd[a1, c1] - cd[cj[d1], b1], cd[d1, a1] + cd[b1, cj[c1]]]]];
derdim[n_] := Module[{N0 = 2^n, E0, D0, eqs, vars},
  E0 = IdentityMatrix[N0]; D0 = Array[d, {N0, N0}]; vars = Flatten[D0];
  eqs = Flatten[Table[D0 . cd[E0[[i]], E0[[j]]] - (cd[D0 . E0[[i]], E0[[j]]] + cd[E0[[i]], D0 . E0[[j]]]), {i, N0}, {j, N0}]];
  Length[vars] - MatrixRank[Normal[CoefficientArrays[eqs, vars][[2]]]]];
Print["Wolfram dim Der(A_n), n=0..4: ", Table[derdim[n], {n, 0, 4}]];
