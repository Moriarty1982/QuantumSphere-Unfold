# Vorab-Notiz H165: Woher kann β_sym = 0,5493 kommen, und gibt es in der Zwei-Auslesen-Lesart eine Bedingung, die den Wert erzwingt?

**Stand:** 2026-11-26, vor der Rechnung festgelegt und vor dem ersten Skriptlauf committet. **Überwiegend nicht blind** (siehe „Vorab offengelegt“).
Auftrag des Autors vom 26.11.2026, 10:22 UTC: „ja und dann schauen wir mal woher die 0.5493 kommen kann und wieso das folgen müsste“.
Skripte **k356** (Python: mpmath für die Summen, sympy für die Identitäten, **Qiskit** `quantum_info` für die Spin-j-Zustände und ihre Überlappe) und
**k356b** (Wolfram Language, hohe Genauigkeit und exakt, unabhängige Gegenprobe). Werkzeugwahl: Wolfram für die transzendente Gleichung und die
symbolischen Summen; Qiskit, weil die Überlappe der symmetrischen Mehr-Qubit-Zustände explizit definierte Zustände sind. Kein HDL/MMA-Vergleich
(kein RUN_TAPE-Ablauf, keine endliche Suche mit Guard). Kein Guard wird berührt.

## Vorwissen geprüft
Die vollständige Sichtung steht in `notes/research/op1_herkunft_beta_sym_h165/Sichtung_Herleitungsversuche.md` (37 Versuche, keiner leitet β_sym her).
Für diesen Test maßgeblich:
- **H47, v4.9.0-r63, r68 (Zählverhältnis):** γ_L = γ_DL/γ_ABCK. γ_T = ln 2/(π√3) (nur j = ½, ein Bit je Durchstoßpunkt), γ_M löst
  Σ_j 2·exp(−2πγ_M√(j(j+1))) = 1 (alle Spins, Gewicht 2 für m = ±j). Nicht blind; die Zuordnung Regel↔Frame ist nicht hergeleitet; SU(2)-Zählung gibt 0,604.
- **k245 (Hopf-Lücke):** mit j + ½ statt √(j(j+1)) in beiden Frames wird γ_L = 2, β = 1/√3 exakt.
- **`op1_readout_frequency`:** Nebenwert 2^(1−γ_L) = 0,549161 (2,5·10⁻⁴ neben 0,549406), dort nicht verwendet.
- **`op1_moran_geometry`, r29, r53:** γ_L als Moran-Dimension, nachträglich.
- **H161, H164 (r66):** zwei Auslesen; β = |⟨K₁|S⟩|; Tetraeder am Hopf-Wert; alles Identitäten in β.
- **r64.4:** die Feldgleichung auf dem Turm legt β_sym nicht fest. **H155/H156:** nur K = (1+β⁴)/3 wird benutzt; gleiche Massenterme brauchen J als Postulat.
- **r64.6(b):** zwei Zahlenwerte im Bestand (0,5493482 gerundet, 0,549406 exakt).
- Suche nach „kohärent“, „coherent state“, „Vektormodell“, „Kegel“, „magic angle“ im Zusammenhang mit β_sym (26.11.): keine Fundstelle zu einer Schließungssumme
  über Überlappe.

## Suchrichtung (Rückwärtssuche)
Ziel: γ_L = 1,864700 (β = 0,549406). Notwendig nach der Sichtung: Gewicht 2 je Spin, Spektrum √(j(j+1)), Einheit „ein Bit bei j = ½“. Jede geschlossene Formel,
die nicht diese Summe ist, kann den Wert höchstens zufällig treffen, weil die Wurzel einer transzendenten Gleichung gesucht ist. Rückwärts gelesen fragt H165
deshalb nicht nach einer neuen Formel, sondern: Liefert die Zwei-Auslesen-Lesart (H161, H164) von sich aus eine Schließungsbedingung der Form
„Summe über alle Spins = 1“, und welchen Wert erzwingt sie?

## Übersetzung (gesetzt)
- c_k = √(k(k+2)/3) mit k = 2j ist die Fläche des Spins j in Einheiten der Fläche von j = ½. Z(g) = Σ_{k≥1} 2^(1 − g·c_k). p_k = 2^(1 − γ_L·c_k) ist das
  Gewicht des Spins k/2 in der M-Zählung.
- Spin j als 2j symmetrisierte Qubits; kohärenter Zustand |j; n⟩ = |n⟩^{⊗2j}. Für das Paar (K₁, S) aus H164 ist |⟨j; K₁|j; S⟩| = β^{2j}.
- Lesart C aus r66 (Hopf-Sphäre als Himmelskugel) bleibt gesetzt.

## Hypothese H165
In der Zwei-Auslesen-Lesart gibt es eine Schließungsbedingung über alle Spins, die β_sym ohne die Literaturwerte γ_BI, γ_string festlegt, und sie trifft
β = 0,549406 als Identität.

## Entscheidungskriterien
- **K-a (Ziel, nicht blind):** Z(g) = 1 hat genau eine positive Wurzel; sie ist γ_M/γ_T auf mindestens 25 Stellen, und β = √((g−1)/(g+1)) = 0,5494056…
  Mit c_k → (k+1)/2·(a_½-Einheit j + ½, also c_k = (k+1)/2) ist die Wurzel exakt 2 (symbolisch). Beides: bestätigt.
- **K-b (Schließung mit Überlappen):** Σ_{j≥½} 2·|⟨j; K₁|j; S⟩|^p = 1 wird für p = 1, 2, 4 gelöst, dazu mit den Exponenten c_k und √(k(k+2)) an Stelle von 2j
  (für p = 2). H165 verlangt: eine dieser fünf Bedingungen trifft β = 0,549406 auf relativ 10⁻⁶. Sonst **widerlegt**.
  Zusatz (Identität, nicht blind): Für p = 2 ist die Lösung β = 1/√3 exakt; geprüft symbolisch und mit Qiskit für j = ½ … 3.
- **K-c (Zahlenkandidaten, strenges Kriterium):** Ein Kandidat gilt nur als Identität, wenn er bei 30 Stellen auf relativ 10⁻⁸ stimmt. Liste, vor dem Lauf fest:
  1. 2^(1−γ_L) = β (Anteil der j = ½-Durchstoßpunkte an der M-Zählung = Überlapp der zwei Auslesen);
  2. die selbstkonsistente Wurzel von 2^(1−g) = √((g−1)/(g+1)) gegen γ_L;
  3. 1/⟨c⟩ = artanh(1/√3) mit ⟨c⟩ = Σ p_k c_k;
  4. ⟨k⟩ = Σ p_k·k gegen γ_L;
  5. ⟨√(j/(j+1))⟩ (mittlerer Kosinus des Kegels im Vektormodell) gegen β und gegen 1/√3;
  6. ⟨1/c⟩ gegen β, 1/γ_L, β²;
  7. p₁/(1−p₁) gegen γ_L − 1 und gegen 1/β² − 2;
  8. −Z′(γ_L)/ln 2 = ⟨c⟩ gegen γ_L − ⅓ und gegen 3/2.
  H165 verlangt hier mindestens eine Identität. Treffer innerhalb 10⁻³ ohne Identität werden als Zufallstreffer gezählt und gegen die Zahl der Vergleiche gestellt.
- **K-d (Kegel, Identität, nicht blind):** cos des Kegelwinkels für j = m = ½ ist j/√(j(j+1)) = 1/√3, und der doppelte Kegelwinkel ist der Tetraederwinkel
  arccos(−⅓). Bestätigt, wenn exakt.
- **Gesamturteil:** **bestätigt**, wenn K-b oder K-c eine Identität für 0,549406 liefert. **Widerlegt**, wenn keine. K-a und K-d sind Feststellungen und
  gehen nicht ins Urteil ein.

## Vorhersage
K-a bestätigt. K-b widerlegt: p = 2 gibt 1/√3 (Hopf-Wert), p = 1 gibt ⅓, p = 4 gibt 3^(−1/4) = 0,7598; mit c_k etwa 0,524, mit √(k(k+2)) etwa 0,689.
K-c: keine Identität; Nr. 1 verfehlt um 4,5·10⁻⁴, Nr. 3 liegt nach grober Kopfrechnung bei etwa 5·10⁻⁴ (unsicher), Nr. 4 bei etwa 1 %, Nr. 5 liegt über 1/√3.
Nr. 2, 6, 7, 8 sind nicht vorgerechnet. K-d bestätigt. **Gesamt: widerlegt.** Erwarteter Ertrag ist die Einordnung: Die Überlapp-Schließung erzwingt den
Hopf-Wert, und der gemessene Wert entsteht erst mit dem Casimir-Spektrum und der Ein-Bit-Einheit.

## Vorab offengelegt
- Vor dieser Notiz ist am 26.11. gegen 10:27 UTC **eine** Wolfram-Auswertung gelaufen, die das Ziel bestimmt hat (γ_M, γ_T, β = 0,54940564097, γ_L = 1,86469976,
  ε = 0,61752958). K-a ist damit nicht blind. Die Auswertung wird in k356b wiederholt und mit Ausgabe abgelegt.
- Die Lösungen zu K-b (⅓, 1/√3, 3^(−1/4), etwa 0,524 und 0,689), die Abweichung von Nr. 1 und die groben Werte zu Nr. 3, 4, 5 habe ich im Kopf überschlagen,
  bevor diese Notiz stand. K-b ist deshalb nicht blind. Blind sind nur Nr. 2, 6, 7, 8 aus K-c.
- Die Aussage „Σ 2β^{4j} = 1 genau bei β² = ⅓“ ist heute beim Entwerfen entstanden, nicht aus dem Bestand.

## Was der Test nicht leistet
Er prüft nur Schließungen in der Lesart C mit kohärenten Zuständen. Er leitet weder die Zählregel (Gewicht 2, alle Spins) noch die Ein-Bit-Einheit von T her.
Kein Datenvergleich. OP1 bleibt in jedem Fall offen, solange die Regel nicht hergeleitet ist. Nächste freie Nummern danach: H166, k357.
