(* k385b (Test H182, Wolfram exakt): Gegenprobe zu Teil a und zum Zusatz. Eigene Cayley-Dickson-Multiplikation. Ausgabe k385b_out.txt. *)
cj[x_] := Prepend[-Rest[x], First[x]];
ml[x_, y_] := If[Length[x] == 1, x y, Module[{h = Length[x]/2, a, b, c, d},
   a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]];
   Join[ml[a, c] - ml[cj[d], b], ml[d, a] + ml[b, cj[c]]]]];
ee = IdentityMatrix[8]; u = ee[[8]];
lu = Transpose[Table[ml[u, ee[[j]]], {j, 8}]]; ru = Transpose[Table[ml[ee[[j]], u], {j, 8}]];
q0 = ee/2 - I/6 lu - I/3 ru; hodd = q0 - ee/2;
jm = Transpose[Table[ml[u, cj[ee[[i]]]], {i, 8}]]; km = DiagonalMatrix[Join[{1}, ConstantArray[-1, 7]]];
pc = DiagonalMatrix[{0, 1, 1, 1, 1, 1, 1, 0}]; ps = DiagonalMatrix[{1, 0, 0, 0, 0, 0, 0, 1}];
hc = pc . hodd . pc; hs = ps . hodd . ps;
Print["hodd hermitesch: ", ConjugateTranspose[hodd] == hodd, "; Conjugate[Q0] == 1 - Q0: ", Conjugate[q0] == ee - q0];
Print["Farbblock: J^T hc J == hc: ", Transpose[jm] . hc . jm == hc, "; farblos: J^T hs J == -hs: ", Transpose[jm] . hs . jm == -hs];
Print["Konjugation: K hc K == hc: ", km . hc . km == hc, "; K hs K == -hs: ", km . hs . km == -hs];
Print["Eigenwerte von hc auf dem Farbblock: ", Sort[Eigenvalues[hc[[2 ;; 7, 2 ;; 7]]]], "; von hs auf {1, U}: ", Sort[Eigenvalues[hs[[{1, 8}, {1, 8}]]]]];
(* Quarkfeld als Ladungs-Eigenzustand: n = (e1 -+ i U e1)/Sqrt[2] *)
c1 = ee[[2]]; uc = ml[u, c1];
Do[n = (c1 + sg I uc)/Sqrt[2]; psi = Cos[th] ee[[1]] + Sin[th] n;
  Print["Vorzeichen ", sg, ": Ladung von n = ", Simplify[Conjugate[n] . q0 . n], "; Psi^dagger hc Psi = ", Simplify[Conjugate[psi] . hc . psi, th \[Element] Reals],
   "; |c|^2 = ", Simplify[Conjugate[psi] . pc . psi, th \[Element] Reals]], {sg, {1, -1}}];
(* Zusatz: bilineare ladungsungerade Form im Farblosen, b(Psi) = Im(x0^2 + xU^2) *)
bf[v_] := Im[v[[1]]^2 + v[[8]]^2];
x = Array[a, 8] + I Array[b, 8]; asm = Element[Join[Array[a, 8], Array[b, 8]], Reals];
Print["b invariant unter J: ", Simplify[ComplexExpand[bf[jm . x] - bf[x]]] == 0, "; unter K: ", Simplify[ComplexExpand[bf[km . x] - bf[x]]] == 0,
  "; ungerade unter komplexer Konjugation: ", Simplify[ComplexExpand[bf[Conjugate[x]] + bf[x]]] == 0];
Print["b auf den Ladungs-Eigenzustaenden (1 -+ i U)/Sqrt[2]: ", bf[(ee[[1]] - I u)/Sqrt[2]], ", ", bf[(ee[[1]] + I u)/Sqrt[2]]];
Print["J (1 - i U)/Sqrt[2] == -i (1 + i U)/Sqrt[2]: ", jm . ((ee[[1]] - I u)/Sqrt[2]) == -I (ee[[1]] + I u)/Sqrt[2]];
(* Leptonfeld: die Invarianten s = |x0|^2 + |xU|^2, p = |x0|^2 |xU|^2, r = Re(x0^2 + xU^2), m2 = |x0^2 + xU^2|^2 bei 45 Grad *)
lep = {Cos[th], Sin[th]};
invs = {lep[[1]]^2 + lep[[2]]^2, lep[[1]]^2 lep[[2]]^2, (lep[[1]]^2 + lep[[2]]^2)^2};
Print["Leptonfeld: Ableitungen von s, p, |x0^2 + xU^2|^2 bei 45 Grad: ", Simplify[D[invs, th] /. th -> Pi/4]];
(* Stationaerer Winkel der Quarks: V = (A -+ C) t + (B -+ D) t^2 *)
Print["t* = ", Solve[D[(A + s C) t + (B + s D) t^2, t] == 0, t]];
td = Sin[48.114 Degree]^2; tu = Sin[52.207 Degree]^2;
Print["Daten: a_d/b_d = ", -2 td, ", a_u/b_u = ", -2 tu, "; mit D = 0: A/B = ", -(td + tu), ", C/B = ", -(tu - td)];
