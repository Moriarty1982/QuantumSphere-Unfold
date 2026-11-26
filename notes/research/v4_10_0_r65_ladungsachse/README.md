# v4.10.0-r65: Ladungsachse und Ladungstyp auf dem Sedenionen-Träger (26.11.2026)

Auftrag des Autors vom 26.11.2026: Companion-Runde zu H162 und k361 mit Einschränkung von r59.6, dazu der Satz im Physik-Artikel.
Die Runde rechnet nichts Neues. Sie hält den Test H162 (k360) und die Erkundung k361 fest. Text: `rounds/v4100_r65_round.tex`,
angehängt an `sources/research/parts/v4100-post-release-layers.tex`.

| Eintrag | Inhalt | Test, Skript | Prüfung |
|---|---|---|---|
| r65.1 | Q_u hat für jede Achse u in Im H_n dasselbe Spektrum und dieselben Symmetrien | H162a (bestätigt, nicht blind), k360 | Wolfram exakt, numpy 200 Zufallsachsen |
| r65.2 | Weg A, Familien-su(2) und H125 Stufe A gelten für jede Achse | H162b, c (bestätigt; b nicht blind) | b Wolfram exakt; c nur numerisch |
| r65.3 | e₈: [Q, ψ] = 0. e₇: setzt Q₈ der Kopie 𝕆₀ fort. Keine Achse leistet beides | H162d (bestätigt, nicht blind), H162e (Erkundung) | d exakt |
| r65.4 | Zwei Ladungstypen (L_u, R_u); Orientierungstabelle; gleiche Seite gibt entgegengesetzte, verschiedene Seiten geben gleiche Orientierung | k361 (Erkundung, nicht blind) | nur numerisch (numpy) |

Präzisierungen älterer Runden (ohne sie umzuschreiben): r64.2 („nicht gerechnet“) ist beantwortet. r13.3, r13.4, r14.4, r59.6 stehen
statt „unter CT-003“ unter „Ladung der Form Q^L_u oder Q^R_u und Setzung S-side“. Der Satz in r59.6, das relative Vorzeichen setze kein
Vorzeichen, ist eingeschränkt: Es hängt an **S-side** (dieselbe Seite der Multiplikation trägt die Familie in beiden Sektoren).
Die Setzung heißt S-side, weil (S1) bis (S3) in r17.5 schon vergeben sind.

Unverändert: H125 Stufe B offen (Frist 31.12.2035, jetzt abhängig von S1 und S-side), CT-003 Platzhalter, zwei Generationen statt drei.
Guards: Γ_guard = (1,1,1,1,1), R_glob = (0,1,1,1,1), β₄ = 1/256. OP1–OP5, C5, C6/T2 offen.

Skripte und Ausgaben: `notes/research/hilbert_shift_felder_2026_11_24/ladungsachse_h162/`. Notizen: `notes/research/predictions/`
(Vorab-Notiz und Ergebnis H162).

## Physik-Artikel (Repo-Quelle, Zenodo 1.0.0 unverändert)
- `sections/04-particles.tex`: Weg A (ein Satz zu H162), Abschnitt zum CP-Vorzeichen (Setzung der Seite statt „keine Konvention“).
- `sections/09-open.tex`: OP4-Absatz und Zeile H125 der Tabelle offener Tests.
- `sections/A-ledger.tex`: Zeile zum relativen CP-Vorzeichen.
- Lokal gebaut: 50 Seiten, keine offenen Verweise, keine Overfull-Boxen. `article.pdf` und `release-info.tex` bleiben auf 1.0.0.

## Mitkorrigiert
`wiki/Forschungsstand.md` enthielt seit dem Merge von #332 drei Zeilen mit Git-Konfliktmarken. Sie sind entfernt; der Text beider Seiten
war vollständig vorhanden.
