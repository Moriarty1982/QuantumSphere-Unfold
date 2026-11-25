# QAM-Artikel, eigenständige Fassung (Englisch)

*What a Conclusion Rests On: Checked Bookkeeping of Status, Inputs and Frames in Long Research Records*

Entwurf vom 25.11.2026, 26 Seiten mit Anhang. Der Artikel stellt die QAM vollständig in sich dar: Modell, Regeln, Beweise ihrer
Eigenschaften, LaTeX-Paket, Lean-Prüfer, MML/MMA mit Belegen, Prämissengraph, Bandmaschine mit HDL-Vergleich und MCP. Man muss
weder den Companion noch das Physik-Paper kennen. Als durchgehendes Beispiel dient ein Gram-Register unter einem Lorentz-Boost
(E = 2e_x, v = 1/4, Intervall [121/162, 961/1202]), das im Text vollständig hergeleitet wird. Das Spinorband steht in Abschnitt 9 als
bedingte Hypothese, die Frage nach einem Quantenrechner im Träger als gekennzeichnete Spekulation in Abschnitt 11.

Der deutsche Entwurf vom 22.11. unter `paper/qam/` bleibt unverändert; aus ihm sind Modell, Lean-Teil, Maschine, MCP und verwandte
Arbeiten übernommen. Koide-Beispiel und Projektzahlen sind entfallen.

Bauen (der Artikel lädt `qam.sty` und `qam-physics.sty`; seine eigene Akte wird beim Setzen geprüft und nach `main.qam` exportiert):

```sh
cd paper/qam-standalone && sh build.sh
```

`build.sh` setzt dreimal, schreibt `record_snapshot.qam` (Anhang C) und prüft die Hashes mit `qamhash.py`. Der Workflow
`qam-paper.yml` baut den Artikel und prüft `main.qam` zusätzlich mit dem Lean-Prüfer `qamcheck`.

| Datei | Inhalt |
|---|---|
| `main.tex` | Präambel, Zusammenfassung |
| `s1_introduction.tex` | stille Übergänge, Beiträge, Zuse und Turing |
| `s2_example.tex` | das Beispiel: Gram-Register unter einem Boost |
| `s3_model.tex` | Akte, Frames, Eintrag, Status, Regeln R1–R4, Hash-Kette |
| `s4_properties.tex` | Sätze mit Beweisen: keine Beförderung, Eingaben, Frames, Hash-Verweise |
| `s5_frames.tex` | Frames als Schnittstelle (`qam-physics.sty`), live geprüft |
| `s6_latex.tex` | `qam.sty`, Fehlermeldungen, Export, drei Prüfer, live geprüft |
| `s7_requests.tex` | MML/MMA, drei Ausgänge am Beispiel, Beleg, abstrakte Maschine |
| `s8_graph.tex` | SQLite-Prämissengraph |
| `s9_tape.tex` | Bandmaschine, HDL-Vergleich, Spinorband-Hypothese |
| `s10_llm.tex` | MCP, Halluzination als Statusfehler |
| `s11_related.tex` | verwandte Arbeiten, Grenzen, Ausblick Quantenrechner, Schluss |
| `a_lean.tex`, `a_reproduction.tex`, `a_record.tex` | Anhänge |
