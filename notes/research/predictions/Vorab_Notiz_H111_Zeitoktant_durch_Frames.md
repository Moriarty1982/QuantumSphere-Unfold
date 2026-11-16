# Vorab-Notiz H111: Generationen aus dem Zeitzyklus, ausgelesen über die Frame-Abbildungen

Festgelegt am 2026-11-16, **vor** der Rechnung. Auftrag des Autors: „Ja, H111 vorab“, nach dem Vergleich der zwei Walzenraster
(`../op3_topology_core_2026_11_16/README.md`, Nachtrag „Die zwei Walzenraster verglichen“). Einordnung OP3, r16.4, r16.7, r16.9, r14. Skript
`k233_test_h111.py` (nach dieser Notiz geschrieben, ausgeführt erst nach dem Commit und nach Freigabe durch den Autor).

## Anlass
Der Vergleich zeigte zwei Oktanten mit derselben Phase π/4: den **Frame-Oktanten** (Ecken e_R, e_T, e_J = +1-Eigenzustände von R = σ_z, T = σ_x,
J_B = σ_y; r16.7; Symmetrieachse (1, 1, 1); Viertelraster) und den **Zeit-Oktanten** (Bahn des Drittelzyklus um die Helizitätsachse mit Überlappung ½;
r16.9; Triolenraster). Die Dreierachsen stehen im magischen Winkel; gemeinsam haben beide Raster nur J_B. Jedes Bild für sich gibt π/4. Geprüft wird
eine Konstruktion, die beide verbindet: Die Generationen kommen aus dem Zeitzyklus, die Auslesung geschieht über die Frame-Eigenzustände.

## Vorwissen geprüft
- r16.4 (Gram-Lesart: √m = Eigenwerte der Gram-Matrix der Auslesezustände; „the three states are readout states, not mass eigenstates“), r16.7, r16.9.
- `../op3_topology_core_2026_11_16/` (zwei Raster, magischer Winkel, gemeinsames Element J_B).
- H106–H110 und die Korrekturterm-Linie (`../op3_correction_term_2026_11_16/`): reine Bilder geben π/4 bzw. 0,679; Biegung braucht eine Verbindung oder
  eine stetige Eingabe.
- Eine Kreuz-Gram-Konstruktion zwischen zwei Oktanten ist im Bestand nicht gefunden (Suche nach „Kreuz-Gram“, „cross-Gram“, „Zeit-Oktant“).

## Festgelegte Konstruktion
- **Zeit-Oktant:** g_l = kohärenter Spin-½-Zustand bei Polarwinkel θ = arccos(1/√3) um eine Helizitätsachse ±z, Azimut φ₀ + 120°·l (l = 0, 1, 2).
- **Lage durch J_B festgelegt:** Eine Generation liegt in der Ebene, die die J_B-Achse (y) und die Helizitätsachse enthält. Modulo 120° gibt das zwei
  nicht gleichwertige Azimute: **φ₀ = 90°** (Generation auf der Seite +y) und **φ₀ = 30°** (eine Generation bei 270°, Seite −y).
- **Helizitätsachse:** **+z** oder **−z** (J_B bildet den einen Zeit-Oktanten auf den anderen ab).
- **Auslesung:** Kreuz-Gram-Matrix A_kl = ⟨e_k | g_l⟩ mit e_k ∈ {e_R, e_T, e_J}. Als √m gelten die **Singulärwerte** von A (Verallgemeinerung der
  Gram-Lesart von r16.4 auf zwei Zustandsfamilien; unabhängig von der Zuordnung k ↔ l und von Phasen der Zustände).
- Aus den drei √m: K = Σσ² / (Σσ)² und die Brannen-Phase 3δ (Fourier-Zerlegung wie in `../op3_chain_diagnosis_2026_11_16/chain.py`).

Das ergibt **4 Versuche** (φ₀ ∈ {30°, 90°} × Achse ∈ {+z, −z}). Kontrolle (nicht gezählt): Ersetzt man den Zeit-Oktanten durch den Frame-Oktanten
selbst, muss die Kreuz-Gram-Matrix die gewöhnliche Gram-Matrix sein und K = 2/3, 3δ = π/4 geben.

## Entscheidungskriterium (vor der Rechnung festgelegt)
- Treffer: |K − 2/3| ≤ 0,001 **und** |3δ − 0,666674| ≤ 0,0002.
- **bestätigt**, wenn genau ein Versuch trifft; **mehrdeutig** bei mehr als einem; **widerlegt** bei keinem.
- Zufallserwartung, vorab geschätzt: 4 Versuche, je höchstens etwa 0,7 % für die Phase, K zusätzlich einschränkend: unter 0,03.

## Offenlegung
- Der Zielwert ist bekannt; blind ist der Test nur in der Konstruktion.
- Die Kreuz-Gram-Lesart (Singulärwerte als √m) ist eine Setzung; andere Verbindungen (Sechseck-Schleife, Lüders-Projektion) werden nicht geprüft.
- Die Lage durch J_B ist die einzige Festlegung ohne freien Parameter, die beide Raster teilen; sie ist eine Setzung.

## Ablauf
1. Diese Notiz und das Skript committen.
2. Nach Freigabe `k233_test_h111.py` ausführen (Ausgabe `k233_out.txt`).
3. Ergebnis-Notiz `Ergebnis_H111_Zeitoktant_durch_Frames.md`.
