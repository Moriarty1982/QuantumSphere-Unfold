# H194: Die H188-Form mit einer unabhängigen Vorhersage

Test, **teilweise**. Prüft den nachträglichen H188-Kandidaten m ∝ (a·l_k + b·l_k²)/(l_i+l_j)² mit zwei vorab festgelegten
unabhängigen Vorhersagen, wie H188 es verlangt hatte.

- `Vorab_Notiz_H194_H188_Form_unabhaengige_Vorhersage.md` — Vorab (Kopie; Original unter `notes/research/predictions/`), Commit 615c984.
- `k402_test_h194.py` / `k402_out.txt` — Fit je Sektor (H194a), gemeinsames ρ (H194b), Spezifität der l_k (H194c), Zufallskontrollen.
- `k402c_kontrolle.py` / `k402c_out.txt` — fairere Genericität: Zufalls-l mit eigener bester Permutation (beide Sektoren 0,00 %).
- `k402b_out.txt` — Wolfram-Gegenprobe der exakten leptonischen Eigenwerte und Fits, bestätigt Python.
- `Ergebnis_H194_H188_Form_unabhaengige_Vorhersage.md` — Befund.

**Kurz:** H194b widerlegt (kein gemeinsames b/a; Up ~ l_k²/z, Down ~ l_k/z, Faktor 680 auseinander). H194c spezifisch: nur
Zuordnung B trifft, und zufällige l-Tripel reproduzieren beide Sektoren in 0,0 % (auch mit eigener bester Permutation). Die
leptonischen Eigenwerte (δ = 2/9) sind für diese Form ausgezeichnet — die erste Quark-Lesart mit mehr als einem reinen Fit. Grenze:
die Funktionsform selbst ist nachträglich gewählt; es fehlt die Herleitung. Aufruf: `python k402_test_h194.py > k402_out.txt`.
