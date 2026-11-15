# OP3: Die Koide-Phase und die Helizitätsachse des (E,B)-Dubletts

15. November 2026, Claude Opus. **Erkundung, nicht blind** (K = 2/3, die Phasen und die Ergebnisse (1)–(3) standen
analytisch vorher fest). Auftrag des Autors: „Ja, prüfen“, nach dem Vorschlag, die Generationen auf der Stokes-Kugel des
Feld-Dubletts (E, B) statt unter den Materiezuständen von C⊗O zu lesen (Anlass: der Nachtrag in
`../op3_frame_map_generations_2026_11_15/README.md`). Keine H-Nummer, kein CT-Eintrag, Guards unverändert.
Skript `helicity_axis.py`, Ausgabe `run/helicity_axis_stdout.txt`.

## Vorwissen geprüft
- **v4.9.0-r04.2:** Die Gram-Matrix G von (E, B) ist für reelle Felder symmetrisch, ohne σ_y-Teil; die Zustände füllen eine
  Scheibe. Materie (b₁ > 0) und Tachyon (b₁ < 0) liegen gegenüber, das Licht in der Mitte, die Photonseite ist sign b₂.
  J_B spiegelt b₁, T spiegelt b₂. Unter Boosts wandert b entlang seiner eigenen Richtung.
- **v4.9.0-r05.2(b):** Für zeitharmonische Felder mit komplexen Amplituden ist der σ_y-Teil von Ĝ = F̂†F̂ gleich
  −2 Im(Ê*·B̂), ±1 für zirkulare und 0 für lineare Polarisation. **Die dritte Achse ist die Helizität**, erzeugt von der
  Dualitätsdrehung; mit ihr wird die Scheibe zur Kugel, das Licht liegt auf der Helizitätsachse. Die Kopplung an
  Schwarze Löcher ist dort offen.
- **v4.9.0-r51:** Die Tachyon-Abbildung z ↦ iz ist σ_y; die Ports sind die Eigenräume von iL_e7.
- **v4.10.0-r07.2(a), (b):** Die Dualitätsdrehung ist eine Symmetrie des freien Maxwell-Feldes (erhaltene Helizität) und
  vertauscht mit Boosts.
- **Literatur:** Tang und Cohen, PRL 104, 163901 (2010) (optische Chiralität, Lipkins Zilch); Bliokh und Nori, PRA 83,
  021803 (2011) (Chiralitätsdichte und Helizität; Verhältnis zur Energiedichte betragsmäßig ≤ 1). Helizität ist nach
  Noether die Erhaltungsgröße der Dualitätssymmetrie. Die Formel für zeitharmonische Felder steht im Repo in r05.2(b);
  die Originalarbeiten sind nicht im Volltext gelesen.

## Ergebnisse
1. **Die Tachyon-Abbildung ist die halbe Drehung um die Helizitätsachse.** (E, B) ↦ (−B, E) ist die Dualitätsdrehung um
   90°; sie kippt b₁ und b₂ und erhält b_y. T, also (E, B) ↦ (E, −B), kippt b₂ und b_y; J_B, also (E, B) ↦ (B, E), kippt b₁
   und b_y. Das ist das Muster von r51.1(a): R erhält die Chiralität, T und J_B tauschen sie. **Die Chiralität der
   Algebra und die Helizität des Dubletts verhalten sich unter den drei Frame-Abbildungen gleich.**
2. **Die σ_y-Pole sind die Ports.** Die σ_y-Eigenvektoren (1, ±i) gehen unter der Abbildung φ von r51.1(c) in 1 ± i e₇
   über, und das sind Eigenvektoren von iL_e7 zu ±1, also Kompensator- und Partnerport. Die Konjugation tauscht sie.
3. **Ohne Helizität keine Koide-Phase.** Drei Zustände in der Scheibe (b_y = 0) haben die Bargmann-Phase 0 oder π
   (500 Stichproben). Für jedes Oktant-Tripel (drei orthonormale Bloch-Vektoren) gilt dagegen exakt
   **Σ_k b_{y,k}² = 1**: Die drei Zustände tragen zusammen genau eine Einheit Helizitätsgewicht, wie man das Oktant auch
   dreht. Reelle Felder allein können die Koide-Phase also nicht tragen; sie braucht komplexe Amplituden, also den
   C-Faktor.
4. **Unter Boosts ist b_y nicht invariant.** Für allgemeine komplexe Amplituden ändert sich b_y unter Boosts deutlich
   (bis |Δb_y| = 1,07 in 300 Stichproben). Erhalten bleibt nur die Zerlegung in die Helizitätsanteile F± = E ± iB: Ein reiner
   Anteil bleibt rein, und die Dualitätsdrehung vertauscht mit dem Boost. Die Gewichte der beiden Anteile ändern sich.

## Folgerungen
- **Was trägt:** Die Lesart ist mit dem Bestand verträglich und braucht kein neues Qubit. Das Dublett (E, B) mit der
  Helizitätsachse aus r05.2 hat genau die drei Achsen σ_z (Materie gegen Tachyon), σ_x (Photonseite) und σ_y (Helizität),
  und die drei Frame-Abbildungen wirken darauf wie in r51. Es gibt dort kein Ladungsproblem wie auf C⊗O, weil die
  Zustände Feldzustände sind.
- **Was nicht trägt:** Der Ort eines Zustands auf der Kugel hängt vom Bezugssystem ab, für b₁, b₂ schon nach r04.2(c) und
  nach (4) auch für b_y. Überlappungen und damit Koide-Daten wären frame-abhängig. Wie in
  `../op3_horizon_shadow_2026_11_15/README.md` (Folgerung 2) müsste die Kugel in einem ausgezeichneten Frame gelesen
  werden. Für ein reelles Feld gibt es ihn (E ∥ B, r04.2(c)); dort liegt der Zustand aber auf dem Rand der Scheibe, ohne
  Helizitätsanteil. Für komplexe Amplituden ist ein solcher Frame nicht untersucht. Ein Frame, in dem drei Generationszustände zugleich ausgezeichnet sind, ist nicht gefunden.
- **Offen wie zuvor:** wie ein Feld-Dublett die Generationen geladener Leptonen trägt (das ist eine Lesart, kein
  Mechanismus); die Überlappung ½; die Biegung zu φ = 2/3 (Kern, γ_M, OP1).

## Einordnung
Ergebnis (1) ist der eigentliche Gewinn: Die Helizitätsachse des Feldes und die Chiralität der Algebra zeigen unter T, J_B
und R dasselbe Verhalten. Damit hängen zwei bisher getrennte Stellen des Papers zusammen (r04/r05 und r51). Für OP3 heißt
es: Die Koide-Phase ist ein Helizitätseffekt, sie braucht komplexe Amplituden. Woher die Überlappung ½ kommt und in
welchem Frame die drei Zustände gelesen werden, bleibt offen.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert.

## Nachtrag 15.11.2026: das Lorentz-invariante Dublett χ = (√s₊, √s₋)
Auftrag des Autors: „Ja, prüfen“, nach dem Vorschlag, die frame-abhängige Hermitesche Stokes-Kugel durch die bilinearen
Invarianten zu ersetzen. **Erkundung, nicht blind.** Skript `invariant_doublet.py`, Ausgabe
`run/invariant_doublet_stdout.txt`.

**Ansatz.** Mit F± = E ± iB sind s± = F±·F± bilinear. Ein Boost wirkt auf F₊ als komplexe Drehung M ∈ SO(3, C) und auf F₋
als M̄; nach v4.8.0-r06.3 bleiben s₊ und s₋ erhalten. Das Paar χ = (√s₊, √s₋) ist ein Dublett, dessen Bloch-Kugel nicht
vom Bezugssystem abhängt. Die Hermitesche Stokes-Kugel von r05.2 hängt dagegen davon ab (Ergebnis (4) oben).

**Ergebnisse**
1. s₊ und s₋ sind unter 500 zufälligen Boosts komplexer Amplituden invariant (relative Abweichung höchstens 10⁻¹⁴).
2. Reelle Felder liegen auf dem Äquator, und ihr Winkel ist −arg s, also die Richtung in der Scheibe von r04 (Radius |b|
   entfällt, nur die invariante Richtung bleibt).
3. Die Frame-Abbildungen wirken wie in r04.2(b) und r51: R dreht den Äquator um π (arg s ↦ arg s + π, Materie ↔ Tachyon),
   T spiegelt arg s ↦ −arg s, J_B spiegelt arg s ↦ π − arg s. Auf die Helizitätskomponente: R erhält sie, T und J_B kehren
   sie um (für allgemeine komplexe Felder geprüft).
4. **Zweigwahl.** Die Wurzeln haben je ein Vorzeichen. Für reelle Felder gibt √s₋ = conj √s₊ eine natürliche Wahl. Die
   andere Wahl liefert den um π um die Helizitätsachse gedrehten Punkt, also genau das R-Bild. Für allgemeine komplexe
   Felder ist ein Punkt der Kugel deshalb nur bis auf R bestimmt; an den Polen spielt die Wahl keine Rolle.
5. **Ein invariantes Oktant existiert.** Materiefeld (E = e₁, B = 0, s = 1), Feld der Photonseite (E = B = e₁/√2, s = i) und
   selbstduales Feld (E = i e₁, B = e₁; s₊ = −4, s₋ = 0, Nordpol). Paarweise Überlappung ½, K = 2/3, Bargmann-Phase −π/4
   (Vorzeichen nach Orientierung). Unter 50 zufälligen Boosts bleiben alle drei Strahlen unverändert.

**Folgerungen**
- **Der Frame-Einwand entfällt.** Auf der invarianten Kugel hängen Überlappungen, K und Phase nicht vom Beobachter ab.
  Die drei Ecken des Oktanten sind drei Feldtypen, die in jedem Bezugssystem dieselben sind: Materie, Photonseite,
  Helizität. Das Oktant aus beiden Zweigen ist eindeutig: Die Äquatorzustände sind reell (natürlicher Zweig), der Pol ist
  zweigfrei.
- **Licht hat keinen Punkt:** Für ebene Wellen ist s₊ = s₋ = 0, also χ = 0. Das passt zu r19 (das Photon als
  Informations-Singular, kein Frame wie die anderen).
- **Zweigwahl = Frame-Wahl M/T:** Die Vorzeichenfreiheit der Wurzel ist für komplexe Felder genau der Tausch durch R. Die
  Unterscheidung von Materie und Tachyon braucht dort eine Spinorwahl. Ob r02.1/r06.4 sie festlegen, ist nicht geprüft.
- **Unverändert offen:** Die Überlappung ½ ist gesetzt (das Oktant wird invariant, nicht hergeleitet). Wie ein
  Feld-Dublett die Generationen geladener Leptonen trägt, bleibt eine Lesart. Die Biegung zu φ = 2/3 bleibt beim Kern
  (γ_M, OP1).

## Nachtrag 15.11.2026: drei Vorzeichen, Frame-Abbildungen als Vierergruppe, kein Dreierzyklus
Auftrag des Autors: „Ja, prüfen“. **Erkundung, nicht blind.** Skript `frame_labels.py`, Ausgabe
`run/frame_labels_stdout.txt`.

**Ergebnisse**
1. **Die drei Achsen der invarianten Kugel sind drei Vorzeichen eines Feldes:** sign Re s (Materie gegen Tachyon),
   sign Im s = sign E·B (Photonseite, r02.1) und das Helizitätsvorzeichen sign(|s₊| − |s₋|). Jede Frame-Abbildung kippt
   zwei davon und erhält genau eines:

   | Abbildung | Re s | Im s | Helizität |
   |---|---|---|---|
   | R | kippt | kippt | bleibt |
   | T | bleibt | kippt | kippt |
   | J_B | kippt | bleibt | kippt |

   Die drei Abbildungen bilden (auf den Vorzeichen) die Kleinsche Vierergruppe.
2. **Die Pole sind die Eigenzustände.** Materiefeld und Tachyonfeld sind Eigenzustände von T (Eigenwerte ±1), die beiden
   Felder der Photonseite Eigenzustände von J_B (±1), selbst- und antiselbstduales Feld Eigenzustände von R (±i). Keiner
   dieser Zustände ist Eigenzustand einer zweiten Abbildung.
3. **Keine lineare Feldabbildung vertauscht die Achsen zyklisch.** Für eine Abbildung der Indexebene (E, B), geschrieben in
   der Basis F± als (F₊, F₋) ↦ (aF₊ + bF₋, cF₊ + dF₋), gilt s₊' = a²s₊ + 2ab F₊·F₋ + b²s₋. Der Mischterm F₊·F₋ ist nicht
   Lorentz-invariant und kommt in χ nicht vor. Auf χ wohldefiniert sind daher nur diagonale (ab = cd = 0, b = c = 0) und
   vertauschende Abbildungen (a = d = 0); numerisch: 0 von 200 zufälligen Abbildungen, ein nicht diagonales Beispiel
   ebenso nicht. Diagonale Abbildungen halten die Pole fest, vertauschende tauschen sie. Keine bringt die
   Helizitätsachse auf den Äquator.

**Folgerungen**
- **Die Überlappung ½ ist bedingt abgeleitet.** Verlangt man von jedem der drei Auslesezustände, Eigenzustand einer
  Frame-Abbildung zu sein, und zwar je einer anderen, liegen sie an Polen dreier senkrechter Achsen: Überlappung ½,
  K = 2/3, Phase ±π/4, invariant unter Boosts. Das Prinzip „vollständiger Satz“ der Komplementaritätsnotiz entfällt, weil
  es genau drei Frame-Abbildungen gibt. Gesetzt bleibt „je Frame-Abbildung ein Auslesezustand“.
- **Die Verteilung auf drei Abbildungen folgt nicht aus einer Feldsymmetrie.** Ein Dreierzyklus der Achsen müsste aus einer
  anderen Struktur kommen. Kandidat im Bestand: die Hurwitz-Einheiten, die auf dem neutralen Qubit N die drei Pauli-Basen
  zyklisch vertauschen (r13.2, unter CT-003). Eine Verbindung von N mit χ ist nicht untersucht.
- **Vorbehalt:** In der Gram-Lesart sind die Massenwurzeln die Eigenwerte der Gram-Matrix; die drei Zustände sind
  Auslesezustände, nicht die Masseneigenzustände.
- Unverändert offen: Biegung (γ_M, OP1), Bezug zu geladenen Leptonen.

## Nachtrag 15.11.2026: Der Hurwitz-Zyklus auf N liefert den Dreierzyklus nicht
Auftrag des Autors: „weiter“. **Erkundung, nicht blind** (analytisch vorher absehbar). Skript `hurwitz_cycle_check.py`,
Ausgabe `run/hurwitz_cycle_check_stdout.txt`.

Gesucht ist eine Struktur, die die drei Feldachsen (Re s, Im s, Helizität) und damit die drei Frame-Abbildungen zyklisch
vertauscht. Feldabbildungen tun es nicht (Nachtrag davor). Kandidat war der Zyklus der Hurwitz-Einheiten auf dem neutralen
Qubit N (v4.10.0-r13.2, unter CT-003), der dort drei Pauli-Basen vertauscht.

1. **R ist auf N ein Skalar** (R|_N = i·1), wie auf C⊗O. R zeichnet auf N keine Achse aus.
2. **T bildet N nicht in sich ab:** conj(N) steht senkrecht auf N (Anteil 0), es ist der ladungskonjugierte Raum N̄. T und
   J_B tauschen N und N̄.
3. Auf χ ist R dagegen eine echte Drehung, und T, J_B sind lineare Pauli-Drehungen. Die Frame-Gruppe wirkt auf N und auf χ
   verschieden. **Eine mit R, T, J_B verträgliche Identifikation von N mit χ gibt es nicht.** Der Hurwitz-Zyklus vertauscht
   Paulis der Rechtswirkung, also der Familien-su(2) von r13.4, nicht die Frame-Abbildungen.

Dazu eine Bemerkung ohne Rechnung: Auf der komplexifizierten Indexebene (E, B) vertauscht das Clifford-Element der
Ordnung 3 die drei Operatoren T ~ σ_z, J_B ~ σ_x und R ~ σ_y zyklisch durch Konjugation. Als Feldabbildung ist es aber nicht
diagonal und daher auf χ nicht wohldefiniert (Nachtrag davor, (3)). Der Zyklus existiert also auf der Ebene der Operatoren,
steigt aber nicht auf die invariante Kugel ab.

**Stand:** Für „je Frame-Abbildung ein Auslesezustand“ ist im Bestand keine Begründung gefunden; das Prinzip bleibt gesetzt.
Zurückgestellte Ideen geprüft: kein Auslöser von I1–I4 trifft auf diese Lücke zu.

## Nachtrag 15.11.2026: Auslesungen eines Objekts sind höchstens drei, und sie bilden ein Oktant
Auftrag des Autors: „Ja, prüfen“. **Erkundung, nicht blind** (das Ziel 3 und 2/3 war bekannt; die Bedingungen sind danach
formuliert). Skript `non_orthogonal_readouts.py`, Ausgabe `run/non_orthogonal_readouts_stdout.txt`.

**Bedingungen.** (1) Eine Auslesung ist Eigenzustand einer Frame-Abbildung. (2) Zwei Auslesungen desselben Objekts sind
nicht orthogonal: Orthogonale Zustände schließen einander aus und wären verschiedene Objekte, nicht zwei Lesarten eines
Objekts (Bedeutung (4) von „ein Objekt“ in `../k220_ein_objekt_2026_11_07/README.md`). (3) Maximalität: Alle solchen
Auslesungen kommen vor.

**Ergebnisse**
1. Auf χ wirken R, T, J_B exakt als σ_z, σ_x, σ_y (bis auf Phase; Abweichung von der Feldwirkung 4·10⁻¹⁶ an den sechs Polen
   und 200 reellen Feldern). Jede hat genau zwei Eigenstrahlen; zusammen sind das die **sechs Pole**: Materie und Tachyon (T),
   die beiden Photonseiten (J_B), selbst- und antiselbstdual (R).
2. Von den Teilmengen der sechs Pole sind 26 ohne orthogonales Paar. Die größte Größe ist **3**, und es gibt genau **8** solche
   Tripel. Alle haben paarweise Überlappung ½, K = 2/3 und Phase ±π/4.
3. Die Frame-Abbildungen zerlegen die 8 Tripel in **2 Bahnen zu je 4**, getrennt nach dem Vorzeichen der Phase (Ecken nach
   Achsen geordnet): −π/4 und +π/4.

**Folgerungen**
- Aus (1)–(3) folgen zugleich die **Zahl drei**, die **Überlappung ½** (K = 2/3) und die **Phase π/4** bis aufs Vorzeichen. Das
  Tripel ist bis auf Frame-Abbildungen und Orientierung eindeutig.
- **Ein Dreierzyklus wird nicht gebraucht.** Die Verteilung auf drei verschiedene Frame-Abbildungen erzwingt die Bedingung
  „nicht orthogonal“: Zwei Auslesungen derselben Abbildung wären orthogonal.
- Die bisher gesetzte Regel „je Frame-Abbildung ein Auslesezustand“ ist damit auf (2) und (3) zurückgeführt.
- **Gesetzt bleiben:** die Maximalität (3) und die Eigenzustands-Bedingung (1); dazu das Vorzeichen der Phase (nur die
  Zeitumkehr kehrt es um), die Biegung zu φ = 2/3 (γ_M, OP1) und der Bezug zu geladenen Leptonen. Die drei Zustände sind
  Auslesezustände; die Massenwurzeln sind die Eigenwerte der Gram-Matrix.
