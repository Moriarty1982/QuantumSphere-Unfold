# Begriffe

Diese Kurzbeschreibungen dienen der Orientierung. Mathematische Definitionen, insbesondere von MM, HC und den einzelnen Operatoren, sind in der jeweils verwendeten Quellfassung nachzulesen.

| Begriff | Orientierung und Grenze |
|---|---|
| Readout | Deklarierter Auslese- bzw. Vergleichsmodus. Eine Aussage für einen Modus gilt nicht automatisch für alle anderen. |
| Guard | Explizite Voraussetzung oder Geltungsbedingung. Eine deklarierte Voraussetzung ist noch kein bewiesener Sachverhalt. |
| Residuum | Im jeweiligen Modell geführter Rest bzw. Witness. Bedeutung und Nullbedingung hängen von der Definition ab. |
| Closure / Terminalität | Projektbegriffe mit konkreten Bedingungen; lokale oder endliche Erfüllung nicht zu globaler Erfüllung erweitern. |
| Nativ | Aus den tatsächlichen Projektdefinitionen und Gleichungen identifiziert; ein angenommener Vergleich oder Fit erfüllt dies nicht automatisch. |
| Layer | Benannter Forschungs- oder Korrekturblock. Die Nummer ist weder ein Release noch ein Beweisstatus. |
| Frame | Deklarierter Bezugsrahmen bzw. spezifizierte Konvention; bei Größenübertragungen die genaue Zuordnung prüfen. |

## QAM, MML und MMA in der Werkzeugschnittstelle

Die [Framework-Dokumentation](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/scripts/qsc_audit/FRAMEWORK_INTERFACE.md) beschreibt ihre Rollen:

- **QAM** hält benannte Objekte, Beziehungen, Voraussetzungen, Residuen und Herkunft fest.
- **MML** formuliert begrenzte Anfragen, etwa `EXPORT` oder `SCRUB`.
- **MMA** prüft die unterstützte Anfrage und liefert `continue`, `guard` oder `reject` mit Kontext.

`continue` bedeutet, dass die unterstützten deklarativen Prüfbedingungen passen. Es beweist keine mathematische Zulässigkeit, Äquivalenz oder Closure. Gleiche Hashwerte und Payloads erzeugen keine mathematische Äquivalenzbeziehung.
