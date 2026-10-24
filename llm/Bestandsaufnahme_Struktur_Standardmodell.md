# Bestandsaufnahme: Was folgt aus der Struktur, was ist eingesetzt?

Stand 2026-10-24, nach v4.9.0-r48. Lebendes Dokument: nach jeder Runde nachführen (Spalte „Stand“, Fundstelle, Datum).
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
| Genau drei Generationen | **A** (unter Lesart), zu prüfen | Triality-Form Re((xy)z) auf 𝕆³ mit S₃-Symmetrie, Träger Hopf-Faserung (v4.8.0-r14/r15), Ablage (Im ℍ)⊗𝕆 (v4.9.0-r33). Mathematischer Hintergrund: Spin(8) hat genau drei 8-dimensionale irreduzible Darstellungen, Out(Spin(8)) = S₃. **Seit v4.9.0-r37 (H22):** t = Re((xy)z) ist die Spin(8)-Triality-Form; die drei Plätze tragen die drei inäquivalenten 8-dim. Darstellungen, ihre Verschiebung ist die äußere Triality, deren Fixgruppe G₂ ⊃ SU(3)_c ist. **Ein Verbot einer vierten Generation folgt daraus nicht**: Die Klassifikation schließt nur einen vierten *neuen* Platz aus, und auf vier Plätzen gibt es eine zyklisch invariante Form. **v4.9.0-r45:** Mit Chiralität können die Generationen nur äquivalente Kopien sein, nicht die inäquivalenten Triality-Darstellungen. |
| Trennung von Farbe und Generation | **B** | Im Companion liegen beide auf demselben Triplett e₄, e₅, e₆ (`thm:three-generations` gegen `thm:octonion-SU3`, festgestellt in v4.8.0-r13). Trennung vorgeschlagen (v4.8.0-r14) und in der Dixon-Ablage darstellbar (v4.9.0-r33). **Seit v4.9.0-r37 (H22) trennbar: Generation = Bahn der Triality auf den Plätzen, Farbe = in ihrer Fixgruppe. Herkunft (v4.9.0-r36, H21):** Die zyklische Symmetrie der Triole e₄ → e₅ → e₆ ist der einzige solche Automorphismus und liegt in SU(3)_c (Weyl-Element); die 120°-Triole der Kerne ist ein Farbzustand. Farbe und Generation sind im Companion also *dasselbe Objekt*. Innerhalb von 𝕆 mit festem e₇ gibt es keine Generationen-ℤ₃, die nicht Farbe wäre: Die Trennung ist **nötig**, ihr Träger (Triality-Plätze oder Im ℍ) bleibt eine Lesart. |
| Generationen-Symmetrie | **A** (strukturell) | Gemeinsame Symmetrie von Ablage und Triality-Form: A₄ = Konjugation mit der binären Tetraedergruppe 2T; auf den links-invarianten Etiketten bleibt ℤ₃ (v4.9.0-r33, Lean `Dixon.lean`, `Lesarten.lean`). |
| Schwache SU(2) und U(1) | **B**, in Teilen **C** | `prop:biquaternion-u1su2` und Seit v4.9.0-r41 in Aufteilung D aufgelöst: Lorentz links, schwache SU(2) rechts, Generationen auf der Triality. `thm:SM`: SU(2) aus den Einheitsquaternionen, U(1) aus dem komplexen Skalar. Probleme: (1) ℂ⊗ℍ enthält ebenso SL(2,ℂ), also die Lorentz-Gruppe; „erzeugt genau U(1)×SU(2)“ ist zu stark, die kompakte Untergruppe ist U(2) = (U(1)×SU(2))/ℤ₂. (2) Die Tabelle in `thm:SM` nennt das U(1) „Elektromagnetismus“; im Standardmodell ist das ungebrochene U(1) die Hyperladung, die elektromagnetische U(1) entsteht erst nach der Brechung als Kombination. (3) **Der ℍ-Faktor ist dreifach belegt:** als Lorentz-Spinor (`thm:three-generations`), als schwache SU(2) (`thm:SM`) und als Generationen-Index (v4.9.0-r33). Kein `\qsstatus`-Vermerk. (4) Die Ladungszuordnung hängt vom Frame ab (J_B: Q ↦ 1 − Q, v4.9.0-r34); die U(1)-Zeile muss ihren Frame nennen. (5) Der Skalar it allein ist nur eine globale Phase; die Ladung ist Q = ½ − (i/6)L_{e₇} − (i/3)R_{e₇}, braucht also innere und äußere Einheit (v4.9.0-r35). |
| Globale Form der Eichgruppe | **D** | Das Standardmodell hat (SU(3)×SU(2)×U(1))/ℤ₆; dazu sagt der Companion nichts. |
| Ladungen einer Generation | **A** (unter Lesart), Konsistenz | Zahloperator auf ℂ⊗𝕆 nach Furey ist mit der Farbe Stab(e₇) des Companion verträglich; Ladungen 0, 1/3, 2/3, 1 als Singulett, Triplett, konjugiertes Triplett, Singulett (v4.9.0-r34, H19a/b). Lesart: ℂ-Faktor = quantenmechanisches i. Keine Vorhersage, die Vielfachheiten sind algebraisch erzwungen. **Frame-abhängig:** J_B bildet Q auf 1 − Q ab (H19d); frame-frei sind nur Spektrum und Farbstruktur. v4.9.0-r48: Sektoren, Farbdimensionen 1, 3, 3, 1, Ladungen und T als Ladungskonjugation in Lean aus der Oktonionen-Multiplikation hergeleitet (`formal/QSFormal/Sektoren.lean`). |
| Hyperladungen | **B** (unter Wahl) | v4.9.0-r41 (H26): In der Aufteilung D (schwache SU(2) rechts auf ℍ) gibt Y/2 := Q − ½ mit Q_em = T₃ + Y/2 genau die Hyperladungen und Ladungen der linkshändigen Dubletts und ihrer Konjugierten, mit richtiger Farbe. Die Wahl Y/2 = Q − ½ ist durch das Muster motiviert, nicht erzwungen. Frame T = Ladungskonjugation. v4.9.0-r42: mit dem Chiralitäts-Kompensator Y/2 = Q − ½ + (1 − C_ch)T₃, volle Hyperladungen einer Generation (Konstruktion). |
| Chiralität (SU(2) wirkt nur links) | **B** (Konstruktion unter Wahl) | Kein Vorkommen. Spur aus v4.9.0-r38: Liest man Materie und Tachyon als die beiden Spinor-Plätze der Triality, ist M ↔ T ein Chiralitätswechsel (nicht gerechnet). **v4.9.0-r40 (H25):** In der Triality-Algebra vertauscht kein 𝔰𝔲(2) mit der Farbe (Zentralisator = span(L_{e₇}, R_{e₇}), die Ladungs-Erzeuger); eine farbverträgliche SU(2) gibt es nur im ℍ-Faktor, zweimal (links, rechts). Lesart „schwache SU(2) = eine Seite der zweiseitigen Notation“, nicht gezeigt. **v4.9.0-r41:** In D ist jeder Zustand ein Dublett; die rechtshändigen Singuletts fehlen. **v4.9.0-r42 (H27):** Ein Kompensator C_ch = ½(id + J), J = i·L_{e₇}, der MM-Matrix lässt die schwache SU(2) nur auf seinem Bild wirken; zusammen mit Y/2 = Q − ½ + (1 − C_ch)T₃ ergibt das den vollen linkshändigen Inhalt einer Generation mit ν_R, richtige Quantenzahlen, anomaliefrei. Konstruktion unter Wahlen, Muster vorab gesehen; nicht hergeleitet. **v4.9.0-r43 (H28):** Unter den Annahmen (schwach rechts, Q_em = T₃ + Q + s) sind die Wahlen erzwungen: vier mögliche Projektoren, Tr Y = 0 ⇒ s = −½, Anomaliefreiheit ⇒ Linksmultiplikation mit e₇; übrig bleiben SM und Frame-Spiegel. Ohne Chiralität ist keine Aussage über die schwache Wechselwirkung möglich. |
| Quarks gegen Leptonen | **B** | Singulett und Triplett unter SU(3) wären die natürliche Trennung, sind im Companion aber nicht so zugeordnet. Quark-Werte aus der Struktur nicht ableitbar (K25). |
| Koide-Relation K = 2/3 | **B** | Die Koide-Form ist exakt Skalar plus symmetrische Triole; K = 2/3 ⇔ \|c\| = t (v4.8.0-r10). Eine Umformulierung, keine Herleitung. Gleich-Norm-Bedingung auch in der v4.9-Linie unabhängig gefunden (K26). |
| Massenhierarchie | **C** für natürliche Potentiale | Natürliche Invarianten auf dem Tripel-Raum geben höchstens zwei verschiedene Massen (H11, H16, H17, H18; Sattel-Sätze v4.9.0-r26.1, r32.1). Lesart: Die Struktur **erklärt**, dass Massen eine Brechung der Generationen-Symmetrie brauchen (wie die Yukawa-Kopplungen im Standardmodell), liefert die Brechung aber nicht. v4.9.0-r44: Genauer muss die Spiegelung ρ (Frame-Triole) gebrochen sein, τ darf bleiben; dann folgt genau die Brannen-Form, Koide bei \|b\| = a/√2 (Verhältnis offen). **v4.9.0-r45:** Die ρ-Brechung folgt aus der Struktur: ρ enthält die Oktonion-Konjugation, die links und rechts tauscht, und die Anomaliefreiheit hat links gewählt. Die Stärke der Brechung bleibt offen. |
| Existenz von Mischung | **B** | Reine Generationen-Symmetrie mit Triole gibt θ₁₃ = 0 (K28.4); Mischung braucht weitere Brechung. v4.9.0-r44: Sind up und down beide τ-symmetrisch, gibt es gar keine Mischung; Mischung verlangt eine für up und down verschiedene Brechung der Triality. v4.9.0-r46: Readouts aus den Verschiebungen (Hilbert-Shift) können τ nie brechen; erst Masken, die einzelne Generationen als Auslesearten unterscheiden, erzeugen Mischung (∝ Gewicht, unterdrückt durch Massenabstände). Herkunft einer solchen Maske offen. v4.9.0-r47: Unter einer Modellannahme (Abweichung der triality-kovarianten Chiralität als schwache Störung) hat die Maske eine feste Form, Quarks diag(0, −2, −1), Leptonen diag(0, 0, −3), demokratisch in der Generationen-Basis, für Leptonen √3 stärker; nur das Gewicht ist frei. |
| Mischungswinkel (PMNS, CKM) | **C** | `prop:pmns-z3` widerlegt (v4.8.0-r12), TM1 und H8 mit JUNO disfavorisiert (v4.8.0-r13), CKM-Zeile hängt an einer Koinzidenz (v4.8.0-r09). Offen: H9 (sin²θ₁₂ = 0,30862) für die nächste JUNO-Messung, nachträglich gefunden. |
| Neutrino-Massenordnung | **B** | H2 verträglich, normale Ordnung, Σm_ν = 0,059 eV (v4.8.0-r12); trennt schwach. |
| Feinstrukturkonstante, Weinberg-Winkel | **B**, offen | k-Tabelle (`thm:k-values`: α „first Dixon plane“); cot θ_W (on-shell) ≈ γ_L, Vorhersage H15 für m_W, noch nicht entschieden (v4.9.0-r07). γ_L selbst ist eingesetzt (OP1). |
| β_sym, γ_L | **B** | Aus γ_BI und γ_string eingesetzt (v4.8.0-r03); OP1 offen (Issue #10). |
| Higgs-Mechanismus | **B**, Typ festgelegt | Nur formal als Portgewichtung (v4.9.0-r06). v4.9.0-r44 (H29): Die farb- und Lorentz-verträglichen Massenterme sind antilinear (Frame-Kopplung M ↔ T) und tragen genau die Quantenzahlen von H und H̃; eichinvariant ist nur ein ν^c-Majorana-Term. Die Art der nötigen Brechung ist damit festgelegt, ihre Ursache nicht. |
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
4. `thm:SM` und `thm:three-generations` tragen seit v4.9.0-r36 einen `\qsstatus`-Vermerk (Autorentscheidung 2026-10-23, nach der
   Frame-Regel für komplexe Einheiten). `prop:biquaternion-u1su2` noch ohne Vermerk.

## Drei Triolen im Korpus (v4.9.0-r37)

Das Wort „Triole“ benennt mindestens drei Strukturen: die **Frame-Triole** Materie–Photon–Tachyon (Originalarbeit `thm:spring`, ℤ₂ mit
Fixpunkt P, Amplituden 1 : 1 : 3), die **Kern-Triole** K₁, K₂, K₃ mit 120° (ℤ₃, in 𝕆 eine Farbdrehung) und die **Platz-Triole** von 𝕆³
(Triality). Seit v4.9.0-r38 (H23): 120°-Triole und Frame-Triole sind zwei Ansichten derselben S₃ auf den Plätzen (ℤ₃-Bahn bzw. Transposition; Photon = fester Vektor-Platz, Materie/Tachyon = Spinor-Plätze). Frames und Generationen können nicht auf derselben Ebene auf den Plätzen liegen; seit v4.9.0-r39 (H24) trennt sie im Modell die Zoomstufe des Hilbert-Shifts (ab Stufe 2 bleibt nur der Generationenkreis). Autorabsicht: Die Triole ist eine Darstellung der Sphäre; die Selbstdurchwanderung wechselt zwischen den Gestalten, ohne
festgelegte Periode. Die Struktur hat die Perioden {1, 2, 3, 4, 6, 12}.

## Aussichtsreiche Abzähl-Tests (Vorschlag, jeweils mit Vorab-Notiz)

| Rang | Test | warum aussichtsreich | was er riskiert |
|---|---|---|---|
| 1 (erledigt, r34) | **Ladungen einer Generation aus der Dixon-Ablage**: Liefert der Zahloperator auf ℂ⊗𝕆 (bzw. in der Ablage) die Ladungen 0, 1/3, 2/3, 1 und ihre Zuordnung zu Leptonen und Quarks? | in der Literatur für ℂ⊗𝕆 gezeigt; wäre die erste Ladungsaussage des Companion | Gelingt es mit der Companion-Zuordnung (Farbe auf e₄..e₆, Singulett e₇) nicht, ist die Zuordnung falsch |
| 2 (erledigt, r37: Träger ja, Verbot nein) | **Genau drei Generationen**: Ist die Triality-Form Re((xy)z) die Spin(8)-Triality, und schließt sie eine vierte Generation aus? | ein echtes Verbot, rein mathematisch prüfbar | Lässt die Struktur auch vier Plätze zu, erklärt sie die Drei nicht |
| 3 | **Woher die schwache SU(2)?** Gibt es neben Lorentz (links) und Generationen (rechts) eine dritte, verträgliche SU(2) in der Ablage, und wirkt sie chiral? | würde den dreifach belegten ℍ-Faktor auflösen | Gibt es keine, ist `thm:SM` in der jetzigen Form nicht haltbar |
| 4 | **Hyperladung statt Elektromagnetismus**: Lässt sich das U(1) aus `thm:SM` als Hyperladung lesen, sodass Q = T₃ + Y/2 herauskommt? | Abzählung, keine Präzisionszahl | Passt keine Zuordnung, ist die U(1)-Zeile falsch |

Rang 1 und 2 lassen sich ohne neue Annahmen über Dynamik prüfen. Beide sind auch in Lean formalisierbar.
