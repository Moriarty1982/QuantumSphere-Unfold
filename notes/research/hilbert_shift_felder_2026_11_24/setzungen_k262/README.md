# Welche Setzung aus H131 trägt die Spannung? (Erkundung k262, nicht blind, 25.11.2026)

**Ergebnis in einem Satz:** Die Spannung sitzt in der Setzung, dass die Neutrinos das **komplexe** Triplett z_k = s_k + i·v_k tragen. Dieselbe Gruppe aus k260
wirkt auf dem **Realteil** s_k allein (ohne Ladungsrichtung) als ganze S₄, linear und reell. Liest man die Majorana-Neutrinos dort, dann gibt ℤ₃ mit einer ungeraden ℤ₂
die TM1-Spalte (2/3, 1/6, 1/6) mit θ₂₃ = 45° und |sin δ| = 1, also genau das Muster von H8. In der Lesart von H131 erreicht kein Paar von Untergruppen die TM1-Spalte.

Auftrag: Autor „ja“ zur Zusammenführung von #301, danach laut Projektübersicht prüfen, welche Setzung die Spannung trägt. **Nicht blind:** Vor der Rechnung stand
analytisch fest, dass eine reelle Massenform in der Platzbasis nach dem Wechsel in die ℤ₃-Basis die μτ-Spiegelung erfüllt (Uₑ†Uₑ* ist die Vertauschung der beiden
komplexen Eigenrichtungen) und dass die ungerade ℤ₂ mit einfachem Eigenvektor (0, 1, 1)/√2 die TM1-Spalte gibt. Deshalb Erkundung, keine H-Nummer. Skripte **k262, k262b**.

Werkzeuge: Python (numpy) für die Gruppe aus k260, alle 30 Untergruppen und alle 900 Paare (G_e, G_ν) in zwei Lesarten, je 40 Stichproben. Wolfram Language exakt für
die TM1-Klasse (k262b). Qiskit nicht eingesetzt (keine Schaltung).

## Vorwissen geprüft
H131 (k261: TM2 mit J = 0), k260 (S₄, mit Ladung A₄), k256 (K∘S₀ hält die TM1-Spalte), H8 (Cayley–Dickson-Involution als CP: TM1, θ₂₃ = 45°, δ = 270°; im Register
„nach JUNO disfavorisiert“), H4 (TM1 gegen TM2; im Register „TM1 zunächst bevorzugt, nach JUNO disfavorisiert“), H39 (TM2, 3,6σ über JUNO), k280 (Kopplung wählt
(2/3, 1/6, 1/6) oder (0, 1/2, 1/2) je nach Vorzeichen), H125 (sin δ_PMNS < 0 erwartet). Literatur (aus Vorwissen, ungeprüft): A₄ mit verallgemeinerter CP und S₄ mit
ℤ₂ = SU geben diese Muster.

## Ergebnisse
1. **Wirkung auf s und v getrennt (k262, Teil 1):** Die 24 Elemente mischen s und v nicht (Rest 0). Auf s wirkt eine reelle vorzeichenbehaftete Permutation A,
   auf v wirkt +A (12 gerade Elemente, det A = +1) oder −A (12 ungerade, det A = −1). Die 24 Matrizen A sind verschieden. **Auf s allein ist die Gruppe also die volle
   S₄, linear.** Antilinear werden die ungeraden Elemente erst auf z = s + i·v, weil sie v gegen s umkehren. Die Gruppe hat 30 Untergruppen (wie S₄).
2. **Lesart A, wie H131 (Teil 2):** Neutrinos auf z, ungerade Elemente antilinear. Über alle 900 Paare von Untergruppen: 240 mit entarteten geladenen Leptonen,
   352 mit entarteten Neutrinos, der Rest in 19 Klassen. **Keine Klasse hat die feste Spalte (2/3, 1/6, 1/6).** Feste Spalten sind nur (1/3, 1/3, 1/3), (0, 1/2, 1/2),
   (1/4, 1/4, 1/2) und (0, 0, 1). Die Klasse aus H131 erscheint wieder (ℤ₃ mit einer Gruppe der Ordnung 4 mit zwei ungeraden Elementen: trimaximale Spalte, J = 0, 24 Paare).
3. **Lesart B (Teil 3, 4):** Neutrinos auf s, Massenform reell, alle 24 Elemente linear. ℤ₃ (4 Gruppen) mit einer ungeraden ℤ₂ (6 Gruppen) gibt 24 Paare in **zwei** Klassen:
   - 12 Paare: feste Spalte **(2/3, 1/6, 1/6)**, zwei Zeilen gleich, J frei. In 2000 Stichproben sin²θ₂₃ = 0,500000 und |sin δ| = 1,000000;
     sin²θ₁₂ = 1 − 2/(3 cos²θ₁₃) auf 7·10⁻¹³; sin²θ₁₃ frei. Bei sin²θ₁₃ = 0,022: **sin²θ₁₂ = 0,3183**.
   - 12 Paare: feste Spalte (0, 1/2, 1/2), J = 0. Als dritte Spalte heißt das θ₁₃ = 0 (ausgeschlossen).
   ℤ₃ mit der geraden ℤ₂: trimaximale Spalte, zwei Zeilen gleich, J frei (TM2 mit μτ-Spiegelung). ℤ₃ mit einer Vierergruppe aus einer geraden und zwei ungeraden
   Spiegelungen: alle drei Spalten fest, (2/3, 1/6, 1/6), (1/3, 1/3, 1/3), (0, 1/2, 1/2), also tribimaximal mit θ₁₃ = 0 (ausgeschlossen).
4. **Wolfram exakt (k262b):** Für T (ℤ₃) und A (ungerade ℤ₂) aus der TM1-Klasse ist die allgemeine A-invariante reelle Form m = {{f, b, c}, {b, d, −b}, {c, −b, f}}
   (vier Parameter). Der einfache Eigenvektor von A ist (1, 0, 1)/√2 und Eigenvektor von m; in der Eigenbasis von T hat er die Betragsquadrate **{2/3, 1/6, 1/6}**.
   Uₑ†Uₑ* = Vertauschung der Zeilen 2 und 3, und Xᵀm′X − m′* = 0 als symbolischer Nullrest: Die μτ-Spiegelung gilt für jede reelle Form, sie braucht A nicht.

## Bewertung
- **Wo die Spannung sitzt:** nicht in der Gruppe und nicht in „Kopie k auf Platz k“ (beide Lesarten benutzen dieselbe Gruppe aus k260), sondern in der Wahl des Trägers
  der Neutrinos. Auf dem komplexen Triplett sind die ungeraden Elemente Ladungskonjugationen und liefern nur J = 0. Auf dem Realteil sind sie gewöhnliche Spiegelungen
  und liefern TM1; die CP-Verletzung kommt dann allein daher, dass die Massenform reell ist und die geladenen Leptonen in der komplexen ℤ₃-Basis stehen.
- **Das ist H8, auf anderem Weg.** TM1 mit θ₂₃ = 45° und δ = ±90° ist das Muster, das H8 aus der Cayley–Dickson-Involution las und k256 als K∘S₀ wiederfand.
  k262 zeigt, dass es aus der Gruppe von k260 folgt, sobald das Neutrino keine Komponente in der Ladungsrichtung hat. H131 und H8 sind damit keine konkurrierenden
  Gruppen, sondern zwei Träger derselben Gruppe.
- **Gegen die Daten:** Das Register führt H8 und TM1 (H4) als „nach JUNO disfavorisiert“. Lesart B ist also keine Rettung, sie verschiebt nur, was verfehlt wird:
  A verfehlt θ₁₂ (0,341), θ₂₃ und δ, B trifft das von H125 erwartete Vorzeichen nicht von selbst (δ = 90° oder 270° bleibt offen) und liegt bei θ₁₂ (0,318) laut Register
  ebenfalls daneben. Ein eigener Vergleich mit aktuellen Daten ist hier nicht gerechnet.
- **Was offen bleibt (diskret):** welche ungerade ℤ₂ (TM1-Spalte oder θ₁₃ = 0, je 12 von 24 Paaren; dieselbe Zweiteilung wie in k280) und das Vorzeichen von sin δ.
  Beides legt die Gruppe nicht fest.
- **Gesetzt bleibt:** dass die Plätze Generationen sind, ℤ₃ für geladene Leptonen, eine ℤ₂ für Neutrinos, Majorana, und jetzt zusätzlich der Träger (z oder s).
  Die Lesart B ist eine Setzung wie A; die Rechnung zeigt nur, welche Setzung welches Muster gibt. OP3 und OP4 bleiben offen, kein Guard ist berührt.
  Vorzeichen der Massenterme und Feldgleichung sind nicht berührt.

## Mögliche nächste Frage
Ob die Algebra den Träger festlegt: Ein Majorana-Neutrino ist ungeladen, das spricht für s; zu prüfen wäre, ob die Massenform K aus H128 oder die Feldgleichung
s und v für das neutrale Feld trennt. Das wäre ein Test mit Vorab-Notiz.

## Dateien
`k262_setzungen.py` (`k262_out.txt`), `k262b_exakt.wl` (`k262b_out.txt`). Aufruf aus diesem Ordner, benutzt `../kollaps_h128/k283_test_h128.py`.
