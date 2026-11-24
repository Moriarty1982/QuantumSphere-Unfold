# Feldkonfigurationen des HS-Turms rückwärts (Erkundung k270–k272, nicht blind, 24.11.2026)

**Ergebnis in einem Satz:** Von oben her gelesen sind fast alle Wahlen im Turm erzwungen oder bloße Konvention. Die
Anomaliefreiheit verlangt N_c = 3 Leitern, und die gibt es erst bei HS(3) (𝕆). HS(2) allein ist anomal und kann daher nicht die
letzte Stufe sein. Das Drehsinn-Bit von HS(1) wird ab HS(2) wegdrehbar und lebt als Links/Rechts-Bit weiter, das r43 durch die
Anomalien festlegt. Das HS(0)-Feld muss schwingen: Jede Variante mit Wachstum oder Drift im Ursprungsfeld (oder in einem späteren
Shift) verliert die kompakte Farbgruppe und hat schon ab HS(1) Nullteiler. Amplitude, Frequenz und Phase des Ursprungsfelds sind
dagegen frei und oben unsichtbar.

Auftrag des Autors (24.11.2026): die Feldkonfigurationen der HS-Stufen rückwärts herausfinden, um zu verstehen, warum etwas so sein
muss; danach das Ursprungsfeld variieren. **Erkundung, nicht blind:** Die Algebra ist Standard (Hurwitz, G₂, gespaltene
Oktonionen, Witten-Anomalie, Furey-Leitern). Neu sind nur die Rückwärtskette im Turm und die Variation des HS(0)-Vorzeichens.
Keine H-Nummer, keine Runde. Vergeben: Skripte **k270, k271, k272** (k257–k269 nutzt ein anderer Faden).

Werkzeuge: Python (numpy, sympy) für die Algebra, die exakten Anomaliespuren und die 27 Vorzeichenmuster (k270, k272). Wolfram
Language unabhängig für die Anomaliespuren N_c = 1…7 und die HS(0)-Gleichung (k271). Die Warnungen dort sind in `k271_out.txt`
festgehalten; die Werte stimmen exakt mit sympy überein. Qiskit wurde nicht eingesetzt (keine Schaltung, kein Messablauf). Kein
HDL-Vergleich (kein RUN_TAPE).

## Vorwissen geprüft
k253 (Regel ψ̇ = uωψ, Turm HS(0)–HS(4)), k254 (Radon–Hurwitz-Achsen 1, 3, 7, 8, 9; S₃; Nullteiler), k255/k256 (Koide aus exp(uπ/4),
Mischung), H19 (Ladungen 0, ⅓, ⅔, 1 auf ℂ⊗𝕆 bestätigt, Konvention u = e₇), r42 (C = ½(1 + iL_e₇) als Chiralitätsprojektor, eine
Generation mit ν_R), r43/H28 (vier Projektoren, Tr Y = 0 ⇒ s = −½, Anomalien wählen Linksmultiplikation, Rest = SM und Frame-Spiegel),
k246, k250 (Drehsinn gesetzt), Frame-Konvention F (Tachyon-Abbildung z ↦ iz). Bisher nicht im Repo: N_c aus der Anomalie im Turm,
das Verhalten des Drehsinn-Bits beim Aufstieg und die Variation des Verdopplungsvorzeichens.

## Rückwärts: was jede Stufe sein muss

| Stufe | Was oben verlangt wird | Nötige Konfiguration | erzwungen | Konvention oder frei |
|---|---|---|---|---|
| HS(3) | SU(3) ungebrochen, Ladungen k/3, anomaliefrei | genau **eine** feste Einheit u in 𝕆; C = ½(1 + iL_u) | N_c = 3; eine Einheit; links (r43); s = −½ | Richtung von u (G₂ wirkt transitiv auf S⁶) |
| HS(2) | Dubletts mit ΔQ = 1, gerade Dublettzahl | eine Leiter (Spin ½), zwei vertauschende SU(2) | dass eine Seite gewählt wird | Achse (SO(3) transitiv) |
| HS(1) | Projektor auf eine Generation | Bild von C = reiner Kreisanteil (b = 0) | die Zerlegung in zwei Kreisanteile | Drehsinn: ab HS(2) wegdrehbar |
| HS(0) | kompakte Gruppen, keine Lecks bis HS(3) | beschränkte Schwingung, a = b | Vorzeichen ψ̈ = −ω²ψ | Amplitude, Frequenz, Phase |

### 1. HS(3): warum genau 𝕆 und genau eine Einheit (k270 A–C, k271)
- **Stabilisatoren in G₂** (k270 A): nichts fest 14 (G₂), eine Einheit 8 (SU(3)), zwei Einheiten 3 (SU(2), sie erzwingen die dritte),
  Quaternion-Tripel 3, nicht-assoziatives Tripel 0. Alle kompakt. SU(3) bleibt also genau dann ungebrochen, wenn das Feld **eine**
  Einheit festhält. Welche Einheit es ist, ist Konvention, denn G₂ dreht jede in jede andere.
- **J = iL_u ist die Fock-Parität** (k270 B): |J − (−1)^N| = 5·10⁻¹⁶. Der r42-Projektor C = ½(1 + J) wählt also die geraden
  Leitersektoren aus.
- **Leiterzahl je Stufe:** N_c = 0, 1, 3, 3, 4 für n = 1…5. Der Wert 3 ergibt sich bei HS(3) zum ersten Mal, bei HS(4) erneut,
  dort aber mit einer überzähligen Achse und mit Lecks.
- **Anomalien im Turm-Modell** (Sektoren k/N_c, Vielfachheit (N_c über k), gerade Sektoren links; exakt in sympy, Wolfram
  unabhängig gleich):

| N_c | Stufe | Tr Y³ | SU(2)²U(1) | Dubletts | nur Singuletts/Fundamentale |
|---|---|---|---|---|---|
| 0 | HS(1) | 0 | 0 | 1 (ungerade: Witten-Anomalie) | ja |
| 1 | HS(2) | **3/4** | **−1/2** | 1 (ungerade) | ja |
| 2 | (kommt im Turm nicht vor) | 0 | 0 | 2 | ja |
| **3** | **HS(3)** | **0** | **0** | **4** | **ja** |
| 4, 5, 7 | HS(5), … | 0 | 0 | 8, 16, 64 | nein (6, 10, 21, 35 …) |

  Anomaliefrei mit reinen Singulett- und Fundamentaldarstellungen sind nur N_c = 2 und 3. Der Turm bietet N_c = 0, 1, 3, 4, …,
  und beides zusammen gilt **nur für N_c = 3**. Gegenprobe mit der SM-Formel für N_c Farben, Q_u = ½ + 1/(2N_c), gegen die Turm-Ladung
  Q_u = (N_c − 1)/N_c: einzige Lösung N_c = 3 (sympy und Wolfram).
- **Lesart:** Drei Farben sind keine freie Zahl. Sie sind die einzige Leiterzahl, bei der die Stufenleiter des Turms ein
  quantenkonsistentes Teilchenspektrum ohne exotische Multipletts trägt. Das verlangt eine normierte Divisionsalgebra der
  Dimension 8. Unter den Annahmen von r43 (schwache SU(2) auf ℍ, Q_em = T₃ + Q + s) ist HS(3) damit die Stufe, auf der der
  Aufbau anhalten **kann**.

### 2. HS(2): warum der Turm dort nicht anhalten kann (k270 C, E)
- HS(2) liefert genau eine Leiter, also Spin ½ und Dubletts mit T₃ = ±½. Allein ist diese Stufe aber anomal (Tr Y³ = 3/4,
  SU(2)²U(1) = −1/2, ein einzelnes Dublett). Ein Leptonenspektrum ohne Quarks ist inkonsistent, deshalb **muss** es eine Stufe mit
  Farbe geben. Das ist ein Grund, warum der Turm über HS(2) hinaus muss, und zwar genau bis HS(3).
- Links- und Rechtsmultiplikation geben zwei vertauschende SU(2) ([L_a, R_b] = 0). Automorphismen erhalten die Seite
  (φL_aφ⁻¹ = L_φ(a), Abweichung 3·10⁻¹⁶). Erst die Anti-Automorphie (Konjugation) tauscht die Seiten (K L_a K = −R_a). Die Wahl der
  Seite ist damit ein **echtes Bit**. Die Achse dagegen ist Konvention.

### 3. HS(1): Wohin wandert der Drehsinn? (k270 D, E)
- Auf ℂ ist u ↦ −u nur durch die Konjugation erreichbar (det −1). Dort ist der Drehsinn ein echtes Bit (k250).
- In ℍ dreht die innere Drehung exp(θj) für θ = 0 … π/2 die Einheit i stetig in −i. In 𝕆 leistet das der Automorphismus
  (a, b) ↦ (a, −b) mit e₇ ↦ −e₇, und G₂ ist zusammenhängend. **Ab HS(2) ist der Drehsinn also Konvention.** Als physikalisches Bit
  bleibt nur links/rechts übrig, und das legt r43 durch die Anomalien fest, bis auf den Frame-Spiegel T. Damit verschiebt sich die
  offene Frage „wer wählt den Drehsinn“ (k246, k250): Oben muss niemand ihn wählen. Übrig bleibt nur die Frage, ob M oder sein
  T-Spiegel realisiert ist.
- Der Projektor C = ½(1 + iL_u), eingeschränkt auf span(1, u), ist exakt der Projektor der HS(1)-Ebene auf **einen Kreisanteil**
  (Abweichung 0). Für die Ellipse a e^{iωt} + b e^{−iωt} ist die Ladung a² − b² die halbe Gewichtsdifferenz der beiden Bilder. Eine
  Generation (Bild von C) ist der reine Kreis b = 0. HS(0) mit a = b hat in beiden Bildern gleiches Gewicht.

### 4. HS(0): was das Ursprungsfeld sein muss
- **Schwingung, nicht Wachstum** (Teil 2 unten): Nur dann gibt es kompakte Gruppen und keine Lecks bis HS(3).
- **a = b:** HS(0) ist die gleich gewichtete Summe beider C-Bilder, also Teilchen- und Antiteilchenbild zu gleichen Teilen. Das
  passt zu k253: zeitumkehr- und hier auch ladungssymmetrisch.
- **Reelle Eins als Bezug:** Der Koide-Zustand exp(uπ/4) = (1 + u)/√2 (k255) und der Projektor ½(1 + iu) gewichten die HS(0)-Richtung
  1 und die HS(1)-Richtung u gleich. Beide oberen Strukturen setzen also eine gemeinsame reelle Eins voraus. Das ist Lesart.
- **Frei:** Amplitude, Frequenz und Phase. Die Regel ist linear und das Produkt homogen (|(λx)(λy) − λ²xy| ≤ 4·10⁻¹⁵). Keine
  Strukturgröße oben hängt davon ab, passend zu k251 (Skala frei).

## Teil 2: Das Ursprungsfeld variieren (k272)
Die HS(0)-Gleichung ψ̈ = g ω² ψ bestimmt, was die neue Einheit des ersten Shifts quadriert: ℓ² = g. g = −1 ist die Schwingung
(cos ωt), g = 0 die Drift (konstant oder linear), g = +1 das Wachstum (cosh ωt) (Wolfram, k271). Verallgemeinert auf jeden Shift
heißt das (a, b)(c, d) = (ac + g d*b, da + bc*). Gerechnet wurden alle 27 Muster (g₁, g₂, g₃) ∈ {−1, 0, +1}³ für die Stufe 8:

| Klasse | Muster | Nullteiler | Der | Stab(e₇) | Lesart |
|---|---|---|---|---|---|
| Standard | (−,−,−) | nein | 14, kompakt (G₂) | 8, kompakt (SU(3)) | Farbe, keine Lecks |
| gespalten | jedes Muster mit +1 und ohne 0 (7 Muster) | ja | 14, Spurform (6−, 8+): gespaltene G₂ | 8, (3−, 5+) = sl(3,ℝ) oder (4−, 4+) = su(2,1) | nicht kompakt, keine Farbe |
| entartet | jedes Muster mit 0 (19 Muster) | ja (nilpotent) | 15 bis 21, nicht halbeinfach | 11 bis 20, nicht halbeinfach | keine Gruppe im üblichen Sinn |

- **Ein einziges Muster trägt.** Schon ein einziger wachsender oder driftender Shift macht die ganze Stufe gespalten bzw.
  entartet. Die Variation des Ursprungsfelds allein, (+1, −1, −1), gibt gespaltene Oktonionen: Die HS(1)-Einheit quadriert zu +1,
  (1 + ℓ)(1 − ℓ) = 0 ist ein Leck schon bei HS(1), und statt SU(3) bleibt sl(3,ℝ). **Rückwärts gelesen:** Jeder Shift muss eine
  *schwingende* Richtung hinzufügen, nicht nur der erste. Das HS(0)-Vorzeichen ist eine notwendige, aber keine hinreichende Bedingung.
- **Frame-Lesart (nicht gerechnet):** ψ̈ = +ω²ψ ist die HS(0)-Gleichung unter ω ↦ iω, also in der Tachyon-Lesart (z ↦ iz). Ein Turm
  auf einem T-gelesenen Ursprungsfeld wäre gespalten: Lorentz-Boosts statt Drehungen (gespaltene komplexe Zahlen), nicht-kompakte
  „Farbe“. Das passt zum Bild, dass Farbe und Ladung M-Größen sind. Für einen echten Vergleich fehlt die deklarierte Transportregel
  zwischen den Frames (Konvention F).
- **Was die Variation nicht ändert:** Amplitude, Frequenz und Phase (siehe oben) sowie die Zahl der Dimensionen (Der bleibt 14 auch
  im gespaltenen Fall). Es ändert sich die *Signatur*, also die Frage, ob die Bahnen geschlossen bleiben.

## Bilanz: erzwungen, Konvention, gesetzt
- **Erzwungen (unter den Annahmen unten):** Schwingung auf jeder Stufe (g = −1), eine feste Einheit in 𝕆, N_c = 3 und damit 𝕆 als
  Farbstufe, Spin ½ bei HS(2), s = −½ und Linksmultiplikation (r43), die Zerlegung von HS(1) in zwei Kreisanteile.
- **Bloße Konvention:** die Richtung von u in 𝕆, die Achse bei HS(2), der Drehsinn ab HS(2), Amplitude, Frequenz und Phase.
- **Weiterhin gesetzt:** der Rahmen von r43 (schwache SU(2) auf ℍ, Q_em = T₃ + Q + s, Projektor auf ℂ⊗𝕆), der Frame-Spiegel (M
  gegen T) und die Zuordnung Kanal = reelle Trägerdimension (k253). Offen bleiben auch Massen, δ von Koide und die Zahl der
  Generationen (k255/k256).

## Grenzen
- Nicht blind: Jedes Einzelergebnis ist Lehrbuchmathematik. Neu ist die Verkettung im Turm. Dass die Anomalien N_c = 3 wählen, gilt
  im Turm-Modell (Ladung k/N_c, gerade Sektoren links), das für N_c ≠ 3 eine Extrapolation der r43-Struktur ist und kein
  gerechneter Turm.
- „HS(2) kann nicht die letzte Stufe sein“ ist ein Konsistenzargument (Anomalie), keine Dynamik.
- Die Variation betrifft nur das Vorzeichen der Verdopplung. Nichtlineare oder gedämpfte Ursprungsfelder sind nicht gerechnet.
- OP1, OP3, OP5 offen; kein Guard berührt; H125/H126 unberührt.

## Mögliche nächste Schritte
- **Nichtlineares HS(0)** (z. B. Duffing-Term): ändert eine amplitudenabhängige Frequenz etwas oben, oder bleibt alles skalenfrei?
- **Rückwärts über HS(3) hinaus:** Welche Konfiguration bei HS(4)/HS(5) verlangt die Generationenzahl 3? Dort wiederholt sich
  N_c = 3 (k270 B), und k255 lieferte das Kopien-Etikett.
- Blinder Test erst mit einer Größe, die hier nicht schon feststeht (Vorab-Notiz nötig).

## Dateien
`k270_rueckwaerts.py` (`k270_out.txt`), `k271_anomalien.wl` (`k271_out.txt`, Wolfram-Ausgabe mit Warnungen),
`k272_hs0_variieren.py` (`k272_out.txt`).
