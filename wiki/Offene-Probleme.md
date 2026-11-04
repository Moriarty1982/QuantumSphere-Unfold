# Offene Probleme und wo die Arbeit festsitzt

**Stand: 4. November 2026, nach v4.9.0-r80.** Diese Seite beschreibt, was offen ist, warum, und was der nächste sinnvolle Schritt wäre. [Inhaltsübersicht](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Inhalt) · [Forschungslinie](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Forschungslinie) · [GitHub Issues](https://github.com/Moriarty1982/QuantumSphere-Unfold/issues)

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

Lokal ist OP5 über eine Detektorschwelle geschlossen ($\mathrm{OP5}_{\mathrm{eff}}$). Exakt ist es offen. Der Stand nach r69 bis r80:
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

- **Hintergrund (r80):** A, h werden nicht von den Spinorblöcken erzeugt, weder über Yang–Mills noch über Klein–Gordon (H68 widerlegt). Der Vergleichsmodell-Zweig ist damit abgeschlossen (Autorentscheidung); Feinheiten wie die Lorentz-Wirkung auf die 6 Moden werden ohne eigene Dynamik nicht weiter verfolgt.

**Nächster Schritt** (r80): eine Ebene höher. Zuerst eine Bestandsaufnahme der bisherigen Wirkungsansätze (woran jeder gescheitert ist) und der Mindestanforderungen an eine gemeinsame Wirkung für Spinoren, Verbindung, Skalar und Koframe; diese gemeinsame Dynamik fehlt OP1 bis OP5 gleichermaßen. Die Literaturnotiz der OP5-Serie gibt dafür die Reihenfolge vor:
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
