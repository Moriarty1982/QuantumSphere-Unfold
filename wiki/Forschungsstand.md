# Forschungsstand

**Quellenstand: 28.10.2026, Commit b12adf5.** Diese Seite fasst dokumentierte Statusaussagen zusammen; sie ist kein neuer Beweisaudit. [Quellenkarte](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Versionen-und-Quellen).

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
- Drei Fehler im Hauptkorpus sind als Kandidaten für Statusnotizen vermerkt: `rem:regularization-B` (Reihenentwicklung und Vorzeichen des Gegenterms; Wert 1,689 statt 0,940), `thm:dirac-probe` und `prop:three-compatible-readings` stützen die Uhrskala noch auf das archivierte `thm:gue-selfdet`, und das Korollar „Cosmological constant revisited“ gibt für dieselbe Größe null und $\gamma_L^5$ an.

OP5 bleibt in der exakten Form offen; die lokale Detektorschließung $\mathrm{OP5}_{\mathrm{eff}}$ ist davon nicht berührt.

## Offene Pflichten und Aussagegrenzen

Die bedingten Cartan- und Kopplungsanalysen liefern keine pauschalen Nachweise regionaler gekoppelter Existenz, vollständiger Gauge-Klassifikation, nativer Massenkoeffizienten oder globaler physikalischer Closure. Für ein bestimmtes Problem die konkrete Quelle und spätere Layer prüfen; dieses Wiki schließt keine OPs.

Die 4.10-Basis hält fest: $R_{\mathrm{glob}}=(0,1,1,1,1)$, $\Gamma_{\mathrm{guard}}=(1,1,1,1,1)$, $\beta_4=\frac{1}{256}$ unverbraucht. Die jüngsten Layer melden unveränderte Guard-Vektoren. Dies sind dokumentierte Projektregister, kein vom Wiki unabhängig geprüftes Zertifikat. $C_5=0$, $C_6/T_2$, globaler Photon-Clock/RH-Satz und globale All-Readout-Closure werden dadurch nicht hergeleitet.

Organisatorische Nachverfolgung: [GitHub Issues](https://github.com/Moriarty1982/QuantumSphere-Unfold/issues). Ein geschlossenes Issue ist für sich kein mathematischer Beweis.
