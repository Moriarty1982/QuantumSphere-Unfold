# Ergebnis H161: Das RAID-Bild gilt für die Etiketten und für zwei Köpfe, nicht für einen Kopf und nicht für einen Datenstrom

**Stand:** 2026-11-26. Vorab-Notiz: `notes/research/predictions/Vorab_Notiz_H161_Spinor_Lesekopf_XOR.md` (Commit b29cc1c, vor dem ersten Lauf).
**Überwiegend nicht blind:** Alle fünf Einzelergebnisse standen als Lehrbuchwissen vor der Rechnung fest und sind so in der Vorab-Notiz offengelegt.
Skripte: `k352_test_h161.py` (Qiskit 2.6.2 mit Aer 0.18.4 für die Messabläufe, sympy/numpy für die Algebra), `k352b_gegenprobe.wl` (Wolfram, exakt),
`k352c_nachtrag_seed.py` (**nachträglich**, Kontrolle der Zufallsströme). Ausgaben: `k352_out.txt`, `k352b_out.txt`, `k352c_out.txt`.
Werkzeugwahl: Qiskit, weil die Aussage ein explizit definierter Messablauf ist; Wolfram für die exakte Algebra. Kein HDL/MMA-Vergleich (RUN_TAPE nicht berührt;
„Band“ ist hier das Bild des Autors, nicht das QAM-Band). Kein Guard berührt.

## Frage
Idee des Autors (26.11.2026): Bei kugelförmigem Kern zeigt sich der gemittelte Umlauf als Spinor auf der Oberfläche, wie ein zweigeteilter Lesekopf über demselben
Band, dessen Auslesen per XOR den Datenstrom rekonstruieren (RAID5). Liegen die Punkte nicht gegenüber, soll eine Verbiegung der Geometrie die Bahnen wieder zu
Kreisen machen, und die Paritätsrekonstruktion erzeugt ein virtuelles drittes Objekt.

## Urteil nach den vorab festgelegten Kriterien
| Kriterium | Vorhersage | Ergebnis |
|---|---|---|
| K-a Etiketten bilden GF(2)², X ⊕ Z = Y | bestätigt | **bestätigt** |
| K-b zwei Köpfe: YY-Bit = XX-Bit ⊕ ZZ-Bit ⊕ c | bestätigt | **bestätigt** (c = 1) |
| K-c ein Kopf: Y-Bit = X-Bit ⊕ Z-Bit | widerlegt | **widerlegt** (Trefferquote 0,51) |
| K-d klassischer Datenstrom (Peres–Mermin) | widerlegt | **widerlegt** (höchstens 5 von 6) |
| K-e Verbiegung auf Gegenpunkte, kreistreu | bestätigt | **bestätigt** |
| Gesamt | trägt teilweise | **trägt teilweise** |

## Befunde
1. **Etiketten (K-a).** Ohne Phase bilden I, X, Z, Y die Gruppe GF(2)² mit X = (1|0), Z = (0|1), Y = (1|1). Je zwei der drei geben per XOR das dritte, genau wie
   drei RAID5-Platten. Das Vorzeichen hängt an der Reihenfolge: X·Z = −iY, Z·X = +iY (Wolfram: exakte Nullmatrizen).
2. **Zwei Köpfe (K-b).** Für zwei Qubits vertauschen XX, ZZ und YY, und (XX)(ZZ) = −YY (exakt). In Qiskit nacheinander gemessen, ist das YY-Bit in allen 4096
   Läufen XX-Bit ⊕ ZZ-Bit ⊕ 1, für alle vier Bell-Zustände **und** für drei Zufallszustände. Die dritte Auslese ist also immer rekonstruierbar, und die Parität
   der drei Platten ist immer ungerade. Bell-Zustände: Φ⁺ (0,0,1), Φ⁻ (1,0,0), Ψ⁺ (0,1,0), Ψ⁻ (1,1,1). Die zwei Bits XX und ZZ benennen den Bell-Zustand.
3. **Ein Kopf (K-c).** Auf einem einzelnen Spinor nacheinander X, Z, Y gelesen, trifft X-Bit ⊕ Z-Bit das Y-Bit in 49,4 % bis 52,6 % der Läufe (Mittel 51,2 %).
   Exakt ist die Wahrscheinlichkeit ½ (Wolfram). Die zwei Hälften eines einzelnen Kopfs stören einander; ihre Auslesen enthalten das dritte Bit nicht.
   Ohne Messung gilt nur x² + y² + z² = 1: Der Betrag von y folgt aus x und z, sein Vorzeichen nicht. Es fehlt genau ein Bit.
4. **Datenstrom (K-d).** Für die neun Zwei-Qubit-Größen des Peres–Mermin-Quadrats erfüllt keine der 512 Belegungen mit ±1 alle sechs Paritätsprüfungen;
   höchstens fünf (96 Belegungen; Wolfram: Verteilung 96 mit einer, 320 mit drei, 96 mit fünf erfüllten). In Qiskit sind alle sechs Prüfungen in 4096 von 4096
   Läufen erfüllt (fünf gerade, eine ungerade). Jeder einzelne RAID-Satz ist also in sich stimmig, aber es gibt kein festes Band, das alle Sätze zugleich bedient.
   Die Werte entstehen beim Lesen.
5. **Verbiegung und drittes Objekt (K-e).** Zu zwei Richtungen im Winkel θ gibt es eine Möbius-Abbildung der Kugel (als Lorentz-Transformation: ein Boost mit
   β = cos(θ/2) längs der Winkelhalbierenden), die sie auf Gegenpunkte legt und Kreise auf Kreise abbildet (exakt im symmetrischen Fall; 1000 Zufallspaare und
   Zufallskreise, Reste 10⁻¹³). Erhalten bleibt die invariante Masse M² = 2E₁E₂(1 − cos θ); im verbogenen System trägt jeder Strahl E′ = M/2.
   Zwei masselose Strahlen, die nicht parallel laufen, haben zusammen eine Ruhemasse und ein Ruhesystem. **Das ist ein drittes Objekt im wörtlichen Sinn:**
   Es gehört keinem der beiden Strahlen allein, und es ist genau die Größe, die die Verbiegung festlegt. Für die Spinoren gilt |⟨ψ₁|ψ₂⟩| = cos(θ/2) = β: Der
   Überlapp der zwei Köpfe ist die Geschwindigkeit des Systems, in dem sie gegenüberliegen; nach der Abbildung sind die Spinoren orthogonal (Rest 10⁻¹⁴).

## Nachträglich (k352c): Zufallsströme
Das Mittel 0,5116 in K-c liegt weiter von ½ als die Zählstatistik des Mittels (0,0017) erwarten lässt. Ursache ist der Simulator, nicht die Schaltung: `k352`
benutzt für alle Schaltungen denselben Startwert, die Läufe sind dadurch nicht unabhängig. Mit benachbarten Startwerten bleibt der Effekt (Mittel 0,4893),
mit weit getrennten Startwerten verschwindet er (200 Zustände: Mittel 0,50029, 0,6 Standardfehler von ½), ebenso bei 2 000 000 Läufen einer Schaltung (0,50024).
Das Urteil zu K-c (50 % ± 5 %) ist davon nicht berührt; der registrierte Lauf bleibt unverändert stehen.

## Einordnung
- Das RAID-Bild trifft etwas Richtiges: Innerhalb eines Satzes vertauschender Auslesen ist die dritte die Parität der beiden anderen. Das ist die Struktur der
  Stabilisator-Codes.
- Es trägt nicht für einen einzelnen Spinor (ein Kopf, drei Leserichtungen) und nicht als Aussage „es gibt einen ursprünglichen Datenstrom“. Die Quantenmechanik
  ist an dieser Stelle strenger als RAID5: Die Paritäten stimmen, obwohl kein Band dahinter liegt.
- Das „virtuelle dritte Objekt“ hat zwei genaue Fassungen, die zusammenpassen: die dritte Platte YY (Parität) und die invariante Masse des Paares (Geometrie).
- Zahl ohne Zuordnung: β = β_sym = 0,5494 entspräche θ = 113,35°. Ob der Winkel zwischen zwei Auslesen im Modell diese Rolle spielt, ist nicht untersucht.

## Grenzen
Übersetzung gesetzt (Spinor = Qubit, Platte = Pauli-Auslese, Verbiegung = Möbius-Abbildung). Idealer Simulator ohne Rauschen. Keine Größe des Companion geht
ein; eine Zuordnung zu Kern, Band oder Frames wird nicht behauptet. H137 (Bandschaltung bleibt klassisch) ist nicht berührt. OP1 bis OP5 bleiben offen.
