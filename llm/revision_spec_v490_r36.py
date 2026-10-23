r"""Ueberarbeitung v4.9.0-r36: Statusvermerke zu thm:three-generations und thm:SM (Regel C aus r25), nach der
Frame-Regel fuer komplexe Einheiten (Autorentscheidung 2026-10-23, v4.9.0-r35/r36).

PATCHES = Liste (alt, neu) exakter Textstuecke. Anwendung lokal und auf GitHub-Fragmente mit
    python llm/apply_patches.py <datei oder Ordner> llm/revision_spec_v490_r36.py
Die Vermerke stehen am Anfang der jeweils folgenden Zeile (einzeilige Anker, unabhaengig vom Zeilenende).
"""
NOTE_GEN = (r"\qsstatus{Status (v4.9.0 revision): the triplet basis \(e_4,e_5,e_6\) and \(\nu_R\leftrightarrow e_7\) hold in the "
            r"inner frame \(J=L_{e_7}\); with the outer unit they translate by \(P_-\) to the charges \(Q=\tfrac23\) and \(Q=0\) "
            r"(v4.9.0-r34, r35).  The sentence on the anti-triplet \((e_1,e_2,e_3)\) is wrong: \(e_1,e_2,e_3\) are the "
            r"\(J\)-images of the same triplet (v4.9.0-r35).  The cyclic symmetry \(e_4\to e_5\to e_6\) is a colour rotation in "
            r"\(SU(3)=\mathrm{Stab}_{G_2}(e_7)\), so the table places colour and generation on the same object (v4.8.0-r13, "
            r"v4.9.0-r36); generations need a second three-fold structure outside \(\OO\) (v4.8.0-r14, v4.9.0-r33).}")
NOTE_SM = (r"\qsstatus{Status (v4.9.0 revision): the complex scalar \(it\) alone generates a global phase, the same on all charge "
           r"sectors, not electromagnetism.  The charge is \(Q=\tfrac12-\tfrac{i}{6}L_{e_7}-\tfrac{i}{3}R_{e_7}\); it needs the "
           r"outer and the inner complex unit, and its assignment to states depends on the frame (v4.9.0-r34, r35).  "
           r"\(\mathbb C\otimes\HH\) also contains \(SL(2,\mathbb C)\); its compact part is \(U(2)\), and the unbroken \(U(1)\) "
           r"of the Standard Model is hypercharge, which is not derived here.}")
A_GEN = r"\begin{theorem}[Koide relation; phase formula archived]\label{thm:koide-triolic}"
A_SM = r"\section[Bell Inequalities and tau-n]{Bell Inequalities and \texorpdfstring{$\tau_n$}{tau_n}}"
PATCHES = [(A_GEN, NOTE_GEN + A_GEN), (A_SM, NOTE_SM + A_SM)]
