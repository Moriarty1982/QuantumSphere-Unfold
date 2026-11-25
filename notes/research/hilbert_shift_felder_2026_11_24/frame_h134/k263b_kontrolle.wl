(* k263b (zu H134, Kontrolle iv, 25.11.2026): unabhaengige Nachrechnung eines Trefferpunkts aus k263c_out.txt (Variante B, eps = artanh(beta_sym), Klasse TM1)
   und der Stelle eps = 0. Geprueft wird die Auswertung (Massen, Winkel, sin delta) aus den Matrizen, nicht die Anpassung selbst. *)
mnu = {{0.8915936324080883, 0.3307333434901660, -0.0518926724260875}, {0.3307333434901660, -0.0134113620310210, 0.0928915729210070}, {-0.0518926724260875, 0.0928915729210070, -0.0003301634527595}};
me = {{-0.0736414571144380, 0.0699668138638372 + (-0.0834096796356286) I, 0.4459272803014827 + (0.5316041925693320) I}, {0.0699668138638372 + (0.0834096796356286) I, -0.0736414571144380, 0.4459272803014833 + (-0.5316041925693316) I}, {0.0109779223171706 + (-0.0130871327844369) I, 0.0109779223171706 + (0.0130871327844369) I, -0.0736414571144380}};
{ve, we} = Eigensystem[me.ConjugateTranspose[me]]; oe = Ordering[ve]; ue = Transpose[we[[oe]]];
{vn, wn} = Eigensystem[mnu]; on = Ordering[Abs[vn]]; un = Transpose[wn[[on]]];
Print["Massenverhaeltnisse geladene Leptonen (Wurzeln der Eigenwerte, normiert): ", Sqrt[ve[[oe]]]/Sqrt[Max[ve]]];
Print["|Eigenwerte| Neutrinos, normiert: ", Abs[vn[[on]]]/Max[Abs[vn]], "; Quadratdifferenzen-Verhaeltnis: ", (Abs[vn[[on]]][[2]]^2 - Abs[vn[[on]]][[1]]^2)/(Abs[vn[[on]]][[3]]^2 - Abs[vn[[on]]][[1]]^2)];
u = ConjugateTranspose[ue].un; p = Abs[u]^2;
s13 = p[[1, 3]]; s12 = p[[1, 2]]/(1 - s13); s23 = p[[2, 3]]/(1 - s13);
jj = Im[u[[1, 1]] u[[2, 2]] Conjugate[u[[1, 2]]] Conjugate[u[[2, 1]]]];
sd = jj/(Sqrt[s12 (1 - s12) s23 (1 - s23) s13] (1 - s13));
Print["sin^2 12 = ", NumberForm[s12, 10], ", sin^2 23 = ", NumberForm[s23, 10], ", sin^2 13 = ", NumberForm[s13, 10], ", sin delta = ", NumberForm[sd, 10]];
Print["eps = 0, TM1 exakt: sin^2 12 bei sin^2 13 = 0.02023 und 0.02376: ", {1 - 2/(3 (1 - 0.02023)), 1 - 2/(3 (1 - 0.02376))}];
