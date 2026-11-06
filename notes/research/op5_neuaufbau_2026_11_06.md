# OP5 neu aufbauen: vom begründeten Kern zur physikalischen Frage

**6. November 2026. Status: beauftragte Quellenordnung und Neufassung einer Arbeitsfrage, kein neuer Test und kein Abschlussnachweis.** Ausgangsstand: `11674501ff915b46e3a8bfb0d2802c31e4a1309d`, öffentliche Baseline v4.10.0, Forschung bis v4.10.0-r05. Codex-Selbstprüfung; frühere Rechnungen und externe Beweise wurden hier nicht unabhängig wiederholt.

## 1. Arbeitsentscheidung des Autors

Der Autor beauftragte nach der Rückverfolgung der Entstehung von OP5, die bisherige Begründung auszusetzen und die Fragestellung vom unabhängig begründeten Kern neu aufzubauen (Chat vom 6.11.2026: „dann mach das mal“; keine genaue Uhrzeit protokolliert).

**Die bisherige Herleitung des OP5-Problems wird als Grundlage ausgesetzt. Ihre tragenden Annahmen sind teilweise widerlegt und teilweise unbegründet. Die Fragestellung wird deshalb vom unabhängig begründeten Kern aus neu aufgebaut.**

Das ist eine Entscheidung über die aktive Forschungsgrundlage, keine pauschale Widerlegung der gesamten Ausgangsidee. Frühere Runden, Negativresultate und Vorab-Kriterien bleiben bestehen. Insbesondere bleiben H96 offen, H97 widerlegt und W1/W2 eingefroren. Weder die lokale Quelle–Rückweg-Aussage noch das allgemeine kosmologische Konstantenproblem werden damit erledigt. Die Guards werden nicht verändert.

## 2. Vorwissen geprüft

Die Such- und Lesespur umfasst die Begriffe OP5, Λ-cancellation, Θ–R balance, bare Λ, Frame-Auslesung und Quelle–Rückweg in den Originalabschnitten und folgenden Befunden:

| Fundstelle | Befund für die neue Frage |
|---|---|
| `sources/research/parts/v470/23_physical_readouts.tex`, `sec:lambda_cancel` | Ursprüngliche explizite Aufgabe: ein als physikalisch gelesener riesiger Λ-Term soll durch Θ und R auf einen Rest reduziert werden. |
| `sources/research/parts/v470/10_sphaera_and_physics.tex`, `thm:einstein`, `prop:lambda-from-frame` | Spektrale Terme werden Gravitation, Materie und Λ zugeordnet; Frame-Term wird mit Λ identifiziert. Diese Zuordnung ist keine unabhängig gesicherte Grundlage. |
| `sources/research/parts/v480-post-release-layers.tex`, v4.8.0-r03 F3/F4 und Nachprüfung | Λ wird mit verschiedenen Dimensionen verwendet; die Einheiteninterpretation von P4 ist falsch. Die feste Planck-Normalisierung stammt laut interner Nachprüfung aus dem Companion. Das Hauptpaper wurde hier nicht erneut extern geprüft. |
| Dieselbe Datei, v4.8.0-r04/r05 | Riemann-Quelle als Beweisgrundlage zurückgezogen; metrische Wirkung nicht definiert; γ₁² als nackte Λ-Skala unbegründet; konkrete Θ-Summenvermutung widerlegt. |
| `sources/research/parts/v470/22_op_transport_arguments.tex`, `thm:op15-closure` | Bedingter Erhaltungssatz unter Klassenerhaltung, faktorisierender Auslesung und Linearität. Keine Berechnung eines Vakuumterms. |
| `analysis/OP5_QAM_Nulluebergang.md` | Detektor-Null ist im skalaren C5-Testfall keine exakte Null; der Testfall ersetzt nicht die gesamte Architektur. |
| `notes/research/v4_10_0_r26_r31/README.md`, r31 | Flussanteile, stationäre Besetzungen und physikalische Dichten sind verschiedene Größen. |
| `notes/research/v4_10_0_r61/README.md`; `v4_10_0_r63_r64/README.md`, r67/r68 | Frame-/Klassenmischung, Vertauschung von β² zwischen Materieanteil und Λ, offene Herkunft und Zählwahl von β. |
| `sources/research/parts/v410-state-mediator-synthesis.tex` | Gemeinsamer Träger erfordert explizite Vergleichsabbildungen; reduzierte Register verlieren unter anderem Orientierung und Skala. |
| `notes/research/v4_10_0_r80/README.md`; `v4_10_0_r81/README.md`; r01–r05 | Vergleichsmodell und Dynamik beantworten zusätzliche Realisierungsfragen; deren Reichweite und spätere Korrekturen bleiben erhalten. |
| `notes/research/predictions/Vorab_Notiz_H96_Omega_M_beta2.md`; `Ergebnis_H97_Bruecke_DESI_DR2.md` | Heutige Zahl unter benannten Annahmen einerseits, gescheiterte konkrete dynamische Brücke andererseits. |

Einordnung im Gesamtbild: T2/T3 als algebraischer Ausgangspunkt, T14 als Beschreibungssprache, T15 als Scope-Grenze; T1 bleibt physikalische Vermutung, T9 bleibt zu begründende kosmologische Identifikation. T13 liefert keine automatische Dynamik. Die Liste zurückgestellter Ideen wurde geprüft: I3 ist durch den Λ-Bezug berührt, aber in den getesteten Formen bereits gescheitert; I4 scheitert unter den geltenden Lesarten. Eine Wiederaufnahme dieser Ideen folgt aus der Neuordnung nicht. I1/I2 werden hier nicht aktiviert, da weder eine neue Skala noch ein neues Zwei-Kegel-/Projektormodell konstruiert wird.

## 3. Die ursprüngliche Abhängigkeit und ihre Lücke

Historische Kette:

`spektraler Träger → Spurformel → metrische Wirkung → physikalischer nackter Λ-Term → vorgegebener Rest → Auslöschungspflicht (OP5)`.

Bereits der Schritt zur wohldefinierten metrischen Wirkung und ihrer physikalischen Variation fehlt. Auch die Größe des nackten Terms folgt nicht. Der Auftrag, genau diesen Beitrag auszulöschen, ist daher keine etablierte Konsequenz des Kerns. Das ist die Begründung für das Aussetzen dieser Fassung; kein späterer Fit und keine lokale Nullprüfung repariert diesen früheren Übergang.

## 4. Neue Arbeitsfrage

**Welche unabhängig definierte physikalische Messgröße lässt sich durch eine explizite, begründete Auslesung aus dem algebraischen Kern gewinnen, und welche überprüfbare Einschränkung folgt daraus, ohne die historische Λ-Auslöschung vorauszusetzen?**

Noch wird keine bestimmte Messgröße als Ergebnis festgelegt. Eine kosmologische Auslesung bleibt ein möglicher Kandidat, keine Pflicht des Kerns. Die Frage ist ebenso sinnvoll, wenn sich zunächst nur eine mathematische Erhaltungsgröße identifizieren lässt oder wenn für den betrachteten Readout keine physikalische Brücke vorliegt.

## 5. Das dafür nötige Wörterbuch

Für jeden Kandidaten wird zuerst ein kleines, quellenbelegtes Datenblatt angelegt:

| Feld | Was ausdrücklich anzugeben ist | Noch nicht automatisch vorhanden |
|---|---|---|
| Träger | konkrete Zustandsmenge, zulässiger Bereich, Skalare und Ausnahmefälle | physikalischer Zustandsraum allein durch die Algebra |
| Transport | konkrete Hin-/Rückabbildungen und erhaltene Struktur | Realisierung der abstrakten Klassenerhaltung |
| Auslesung | vollständige Abbildung, verworfene Information, Normierung | Rekonstruktion von Orientierung/Skala aus einem reduzierten Register |
| Invariante | welche Größe verglichen wird und welche Zustände sie unterscheidet | Gleichheit vollständiger Zustände oder physikalischer Observablen |
| Messgröße | unabhängige Definition, Einheit, Messprotokoll oder operationaler Vergleich | kosmologische Bedeutung eines Kaskadenlabels |
| Beobachter und Zeit | M/T/P nach Konvention F; explizite Vergleichsabbildung; Epoche und Uhr | Gleichsetzung des Referenzzustands R mit Photon proper |
| Konsequenz | aus den genannten Voraussetzungen folgende Einschränkung | neuer freier Parameter als angebliche Vorhersage |

Dies sind Begriffs- und Nachweispflichten, keine Vorab-Notiz für einen bereits definierten Test. Neue Tests mit Entscheidungskriterien benötigen weiterhin eine eigene freie H-Nummer und einen Commit vor der Rechnung.

## 6. Was als Ausgangspunkt bleibt und was nicht übernommen wird

- Beibehalten: unabhängig definierte Involution und Kompensator im jeweils angegebenen reellen/komplexen Rahmen, Sektorstruktur, explizit bedingter Quelle–Rückweg-Satz und unveränderte Guards.
- Nicht vorausgesetzt: dass ein spektraler Pol ein physikalischer Vakuumterm ist, dass dessen Skala γ₁² oder Planck-groß ist, dass der vollständige Vakuumterm im Photon-Frame verschwinden muss oder dass ein Rest zwingend β² beträgt.
- Ebenfalls nicht vorausgesetzt: Übergangswahrscheinlichkeit = Besetzung = Energiedichteanteil; Detektor-Null = exakte Null; mathematisches Frame-Label = physikalischer Beobachter.
- H96 bleibt als bestehende, getrennte empirische Hypothese mit ihren ursprünglichen Kriterien bestehen. Die Neuordnung liefert ihr keinen zusätzlichen Beweis und keine neue Datenbestätigung.

## 7. Konkreter nächster Schritt

Zuerst das vorhandene Quelle–Rückweg-Paket aus `21_inflow_and_transport_statement.tex` und `22_op_transport_arguments.tex` instanziieren: für genau eine bereits im Text definierte Route Träger, Transport, Auslesung und Invariante mit ihren Fundstellen zusammentragen. Jede dort nur angenommene Größe bleibt als Annahme markiert. Erst danach prüfen, ob dieses Paket überhaupt eine Verbindung zu einer unabhängig definierten Messgröße enthält.

Dieser Schritt verwendet keine neue Wirkung, keine neuen Gewichte und keinen neuen Nullbegriff. Findet sich keine konkrete Instanz, lautet der Befund „abstrakter bedingter Satz; physikalische Brücke fehlt“, nicht „OP5 geschlossen“ und nicht „physikalische Theorie widerlegt“.

## 8. Reichweite und Dokumentstatus

Dies ist eine neue Arbeitsnotiz zur beauftragten Neuformulierung, noch keine nummerierte Forschungsschicht und kein neues Theorem. Die historische Quellenkette bleibt lesbar. Die Übernahme in eine spätere Runde erfolgt gesondert nach der Projektanleitung. Keine Änderung an veröffentlichten TeX-/PDF-Payloads, keine Änderung von Γ_guard, R_glob oder β₄, kein Merge auf main.
