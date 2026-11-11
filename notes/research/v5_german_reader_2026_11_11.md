# Deutsche Lesefassung der erweiterten Physikfassung

11.11.2026, Codex. Auftrag: vollständige deutsche Version für den Autor.
Keine neue Forschung, Rechnung, Beweisfreigabe oder Statusänderung.

Die Argumentation sämtlicher sieben Abschnitte, Zusammenfassung und neun
Propositionen samt Beweisen wurden ins Deutsche übertragen. Literaturtitel
und technische Kennungen bleiben im Original. Die Quellen stehen unter
`qam/editions/de/`; `sources.json` bindet sie an die englische Physikedition
`1db88536ab67af7a1087fb999f63ef46ccfb9a0f8d22335c8969cf51a306c1d8`.

Erzeugung: `python -m qam.tools.build_v5_german_reader --source ENGLISCHES_PAPER_TEX --out NEUER_ORDNER`.
Beispiel und Verfahren stehen in `qam/editions/de/README.md`. Diese
persönliche Leseübersetzung ist kein eigenes Sprachprofil des
Editionsspeichers. Die englischen Datenbankobjekte bleiben unverändert.

Ausgabe: `build/qam-v5-physics-de-final/paper.pdf`, 29 Seiten, davon
27 Haupttext einschließlich Literatur und zwei Beweisanhang. Ein
`translation.json` mit Quell-, Übersetzungs- und Ausgabehashes liegt daneben.

Prüfungen:

- Alle 640 mathematischen Fragmente der Vorlage vollständig übernommen;
  fehlende oder doppelte Platzhalter brechen die Erzeugung ab.
  Ein zusätzlicher Multimengenvergleich prüft das gesamte Dokument.
- Erst nach diesem Abgleich wird die rein sprachliche Tabellenbeschriftung
  `multiplicity` in `Vielfachheit` übersetzt; keine algebraische Änderung.
- Erneute Erzeugung liefert bytegleichen LaTeX-Text. Eine veränderte
  englische Vorlage wurde zurückgewiesen, bevor ein Ausgabeordner entstand.
- Zweimal pdflatex ohne Shell-Escape; abschließendes Log ohne Overfull,
  undefined, Rerun oder mehrfache Labels.
- Alle 29 Seiten visuell geprüft. Nach den letzten sprachlichen Änderungen
  nochmals gerendert: nur Tabellen- und Literaturseite änderten ihre
  gerenderten Bilder; beide erneut visuell geprüft.

Selbstkorrekturlesen: vollständige neue Übersetzung, Anschluss von Prosa
und Formeln, Voraussetzungen und Negationen, LaTeX-Struktur, Zitate und
Gleichungsnummern. Keine mathematischen Symboländerungen; nur die genannte
Tabellenbeschriftung lokalisiert. Die Beweise wurden nicht neu entworfen
oder unabhängig begutachtet. Offene Guards und physikalische
Identifikationspflichten bleiben wie in der englischen Ausgabe bestehen.
