# Ausgearbeitete Physikfassung: redaktioneller Prüfbericht

11. November 2026, Codex. Autorenauftrag: die kurze Physikfassung zu einer
eigenständig lesbaren Argumentation ausbauen. Redaktionelle Synthese und
analytische Erläuterung vorhandener Befunde; keine neue blinde Hypothese,
Simulation, H-Nummer, Messung oder Beweisfreigabe.

## Quellen und Umfang

Sieben Dateien `qam/editions/v5_expanded_*.tex` ergänzen die Einführungen
aus `v5_physics_article.tex`. Jede wird als gehashtes Erklärungsobjekt
registriert und in den passenden Abschnitt aufgenommen. Originale
Rohimporte und historische Runden erhalten dadurch keinen neuen Status.

| Modul | Inhalt und maßgebliche Projektquellen |
|---|---|
| question | Observable Äquivalenz und induzierte Abbildung; Register-Gegenbeispiel und Autonomiekriterium. |
| core | Biquaternionen, Konjugationen, Pauli-Realisierung, elektromagnetische Invarianten und Realifizierung. Companion-Trägerdefinition, HC-Definitionsbereiche, Baez als externer Überblick. |
| method | `qam/lean/QAM/Provenance.lean`, `qam/examples/gram-boost.tex`, `gram-range-rule.qam`, `gram_range_mml.json`: begrenzte Ausführungssemantik und Lorentz-Intervallrechnung. |
| particles | r34/r35 in `sources/research/parts/v490-post-release-layers.tex`: bedingte Leiteralgebra; `generation-coupling.tex`: Seeds, Defektoperator und Spektrums-/Slotunterscheidung. |
| masses | `generation-coupling.tex`, `native-operator-link.tex`, `hc-mass-identification.tex`, `v4110-koide-overlap.tex`; bestehende kuratierte Koide-/HC-Beweise und HC–Koide-Brücke unverändert. |
| geometry | `hc-dynamics-and-geometry.tex`, `cartan-normal-source.tex`: Lift, Gedächtnis, kanonische Reduktion, Wirkungswahl, Koframe, endliche Quellenkompatibilität und bedingte Subsidiärgleichung. |
| limits | `zeta_prime_operator_uncertainty_2026_11_11.md`, `zeta_positive_spectral_packet_2026_11_11.md`, DLMF 27.4.12 und Robertson 1929. |

## Konkret abgerufener MMA-Beleg

Über den schreibgeschützten QAM-Server per Hash abgerufen und geprüft,
nicht neu ausgeführt:

`ee5266bb67739789f1a14b3fcf732afd16184d94b9f090217d8c5003c64ebf8703ffc67262e72a6823e7e9cbdc4610006b41f29c658c6c4845a81e46d96e3722`.

Vollständiger Datensatz: `qam/editions/evidence/gram_interval_receipt.json`.
Anfrage `gram_boost_interval`, READOUT mit `em.gram-boost-range`, Präparation
`E2x-B-unit-yz`, Lab nach Boosted, z-Boost 1/4 und Messintervall [-1/4,1/4].
Ergebnis exakt [121/162,961/1202].

Prämissen: bedingte Vorbereitung `BE014772A536438E3767BBAE3EBC7AE5`, dann
bedingte Lorentz-Regel `7C36EDC97D94E61FF80542EC521D2BC9`. Status continue,
keine zusätzlichen Adapterpflichten, keine fehlenden aufgezeichneten
Prämissen. `closure_proved=false` und `mathematical_relations_proved=false`
bleiben erhalten. Die allgemeine analytische Herleitung steht im Paper;
der Beleg betrifft die konkrete Anfrage und ihren gespeicherten Kontext.

## Grenzen und Selbstprüfung

Die Herleitungen wurden gegen die benannten Projektquellen und im
mathematischen Zusammenhang selbst geprüft. Keine unabhängige Begutachtung
oder formale Gesamtverifikation. Insbesondere bleiben offen:

- Native Leiterdarstellung, Chiralität und elektroschwache Zuordnung;
  die Zählung ist bedingt durch CAR und zyklisches Vakuum.
- Native Übergangsoperation, physikalisches Wurzelgesetz, Normselektion,
  Phase und Massenskala. Die Schur-Auslesung setzt Hermitizität, kanonische
  Normierung und Lücke voraus; ihre nichtnulligen leichten Zustände sind gedresst.
- Präparation und Erhaltung positiver Zustandsbereiche. Zyklizität bestimmt
  keinen Koide-Radius; die Positivitäts- und antipodalen Grenzen bleiben.
- Die autonome Reduktion und ein dissipativer Mechanismus. Reversible
  Amplituden-/Phasenkopplung ist keine Viskosität.
- Regionale Feldexistenz. Endliche Jet-Kompatibilität reicht nicht;
  die Subsidiärgleichung benötigt Konstitutiv- und Sondengleichung auf
  einem offenen Gebiet und beweist deren Fortpflanzung nicht.
- Native Zeta-Präparation, Profilwahl, Energie-/Massenauslesung und Einheiten.
  Der Operatorvergleich gilt bei sigma > 1, nicht auf der kritischen Linie.

Selbstkorrekturlesen: neue Textblöcke und ihr Anschluss. Lokale
mathematische Schreibkorrekturen im Entwurf: Tr[(cI ± D)^2] statt der
mehrdeutigen Tr(cI ± D)^2; explizite 3-mal-2-Beispielmatrix ohne irrtümliche
Transposition. Voraussetzung eta >= 0 beim erneuten Gebrauch wiederholt.
Keine Änderungen an Originalbeweisen oder Altrunden.

## Ausgabe und Prüfung

`build/qam-v5-expanded-final/physics/paper.pdf`: 27 Seiten, davon
24 Argumentation, 1 Literatur und 2 Anhang. Zweimal pdflatex ohne
Shell-Escape. Abschließendes Log ohne Overfull, undefined, Rerun oder
mehrfache Labels. Alle 27 gerenderten Seiten visuell geprüft.
29 Storetests erfolgreich; anschließend alle drei Editionstests nochmals
erfolgreich. Die Integration prüft Quellenbindung der Erweiterungen,
tatsächliche Aufnahme, Wiederholbarkeit und Erhaltung offener Kandidaten.

Physik: `1db88536ab67af7a1087fb999f63ef46ccfb9a0f8d22335c8969cf51a306c1d8`.
Lang: `7dac95aad8d2d2db2e36090a24d298d975f06c24f88a1b0035f9139faa3bc0df`.
Snapshot: `fda9214d02e556594f39696505729fd64e8624055237ecf880d6bafe89d646b4`.

Stand 5.0.0-draft. Kein Main-Merge, Zenodo-Upload, Release oder OP-Abschluss.
Gemeinsamer Zwei-PDF-Releasejob und fachliche Schlussprüfung bleiben separat.
