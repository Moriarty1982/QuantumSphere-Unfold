(* k441b: Wolfram-Gegenprobe zu H227 (Bilanz der Leptonenmassen), unabhaengig von k441 (FindRoot/Brent statt scipy).
   Zwei Auswertungen ueber den Wolfram-Kernel; Ausgabe k441b_out.txt. Im ersten Lauf lief FindRoot ohne Klammerung auf einen falschen Zweig
   (delta = 2,2003, m_tau,pred = m_mu); Teile 2 und 3 dieses Laufs (Neutrino-Wurzeln, Massen, m_beta, m_bb) haengen davon nicht ab und werden gewertet;
   Teil 1 und das Skalenverhaeltnis stammen aus dem zweiten Lauf mit geklammerter Brent-Suche. *)
a = Sqrt[2]; x = 0.0395773407`20;
rt[d_] := Table[1 + a Cos[d + 2 Pi k/3], {k, 0, 2}];
me = 0.51099895`20; mmu = 105.6583755`20;
f[d_?NumericQ] := Module[{m = Sort[rt[d]^2]}, m[[1]]/m[[2]] - me/mmu];
de = d /. FindRoot[f[d], {d, 0.15, 0.26}, Method -> "Brent", WorkingPrecision -> 20];
ms = Sort[rt[de]^2]; mu2 = me/ms[[1]];
Print["1 delta(e,mu) = ", de, " ; x = ", N[Pi/12 - de, 12], " ; m_tau,pred = ", mu2 ms[[3]], " MeV ; M_e = ", mu2, " MeV"];
rn = SortBy[rt[Pi/6 - x], #^2 &]; mn = rn^2;
Print["2 Wurzeln Neutrino = ", N[rn, 7], " ; R = ", N[(mn[[2]]^2 - mn[[1]]^2)/(mn[[3]]^2 - mn[[1]]^2), 7]];
mnu = Sqrt[2.511*^-3/(mn[[3]]^2 - mn[[1]]^2)]; m = mnu mn;
u2 = {(1 - 0.307) (1 - 0.0220), 0.307 (1 - 0.0220), 0.0220};
Print["3 m (meV) = ", N[1000 m, 6], " ; Sigma = ", N[1000 Total[m], 6], " ; m_beta = ", N[1000 Sqrt[Total[u2 m^2]], 6], " ; m_bb max = ", N[1000 Total[u2 m], 6],
  " ; m_bb min = ", N[1000 Max[0, 2 Max[u2 m] - Total[u2 m]], 6], " ; Vorzeichen-Lesart = ", N[1000 Abs[Total[Sign[rn] u2 m]], 6]];
rho = mnu/(mu2 10^6);
Print["4 rho = ", ScientificForm[N[rho, 7]], " ; n(beta_sym) = ", N[Log[rho]/Log[0.5494056410], 6], " ; n(gamma_M) = ", N[Log[rho]/Log[0.2375329580], 6],
  " ; n(1/gamma_L) = ", N[-Log[rho]/Log[1.8646997646], 6], " ; n(exp(-2eps)) = ", N[-Log[rho]/(2 ArcTanh[0.5494056410]), 6],
  " ; v^2/M_nu (GeV) = ", ScientificForm[N[(246.22*^9)^2/mnu/10^9, 5]], " ; M_e^2/M_nu (GeV) = ", ScientificForm[N[(mu2 10^6)^2/mnu/10^9, 5]]];
