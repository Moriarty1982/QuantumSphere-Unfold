# Erkundung: Struktur des Ω-erweiterten OP5-Symbols (Grad 5 bis 10)

Stand: 2. November 2026, Fortsetzung von `Gegenpruefung_OP5_Stand_cf48496.md`.
Erkundung ohne Vorab-Notiz; keine Vorhersage, kein Existenzsatz.
Eingaben: `completion-omega-witness.npz` (J = vervollständigtes Erstordnungssymbol 32×96, θ = Ω-Kovektor 480, beide float64)
und der 70-stellige Keim bei (1, 3/5, 0, 0) aus `analysis/op5-field-slices/state-sufficiency-2026-10-30`.
Skripte: `k110`–`k124` (Aufruf jeweils mit dem Pfad dieses Analyseordners als Argument).

## Ausgangsfrage

In der Ausgangsnotiz `RANK_RESOLUTION_2026-10-30.md` ergab die Spencer-Zählung H^{5,2} je nach Schwelle 1, 0 oder −1.

## Befunde

1. **Die −1 ist ein Artefakt.** Die bei Schwelle 1e-11 zusätzlich gezählte Bildrichtung (σ ≈ 1,4e-10) liegt zu 98 % außerhalb
   des Kerns der ausgehenden Abbildung, verletzt also δ² = 0 (k110). Projiziert man das Bild zuerst auf den Kern, wird die
   Zählung nie negativ.
2. **Exakte Zählregel.** Mit H^{6,1} = 0 (Prolongation) und dem stabilen Ausgangsrang 1024 gilt H^{5,2} = dim g_7 − 722.
3. **Direkter Aufbau des Symbols, saubere Lücken (≥ 5e-8 gegen ≤ 3e-15):**

   | Grad | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
   |---|---|---|---|---|---|---|---|---|---|
   | ohne Ω | 127 | 209 | 312 | 437 | 585 | 757 | 954 | | |
   | echtes θ | 127 | 208 | 308 | 427 | 565 | 726 | 910 | 1118 | 1351 |
   | zufälliges θ | 127 | 208 | 308 | 427 | 565 | 722 | 898 | 1093 | |

   Mit dem gespeicherten θ folgt H^{5,2} = 4. Die alte rekursive Zählung war durch eine schlecht konditionierte Basis
   von g_6 (σ ≈ 5e-8) verrauscht.
4. **θ liegt exakt auf einem Sonderort.** Zufällige Störung um ε lässt die vier zusätzlichen Nullwerte bei Grad 7
   linear in ε wachsen (k113).
5. **Ω ist blind für die freie Richtung.** Generisch hat J(ξ) einen eindimensionalen Kern k(ξ), das ist eine freie Funktion
   von vier Variablen. Es gilt θ(ξ)·k(ξ) ≈ 1e-15 für das echte θ, gegen 1e-2 bei zufälligem θ (k123). Deshalb
   wächst die Hilbert-Funktion ab Grad 7 wieder kubisch, und Ω legt die freie Funktion nicht fest.
6. **Die vier Grad-7-Beziehungen** haben die Form c_k(∂)Ω ∈ ⟨J⟩ mit c_k = q·d_k (k116–k119):
   - q ist exakt der Lichtkegel des Coframes. In Rahmenkomponenten η = Vᵀξ ist q gleich diag(1,−1,−1,−1),
     mit Abweichung 8e-13 (k121). Auf q = 0 verliert J(ξ) fünf Ränge.
   - Die d_k erzeugen das Ideal zweier reeller, windschiefer 2-Ebenen Π₀ (raumartig, (0,2)) und Π₁ (zeitartig, (1,1))
     im Kovektorraum. Hilbert-Funktion 12/25/44 exakt; die Ebenen sind nicht q-orthogonal.
   - Auf Π₀ ∪ Π₁ verliert J(ξ) einen weiteren Rang (k123). Die Ebenen gehören also zur charakteristischen Menge des
     ursprünglichen Systems.
   - Lesart: θ ist eine rationale Kombination der J-Zeilen mit Nenner auf Kegel ∪ Π₀ ∪ Π₁. Ω trägt nur dort neue
     Information.
7. **Herkunft der Ebenen noch offen.** Sie sind nicht aus Strom- und Spin-Bilinearen des Zustands gespannt (beste
   Übereinstimmung 11,7°, k122). Sie sind auch keine invarianten Ebenen von E⁻¹·Im(Ψ†QDΨ) oder der K-Varianten (≥ 32°, k124).
   Im Rahmen liegen die Ströme in (e₀,e₁) und der Spin entlang e₂.

## Grenzen

θ stammt vom älteren Keim (Abweichung etwa 1e-7). Die Exaktheit der Struktur (1e-15, linear wachsend unter Störung)
spricht für Struktur und gegen Zufall. Bestätigung erfordert θ in hoher Genauigkeit. Die Herkunft von Π₀ und Π₁ und
die Identität der freien Funktion sind offen.

## Folgerung für den Weg zu einem Existenzsatz

Erst die freie Funktion festlegen (Eichung), dann die Involutivität neu prüfen. Die Grad-5-Frage „0 oder 1“ war in
dieser Form falsch gestellt.
