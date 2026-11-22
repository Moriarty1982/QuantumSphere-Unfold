# Methoden-Notiz: Zeitumkehr- oder Spiegelbild in der Familie der vervollständigten ersten Jets (Erkundung, vor der Rechnung festgelegt)

22. November 2026. Auftrag des Autors: „weiter“ nach Runde v4.10.0-r42. Keine H-Nummer.
**Teilweise nicht blind:** Eine Abzählung lässt erwarten, dass jede Bildbedingung für sich lösbar ist: 31 unabhängige Bedingungen
und 40 Bildbedingungen stehen 96 freien Ableitungen gegenüber. Die Rechnung prüft, ob die Struktur das verhindert.

## Vorwissen geprüft
- r42: Am vorliegenden Jet ist Block 2 in den Ableitungen weder T-, R- noch I-Bild von Block 0 (relativ 1,28; 1,87; 0,72). Der Jet löst
  dort nur F = 0 und g = 0.
- `analysis/op5-field-slices/state-sufficiency-2026-10-30/PRECISION_COMPLETED_RESTART.md`, `precision_completed_root.py`,
  `precision-completed-root-result.json`: Die vervollständigten Bedingungen R = (F, G, dg) haben 32 Komponenten, davon 31 unabhängig, bei
  96 reellen ersten Ableitungen und festem ψ. Die gespeicherte Newton-Lösung ändert die Ableitungen nur um 1,7·10⁻¹⁴; sie ist eine Lösung
  einer Familie, kein eindeutiger Jet.
- r41: Werte am Keim: Block 2 ist bis auf 7,9·10⁻⁴ T- und R-Bild von Block 0.

## Werkzeug
Python mit mpmath, Auswertung von R über den vorhandenen Bau `precision_completed_rebuild.py` (Pfade als Argumente, keine festen Pfade
im neuen Skript), 40 Stellen. Wolfram nicht nötig (numerische Jacobi- und Kleinste-Quadrate-Rechnung an einem Punkt), Qiskit nicht
geeignet. Skript `jet_family_images.py`, Ausgabe `run/jet_family_images.txt`.

## Rechnung
1. **Ausgangsjet:** r42-Maß am vervollständigten Jet statt am primitiven.
2. **Familie:** Jacobi-Matrix von R nach den 96 Ableitungen am vervollständigten Jet; Rang; Dimension der Lösungsfamilie (linear).
3. **Bildbedingungen:** Für X ∈ {T, R, I} sind die 40 Gleichungen m_X = ∂_μF₂ − X(∂_μF₀) = 0 (10 normierte Fierz-Größen, 4 Richtungen)
   linear in den Ableitungen. Gemeinsames Newton-Verfahren (minimale Norm, 3 Schritte) für R = 0 und m_X = 0. Ergebnis: größter Rest von R,
   relative Bildabweichung max|m_X| / max|∂F₀| und Änderung der Ableitungen.
4. **Beide zugleich:** dasselbe für m_T = 0 und m_R = 0 gemeinsam.

## Raster (vorab)
Ein Bild heißt verträglich, wenn nach dem Verfahren |R| ≤ 10⁻²⁰ und die relative Bildabweichung ≤ 10⁻² ist.
- **Zeitumkehr entschieden:** T verträglich, R nicht.
- **Spiegelung entschieden:** R verträglich, T nicht.
- **unterbestimmt:** T und R je für sich verträglich. Dann entscheidet der erste Jet die Frage nicht, und der Befund „keines passt“ aus r42
  hängt an der gewählten Lösung. Ob beide zugleich gehen, wird zusätzlich angegeben.
- **keines verträglich:** Dann kann der Gegenstrom unter den Modellbedingungen in erster Ordnung kein lokales Bild sein; r42 wäre gestützt.

Frames: Keim im Materie-Frame M, Koordinaten des Vergleichsmodells. OP5 bleibt offen.
