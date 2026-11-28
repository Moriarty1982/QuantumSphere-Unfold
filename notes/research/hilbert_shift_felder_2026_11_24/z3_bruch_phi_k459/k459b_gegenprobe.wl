(* k459b (Erkundung, nicht blind): symbolische Gegenprobe der Leck-Energie als phi-Potential. Zwei Aufrufe. *)
En[p_] := wI Sin[3 (Pi/12 - p)]^2 + wR Sin[3 (Pi/6 - p)]^2;
Print["dE/dphi = ", Simplify[TrigReduce[D[En[p], p]]]];
Print["Gleiche Gewichte: stationaer in [-Pi/12, Pi/4): ", Solve[(D[En[p], p] /. {wI -> 1, wR -> 1}) == 0 && -Pi/12 <= p < Pi/4, p]];
Print["E''(Pi/8) bei (1,1): ", Simplify[D[En[p], {p, 2}] /. {wI -> 1, wR -> 1, p -> Pi/8}]];
Print["Gewichtsverhaeltnis fuer Stationaritaet bei x: ", N[-Tan[6 * 0.0395773], 10]];
Print["Abstand delta_Im zum Z3-Schluss (Grad): ", N[0.2222220470731/Degree, 8], "; |sin 3 delta_Im| = ", N[Abs[Sin[3*0.2222220470731]], 8]];
(* zweiter Aufruf *)
sol = Solve[-3 (Cos[6 p] + Sin[6 p]) == 0 && -Pi/12 <= p < Pi/4, p]; Print[N[p /. sol, 10], " ; Pi/8 = ", N[Pi/8, 10], ", -Pi/24 = ", N[-Pi/24, 10]]
