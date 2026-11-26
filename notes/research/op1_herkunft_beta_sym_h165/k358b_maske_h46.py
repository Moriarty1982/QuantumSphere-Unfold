"""k358b (Erkundung, Nachrechnung): Maskenrechnung zu H45/H46 bei drei Werten von beta_sym.

Fuehrt den unveraenderten Code von notes/research/v4_10_0_r63_r64/llm/k105_h46_exakt.py aus und ersetzt darin nur die Zeile
mit den Kandidaten fuer eps (dort 0.549406 und 0.5493) durch 0.5493, 0.5493482 und 0.5494056410.
Aufruf: python k358b_maske_h46.py
"""
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[3]
src = (REPO / "notes/research/v4_10_0_r63_r64/llm/k105_h46_exakt.py").read_text()
old = 'K = {"artanh(beta exakt)": float(np.arctanh(0.549406)), "artanh(0.5493)": float(np.arctanh(0.5493))}'
new = 'K = {"artanh(0.5494056410)": float(np.arctanh(0.5494056410)), "artanh(0.5493482)": float(np.arctanh(0.5493482)), "artanh(0.5493)": float(np.arctanh(0.5493))}'
assert src.count(old) == 1, "Kandidatenzeile in k105 nicht gefunden"
exec(compile(src.replace(old, new), "k105_mit_drei_werten", "exec"))
