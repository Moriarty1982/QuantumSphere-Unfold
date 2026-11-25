(* k300b: Gegenprobe zu k300 (Zahlen) und k301 (Winkelmittel, Schranken) in Wolfram Language.
   Aufruf: wolframscript -file k300b_gegenprobe.wl > k300b_out.txt *)
mW = 80.37; mZ = 91.19; mt = 172.6; mh = 125.2; v = 246.22;
SB = 3 (2 mW^4 + mZ^4); SF = 12 mt^4; pref = 1/(8 Pi^2 v^2);
Print["U1 m_s nur Eichfelder: ", Sqrt[pref SB], " GeV ; Faktor ", mh/Sqrt[pref SB], " ; mit Top m_s^2 = ", pref (SB - SF)];
miss = mh^2/pref - SB + SF;
Print["U2 fehlende Summe: ", miss, " ; Massen fuer n = 1, 2, 4, 8: ", (miss/#)^(1/4) & /@ {1, 2, 4, 8}];
Si = p u^2 + s (1 - u^2); Sg = p + 2 s;
m1 = Integrate[Si, {u, 0, 1}]; m2 = Integrate[Si^2, {u, 0, 1}];
Print["U3 <S_i> = ", InputForm[Simplify[m1]], " ; <S_i^2> = ", InputForm[Factor[m2]], " ; bestes T = ", InputForm[Simplify[Sg m1/m2]]];
Tq = Simplify[(Sg m1/m2) /. p -> q s];
Print["U4 T(q): ", InputForm[Tq], " ; Extremum ", InputForm[Solve[D[Tq, q] == 0 && q > 0, q]], " ; Grenzen q->0, q->Infinity, q=1: ", {Limit[Tq, q -> 0], Limit[Tq, q -> Infinity], Tq /. q -> 1}];
Print["U5 HC: T = ", With[{m = (1.8644 - 1)/(1.8644 + 1)}, ((1 + m^2)/(1 - m^2))^2]];
