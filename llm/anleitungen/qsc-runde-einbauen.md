# Anleitung: eine QSC-Runde einbauen

Werkzeugunabhängig. Gilt für das Projekt Quantum Sphaera: lokaler Ordner `Quantum Sphera` des Autors und GitHub-Repo
`Moriarty1982/QuantumSphere-Unfold`.

## Vorher
1. **Stand lesen, nicht raten.** Lokal `AGENTS.md` (Rundentabelle, aktueller Stand) und `git log --oneline -5` ansehen,
   auf GitHub `git log origin/main`. Die letzte Runde steht am Ende von
   `sources/research/parts/v4100-post-release-layers.tex` (Runden bis v4.9.0-r86 in `v490-post-release-layers.tex`).
2. **Doppelte Arbeit vermeiden.** Prüfen, ob die Runde schon existiert: Branch `research/v4.10-rNN-*` oder Commits mit „rNN“.
3. **Neue Tests vorab festschreiben.** Erst die Vorab-Notiz `llm/Vorab_Notiz_HNN_*.md` committen, dann rechnen. Dabei
   prüfen, ob die H-Nummer frei ist.

## Format der Runde
- **Kopf:** `\clearpage`, `\section*{v4.10.0-rNN Source-Only: …}`, `\addcontentsline{toc}{section}{…}` und
  `\label{sec:v4100-rNN-…}` (seit dem v4.10.0-Release am 2026-11-06; die Runden v4.9.0-r01–r86 behalten ihre Namen).
- **Einleitung:** ein Absatz „Purpose“, dann der Source-only-Absatz mit der Version-DOI 10.5281/zenodo.23991357 (v4.10.0) und der
  Concept-DOI 10.5281/zenodo.19210728 (beide unverändert).
- **Ergebnisse:** jeweils als `Theoremlet v4.10.0-rNN.k` mit Beweisskizze oder Messung. Widerlegte Tests als solche
  benennen, Korrekturen früherer Aussagen ausdrücklich machen.
- **Frames:** eigener Unterabschnitt `subsec:v4100-rNN-frames` (Tabelle M/T/P).
- **Register und Ledger:** Guards Γ_guard = (1,1,1,1,1), R_glob = (0,1,1,1,1) und β₄ = 1/256 bleiben unverändert,
  sofern der Autor nichts anderes beschließt.
- **Append-only:** bestehende Runden nie umschreiben. Lange `\texttt`-Dateinamen mit `\allowbreak` umbrechen.

## Einbau
1. **Lokal einfügen:** die Runde unmittelbar vor `\end{document}` in `Quantum_Sphaera_Companion_v4_8_0_source.tex`
   einsetzen und eine Kopie als `llm/v4100_rNN_round.tex` ablegen.
2. **Guard-Linter:** `python3 llm/training/guard_linter.py Quantum_Sphaera_Companion_v4_8_0_source.tex --start <Zeile>`.
   Ziel sind 0 Treffer.
3. **Lokaler Build:** dreimal `pdflatex` (TeX Live 2022) in einem Build-Ordner, in den `figures/` mitkopiert wurde. Danach
   `python3 .claude/skills/quantum-sphaera/tools/qs.py audit`: harte Werte müssen 0 sein; Overfull-Zahl, Seiten und
   Labels notieren.
4. **GitHub-Branch:** `research/v4.10-rNN-<thema>` anlegen. Darin:
   - die Runde wörtlich an `sources/research/parts/v4100-post-release-layers.tex` anhängen (seit v4.10.0-r01 vorhanden,
     eingebunden in `parts/support-route.tex`);
   - die Notizen unter `notes/research/v4_10_0_rNN/` ablegen: `README.md` mit einer Tabelle der Theoremlets,
     `rounds/v4100_rNN_round.tex` und `llm/`;
   - die Vorab-Notizen nach `notes/research/predictions/` legen.
5. **Kandidaten-Build:** `python3 .github/scripts/qsc_latex_build.py --source-dir sources/research --output-dir <ABSOLUTER Pfad>`.
6. **Lokale Historie anbinden:** lokal `git bundle create rNN.bundle <letzter eingebundener Commit>..main` ausführen, auf dem
   GitHub-Branch fetchen und `git merge -s ours` (Dateibaum unverändert).
7. **Wiki im selben PR:** den Ordner `wiki/` anpassen, mindestens Forschungsstand, Forschungslinie, Offene-Probleme,
   Vorhersagen-und-Tests, Inhalt und Content-overview. Das Wiki gibt den Inhalt wieder, nicht nur Links. Mathe mit `|` oder
   `_` in Tabellen als Backtick-Mathe schreiben. Der Workflow „Wiki Sync“ spiegelt nach dem Merge automatisch.
8. **CI:** den Workflow „QSC LaTeX PDF Build“ (`qsc-latex-build.yml`) auf dem Branch starten, mit `build_historical=false`.
   Ist GraphQL gesperrt, über REST:
   `gh api -X POST repos/Moriarty1982/QuantumSphere-Unfold/actions/workflows/266457854/dispatches -f ref=<branch> -f 'inputs[build_historical]=false'`.
   Ohne GitHub-Zugang des Modells startet der Autor den Lauf in der Actions-Oberfläche.
9. **PR:** englischer Titel; im Text Inhalt, Dateien und Prüfzahlen.
10. **Merge nur nach ausdrücklicher Freigabe.** Danach in `AGENTS.md` die Zeile der Runde um „PR #NN gemergt als <sha>“
    ergänzen und die Kernkarte (`llm/Kernkarte_Quantum_Sphaera_v1.md`, Abschnitt 7) nachziehen.

## Fallstricke
- Git-Lock-Dateien in synchronisierten Ordnern (OneDrive) nach Abbrüchen: nur eigene `.lock` entfernen.
- Ausgaben knapp halten: Skripte als Dateien, nur Zusammenfassungen ausgeben.
