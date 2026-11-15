# v4.10.0-r14: Statusvermerke zu Koide-Bezug, gebogenen Achsen und bewachtem Kern

15. November 2026. Teil der Vorbereitung von v5.1.0 (Autorenauftrag: neue Unterversion beider Ausgaben). Die Runde steht
als Datei `rounds/v4100_r14_round.tex` und ist an `sources/research/parts/v4100-post-release-layers.tex` angehängt.
Außer H104 sind alle Einträge Erkundungen ohne Vorab-Notiz und ohne Datenvergleich. Guards unverändert, keine neue H-Nummer.

| Theoremlet | Inhalt | Quelle |
|---|---|---|
| r14.1 | H104 widerlegt: Bei freiem Flächenspektrum trifft ein zweites Zählregel-Paar alle drei Fenster | `../predictions/Ergebnis_H104_Zaehlregel_Flaechenspektren.md` |
| r14.2 | Slot-Fourier F (2T auf dem Dublett, K = 2/3, π/4) und seine Grenzen; Bezugsauswahl durch H = −(aQ + bR) verlangt a = b | `../op3_slot_fourier_2t_2026_11_14.md`, Codex-Notizen zu PR #123 |
| r14.3 | Keine Quelle für a = b: monomiale Symmetrien, 54 MUB-Paare, F-Selbstdualität, r47-Maske (ε* ≈ 0,104 gegen Fit 0,44–0,82), Frame-Lesarten, r33 nicht der Engpass, e8-Rollentausch | `../op3_action_balance_search_2026_11_14/README.md` |
| r14.4 | Abbildung C⊗S → C⊗H⊗O: 20-dimensionale Familie; Familien-su(2) nur am Platz des Lorentz-Spins | `../op3_cs_dixon_map_2026_11_15/README.md` |
| r14.5 | Gebogene Achsen: det G = (√2 cos φ − 1)/2; Oktant als Grenzfall mit Masse null; φ = 2/3 gibt die Leptonverhältnisse | ebenda, Nachtrag |
| r14.6 | Bewachter Kern als flussfreie Kappe: Vorzeichen aus der Lage, genau ein Kern, verdrängter Fluss am Gegenpol (Umkehrwalze), Kugel gegen Faser-Volltorus | `../op3_guarded_core_flux_2026_11_15/README.md` |
| r14.7 | Kerngröße: Zählregel und Horizontliteratur (ABK, ENP) legen γ_M nicht fest; als Frame-Quant fällt sie mit OP1 zusammen | ebenda |
| Berichtigungen | H99 liegt nicht auf dem Oktanten; bei einem Kern entweicht kein Fluss | ebenda |

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 1786`):
  0 Kandidaten in den Zeilen 1786–1954.
- Der Build läuft über den gepaarten Dokumentbau der Version 5 (Workflow „QSC v5 paired document draft“).
