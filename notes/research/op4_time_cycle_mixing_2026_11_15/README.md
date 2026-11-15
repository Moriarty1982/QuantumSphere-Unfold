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
