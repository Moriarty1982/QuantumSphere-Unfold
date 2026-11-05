# Ergebnis H77: Das Tachyonbild einer Wirkung ist nach Lesart B zu bilden

Vorab-Notiz `Vorab_Notiz_H77_Lesart_Tachyonbild.md`, Commit `d087d67` (nicht blind). Skripte `k192_lesart_tachyonbild.py` (Ausgabe `k192_out.json`) und `k192b_higgs_bild.py` (Nachrechnung, Ausgabe: M um 0 instabil, B um 0 stabil).

## Ergebnis (wie erwartet)
| Lesart | Dispersion | K1 tachyonisch | K2 masselos L_T = −L_M | K3 Energie der Mode entgegengesetzt | verträglich | Vakuumenergie eines konstanten V₀ |
|---|---|---|---|---|---|---|
| A: L_T = −L_M | ω² = k² + m² | nein | ja | ja | **nein** | −V₀ |
| B: X ↦ −X, Potential bleibt | ω² = k² − m² | ja | ja | ja | **ja** | +V₀ |
| B′: m² ↦ −m² | ω² = k² − m² | ja | nein | nein | **nein** | −V₀ |

Materie zum Vergleich: ω² = k² + m², mittlere Energie A₀²(k² + m²)/2, Vakuumenergie +V₀. Unter B hat eine laufende Mode (k > m) die mittlere Energie −A₀²(k² − m²)/2.

**H77 bestätigt:** Nur Lesart B ist mit r07.2 (Invariante wechselt das Vorzeichen), r20.2 (raumartige Vierergeschwindigkeit), H71 (tachyonische Masse), r81 (Kinetik s_T = −1) und F3 auf Auslesegrößen (Energie der Mode mit Phase −1) zugleich verträglich. Lesart A (Energieparität) erzeugt eine Geist-Kopie mit normaler Dispersion, also keinen Tachyon im Sinn von r20.

## Folgen (nach der Vorab-Notiz)
- **r82.1(b) ist nicht gedeckt.** Unter B behält ein Potential ohne Ableitungen sein Vorzeichen. Die Higgs-Vakuumenergie des Bildes hebt die der Materie nicht auf. Mehr noch (Nachrechnung `k192b_higgs_bild.py`, sympy): Unter B ist die Bewegungsgleichung des homogenen Higgs-Bildes φ̈ = +V′(φ). Um φ = 0 gilt φ̈ = −2μ²φ, der Ursprung ist **stabil**. Das Bild kondensiert also nicht, seine Vakuumenergie ist V(0) = 0, und die Summe ist a·V_min statt (a − b)·V_min. Das passt zur Tachyon-Abbildung: Die tachyonische Masse des Higgs in M wird im Bild eine normale Masse. r82.1(b) und (c) werden in der nächsten Runde korrigiert (append-only).
- **r82.2 (H74) bleibt gültig:** Eine laufende T-Mode unter B ist per Mode genau ein Oszillator negativer Energie mit Frequenz √(k² − m²), L = −½(q̇² − ω_T²q²). Das ist das Modell von H74.
- **r82.3 (H75) bleibt gültig:** Kinetische Energie und Energie-Impuls-Tensor bewegter T-Materie wechseln unter B das Vorzeichen (u ↦ iw), also negative träge und schwere Masse wie in H75.
- **H76 bleibt gültig:** Masselos stimmen A und B überein.
- **r82.4 (Torsions-Paarkanal) ist nicht berührt.**
- **Geist-Kondensation (Erkundung):** Unter B wird aus einer gesunden Materie-Seite X/2 + cX² die Form −X/2 + cX² mit stabilem Kondensat, eigenem Rahmen und w = −1. Das ist jetzt die Lesart, die zur Struktur passt; der Term cX² bleibt eine Eingabe.

## Einordnung
Mit B fällt der Mechanismus gegen das 10⁵⁵-Problem aus r82.1 weg. Stattdessen bietet B einen Mechanismus für Rahmen und Stabilität (Geist-Kondensation). Ob dessen Λ-artiger Beitrag mit der Higgs-Vakuumenergie zusammenhängt, ist offen. OP5 bleibt offen.
