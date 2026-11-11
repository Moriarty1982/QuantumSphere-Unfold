# Präzisierungen nach der fachlichen Selbstprüfung

11. November 2026. Nachtrag zur unverändert archivierten Selbstprüfung
unter `referee/v5-physics-2026-11-11-pass1/`. Keine neue Forschungshypothese,
kein OP-Abschluss, keine unabhängige Begutachtung.

## Eingriff und fachlicher Abgleich

In der englischen Physikfassung und der deutschen Leseübersetzung sind
die beiden lokalen Hinweise des Berichts umgesetzt:

- Das komplexe Amplitudenpaar des quadratischen Modells ist ausdrücklich
  nichtnullig. Damit ist X_0 positiv und der dortige Quotient definiert.
- Die zyklische Wurzelform wird ausdrücklich für eine nichtnullige
  Übergangs-Gram-Matrix verwendet. Ihre positive Wurzel hat dann positive
  Spur, also a>0; für Q=0 wird kein Koide-Quotient behauptet.
- Im Schur-Beispiel wird die Kopplungsskala ausdrücklich reell gewählt.
  Damit bleiben die geschriebenen mu²-Formeln anwendbar; eine komplexe
  Kopplung würde Betragsquadrate benötigen.

Alle 640 mathematischen Fragmente der englischen Ausgabe stimmen in
derselben Reihenfolge mit dem archivierten Reviewmanuskript überein.
Die Übersetzung erhält dieselben Fragmente, abgesehen von der bereits
vorhandenen Übersetzung einer Tabellenbeschriftung. Die Einschränkungen
stehen als Prosa bei den jeweiligen Definitionen; sie wurden auch in den
deutschen Vorlagen nachgezogen. Originalbeweise und historische Runden
wurden nicht verändert.

Selbstkorrekturlesen umfasst die drei geänderten Sätze und ihre Formeln.
Erneuter kontextueller Abgleich von Titel, Abstract, Einleitung und Schluss
mit diesen Änderungen: Die neuen Voraussetzungen präzisieren die bereits
verwendete nichtnullige/reelle Lesart; es entsteht keine neue physikalische
Behauptung. Die Argumentordnung und die Unterscheidung von J, P_c und
innerer komplexer Struktur bleiben bestehen. Dies ist eine erneute lokale
Selbstprüfung, keine neu ausgeführte unabhängige Prüfung aller Beweise.
Der frühere Report bleibt an seinen alten Snapshot gebunden; dieser Nachtrag
überschreibt dessen Evidenz und Quellenhashes nicht.

## Validierung

- Drei Editionstests erfolgreich, 34,8 Sekunden.
- Gemeinsamer neuer Build: `build/v5-precision-paired-verified/`,
  Langfassung 1402 Seiten, englisches Physikpaper 27 Seiten.
- Beide Abschlussprotokolle: keine undefinierten Verweise, doppelten
  Labels, Rerun-Meldungen oder Satzüberläufe. Alle 111 Paketprüfsummen
  wurden nach dem Build geprüft.
- Deutsche Leseübersetzung neu an die englische Edition gebunden:
  `build/v5-precision-de-final/compile/paper.pdf`, 29 Seiten. Zwei
  Satzläufe, dieselben vier Befundzahlen jeweils null.
- Vergleich der extrahierten Seitentexte mit den vorherigen lokalen PDFs:
  Englisch Seiten 12,14–16 verändert; Deutsch Seiten 14,16–27 verändert
  (einschließlich nachfolgender Umbruchverschiebungen). Alle 17 betroffenen
  Seiten wurden gerendert und in vier Kontaktbögen gesichtet; keine
  Überlagerung, abgeschnittene Formel oder unlesbare Tabellenstelle gefunden.
  Keine erneute Gesamtsichtung der 1402-seitigen Langfassung.
- Ein erster eingeschränkter Satzversuch scheiterte vor dem LaTeX-Start
  am Zugriff auf die vorhandene MiKTeX-Benutzerkonfiguration. Der neue
  Build mit entsprechendem Zugriff war erfolgreich. Das fehlgeschlagene
  Paket wird nicht als erfolgreiche Ausgabe geführt.

Die registrierten Aussagen-/Editionen erhalten neue Inhalts-/Quellhashes.
`publication_ready=false` und `incomplete_argument_review=true` bleiben
bestehen. Die Entwurfsmetadaten und ihr bisheriger Trockenlauf betreffen
weiterhin die ausdrücklich bezeichneten älteren PDFs; der finale Upload
benötigt eine erneute Prüfung seiner konkreten Dateien.
