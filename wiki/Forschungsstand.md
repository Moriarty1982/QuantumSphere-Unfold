# Forschungsstand

**Quellenstand: 2.11.2026, GitHub `main` bei cf48496 plus Runden r70 und r71.** Diese Seite fasst den aktuellen Stand zusammen; sie ist kein neuer Beweisaudit. Was im Companion insgesamt steht, beschreibt die [Inhaltsübersicht](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Inhalt); die Ergebnisse aller Runden nach Themen die [Forschungslinie](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Forschungslinie). [Quellenkarte](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Versionen-und-Quellen).

## Bedingte Ergebnisse

Die v4.9.0-Linie enthält unter anderem bedingte Cartan-Vergleiche, endliche Normal-Inversen und Quellgesetze, Koide-bezogene Gleichnormbedingungen sowie Untersuchungen zur HC-Massenidentifikation und Generationenkopplung. Voraussetzungen und Einschränkungen stehen in den jeweiligen Abschnitten und Analysen. Ein endlicher Inversen- oder Kompatibilitätssatz liefert für sich weder regionale PDE-Existenz noch native physikalische Identifikation.

## Jüngste Korrekturen auf der 4.10-Basis

Die [Basisrevision](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/v4_10_0_base/README.md) archiviert zurückgezogene Aussagen, korrigiert bekannte Fehler und kennzeichnet offene bzw. umgedeutete Aussagen. Historischer Text ist zusammen mit seinem aktuellen Status zu interpretieren.

Die [Layer r63–r68](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/v4_10_0_r63_r64/README.md) unterscheiden Zählregeln und prüfen deren Frame-Deutung. Dokumentiert wird insbesondere:

- `thm:k-values` mit $k(\gamma_{\mathrm{BI}})=0$ widerspricht `thm:frame-offset`. Dieser Widerspruch ist nicht neu: v4.9.0-r09 hat ihn bereits festgestellt und aufgelöst, indem `thm:frame-offset` nur vom strukturellen Faktor $\gamma_L$ spricht. r66 korrigiert die fehlende Zitierung in r64 und erweitert die Statusnotiz.
- In der Zähllesart liegt der Frame-Unterschied in $\gamma$; die Zuordnungen für $\hbar$ und $G$ benötigen eine andere Begründung.
- Die Photon-Planck-Skalierung $\gamma_L^{-3/2}$ und der Vakuumquotient $\gamma_L^5$ werden durch diese Lesart nicht gestützt.
- Im Hawking-Abschnitt wird eine Tachyonzählung dem austretenden Photon zugeordnet. r65 ergänzt hierzu Statusnotizen im Haupttext.
- In der Zähllesart ist der strukturelle Faktor eine feste Zahl; die beiden Zählregeln sind diskret und liefern keinen stetig driftenden lokalen Frame-Faktor (r66). Die Drift-Lesarten aus r08/r09 sind ohnehin durch Atomuhren ausgeschlossen.
- Zu Einsteins „größtem Fehler“ (`rem:einstein-blunder`, r67): Die Bemerkung und die Feldgleichung in `rem:omega-bsym` setzen $\beta_{\mathrm{sym}}^2$ auf $\Lambda$, `thm:dark-energy` setzt denselben Wert auf die Materie ($\Omega_M=\beta_{\mathrm{sym}}^2$). In der Zähllesart ist $\Lambda$ als Krümmung frame-unabhängig; erklärbar wäre höchstens der Anteil $\Omega_\Lambda=2\gamma_T/(\gamma_M+\gamma_T)\approx0{,}698$, und nur für die heutige Epoche. Offen bleibt, warum ein Zählanteil einem Energieanteil entsprechen soll.
- Unabhängige Nachrechnung (r68): Die Zahlen von H47 und r63–r67 bestätigen sich. Einschränkung: Die Zähllesart funktioniert nur mit der U(1)-Behandlung der Horizontzustände ($\gamma\approx0{,}2375$). Die als besser begründet geltende SU(2)-Behandlung ergibt $\gamma\approx0{,}274$ und $\beta_{\mathrm{sym}}\approx0{,}604$, außerhalb des Leptonfensters. Die registrierte Vorhersage H46 bleibt mit dem ungerundeten Wert gültig.

Das sind Einschränkungen bestimmter Argumente, keine allgemeine Widerlegung jeder möglichen Gravitationstheorie.

## OP5: Vakuumterm, Frames und Neutralität (r69)

Der Autor hat vom 25. bis 27. Oktober mit einem weiteren Sprachmodell an OP5 gearbeitet; die Notizen liegen unter `analysis/` (Prefix `OP5_`). [Layer r69](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/b12adf5fc0a69d32e0405b78dfb505c3b9bbea44/notes/research/v4_10_0_r69/README.md) bindet sie ein. Alle Prüfskripte ließen sich reproduzieren, neun Aussagen wurden mit eigenem Code nachgerechnet. Jede positive Aussage der Serie ist bedingt (Vergleichsmodell, gewählter Zeuge oder zwei Stichpunkte). Festgehalten wird:

- Ein passiver, invertierbarer Frame-Wechsel skaliert einen Bilanzdefekt nur; er kann ihn nicht beseitigen. Die Ersetzung von $\gamma_L$ durch $e^\eta$ schließt die historische Bilanz nicht.
- „Neutral“ hat drei verschiedene Bedeutungen: Mittelpunkt zweier Skalenframes; gleichgewichtige Mischung eines Zustands mit seinem Tachyonbild ($I/2$, Etikett P); flussfreier Beobachter zweier Nullströme (Stress $\mathrm{diag}(\rho,\rho,0,0)$, kein Vakuumtensor). Sie dürfen nicht gleichgesetzt werden.
- Keine der geprüften Routen legt den absoluten Vakuumterm fest. Ein gemeinsamer Energieversatz ist bei festem Hintergrund unbeobachtbar; im alternativen affinen Vergleichsmodell löst ein Zweig die Feldgleichungen für jede Konstante.
- Der Lichtkegel der Sondengleichung kommt aus der Clifford-Struktur, nicht aus Masse-, $M_{16}$-, triadischen oder HC-Termen. Kegeldaten legen weder eine absolute Skala noch das Gewicht eines Vakuumterms fest.
- Mit der verbundenen Querauslese $E=\tfrac12 Dj$ gilt $T=\tfrac12 Rj$. Torsionsfrei und mit gewöhnlicher Einstein-Vakuumgleichung folgt $\Lambda_{\mathrm{geom}}=0$, wo $j\neq0$: ein Ausschluss unter diesen Voraussetzungen, keine Aufhebung von Vakuumenergie.
- Drei Fehler im Hauptkorpus wurden gefunden: `rem:regularization-B` (Reihenentwicklung und Vorzeichen des Gegenterms falsch; der Wert 0,940 stimmt nicht), `thm:dirac-probe` und `prop:three-compatible-readings` stützen die Uhrskala auf das archivierte `thm:gue-selfdet`, und das Korollar „Cosmological constant revisited“ gibt für dieselbe Größe null und $\gamma_L^5$ an. Alle drei sind seit der 4.10-Konsolidierung korrigiert bzw. mit Statusvermerk versehen (siehe unten). Der in r69 genannte richtige Wert 1,689 war selbst falsch; richtig ist 1,686953 (r70).

OP5 bleibt in der exakten Form offen; die lokale Detektorschließung $\mathrm{OP5}_{\mathrm{eff}}$ ist davon nicht berührt.

## 4.10-Konsolidierung, H48 und Λ als Mischung (r70)

Am 29. und 30. Oktober hat das zweite Sprachmodell den Forschungskandidaten direkt weitergeschrieben; Runde r70 übernimmt das in die lokale Gesamtquelle und verbucht es.

- **Korrekturen im Hauptkorpus.**
  - Die Regularisierung lautet jetzt $R(\tau) = -1/\tau + 1 - \tfrac{11}{24}\tau + \dots$ mit Gegenterm $-\log(\varepsilon/\mu)$. Der endliche Teil bei $T = 0{,}393$, $\mu = 1$ ist 1,686953 und hängt von der gewählten Skala $\mu$ ab. Das alte Ziel 0,893 ist zurückgezogen.
  - Statusvermerke stehen jetzt an der Dirac-Sonde, an den drei Lesarten der fermionischen Sonde, am Λ-Korollar, an der Verschränkung als gemeinsamer Eigenzeit (eine gemeinsame Uhr beweist allein keine Verschränkung) und an der alten Vorhersageliste.
  - Die Faser $S^7$ war als Gruppe „$\supset G_2 \supset SU(3)$“ beschriftet. Das ist falsch und entfernt: $G_2$ ist die Automorphismengruppe der Oktonionen, $SU(3)$ der Stabilisator einer imaginären Einheit.
- **Neuer Abschnitt „States, Mediators and Clock Comparisons“.**
  - **Vermittler:** Quanten- und Relativitätsauslesung eines gemeinsamen Trägers werden nur über einen Vermittler mit ausdrücklichen Beweispflichten verbunden.
  - **Feld-Dublett:** Das reale Dublett $[E\,|\,B]$ lässt sich lokal aus seiner Gram-Matrix und drei Orientierungsparametern vollständig zurückgewinnen. Der normierte Zustand allein verliert Skala und Flussrichtung.
  - **Uhren:** Zwei Uhren mit festen Raten stimmen nach einer Kalibrierung $\tau = at_a = bt_b$ überein; dafür braucht es keine zweite Quantenzeit.
  - **Numerik:** Die numerische Verträglichkeit der Feldgleichungen erreicht an drei Punkten die vierte Ableitungsordnung. Das ist keine Lösung auf einem Gebiet.
- **H48 (Vorab-Test, widerlegt).** Getestet wurde, ob $\beta_{\mathrm{sym}}$ als eingefrorene Länge des Materie/Tachyon-Zustands aus einer Dynamik folgt.
  - Der eingefrorene Wert hängt an Expansion und Dichte, nicht nur an einem Ratenverhältnis.
  - Ein Einstein–Cartan-Spinterm koppelt nicht, weil der Zustand in der dichten Phase senkrecht zur Chiralitätsachse liegt.
- **Λ als Mischung über Sektor-Kreuzungen (Erkundung).** Keine der 26 Lesarten trifft besser als Zufall. $\Omega_M = \beta_{\mathrm{sym}}^2 \approx 0{,}302$ bleibt die beste Zahl (Planck 2018 −1,9σ, DESI DR2 +0,5σ).
  - Festgehalten wird eine Identität: $\beta^2$ ist das Verhältnis der beiden Eigenwerte des Materie/Tachyon-Zustands.

Nichts davon schließt OP5 oder ändert die Guards.

## OP5: Struktur des Vergleichssystems und eine exakte Eichsymmetrie (r71)

Am 2. November hat der Autor die OP5-Arbeit dort fortgesetzt, wo das zweite Sprachmodell aufgehört hatte (Commit `cf48496`): ein auf 70 Stellen genauer Feldkeim bis zur fünften Ordnung im festen Vergleichsmodell, die zusätzliche Bedingung $\Omega$ an die dritten Ableitungen und eine Zählung bei Grad 5, die je nach Schwelle 1, 0 oder −1 ergab. Runde r71 hält fest:

- **Der Keim ist unabhängig bestätigt.** Zwei eigene Implementierungen ohne gemeinsamen Code mit dem anderen Modell zeigen, dass der Keim das vollständige System $R = (F, G, dg)$ bis Grad 3 erfüllt. Dazu gehört auch der Teil $G$, der vorher nur vom anderen Modell geprüft war.
- **Die −1 ist ein Rechenartefakt.** Mitgezählt wurde eine Richtung, die die Grundregel „der Rand eines Randes ist null“ verletzt. Sauber gezählt kommen mit dem gespeicherten $\Omega$ bei Grad 5 vier neue Klassen heraus, nicht 0 oder 1.
- **Die Struktur dahinter.**
  - Das System lässt eine freie Funktion von vier Variablen unbestimmt.
  - $\Omega$ ist für diese freie Richtung blind und bringt neue Information nur für Wellen auf dem Lichtkegel der rekonstruierten Geometrie oder in zwei besonderen Ebenen.
- **Die freie Funktion ist eine exakte Eichsymmetrie.** Sie verschiebt das Feld entlang des Polarwinkels $\vartheta$. Der Hintergrund des Modells hängt nur von $t$, $r$ und $\varphi$ ab: Die Masse ist $h(t, r)$, die Verbindung ist $A = M(t)\,d\varphi$. Deshalb ändert keine $\vartheta$-Umparametrisierung die Gleichungen.
- **H49 (Vorab-Test, widerlegt).** Vermutet war, dass abseits des Äquators schon bei den zweiten Ableitungen eine versteckte Bedingung auftaucht. Das trifft nicht zu. Die Prämisse, ein Term $\propto z/\rho^2$ breche die Freiheit, war falsch.
- **H50 (Vorab-Test, widerlegt).** Gefragt war, ob $\Omega$ über die $\vartheta$-Richtung auf $\Psi$ zurückwirkt (Frage des Autors). Das tut es nicht: $\Omega$ ist eichinvariant und ändert sich unter allen geprüften Verschiebungen um höchstens $10^{-10}$.

Folgerung: Vor einem Existenzsatz nach Cartan–Kuranishi muss die $\vartheta$-Eichung festgelegt werden. Die Symmetrie gehört zum gewählten Hintergrund; ein Hintergrund, der von $\vartheta$ abhängt, würde sie brechen. OP5 bleibt offen, die Guards sind unverändert.

## Offene Pflichten und Aussagegrenzen

Die bedingten Cartan- und Kopplungsanalysen liefern keine pauschalen Nachweise regionaler gekoppelter Existenz, vollständiger Gauge-Klassifikation, nativer Massenkoeffizienten oder globaler physikalischer Closure. Für ein bestimmtes Problem die konkrete Quelle und spätere Layer prüfen; dieses Wiki schließt keine OPs. Eine ausführliche Darstellung, woran die Arbeit hängt, steht unter [Offene Probleme](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Offene-Probleme); alle Vorab-Tests unter [Vorhersagen und Tests](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Vorhersagen-und-Tests).

Die 4.10-Basis hält fest: $R_{\mathrm{glob}}=(0,1,1,1,1)$, $\Gamma_{\mathrm{guard}}=(1,1,1,1,1)$, $\beta_4=\frac{1}{256}$ unverbraucht. Die jüngsten Layer melden unveränderte Guard-Vektoren. Dies sind dokumentierte Projektregister, kein vom Wiki unabhängig geprüftes Zertifikat. $C_5=0$, $C_6/T_2$, globaler Photon-Clock/RH-Satz und globale All-Readout-Closure werden dadurch nicht hergeleitet.

Organisatorische Nachverfolgung: [GitHub Issues](https://github.com/Moriarty1982/QuantumSphere-Unfold/issues). Ein geschlossenes Issue ist für sich kein mathematischer Beweis.
