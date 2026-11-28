# Ergebnis H223 (k437): Kein natürlicher Elternterm bindet das Vorzeichen unter J — das Vorzeichen der Daten steckt im J-verbotenen Teil

**Datum:** 2026-11-28. **Vorab:** `Vorab_H223_Elternterm_Vorzeichen.md` (Commit f052b0c, vor der Rechnung). **Urteil: widerlegt** (kein benannter Kandidat gibt nach
J-Projektion β₃ < 0). **Werkzeuge:** Python/sympy (`k437_test_h223.py` → `k437_out.txt`), Wolfram unabhängig (`k437b_gegenprobe.wl` → `k437b_out.txt`); alle Werte gleich.
a und b nicht blind (vorab überschlagen und offen gelegt), c und d blind. Qiskit nicht einschlägig.

## Frage
Nach H222 wählt das Vorzeichen des sextischen Terms β₃ φ³r³ cos 3δ den Zweig, und nach k436 legen es weder J noch Stabilität fest. Bindet ein Elternterm, etwa das
Quadrat u² eines kubischen Bausteins (positiv, also mit festem Vorzeichen), β₃ so, dass beide Lepton-Sektoren den Daten-Zweig wählen?

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| a (nicht blind) | β₃ = κα′: κ = +1 wählt im Im-Sektor falsch (+1,57), im Re-Sektor richtig; κ = −1 umgekehrt (±0,24) | genau ein Sektor falsch | **bestätigt**: Bindung an α′ mit festem κ ausgeschlossen |
| b (nicht blind) | u = det W: J-projiziert β₃ = +4 → falscher Zweig in beiden; voll (ohne J) richtiger Zweig in beiden (−1,11 / −0,17). u = Tr W³: β₃ = +36, J-projiziert und voll falsch | — | wie überschlagen |
| c (blind) | allgemein u = x(Tr W)³ + y Tr W·Tr W² + z det W: **β₃(J) = 4z(27x + 9y + z)**, also Vorzeichen von Z·X (X = φ³-, Z = r³ cos 3δ-Koeffizient); 48,9 % der Richtungen hätten β₃ < 0. Benannte Kandidaten: det W +4, Tr W³ +36, (Tr W)³ 0, det der spurfreien Matrix 0, Tr W·Tr W² 0, Tr W³ − (Tr W)³/9 0, e₁e₂ − 9e₃ 0 | ein benannter mit β₃ < 0 | **keiner** |
| d (blind) | Spur- und Determinanteninvarianten hängen von δ nur über cos 3δ ab | — | kein cos δ (c₄ = 0), kein cos 2(δ − χ), keine Bindung an α′ |

**Gesamturteil nach Vorab: widerlegt.**

## Lesart
- **Die natürlichen kubischen Bausteine geben unter J das falsche Vorzeichen oder keines.** det W und Tr W³ haben Spur- und Nebendiagonal-Anteil mit gleichem Vorzeichen
  (X, Z > 0), ihr Quadrat liefert β₃ > 0 und wählt in beiden Sektoren den verworfenen Zweig. Spurfreie Bausteine (X = 0) und reine Spurbausteine (Z = 0) wählen nichts.
- **Nachträglich bemerkt (nicht in der Vorab-Notiz):** Das Vorzeichen der Daten kommt im vollen Quadrat nur aus dem **J-verbotenen** Teil. Für det W ist der cos 3δ-Anteil
  von N² gleich 4φr³(φ² − 3r²); bei K = ⅔ (φ² = 2r²) überwiegt −12φr⁵ den J-erlaubten Teil +4φ³r³. Ebenso hat e₁e₂ − 9e₃ (verschwindet bei drei gleichen Eigenwerten)
  nur den J-verbotenen Kreuzterm −648φr⁵ cos 3δ und wählt voll den Daten-Zweig. Das Vorzeichen, das die Daten verlangen, und das Postulat J in der Ebenen-Lesart stehen
  damit bei Ordnung 6 gegeneinander, sobald der Term aus einem Quadrat kommen soll.
- **Bindung an den Spin-1-Term ist strukturell ausgeschlossen:** mit festem κ wegen der entgegengesetzten Vorzeichen von α′ (a); über Spur und Determinante, weil diese
  den Mischungswinkel χ nicht sehen (d). Ein Elternterm müsste die Konjugation σ bzw. χ enthalten und dabei zwischen χ = 0 und χ = π/4 das Vorzeichen wechseln
  (etwa über cos 4χ); einen solchen Term liefert der Rahmen bisher nicht (nicht gerechnet).

## Hergeleitet, gesetzt, nachträglich
- **Gerechnet:** β₃(J) für die ganze kubische Invariantenfamilie (symbolisch), Zweigwahl je Kandidat, J-projiziert und voll.
- **Gesetzt:** Elternterm der Form u²; J in der Ebenen-Lesart (H157/H158); Zirkulante in H₃(ℂ); K = ⅔; φ > 0; Sektorvorzeichen von α′ (H168).
- **Nachträglich:** Daten-Vorzeichen nur aus J-verbotenen Teilen (N², e₁e₂ − 9e₃).

## Folgerung für den Strang
Die Weggabel aus k436 ist enger geworden: Entweder wird das Vorzeichen gesetzt (es wird dann durch die Daten mit 51σ geprüft, H222), oder J gilt bei Ordnung 6 nicht in
der Ebenen-Lesart — dann wäre N² zulässig und Stabilität gäbe das richtige Vorzeichen. Das zweite wäre eine Änderung an einem Postulat und gehört dem Autor.

## Grenzen
Nur Elternterme u² mit u aus Spur und Determinante der H₃(ℂ)-Zirkulante; Produkte verschiedener Bausteine, Terme mit σ/χ und oktonionische Bausteine (A₄-Vorzeichenpaare,
cos δ) nicht gerechnet. Baumniveau. Kein Guard berührt; OP3/OP4 offen.

## Dateien
`Vorab_H223_Elternterm_Vorzeichen.md`, `k437_test_h223.py`/`k437_out.txt`, `k437b_gegenprobe.wl`/`k437b_out.txt`.

Vergeben: H223, k437. Nächste frei: H224, k438 (vor Vergabe gegen `main` prüfen).
