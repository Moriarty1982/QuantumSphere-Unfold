# Vorab-Notiz H28: Ist die Wahl in r42 erzwungen? Chiralitätsprojektor und Hyperladungs-Versatz aus Anomaliefreiheit

Festgelegt am 2026-10-23, **vor** der Rechnung. Autorfrage (2026-10-23): wieso genau diese Wahl. Bezug: H27/r42 (C_ch = ½(id + J),
J = i·L_{e₇}, Y/2 = Q − ½ + (1 − C)T₃), H25/r40 (Zentralisator der Farbe = span(L_{e₇}, R_{e₇})), H20/r35 (Q = ½ − (i/6)L_{e₇} − (i/3)R_{e₇}).

## Rahmen

Auf ℂ⊗ℍ⊗𝕆 wie in r41/r42. Ein **Chiralitätsprojektor** ist C = ½(1 + J) mit J hermitesch, J² = 1, J ≠ ±1, J auf ℂ⊗𝕆 (gehoben), J vertauscht
mit Farbe, Lorentz, R_q und Q, und Rang C = 16. Wirksame schwache SU(2) T_a′ = C T_a; Ladung Q_em = T₃ + Q + s mit einem Versatz s ∈ ℝ;
Hyperladung Y/2 := Q_em − T₃′ = Q + s + (1 − C)T₃.

## Offenlegung (Vorüberlegung vor der Notiz, nur analytisch)

Auf den Q-Sektoren gilt Q = ½ − (iL_{e₇})/6 − (iR_{e₇})/3, mit iL_{e₇}, iR_{e₇} = ±1; daraus folgt: iL_{e₇} = +1 auf {0, 2/3}, iR_{e₇} = +1 auf
{0, 1/3}. Für J = i·R_{e₇} habe ich von Hand die SU(2)²U(1)-Spur −1 und eine von null verschiedene kubische Spur erhalten (anomal).
Tr Q über ℂ⊗𝕆 ist 4, also Tr Y = 0 genau für s = −½. Die übrigen Fälle sind nicht vorab gerechnet.

## Hypothesen

- **H28a (Klassifikation):** Die Chiralitätsprojektoren im Sinn des Rahmens sind genau die vier mit J ∈ {iL_{e₇}, −iL_{e₇}, iR_{e₇}, −iR_{e₇}}; ihre
  Bilder sind die Sektorpaare {0, 2/3}, {1, 1/3}, {0, 1/3}, {1, 2/3}. (Geprüft: jede hermitesche Involution im Kommutant von Farbe und Q auf
  ℂ⊗𝕆, die auf jedem Q-Sektor ein Vorzeichen hat, mit Bild aus einem Singulett und einem Triplett.)
- **H28b (Versatz):** Für jede der vier Wahlen ist Tr Y = 0 (gravitative Anomalie) genau für s = −½.
- **H28c (Auswahl durch Anomalien):** Mit s = −½ sind alle vier Anomalie-Spuren (Tr Y, Tr Y³, SU(2)²U(1), SU(3)²U(1)) genau für J = ±iL_{e₇} null;
  für J = ±iR_{e₇} sind SU(2)²U(1) und Tr Y³ nicht null. Die Anomaliefreiheit wählt also die **Linksmultiplikation** mit e₇.
- **H28d (Frame):** Die beiden zulässigen Wahlen J = ±iL_{e₇} gehen durch T ineinander über (T J T⁻¹ = −J): Standardmodell und sein
  Spiegelbild. Bis auf den Frame ist die Wahl eindeutig.

## Entscheidungskriterium (verbindlich)

Jede Hypothese bestätigt oder widerlegt nach der wörtlichen Aussage (exakte Bruchrechnung der Spuren, Toleranz 10⁻⁹). Einordnung vorab:
- H28a–d bestätigt ⇒ Die Wahl aus r42 ist unter den Annahmen des Rahmens **bis auf den Frame erzwungen**: Farbverträglichkeit,
  Ladungserhaltung und Anomaliefreiheit lassen nur J = ±iL_{e₇} und s = −½ zu. Das beantwortet „warum diese Wahl“ teilweise, durch Konsistenz.
- Offen bleibt der Rahmen selbst: dass die schwache SU(2) rechts auf ℍ sitzt, dass Q_em = T₃ + Q + s gilt und dass J auf ℂ⊗𝕆 wirkt. Das sind
  weiterhin Annahmen.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
