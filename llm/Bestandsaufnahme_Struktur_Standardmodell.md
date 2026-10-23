# Bestandsaufnahme: Was folgt aus der Struktur, was ist eingesetzt?

Stand 2026-10-23, nach v4.9.0-r35. Lebendes Dokument: nach jeder Runde nachführen (Spalte „Stand“, Fundstelle, Datum).
Zweck (Autorabsicht): Eine vereinheitlichte Theorie muss keine neue Physik einführen, sondern erklären, **warum** das
Standardmodell diese Struktur hat. Das wird hier Merkmal für Merkmal geprüft. Eine Erklärung zählt nur, wenn die Struktur
eine Alternative **ausschließt**: Sie muss etwas verbieten.

## Einstufung

| Stufe | Bedeutung |
|---|---|
| **A** | folgt aus der Struktur (ggf. unter einer benannten Lesart) und schließt Alternativen aus |
| **B** | ist in der Struktur darstellbar, aber eingesetzt oder nur umformuliert, nicht erzwungen |
| **C** | widersprochen oder widerlegt |
| **D** | fehlt: Die Struktur sagt dazu bisher nichts |

## Tabelle

| Merkmal des Standardmodells | Stand | Begründung und Fundstelle |
|---|---|---|
| Lorentz-Gruppe, Signatur (3,1) | **A** | Biquaternion-Kern ℂ⊗ℍ, Signaturanalyse, Lesart B mit SO(3,ℂ) ≅ Lorentz (v4.8.0-r06, K1/K8). Klassische Mathematik, als Ausgangspunkt gesetzt, aber sauber. |
| Farbgruppe SU(3) | **A** (unter Lesart) | SU(3) = Stabilisator von e₇ in G₂ = Aut(𝕆) (`thm:octonion-SU3`). Zusätzlich: Der symmetrische Punkt ω = exp(2πe₇/3) des Generationen-Tripels hat genau SU(3) als Stabilisator (v4.8.0-r15). Dass das die Farbe *ist*, ist Lesart. |
| Farbe als Triplett, Singulett daneben | **A** (unter Lesart), Anti-Triplett-Satz **C** | 𝕆 = ℂ ⊕ ℂ³ unter SU(3) (`thm:octonion-SU3`) gilt im inneren Frame J = L_{e₇} mit komplexer Basis e₄, e₅, e₆ und Singulett span(1, e₇) (v4.9.0-r35, H20a). Mit dem äußeren ℂ-Faktor sind die Zustände 1 ± i·e₇ und e_a ± i·e₇e_a (r34, H19b); die Übersetzung ist P_± = ½(1 ∓ iJ), mit P₋ deckt sich die Companion-Zuordnung (ν_R auf e₇) mit Furey (H20c). Die Widerlegung H19c war ein Frame-Unterschied. Falsch bleibt der Satz „Anti-Triplett (e₁, e₂, e₃)“ (H20b, Frame-Vermischung). |
| Genau drei Generationen | **A** (unter Lesart), zu prüfen | Triality-Form Re((xy)z) auf 𝕆³ mit S₃-Symmetrie, Träger Hopf-Faserung (v4.8.0-r14/r15), Ablage (Im ℍ)⊗𝕆 (v4.9.0-r33). Mathematischer Hintergrund: Spin(8) hat genau drei 8-dimensionale irreduzible Darstellungen, Out(Spin(8)) = S₃. **Das wäre ein echtes Verbot einer vierten Generation**, aber der Zusammenhang zwischen Spin(8)-Triality und der Triality-Form des Companion ist nicht ausgeschrieben. |
| Trennung von Farbe und Generation | **B** | Im Companion liegen beide auf demselben Triplett e₄, e₅, e₆ (`thm:three-generations` gegen `thm:octonion-SU3`, festgestellt in v4.8.0-r13). Trennung vorgeschlagen (v4.8.0-r14) und in der Dixon-Ablage darstellbar (v4.9.0-r33). Eine Lesart, nicht erzwungen. |
| Generationen-Symmetrie | **A** (strukturell) | Gemeinsame Symmetrie von Ablage und Triality-Form: A₄ = Konjugation mit der binären Tetraedergruppe 2T; auf den links-invarianten Etiketten bleibt ℤ₃ (v4.9.0-r33, Lean `Dixon.lean`, `Lesarten.lean`). |
| Schwache SU(2) und U(1) | **B**, in Teilen **C** | `prop:biquaternion-u1su2` und `thm:SM`: SU(2) aus den Einheitsquaternionen, U(1) aus dem komplexen Skalar. Probleme: (1) ℂ⊗ℍ enthält ebenso SL(2,ℂ), also die Lorentz-Gruppe; „erzeugt genau U(1)×SU(2)“ ist zu stark, die kompakte Untergruppe ist U(2) = (U(1)×SU(2))/ℤ₂. (2) Die Tabelle in `thm:SM` nennt das U(1) „Elektromagnetismus“; im Standardmodell ist das ungebrochene U(1) die Hyperladung, die elektromagnetische U(1) entsteht erst nach der Brechung als Kombination. (3) **Der ℍ-Faktor ist dreifach belegt:** als Lorentz-Spinor (`thm:three-generations`), als schwache SU(2) (`thm:SM`) und als Generationen-Index (v4.9.0-r33). Kein `\qsstatus`-Vermerk. (4) Die Ladungszuordnung hängt vom Frame ab (J_B: Q ↦ 1 − Q, v4.9.0-r34); die U(1)-Zeile muss ihren Frame nennen. (5) Der Skalar it allein ist nur eine globale Phase; die Ladung ist Q = ½ − (i/6)L_{e₇} − (i/3)R_{e₇}, braucht also innere und äußere Einheit (v4.9.0-r35). |
| Globale Form der Eichgruppe | **D** | Das Standardmodell hat (SU(3)×SU(2)×U(1))/ℤ₆; dazu sagt der Companion nichts. |
| Ladungen einer Generation | **A** (unter Lesart), Konsistenz | Zahloperator auf ℂ⊗𝕆 nach Furey ist mit der Farbe Stab(e₇) des Companion verträglich; Ladungen 0, 1/3, 2/3, 1 als Singulett, Triplett, konjugiertes Triplett, Singulett (v4.9.0-r34, H19a/b). Lesart: ℂ-Faktor = quantenmechanisches i. Keine Vorhersage, die Vielfachheiten sind algebraisch erzwungen. **Frame-abhängig:** J_B bildet Q auf 1 − Q ab (H19d); frame-frei sind nur Spektrum und Farbstruktur. |
| Hyperladungen | **D** | Nirgends hergeleitet (kein Vorkommen von „hypercharge“). Test 4. |
| Chiralität (SU(2) wirkt nur links) | **D** | Kein Vorkommen. Ohne Chiralität ist keine Aussage über die schwache Wechselwirkung möglich. |
| Quarks gegen Leptonen | **B** | Singulett und Triplett unter SU(3) wären die natürliche Trennung, sind im Companion aber nicht so zugeordnet. Quark-Werte aus der Struktur nicht ableitbar (K25). |
| Koide-Relation K = 2/3 | **B** | Die Koide-Form ist exakt Skalar plus symmetrische Triole; K = 2/3 ⇔ \|c\| = t (v4.8.0-r10). Eine Umformulierung, keine Herleitung. Gleich-Norm-Bedingung auch in der v4.9-Linie unabhängig gefunden (K26). |
| Massenhierarchie | **C** für natürliche Potentiale | Natürliche Invarianten auf dem Tripel-Raum geben höchstens zwei verschiedene Massen (H11, H16, H17, H18; Sattel-Sätze v4.9.0-r26.1, r32.1). Lesart: Die Struktur **erklärt**, dass Massen eine Brechung der Generationen-Symmetrie brauchen (wie die Yukawa-Kopplungen im Standardmodell), liefert die Brechung aber nicht. |
| Existenz von Mischung | **B** | Reine Generationen-Symmetrie mit Triole gibt θ₁₃ = 0 (K28.4); Mischung braucht weitere Brechung. |
| Mischungswinkel (PMNS, CKM) | **C** | `prop:pmns-z3` widerlegt (v4.8.0-r12), TM1 und H8 mit JUNO disfavorisiert (v4.8.0-r13), CKM-Zeile hängt an einer Koinzidenz (v4.8.0-r09). Offen: H9 (sin²θ₁₂ = 0,30862) für die nächste JUNO-Messung, nachträglich gefunden. |
| Neutrino-Massenordnung | **B** | H2 verträglich, normale Ordnung, Σm_ν = 0,059 eV (v4.8.0-r12); trennt schwach. |
| Feinstrukturkonstante, Weinberg-Winkel | **B**, offen | k-Tabelle (`thm:k-values`: α „first Dixon plane“); cot θ_W (on-shell) ≈ γ_L, Vorhersage H15 für m_W, noch nicht entschieden (v4.9.0-r07). γ_L selbst ist eingesetzt (OP1). |
| β_sym, γ_L | **B** | Aus γ_BI und γ_string eingesetzt (v4.8.0-r03); OP1 offen (Issue #10). |
| Higgs-Mechanismus | **B** | Nur formal als Portgewichtung (v4.9.0-r06). |
| Gravitation, Λ | **B**/offen | Feldgleichungsschicht korrigiert (v4.8.0-r05), Wirkung nicht definiert; Cartan-Jets endlich, keine regionale Existenz (Issue #16). |

## Was daraus folgt

1. **Stark (A)** ist bisher die *Gruppen*-Seite: Lorentz, SU(3) als Stabilisator, drei Plätze mit S₃ bzw. A₄. Das ist
   Mathematik, deren physikalische Zuordnung eine Lesart bleibt. Genau so beginnen aber auch die Divisionsalgebra-Programme
   in der Literatur.
2. **Es fehlen (D)** gerade die Merkmale, an denen sich ein solcher Ansatz am schärfsten prüfen lässt: Hyperladungen und
   Chiralität. Hier verbietet die Struktur noch nichts. Die Ladungen einer Generation folgen seit v4.9.0-r34 unter Lesart
   (Konsistenz mit Furey); ihre Zuordnung zu Zuständen hängt vom Frame ab.
3. **Der ℍ-Faktor ist überbelegt.** Lorentz, schwache SU(2) und Generationen können nicht alle dieselbe Wirkung auf
   demselben ℍ sein. Die Links-/Rechts-Trennung aus v4.9.0-r33 (Lorentz von links, Generationen rechts) ist ein Ansatz.
   Dann bleibt zu klären, woher die schwache SU(2) kommt.
4. `thm:SM` und `prop:biquaternion-u1su2` tragen keinen `\qsstatus`-Vermerk, obwohl Teile davon zu stark formuliert sind.
   Kandidat für Regel C der Überarbeitung (Autorentscheidung).

## Aussichtsreiche Abzähl-Tests (Vorschlag, jeweils mit Vorab-Notiz)

| Rang | Test | warum aussichtsreich | was er riskiert |
|---|---|---|---|
| 1 (erledigt, r34) | **Ladungen einer Generation aus der Dixon-Ablage**: Liefert der Zahloperator auf ℂ⊗𝕆 (bzw. in der Ablage) die Ladungen 0, 1/3, 2/3, 1 und ihre Zuordnung zu Leptonen und Quarks? | in der Literatur für ℂ⊗𝕆 gezeigt; wäre die erste Ladungsaussage des Companion | Gelingt es mit der Companion-Zuordnung (Farbe auf e₄..e₆, Singulett e₇) nicht, ist die Zuordnung falsch |
| 2 | **Genau drei Generationen**: Ist die Triality-Form Re((xy)z) die Spin(8)-Triality, und schließt sie eine vierte Generation aus? | ein echtes Verbot, rein mathematisch prüfbar | Lässt die Struktur auch vier Plätze zu, erklärt sie die Drei nicht |
| 3 | **Woher die schwache SU(2)?** Gibt es neben Lorentz (links) und Generationen (rechts) eine dritte, verträgliche SU(2) in der Ablage, und wirkt sie chiral? | würde den dreifach belegten ℍ-Faktor auflösen | Gibt es keine, ist `thm:SM` in der jetzigen Form nicht haltbar |
| 4 | **Hyperladung statt Elektromagnetismus**: Lässt sich das U(1) aus `thm:SM` als Hyperladung lesen, sodass Q = T₃ + Y/2 herauskommt? | Abzählung, keine Präzisionszahl | Passt keine Zuordnung, ist die U(1)-Zeile falsch |

Rang 1 und 2 lassen sich ohne neue Annahmen über Dynamik prüfen. Beide sind auch in Lean formalisierbar.
