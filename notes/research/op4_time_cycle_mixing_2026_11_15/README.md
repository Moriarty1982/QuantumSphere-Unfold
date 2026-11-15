# OP4: Der Zeitzyklus als Dreierzyklus der Dirac-Auslesung

15. November 2026, Claude Opus. **Erkundung, nicht blind** (TM2 und seine Spannung mit JUNO waren bekannt). Auftrag des
Autors: „Ja, prüfen“. Keine H-Nummer, kein CT-Eintrag, Guards unverändert. Skript `time_cycle_mixing.py`, Ausgabe
`run/time_cycle_mixing_stdout.txt`.

## Vorwissen geprüft
- **H39 (v4.9.0-r55):** Jede Teilchenart liest ihre Masse in der Basis einer Untergruppe von A₄. Dirac-Kopplungen (u, d, e)
  sind zirkulant, also invariant unter dem Slotzyklus τ ≅ ℤ₃; Neutrinos (Majorana) lesen mit einer Gruppe G_M, die die Struktur
  nicht festlegt. Mit G_M ≅ ℤ₂ und fester Spalte ν₂ entsteht TM2, sin²θ₁₂ = 1/(3 cos²θ₁₃) ≈ 0,341, 3,6σ über JUNO; die
  Maske aus r57 korrigiert das.
- **H6 (v4.8.0-r12):** Die Diedergruppe S₃ mit der Triole wählt die Fortsetzung mit θ₁₃ = 0.
- **r16.9:** Die Verschiebung um ein Drittel der Periode von s(t) ist ein natürlicher Dreierzyklus auf (s₊, w, s̄₋); die
  Masseneigenzustände sind die drei Frequenzanteile, die Auslesezustände ihre Bahn.
- **r38:** Transposition ρ der Slots (fixiert Slot 1, tauscht 2 und 3).
- **H9** (offen): sin²θ₁₂ = 0,3086; geprüft wird an der nächsten JUNO-Messung mit σ ≤ 0,004. Eine solche Veröffentlichung
  wurde am 15.11. nicht gefunden.

## Ergebnisse
1. **Zeitzyklus und Slotzyklus sind gleichwertig.** Die Fourier-Matrix diagonalisiert τ mit den Eigenwerten 1, ω, ω̄, genau
   denen der Zeitverschiebung auf (w, s̄₋, s₊). Unter dieser Zuordnung sind die **Slotzustände die drei gleich gewichteten
   Auslesungen** zu den Zeiten 0, T/3, 2T/3 (|Komponenten|² = ⅓ auf jedem Frequenzanteil), die **Fourier-Moden die
   Masseneigenzustände** der geladenen Leptonen.
2. **Die Frame-Abbildung T fixiert jeden Slotzustand.** Sie wirkt auf den Slots als komplexe Konjugation, nicht als die
   Transposition ρ. (Erwartet war vor dem Lauf ρ; das trifft nicht zu.)
3. **Die beiden ℤ₂-Kandidaten für die Neutrinos:**
   - die A₄-Vorzeichenmatrix diag(1, −1, −1) aus r55: feste Spalte mit |U|² = (⅓, ⅓, ⅓), also **TM2**; in diesem Bild ist ν₂
     die gleich gewichtete Auslesung zur Zeit 0, eine Slotrichtung. sin²θ₁₂ = 0,3409 gegen JUNO 0,3092 ± 0,0087;
   - die Transposition ρ: feste Spalte |U|² = (0, ½, ½), also θ₁₃ = 0 bzw. die von H6 gewählte, ausgeschlossene Fortsetzung.

## Folgerungen
- **Was trägt:** Der Dreierzyklus der Dirac-Auslesung aus r55 hat im Zeitzyklus eine physikalische Lesart. Die Flavourbasis
  der geladenen Leptonen ist die Basis der Frequenzanteile von s(t), die Slotbasis die der Auslesezeitpunkte. TM2 heißt
  dann: Ein Neutrino-Masseneigenzustand ist die gleich gewichtete Auslesung zu einem Zeitpunkt.
- **Was nicht trägt:** Die ℤ₂ der Neutrinos hat keine Frame-Herkunft. Die Vorzeichenmatrix (zwei Auslesungen mit Minus) ist
  weder eine Zeitverschiebung noch eine Frame-Abbildung; die Zeitumkehr T fixiert alle Slots; die Transposition ρ gibt
  θ₁₃ = 0. Eine Zahl folgt nicht, und die Spannung von TM2 mit JUNO bleibt.
- **Kein Test.** Die Lesart erklärt das bekannte Muster, sagt aber nichts Neues voraus. H9 bleibt der offene Prüfstein für θ₁₂.

OP4 bleibt offen. OP1–OP5, C5, C6/T2 und die Guards sind unverändert.

## Nachtrag 15.11.2026: Die Neutrino-ℤ₂ als Zentrumselement von Spin(8)
Auftrag des Autors: „Ja, prüfen“. **Erkundung, nicht blind** (TM2, r38.1(c) und die Treffer von H41 waren bekannt; die
Aufteilung der Treffer nach festem Slot ist eine nachträgliche Auswertung derselben Daten). Skript `spin8_center_z2.py`,
Ausgabe `run/spin8_center_z2_stdout.txt`.

1. **(1, −1, −1) ist die Fermionparität von Spin(8).** In Cl(8) ist die Drehung um 2π auf dem Vektor +1 und auf beiden
   chiralen Spinoren −1. Auf den Trialitäts-Slots (8_v, 8_s, 8_c) ist das genau das Vorzeichentripel aus r38.1(c), das als
   ℤ₂ der Neutrinos (r55) TM2 erzeugt.
2. **Eine Majorana-Matrix mit dieser Invarianz gibt TM2.** Für 500 zufällige symmetrische Matrizen mit D M D = M,
   D = diag(1, −1, −1), ist die feste Spalte in der Flavourbasis exakt (⅓, ⅓, ⅓). Der Vektor-Slot entkoppelt; ν₂ ist der
   Vektor-Slot, im Zeitbild die gleich gewichtete Auslesung zur Zeit 0.
3. **Die Maske aus r57 unterscheidet die drei ℤ₂.** Mit der Lepton-Maske W_l = (0, 0, −3) (Variante A von H41, gleiche Daten
   und Raster wie k97) treffen nur die ℤ₂, deren fester Slot das Maskengewicht 0 hat: Slot 1 und Slot 2 je 388 Treffer
   (zusammen die 776 von H41), Slot 3 keinen. Nach r47 hat der Bezugsslot stets das Gewicht 0 („beide Chiralitäten stimmen
   dort überein“). **Die Lesart „fester Slot = Vektor-Slot = Bezugsslot“ ist damit mit H41 verträglich.** Zwischen Slot 1 und
   Slot 2 entscheidet die Lepton-Maske nicht.

**Folgerung:** Die bisher freie Gruppe G_M der Neutrinos (r55) lässt sich als (−1)^F von Spin(8) lesen, im Bezugssystem, in dem
ein maskenfreier Slot der Vektor ist. Die Majorana-Kopplung respektiert die Fermionparität der Trialität, die Dirac-Kopplung
den Zyklus τ. Neu ist die Begründung, nicht das Muster: Es bleibt TM2 mit Maskenkorrektur, θ₂₃ frei, keine neue Zahl.
Gesetzt bleiben: warum Majorana (−1)^F respektiert und Dirac nicht (Lesart: ein Feld mit sich selbst gegen links an rechts),
die Zuordnung der Generationen zu den Trialitäts-Slots (r37) und die Wahl des Vektor-Slots.
