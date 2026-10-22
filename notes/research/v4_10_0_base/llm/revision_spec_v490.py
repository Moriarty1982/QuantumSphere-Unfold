r"""Eingriffe der Ueberarbeitung v4.9.0-r25 (Spezifikation).

Wortgleich dieselben Eingriffe wie in llm/aufraeumen_v490.py (lokal, schon angewandt). Wird von
llm/aufraeumen_v410_github.py mit exec geladen; erwartet do_archive, do_replace, do_status, after.
"""

# ---------------- A: Sackgassen ----------------
do_archive("thm:koide-triolic", "Koide relation; phase formula archived",
    r"The lepton masses satisfy the Koide relation \(K=2/3\) to within \(0.005\%\).  This is an empirical fact; its "
    r"derivation from the triolic structure is open.  The phase formula \(\theta_K=\pi-\sqrt2\arcsin\bsym\) of the earlier "
    r"version is excluded by data at about \(300\)--\(400\sigma\) (v4.8.0-r09).",
    r"phase formula excluded by data (v4.8.0-r09); \(K=2/3\) stays as empirical fact")
do_archive("thm:gue", "GUE statistics; derivation archived",
    r"The spacing statistics of the Riemann zeros follow GUE.  This is an empirical fact (v4.8.0-r05).  The derivation "
    r"from the Sphaera given in the earlier version is withdrawn.",
    r"derivation withdrawn (v4.8.0-r05); GUE stays as empirical fact")
do_archive("thm:gue-selfdet", "GUE self-determination of \\(\\gL\\); archived",
    r"The claim that the photon-frame unfolding singles out \(\mu=\gL\) is not confirmed.  The minimum lies at \(\mu=1\), "
    r"and the claim is contradicted on zeros \(1\)--\(2000\) (v4.8.0-r08).",
    r"not confirmed, contradicted on zeros 1--2000 (v4.8.0-r08)")
do_archive("cor:odlyzko", "Prediction P1; archived",
    r"By its own criterion the prediction is falsified at low height, and its asymptotic form is excluded by the "
    r"\(1/\log\gamma\) decay (v4.8.0-r08).",
    r"falsified at low height, asymptotic form excluded (v4.8.0-r08)")
do_archive("conj:cl-correction", "\\(\\bsym\\)-formula P3; archived",
    r"The formula \(\bsym=(1/\sqrt3)\exp(-\gamma_1/(4\pi\gL^5))\) matched the measured value to \(0.018\%\) with an exponent "
    r"fixed after the fact.  v4.8.0-r09 classes the match as a coincidence (look-elsewhere about \(11\%\)); under the class "
    r"split of v4.9.0-r19 it is lost (\(-0.15\%\)).  The continuum value \(\bsym^{\rm Hopf}=1/\sqrt3\) and the existence of a "
    r"lattice correction are not affected.",
    r"coincidence, exponent post hoc (v4.8.0-r09); lost under the class split (v4.9.0-r19)")
do_archive("prop:exponent-5", "The \\(\\gL^5\\) exponent; archived",
    r"The exponent \(5\) was chosen after the fact (v4.8.0-r09).  It is archived together with the formula of "
    r"Remark~\ref{conj:cl-correction}.",
    r"exponent chosen post hoc (v4.8.0-r09)")
do_archive("thm:self-consistent-gL", "Self-consistent \\(\\gL\\); archived",
    r"The coupled system of the earlier version rests on the formula of Remark~\ref{conj:cl-correction}, archived as a "
    r"coincidence.  \(\gL=\gBI/\gstring\) remains an input, the ratio of two published Barbero--Immirzi values "
    r"(v4.8.0-r03 F11).",
    r"rests on the archived P3 formula; \(\gL\) remains an input (v4.8.0-r03 F11)")
do_archive("cor:op1-resolved", "OP~1; claimed resolution archived",
    r"OP~1 is not resolved.  The claimed resolution at \(0.04\%\) used the formula of Remark~\ref{conj:cl-correction}, "
    r"archived as a coincidence (v4.8.0-r09).  OP~1 stays open.",
    r"claimed resolution rests on the archived P3 formula; OP1 open")
do_archive("prop:pmns-z3", "PMNS from the triolic \\(\\mathbb Z/3\\mathbb Z\\); archived",
    r"Refuted by the pre-registered neutrino and mixing tests of v4.8.0-r12.",
    r"refuted (v4.8.0-r12)")
do_archive("prop:H0-tension", "\\(H_0\\) tension as \\(\\bsym(t)\\) evolution; archived",
    r"The required drift of the local frame factor, about \(1.6\times10^{-12}\) per year, is excluded by atomic clocks by "
    r"about six orders of magnitude (v4.9.0-r08).  No working mechanism remains (v4.9.0-r09).",
    r"drift excluded by atomic clocks (v4.9.0-r08); no mechanism left (v4.9.0-r09)")
do_archive("prop:saturation", "Saturation model; archived",
    r"Items (1) and (2) have no basis left (v4.9.0-r15).  The end state \(\bsym\to1\) is the photon fixed point of "
    r"Convention F (v4.9.0-r23).",
    r"no basis left (v4.9.0-r15)")
do_archive("prop:bare-lambda", "Bare \\(\\Lambda\\); archived",
    r"The value \(\Lambda_{\rm bare}\sim\gamma_1^2\) is unsupported, and the proposition is withdrawn as a derivation "
    r"(v4.8.0-r05).",
    r"withdrawn as derivation; \(\gamma_1^2\) unsupported (v4.8.0-r05)")
do_archive("conj:theta-sum-B", "Theta-sum balance conjecture; archived",
    r"The conjectured value \(\mathcal T(T)\approx0.893\) is false.  The sum is \(-0.1097\) (v4.8.0-r05), and OP~5 Step~(B)"
    r" has no valid form on this route.",
    r"false: \(\mathcal T(T)=-0.1097\), not \(0.893\) (v4.8.0-r05)")
do_archive("rem:explicit-formula-remainder", "Remainder estimate; archived",
    r"The remainder estimate that was to support Proposition~\ref{conj:theta-sum-B} is withdrawn with it (v4.8.0-r05).",
    r"withdrawn with the Theta-sum conjecture (v4.8.0-r05)")

# ---------------- B: Korrekturen ----------------
do_replace(r"Riemann Hypothesis & $\gamma^-_\rho=0$ for all zeros & \cite{brendecke2026rh}\\",
           r"Riemann Hypothesis & not a result of the framework (withdrawn, v4.8.0-r04) & ---\\")
archive.append(("thm:toe", "row", "Structural unification target, table row",
                r"the row ``Riemann Hypothesis'' was withdrawn (v4.8.0-r04)",
                r"Riemann Hypothesis & $\gamma^-_\rho=0$ for all zeros & \cite{brendecke2026rh}\\"))
do_replace(" = \\gL^6\\approx 41.8,", " = \\gL^5\\approx 22.5,")
do_replace(" = \\gL^{6} \\approx 42.0.\n\\end{equation}", " = \\gL^{5} \\approx 22.5.\n\\end{equation}")
do_replace(" = \\left(\\frac{\\lP^{(\\mathrm{matter})}}{\\lP^{(\\mathrm{photon})}}\\right)^4\n",
           " = \\frac{\\hbar^{(\\mathrm{photon})}}{\\hbar^{(\\mathrm{matter})}}"
           "\\left(\\frac{\\lP^{(\\mathrm{matter})}}{\\lP^{(\\mathrm{photon})}}\\right)^4\n")
do_replace("so $(\\ell_P^{(\\mathrm{matter})}/\\ell_P^{(\\mathrm{photon})})^4 = \\gL^6$.",
           "so $(\\ell_P^{(\\mathrm{matter})}/\\ell_P^{(\\mathrm{photon})})^4 = \\gL^6$; with "
           "$\\rho_{\\mathrm{vac}}\\sim\\hbar c\\,\\ell_P^{-4}$ and $k(\\hbar)=1$ the ratio is $\\gL^{6-1}=\\gL^5$.")
do_replace("$\\gL^6 \\approx 42.0$ in the vacuum energy density. Such an argument",
           "$\\gL^5 \\approx 22.5$ in the vacuum energy density. Such an argument")
do_replace("of $\\gL^6 \\cdot 10^{-122} \\approx 10^{-120.4}$ even after perfect",
           "of $\\gL^5 \\cdot 10^{-122} \\approx 10^{-120.6}$ even after perfect")
do_replace("= \\gL^{-6}\\rho_{\\mathrm{vac}}^{(\\mathrm{photon})}$, so any",
           "= \\gL^{-5}\\rho_{\\mathrm{vac}}^{(\\mathrm{photon})}$, so any")
do_replace("ratio $\\gL^6$-times larger in the photon frame.", "ratio $\\gL^5$-times larger in the photon frame.")
do_replace("Matter-frame computations carry a systematic error of $\\gL^6 \\approx 42$",
           "Matter-frame computations carry a systematic error of $\\gL^5 \\approx 22.5$")
do_replace("Matter-frame error = $\\gL^6 \\approx 42.0$", "Matter-frame error = $\\gL^5 \\approx 22.5$")
do_replace(" = \\gL^{k(\\alpha)-k(G_N)} \\cdot \\frac{k(\\alpha)}{k(G_N)}\n = \\gL^{-1} = \\frac{\\gstring}{\\gBI} \\approx 0.537,",
           " = \\frac{k(\\alpha)}{k(G_N)} = \\frac12,")
do_replace("The deviation is $\\approx 46\\%$ but requires", "The deviation is $50\\%$ but requires")
do_replace("$\\alpha^{-1}$ & $137.035\\,999\\,084$ & 1", "$\\alpha$ & $1/137.035\\,999\\,084$ & 1")
do_replace("The quaternion identity $e_3=e_1 e_2$ ensures this is always orthogonal\nto both inputs.",
           "The quaternion identity $e_3=e_1 e_2$ makes the product $z\\times J_Bz=2E\\times B$ orthogonal to both\n"
           "inputs; the average $C(f)$ itself is not.")

B = r"Corrected in the v4.9.0 revision"
do_status("prop:uv-photon", B + r": the ratio is \(\gL^5\approx22.5\), not \(\gL^6\approx42.0\).  As an energy density "
          r"\(\rho_{\rm vac}\sim\hbar c\,\lP^{-4}\) has \(k=-5\) (v4.8.0-r03 F1).")
do_status("cor:matter-error", B + r": \(\gL^5\approx22.5\) and residual \(10^{-120.6}\), earlier \(\gL^6\approx42.0\) and "
          r"\(10^{-120.4}\) (v4.8.0-r03 F1).")
do_status("thm:k-values", B + r": the \(k=1\) of the first row belongs to \(\alpha\), not to \(\alpha^{-1}\) as earlier "
          r"printed (v4.8.0-r03 F2, closed in v4.9.0-r08).  Conversion ways: v4.9.0-r18, r19 (class split offered).")
do_status("prop:compensator", B + r": orthogonality holds for the product \(z\times J_Bz=2E\times B\), not for the average "
          r"(v4.9.0-r03.4); earlier text: ``this is always orthogonal to both inputs''.")
do_status("cor:falsifiable", B + r" (P4: \(\gL^5\approx22.5\), earlier \(\gL^6\approx42\); P5: \(1/2\), earlier "
          r"\(\gL^{-1}\approx0.537\)).  Status of P1--P6: P1 not confirmed, archived (v4.8.0-r08); P2 phase formula "
          r"excluded, archived (v4.8.0-r09); P3 coincidence, archived (v4.8.0-r09, v4.9.0-r19); P4 contradicted as stated "
          r"(v4.8.0-r03 F4); P5 corrected to \(1/2\), untestable at present (v4.9.0-r09); P6 untested, assumption \(k(M)=0\) "
          r"explicit (v4.8.0-r03 F6).")
do_status("thm:toe", B + r": the row ``Riemann Hypothesis'' is withdrawn (v4.8.0-r04); a global photon-clock/RH "
          r"statement is forbidden by the guard \(W_\gamma^{\rm glob}\).  Original row in \S\ref{sec:v490-archive}.")

# ---------------- C: Statusvermerke ----------------
S = r"Status (v4.9.0 revision)"
for lab, txt in [
    ("thm:unity", r"conjecture; the Stone--von Neumann justification is withdrawn (v4.8.0-r04); Reading~B gives a precise form via duality (v4.8.0-r07)."),
    ("def:biquaternion", r"Minkowski reading replaced: signature \((1,6)\), natural norm \(N(q)\), Reading~B (v4.8.0-r06)."),
    ("thm:lorentz", r"shows \(J\)-invariance; the Lorentz action comes from Reading~B (v4.8.0-r06)."),
    ("thm:fractal", r"null axis redefined as \(s=0\), directions \(S_0\) (v4.8.0-r06); transport open."),
    ("thm:unitary-equiv", r"open (v4.8.0-r04)."),
    ("thm:symmetric-frame", r"the tachyon at \(-\bsym\) is the real projection \(T|_R\) of the tachyon rapidity \(-\eta+i\pi/2\); in its own frame \(\beta_T^2=1/\bsym^2\) (v4.9.0-r24.2).  \(\gL\) is the ratio of Bloch lengths \(|b_R|/|b_M|\) (v4.9.0-r24.3).  The sign of \(\beta\) is an orientation code; the sector is fixed by the sign of \(s\) (v4.8.0-r07, v4.9.0-r24.1)."),
    ("thm:frame-offset", r"structural statement about \(\gL\) (author, v4.9.0-r16); conversions as in v4.9.0-r18, r19."),
    ("prop:hawking-gBI-tachyon", r"item (ii): frame order does not match the axis (v4.9.0-r01); item (iii) holds to \(-0.55\%\) under the class split (v4.9.0-r19); assumption \(k(M)=0\) explicit (v4.8.0-r03 F6); in the tachyon frame \(T_H\) changes sign (v4.9.0-r23)."),
    ("thm:hopf", r"Hopf fibrations classical; physical identification a conjecture; the chain \(S^{15}\to S^8\to S^4\to S^2\) is not a composition of Hopf maps (v4.8.0-r09)."),
    ("thm:dark-energy", r"present-epoch statement (v4.9.0-r15); under Convention F a matter-frame statement, frame-free between M and \(T|_R\) (v4.9.0-r22, r24); the epoch reading is with the author."),
    ("thm:einstein", r"structural conjecture; the action is undefined (v4.8.0-r05)."),
    ("thm:eom", r"projector algebra kept; the zero reading is withdrawn (v4.8.0-r04)."),
    ("cor:gue-frame", r"items (ii), (iii) are conversions of weight \(k=1\); the photon-frame unfolding is not confirmed (v4.8.0-r08)."),
    ("thm:planck-photon", r"conversion from the matter frame to the reference frame R (v4.9.0-r24); under the class split the factor is \(e^{3\eta/2}\) (v4.9.0-r19); tachyon phase \(\mp i\) (v4.9.0-r22)."),
    ("thm:tribonacci", r"equivalent to \(\cosh2\eta=e^\eta\), the point where the three readings of the offset coincide (v4.9.0-r01, r18)."),
    ("thm:hc-quasiconformal", r"matter-frame statement; in the tachyon's own frame \(|\mu|>1\) and the map reverses orientation (v4.9.0-r23)."),
    ("thm:lambda-zero", r"(i) holds by the definition of the reference frame R, the pure state (v4.9.0-r24); at the photon proper the frame term is maximal; (iii) is off by \(10^{121}\) (v4.8.0-r03 F8, F9)."),
]:
    do_status(lab, S + ": " + txt)

after("No CODATA value has ever been measured in the photon frame.\n\\end{remark}",
    S + r": under Convention F (v4.9.0-r22, r24) the frame called photon frame in this section is the reference frame R, "
    r"the pure doublet state \(|b|=1\).  The conversion \(X^{(\rm photon)}=\gL^{-k}X^{(\rm matter)}\) goes from the matter "
    r"frame to R, with \(\gL=|b_R|/|b_M|\).  The photon proper, \(b=0\), is reached only as \(\beta\to1\).  Ways A and C of "
    r"the conversion: v4.9.0-r18, r19 (class split offered, decision with the author).")
after(" \\item \\textbf{Photon} ($K_3=e_1 e_2$): $\\mathrm{Re}(z_3)=0$, boost $\\beta=0$, lightlike.\n\\end{itemize}\n\\end{definition}",
    S + r": the sign of \(\beta\) here is an orientation code.  Theorem~\ref{thm:symmetric-frame} uses the opposite "
    r"convention; the two differ by charge conjugation \(z\mapsto-z\), which leaves \(s=z\cdot z\) unchanged.  The sector "
    r"is fixed by the sign of \(s\) (v4.8.0-r07, v4.9.0-r24.1).")
do_status("rem:open", S + r": P4 as stated is contradicted (v4.8.0-r03 F4); the type of \(\Lambda\) is open (F3); the "
          r"\(\Theta\)-sum route is false (v4.8.0-r05).")


def archive_tex(archive):
    rows = "\n".join(r"%s & %s\\" % (
        ("Table row of Thm.~\\ref{%s}" % lab) if env == "row" else ("%s~\\ref{%s}" % (env.capitalize(), lab)), verdict)
        for lab, env, title, verdict, body in archive)
    parts = [r"""% ============================================================================
\clearpage
\section*{Archived Statements of the Main Body}
\addcontentsline{toc}{section}{Archived Statements of the Main Body}
\label{sec:v490-archive}
% ============================================================================

This appendix was created in the v4.9.0 revision (v4.9.0-r25, 2026-10-22, at the author's request) and opens the
4.10 base.  It keeps, word for word, statements of the main body that later layers refuted, excluded or withdrew.  At
their original place each statement keeps its number and label, followed by its status and a pointer here, so every
earlier reference still resolves.  Nothing is deleted; the frozen state of the fragments is kept under the tag
\texttt{v4.9.0}.  The rounds, including all tests and refutations, are not touched.

\begin{center}
\small
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.32\textwidth}>{\raggedright\arraybackslash}p{0.60\textwidth}@{}}
\toprule
statement & reason\\
\midrule
""" + rows + r"""
\bottomrule
\end{longtable}
\end{center}
"""]
    for lab, env, title, verdict, body in archive:
        head = ("Table row of Theorem~\\ref{%s}" % lab) if env == "row" else ("%s~\\ref{%s}" % (env.capitalize(), lab))
        parts.append("\\begin{qsarchived}{%s%s}\n%s\n\\end{qsarchived}\n" % (
            head, (" [" + title + "]") if title and env != "row" else "",
            ("\\begin{tabular}{lll}\n" + body + "\n\\end{tabular}") if env == "row" else body))
    return "\n".join(parts) + "\n"
