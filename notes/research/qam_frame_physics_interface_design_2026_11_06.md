# Entwurf: QAM als Frame-Schnittstellensprache mit framegebundenem Physikmapping

**6. November 2026. Eigenständige Quellenlektüre und Schnittstellenentwurf durch einen gesonderten Codex-Agenten.** Basis `4ab1a9e063a4b6ce975c84b5a1c4cd4471938465`. Auftrag des Autors: QAM erneut genau lesen und als Frame-Schnittstellensprache entwerfen; die ART und ihr Physikmapping gelten im ausdrücklich zugeordneten Frame. Dies ist kein neuer physikalischer Test, kein Beweis der Einheitshypothese und keine Änderung vorhandener QAM-Axiome. Die konkrete ART-Belegung unten ist ein Entwurf auf Basis der vorhandenen Grammatik, keine Behauptung eines bereits implementierten ART-Adapters.

## 1. Ergebnis der erneuten Lektüre

Die Nutzerbeschreibung passt zu einer bereits ausdrücklich vorhandenen Rolle von QAM. Die zweiseitigen Tensoranzeigen kennzeichnen links Frame, Beobachter, Sprache oder Readout und rechts Struktur, Feld, Operator oder Transport. Gewöhnliche Tensorrechnung wird nicht ersetzt. Eine framegebundene physikalische Interpretation kann deshalb die bekannten ART-Tensoren und ihre Operationen übernehmen, ohne eine zweite Tensoralgebra oder eine Herleitung der ART aus QAM zu verlangen.

Zu trennen sind dabei drei Aufgaben:

1. **QAM-Schnittstelle:** Auf welchem Träger, in welcher Rolle und mit welchem Frame wird ein Objekt oder eine Beziehung verwendet?
2. **Physikmapping eines Frames:** Welche gewöhnlichen mathematisch-physikalischen Objekte und Gesetze interpretiert dieses Profil?
3. **Verbindung zweier Frames:** Welche ausdrücklich deklarierte Abbildung verbindet ihre Objekte, Readouts oder Vergleiche, und auf welchem Bereich?

Der ART-Frame ist kein universeller Maßstab, den QAM allen anderen Frames aufzwingt. Ein Transport zu einem anderen Frame importiert dessen ART-Bedeutung nicht automatisch. Umgekehrt ist ein korrektes lokales ART-Mapping keine Ableitung der ART aus QAM. Das ist keine neue Einschränkung der Sprache, sondern ihre saubere Anwendung.

## 2. Quellen und genaue vorhandene Semantik

Alle Pfade relativ zum Repository; Labels sind gegenüber beweglichen Zeilennummern maßgeblich.

| Quelle / Locator | Bereits definierter Inhalt | Folgerung für diesen Entwurf |
|---|---|---|
| `sources/parts/01_qam_mml_mma_pre_v4_infrastructure/04_qam_predicates_transport_shell.tex`, Prädikat- und Relationsblock, `def:qam-closure-compatible-readout` | markierte Mengen-/Tupelcodes; `QState`, `QLayer`, `QOp`, `QReadout`; Beziehungen `QAdmTransport`, `QClEq`, `QRead` | Gegenstandsart und Anwendungssemantik lassen sich trennen; `QRead` allein ist keine physische Messkopplung |
| gleicher Ordner, `02_store_array_and_pre_v4_readouts.tex`, `def:two-sided-structural-tensor-interface` | Anzeige `{}^{A}{}_{B}T^{i}{}_{j}`; Frontrollen Frame/Readout/Sprache/Beobachter, Backrollen Struktur/Feld/Aktion | Die Front muss nicht ausschließlich aus zwei verschiedenen physischen Frames bestehen |
| ebenda, `def:two-sided-admissible-contractions`, `prop:two-sided-conservative-expansion` | gewöhnliche Ober-/Unterindexpaarung; explizite Vergleichstensoren und Selektoren; Expansion in gewöhnliche Rollendaten | Keine zweite Tensorrechnung nötig; ein gleichdimensionierter Raum wird nicht still identifiziert |
| ebenda, `ex:two-sided-hc-mm-sandwich` | Beispiel `{}^{R}{}_{Ω}M^{i}{}_{j}` als Readout-/Strukturschnittstelle | eine konkrete Frontbelegung muss deklariert werden, nicht erraten |
| gleicher Ordner, `03_two_sided_tensor_masks_and_freeze.tex`, `def:r03-two-sided-role-erasure-map`, `prop:r03-role-erasure-normal-form` | Erasure expandiert Front-/Backrollen in QAM-Daten; Guards, Vergleiche, Selektoren und Provenienz bleiben erhalten | Rollenerasure ist keine physikalische Interpretation oder Verlust physikalischer Geltungsbedingungen |
| ebenda, `def:r03-guarded-mixed-readout-normal-form`, `prop:r03-mask-filter-conservativity` | explizite Readouts, Kompatibilität, Aggregation und Masken; Masken ändern keine Payloads | Mischungen erhalten keine stillen gemeinsamen Physikgesetze |
| gleicher Ordner, `05_qam_tensor_admissibility_translation.tex`, Tensorformation und Zulässigkeit | Tag 7 ist kontrollierte Komposition von QAM-Objekten, noch keine vollständige Tensoralgebra | ein gewöhnlicher ART-Tensor als Payload ist nicht allein deshalb ein neuer primitiver QAM-Tensortyp |
| `sources/research/parts/v470/07_qam_infrastructure.tex`, dieselben zweiseitigen Labels | in der Forschungsfassung mitgeführte Primärdefinitionen | Entwurf schließt an den geltenden Quellenbestand an |
| `paper/qam/s2_language.tex`, Frames und zweiseitige Anzeige; `s5_case.tex`, Übersetzungstabelle | frameindizierte Größen; Beispiel `{}^{T}{}_{M}J^{i}{}_{j}z^j`; Spalten erklären Quelle/Ziel und Strukturrolle | explizite physikalische Zuordnungen können in der Schnittstelle sichtbar gemacht werden; das alte konkrete J-Beispiel ersetzt nicht spätere Framekorrekturen |
| `paper/qam/s4_lean.tex`, Routes | je Route ein Modell; Kompositionsgesetz ausdrücklich als Annahme | weder universelle Invertierbarkeit noch identische Physik aller Frames ist Sprachvoraussetzung |
| `qam/README.md` und `paper/qam/s7_limits.tex` | aktuelle TeX-/Lean-Prüfung von Framepfaden, Inputs, Herkunft und Status; nur deklarierte Angaben werden geprüft | Implementierungsumfang ist kleiner als die mögliche mathematische Ausdrucksfähigkeit |
| `scripts/qsc_audit/TENSOR_GRAMMAR.md`, Inputs/Operationen/Grenzen | explizite Indexräume und Rollen, lokale Paarungsprüfungen, Vergleichstensoren; kein vollständiger Formelauswerter | ein ART-Adapter kann die vorhandenen Rollen weiterverwenden; vollständige ART-Semantik ist damit noch nicht ausgeführt |

Die alte Benennung M/T/P bleibt nach Konvention F zu lesen. Der folgende Name `F_ART` ist zunächst ein Profilname. Eine Gleichsetzung `F_ART = M` wäre eine zusätzliche ausdrücklich zu treffende Projektbelegung, keine durch QAM oder diesen Entwurf erzwungene Tatsache.

## 3. Was ein Frame-Physikprofil festlegt

**Entwurfsbezeichnung, kein neuer primitiver QAM-Tag:** Ein Profil `Phys[F]` ist eine versionierte Zusammenstellung bereits speicherbarer Objekte und Beziehungen:

- Profil-/Framekennung und Geltungsbereich;
- zugelassene Träger und ihre gewöhnlichen mathematischen Typen;
- Bedeutungszuordnung für Symbole, Konstanten, Indizes und Operationen;
- verwendete Konventionen, etwa Einheiten, Signatur und Krümmungsvorzeichen;
- darin geltende Gleichungen, Definitionen und externe Modellannahmen mit ihrem Begründungsstatus;
- benannte Readouts, Auswertungsbereiche und gegebenenfalls Messkalibrierungen;
- optional deklarierte Verbindungen zu anderen Profilen, mit eigener Reichweite.

Das ist ein **Wörterbuch mit Geltungskontext**, kein universelles Naturgesetz. Ein Frame kann hier ein Physik-/Ausleseprofil bezeichnen. Ein gewöhnlicher Koordinatenchartwechsel innerhalb der ART ist eine andere Achse und wird nicht mit einem Wechsel von `Phys[F]` gleichgesetzt. Bei Bedarf werden beide Achsen getrennt benannt; die aktuelle Software behandelt solche Kombinationen zunächst über ausdrücklich benannte Frames/Maps.

Auch „operator“ ist nicht automatisch „Dynamik“, und `QRead(r,s,w)` ist nicht automatisch ein Messgerät: Ein physisches Instrument benötigt in dem Profil seine eigene Interpretation. Eine rein mathematische Interpretation einer Tensorformel benötigt dagegen keine neu erfundene Messdynamik.

## 4. Konkretes ART-Profil ohne neue ART

Wir wählen für das Beispiel ein gewöhnliches klassisches ART-Modell auf einem vierdimensionalen Mannigfaltigkeitsbereich U mit hinreichend glatter Lorentzmetrik g und ihrer Levi-Civita-Verbindung. Signatur, Krümmungsdefinition, Einheiten und die Regularität der tatsächlich benutzten Formeln sind Teil des Profils. Beispielsweise reichen für die punktweise klassische Krümmungsformel lokale C²-Metrikkomponenten; stärkere Sätze können stärkere Voraussetzungen benötigen.

Das Profil ordnet zu:

| QAM-Payloadsymbol | Interpretation in `Phys[F_ART]` |
|---|---|
| `g` | gewöhnliche Lorentzmetrik, kovarianter Rang-2-Tensor |
| `g_inv` | die zugehörige inverse Metrik, kontravarianter Rang-2-Tensor |
| `Ric` | Ricci-Tensor der im Profil festgelegten Verbindung/Krümmungskonvention |
| `R_scalar` | gewöhnliche Kontraktion `g_inv^{αβ} Ric_{αβ}` |
| `Ein` | Einstein-Tensor `Ric − (1/2) R_scalar g` |
| `T` | Energie-Impuls-Tensor des im Profil angegebenen Materiemodells |
| `Lambda`, `G_N`, `c` | Skalare mit ihren gewöhnlichen im Profil festgelegten Dimensionen und Bedeutungen |
| `+`, Skalarprodukt, Kontraktion, `=` | die gewöhnlichen mathematischen Operationen auf diesen Objekten |

Die Verbindung zwischen `g`, `Ric`, `R_scalar` und `Ein` wird mit importiert. Sie sind nicht voneinander unabhängige beliebige Arrays. Es ist keine neue Herleitung der ART erforderlich, um diese vorhandene Modellgleichung in diesem Frame auszudrücken:

\[
G_{\mu\nu}(g)+\Lambda g_{\mu\nu}
=\frac{8\pi G_N}{c^4}T_{\mu\nu}.
\]

„Gilt im Profil“ heißt hier: als Feldgleichung dieses Physikmodells mit den angegebenen Voraussetzungen aufgenommen. Es erklärt weder die ART zur voraussetzungslos bewiesenen Aussage noch reduziert es ihre etablierte Physik auf eine uninterpretierte neue QAM-Hypothese. Der genaue Belegstatus wird übernommen, nicht durch die Übersetzung erhöht oder abgesenkt.

## 5. ART mit wirklich deklarierten zweiseitigen Indizes

Die Quellen legen keine einzige zwingende Belegung aller Frontslots fest. Daher wird für den Entwurf **eine konkrete erlaubte Belegung** gewählt:

- links oben `F_ART`: Ziel-Frame des Physikreadouts;
- links unten `L_ART`: Eingangsprofil der gewöhnlichen ART-Tensorsprache/Payloads;
- rechts `μ,ν`: kovariante Struktur-/Feldindizes im Kotangentialraum des angegebenen U;
- Frontslots sind hier **Frame-/Sprachrollen**, keine Raumzeitindizes;
- `F_ART` und `L_ART` sind in der Gleichung feste freie Rollenbezeichnungen. Es wird nicht über Physikframes summiert.

Die zweiseitige Darstellung einer solchen Payload ist damit

\[
{}^{F_{\mathrm{ART}}}{}_{L_{\mathrm{ART}}}\mathcal X_{\mu\nu}.
\]

Sie sagt: „die gewöhnliche kovariante Tensorpayload X, interpretiert durch das ART-Sprachprofil im Frame F_ART“. Der untere Frontslot ist **kein behaupteter zweiter physischer Quellframe**. Er ist gemäß Primärdefinition eine Sprach-/Readout-Eingangsrolle. Das ist gerade der Unterschied zur gesonderten Transportanzeige `{}^{A}{}_{B}K` mit zwei physischen Framekennungen.

Für die ART-Gleichung gibt es zwei gleichwertige Darstellungsstufen:

**Ganzes Gleichungsobjekt:**

\[
{}^{F_{\mathrm{ART}}}{}_{L_{\mathrm{ART}}}
\left[\mathcal G_{\mu\nu}+\Lambda\mathcal g_{\mu\nu}
-\frac{8\pi G_N}{c^4}\mathcal T_{\mu\nu}=0\right].
\]

Die Klammer ist eine Gleichungspayload, auf die das deklarierte Interpretationsprofil angewendet wird; die Frontindizes sind kein neu erfundener Multiplikationsoperator.

**Ausgeschriebene tensorielle Terme im selben Profil:**

\[
{}^{F_{\mathrm{ART}}}{}_{L_{\mathrm{ART}}}\mathcal G_{\mu\nu}
+{}^{F_{\mathrm{ART}}}\Lambda\,
{}^{F_{\mathrm{ART}}}{}_{L_{\mathrm{ART}}}\mathcal g_{\mu\nu}
= {}^{F_{\mathrm{ART}}}\!\left(\frac{8\pi G_N}{c^4}\right)
{}^{F_{\mathrm{ART}}}{}_{L_{\mathrm{ART}}}\mathcal T_{\mu\nu}.
\]

Die Skalare tragen hier zur Lesbarkeit nur die Framekennzeichnung; ihre Sprachprofile stehen im gemeinsamen Kontext. Alle drei Rang-2-Terme haben dieselben freien Frontrollen und dieselben beiden kovarianten Backslots. Addition und Gleichheit sind daher innerhalb dieses deklarierten Profils die gewöhnlichen Operationen.

Eine Kontraktion rechts verwendet wie gewohnt z.B. `g^{αβ} Ric_{αβ}`. Das inverse g ist dabei der explizite Vergleichstensor; es wird keine rohe Unterindex-/Unterindex-Summation eingeführt. Indexräume müssen übereinstimmen, nicht nur dieselbe Dimension haben.

Diese Formeln sind ein semantischer Notationsentwurf. Sie sind nicht als bereits ausführbare `qam.sty`- oder JSON-Formelsyntax ausgegeben. Die linke Sprachrolle kann in einer anderen Implementierung als Profilmetadatum geführt und im Druck unterdrückt werden; ihre Bedeutung darf dabei nicht verloren gehen.

## 6. Was „1:1 mappen“ für dieses Beispiel präzise heißt

Auf einem festgelegten Teilbestand gewöhnlicher ART-Ausdrücke gibt es eine Kodierung `Enc_F` in die QAM-Rollenanzeige und eine Interpretation `Phys_F` zurück in das gewöhnliche Modell. Der lokale Vertrag ist:

\[
\operatorname{Phys}_F(\operatorname{Enc}_F(e))=e,
\]

gegebenenfalls bis auf ausdrücklich zugelassene harmlose Notationsnormalformen, etwa gebundene Indexnamen. Bedeutungen, Definitionsbereich, Konventionen und Annahmen bleiben dieselben. Der Rückweg ist nur auf dem deklarierten Bild der Kodierung verlangt; er macht nicht jede mögliche QAM-Payload zu einer ART-Formel.

Die Übereinstimmung der gewöhnlichen Addition, Kontraktion und Krümmungskonstruktion folgt für dieses Beispiel daraus, dass das Wörterbuch genau diese Operationen interpretiert. Das ist **kein allgemeines Linearitätsaxiom für alle QAM-Readouts oder physikalischen Framewechsel**. Insbesondere wird die nichtlineare Abhängigkeit G(g) nicht durch eine willkürliche lineare Abbildung auf beliebige Arrays ersetzt.

Die vorhandene **Rollenerasure** ist eine weitere, andere Expansion: Sie übersetzt die visuelle Front-/Backanzeige in explizite QAM-Rollendaten. Sie muss Guards, Maps, Selektoren und Provenienz erhalten. Sie ist nicht der ART-Decoder `Phys_F`.

Auch Bytegleichheit von Kodierungen oder Hashes ist weder physikalische Äquivalenz noch ein Wahrheitsbeweis. Umgekehrt können verschiedene syntaktische Formen dieselbe gewöhnliche Gleichung bedeuten.

## 7. Inter-Frame-Schnittstellen bleiben gesonderte Objekte

Ein Übergang von einem Frame B nach A wird etwa durch einen deklarierten Operator-/Readoutcode `K_{A←B}` mit seinem Definitionsbereich und Zieltyp beschrieben. Die passende Anzeige kann wirklich zwei physische Frontslots tragen:

\[
{}^{A}{}_{B}\mathcal K^{i}{}_{j}.
\]

Hier sind i,j die konkret deklarierten strukturellen Eingangs-/Ausgangsslots. Ob K linear, nichtlinear, partiell, invertierbar, selektiv, nur vergleichend oder informationsreduzierend ist, gehört zum jeweiligen Mapping. Aus der Anzeige folgt keine dieser Eigenschaften.

Eine nichtlineare oder partielle Abbildung wird in ihrer Expansion durch passende Graph-/Readoutdaten beschrieben. Die tensorartige Kurzschreibweise behauptet dann nicht, sie sei bereits ein gewöhnlicher linearer Rang-(1,1)-Tensor. Eine solche Tensorinterpretation wäre gesondert zu deklarieren.

Ein ART-Gleichungsrecord im Frame F_ART kann nur über einen ausdrücklich deklarierten passenden Übergang in einen anderen Frame übernommen werden. **Dass dort dieselbe ART-Gleichung mit derselben Interpretation gilt, ist keine sprachliche Voreinstellung.** Der Übergang kann dort eine anders interpretierte Relation, eine eingeschränkte Aussage oder nur einen Vergleichswert liefern.

Ein Kommutativitätsdiagramm zwischen zwei Physikprofilen wird nur für den jeweils behaupteten Vergleich verlangt. Beispielsweise muss ein gewöhnlicher ART-Koordinatenwechsel innerhalb desselben Profils die schon geltende Tensorbedeutung erhalten. Ein physikalisch anders gemappter Frame braucht dagegen seinen eigenen Vertrag. Ebenso verlangt QAM nicht universal `K_{B←A}K_{A←B}=I`; falls ein Rückweg nur eine Closure-Klasse oder ein bestimmtes Readout erhält, muss genau diese schwächere Relation benannt werden.

Die Einheitshypothese kann später einen gemeinsamen Träger und zwei framegebundene Readouts verlangen. QAM kann diese Aufgabe ausdrücken. Die Sprache selbst erzwingt weder die Existenz eines solchen gemeinsamen physischen Objekts noch universelle Gleichheit aller Energiebegriffe zwischen den Profilen.

## 8. Status und Herkunft ohne Physikverlust

Für das ART-Beispiel werden getrennt verzeichnet:

- Definitionen des ART-Profils und der Notationskodierung;
- importierte mathematische Aussagen mit ihren Voraussetzungen;
- die als Modellgleichung verwendete Einstein-Gleichung;
- empirische Referenzen und Kalibrierungsdaten, soweit benötigt;
- eine eventuell nur bedingte inter-frame physikalische Interpretation;
- der Nachweis beziehungsweise die Prüfung der konkreten Übersetzung.

Ein korrekter Übersetzungsnachweis kann mathematisch bewiesen sein, während eine zusätzliche physikalische Identifikation zwischen Frames weiterhin hypothetisch ist. Das sind verschiedene Claims. Sie sollten nicht in einen einzigen globalen Wahrheitsstatus gedrängt werden. Der aktuelle Checker bietet eine grobe Statusordnung und Eingabeherkunft; dies ersetzt keine inhaltliche Prüfung der Zuordnung.

## 9. Was die vorhandene Software schon kann und was minimal fehlt

| Teil | Bereits vorhanden | Kleinste Ergänzung für das Beispiel |
|---|---|---|
| Träger und Payloads | QAM-Tupel-/Objektkontext, Graphen und Relationen | konkrete Profil-/Objektbelegung der ART-Daten |
| Front-/Backrollen | Quellgrammatik und JSON-Indexslots | Rollen F_ART/L_ART und lokale Raumzeitindexräume deklarieren |
| gewöhnliche Tensoren | können als bekannte mathematische Objekte/Payloads geführt werden | Bedeutungsschlüssel zu g, Ric, Ein, T und Konstanten dokumentieren |
| Ausdruckssemantik | keine allgemeine automatische Formelauswertung im aktuellen Rollenprüfer | für eine ausführbare Fassung Referenz auf vorhandene Tensorrepräsentation oder begrenzten Adapter festlegen; keine neue universelle Algebra nötig |
| Framepfade | TeX-/Lean-Mapdeklarationen und Konversionen | nur tatsächlich verwendete Übergänge eintragen |
| Rollenprüfung | lokale Kontraktion, Vergleiche, Masken | Beispielrollen prüfen; vollständige Ausdrucksprüfung bei Bedarf gesondert implementieren |
| Herkunft/Status | QAM-Register, Quellenlinks, Hashketten | importierte ART-Aussagen von Mapping- und Transportclaims getrennt registrieren |
| Export | Frameworkansicht und `.qam`-Records | ART-Wörterbuch als versionierten Payload-/Profilbestand exportierbar machen |

Es ist weder ein neuer primitiver Tensor-Tag noch ein globaler Namespace-Shift erforderlich, um dieses Beispiel zu schreiben. Ein neuer Formelauswerter wäre eine Implementierungsoption, nicht die Voraussetzung dafür, dass QAM bekannte Physik framegebunden ausdrücken kann.

Die aktuellen Werkzeuge prüfen jedoch nicht bereits die Levi-Civita-Verbindung, die Einstein-Gleichung, sämtliche Indexvorkommen einer ganzen Formel oder die Physik eines Framewechsels. Ihre erfolgreich geprüften Herkunfts-/Rollendaten dürfen nicht als Prüfung dieser Inhalte ausgegeben werden.

## 10. Korrekturen an der bisherigen Gesprächsinterpretation

1. **Zu stark war:** Zum Kodieren bekannter physikalischer Formeln müsse erst eine neue QAM-Tensor-/Formelsprache aufgebaut werden. **Korrektur:** Die bekannte Mathematik kann in einem Frame-Physikprofil direkt interpretiert werden; eine allgemeine ausführbare Formelsyntax ist ein gesonderter Werkzeugausbau.
2. **Zu stark war:** Eine universelle lineare Abbildung müsse die Einstein-Gleichung auf jeden Frame übertragen. **Korrektur:** Nur das lokale ART-Wörterbuch ist hier festgelegt; inter-frame Beziehungen benötigen eigene Maps und Eigenschaften.
3. **Zu eng war:** Frontindex A/B müsse immer „physischer Ziel-/Quellframe“ bedeuten. **Korrektur:** Die Primärdefinition nennt auch Sprache, Readout und Beobachter. Im Beispiel muss die gewählte Rolle pro Slot ausdrücklich sein.
4. **Unzulässig wäre:** Die ART als gemeinsame universelle Außenphysik zur Prüfung sämtlicher Frames vorauszusetzen. **Korrektur:** Sie gilt mit der hier gewählten Bedeutung im bezeichneten Physikprofil. Eine Beziehung zu anderen Profilen wird gesondert formuliert.
5. **Unverändert gültig, aber eng zu lesen:** Frühere Gegenbeispiele zu Projektion, Sättigung, Eigenwertverhältnissen oder festgehaltenen Energiegewichten gelten unter ihren expliziten gemeinsamen Feld-/Operator-/Messkonventionen. Sie sind keine Widerlegung beliebiger anderer framegebundener Physikmappings. Unterschiedliche Bedeutungen dürfen aber auch nicht nachträglich ohne deklarierte Schnittstelle zur Rettung einer konkreten gemeinsamen Behauptung eingesetzt werden.
6. **Unverändert offen:** QAM ist nicht selbst die physikalische Herleitung der Einheitshypothese. Sie ist gerade geeignet, deren gewünschte Mappings und noch zu prüfende Beziehungen klar zu formulieren. Die Hypothese bleibt Forschungsziel, nicht Sprachaxiom und nicht schon widerlegt, weil ein bestimmter Kandidat scheitert.

## 11. Konkreter erster Lieferumfang einer Umsetzung

Ein kleiner ART-Demonstrator würde genau Folgendes liefern:

1. eine Datei für `Phys[F_ART]` mit den oben benannten gewöhnlichen Objekten, Konventionen und geltenden Gleichungen;
2. die eine Einstein-Gleichung als gewöhnliche Payload und als zweiseitige QAM-Anzeige;
3. ein Erasure-Beispiel, das Front-/Backrollen, Geltungsbereich und Herkunft vollständig expandiert;
4. eine Rückübersetzung in exakt die gewöhnliche ART-Gleichung auf dem festgelegten Bereich;
5. einen gesondert deklarierten inter-frame Platzhalter, dessen physikalische Bedeutung offen bleibt, statt ART still zu exportieren;
6. einen Vergleich zwischen dem tatsächlichen Prüfumfang der vorhandenen Werkzeuge und der noch nicht automatisierten Semantik.

Dies ist eine konkrete Schnittstellen-/Dokumentationsaufgabe. Dafür muss keine neue Physik gewählt und kein neuer H-Test vorgetäuscht werden. Der vorliegende Auftrag wurde hier als Entwurf erledigt; kein Adaptercode oder formal bewiesener Physikmapping-Checker wurde behauptet.

## 12. Provenienz und Projektstatus

Quellen wurden in einer separaten Agentenlektüre geprüft; der Entwurf verwendet die jüngste ausdrückliche Nutzerklärung als beabsichtigte Rolle der Sprache. Bekannte Quellentexte und Werkzeuggrenzen sind von den konkreten neuen Belegungen F_ART/L_ART unterschieden. Die Liste zurückgestellter Ideen wurde auf Auslöser geprüft: Es wird kein Zwei-Kegel-/String-, Spin-/C7-, Reservoir- oder Λ-Mechanismus konstruiert, daher hier keine solche Idee als Lösung aktiviert.

Nur diese neue Designnotiz wurde durch den Agenten geschrieben. Keine bestehenden Runden oder Beweise umgeschrieben; keine Veröffentlichung, kein Commit/Push, kein Merge durch diesen Agenten. Wiki-/Übergabeintegration erfolgt gegebenenfalls durch den koordinierenden Agenten. Guards und öffentliche Baseline bleiben unverändert.
