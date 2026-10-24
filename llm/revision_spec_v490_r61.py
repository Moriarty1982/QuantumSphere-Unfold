r"""Ueberarbeitung v4.9.0-r61: Statusvermerke zu thm:bsym-hopf, rem:bsym-hopf-gap, thm:tribonacci und rem:op1-tribonacci (Regel C aus r25),
nach der Frame-Pruefung der offenen Probleme (v4.9.0-r61, Autorentscheidung 2026-10-24).

PATCHES = Liste (alt, neu) exakter Textstuecke. Anwendung lokal und auf GitHub-Fragmente mit
    python llm/apply_patches.py <datei oder Ordner> llm/revision_spec_v490_r61.py
Die neuen Vermerke stehen am Anfang der jeweils folgenden Zeile (einzeilige Anker); der vorhandene Vermerk zu thm:tribonacci wird erweitert.
"""
NOTE_HOPF = (r"\qsstatus{Status (v4.9.0 revision): \(\bsym=\sin(\theta_H/2)\) is the half-angle relation of a pure state measured from the photon pole, "
             r"i.e.\ in the reference frame R (v4.9.0-r24).  The matter frame of Convention~F at the same \(\bsym\) is a mixed state: at \(\bsym^2=\tfrac13\) "
             r"the pure Hopf state has populations \((\tfrac23,\tfrac13)\), the matter state \((\tfrac34,\tfrac14)\) with \(|b|=\tfrac12\) (v4.9.0-r17).  "
             r"The theorem therefore reads an R-frame state as the matter offset (v4.9.0-r61).}")
NOTE_GAP = (r"\qsstatus{Status (v4.9.0 revision): OP~1 stays open, but its target is the matter-frame value itself.  The Hopf value compares an R-frame "
            r"pure state with the mixed matter state, and the gap to it is not a like-for-like difference (v4.9.0-r61); the prime-lattice reading of the "
            r"gap is not needed for that.  Under the flavour reading of v4.9.0-r55 to r60 the lepton data give \(\bsym\in[0.545,0.570]\), containing the "
            r"measured value and excluding the Hopf and Tribonacci values (v4.9.0-r61, not a blind test).}")
OLD_TRI = r"\qsstatus{Status (v4.9.0 revision): equivalent to \(\cosh2\eta=e^\eta\), the point where the three readings of the offset coincide (v4.9.0-r01, r18).}"
NEW_TRI = (r"\qsstatus{Status (v4.9.0 revision): equivalent to \(\cosh2\eta=e^\eta\), the point where the three readings of the offset coincide (v4.9.0-r01, r18).  "
           r"The condition \(\gL=1/\bsym\) equates a readout quantity of the matter frame with \(1/\bsym=\beta_T\), the tachyon offset in its own measure "
           r"(v4.9.0-r24.2), and way~A with way~C (v4.9.0-r19); it is not a frame-consistent fixed point (v4.9.0-r61).}")
NOTE_OP4 = (r"\qsstatus{Status (v4.9.0 revision): the resolution claimed here is withdrawn (Corollary~\ref{cor:op1-resolved}).  The continuum-limit "
            r"correction line (OP~4) measures the distance between the matter value and the Tribonacci and Hopf values, which come from other frames or "
            r"classes; in this form OP~4 is ill-posed, and only OP~1 remains (v4.9.0-r61).}")
A_HOPF = r"\begin{remark}[The Hopf gap and OP~1]"
A_GAP = r"\begin{theorem}[Three fermion generations from $\OO$]"
A_OP4 = r"\begin{theorem}[First machine-fused coupled OP-entry theorem]"
PATCHES = [(A_HOPF, NOTE_HOPF + A_HOPF), (A_GAP, NOTE_GAP + A_GAP), (OLD_TRI, NEW_TRI), (A_OP4, NOTE_OP4 + A_OP4)]
