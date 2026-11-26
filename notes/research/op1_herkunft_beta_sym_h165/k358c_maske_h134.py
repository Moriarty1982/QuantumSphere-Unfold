"""k358c (Erkundung, Nachrechnung): Test H134 (k263) mit eps = artanh(0.5494056410) statt artanh(0.5493).

Fuehrt den unveraenderten Code von notes/research/hilbert_shift_felder_2026_11_24/frame_h134/k263_test_h134.py aus und ersetzt
darin nur den Wert 0.5493 in der Zeile fuer ETA. Vergleich: k263_out.txt im selben Ordner (Raster 2 Grad).
Aufruf: python k358c_maske_h134.py
"""
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[3]
path = REPO / "notes/research/hilbert_shift_felder_2026_11_24/frame_h134/k263_test_h134.py"
src = path.read_text()
old = "ETA, HOPF = float(np.arctanh(0.5493)), float(np.arctanh(1/np.sqrt(3)))"
new = "ETA, HOPF = float(np.arctanh(0.5494056410)), float(np.arctanh(1/np.sqrt(3)))"
assert src.count(old) == 1, "ETA-Zeile in k263 nicht gefunden"
sys.argv = [str(path)]
if __name__ == "__main__":
    exec(compile(src.replace(old, new), str(path), "exec"))
