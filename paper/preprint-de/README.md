# Quantum Sphaera – Artikel zur Vereinheitlichung

**Fassung 0.2.0** veröffentlicht am 23. November 2026: [Zenodo](https://zenodo.org/records/24481107), Version-DOI [10.5281/zenodo.24481107](https://doi.org/10.5281/zenodo.24481107), [GitHub-Release](https://github.com/Moriarty1982/QuantumSphere-Unfold/releases/tag/preprint-de-v0.2.0) · [Fassung 0.1.0](https://doi.org/10.5281/zenodo.24405553) · Concept-DOI [10.5281/zenodo.24405552](https://doi.org/10.5281/zenodo.24405552) · [Zenodo-Angaben](ZENODO.md) · [Release-Paket und Schritte](../../release/preprint-de-v0.2.0/README.md)

Eigenständiger deutscher LaTeX-Entwurf über den gemeinsamen mathematischen Rahmen für Materie, Eichstruktur und Raumzeitgeometrie. Die Fassung ist als einspaltiger Fachartikel in fünf Abschnitte gegliedert. Abschnitt 4.4 verfolgt im linearen OP5-Vergleich eine präparierte Materiequelle bis zum geometrischen Achsenkontrast. Die Quellenidentifikation, die vollständige gewöhnliche Bilanz zweiter Ordnung und die Apparaturantwort sind offene physikalische Schritte.

## Stand im Repository

Am 22. November 2026 aus dem Codex-Arbeitsordner übernommen (Überarbeitungsentwurf vom 20.11., 21:55) und ergänzt um
Abschnitt 3.3.3 „Welches Vorzeichen der Oktantschritt hat“ (H115–H117) und Abschnitt 5.4 „Was an einer einzigen Zahl hängt“
(Wurzelkarte, Zufallsabschätzung, Rovelli–Speziale). Der Artikel wird vor jeder Übergabe auf den Forschungsstand gebracht
(`AGENTS.md`). Eine neue Zenodo-Version entsteht nur mit Freigabe des Autors. Beim Übernehmen wurden die Zeilenenden auf LF
gesetzt; die Hashes in `baseline.json` beziehen sich auf den Codex-Stand.

Nachtrag 22.11.2026: Anhang B (`sections/b-herleitungen-op5.tex`) leitet die Gleichungen der OP5-Fallstudie in Abschnitt 4.4 her
(vom Antriebsoperator bis zur Energiebilanz beim Schalten) und legt die beiden Annahmen offen, den Antriebsoperator und die
Gleichsetzung der Quellen; Wolfram-Prüfung unter `audit/anhang-b/`. Maßgebliche Quelle ist der Companion, Runde v4.10.0-r32
(`notes/research/v4_10_0_r32/`); der Anhang gibt sie wieder.

Nachtrag 23.11.2026: Abschnitt 5.4 nennt die Zählregel als Dimensionsformel (Runde v4.10.0-r53, mit Literatureintrag zur OpenAI-Familie 148),
Anhang B den Strukturunterschied der Auslese zwischen OP1 und OP5 (Runde v4.10.0-r54). Abschnitt 5.6 beginnt mit der Querschnittssicht auf
die offenen Probleme (Runde v4.10.0-r55), ergänzt beim nativen Operator die Orientierung der Zählung (r53) und beim Quellgesetz das Ergebnis
von r54. Die veröffentlichte Zenodo-Fassung 0.1.0 (24 Seiten) bleibt unverändert.

Veröffentlichung 23.11.2026: Fassung 0.2.0 (55 Seiten) ist auf Zenodo erschienen, DOI 10.5281/zenodo.24481107. Tag `preprint-de-v0.2.0`
fixiert den Quellstand des PDFs (Commit 1db863c8); die Repo-Links im Artikel zeigen auf d2020d17 auf `main`. Spätere Änderungen hier
gehören zur nächsten Fassung.

## Querverweise

- [QuantumSphere-Unfold auf GitHub](https://github.com/Moriarty1982/QuantumSphere-Unfold). Grundlage der Fassung 0.1.0 war der [`main`-Stand nach PR #211](https://github.com/Moriarty1982/QuantumSphere-Unfold/commit/f2a4e687273f2ec7f4124d490e696e07c00f387a) vom 20. November 2026; die Links des heutigen Entwurfs sind auf Commit [`d2020d17`](https://github.com/Moriarty1982/QuantumSphere-Unfold/commit/d2020d178a483d1baa7be3871ca2e9d597992059) (Merge von PR #268, Runden bis v4.10.0-r55) gepinnt.
- [Quantum Sphaera Companion v5.3.0](https://doi.org/10.5281/zenodo.24434403). Der Datensatz enthält Vollausgabe und 31-seitige Physik-Ausgabe (Runden bis v4.10.0-r30). Beide sind im Manuskript gesondert zitiert; die späteren Runden zitiert der Entwurf als Forschungsschichten nach v5.3.0.
- [Quellennachweis pro Abschnitt](SOURCES.md).
- [Entwurf des eigenständigen QAM-Artikels](../qam/README.md).

## Wolfram-Rechenkontrolle

Anhang A der PDF stellt die Eingabeskripte und Originalausgaben der vier ausgewerteten Wolfram-Läufe blockweise nebeneinander. [Prüfbericht mit Skripten und Originalausgaben](audit/wolfram-v0.1.0/README.md). Das Begleitarchiv `build/wolfram-begleitmaterial-0.1.0.zip` entsteht beim Bau der Veröffentlichung (nicht im Repository) und enthält zusätzlich den anhand des Manifests verifizierten Stand der geprüften Veröffentlichung. Anhang A deckt die Fassung 0.1.0 ab; die Herleitungen von Anhang B sind unter `audit/anhang-b/` geprüft. Anhang C zeigt die Originalausgaben zu den neuen Zahlen in 5.4 und 5.6 (Runden r52–r54); Skripte und Ausgaben liegen unter `audit/anhang-c/`. Die übrigen späteren Befunde belegen die jeweiligen Companion-Runden.

## Abbildungen

Die vier Vektorabbildungen sind als [TikZ-Quellen](figures/) in den Artikel eingebunden. Sie zeigen die Feldprojektion, die Gram-Determinante als Funktion der Phase, die beiden OP5-Antwortwege und die führenden Terme am Achsenprofil. Die Plots zeigen die angegebenen mathematischen Ausdrücke.

## PDF bauen

Benötigt werden pdfLaTeX, Babel mit Deutsch, AMS-Pakete, geometry, TikZ, fvextra und hyperref. Im Projektordner `build` anlegen und den folgenden Befehl zweimal ausführen. Falls LaTeX erneut um einen Durchlauf bittet, den Befehl wiederholen.

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build article.tex
```

Das Ergebnis liegt in `build/article.pdf`.
