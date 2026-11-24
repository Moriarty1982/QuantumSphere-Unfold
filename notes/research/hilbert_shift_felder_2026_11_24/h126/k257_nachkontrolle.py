"""k257 Nachkontrolle (nach der Auswertung, kein Kriterium): Eigenwerte von MM^dagger an Stichpunkten,
Anteil der Punkte mit Nicht-Assoziativitaetsbeitrag > 1e-9."""
import numpy as np
src = open("k257_test_h126.py").read().split('print("=== delta_e-Anpassung ===")')[0]
ns = {}; exec(src, ns); M_of, U_of = ns["M_of"], ns["U_of"]
for c, d in [(30, 0), (60, 45), (90, 45), (100.5, 294.5), (137, 200)]:
    M = M_of(np.deg2rad(c), np.deg2rad(d)); ev, _ = U_of(M)
    na = np.linalg.norm(M - M_of(np.deg2rad(c), np.deg2rad(d), True)) / np.linalg.norm(M)
    print(f"chi={c}, dnu={d}: Eigenwerte MM^dag = {np.round(ev, 9)}, rang M = {np.linalg.matrix_rank(M, 1e-9)}, Nicht-Assoz. = {na:.3e}")
cnt = 0; tot = 0
for c in np.arange(0, 180.01, 2):
    for d in np.arange(0, 360, 2):
        tot += 1
        M = M_of(np.deg2rad(c), np.deg2rad(d))
        if np.linalg.norm(M - M_of(np.deg2rad(c), np.deg2rad(d), True)) / np.linalg.norm(M) > 1e-9: cnt += 1
print(f"Anteil mit Nicht-Assoziativitaet > 1e-9: {cnt}/{tot}")
