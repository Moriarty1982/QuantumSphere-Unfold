# Vorab-Notiz H58: Cartan-Test des erweiterten Symbols mit konsistenten Daten (nicht blind)

Festgeschrieben vor der Rechnung (3. November 2026). **Nicht blind:** Die Zahlen aus H56/H57 sind bekannt. Betrifft nur das
OP5-Vergleichsmodell. OP5 bleibt offen.

## Änderung gegenüber H56/H57

Alle Bestandteile des Symbols kommen aus derselben exakten Linearisierung am reparierten Keim (`k142_lin2.npz`):

- J = A(0) (Grad-0-Koeffizient von A);
- θ (Ω-Bedingung) neu bestimmt wie die vier Bedingungen: K₃ = zulässige c₃ mit den Gleichungen vom Grad 2 (Jet bis
  Grad 2 fest), K₄ = dasselbe mit den Gleichungen bis Grad 3; θ = die Linearform auf K₃, die auf K₄ verschwindet;
- σ_k wie in H56 (`k144_bedingungen_p1.npy`), ohne Projektion;
- Eichzeile wie bisher.

Das gespeicherte θ aus `completion-omega-witness.npz` wird nicht verwendet.

## Gültigkeit

- dim K₃ − dim K₄ = 1.
- Ohne σ müssen sich die geeichten Dimensionen g'_p = 117, 188, 273, 371, 481, 606, 745, 898 (p = 2…9) ergeben.
- Jeder verwendete Rang hat eine Lücke ≥ 1e4; die drei Koordinatensysteme stimmen überein; dim g''_{p+1} ≤ Σ.

## Hypothese H58

Mit σ: dim g''_p = 477, 594, 723, 865 (p = 6…9); nicht involutiv bei p = 6 und 7, involutiv bei p = 8 (wie H56).

## Kriterium

- **Bestätigt:** alle Aussagen der Hypothese, bei erfüllter Gültigkeit.
- **Widerlegt:** gültiger Lauf mit anderem Ergebnis (zum Beispiel dim g''_8 = 724 und Involution bei p = 7).
- **Ungültig:** eine Gültigkeitsbedingung verletzt.

## Grenzen

float64. Die vier Bedingungen sind aus einem Rang mit kleinem Singulärwert (1e-9) bestimmt; ihre Genauigkeit liegt bei
etwa 1e-7 bis 1e-6. Reicht das nicht, ist echte Mehrgenauigkeit nötig.
