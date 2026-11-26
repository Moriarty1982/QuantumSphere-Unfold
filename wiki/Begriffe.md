# Begriffe

Diese Kurzbeschreibungen dienen der Orientierung. Mathematische Definitionen, insbesondere von MM (Kompensatormatrix $\mathcal M_{16}$, bis r75 „Millennium-Matrix“), HC und den einzelnen Operatoren, sind in der jeweils verwendeten Quellfassung nachzulesen.

| Begriff | Orientierung und Grenze |
|---|---|
| Readout | Deklarierter Auslese- bzw. Vergleichsmodus. Eine Aussage für einen Modus gilt nicht automatisch für alle anderen. |
| Guard | Explizite Voraussetzung oder Geltungsbedingung. Eine deklarierte Voraussetzung ist noch kein bewiesener Sachverhalt. |
| Residuum | Im jeweiligen Modell geführter Rest bzw. Witness. Bedeutung und Nullbedingung hängen von der Definition ab. |
| Closure / Terminalität | Projektbegriffe mit konkreten Bedingungen; lokale oder endliche Erfüllung nicht zu globaler Erfüllung erweitern. |
| Nativ | Aus den tatsächlichen Projektdefinitionen und Gleichungen identifiziert; ein angenommener Vergleich oder Fit erfüllt dies nicht automatisch. |
| Layer | Benannter Forschungs- oder Korrekturblock. Die Nummer ist weder ein Release noch ein Beweisstatus. |
| Frame | Deklarierter Bezugsrahmen bzw. spezifizierte Konvention; bei Größenübertragungen die genaue Zuordnung prüfen. |
| Ruheframe R, Materie-Frame M, Dual-Frame T, Lichtpunkt P | Namen der vier Frames seit v4.10.0-r69. Ältere Namen: Referenz- bzw. Bezugsframe (R), Tachyon-Frame (T), Photon-Eigenframe (P). Ein Frame ist die Verteilung desselben Felddublett-Zustands auf die zwei Ports des Kompensators: R 1 : 0, M 1 : x, T x : 1, P 1 : 1 mit x = β_sym². |
| Re-Sektor, Im-Sektor | Seit v4.10.0-r69 die Namen für den Sektor der neutralen (c = 0) und der geladenen Leptonen (c = 1): Real- und Imaginärteil derselben Form (H170). Nur für Leptonen, Lesart unter H99. |
| Port | Einer der zwei Ausgänge des Kompensators (Kompensatorport, Partnerport). |
| W1, W2 | Gemeinsame Wirkungen seit r81: Einstein–Cartan mit eigenem Koframe, 16 Weyl-Zustände auf der Dixon-Ablage, U(1) aus der inneren Einheit (W1); dazu ein Higgs-Dublett (W2). Unter benannten Autorentscheidungen, ohne eigene Skala. |
| Tachyonbild einer Wirkung | Seit r83 (H77) nach Lesart B: Die Kinematik wird fortgesetzt (Impulse p ↦ ip, also X ↦ −X), Konstanten und Potentiale bleiben. Die Energieparität (ganzes Bild mit umgekehrtem Vorzeichen) ist ausgeschlossen. |
| Zweite Lesart | Autorentscheidung (r84): Der Tachyon-Anteil ist dasselbe Feld, gelesen durch den vollständigen komplexen Boost mit Rapidität iπ (Spinor S = −iσ_n und Argument Λ(iπ)x), mit holomorph abgebildeter Adjungierter. Ergebnis: Kinetik mit a − b, Potentiale mit a + b. |
| Gebiet G1, G2 | Wo die Lesarten leben: G1 beide auf der ganzen Zeitachse; G2 (Autorentscheidung r85) Tachyon-Lesart vor, Materie-Lesart nach dem Urknall, nur am Urknall verbunden. |
| Epoche τ* | Bei einem Zeitversatz δ ≠ 0 die frühe Epoche, an der die Kinetik der Skalare verschwindet (Strahlung: τ* = β_sym·δ/(1 + β_sym)); dort sind Quantenmoden singulär (H84). |

## QAM, MML und MMA in der Werkzeugschnittstelle

Die [Framework-Dokumentation](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/scripts/qsc_audit/FRAMEWORK_INTERFACE.md) beschreibt ihre Rollen:

- **QAM** hält benannte Objekte, Beziehungen, Voraussetzungen, Residuen und Herkunft fest.
- **MML** formuliert begrenzte Anfragen, etwa `EXPORT` oder `SCRUB`.
- **MMA** prüft die unterstützte Anfrage und liefert `continue`, `guard` oder `reject` mit Kontext.

`continue` bedeutet, dass die unterstützten deklarativen Prüfbedingungen passen. Es beweist keine mathematische Zulässigkeit, Äquivalenz oder Closure. Gleiche Hashwerte und Payloads erzeugen keine mathematische Äquivalenzbeziehung.
