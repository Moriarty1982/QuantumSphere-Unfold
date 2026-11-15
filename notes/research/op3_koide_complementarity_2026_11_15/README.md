# OP3: Koide 2/3 als vollständige Komplementarität eines Qubits

15. November 2026, Claude Opus. **Erkundung, nicht blind**: Koide 2/3 und die Zahl drei der Generationen waren bekannt.
Auf „weiter“ des Autors festgehalten, nach `../op3_spin1_triangle_2026_11_15/README.md` (Koide verlangt drei Zustände
auf halbem Fubini–Study-Weg zwischen gleich und orthogonal). Keine H-Nummer, kein CT-Eintrag, Guards unverändert.
Skript `mub.py`, Ausgabe `run/mub_stdout.txt`.

## Vorwissen geprüft
- **Oktanten-Tripel** (r12): drei Spin-½-Zustände an orthogonalen Achsen, Überlappung ½, Phase π/4.
- **r13.2:** Auf dem neutralen Qubit N (unter CT-003) ist i R_e7, i R_e15, i R_e8 ein Pauli-Tripel. Der Bezug, ein
  Eigenzustand einer Hurwitz-Einheit der Ordnung 3, hat eine Bahn mit Überlappung ½ (Konstruktion mit bekanntem Ziel).
- **r14.3(b):** gegenseitig unverzerrte Basen der Weyl-Gruppe in Dimension 3, im Zusammenhang der Bezugsauswahl.
- **r63.2:** Robertson-Sättigung; das Paper baut auf dem Heisenberg-Kompensator auf.
- Die Lesart „ein Zustand je komplementärer Basis eines Qubits“ steht im Repo nicht; Volltextsuche nach unbiased,
  unverzerrt und komplementär fand nur r13.6 (komplementäre Wege) und r14.3(b).

## Befund
1. **Der Oktant ist ein vollständiger Satz komplementärer Messungen.** Seine drei Zustände sind je ein Eigenzustand von
   σx, σy und σz, also je einer aus jeder der drei gegenseitig unverzerrten Basen eines Qubits. Überlappung ½ heißt
   hier: Misst man einen Zustand in der Basis eines anderen, ist das Ergebnis ein Münzwurf.
2. **Zählung (Wootters–Fields, geprüft für d = 2, 3, 5, 7).** In Dimension d gibt es höchstens d + 1 gegenseitig
   unverzerrte Basen mit paarweiser Überlappung 1/d. Nimmt man aus jeder Basis eines vollständigen Satzes einen Zustand,
   erhält man N = d + 1 Zustände mit
   **K = Tr G²/(Tr G)² = 2/(d + 1) = 2/N**
   (geprüft: d = 2 → 2/3, d = 3 → 1/2, d = 5 → 1/3, d = 7 → 1/4). Der Rang ist höchstens d < N, also verschwindet stets
   mindestens eine Masse.
3. **Nur d = 2 gibt drei Zustände.** Drei Generationen als vollständig komplementäre Lesarten eines Zustands verlangen
   d = 2 und geben K = 2/3. Die beiden Zahlen „drei Generationen“ und „Koide 2/3“ wären in dieser Lesart eine einzige
   Aussage: **K = 2/N bei N = 3.**

**Berichtigung einer Aussage im Gespräch:** Die Tabelle mit K = (1 + 2/d)/3 und der Querbezug „K = 5/9 entspricht
d = 3“ gelten nur für *drei* Zustände aus verschiedenen Basen, nicht für einen vollständigen Satz. Für den vollständigen
Satz gilt K = 2/(d + 1). Die Kernaussage (nur d = 2 gibt drei Basen und K = 2/3) bleibt.

## Einordnung
- **Spin ½ statt Spin 1:** Die Lesart verlangt den Qubit-Oktanten, also flache Achsen mit einer Masse null. Das
  Spin-1-Dreieck ist nicht gegenseitig unverzerrt. Die Biegung zu den echten Massen bleibt Sache des Kerns (γ_M, OP1).
- **Leichtes Elektron:** Die Leptonen liegen nahe am flachen Grenzfall, in dem eine Masse verschwindet. Das passt zu einer
  sehr kleinen Elektronmasse, ist aber nur eine qualitative Übereinstimmung.
- **Generation und Spin:** Nach `../op3_cs_dixon_map_2026_11_15/README.md` sitzen die Generationen über Farbe und
  Ladung am Platz des Spins. Die Lesart hier macht die drei Generationen zu den drei komplementären Lesarten eines
  Spin-½-Zustands; beides ist verträglich.
- **Nativ unter CT-003:** r13.2 realisiert genau diese Struktur auf N (Pauli-Tripel, Hurwitz-Zyklus vertauscht die drei
  Basen zyklisch). Neu ist die Deutung und die Eindeutigkeit von d = 2.

## Annahmen und Grenzen
- **Nicht blind;** keine neue Zahl.
- **Zwei Prinzipien sind gesetzt:** „ein Generationszustand je komplementärer Basis“ und „vollständiger Satz“. Beide sind
  nicht aus dem Bestand hergeleitet.
- **Die Ladungsneutralität** des Qubits hängt weiter an CT-003.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert.
