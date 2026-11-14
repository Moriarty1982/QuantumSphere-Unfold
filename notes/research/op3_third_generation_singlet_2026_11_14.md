# Erkundung: Die dritte Generation als Singulett – S ⊕ O gegen O³

14. November 2026. Autor: „Dritte Generation suchen“. Rückwärtssuche über Bedingungen, keine Simulation von
Kandidaten. Erkundung ohne Vorab-Notiz, kein Datenvergleich, keine H-Nummer, kein MMA-Beleg, keine Änderung an Guards.
Einordnung T5/T7/T8, OP3. Skript `op3_third_generation_singlet_2026_11_14.py`, Ausgabe `..._out.txt`.

**Blindheit:** Der Vergleich der Z₃-Zerlegungen (Punkt 1) war vor der Rechnung nicht bekannt. Punkt 2 ist analytisch
und nur nachgerechnet. Punkt 3 folgt aus der Konstruktion und ist nicht blind.

## Vorwissen geprüft
- `op3_family_su2_right_action_2026_11_14.md`, `op3_majorana_vector_n_2026_11_14.md`: C⊗S als Familien-Dublett, zwei
  Generationen, kein Spektrum.
- `op3_triality_carrier_gate_2026_11_12.md` (Weg B): O³ mit t(x,y,z) = Re((xy)z), τ(x,y,z) = (y,z,x),
  ρ(x,y,z) = (x̄,z̄,ȳ); diagonale Automorphismen vertauschen mit den Slotoperationen.
- K28 (`v4_8_0_r03_r12/llm/Trennung_Farbe_Generation.md`): S = (1,1) ⊕ (1,sgn) ⊕ (7,2) unter G_2 × S_3.
- k85: Q8 = Q_S|_O gibt auf C⊗O genau eine Generation.
- `op3_neutral_su2_octant_2026_11_13.md`: Einbettungstabelle (SO(3) als Vektor ohne Spinor; SU(2) als 2 + 1).
- `op3_gram_torus_bound_2026_11_12.md`, `op3_generation_carrier_review_2026_11_13.md`: K ≤ 1/2 für reelle Träger.
- Nicht gefunden: ein Vergleich von S ⊕ O mit O³ als Darstellungen des Zyklus.

## Suchrichtung
Ziel: drei Generationen, davon C⊗S als Dublett und eine als Singulett (2 + 1). Notwendig:
1. Farbe und Ladung auf dem ganzen Träger, mit dem Inhalt dreier Generationen;
2. ein Zyklus der Ordnung 3, der auf dem Dublett als Element von SU(2) wirkt und das Singulett festlässt;
3. Verträglichkeit mit dem Slotzyklus τ, falls der Träger Weg B (O³) sein soll.

Dass irgendeine su(2) vom Typ 2 + 1 existiert, folgt für drei Generationen aus Schur (Kommutant U(3) je Teilchenart)
und ist kein Befund. Geprüft wird, ob die vorhandenen nativen Zyklen ψ und τ dazu passen.

## Ergebnis

**1. S ⊕ O und O³ stimmen im farbigen Teil überein und unterscheiden sich in genau einer neutralen Ebene.**
Vielfachheiten der Eigenwerte (1, ω, ω̄) des Zyklus auf den reellen Trägern:

| Träger | gesamt | farbneutral | farbig |
|---|---|---|---|
| (S, ψ) | (2, 7, 7) | (2, 1, 1) | (0, 6, 6) |
| (S ⊕ O, ψ ⊕ 1) | (10, 7, 7) | (4, 1, 1) | (6, 6, 6) |
| (O³, τ) | (8, 8, 8) | (2, 2, 2) | (6, 6, 6) |

Je Teilchenart, komplex, mit Q_* ⊕ Q8 beziehungsweise Q8 je Slot:

| Teilchen | ψ ⊕ 1 auf S ⊕ O | τ auf O³ |
|---|---|---|
| ν | (2, 1, 0) | (1, 1, 1) |
| e⁺ | (2, 0, 1) | (1, 1, 1) |
| u | (3, 3, 3) | (3, 3, 3) |
| d̄ | (3, 3, 3) | (3, 3, 3) |

Für die Quarks ist „S als Dublett plus O als Singulett“ also dieselbe Z₃-Darstellung wie Weg B. Bei den Leptonen ist
eine gedrehte Ebene durch zwei feste Richtungen ersetzt. Das ist die Ebene span(1, e_8) der Sedenionen: Unter ψ sind
1 und e_8 fest, in O³ dreht τ die entsprechende Ebene. Genau dort sitzen die Ladungsachse e_8 und der ψ-feste
Neutrinozustand 1 + i e_8.

**2. Die e_8-Ladung lässt sich nicht τ-symmetrisch auf drei Plätze setzen.** Auf dem neutralen Teil R² ⊗ R³ braucht
eine Ladung Q = 1/2 − (i/2)A eine komplexe Struktur, A² = −1. Mit dem Ansatz A = d(1 ⊗ J) + c(Zyklus ⊗ X) und der
Paarkopplung X aus der Sedenionen-Multiplikation:

| X aus | Gestalt | kleinstes \|A² + 1\| bei \|c\| ≥ 0,3 |
|---|---|---|
| L_e8 (die e_8-Ladung) | Spiegelung | 0,31 (am Rand, wächst mit \|c\|) |
| R_e8 | Eins | 1,41 |
| L_e15 | Spiegelung | 0,31 (am Rand) |
| R_e15 | Drehung J | 0 bei \|c\| = 2/3, \|d\| = 1/3 (exakt, 3·10⁻¹⁶) |

Grund: Im Nebendiagonalblock von A² steht c²·XᵀXᵀ, und das ist für eine Spiegelung c²·1. Q_* ist also eine
Paarstruktur; sie zeichnet zwei Plätze aus und bricht τ. Die eine Lösung (X = J) ist A = M ⊗ J mit M = −1 auf der
symmetrischen Mode und +1 auf dem τ-Dublett: die Slot-Ladung mit e_7, mit entgegengesetzter Orientierung auf
Singulett und Dublett.

**3. Weg B hat ein τ-symmetrisches 2 + 1 für alle Teilchenarten.** Mit Q8 je Slot vertauscht τ mit Farbe und Ladung,
und der Inhalt sind drei Generationen. Die Fourier-Moden der Slots zerlegen die Generationen in die symmetrische Mode
(Singulett, τ = 1) und das Dublett (ω, ω̄). Auf dem Dublett ist τ = diag(ω, ω̄): Determinante 1, Ordnung 3, also ein
Element von SU(2) wie im Profil verlangt. Die Bahn eines Dublett-Zustands unter τ:
- Ein reeller Slot-Vektor liegt am Äquator: ρ² = 1/4, K = 1/2.
- Ein Zustand unter dem magischen Winkel gäbe ρ² = 1/2, K = 2/3, π/4. Einen nativen Grund dafür gibt es nicht.

Die native Slotgruppe von Weg B ist S_3 = ⟨τ, ρ⟩. Auf der Bloch-Kugel des Dubletts ist das eine Diedergruppe: Die
zweizähligen Achsen stehen senkrecht auf der dreizähligen (analytisch). Der magische Winkel kommt in ihr nicht vor.

## Bewertung
- **Die beiden Wege sind komplementär.**

  | | Weg A (C⊗S, Q_*) | Weg B (C⊗O³, Q8 je Slot) |
  |---|---|---|
  | Generationen | 2 | 3 |
  | Zyklus der Ordnung 3 auf einem Dublett | ψ (nur als Phase, Leptonen (1, ω)) | τ = diag(ω, ω̄), alle Arten |
  | Gruppe mit magischem Winkel | 2T (Hurwitz-Einheiten von H_n) | fehlt; S_3 gibt nur 90° |
  | K aus nativem Bezug | 2/3 (mit Annahme e_8) | 1/2 |

- **Antwort auf die Frage:** Eine dritte Generation als Singulett neben C⊗S gibt es im Sinn von Weg B für die Quarks
  ohne Widerspruch. Für die Leptonen passt sie nicht: Die Ebene span(1, e_8), an der Q_* und N hängen, hat in O³ kein
  Gegenstück, und Q_* lässt sich nicht τ-symmetrisch fortsetzen. S ⊕ O mit Q_* ⊕ Q8 bleibt möglich, ist dann aber
  eine Setzung ohne Zyklus über alle drei Generationen.
- **Was jetzt genau fehlt:** auf dem τ-Dublett von Weg B eine zweizählige Achse unter dem magischen Winkel, also eine
  Erweiterung von S_3 zu 2T (oder A_4 auf der Bloch-Kugel). Oder umgekehrt in Weg A ein dritter Platz, der die Ebene
  span(1, e_8) nicht festhält.
- r55 nennt A_4 als gemeinsame Platzsymmetrie von Dixon-Ablage und Trialitätsplätzen. Ob dieses A_4 auf dem τ-Dublett
  wirkt (A_4 hat keine zweidimensionale irreduzible Darstellung, 2T schon), ist hier nicht geprüft.
- Koide 2/3 und die Phase sind **nicht** hergeleitet. OP3/OP4 bleiben offen. OP1–OP5, C5 und C6/T2 sind unverändert.
  H100 und H102 bleiben unberührt. Die Aussagen zu Weg A erben die Guards von CT-003.
- Zurückgestellte Ideen: Keiner der Auslöser I1–I5 trifft zu.

## Mögliche nächste Schritte (Autorentscheidung)
- Prüfen, ob die volle Trialitätsgruppe (Spin(8) mit äußerem S_3, r37) oder das A_4 aus r55 auf dem τ-Dublett eine
  zweizählige Achse außerhalb des Äquators liefert. Das ist die direkt benannte Lücke.
- Die Linie ablegen, bis H100 oder H102 entschieden sind.
