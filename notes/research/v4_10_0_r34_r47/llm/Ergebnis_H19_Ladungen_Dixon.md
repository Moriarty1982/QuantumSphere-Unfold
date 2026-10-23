# Ergebnis H19: Ladungen einer Generation aus der Dixon-Ablage

Vorab-Notiz: `Vorab_Notiz_H19_Ladungen_Dixon.md`, Commit 1e60410 (2026-10-23 18:02 MESZ), vor der Rechnung.
Skript: `k75_test_h19.py`, Ausgabe `k75_out.txt`. Kriterium unverändert. Ein Indexfehler im Skript (transponierte
Koeffizientenmatrix beim Aufbau von Stab(e₇)) wurde vor der Auswertung behoben; er hatte zu einem Abbruch geführt, nicht zu
einem Ergebnis.

## Ergebnisse (M)

Kontrollen: Clifford-Relationen der L_a und Fermion-Relationen der α_a exakt; Derivationen von 𝕆 Dimension 14 (G₂), davon
mit D(e₇) = 0 Dimension 8 (SU(3)); die Exponentiale sind Automorphismen (Abweichung 2·10⁻¹⁴).

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H19a Farbe vertauscht mit Q | **bestätigt** | [D, Q] = 4·10⁻¹⁶ für die Basis von Stab(e₇), [g, Q] = 10⁻¹⁵ für 50 Gruppenelemente |
| H19b Sektoren | **bestätigt** | Q = 0 und Q = 1: je ein Singulett in span_ℂ(1, e₇); Q = 1/3 und 2/3: je ein irreduzibles Triplett in span_ℂ(e₁..e₆), zueinander konjugiert, nicht selbstkonjugiert |
| H19c wörtliche Companion-Zuordnung | **widerlegt** | Q bildet span(e₄, e₅, e₆) nicht in sich ab (Abweichung 0,167); e₇ ist kein Eigenvektor (0,5). Die Eigenzustände sind 1 ± i·e₇ (Singuletts) und Paare e_a ± i·e₇e_a (Tripletts, z. B. e₂ und e₅) |
| H19d Frames | **bestätigt** | T Q T⁻¹ = 1 − Q, J_B Q J_B⁻¹ = 1 − Q, R Q R⁻¹ = Q, jeweils exakt |
| H19e drei Plätze | **bestätigt** | Q auf jedem Platz gleich, keine Kopplung; folgt aus der Tensorstruktur |

## Einordnung

- **H19a/b** reproduzieren das bekannte Ergebnis von Furey in der Konvention des Companion. Die Farbgruppe Stab(e₇) und der
  Zahloperator passen zusammen. Aus der Struktur folgt damit das Ladungsmuster einer Generation: zwei farblose Zustände mit
  Q = 0 und 1, zwei Farb-Tripletts mit 1/3 und 2/3, jeweils zueinander konjugiert. In Fureys Lesart sind das ν, d̄, u, e⁺. Das
  ist eine **Konsistenzprüfung, keine Vorhersage über die Natur**; die Vielfachheiten waren algebraisch erzwungen.
  Voraussetzung ist die Lesart des ℂ-Faktors als quantenmechanisches i (K77.9).
- **H19c** zeigt einen echten Fehler im Companion. `thm:octonion-SU3` und `thm:three-generations` legen Farbe auf den reellen
  Spann von e₄, e₅, e₆ und ν_R auf e₇. Richtig sind komplexe Kombinationen, die e₄..e₆ mit e₁..e₃ bzw. 1 mit e₇ verbinden. Die
  Tabelle in `thm:three-generations` (Gen_i ↔ e_{i+3}) ist damit auch für die Ladung falsch, nicht nur wegen der
  Doppelbelegung von Farbe und Generation (v4.8.0-r13). Kandidat für einen Statusvermerk (Regel B oder C).
- **H19d** zum Autorhinweis „`thm:SM` nur in einem Frame entwickelt“: Der Frame-Wechsel J_B vertauscht die Ladungssektoren,
  Q ↦ 1 − Q (Q = 0 ↔ 1, 1/3 ↔ 2/3). Frame-frei sind das Ladungs*spektrum* {0, 1/3, 2/3, 1} und die Farbstruktur; *welcher*
  Zustand welche Ladung trägt, hängt vom Frame ab. Das ist nicht die Ladungskonjugation Q ↦ −Q, sondern Ladungskonjugation
  zusammen mit einer Verschiebung um eine Einheit. Die Wirkung kommt vom Zeitumkehr-Anteil T in J_B = R ∘ T; R allein lässt Q
  fest. Eine Ladungsaussage wie die U(1)-Zeile von `thm:SM` muss also ihren Frame angeben.
- Für die Bestandsaufnahme (K79) heißt das: „Ladungen“ geht von D (fehlt) nach **A unter Lesart** (Spektrum und Farbstruktur
  aus der Ablage), die wörtliche Zuordnung des Companion nach **C**.
- Nicht gezeigt: Hyperladung und Chiralität, also die schwache Seite (Tests 3 und 4 der Bestandsaufnahme).
