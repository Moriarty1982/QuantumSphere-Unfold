r"""Ueberarbeitung v4.9.0-r66: Korrektur des Statusvermerks zu thm:k-values aus r65 (Regel C aus r25).
Der Widerspruch k(gBI)=0 gegen thm:frame-offset stand schon in v4.9.0-r09 und ist dort aufgeloest; r64/r65 haben das nicht zitiert.

PATCHES = Liste (alt, neu) exakter Textstuecke. Anwendung lokal und auf GitHub-Fragmente mit
    python llm/apply_patches.py <datei oder Ordner> llm/revision_spec_v490_r66.py
"""
OLD_K = r"both countings identically; the entries \(k(\hbar)=1\), \(k(G_N)=2\) then need a source other than \(\gL\) (v4.9.0-r64).}"
NEW_K = (r"both countings identically; the entries \(k(\hbar)=1\), \(k(G_N)=2\) then need a source other than \(\gL\) (v4.9.0-r64).  The contradiction "
         r"was already found as item~1 of v4.9.0-r09 and resolved there by reading Theorem~\ref{thm:frame-offset} as a statement about the structural factor alone; "
         r"under v4.9.0-r63 that structural factor is the counting ratio (v4.9.0-r66).}")
PATCHES = [(OLD_K, NEW_K)]
