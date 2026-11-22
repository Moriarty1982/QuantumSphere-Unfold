# Zeitumkehr oder Spiegelung am ersten Jet des OP5-Keims: unentschieden, keines passt (Erkundung, 22.11.2026)

**Ergebnis in einem Satz:** In den ersten Ableitungen ist der Gegenstrom-Block 2 weder das Zeitumkehrbild noch das Spiegelbild noch die
bloße innere Umkehr der mitlaufenden Blöcke; die Abweichungen liegen bei 0,4 bis 1,9 der Ableitungsskala statt unter 10⁻². Die
Bildbeziehung aus r41 gilt also nur für die Werte am Keimpunkt, nicht als lokale Feldbeziehung. **Nach dem vorab festgelegten Raster:
unentschieden (keines passt).**

Auftrag des Autors: „weiter“ nach r41. Verfahren vorab: `Methoden_Notiz.md` (Commit 8006e893). Teilweise nicht blind: Die Handskizze
erwartete die innere Umkehr I; sie trifft nicht zu. Skript `counterflow_jet.py` (Python, mpmath 40 Stellen, Keimordner als Argument),
Ausgabe `run/counterflow_jet.txt`. Wolfram nicht nötig (keine symbolische Rechnung), Qiskit nicht geeignet. Keine H-Nummer.

## Ergebnis
| Bild von | T (Zeitumkehr) | R (Spiegelung x ↦ −x) | I (innere Umkehr) |
|---|---|---|---|
| Block 0, je μ = (t, x, y, z) | 1,28; 0,38; 0,72; 0,67 | 0,49; 0,77; 1,87; 0,33 | 0,49; 0,38; 0,72; 0,67 |
| Block 0, gesamt | 1,28 | 1,87 | 0,72 |
| Block 1, gesamt | 1,07 | 0,93 | 1,07 |

Relative Abweichung = max |∂_μF₂ − ∂_μ(Bild)| / max |∂F_Quelle|; Raster 10⁻². Zum Vergleich unterscheiden sich die Blöcke 0 und 1 derselben
Laufrichtung in den Ableitungen um das 4,9-Fache der Skala von Block 0.

Nachträglich, nicht vorab festgelegt: v = J^x/J⁰ und Ableitungen
| Block | v | ∂_t v | ∂_x v |
|---|---|---|---|
| 0 | 0,5998 | −0,494 | 0,717 |
| 1 | 0,5978 | −2,860 | 3,207 |
| 2 | −0,6002 | 1,102 | −0,246 |
Die Hubble-Form v = ±x/t gäbe ∂_t v = ∓0,6 und ∂_x v = ±1.

## Lesart
- Die Werte am Keimpunkt zeigen Gegenstrom und Zeitumkehrbild (r41), die Ableitungen nicht. Die Gleichgewichtung beider Orientierungen ist
  damit eine Eigenschaft des Punktes, keine nachgewiesene Eigenschaft des Feldes in seiner Umgebung.
- Die Bezeichnung „Hubble-artige Strömung“ in k168 ist eine Lesart aus den Werten; der Jet folgt dieser Form nicht.
- Grenze: Der Jet erfüllt laut Datei F = 0 und g = 0, die vervollständigten G- und dg-Bedingungen sind nicht gelöst. Ein vervollständigter
  Jet könnte andere Ableitungen haben; diese Prüfung gilt für den vorliegenden.
- r41 bleibt unverändert (append-only); seine Lesart ist hiermit auf den Keimpunkt eingeschränkt.
- OP5 und H96 bleiben offen; OP3 ruht und wird nicht berührt.
