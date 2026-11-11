# Version 5: Stand vor der Veröffentlichung

11. November 2026. Bestandsaufnahme der technischen Vorbereitung; keine
neue Beweisprüfung, wissenschaftliche Freigabe oder Veröffentlichung.

## Konkretes geprüftes Entwurfspaket

GitHub-Lauf 43078619869 baut Commit
`875a6adf124d711bb093454bf7ace02c06551a47`.
Die Langfassung umfasst dort 1401 Seiten, die englische Physikfassung 27.
Beide stammen aus Snapshot
`929fa8172dac3418412ab428572f21abb127b8d2b708b43752d06a35933180b6`.
Der lokale Satz umfasst 1402 bzw. 27 Seiten; die Seitenzahl ist abhängig
von der Buildumgebung und ersetzt keinen Inhaltsvergleich.

Beide Buildberichte enthalten Nullwerte für offene Verweise, doppelte
Labels, Rerun-Meldungen und Satzüberläufe. Alle 111 Paketprüfsummen wurden
nach dem Herunterladen geprüft. Die Sichtprüfung der Linux-Ausgabe umfasst
53 Seiten mit den betroffenen Satzbereichen, keine Gesamtsichtung des
Companion. Details zur Inhaltserhaltung stehen im Layoutprüfbericht.

Alle vier PR-Prüfungen von #96 bestanden: Lean, TeX sowie die Linux- und
Windows-Tests. Beide Editionen behalten `incomplete_argument_review=true`;
das Paket behält `publication_ready=false`. Diese Werte sind kein Beweis
einer falschen Aussage, sondern kennzeichnen den offenen Prüfungsumfang.

## Verbleibende Schritte in Reihenfolge

1. Nach ausdrücklicher Autorenfreigabe PR #95 mergen, dann die Basis von
   PR #96 auf main umstellen und dessen Diff und Prüfungen erneut prüfen.
   PR #96 ebenfalls nur nach ausdrücklicher Freigabe mergen.
2. Fachliche Schlussprüfung der ausgewählten Physikargumentation durchführen:
   Voraussetzungen, Frame-Abbildungen, Modellannahmen und Reichweite jeder
   Schlussfolgerung gegen die Quellen prüfen. Ausgangspunkt ist
   `v5_expanded_physics_editorial_review_2026_11_11.md`; dessen Selbstprüfung
   ersetzt keine unabhängige Begutachtung. Rohimporte bleiben als solche
   gekennzeichnet. Offene Forschung darf veröffentlicht werden, sofern
   Behauptungen und Einschränkungen zutreffend dargestellt sind.
3. Konkrete v5-Metadaten, Änderungsübersicht und Paketbeschreibung erstellen.
   Die Langfassung bewahrt Entwicklung und Prüfprotokolle; die Physikfassung
   stellt die ausgewählte Argumentation einschließlich QAM/MML/MMA-Methode
   eigenständig dar. Die deutsche Lesefassung ist bislang eine zusätzliche
   Lesehilfe und kein drittes automatisch erzeugtes Release-Dokument.
4. Nach Festlegung des Release-Inhalts einen unveränderten Quellstand
   einfrieren, beide PDFs gemeinsam neu bauen und Quellen, Editionen,
   Prüfsummen und Sichtprüfung genau an diesen Stand binden. Das bisherige
   Paket ist ein Entwurf und wird nicht still zum Release umbenannt.
5. Zenodo-Trockenlauf mit den konkreten Dateien und Metadaten prüfen.
   Reservierung, Upload und Veröffentlichung folgen jeweils nur auf die
   dafür erforderliche ausdrückliche Freigabe gemäß Release-Anleitung.
   Erst nach Reservierung wird eine neue Version-DOI eingetragen;
   bis dahin bleibt v4.11.0 die öffentliche Zitationsbaseline.

Es wurden keine OPs geschlossen, keine wissenschaftlichen Guards geändert
und keine Zenodo-Aktionen ausgeführt.

## Nachtrag: fachliche Selbstprüfung

Die vollständige englische Physikfassung samt Anhang wurde im folgenden
Arbeitsblock sequentiell selbst geprüft. Bericht und unveränderlicher
Manuskriptsnapshot: `referee/v5-physics-2026-11-11-pass1/report.md`.
Kein tragender Fehler wurde festgestellt. Dies ersetzt keine unabhängige
Begutachtung. Die beiden lokalen Präzisierungsvorschläge und die Grenze
der Robertson-Quellenauthentifizierung stehen dort; keine Manuskript-
oder Beweisstatusänderung. Die nächste Vorbereitung betrifft Metadaten
und Änderungsübersicht; die bisherigen Merge-/Zenodo-Freigaben bleiben
unverändert erforderlich.
