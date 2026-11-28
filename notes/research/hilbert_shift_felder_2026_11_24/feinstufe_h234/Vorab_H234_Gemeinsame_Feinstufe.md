# Vorab H234 (k448): Tragen alle Feinwerte eine gemeinsame Feinstufe ε? (Grob/Fein)

**Datum:** 2026-11-28. Vor der Rechnung geschrieben und committet. Anlass: Marc 15:31 („Was ist, wenn unsere ganzen Eingaben Grob- und Feintuning
darstellen?“), Wahl 15:32 „Gemeinsame Feinstufe zuerst“. Werkzeuge: Python (`k448_test_h234.py`) mit Monte-Carlo-Zufallsabschätzung, Wolfram
(`k448b_gegenprobe.wl`) unabhängig für die Gitterreste. Qiskit nicht einschlägig.

## Frage
Die groben Werte sind diskret und hergeleitet (π/12, π/6, K = ⅔, Oktant, Achteldrehungen; nach H233 Rotorstellungen). Die feinen Werte sind kleine stetige
Abweichungen ohne Mechanismus. Spart ein Zwei-Stufen-Bild Eingaben? Das geht nur, wenn alle Feinwerte aus **einer** kleinen Zahl ε folgen:
F_i = c_i · ε^(n_i) mit einfachen Faktoren c_i und kleinen ganzen n_i.

## Vorwissen geprüft
H233 (Baumwerte sind Rotorstellungen, φ nicht), H221–H232 (φ ohne Herleitung), H196–H204 (D/B − 1 frei, Rang 4), k394–k396 (HC-Schleife mit Fixpunkt ½;
1/γ_L − ½ = mittlerer Casimir-Überschuss; nachträglich 2^(1−γ_L) ≈ β_sym), H213 (x_ν − x = 1,78σ), k358 (2σ-Fenster für β). Keine frühere Rechnung zu einer
gemeinsamen Feinstufe.

## Feinwerte (festgelegt)
| Nr. | Feinwert | grober Bezug | Wert | σ |
|---|---|---|---|---|
| F1 | φ (Lepton-Versatz) | Baumwerte π/12, π/6 | 0,0395773407 | 7,8·10⁻⁷ |
| F2 | β_sym − ½ | Fixpunkt ½ der HC-Schleife (k394), gesetzte Lesart | 0,0494056 | 1,8·10⁻⁴ (k358) |
| F3 | D/B − 1 (Quarks) | D = B (H196) | 0,0085 | 0,001 |
| F4 | x_ν − x | gleicher Versatz in beiden Sektoren | 0,00378 | 0,00213 |
Nicht aufgenommen: die Mischungswinkel (θ₁₃, θ₁₂ − TM1) folgen im Bild aus φ (H207) und sind nicht unabhängig.

## Grammatik (festgelegt)
c ∈ {1, 2, 3, 4, ½, ⅓, ¼, ⅔, 3/2, √2, 1/√2, √3, 1/√3, π, 1/π} (15 Werte), n ∈ {1, 2, 3}.
- **Lesart A:** ε := φ (der schärfste Feinwert setzt die Stufe). Für F2 bis F4 wird das beste (c, n) gesucht. Treffer, wenn |F_j − c·ε^n| ≤ 2σ_j.
- **Lesart B:** ε frei; auch φ = c₁·ε^(n₁). Gesucht ist ein ε, bei dem möglichst viele der vier Werte zugleich treffen. F1 muss treffen (σ bindet ε).

## Zufallsabschätzung
Monte Carlo: F2 bis F4 werden durch Zufallszahlen ersetzt, log-gleichverteilt in [10⁻³; 10⁻¹], mit denselben relativen Fehlern. Dann wird dieselbe Suche
ausgeführt (10⁵ Durchläufe). p = Anteil der Durchläufe mit mindestens so vielen Treffern wie beobachtet, getrennt für die scharfen Werte (F2, F3) und für alle.

## Offenlegung
Beim Aufstellen der Liste fiel mir auf: (β_sym − ½)/φ = 1,248, nahe 5/4. Der Faktor 5/4 ist **nicht** in der Grammatik und wird nicht gewertet, sondern nur
nachträglich mit Zufallsabschätzung berichtet. Sonst ist nichts vorab gerechnet. F4 hat einen großen Fehler (56 %) und trifft fast immer; das Monte Carlo
berücksichtigt das.

## Entscheidung
- **trägt:** In Lesart A oder B treffen F2 **und** F3 (die scharfen), und das Monte Carlo gibt p < 0,01 dafür.
- **trägt teilweise:** Nur einer der scharfen Werte trifft, mit p < 0,05.
- **widerlegt:** sonst. Dann sind die Feinwerte unabhängig, und das Zwei-Stufen-Bild spart keine Eingaben.

## Gesetzt
Liste der Feinwerte und ihre groben Bezüge (besonders ½ für β_sym), Grammatik (c, n), Intervall der Zufallszahlen.
