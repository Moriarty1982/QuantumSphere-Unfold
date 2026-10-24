r"""Ueberarbeitung v4.9.0-r64: Statusvermerke zu thm:k-values, thm:planck-photon und thm:hawking-triolic (Regel C aus r25),
nach der Frame-Pruefung der Gravitationssaetze (v4.9.0-r64, Autorentscheidung 2026-10-25).

PATCHES = Liste (alt, neu) exakter Textstuecke. Anwendung lokal und auf GitHub-Fragmente mit
    python llm/apply_patches.py <datei oder Ordner> llm/revision_spec_v490_r64.py
Die vorhandenen Vermerke zu thm:k-values und thm:planck-photon werden erweitert; der Vermerk zu thm:hawking-triolic steht vor dem Theorem.
"""
OLD_K = r"Conversion ways: v4.9.0-r18, r19 (class split offered).}"
NEW_K = (r"Conversion ways: v4.9.0-r18, r19 (class split offered).  The entry \(k(\gBI)=0\) contradicts Theorem~\ref{thm:frame-offset}, which calls \(\gBI\) "
         r"the Lorentz-transformed \(\gstring\).  Under the counting reading of v4.9.0-r63 the frame difference sits in \(\gamma\) itself, and \(\hbar\), \(G_N\) enter "
         r"both countings identically; the entries \(k(\hbar)=1\), \(k(G_N)=2\) then need a source other than \(\gL\) (v4.9.0-r64).}")
OLD_P = r"tachyon phase \(\mp i\) (v4.9.0-r22).}"
NEW_P = (r"tachyon phase \(\mp i\) (v4.9.0-r22).  Under the counting reading of v4.9.0-r63 both countings use the same \(\lP\); the factor \(\gL^{-3/2}\) "
         r"converts \(\hbar\) and \(G_N\) with the counting ratio and is not supported by that reading (v4.9.0-r64).}")
NOTE_H = (r"\qsstatus{Status (v4.9.0 revision): under the counting reading of v4.9.0-r63, \(\gstring\) is the minimal-spin counting of the tachyon floor, "
          r"i.e.\ of the infalling partner; the theorem assigns it to the escaping photon in the reference frame R and reads T as R (v4.9.0-r64).}")
A_H = r"\begin{theorem}[Hawking radiation from the triolic structure]"
PATCHES = [(OLD_K, NEW_K), (OLD_P, NEW_P), (A_H, NOTE_H + A_H)]
