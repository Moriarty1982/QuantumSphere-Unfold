# Was im Companion steht

**Stand: 5. November 2026, Forschungsfassung 4.10.0-draft mit Runden bis v4.10.0-r08.** Diese Seite gibt den Inhalt des *Quantum Sphaera Companion* wieder: Was wird angenommen, was wird definiert und gezeigt, und wie weit trägt es heute? Die Quellenangaben am Ende jedes Abschnitts dienen zum Nachprüfen; zum Verstehen sollte diese Seite allein reichen. [English version](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Content-overview) · [Startseite](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Home)

## So ist jede Aussage zu lesen

Der Companion trennt drei Ebenen, und dieses Wiki übernimmt die Trennung:

| Ebene | Bedeutung |
|---|---|
| **Vermutung** | die Ausgangshypothese, von der aus die Mathematik entwickelt wurde |
| **Mathematik** | eine im Companion gebaute Definition, ein Satz oder eine Konstruktion |
| **Stand** | was davon bewiesen, nur lokal oder bedingt gesichert, numerisch geprüft, widerlegt oder offen ist |

Dass Mathematik aus einer Vermutung heraus gebaut wurde, beweist die Vermutung nicht. Ob aus der Grundvermutung eine vereinheitlichte Theorie folgt, ist offen.

## Die Grundvermutung

Raumzeit und Teilchen sind Projektionen einer darunterliegenden Informationsebene. Materie, Licht (Photon) und ein Tachyon-Sektor sollen *dasselbe* Objekt sein, gesehen aus drei verschiedenen Bezugsrahmen (Frames). Die Raumzeit-Punkte sollen aus einem „Taktgeber“ gewonnen werden, ursprünglich den Nullstellen der Riemannschen Zetafunktion.

**Stand:** Vermutung. Die Riemann-Arbeit, aus der der Taktgeber stammt, ist seit v4.8.0-r04 keine Beweisquelle mehr; ihre Beweiskette für die Riemannsche Vermutung trägt nicht.

## 1. Die Sprache: QAM über ZF

Der Companion beschreibt Zustände, Schichten, Operatoren, Auslesungen und Zweige in einer eigenen kodierten Sprache, der **QAM**. Sie ersetzt die Mengenlehre nicht, sondern sitzt auf ihr: Acht Grundbegriffe (Zustand, Schicht, Operator, Auslesung, Zweig, Hülle, Zeuge, Tensor) werden als markierte Tupel in der Zermelo–Fraenkel-Mengenlehre definiert. Das erste Tupelelement ist ein Typ-Kennzeichen, deshalb können sich die Klassen nicht überschneiden. Darüber liegen eine endliche Befehlssprache (MML) und deren Ausführungssemantik (MMA).

**Stand:** Die Definitionen sind sauber. Sie sind Erkennungsregeln, kein eigenes Axiomensystem. Dass die Rückübersetzung in reine Mengenlehre funktioniert, ist für den zulässigen Teil gezeigt, aber schwächer als eine volle wechselseitige Interpretierbarkeit.

*Quelle: Anhang „Complete QAM, MML and MMA Infrastructure“; Primitive bei `def:qam-kernel-bridge-datum`.*

## 2. Der Grundbaustein: drei komplexe Kerne

Jede Stufe der Struktur hat einen **Biquaternion-Kern** aus drei komplexen Kernen $K_1, K_2, K_3$:

$$
q = it\cdot 1 + z_1e_1 + z_2e_2 + z_3e_3,\qquad e_3 = e_1e_2,\quad z_k\in\mathbb C.
$$

Eine **Involution** $J$ (zweimal angewandt ergibt sie wieder den Ausgangszustand) zerlegt jeden Zustand in einen symmetrischen und einen antisymmetrischen Teil:

$$
C(f) = \tfrac12(f+Jf),\qquad A(f) = \tfrac12(f-Jf).
$$

$C$ heißt **Heisenberg-Kompensator**. Er wählt den $J$-symmetrischen Teil aus; zweimal angewandt ändert er nichts mehr ($C^2 = C$).

**Welcher Sektor welcher ist** (seit v4.8.0-r07): Entscheidend ist das Vorzeichen von $s = z_1^2 + z_2^2 + z_3^2$. Materie hat $s>0$, Tachyon $s<0$, Licht liegt auf $s = 0$. Die ursprüngliche Norm $-t^2 + \sum|z_k|^2$ hatte die falsche Signatur (1,6); seit r06 gilt die natürliche Norm $q\bar q$ („Lesart B“, mit der Gruppe $SO(3,\mathbb C)$ als Lorentz-Wirkung).

**Stand:** Zerlegung und Sektorregel sind gesicherte Mathematik. Die Behauptung, die drei Kerne trügen unitär äquivalente Darstellungen, stützte sich auf die Riemann-Arbeit und ist offen. Dass die Sektoren Materie, Tachyon und Licht *sind*, ist Vermutung.

*Quelle: `def:biquaternion`, `thm:unitary-equiv`, Runden v4.8.0-r06/r07.*

## 3. Hopf-Struktur und die Frame-Konstanten

Die drei Stufen der Struktur werden mit den drei klassischen Hopf-Faserungen verbunden: $S^2$ (Licht, Weyl-Spinor), $S^4$ (Materie, Dirac-Spinor), $S^8$ (drei Generationen, oktonionischer Spinor). Die Fasern $S^1 \cong U(1)$, $S^3 \cong SU(2)$ und $S^7$ sollen die Eichgruppen tragen.

Der zentrale Zahlenwert ist der **Frame-Versatz** zwischen Materie und Licht:

| Größe | Wert | Herkunft |
|---|---|---|
| $\gamma_{\mathrm{string}} = \ln 2/(\pi\sqrt3)$ | 0,12738 | Barbero–Immirzi-Wert nach ABCK (nur Spin ½) |
| $\gamma_{\mathrm{BI}}$ | 0,2375 | Barbero–Immirzi-Wert nach Domagała–Lewandowski/Meissner |
| $\gamma_L = \gamma_{\mathrm{BI}}/\gamma_{\mathrm{string}}$ | 1,8644 | Verhältnis der beiden |
| $\beta_{\mathrm{sym}} = \sqrt{(\gamma_L-1)/(\gamma_L+1)}$ | 0,5494 | Frame-Versatz |

**Stand:** Die Hopf-Faserungen sind klassische Mathematik, ihre Zuordnung zu Teilchen ist Vermutung. $\beta_{\mathrm{sym}}$ wird **eingesetzt**, nicht hergeleitet. Seit r63 wird es als Verhältnis zweier Zählungen von Horizontzuständen gelesen; das funktioniert aber nur mit der U(1)-Zählung, und die Literatur hält die SU(2)-Zählung für besser begründet (r68). Die frühere Beschriftung der Faser $S^7$ als Gruppe „$\supset G_2 \supset SU(3)$“ war falsch und ist korrigiert: $G_2$ ist die Automorphismengruppe der Oktonionen, $SU(3)$ der Stabilisator einer imaginären Einheit.

*Quelle: `thm:hopf`, `thm:three-generations`; Runden r63–r68, r70.*

## 4. Triolen

Die Grundstruktur ist dreigliedrig: drei gleich lange, um 120° gedrehte komplexe Zahlen summieren sich zu null ($1 + \omega + \omega^2 = 0$). Geometrisch wird das als **triolischer Orbit-Scan** gefasst: Bahnen um einen bewachten Kern, die ihm nie näher als ein Abstand $\varepsilon$ kommen, mit Linsen-Triole, Teilchen-Triole und einem Shift-Selektor, der zwei Regime vertauscht.

Im Lauf der v4.9.0-Runden hat sich gezeigt, dass das Wort „Triole“ drei verschiedene Strukturen bezeichnet: die drei Frames Materie/Photon/Tachyon, die drei Kerne im 120°-Abstand, und drei Plätze $(x,y,z)$ der Triality-Form $t = \mathrm{Re}((xy)z)$ der Oktonionen (r37).

**Stand:** Der Orbit-Scan ist sauber definiert und im gesetzten Rahmen bewiesen, als lokales Auslesemodell, nicht als physikalische Bahn. Die Übertragung auf eine globale Struktur ist offen.

*Quelle: `sec:alternating-triolic-orbit-scan`, `thm:strict-alternating-triolic-orbit-scan`; Runden r37, r38.*

## 5. Fraktal und Lichtachse

Auf jeder Stufe gibt es eine **Null-Achse** (die Zustände mit $s = 0$). Behauptet wird, dass die Kaskade diese Achse von Stufe zu Stufe abbildet ($\hat K(L_n) = L_{n-1}$) und die globale Null-Achse die Lichtachse ist. Eine Kristall-Fraktal-Probe liefert eine diagnostische Dimension $D_{\mathrm{res}} \approx 2{,}435$.

**Stand:** „Fraktal“ meint hier den selbstähnlichen Transport derselben Struktur, keine fraktale Dimension im strengen Sinn. Der Transport ist ausdrücklich offen („transport open“); der Beweis ist nur skizziert. $D_{\mathrm{res}}$ ist eine Kennzahl, kein Beweis.

*Quelle: `thm:fractal`, Abschnitt „Fractal Self-Traversal Along the Light Axis“.*

## 6. Die Mastergleichung

Alles soll in eine strukturelle Gleichung münden:

$$
\mathfrak G[\Psi,g] + \mathfrak T_{\mathrm{tri}}[\Psi] + \mathfrak H_{\mathrm{HC}}[\Psi] + \mathfrak Q_{\mathrm{cl}}[\Psi] + \mathfrak B_\beta[\Psi] = 0
$$

mit Beiträgen für Geometrie, Triolen-Dynamik, Kompensator, Schließung und Frame-Phase. Eine Kette von der Triolenquelle über die 16-dimensionale **Kompensatormatrix** (bis r75 „Millennium-Matrix“) $\mathcal M_{16}$ bis zu Materie, Tachyon, Photon und Feldgleichungen ordnet die Bestandteile.

**Stand:** Die Gleichung ist eine Gliederung dessen, was zusammenwirken soll. Ihre Kopplungen sind nicht bestimmt, eine definierte Wirkung fehlt. Auf GitHub prüfen eigene Abschnitte, was daraus folgt und was nicht:
- **Spektrale Identifikation:** Dass zwei Operatoren vertauschen, macht ein Bild noch nicht zu einem einzigen Eigenraum. Ausreichende Zusatzbedingungen werden angegeben (`v480:conditional-mm`).
- **Massen aus dem Kompensator:** Direkte Wege vom Kompensator zu den Leptonmassen werden einzeln widerlegt; ein frei angepasster Kompensator sagt keine Massenwurzeln voraus (`v480:hc-mass-identification`).
- **Generationen und Kopplung:** Eine zyklische Kopplung kann die Brannen-Form der Massen erzeugen, aber gemeinsame Phasen fallen heraus, und die Gram-Matrix bleibt unterbestimmt (`v480:generation-coupling`).
- **Skalen:** Kopplungs- und Lückenskala bleiben freie Eingaben; eine Skalenwahl repariert eine falsche Form nicht (`v480:native-operator-link`, Kopplungskandidat).
- **Dynamik und Geometrie:** Positivität der Massenwurzeln ist eine eigene dynamische Pflicht; eine Projektion behält verborgene Zustände; eine aus Spinoren rekonstruierte Geometrie ist bedingt und nicht automatisch Lösung der Feldgleichungen (`v480:hc-dynamics-geometry`).
- **Einstein–Cartan-Vergleich:** Für ein ausdrücklich hinzugefügtes Vergleichsmodell werden endliche Ableitungsdaten verträglich gemacht; das ist keine Lösung auf einem Gebiet (Cartan-Abschnitt).

*Quelle: `thm:master-structural`, `thm:master-field-equation`; die genannten 4.8-Forschungsabschnitte.*

## 7. Die offenen Probleme OP1–OP5

| OP | Frage | Stand |
|---|---|---|
| OP1 | Warum $\beta_{\mathrm{sym}} \approx 0{,}549$ und nicht der symmetrische Wert $1/\sqrt3$? $\beta_{\mathrm{sym}}$ aus der Struktur herleiten statt einsetzen | offen; seit r63 umformuliert zu „die beiden Zählregeln aus den Frames begründen“ |
| OP2 | Dirac-Operator $`D_- = L_0\vert_{H^+_-}`$ auf dem antisymmetrischen Sektor | in der alten Fassung als existent und selbstadjungiert markiert, gestützt auf die Riemann-Arbeit (seit v4.8.0-r04 keine Beweisquelle); der letzte Schritt ist dasselbe Problem wie OP1 |
| OP3 | zulässiger Hüllen-Übergang („shell passage“) mit Schließungszertifikat in der QAM | als lokales Zertifikat formuliert (`thm:qam-op3-shell-closure`), im Kristallbild als Zellverträglichkeit gelesen |
| OP4 | Herkunft der Mischungswinkel (CKM/PMNS, Cabibbo-Winkel) | offen; r61: in der alten Form falsch gestellt |
| OP5 | kosmologische Konstante und Vakuumbilanz | nur lokal (Detektorschwelle) geschlossen, exakt offen; im numerischen Vergleichssystem eine exakte Polarwinkel-Eichsymmetrie gefunden (r71); geeicht ist das Symbol ab Ordnung 6 involutiv, aber dem System fehlten vier Bedingungen sechster Ordnung, inzwischen bestätigt und bestimmt (r72, r73); mit ihnen ist das System am Keim formal integrabel, trägt 6 masselose Moden und ist als Konstruktion kovariant; die Lorentz-Brechung kommt vom Hintergrund (r77); R und Ω sind auch auf Werteebene kovariant, die Eichung erhält nur so(1,2) (r78); die vier Bedingungen sind eichunabhängig (r79); der Hintergrund wird nicht von den Spinoren erzeugt (kein Yang–Mills, kein Klein–Gordon mit ihnen als Quelle), der Vergleichsmodell-Zweig ist damit abgeschlossen (r80); eine gemeinsame Wirkung W1 ist aufgestellt, ein Vakuumterm aus tachyonischen Moden ist möglich, seine Größe aber nicht festgelegt (r81); mit Higgs-Sektor W2 schien sich die Vakuumenergie bei Photon-Gewichten aufzuheben (r82), das ist mit der richtigen Lesart des Tachyonbilds zurückgezogen (r83); das Vakuum zerfällt ohne ausgezeichneten Rahmen über die Gravitation (r83), eine Geist-Kondensation könnte Rahmen und Stabilität liefern; als zweite Lesart desselben Feldes mit vollständigem komplexem Boost ist der Tachyon-Anteil isotrop, stabil und ohne Zerfall (r84); mit dem Tachyon-Anteil vor dem Urknall wird der Urknall ein CPT-artiger Übergang mit einer durch β_sym festgelegten Teilchenbeimischung (r85), von einem zweiten System bestätigt; die Feldgleichungen der gemeinsamen Wirkung sind bis auf die volle Einstein-Gleichung unabhängig hergeleitet, ein homogener Fermionzustand ist steife Materie, kein Vakuumterm (r86); eine Skala liefert die Struktur nicht |

Ausführlich: [Offene Probleme](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Offene-Probleme).

## 8. Physikalische Auslesungen: kosmologische Konstante, Planck-Länge, Hawking

Der Companion leitet aus dem Frame-Versatz physikalische Größen ab. Der heutige Stand nach den Prüfrunden:

- **Kosmologische Konstante:** Die alte Rechnung setzt $\Lambda$ im Photon-Frame auf null und erklärt den beobachteten Wert als Messeffekt des Materie-Frames. Mehrere Glieder dieser Kette tragen nicht: Die verwendete Spurformel ist keine definierte Wirkung (v4.8.0-r05), die Zahl $\beta^2/\ell_P^2$ ist um den Faktor $10^{121}$ zu groß, und das Korollar „Cosmological constant revisited“ nennt für dieselbe Größe zugleich null und ein endliches Verhältnis $\gamma_L^5$. Haltbar ist nur die Lesart $\Omega_M = \beta_{\mathrm{sym}}^2 \approx 0{,}302$ als Anteil (Planck 2018: 0,315 ± 0,007; DESI DR2: 0,2975 ± 0,0086), und auch sie nur für die heutige Epoche (r67).
- **Regularisierung der alten Bilanz:** Die gedruckte Entwicklung, der Gegenterm und der Wert 0,940 waren falsch. Richtig ist $R(\tau) = -1/\tau + 1 - \tfrac{11}{24}\tau + \dots$ mit Gegenterm $-\log(\varepsilon/\mu)$ und endlichem Teil 1,686953 bei $T = 0{,}393$, $\mu = 1$ (r69, korrigiert r70).
- **Planck-Länge und Hawking-Temperatur:** In der Zähl-Lesart (r63) steckt der Frame-Unterschied in $\gamma$, nicht in $\hbar$ oder $G$. Die Photon-Planck-Skalierung $\gamma_L^{-3/2}$ und der Vakuumquotient $\gamma_L^5$ werden dadurch nicht gestützt (r64); der Hawking-Abschnitt ordnet eine Tachyonzählung dem austretenden Photon zu (r64, Statusvermerk r65).
- **Entropiefaktor und Gravitationskopplung:** Nach der Herleitung von Dorau und Much (PRL 2026) bestimmt der Vorfaktor des Flächengesetzes die Gravitationskopplung, $G_{\mathrm{eff}} = G/c$. Die beiden Horizontzählungen des Companion unterscheiden sich bei gleichem $\gamma$ um $\gamma_L$; ein einziges gemessenes $G$ verlangt deshalb, dass jeder Frame mit seinem eigenen passenden $\gamma$ zählt (v4.10.0-r06). $\Lambda$ bleibt auch dort frei.
- **Gravitation in beiden Frames:** Für das freie Maxwell-Feld gibt dieselbe Herleitung im Tachyon-Frame dieselbe Einstein-Gleichung, weil die Tachyon-Abbildung (Dualitätsdrehung) mit den Lorentz-Transformationen vertauscht und der Energie-Impuls-Tensor dualitätsinvariant ist (v4.10.0-r07). Den Vorfaktor ¼ des Flächengesetzes liefert der Companion nicht: Er fällt im Verhältnis der beiden Zählungen heraus.
- **Annahmen und Vorhersagen:** Die offenen Vorhersagen H15, H46 und H96 hängen am selben γ_L-Kern (Literaturwerte und Zählregel je Frame), H42 nicht (v4.10.0-r08). Alle vier ruhen auf Lesarten des Kerns, nicht auf Herleitungen.
- **Alte Vorhersagen P1–P6:** keine bestätigt (P1 nicht bestätigt, P2 ausgeschlossen, P3 Zufall, P4 widersprüchlich, P5 korrigiert auf ½, P6 ungetestet).

*Quelle: `thm:dark-energy`, `rem:regularization-B`, `cor:falsifiable`; Runden v4.8.0-r03–r09, v4.9.0-r63–r70.*

## 9. Die Standardmodell-Struktur aus den Oktonionen

Die Runden r32–r60 bauen aus der Dixon-Algebra $\mathbb C \otimes \mathbb H \otimes \mathbb O$ schrittweise die Bausteine einer Teilchengeneration: Ladungen 0, 1/3, 2/3, 1 aus einem Zahloperator (r34, r35), die volle linkshändige Generation mit rechtshändigem Neutrino und anomaliefreien Quantenzahlen, wenn der Kompensator als Chiralitätsprojektor gelesen wird (r42, r43), und Generationen als Bahnen der Triality-Symmetrie (r37). Massen und Mischung bleiben der schwierige Teil: Masken und Kopplungen passen die Mischungsdaten an, erklären sie aber nicht (r50–r56). Ausführlich: [Forschungslinie](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Forschungslinie).

**Stand:** konstruiert unter benannten Wahlen; die Wahlen selbst sind nur teilweise hergeleitet.

## 10. Was nie behauptet wird

Der Companion arbeitet mit **Guards**: einer Liste erlaubter (lokaler, effektiver, frame-typisierter) und verbotener (exakter, globaler) Aussagen. Nie behauptet werden eine exakte endliche C5-Nullschließung, eine exakte Terminalität aller Auslesungen, eine T2-Schließung, ein globaler Photon-Uhr- bzw. Riemann-Satz und eine globale Schließung aller Auslesungen. Seit Runde r60 stehen alle fünf Guards unverändert. Die sichere Formulierung lautet: *guarded effective/local and frame-typed closures, not exact global closure.*

[Forschungslinie](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Forschungslinie) · [Vorhersagen und Tests](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Vorhersagen-und-Tests) · [Offene Probleme](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Offene-Probleme) · [Begriffe](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Begriffe)
