# Offene Probleme und wo die Arbeit festsitzt

**Stand: 6. November 2026, nach v4.10.0-r05.** Diese Seite beschreibt, was offen ist, warum, und was der nächste sinnvolle Schritt wäre. [Inhaltsübersicht](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Inhalt) · [Forschungslinie](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Forschungslinie) · [GitHub Issues](https://github.com/Moriarty1982/QuantumSphere-Unfold/issues)

## Der gemeinsame Kern: Es fehlt eine Dynamik

Fast alle offenen Punkte hängen an derselben Lücke: Es gibt keine gemeinsame, in allen Feldern variierte Wirkung, aus der die Größen folgen. Bisher werden sie gesetzt. Aus den Ergebnissen der Runden ergibt sich ziemlich genau, was eine solche Dynamik leisten müsste:

1. **Eine Wirkung für alle Felder.** Coframe, Verbindung und Materie müssen eigene, rückwirkende Felder sein. Eine nur aus den Sonden zusammengesetzte Geometrie wird flach (r69).
2. **Materie und Tachyon mit demselben Lichtkegel.** Beide brauchen denselben kinetischen Term. Die Abbildung $z \mapsto iz$ muss eine Symmetrie der Wirkung sein.
3. **Der Kompensator als Kopplung**, nicht als nachträglicher Projektor.
4. **$\Lambda$ als Integrationskonstante** (unimodular oder sequestrierend). Zustand, Frame und Normierung legen den absoluten Vakuumterm nie fest (r69).
5. **Ein Randterm, der nur eine U(1) zählt.** Die innere Einheit $J = L_{e_7}$ wählt in $SU(2)$ genau eine U(1) aus. Das könnte die Zählregel hinter $\beta_{\mathrm{sym}}$ begründen (Vermutung).
6. **Triality als Symmetrie der Kinetik**, gebrochen durch die Chiralität.
7. **Eine Uhr aus der Phasendifferenz** zwischen Materie und Tachyon; ein gemeinsamer Energieversatz ist nicht beobachtbar.

Ein erster Test dieser Skizze (H48) zeigt eine Grenze: In der einfachsten Reduktion folgt $\beta_{\mathrm{sym}}$ nicht aus der Dynamik, weil ein eingefrorener Wert immer die Expansionsgeschichte mitträgt. Ein dimensionsloser Strukturwert müsste aus einem dimensionslosen Verhältnis kommen, zum Beispiel aus zwei Zählungen (r63) oder einem Winkel je Ereignis (r27: 28,78° statt 30°).

## OP1: Woher kommt $\beta_{\mathrm{sym}}$?

$\beta_{\mathrm{sym}} \approx 0{,}549$ wird aus zwei veröffentlichten Barbero–Immirzi-Werten gebildet und eingesetzt. Die Zähl-Lesart (r63) liest es als Verhältnis einer Minimal-Spin-Zählung (Tachyon) zu einer Voll-Spin-Zählung (Materie). Sie trifft das aus der Leptonmischung gewonnene Fenster. Allerdings nur mit der U(1)-Behandlung der Horizontzustände; die besser begründete SU(2)-Behandlung gibt 0,604 (r68).

**Offen:** warum die Frames gerade diese Zählregeln wählen. **Nächster Schritt:** die U(1)-Auswahl aus der inneren Einheit $J$ herleiten oder ausschließen.

## OP2: Dirac-Operator auf dem antisymmetrischen Sektor

Die alte Fassung markiert Existenz und Selbstadjungiertheit von $`D_- = L_0\vert_{H^+_-}`$ als geschlossen. Beide Beweise stützen sich aber auf die Riemann-Arbeit, die seit v4.8.0-r04 keine Beweisquelle mehr ist. Der letzte Schritt, den Versatz aus dem Spektrum abzulesen, ist dasselbe Problem wie OP1.

## OP3: Zulässige Hüllen-Übergänge

In der QAM als lokales Schließungszertifikat formuliert und im Kristallbild als Verträglichkeit benachbarter Zellen gelesen. Für die aktive Schließungsphase reicht das nach dem Text nicht mehr; eine lokale Persistenzkorrektur wird verlangt.

## OP4: Herkunft der Mischungswinkel

Mehrere Konstruktionen treffen die Mischungsdaten, aber als Anpassung (r54, r56). Die Lesart je Teilchenart (r55) mit Maskenkorrektur (r57) passt und liefert die offenen Vorhersagen H42 und H46. Nach r61 war OP4 in der alten Form falsch gestellt, weil es Frames vermischt.

## OP5: kosmologische Konstante und Vakuumbilanz

**Erste analytische Erkundung zur Zustandsauswahl (6.11., nicht blind):** Im minimalen Feld-/Gram-Modell existiert bei fester Normierung, Orientierung und positivem Sektor eine ganze Familie mit beliebigem Eigenwertverhältnis 0 < q < 1. Dieselbe Projektoralgebra wählt den H96-Wert daher nicht aus. Selbst ein festes Register benötigt eine unabhängig begründete Energiezuordnung: Bei positiven Gewichten ist der Minusanteil w₋q/(w₊+w₋q), nicht automatisch q. Das sind Gegenbeispiele zur Hinlänglichkeit der Minimaldaten, kein Unmöglichkeitssatz für jedes zusätzliche physikalische Gesetz. [Explizite Zustände, Beweise und Grenzen](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/op5_state_selection_exploration_2026_11_06.md).

**Gesamturteil der Rückverfolgung (Arbeitsnotiz, 6.11.):** Die historische Λ-Auslöschungspflicht war keine etablierte Konsequenz des Kerns. Lokale Projektor-/Feldauslesungen und bedingte Erhaltungssätze bleiben davon getrennt. Die kosmologische Restbehauptung ist die zusätzliche Identifikation q = Ω_M(heute), wie in H96 registriert; Kaskade und Zählumformung liefern dafür keinen unabhängigen zweiten Nachweis. Die neu aufgebaute Frage verlangt eine unabhängig definierte Messgröße, eine explizite Ausleseabbildung und eine nicht schon vorausgesetzte Zustandsauswahl. Die unmittelbare Quellenrekonstruktion ist damit vorläufig abgeschlossen; eine neue physikalische Herleitung wäre ein eigener nächster Schritt. [Gesamturteil und Index der sechs Arbeitsnotizen](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/op5_reconstruction_verdict_2026_11_06.md).

**Arbeitsentscheidung vom 6.11.2026 nach r05: die ursprüngliche Begründung aussetzen.** Die historische Auslöschungsfrage setzte voraus, dass spektrale Terme einen physikalischen, riesigen Λ-Beitrag erzeugen. Die dafür verwendete metrische Wirkung ist nicht definiert; auch die Skala des nackten Terms ist nicht hergeleitet (v4.8.0-r04/r05). Einzelne Annahmen sind widerlegt oder zurückgezogen, andere unbegründet. Das ist keine pauschale Widerlegung jeder möglichen physikalischen Auslesung.

Die neue Arbeitsfrage lautet: **Welche unabhängig definierte physikalische Messgröße lässt sich durch eine explizite, begründete Auslesung aus dem algebraischen Kern gewinnen, und welche überprüfbare Einschränkung folgt daraus?** Weder ein auszulöschender Vakuumterm noch dessen Restwert werden vorausgesetzt. Zuerst wird für eine vorhandene Quelle–Rückweg-Route das Wörterbuch aus Träger, Transport, Auslesung und Invariante rekonstruiert. Der bedingte Schließungssatz ersetzt dabei nicht den Nachweis seiner Voraussetzungen oder einer physikalischen Brücke. [Begründung, Quellen und Arbeitsauftrag](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/op5_neuaufbau_2026_11_06.md).

Die folgende r05-Trennung bleibt als dokumentierter Stand erhalten: H96 ist offen, H97 widerlegt und W1/W2 eingefroren. Diese neue Arbeitsnotiz ist noch keine nummerierte Forschungsschicht; OP5 wird nicht als insgesamt geschlossen dargestellt.

**Erster Rekonstruktionsbefund (Arbeitsnotiz, 6.11.):** Das Quelle–Rückweg-Paket in den Teilen 21/22 ist ein bedingtes Schema. Klassenerhaltung und Readout-Faktorisierung werden vorausgesetzt; eine konkrete native Route ist in der untersuchten Verweiskette noch nicht instanziiert. Die zwei gerichteten Auslesungen starten formal am selben Quellzustand, nicht an den beiden Enden eines berechneten Hin-und-zurück-Durchlaufs. QAM-Brücken bleiben an ihre ausdrücklich genannten Voraussetzungen gebunden. Das widerlegt den bedingten Satz nicht, lokalisiert aber die fehlende Realisierung. Nächster Ansatzpunkt ist das bereits explizite Feld-/Gram-Wörterbuch einschließlich Orientierung und Skala, ohne ihm vorab kosmologische Bedeutung zuzuschreiben. [Datenblatt und Prüfgrenzen](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/op5_route_inventory_2026_11_06.md).

**Konkretes Auslese-Datenblatt (Arbeitsnotiz, 6.11.):** Das reale Feld-Doppel F = [E|B] liefert mit G = FᵀF und ρ = G/tr G die normierten Projektorportanteile p₊ = 1/2 + (E·B)/tr G und p₋ = 1−p₊. Absolute Portgrößen benötigen die Skala, allgemeine gerichtete Beobachterwechsel zusätzlich die räumliche Orientierung. Ein nichtverschwindendes nulles elektromagnetisches Feld hat ρ = I/2 und gleiche Portanteile; ein reiner Kompensatorport hat dagegen ρ = C₊. Keines dieser Register ist das vollständige Nullfeld. Diese bereits vorhandenen Formeln präzisieren einen lokalen Auslesekandidaten, keinen Vakuumterm und noch keine native OP-Route. Apparatur/Kalibrierung und die Unterscheidung aktiver Operation, passiven Beobachterwechsels und Messselektion bleiben ausdrücklich zu prüfen. [Feld-/Port-Datenblatt](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/op5_field_readout_inventory_2026_11_06.md).

**Operative Klärung (Arbeitsnotiz, 6.11.):** Die Einzelportprojektion ist keine invertierbare passive Frameumrechnung. Spiegelung J_B, korrigierte Tachyon-Dualitätsdrehung z ↦ iz, Zeitumkehr und gewöhnlicher Beobachterboost bleiben verschiedene Operationen (r02–r04, Korrekturen r28/r51). Portwerte vergleichen Zustand und Analysator gemeinsam; bei einer bloßen orthogonalen internen Basisumrechnung müssen beide mittransformiert werden. Die r03-Referenzphase gehört zum Aufbau und bestimmt nicht von selbst β_sym. Die nächste offene Verbindung ist die Zuordnung des feldabhängigen Rapiditäts-/Sichtbarkeitsparameters zum projektweiten symmetrischen Frame-Versatz. [Operations-Datenblatt](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/op5_operations_inventory_2026_11_06.md).

**Frame-/Parameterprüfung (Arbeitsnotiz, 6.11.):** r24 löst die zunächst anhand von r17 offene Referenzbenennung auf: Der alte „Photon-Frame“ ist R (reines Register), während P das lichtartige Register I/2 bezeichnet. Ein endlicher γ_L vergleicht in dieser Lesart M mit R. r17 liefert β² als Eigenwertverhältnis λ₋/λ₊; der kleinere normierte Eigenanteil ist dagegen β²/(1+β²), und ein fester Messport liest diese Eigenwerte nur bei passender Ausrichtung. Die Auswahl eines konkreten Feldzustands mit η_f = η_sym und die Gleichsetzung des Verhältnisses mit Ω_M bleiben zusätzliche Verpflichtungen. [Quellen und genaue Typentrennung](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/op5_frame_identification_2026_11_06.md).

**Nennerprüfung (Arbeitsnotiz, 6.11.):** Register-Eigenwertverhältnis, bedingter Ausflussanteil aus S8, Kontrast zweier γ-Parameter und Materiedichte relativ zur kritischen Dichte haben verschiedene Bezugsgrößen. r31 setzt β² als Verzweigung ein und zeigt im Modell dessen stationäre Flussstabilität; es leitet β² nicht unabhängig her. r63/r67 verwenden Lösungen verschiedener Zählgleichungen, keine bereits gemeinsam gezählten Materie-/Vakuumzustände. Die verbleibende Gleichsetzung mit Ω_M(heute) ist deshalb eine zusätzliche physikalische Hypothese, wie in H96 registriert. [Nennerprüfung und präzisierte Abhängigkeiten](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/op5_denominator_audit_2026_11_06.md).

**Neuordnung (v4.10.0-r05, Autorentscheidung):** OP5 hat drei Teile.

1. *OP5-Kern:* Umkehr-Schließung I(OP1) = I(OP5_sym), lokal geschlossen.
2. *Λ-Auslesung:* Ω_Λ : Ω_M = (1 − β²) : β² als Verzweigung der Kaskade, Epoche heute. Daraus die Vorhersage H96 (Ω_M = 0,30185, offen); die einfachste Dynamik dafür ist widerlegt (H97).
3. *Dynamik-Programm W1/W2:* eingefroren.

Der folgende Text beschreibt den Stand des Dynamik-Zweigs bis v4.10.0-r04.

Lokal ist OP5 über eine Detektorschwelle geschlossen ($\mathrm{OP5}_{\mathrm{eff}}$). Exakt ist es offen. Der Stand nach r69 bis r86:
- **Frame-Wechsel:** Ein passiver Frame-Wechsel beseitigt keinen Bilanzfehler.
- **Neutralität:** „Neutral“ hat drei verschiedene Bedeutungen, und keine davon legt den Vakuumterm fest.
- **Lichtkegel:** Der Kegel kommt aus der Clifford-Struktur. Kegeldaten legen weder eine absolute Skala noch das Gewicht eines Vakuumterms fest.
- **Rekonstruierte Geometrie:** Zwei komplexe Sonden geben eine vierdimensionale Geometrie, lösen aber ihre eigenen Gleichungen nicht.
- **Numerik:** Die numerische Verträglichkeit reicht bis zur vierten Ableitungsordnung an drei Punkten. Das ist keine Lösung auf einem Gebiet. Am Punkt (1, 3/5, 0, 0) gibt es einen 70-stelligen Keim bis zur fünften Ordnung, unabhängig bestätigt (r71).
- **Eichfreiheit im Vergleichssystem (r71):** Das System lässt eine Funktion von vier Variablen frei, nämlich Verschiebungen entlang des Polarwinkels $\vartheta$. Das ist eine exakte Symmetrie des gewählten Hintergrunds. Die Zusatzbedingung $\Omega$ ist eichinvariant und legt sie nicht fest (H50). Solange diese Freiheit nicht geeicht ist, ist die Frage nach weiteren versteckten Bedingungen nicht sauber gestellt.

- **Eichung und Vollständigkeit (r72):** Die $\vartheta$-Freiheit ist durch eine Bedingung an eine Stromkomponente geeicht. Das geeichte Symbol ist ab Ordnung 6 involutiv (H51 bestätigt). Beim Fortsetzen der Taylorreihe treten aber nach allem Anschein vier weitere Bedingungen an die sechsten Ableitungen auf; die Spencer-Kohomologie lässt genau vier zu. Formal bestätigt ist das nicht (H52 bis H54 ungültig). Solange diese vier nicht bestimmt sind, ist das System nicht vollständig und kein Existenzsatz nach Cartan–Kähler möglich.

- **Vier zusätzliche Bedingungen (r73):** an einem zweiten Punkt bestätigt (H55) und bestimmt: Gleichungen sechster Ordnung, die nur lichtartige Wellen betreffen, die Reste der Beziehungen $q\,d_k\,\Omega$. Mit ihnen ist das Symbol bei Ordnung 6 nicht involutiv; ob es bei 7 oder 8 involutiv wird, ist mit der vorhandenen Genauigkeit nicht entscheidbar (H56, H57 ungültig).

- **Genauigkeitsgrenze (r74):** Mit konsistenten Daten wird das erweiterte Symbol nach allem Anschein erst bei Ordnung 8 involutiv. Weitere versteckte Bedingungen (bis zu vier an siebten, drei an achten Ableitungen) sind nicht ausgeschlossen. Die Entscheidung scheitert an einer strukturellen Genauigkeitsgrenze: $\Omega$ und die vier Bedingungen sind fast Folgen der Grundgleichungen.

- **Hohe Genauigkeit (r77):**
  - Keine weiteren versteckten Bedingungen (H59): Das erweiterte System ist am Keim formal integrabel und trägt 6 masselose Moden (H60).
  - Die Konstruktion R ist kovariant (H64). Lorentz-Symmetrie fehlt nur, weil der Hintergrund fest ist (H62, H63). Welchen Spin die Moden tragen, ist offen (H61 widerlegt).

- **Kovarianz (r78):** R und Ω sind kovariant (H66). Die Eichung zeichnet die y-Richtung aus, nur so(1,2) bleibt erhalten (H65(b)).

- **Eichunabhängigkeit (r79):** Die vier Bedingungen sind in fünf Eichungen gleich, auch in der kovarianten Ψ̄Ψ (H67).

- **Urknall-Übergang (v4.10.0-r02, r03):** Asymptotik hergeleitet (H93); Fermionen ohne Beimischung, CPT exakt; Bosonen-Norm nur außerhalb k ~ 1/Δ erhalten (H94); Δ ≲ Planck-Länge (Autorentscheidung); Drehsinne exakt konjugiert. Offen: die gesamte erzeugte Bosonen-Energie (hängt am Planck-Bereich).
- **Λ unter G2 (v4.10.0-r03):** Kein Mechanismus aus dem Tachyon-Sektor (Mischung, tachyonische Kondensation, Geist-Kondensat) gibt nach dem Urknall einen Vakuumterm; Λ = a·V_min ist frei. G1 hilft nicht (r04), und I3 ist auch mit zugelassenem Tachyon-Zweig gescheitert (feste Gewichte: CMB; dynamisches Zweig-Gas: H95). Λ ist eine Eingabe; offen ist, ob es überhaupt aus der Struktur folgen kann.
- **Einstein-Gleichung von W1 (v4.10.0-r01):** voll nichtlinear hergeleitet und verträglich (H90); das Vorzeichen der Gravitationswirkung ist korrigiert (−R/2κ, Autorentscheidung). Damit ist der homogene Fermionzustand steif mit ρ = p < 0 und der Torsions-Paarkanal abstoßend. Offen: die Skala von Λ.
- **Prüfung mit Wolfram (r86):** Die Urknall-Zahlen von r85 und die Feldgleichungen von W1 sind von einem zweiten System bestätigt bzw. aus den Definitionen hergeleitet (H87–H89). Der homogene Zustand der Fermionen ist steife Materie (ρ = p > 0), kein Vakuumterm. Offen: die volle nichtlineare Einstein-Gleichung und die Bianchi-Identität von W1, ein vorab festgelegter Test des Abfalls e^{−πkΔ} mit Potenzvorfaktor, weiter die Dauer Δ und die Skala von Λ.
- **Massen und Urknall (r85):** Massen tragen unter der zweiten Lesart; die Gewichte aus r19 werden für die Eichkopplungen getroffen, für die Gravitation nicht. Mit dem Tachyon-Anteil vor dem Urknall (G2) ist der Urknall ein CPT-artiger Übergang mit einer durch β_sym festgelegten Beimischung. Offen: die Dauer Δ des Übergangs, die Bedeutung der Asymmetrie der Drehsinne, die Übergangsbedingung für Fermionen, das F3-Gewicht der Fermion-Kinetik (Arbeitsannahme 1) und weiter die Skala von Λ.
- **T-Anteil als zweite Lesart (r84):** Als dasselbe Feld in zweiter Lesart, mit vollständigem komplexem Boost und holomorpher Adjungierter, ist der Tachyon-Anteil isotrop und stabil, ohne Zerfall (H79). Im flachen Raum normiert er nur die Kinetik um; Λ wird nicht aufgehoben. Offen: ob der Versatz δ ≠ 0 mit seiner Epoche τ* physikalisch gewollt ist, ob die Modenauswahl beobachtbare Folgen hat, und die Skala.
- **Vakuumzerfall und Lesart des Tachyonbilds (r83):** Ohne ausgezeichneten Rahmen zerfällt das Vakuum über die Gravitation unbeschränkt (H76); die Daten verlangen eine Grenze ≲ 14 MeV in einem solchen Rahmen. Das Tachyonbild einer Wirkung ist mit fortgesetzter Kinematik zu bilden (H77); damit ist die Aufhebung der Higgs-Vakuumenergie aus r82 zurückgezogen. Eine Geist-Kondensation könnte Rahmen und Stabilität liefern. Offen: ob die Struktur den Term cX² und eine Skala festlegt, und das Λ-Problem von 10⁵⁵.
- **Higgs-Sektor und Stabilität (r82):** Mit dem Tachyonbild schien sich die Higgs-Vakuumenergie bei Photon-Gewichten exakt aufzuheben (in r83 zurückgezogen). Bei direkter Kopplung der Sektoren ist das instabil (H74); bei reiner Gravitation gibt es keine exponentielle Instabilität, aber gemeinsames Durchgehen (H75). Der Torsions-Paarkanal kondensiert nur an der Planck-Skala. Offen damals: der Quanten-Zerfall (in r83 behandelt), die Skala, ein zusammengesetztes Higgs.
- **Gemeinsame Wirkung (r81):** W1 erzeugt allein keinen Vakuumterm. Ein Λ-artiger Term entsteht aus tachyonischen Moden beider Normvorzeichen, die Struktur legt seine Größe aber nicht fest. Offen: Higgs-Sektor in W1, die Skala (Masse des Tachyon-Partners, Stringspannung), Rückwirkung auf die Expansion.
- **Hintergrund (r80):** A, h werden nicht von den Spinorblöcken erzeugt, weder über Yang–Mills noch über Klein–Gordon (H68 widerlegt). Der Vergleichsmodell-Zweig ist damit abgeschlossen (Autorentscheidung); Feinheiten wie die Lorentz-Wirkung auf die 6 Moden werden ohne eigene Dynamik nicht weiter verfolgt.

**Nächster Schritt** (r80): eine Ebene höher. Zuerst eine Bestandsaufnahme der bisherigen Wirkungsansätze (woran jeder gescheitert ist) und der Mindestanforderungen an eine gemeinsame Wirkung für Spinoren, Verbindung, Skalar und Koframe; diese gemeinsame Dynamik fehlt OP1 bis OP5 gleichermaßen. Die [Bestandsaufnahme](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/v4_10_0_w1/Bestandsaufnahme_Wirkungsansaetze.md) sammelt rund ein Dutzend bisherige Ansätze. Fast alle scheitern an einer von fünf Stellen: Ein Teil der Felder wird festgehalten statt variiert; das Wörterbuch von den Spinoren zum Koframe (Spurhindernis, Rangschranke, Flachheit, Bruch der Stromerhaltung); endliche Strafen statt exakter Bedingungen; ungeklärte Stationarität (reell oder komplex, welche Adjungierte); Quellen, die nicht in der Eichalgebra liegen. Daraus folgen acht Mindestanforderungen an eine Wirkung, unter anderem alle Felder unabhängig variiert, Schließung als exakte Bedingung, ein gemeinsamer Lichtkegel und ein nicht freier Vakuumterm. Vor jeder Rechnung muss der Autor fünf Fragen entscheiden: Koframe als eigenes Feld oder als Funktion der Spinoren, reelle oder komplexe Wirkung, Gravitationsterm, Eichgruppe, und ob P_C7 exakt gesetzt oder dynamisch ausgewählt wird. Die Literaturnotiz der OP5-Serie gibt dafür die Reihenfolge vor:
1. polare Spinorvariablen (Fabbri) und Fierz-Rekonstruktion,
2. Nebenbedingungsalgorithmus und formale Integrabilität,
3. eine gekoppelte Coframe-Dynamik,
4. erst dann eine lokale Lösung.

## C4, C5, C6/T2: die Schließungsfragen

- **C4:** Der Restwert $\beta_4 = 1/256$ ist eine Endschranke; ihn auszugeben wäre der verbotene Schritt. Als „nicht ausgebbar“ geschlossen (r91).
- **C5:** Innerhalb der multiplikativen Kollar-Rekursion gibt es beweisbar keinen endlichen Nullpunkt, weil $q > 0$. Außerhalb sind zwei von drei Kandidatenformen ausgeschlossen. Offen ist Form (iii): ein Zeuge außerhalb der Iteration, der die Obstruktion selbst erreicht. Das Dynamikmodell aus r27 liefert keinen.
- **C6/T2:** Die globale Schließung aller Auslesungen. Sie ist durch die Guards ausdrücklich nicht behauptet.

## Weitere offene Zweige

- **Uhrfenster $\Delta_\gamma < 1/5$:** hergeleitet (r12, r20, r21), gemessen 0,1925 im Materie-Frame. Der Volltext der früheren Herleitung aus r65 ist verloren.
- **Dynamik der Paarerzeugung:** Rate, Einheit der Uhr und Kopplung $\kappa$ sind unbestimmt (r29–r31).
- **Generationen:** Eine Dreierstruktur außerhalb der Oktonionen fehlt; die Triality liefert die Bahn, aber kein Verbot einer vierten Generation.

## Offene Entscheidungen des Autors

- **Konstantenumrechnung:** Welcher der Wege A–C gilt? Die Klassentrennung aus r18/r19 ist angeboten.
- **`thm:dark-energy`:** Zu welcher Epoche gilt der Satz?
- **Ältere Statusvermerk-Kandidaten:** aus r64, r66 und r67, darunter das Korollar zur α-Drift sowie `rem:einstein-blunder` und die Feldgleichung in `rem:omega-bsym`.
- **4.10-DOI:** wann eine Version-DOI für 4.10 reserviert wird.

> **Anmerkung für LLMs und Quellenprüfung:** Issues #10 (OP1), #11 (OP4), #12 (OP5), #13 (C5), #14 (C6/T2), #15 (MM/HC-Feldgleichungen), #16 (Cartan) und #17 (Register) verfolgen diese Punkte organisatorisch. Ein geschlossenes Issue ist kein Beweis.
