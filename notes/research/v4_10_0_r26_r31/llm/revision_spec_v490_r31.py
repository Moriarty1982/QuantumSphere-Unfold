r"""Ueberarbeitung v4.9.0-r31: erweiterter Statusvermerk zu thm:dark-energy (Regel C aus r25).

PATCHES = Liste (alt, neu) exakter Textstuecke. Anwendung lokal und auf GitHub-Fragmente mit
    python llm/apply_patches.py <datei oder Ordner> llm/revision_spec_v490_r31.py
"""
OLD_NOTE = (r"\qsstatus{Status (v4.9.0 revision): present-epoch statement (v4.9.0-r15); under Convention F a matter-frame "
            r"statement, frame-free between M and \(T|_R\) (v4.9.0-r22, r24); the epoch reading is with the author.}")
NEW_NOTE = (r"\qsstatus{Status (v4.9.0 revision): present-epoch statement (v4.9.0-r15); under Convention F a matter-frame "
            r"statement, frame-free between M and \(T|_R\) (v4.9.0-r22, r24); the epoch reading is with the author.  The Markov "
            r"chain is the author's tool to predict the probabilities and to test whether the cascade stabilises itself (author, "
            r"2026-10-22).  As given, \(S^2\) absorbs everything, and the only stationary state is the photon.  With a return path "
            r"\(S^2\to S^8\), for instance pair creation from the vacuum (v4.9.0-r29), the chain has a unique stationary "
            r"distribution, and the fractions of the flux out of \(S^8\) are \(\bsym^2\) and \(1-\bsym^2\) for every return rate "
            r"(v4.9.0-r31).  Within one step \(\bsym^2\) is a weight; successive steps of amplitudes compose through the "
            r"compensator (v4.9.0-r30).}")
PATCHES = [(OLD_NOTE, NEW_NOTE)]
