# Rückwärtssuche: was ein Auswahlprinzip für die geladenen Leptonen festlegen muss

13. November 2026, spät. Autorenauftrag: „weiter“ (Übergabe, zur Wahl: Auswahlprinzip für Koide). Rückwärtssuche, nicht
blind, kein Datenvergleich außer den bekannten Polmassen. Keine H-Nummer. Skript `op3_selection_principle_2026_11_13.py`.

## Vorwissen geprüft
`op3_koide_potential_2026_11_13.md` (Koide = qubitartige Treue; Potential nur abgestimmt), Gram-Notiz (Rand des Bogens:
Rang 2, leichtester Zustand masselos), η-Notiz (Oktant, Phase π/4), v4.8.0-r11 (H1: δ = 2/9 nur bei Polmassen).

## Ergebnis
1. **Die Elektronmasse ist der Abstand vom Qubit-Rand.** Bei ρ² = 1/2 ist der kleinste Eigenwert in erster Ordnung
   s_min ≈ π/12 − θ. Für die geladenen Leptonen: π/12 − θ_e = 0,03957, √m_e/⟨√m⟩ = 0,04035 (Verhältnis 1,02, der Rest ist
   zweite Ordnung). Am Rand (θ = π/12) wäre das Elektron masselos; m_e/m_τ = 2,9·10⁻⁴ entspricht dem Abstand 0,040.
2. **Damit sind genau zwei Zahlen festzulegen:**
   - die Treue 1/2 (Koide, ρ² = 1/2), die den Qubit-Oktanten auszeichnet;
   - der Abstand vom Oktanten, gleichwertig θ_e = 0,2222 oder die Bargmann-Differenz π/4 − 3θ_e = 0,1187.
   Die zweite Zahl ist die Elektronmasse in Einheiten des Mittelwerts. Für sie gibt es keinen nativen Kandidaten; 3θ_e ≈ 2/3
   ist Brannens Wert, dessen Allgemeingültigkeit H1 widerlegt hat.
3. **Bild.** Die geladenen Leptonen sind ein Qubit-Oktant (Treue 1/2), um 0,04 aus der Qubit-Ebene herausgehoben; die
   Neutrinos liegen nach H99 um denselben Fluss π/4 jenseits des Randes. Das ordnet die Zahlen, erklärt sie aber nicht.

## Bewertung
Ein Auswahlprinzip muss zwei unabhängige Zahlen liefern: die Treue 1/2 und den Abstand vom Qubit-Rand (die
Elektronmasse). Bisher ist keine der beiden im Companion hergeleitet. OP3/OP4 offen; H100 unberührt.

## Herleitungsversuch (13.11., spät, Autor: „dann versuchen wir das mal herzuleiten“)

Vorwissen zusätzlich: r55 (A_4 als Platzsymmetrie; Dirac-Auslesung ℤ₃, Majorana-Auslesung ℤ₂), r33.2 (Rechtswirkung von
1 + i + j + k vertauscht die Labels zyklisch), r47 (Generationsmaske aus der trialitätskovarianten Chiralität),
Prüfung Punkt 3 (Hurwitz-Einheit, 2T über A_4). Zurückgestellte Ideen: kein Auslöser. Skript, Abschnitt „Teil A“.

**Teil A: Die Treue 1/2 folgt aus der A_4-Geometrie (bedingt hergeleitet).**
- Für einen Qubit-Zustand unter dem Winkel β zur Achse einer 120°-Drehung hat seine Bahn (drei Zustände) die Gram-Matrix
  vom Rang 2 und **K = (1 + cos² β)/2** (numerisch 10⁻¹⁶). K = 2/3 gilt genau bei cos² β = 1/3, dem magischen Winkel.
- In den endlichen Untergruppen von SU(2) liegen die Bahnen von Eigenzuständen zweizähliger Achsen unter dreizähligen
  Drehungen bei:

  | Gruppe | K-Werte |
  |---|---|
  | Tetraeder A_4 | **nur 2/3** |
  | Oktaeder S_4, Koordinatenachsen | 2/3 |
  | Oktaeder S_4, Kantenachsen | 1/2; 5/6 |
  | Ikosaeder A_5 | 0,564; 2/3 (über die enthaltene A_4); 0,936 |

  **In A_4 ist K = 2/3 der einzige mögliche Wert.** Jede zweizählige Achse steht dort unter dem magischen Winkel zu jeder
  dreizähligen.
- Damit ist Koide bedingt hergeleitet: Wenn (i) die Plätze Qubit-Zustände tragen, (ii) der Bezug ein Eigenzustand eines
  Elements der Klein-Gruppe von A_4 ist und (iii) die Plätze dessen Bahn unter dem ℤ₃ von A_4 sind, dann folgt ρ² = 1/2
  zwingend, ohne freie Zahl. A_4 ist im Companion die Platzsymmetrie (r55); die zyklische Rechtswirkung aus r33.2 ist die
  zugehörige Hurwitz-Einheit. Auffällig: Der Bezug kommt aus der ℤ₂-, der Zyklus aus der ℤ₃-Untergruppe, also genau aus
  den beiden Auslesungen von r55 (Majorana ℤ₂, Dirac ℤ₃).
- Offen bleibt Voraussetzung (i): ein farb- und ladungsneutrales Qubit als Träger (Trägersuche vom 13.11. negativ).

**Teil B: Der Abstand vom Oktanten ist ein Bruch der A_4-Symmetrie.**
- Die exakte A_4-Konstruktion liefert Rang 2, also θ = π/12 und ein masseloses Elektron. Ein Elektron mit Masse verlangt,
  dass die Plätze aus der Qubit-Ebene heraustreten; das bricht die exakte A_4- bzw. Qubit-Struktur.
- Die Größe des Bruchs ist die Elektronmasse in Einheiten des Mittels: Gewicht der dritten Fourier-Richtung
  s_min/3 = 0,0134, Abstand π/12 − θ_e = 0,0396. Ein Ansatz mit einer gemeinsamen dritten Komponente aller Plätze kann
  Koide nicht erhalten (keine Lösung mit positivem Gewicht); die Anhebung muss selbst zyklisch sein.
- Ein nativer Kandidat für den Bruch ist die Generationsmaske aus r47 (trialitätskovariante Chiralität), die A_4 bereits
  bricht. Geprüft ist das nicht; ein Vergleich mit dem bekannten Wert wäre nicht blind und bräuchte eine Vorab-Notiz.

**Bewertung.** Die erste der beiden Zahlen (Treue 1/2) ist bedingt hergeleitet: Sie ist der einzige Wert, den die
A_4-Geometrie auf einem Qubit zulässt. Die zweite (Abstand vom Oktanten, Elektronmasse) ist als A_4-Bruch eingeordnet,
aber nicht hergeleitet. Offen sind der Qubit-Träger und die Größe des Bruchs. OP3/OP4 offen; H100 unberührt.

## Nachtrag: andere Anhebung gesucht (13.11., spät, Autor: „Andere Anhebung suchen“)

Rückwärtssuche nach H101. Skript, Abschnitt „Andere Anhebung“. Nicht blind, kein Test.

1. **Nur ein Fluss erhält Koide.** Eine allgemeine hermitesche Störung des Oktanten (Diagonale fest) ändert K schon in
   erster Ordnung (typisch dK/dε ≈ 0,25). Eine reine Phasendrehung der Überlappungen ändert K in keiner Ordnung (10⁻¹²),
   weil K nur von den Beträgen abhängt; eichinvariant bleibt davon nur der Fluss durch das Platzdreieck. **Jede Anhebung,
   die Koide exakt erhält, ist eine Flussänderung.**
2. **Der nötige Fluss.** Vom Oktanten (Fluss π/4, Elektron masselos) zu den geladenen Leptonen ist ΔΦ = 3(π/12 − θ_e) =
   0,11872 rad. Danach ist das Spektrum (0,0404; 0,5802; 2,3794) mit K = 2/3 exakt. Der Fluss der geladenen Leptonen ist
   3θ_e = 0,666674, also Brannens 2/3 (δ = 2/9) innerhalb der Unsicherheit.
3. **Native Quellen.** ΔΦ = 0,2267 · π/6; native Phasen (ω, i, −1) geben nur ganze Vielfache von π/6, die Hyperladungs-Regel
   Vielfache von π/4. Ein Fluss von 0,1187 rad (bzw. 2/3 rad insgesamt) braucht eine stetige Größe, etwa eine
   U(1)-Verbindung mit nicht quantisiertem Fluss.

**Bewertung.** Die Suche schließt einen Kreis: Eine Koide-erhaltende Anhebung des Elektrons ist genau eine Änderung der
Brannen-Phase, und deren Herleitung ist das historische OP3 (θ_K bzw. δ = 2/9), dessen Allgemeingültigkeit H1 widerlegt
hat. Eine andere, neue Anhebung gibt es nicht: Alles außer einem Fluss bricht Koide. OP3 bleibt offen; die Frage ist jetzt
scharf gestellt als „Woher kommt ein Fluss von 2/3 rad durch das Platzdreieck der geladenen Leptonen?“
