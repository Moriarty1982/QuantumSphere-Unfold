# OP3: Lässt sich die Brücke aus r15.5 zeigen? Kommutanten-Prüfung

15. November 2026, Claude Opus. **Erkundung, nicht blind:** Das Ergebnis folgt vor der Rechnung aus dem Lemma von Schur;
die Rechnung bestätigt es auf dem konkreten Träger. Auftrag des Autors: „kannst du versuchen die brücke aus r15.5 zu zeigen“.
Keine H-Nummer, kein CT-Eintrag, Guards unverändert. Skript `frame_bridge_commutant.py`, Ausgabe
`run/frame_bridge_commutant_stdout.txt`.

## Was zu zeigen wäre
r15.5 liest die drei Generationen als je einen Eigenzustand der drei Frame-Abbildungen T (σ_z), J_B (σ_x) und R (z ↦ iz) des
Dubletts (E, B). Offen ist laut r15.5, ob der Generationsindex auf dem Frame-Dublett sitzt.

## Vorwissen geprüft
- `../op3_frame_map_generations_2026_11_15/README.md`, **Nachtrag 15.11.:** auf C ⊗ O nein. R ist dort skalar, T und J_B haben
  dieselben Eigenstrahlen, kein T-Eigenzustand hat bestimmte Ladung. Geprüft auf Stichproben, nur auf C ⊗ O. Als r16.1 in
  der Runde.
- **r16.2–r16.9** (nachträglich gefunden: Die Rechnung lief zuerst auf einem Zweig vor r16; der Abgleich mit `main` kam
  danach): Die Koide-Phase braucht die Helizitätsachse, also komplexe Amplituden (r16.2). Auf dem Lorentz-invarianten
  Dublett χ = (√s₊, √s₋) wirken R, T, J_B bis auf Phasen als σ_z, σ_x, σ_y (r16.3, r16.7); die sechs Pole geben das Oktant als
  größte nicht orthogonale Auswahl. Die drei Zustände sind Auslesezustände, keine Masseneigenzustände (r16.4). Offen nach
  r16.7: Regel (1) und (3), Vorzeichen, Biegung und **ein geladener Träger**. Diese Erkundung beantwortet den letzten Punkt.
- r14.3(d): T, J_B, R schließen sich zu sl(2, R) zusammen. r14.4: Die Familien-su(2) der Sedenionen (Weg A, unter CT-003)
  fällt auf die Linkswirkung von ℍ, also den Lorentz-Spinor. r13.4: Weg A hat zwei Generationen als Dublett.
- r04: Die Zustände des reellen Dubletts füllen eine Scheibe, keine Kugel (kein σ_y-Anteil).
- Literatur (Prüfung zum Kern-Paper, `paper/kernel-note/outline.md`): Golat, Vernon, Rodríguez-Fortuño, arXiv:2405.15718.
  Für zeitharmonische Felder hat das Dublett (E, H) drei Basen EM, PA, RL; die dritte Achse ist die Helizität.
- Brannen, arXiv:1006.3114: das Koide-Tripel aus den drei unverzerrten Basen des Spins (`paper/koide-note/novelty_check.md`).

## Rückwärtssuche: notwendige Bedingungen
Ein Generations-Qubit im Sinn von r15.5 braucht:
1. **Drei paarweise antikommutierende Involutionen** auf einem zweidimensionalen komplexen Raum W (dann sind ihre Eigenbasen
   paarweise unverzerrt).
2. **Verträglichkeit mit den Symmetrien:** Alle Generationen haben dieselben Eichladungen und denselben Spin. Die drei
   Operatoren müssen deshalb mit SU(3)_c × SU(2)' × U(1)_Y und der Lorentzgruppe vertauschen, also im Kommutanten liegen.
3. **Frame-Abbildungen:** Die drei Operatoren sollen T, J_B und R sein, so wie r51 sie über den C-Faktor definiert.

Nach Schur ist der Kommutant einer Darstellung die Summe von Matrixalgebren M_n(C) über den Vielfachheiten n der irreduziblen
Bestandteile. Antikommutierende Operatoren gibt es darin nur bei n ≥ 2.

## Ergebnisse
**Teil A, reelles Dublett.**
- R² = −1: R ist keine Involution, sondern eine komplexe Struktur. Die Involutionen von O(2) außer ±1 sind die Spiegelungen,
  eine ganze Kreislinie. Paarweise antikommutierend sind davon höchstens zwei (σ_z, σ_x).
- T, J_B, R spannen sl(2, R) auf (Spurform indefinit), nicht su(2). Das passt zur Scheibe von r04.
- Drei unverzerrte Basen entstehen erst nach Komplexifizierung mit einer **zweiten, von i verschiedenen Einheit j**. Dann ist
  jR eine Involution, und alle Überlappungen sind ½. Die Zahl drei ist damit d + 1 für d = 2 (r15.4), nicht die Zahl der
  Involutionen des reellen Dubletts. Auf χ (r16.3) liefern die komplexen Amplituden diese zweite Einheit; dort sind die drei
  Abbildungen Pauli-Matrizen (r16.7). Teil A bestätigt also r14.3(d) und r16.2 und fügt nur die Zählung hinzu.

**Teil B, eine Generation auf C ⊗ ℍ ⊗ O** (Konventionen von `paper/short`, Abschnitt 5; Farbe als Derivationen von O, die e₇
festhalten):
- Die Prüfungen der Konstruktion stimmen: g₂ hat Dimension 14, su(3) Dimension 8, SU(2)' und Y vertauschen mit Lorentz und
  Farbe. Das Spektrum von Y gibt die sechs Weyl-Multipletts (Q, L, u^c, d^c, e^c, ν^c) mit den richtigen Vielfachheiten.
- **Komplex-linearer Kommutant: Dimension 6, kommutativ.** Antilinearer Kommutant: Dimension 0. Der reelle Kommutant ist C⁶:
  je Multiplett nur die Phasen.
- Damit gibt es auf einer Generation **kein** Paar antikommutierender, symmetrieverträglicher Operatoren, also kein
  Generations-Qubit, weder aus den Frame-Abbildungen noch aus anderen Operatoren.
- R = i·1 liegt im Kommutanten, aber zentral. T = K vertauscht nicht mit Lorentz, SU(2)' und Y (es bildet auf die konjugierte
  Darstellung ab, Ladungskonjugation); J_B = iK ebenso nicht.

Das verallgemeinert den Nachtrag vom 15.11. von Stichproben auf C ⊗ O zu einer vollständigen Aussage über alle
symmetrieverträglichen Operatoren auf einer Generation.

**Teil C, n Kopien.** Bei n = 2 vertauschen 1 ⊗ σ_k mit allen Generatoren; der Kommutant enthält M₂(C), und ein Qubit mit drei
unverzerrten Basen ist vorhanden. R wirkt auf diesem Kopienraum skalar, T liegt weiterhin nicht im Kommutanten.

## Folge für r15.5 und für den offenen Punkt „geladener Träger“ von r16.7
- **Auch Auslesezustände brauchen Kopien.** Nach r16.4 sind die drei Zustände Auslesezustände in einem Raum W, und die
  Wurzelmassen sind die Eigenwerte ihrer Gram-Matrix auf dem Generationsraum C³. Damit diese Massenmatrix mit den Ladungen
  vertauscht, muss die Abbildung C³ → W die Identität auf dem Ladungsanteil sein. Der Träger enthält dann C³ (bzw. W) als
  Vielfachheitsraum der Eichdarstellung, und Schur verlangt wieder mehrere Kopien.
- **Nicht zeigbar in der gestellten Form.** Auf einem Träger mit einer Generation schließt Schur jedes Generations-Qubit aus.
  Die Frame-Abbildungen von r51 können den Generationsindex nicht tragen: R ist zentral, T und J_B sind keine Symmetrien.
- **Was nötig wäre:** ein Träger, der die Generation bereits mindestens zweimal enthält (Weg A unter CT-003 hat zwei Kopien),
  und dazu Frame-Abbildungen, die neu auf dem Kopienraum definiert werden. Beides wäre eine Setzung. Die Zahl der Generationen
  wäre dann Eingabe, nicht Ergebnis; die Lesart „drei Generationen = drei Frame-Abbildungen“ würde zirkulär.
- **Was richtig bleibt:** Für das Photon gilt die Brücke. Das Dublett (E, H) zeitharmonischer Felder, komplexifiziert mit der
  Phasoren-Einheit, hat genau die drei Basen EM (σ_z), PA (σ_x, die Kompensator-Ports) und RL (Helizität, Eigenbasis der
  Viertel-Dualitätsdrehung). Das steht bei Golat et al. 2024. Eigen ist am Companion nur der Grund für d = 2: zwei Felder E und B.
- Die einzigen nativen Orte mit drei antikommutierenden Strukturen auf einer Generation sind Spin (Linkswirkung von ℍ) und
  schwacher Isospin (Rechtswirkung). Beide sind Symmetriegeneratoren und nicht im Kommutanten; Koide-Zustände dort brechen
  Drehinvarianz bzw. Q_em (r33, r14.4). Das ist Brannens Bild mit seinem bekannten Einwand.

Kein OP wird geschlossen. OP3 bleibt offen; die Lesart r15.5 wird eingeschränkt, nicht berichtigt. Nach Append-only gehört der
Befund als Statusvermerk in eine neue Runde.

## Zurückgestellte Ideen
Ein Ansatz ist gescheitert; geprüft gegen I1–I5 (`../v4_10_0_w1/Zurueckgestellte_Ideen.md`). Keiner der Auslöser trifft zu:
keine zwei unvereinbaren Frames oder Lichtkegel (I1), keine Schließungsbedingung mit unklarem Platz (I2), keine Λ- oder
Dunkle-Materie-Rechnung (I3), kein Higgs- oder Tachyon-Sektor (I4), keine Infrastrukturfrage (I5).
