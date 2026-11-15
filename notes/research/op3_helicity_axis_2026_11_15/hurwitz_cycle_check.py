"""Kann der Hurwitz-Zyklus auf dem neutralen Qubit N (v4.10.0-r13.2, unter CT-003) den fehlenden Dreierzyklus der
Feldachsen liefern? Pruefung der Darstellung der Frame-Abbildungen auf N (Erkundung, nicht blind).

Frame-Abbildungen auf C x S wie in v4.9.0-r51: R = Multiplikation mit i (C-linear), T = komplexe Konjugation,
J_B = R o T. Auf dem chi-Dublett wirken R, T, J_B dagegen als drei verschiedene Pauli-Drehungen (frame_labels.py).
Aufruf: python hurwitz_cycle_check.py <Pfad zu notes/research>
"""
import importlib.util, os, sys
import numpy as np

base = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location("k225", os.path.join(base, "predictions", "k225_test_h103.py"))
k = importlib.util.module_from_spec(spec); spec.loader.exec_module(k)
B = k.B                                     # 16x2, Basis von N in C x S
PN = B @ B.conj().T                          # Projektor auf N

# (1) R auf N: skalar
RN = B.conj().T @ (1j * np.eye(16)) @ B
print(f"(1) R auf N = i * 1: {np.allclose(RN, 1j * np.eye(2))} -> R zeichnet auf N keine Achse aus")

# (2) T (komplexe Konjugation) bildet N nicht in sich ab
Bc = B.conj()
overlap = np.linalg.norm(PN @ Bc) / np.linalg.norm(Bc)
print(f"(2) Anteil von conj(N) in N: {overlap:.3f} -> T (und J_B) bilden N {'in sich' if overlap > 1 - 1e-9 else 'nicht in sich'} ab")

# (3) Folge: Die Frame-Gruppe wirkt auf N nicht wie auf chi (dort R nicht skalar, T linear und N-erhaltend).
print("(3) Es gibt keine mit R, T, J_B vertraegliche Identifikation von N mit chi; der Hurwitz-Zyklus auf N vertauscht")
print("    Paulis der Rechtswirkung (Familien-su(2), r13.4), nicht die Frame-Abbildungen.")
