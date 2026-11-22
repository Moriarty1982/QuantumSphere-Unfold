# Quantum Sphaera – Artikel zur Vereinheitlichung

**Lokaler Überarbeitungsentwurf zu 0.1.0** · [Veröffentlichte Fassung auf Zenodo](https://doi.org/10.5281/zenodo.24405553)

Eigenständiger deutscher LaTeX-Entwurf über den gemeinsamen mathematischen Rahmen für Materie, Eichstruktur und Raumzeitgeometrie. Die Fassung ist als einspaltiger Fachartikel in fünf Abschnitte gegliedert. Abschnitt 4.4 verfolgt im linearen OP5-Vergleich eine präparierte Materiequelle bis zum geometrischen Achsenkontrast. Die Quellenidentifikation, die vollständige gewöhnliche Bilanz zweiter Ordnung und die Apparaturantwort sind offene physikalische Schritte.

## Querverweise

- [QuantumSphere-Unfold auf GitHub](https://github.com/Moriarty1982/QuantumSphere-Unfold). Die Arbeitsgrundlage ist der bestätigte [`main`-Stand nach PR #211](https://github.com/Moriarty1982/QuantumSphere-Unfold/commit/f2a4e687273f2ec7f4124d490e696e07c00f387a) vom 20. November 2026.
- [Quantum Sphaera Companion v5.2.0](https://doi.org/10.5281/zenodo.24294648). Der Datensatz enthält Vollausgabe und 30-seitige Physik-Ausgabe. Beide sind im Manuskript gesondert zitiert.
- [Quellennachweis pro Abschnitt](SOURCES.md).
- [Plan für den eigenständigen QAM-Artikel](QAM-ARTIKELPLAN.md).

## Wolfram-Rechenkontrolle

Anhang A der PDF stellt die Eingabeskripte und Originalausgaben der vier ausgewerteten Wolfram-Läufe blockweise nebeneinander. [Prüfbericht mit Skripten und Originalausgaben](audit/wolfram-v0.1.0/README.md). Das [Begleitarchiv](build/wolfram-begleitmaterial-0.1.0.zip) enthält zusätzlich den anhand des Manifests verifizierten Stand der geprüften Veröffentlichung.

## Abbildungen

Die vier Vektorabbildungen sind als [TikZ-Quellen](figures/) in den Artikel eingebunden. Sie zeigen die Feldprojektion, die Gram-Determinante als Funktion der Phase, die beiden OP5-Antwortwege und die führenden Terme am Achsenprofil. Die Plots zeigen die angegebenen mathematischen Ausdrücke.

## PDF bauen

Benötigt werden pdfLaTeX, Babel mit Deutsch, AMS-Pakete, geometry, TikZ, fvextra und hyperref. Im Projektordner `build` anlegen und den folgenden Befehl zweimal ausführen. Falls LaTeX erneut um einen Durchlauf bittet, den Befehl wiederholen.

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build article.tex
```

Das Ergebnis liegt in `build/article.pdf`.
