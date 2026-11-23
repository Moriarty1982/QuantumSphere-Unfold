# Zenodo-Angaben zur Fassung 0.2.0

**Status:** veröffentlicht am 23.11.2026, [Record 24481107](https://zenodo.org/records/24481107), Version-DOI 10.5281/zenodo.24481107, [GitHub-Release](https://github.com/Moriarty1982/QuantumSphere-Unfold/releases/tag/preprint-de-v0.2.0). Eine neue Zenodo-Version entsteht nur mit ausdrücklicher Freigabe des Autors
(`AGENTS.md`). Concept-DOI 10.5281/zenodo.24405552; vorige Fassung 0.1.0 (20.11.2026, 24 Seiten), DOI 10.5281/zenodo.24405553.

**Umsetzung:** Die Metadaten stehen maschinenlesbar in `release/zenodo/metadata_preprint_de_0_2_0.json`, Paket und Schrittfolge
(Reservierung, Titelseite mit Version-DOI, Upload, Veröffentlichung) in `release/preprint-de-v0.2.0/README.md`. Fassung 0.2.0 hat
55 Seiten; der lokale Trockenlauf des Zenodo-Skripts ist bestanden.

## Vorgeschlagene Metadaten
- **Titel:** Quantum Sphaera: Auf dem Weg zu einem gemeinsamen Rahmen für Materie, Eichstruktur und Raumzeitgeometrie
- **Version:** 0.2.0 (Vorschlag)
- **Sprache:** Deutsch; **Typ:** Preprint; **Lizenz:** CC BY 4.0 (wie 0.1.0)
- **Schlagwörter:** Quantum Sphaera; mathematische Physik; Heisenberg-Kompensator; Koide-Relation; OP5; QAM; Barbero-Immirzi-Parameter;
  Horizontzählung
- **Verwandte Werke:** Quantum Sphaera Companion v5.3.0 (DOI 10.5281/zenodo.24434403), „is supplemented by“; Repository
  github.com/Moriarty1982/QuantumSphere-Unfold, Quellstand zum Zeitpunkt der Veröffentlichung (Commit beim Release eintragen)

## Beschreibung (deutsch)
Dieser deutschsprachige Preprint fragt, was ein Heisenberg-Kompensator leisten müsste, und folgt dieser Frage vom Photon zu einem
gemeinsamen mathematischen Träger für Materie, Eichstruktur und Raumzeitgeometrie. Ein Feldbeispiel präzisiert die Rolle der Projektion,
die Biquaternionen dienen als Träger, und ein Vergleich mit der Dixon-Algebra grenzt ein, wo ein Generationsindex sitzen kann. Die
Massenauslese wird an der Koide-Relation untersucht; das Vorzeichen des Oktantschritts erweist sich als Zeitorientierung der Auslese,
die kein Baustein festlegt. Eine Fallstudie zu OP5 verfolgt eine präparierte Materiequelle bis zum geometrischen Achsenkontrast: Der
gewöhnliche Beitrag folgt aus der linearisierten Einstein-Gleichung, der gerichtete Kontrast braucht einen Vermittler, den die
Vergleichswirkung nicht enthält, und ist im Vakuum nur mit verschwindend kleiner Kopplung verträglich.

Neu gegenüber 0.1.0: Abschnitt zum Vorzeichen des Oktantschritts; Abschnitt „Was an einer einzigen Zahl hängt“ (Zählregeln eines
Horizonts, Zufallsabschätzung, Rovelli–Speziale, Holst-Term, Frame-Abbildung J_B, Zählregel als Dimensionsformel); eine Übersicht der
offenen Probleme und ihrer Zusammenhänge; ein Abschnitt zu den Messungen, die die Zahl prüfen (H9, H96, H102, H112, H15, mit
Datenstand 23.11.2026); ein Hinweis zur Arbeitsweise; Anhang B mit den Herleitungen zur OP5-Fallstudie und dem Stand der
Vermittlersuche; Anhang C mit den Rechnungen zu den neuen Abschnitten. Alle
offenen Probleme bleiben offen; der Artikel legt offen, welche Annahmen jede Rechnung mitführt.

## Kurzfassung (englisch)
This German-language preprint asks what a Heisenberg compensator would have to do and follows the question from the photon to a common
mathematical carrier for matter, gauge structure and spacetime geometry. A field example fixes the role of the projection, biquaternions
serve as the carrier, and a comparison with the Dixon algebra narrows down where a generation index can sit. The mass readout is studied
at the Koide relation; the sign of the octant step turns out to be a time orientation of the readout that no ingredient fixes. A case
study of OP5 follows a prepared matter source to the geometric axis contrast: the ordinary part follows from the linearized Einstein
equation, while the directed contrast needs a mediator that the comparison action lacks and is compatible in vacuum only with a vanishingly
small coupling. All open problems remain open; the article states which assumptions each calculation carries.

## Vor dem Release prüfen
- Kopfzeile in `article.tex` von „Entwurf zu Fassung 0.2.0“ auf „Fassung 0.2.0“ setzen, Datum anpassen.
- Links der Literatur auf den Release-Commit pinnen (erledigt: d2020d17, Merge von PR #268 auf `main`; der frühere Pin 852dc9b5 war ein Zwischencommit des PR-Zweigs).
- PDF bauen, Seitenzahl in README und hier nachtragen; Begleitarchiv der Wolfram-Prüfungen neu bauen, falls gewünscht.
- Vorschau-PDF auf Zenodo prüfen (Haupt-PDF als Vorschau, keine Abbildung).
