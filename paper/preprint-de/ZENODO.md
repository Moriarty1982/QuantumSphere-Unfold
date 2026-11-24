# Zenodo-Angaben zur Fassung 0.3.0

**Status:** reserviert am 24.11.2026 (Entwurf 24497991, Version-DOI 10.5281/zenodo.24497991, auf der Titelseite eingetragen); nicht hochgeladen, nicht veröffentlicht. Eine neue Zenodo-Version entsteht nur mit ausdrücklicher
Freigabe des Autors (`AGENTS.md`). Concept-DOI 10.5281/zenodo.24405552; vorige Fassung 0.2.0 (23.11.2026, 55 Seiten),
[Record 24481107](https://zenodo.org/records/24481107), DOI 10.5281/zenodo.24481107; davor 0.1.0, DOI 10.5281/zenodo.24405553.

**Umsetzung:** Die Metadaten stehen maschinenlesbar in `release/zenodo/metadata_preprint_de_0_3_0.json`, Paket, Änderungsliste (Tests
getrennt von Erkundungen) und Schrittfolge in `release/preprint-de-v0.3.0/README.md`. Fassung 0.3.0 hat 58 Seiten; der lokale Trockenlauf
des Zenodo-Skripts ist bestanden.

## Vorgeschlagene Metadaten
- **Titel:** Quantum Sphaera: Auf dem Weg zu einem gemeinsamen Rahmen für Materie, Eichstruktur und Raumzeitgeometrie
- **Version:** 0.3.0 (Vorschlag)
- **Sprache:** Deutsch; **Typ:** Preprint; **Lizenz:** CC BY 4.0 (wie 0.1.0 und 0.2.0)
- **Schlagwörter:** Quantum Sphaera; mathematische Physik; Heisenberg-Kompensator; Koide-Relation; OP5; QAM; Barbero-Immirzi-Parameter; Horizontzählung; Cayley-Dickson-Turm; CP-Verletzung
- **Verwandte Werke:** Quantum Sphaera Companion v5.3.0 (DOI 10.5281/zenodo.24434403), „references“; Repository
  github.com/Moriarty1982/QuantumSphere-Unfold, Quellstand zum Zeitpunkt der Veröffentlichung (Commit beim Release eintragen)

## Beschreibung (deutsch)
Dieser deutschsprachige Preprint fragt, was ein Heisenberg-Kompensator leisten müsste, und folgt dieser Frage vom Photon zu einem gemeinsamen mathematischen Träger für Materie, Eichstruktur und Raumzeitgeometrie. Ein Feldbeispiel präzisiert die Rolle der Projektion, die Biquaternionen dienen als Träger, und ein Vergleich mit der Dixon-Algebra grenzt ein, wo ein Generationsindex sitzen kann. Die Massenauslese wird an der Koide-Relation untersucht; das Vorzeichen des Oktantschritts erweist sich als Zeitorientierung der Auslese, die kein Baustein festlegt. Eine Fallstudie zu OP5 verfolgt eine präparierte Materiequelle bis zum geometrischen Achsenkontrast: Der gewöhnliche Beitrag folgt aus der linearisierten Einstein-Gleichung, der gerichtete Kontrast braucht einen Vermittler, den die Vergleichswirkung nicht enthält, und ist im Vakuum nur mit verschwindend kleiner Kopplung verträglich. Der Drehsinn der Auslese erweist sich als Konvention; festgelegt ist nur ein relatives Vorzeichen zwischen Leptonen und Quarks.

Neu gegenüber Fassung 0.2.0 (doi:10.5281/zenodo.24481107): Abschnitt 5.7 „Drehsinn und Turm der Hilbert-Shifts“ nach Runde v4.10.0-r59 des Companion. Er fasst Erkundungen zusammen, die nicht blind sind und nichts prüfen (Nullpunkt der Fläche und Hopf-Wert, Restdrehung als Holonomie, Licht als Vermittler, Lichtgewicht, Λ und Drehrate; Erzeugungsregel des Cayley-Dickson-Turms, diskrete S₃ und Bott-Periode bei den Sedenionen, Koide-Bedingung bei exp(uπ/4), Rückwärtslesung mit N_c = 3, nichtlineares Ursprungsfeld), und zwei vorab festgelegte Tests: H125 (relatives CP-Vorzeichen; Strukturstufe bestätigt, nicht blind; Vorhersage sin δ_PMNS < 0 offen bis spätestens 2035) und H126 (Neutrino-Mischung aus zwei Oktonion-Richtungen; nach dem Kriterium nicht prüfbar). Abschnitt 5.8 nennt den Negativ-Schluss für den Absolutwert von Λ (Runde r56), den Attraktor-Weg der Kaskade (Runde r57, H124: nicht ausgeschlossen, aber Ω_M heute ≈ 0,50 verlangt) und die zeitlich geordnete Oktant-Auslese (Runde r58, H123: trennt die Orientierungen nur für j ∉ 2ℕ, Zählregel verfehlt die Daten); Anhang C zeigt dazu die Originalausgaben, mit Qiskit-Kontrolle. Umfang 58 Seiten.

## Kurzfassung (englisch)
This German-language preprint asks what a Heisenberg compensator would have to do and follows the question from the photon to a common mathematical carrier for matter, gauge structure and spacetime geometry. A field example fixes the role of the projection, biquaternions serve as the carrier, and a comparison with the Dixon algebra narrows down where a generation index can sit. The mass readout is studied at the Koide relation; the sign of the octant step turns out to be a time orientation of the readout that no ingredient fixes. A case study of OP5 follows a prepared matter source to the geometric axis contrast: the ordinary part follows from the linearized Einstein equation, while the directed contrast needs a mediator that the comparison action lacks and is compatible in vacuum only with a vanishingly small coupling. A series of explorations finds the handedness of the readout to be a convention; only a relative sign between leptons and quarks is fixed, and its consequence sin δ_PMNS < 0 stands as an open prediction against future data. All open problems remain open; the article states which assumptions each calculation carries.

## Vor dem Release prüfen
- Literaturlinks pinnen (erledigt: `towerlayer` und SOURCES 5.7 auf 73d6a5d7, Merge von PR #285; `lambdainput` auf 1f7318f5).
- Nach der Reservierung `\versiondoi` setzen, PDF bauen, Seitenzahl hier und im Release-README prüfen.
- Vorschau-PDF auf Zenodo prüfen (Haupt-PDF als Vorschau, keine Abbildung).
