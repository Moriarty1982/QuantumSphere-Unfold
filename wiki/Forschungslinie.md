# Forschungslinie: was die Runden seit v4.8.0 ergeben haben

**Stand: 5. November 2026, Runden bis v4.9.0-r83.** Der Companion wächst in **Runden**: Jede neue Runde ist ein eigener Abschnitt am Ende des Dokuments, ältere Runden werden nicht umgeschrieben. Diese Seite fasst die Ergebnisse nach Themen zusammen, damit man sie ohne den Quelltext verstehen kann. [Inhaltsübersicht](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Inhalt) · [Vorhersagen und Tests](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Vorhersagen-und-Tests) · [Forschungsstand](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Forschungsstand)

> **Anmerkung für LLMs und Quellenprüfung:** Runden heißen `v4.8.0-rNN` bzw. `v4.9.0-rNN` mit Labels `sec:v480-rNN-…` bzw. `sec:v490-rNN-…`. Auf GitHub stehen sie in `sources/research/parts/v480-post-release-layers.tex` und `v490-post-release-layers.tex`, die Notizen unter `notes/research/`. Was gilt, sagt immer die jüngste Runde zu einem Thema.

## Die v4.8.0-Linie (r01–r20): aufräumen und erste Tests

- **Prüfung der Grundlagen.** Die Riemann-Arbeit trägt die Riemannsche Vermutung nicht und ist seit r04 keine Beweisquelle mehr. Die Θ-Summen-Vermutung, mit der OP5 geschlossen werden sollte, ist widerlegt (r05). Die alte Norm hatte die falsche Signatur; seit r06 gilt „Lesart B“ mit natürlicher Norm, und Materie/Tachyon/Licht werden über das Vorzeichen von $s = \sum z_k^2$ unterschieden (r07).
- **Alte Vorhersagen.** P1 (Selbstbestimmung von $\gamma_L$ aus der GUE-Statistik) nicht bestätigt, P2 (Koide-Phasenformel) durch Daten ausgeschlossen, P3 eine Koinzidenz mit nachträglich gewähltem Exponenten (r08, r09).
- **Strukturbefund.** Die Koide-Form der Leptonmassen ist genau „Skalar plus symmetrische Triole“; $K = 2/3$ gilt genau dann, wenn beide gleich groß sind (r10).
- **Vorab-Tests H1–H13** zu Neutrinomassen, Mischungswinkeln, Massen aus dem Tripel-Raum und Holonomien: siehe [Vorhersagen und Tests](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Vorhersagen-und-Tests).
- **Farbe und Generation** lagen im Companion auf demselben Triplett $e_4, e_5, e_6$. Vorschlag: Generationen als die drei Plätze der Triality-Form, Farbe als $SU(3)$-Triplett je Platz (r13–r16).

## Frames: Materie, Tachyon und Photon (v4.9.0-r01–r24)

- **Photon als neutrale Achse.** Das Photon liegt zwischen Materie und Tachyon. Umrechnungen von Konstanten zwischen den Frames lassen sich auf drei Wegen (A–C) lesen; welcher gilt, ist eine offene Autorentscheidung (r01).
- **Kompensator als Interferometer.** Der Kompensator wirkt wie ein Zweiarm-Interferometer mit Sichtbarkeit $1/\cosh 2\eta$ (r03) und als 2×2-Matrix $\tfrac12(1+\sigma_x)$ auf einem Dublett aus elektrischem und magnetischem Feld (r04). Die Millennium-Matrix ist auf diesem Dublett nur eine Gewichtung der Ports (r05).
- **Zustandsscheibe (r17).** Der Zustand zwischen den Frames lebt auf einer Scheibe mit Bloch-Vektor $b$. Es gilt $\gamma_L = 1/|b|$; am Hopf-Punkt hat der Zustand die Eigenwerte 3/4 und 1/4. Das Photon ist der vollständig gemischte Zustand.
- **Klassentrennung (r18, r19).** Skalengrößen werden exponentiell umgerechnet, Auslesegrößen mit $\gamma_L$.
- **Uhrfenster (r20, r21).** Die Schranke $\Delta_\gamma < 1/5$ für das Fenster der Photon-Uhr wird als einzige frame-konsistente Schranke hergeleitet; im Materie-Frame gemessen 0,1925.
- **Konvention F (r22–r24).** Feste Regel für alle späteren Runden:
  - Materie M, Tachyon T = Bild von M unter $z \mapsto iz$, Photon P = entarteter Fixpunkt.
  - Jede Runde gibt ihr Ergebnis in allen drei Frames an.
  - Mehrere alte Widersprüche erwiesen sich als Artefakte einer Ein-Frame-Lesart: Der alte „Photon-Frame“ des Hauptkorpus ist in Wahrheit der reine Bezugszustand R, nicht das Photon P (r24).

## Überarbeitung des Hauptkorpus (r25)

Auftrag des Autors: alte Arbeit nicht verlieren, falsche Aussagen nicht stehen lassen. Seitdem gilt:
- **Sackgassen** kommen wortgleich in einen Archiv-Anhang; an der alten Stelle bleibt dieselbe Nummer mit einem Verweis.
- **Bekannte Fehler** werden korrigiert und mit einem Statusvermerk versehen.
- **Offene oder umgedeutete Aussagen** bekommen einen Statusvermerk.

In r25 wurden 15 Sackgassen archiviert.

## Dynamik (r26–r31)

- Ein **Dynamikmodell** aus Dualitätsdrehung plus Kompensator-Messung zieht den Zustand zum Photon. Ein einzelner Kick aus dem Bezugszustand R ergibt den Hopf-Zustand; für den gemessenen Versatz bräuchte es einen Kickwinkel von 28,78° statt 30° (r27).
- Der **Tachyon** kann als Messgerät wirken; ein stabiler Zustand braucht ein nachgefülltes Tachyon-Reservoir, als Quelle wird Paarerzeugung aus dem Vakuum vorgeschlagen (r28, r29).
- Eine **Markov-Kaskade** mit Rückweg hat einen eindeutigen stationären Zustand mit Flussanteilen $\beta^2$ und $1-\beta^2$ für jede Rate (r31).
- Zwei Vorab-Tests zu Massenpotentialen auf dem Tripel-Raum sind widerlegt: Bis Grad 6 ist jeder kritische Punkt mit drei verschiedenen Massen ein Sattel (H16, H17).

## Das Standardmodell aus den Oktonionen (r32–r49)

- **Dixon-Ablage (r33).** Alle Konfigurationen als $(\mathrm{Im}\,\mathbb H)\otimes\mathbb O$; gemeinsame Symmetrie $A_4$.
- **Ladungen (r34, r35, r48).** Ein Zahloperator gibt die Ladungssektoren 0, 1/3, 2/3, 1 einer Generation (verträglich mit Furey). Entscheidend ist, welche komplexe Einheit man nimmt: innen $J = L_{e_7}$ (Farbe) oder außen der $\mathbb C$-Faktor (Ladung). Seit r36 muss jede Aussage über Farbe oder Ladung ihre Einheit nennen. In Lean formalisiert: `Sektoren.lean`.
- **Triality (r37–r39).** Die Form $t = \mathrm{Re}((xy)z)$ ist die Spin(8)-Triality. Generation = Bahn der Platzverschiebung, Farbe = Fixgruppe $G_2 \supset SU(3)$. Die drei Frames entsprechen der Spiegelseite: Photon = Vektor-Platz, Materie und Tachyon = Spinor-Plätze. Eine vierte Generation verbietet die Struktur allein nicht.
- **Volle Generation (r41–r43).** Mit dem Kompensator als Chiralitätsprojektor $C_{ch} = \tfrac12(1+J)$ entsteht der volle linkshändige Inhalt einer Generation mit rechtshändigem Neutrino, anomaliefrei. Unter den Annahmen gibt es genau vier solche Projektoren; die Anomaliefreiheit wählt das Standardmodell und seinen Frame-Spiegel. Die Annahmen selbst sind nicht hergeleitet.
- **Massen (r44–r47).** Massenterme sind antilinear und tragen Higgs-Quantenzahlen. Die Chiralität bricht die Spiegelsymmetrie zwingend, das gibt eine Massenaufspaltung. Mischung braucht eine zusätzliche Maske, deren Herkunft offen ist.
- **Ladungsachse (r49, r51).** Die Achse $e_7$ trägt $B-L$, nicht die elektrische Ladung. Korrektur: Was in r41–r49 „T“ hieß, ist Zeitumkehr, nicht der Tachyon-Frame.

## Massen und Mischung (r50–r60)

- Die Maske aus r47 erklärt die Mischung nicht (r50, r52).
- Ein Parameter $\varepsilon$ je Sektor trifft CKM und PMNS, ist aber eine Anpassung, keine Erklärung (r54, r56).
- Je Teilchenart eine Untergruppe der $A_4$ (r55): Für Majorana-Neutrinos ergibt sich die TM2-Mischung mit $\sin^2\theta_{12} \approx 0{,}341$, 3,6σ über JUNO 2025. Mit Maskenkorrektur passen alle drei Winkel (r57).
- $\varepsilon$ als Rapidität des Materie-Frames (r60) trifft und legt $\sin^2\theta_{23} \in [0{,}49;\,0{,}50]$ fest; daraus die Vorhersage **H46**.

## Frames der offenen Probleme und der Gravitation (r61–r68)

- **OP1–OP5 im Frame-Licht (r61).** Mehrere alte Herleitungen mischen Materie- und Tachyon-Frame (Tribonacci, Hopf). OP4 ist in der alten Form falsch gestellt.
- **Zähl-Lesart (r63).** $\beta_{\mathrm{sym}}$ als Verhältnis zweier Zählungen von Horizontzuständen: Der Tachyon-Frame zählt nur Spin ½, der Materie-Frame alle Spins mit Gewicht 2. Das trifft das Leptonfenster.
- **Gravitationssätze (r64–r66).** In dieser Lesart sitzt der Frame-Unterschied in $\gamma$, nicht in $\hbar$ oder $G$; mehrere alte Folgerungen werden nicht gestützt.
- **Einsteins „größter Fehler“ (r67).** Der Companion setzt denselben Wert $\beta^2$ einmal auf $\Lambda$ und einmal auf die Materie. In Zählform ist $\Omega_M = 0{,}302$, $\Omega_\Lambda = 0{,}698$, gültig nur für die heutige Epoche.
- **Nachrechnung (r68).** Die Zahlen bestätigen sich. Die Zähl-Lesart braucht aber die U(1)-Zählung; die besser begründete SU(2)-Zählung gibt $\beta = 0{,}604$, außerhalb des Fensters.

## OP5, die 4.10-Konsolidierung und eine gemeinsame Dynamik (r69–r74)

- **OP5-Serie (r69).** Vom 25. bis 27.10. hat der Autor mit einem weiteren Sprachmodell an OP5 gearbeitet. Ergebnisse:
  - Ein Frame-Wechsel kann einen Bilanzfehler nicht beseitigen.
  - „Neutral“ hat drei verschiedene Bedeutungen.
  - Keine Route legt den absoluten Vakuumterm fest.
  - Der Lichtkegel der Sonden kommt aus der Clifford-Struktur.
  - Unter Torsionsfreiheit und der gewöhnlichen Einstein-Vakuumgleichung muss die geometrische kosmologische Konstante dort verschwinden, wo der Querstrom nicht null ist; das ist ein Ausschluss unter Voraussetzungen.
  - Drei Fehler im Hauptkorpus gefunden.
- **4.10-Konsolidierung (r70).**
  - Die drei Fehler sind korrigiert: Regularisierung, archivierte GUE-Uhrskala, Λ-Korollar. Ebenso eine falsche Gruppenbeschriftung an der Hopf-Faser $S^7$.
  - Neu ist der Abschnitt „States, Mediators and Clock Comparisons“:
    - Er trennt Quanten- und Relativitätsauslesungen über einen Vermittler mit klaren Beweispflichten.
    - Er rekonstruiert das reale Feld-Dublett lokal vollständig aus Gram-Matrix und Orientierung.
    - Er zeigt, dass eine gemeinsame Uhr allein keine Verschränkung beweist.
    - Er treibt eine numerische Verträglichkeitsprüfung bis zur vierten Ableitungsordnung an drei Punkten. Das ist keine Lösung auf einem Gebiet.
  - In r69 stand für den korrigierten Wert 1,689; richtig ist 1,686953.
- **Gemeinsame Dynamik (H48, r70).** Getestet wurde, ob $\beta_{\mathrm{sym}}$ als eingefrorene Länge des Zustands aus einer Dynamik folgt.
  - Ergebnis: widerlegt. Der eingefrorene Wert hängt an der Expansionsgeschichte.
  - Ein Einstein–Cartan-Spinterm koppelt in der dichten Phase nicht an den Zustand.
- **Λ als Mischung (Erkundung, r70).** Die Idee, $\Lambda$ sei eine Mischung über Kreuzungen der Sektoren, liefert keine bessere Zahl als $\Omega_M = \beta^2$.
  - Es bleibt eine Identität: $\beta^2$ ist das Verhältnis der beiden Eigenwerte des Materie/Tachyon-Zustands.
- **Struktur des Vergleichssystems (r71).** Der 70-stellige Keim des anderen Modells ist unabhängig bestätigt.
  - Die rätselhafte −1 bei Grad 5 war ein Rechenartefakt.
  - Das Vergleichssystem hat eine exakte Eichsymmetrie entlang des Polarwinkels $\vartheta$, weil sein Hintergrund nur $t$, $r$ und $\varphi$ kennt.
  - $\Omega$ ist eichinvariant und trägt neue Information nur auf dem Lichtkegel und auf zwei Ebenen.
  - Zwei Vorab-Tests (H49, H50) sind widerlegt.
  - Nächster Schritt: die $\vartheta$-Eichung festlegen, dann die Vollständigkeit prüfen.
- **Eichung und Cartan-Test (r72).** Die $\vartheta$-Freiheit wird durch eine Bedingung an eine Stromkomponente festgelegt; sie entfernt genau die freie Funktion.
  - H51 bestätigt: Das geeichte Symbol ist ab Ordnung 6 involutiv (Cartan-Test), vorher nicht. Übrig bleiben formal 14 Funktionen von drei Variablen.
  - H52 bis H54 (formale Integrabilität) sind wegen Planungsfehlern ungültig. Sie zeigen aber: Die gespeicherte fünfte Ordnung des Keims ist nicht fortsetzbar; bis zu den Gleichungen vom Grad 6 ist alles sauber; mit Grad 7 kommen vier Bedingungen an die sechsten Ableitungen hinzu.
  - Die Spencer-Kohomologie lässt genau vier zu, eine Fehlerschranke schließt ein Rechenartefakt aus. Formal bestätigt ist das nicht.
  - Nächster Schritt: zweiter Grundpunkt (H55), dann die vier Bedingungen bestimmen und den Cartan-Test wiederholen.
- **Die vier Bedingungen (r73).** H55 bestätigt sie an einem zweiten Punkt: Das geeichte System ist bei Ordnung 6 nicht formal integrabel.
  - Es sind Gleichungen sechster Ordnung, die nur lichtartige Wellen betreffen und je Richtung eine Polarisation festlegen; ihre Richtungsabhängigkeit kommt aus den beiden Ebenen von r71. Es sind die Reste der vier Beziehungen $q\,d_k\,\Omega$.
  - Der Cartan-Test mit ihnen (H56, H57) ist ungültig: bei Ordnung 6 nicht involutiv, ab Ordnung 8 reicht die Genauigkeit nicht.
  - Nächster Schritt: konsistente Daten in höherer Genauigkeit.
- **Konsistente Daten und Genauigkeitsgrenze (r74).** Mit $\Omega$ neu am reparierten Keim wird das erweiterte Symbol erstmals bei Ordnung 8 involutiv (H58, formal ungültig). Die Spencer-Kohomologie lässt bis zu vier weitere Bedingungen an siebten und drei an achten Ableitungen zu.
  - Die Grenze ist strukturell: $\Omega$ und die vier Bedingungen sind fast Folgen der Grundgleichungen. Stufenweise Elimination und ebene Wellen heben sie nicht auf.
- **Hohe Genauigkeit und Kovarianz (r77).** In 70 Stellen zeigt sich:
  - Es gibt genau vier versteckte Bedingungen.
  - Das Symbol ist erstmals bei Ordnung 8 involutiv.
  - Auf 7- und 8-Jets gibt es keine weiteren Bedingungen (H59), das System ist also am Keim formal integrabel.
  - Es trägt 6 masselose Moden (H60). Diese sind nicht vom Weyl- oder Majorana-Typ (H61).
  - Bei festem Hintergrund ist das Symbol nur unter Skalierung invariant (H62, H63).
  - Die Konstruktion R ist kovariant (H64). Die Lorentz-Brechung kommt vom Hintergrund.
- **Kovarianz auf Werteebene (r78).** R ist samt allen Termen niedrigerer Ordnung kovariant (H66), damit auch Ω. Die Eichung Ψ†K₂Ψ = S bleibt nur unter so(1,2) erhalten (H65(b)). Die vier Bedingungen sind daher höchstens unter so(1,2) kovariant.
- **Eichunabhängigkeit (r79).** In fünf Eichungen, darunter der Lorentz-Skalar Ψ̄Ψ, gibt es jeweils genau die vier Bedingungen und 6 Polarisationen (H67). Die Bedingungen sind damit kovarianter Inhalt des Systems; die Lorentz-Brechung kommt nur vom Hintergrund.
- **Hintergrund nicht aus den Spinoren, Abschluss (r80).** Die drei Spinorblöcke sind reguläre Dirac-Flüssigkeiten in einer Hubble-artigen Gegenströmung mit Spins entlang der Azimutachse (Erkundung). Der Hintergrund A, h erfüllt aber weder Yang–Mills noch Klein–Gordon mit diesen Blöcken als Quelle (H68 widerlegt, Residuen 0,83–1,0); die Quellen sind rund tausendmal zu klein und zeigen in andere Farbrichtungen. Auf Entscheidung des Autors ist der Zweig r71–r80 damit abgeschlossen. Die Ergebnisse bleiben lokale Aussagen über ein Vergleichsmodell mit vorgegebenem Hintergrund; weiter geht es eine Ebene höher mit der gemeinsamen Dynamik.
- **Gemeinsame Wirkung W1 (r81).** Nach dem Abschluss des Vergleichsmodells eine eigene Wirkung: Koframe als eigenes Feld, Einstein–Cartan ohne Λ, die 16 Weyl-Zustände einer Generation auf der Dixon-Ablage. Die komplexe Lesart verlangt eine Strombilanz zwischen Materie und Tachyonbild; ein mitbewegt versetztes Paar erfüllt sie exakt und ist energetisch neutral (H69, H70). Mit Masse wird das Tachyonbild tachyonisch (H71). Ein Vakuumterm ist aus tachyonischen Moden möglich, seine Größe aber frei (H72, H73 widerlegt). Das Higgs-Feld lässt sich als Übergang zwischen Materie und gegenläufigem Tachyonbild lesen. Korrigiert wird unter anderem die Frame-Lesart von r44.
- **Higgs-Sektor und Stabilität (r82).** W2 ergänzt W1 um ein Higgs-Dublett; das Vorzeichen −μ² wird als tachyonischer Übergangskonnektor gelesen, nicht hergeleitet. Mit dem Tachyonbild aller Felder sollte sich die Higgs-Vakuumenergie bei Photon-Gewichten exakt aufheben (in r83 zurückgezogen, siehe dort). Diese Aufhebung ist bei direkter Kopplung instabil (H74), bei reiner Gravitation nicht exponentiell instabil, aber mit gemeinsamem Durchgehen (H75). Der Torsionsterm von W1 ist in einem Paarkanal anziehend, kondensiert aber erst an der Planck-Skala. Mechanismen ja, Skala nein.
- **Vakuumzerfall und Tachyonbild einer Wirkung (r83).** Über das Graviton zerfällt das Vakuum in ein Materie-Paar und ein Paar negativer Energie; ohne ausgezeichneten Rahmen ist die Rate unbeschränkt (H76), mit Rahmen-Cutoff ist sie endlich, und die Daten verlangen Λ ≲ 14 MeV. Das Tachyonbild einer Wirkung ist so zu bilden, dass die Kinematik fortgesetzt wird und Konstanten und Potentiale bleiben (H77); nur das passt zu r20, H71 und r81. Damit fällt die Aufhebung der Higgs-Vakuumenergie aus r82 weg: Das Higgs-Bild ist um null stabil. Dafür wird ein gesunder Term X/2 + cX² im Bild zu einer Geist-Kondensation mit eigenem Rahmen, w = −1 und ohne Zerfall (Erkundung).

## Namen (r75)

- **Kompensatormatrix statt Millennium-Matrix.** Die Matrix $\mathcal M_{16}$ heißt seit r75 Kompensatormatrix (Autorentscheidung). Nur der Name ändert sich; Symbol, Labels, das Kürzel MM und alle Aussagen bleiben. Runde r76 korrigiert r75: Der Name „layer-transport matrix“ aus r05 wird durch Kompensatormatrix ersetzt; „port-weighting matrix“ für die Dublett-Einschränkung bleibt.

[Inhaltsübersicht](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Inhalt) · [Offene Probleme](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Offene-Probleme)
